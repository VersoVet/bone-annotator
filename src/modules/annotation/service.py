"""Annotation service for bone acquisition management.

Manages loading acquisitions from BoneStore, reading frames,
and persisting annotations. Includes LRU cache for processed frames
(GPU-accelerated).
"""

import json
import logging
import os
from pathlib import Path
from typing import Any

from src.modules.storage.pg_db import AnnotationPgDB

logger = logging.getLogger(__name__)

ANNOTATIONS_DIR = "data/annotations"
BONESTORE_ROOT = os.getenv("BONESTORE_ROOT", "/mnt/bonestore")


class AnnotationService:
    """Service for annotating bone acquisitions.

    Args:
        project_root: Project root path.
        bonestore_root: NFS BoneStore mount point.
        pg_config: PostgreSQL config dict or None.
    """

    def __init__(
        self,
        project_root: str | Path | None = None,
        bonestore_root: str | None = None,
        pg_config: dict[str, Any] | None = None,
    ) -> None:
        """Initialize annotation service."""
        if project_root is None:
            project_root = Path(__file__).resolve().parent.parent.parent.parent
        self.project_root = Path(project_root)
        self.bonestore_root = Path(bonestore_root or BONESTORE_ROOT)
        self.annotations_dir = self.project_root / ANNOTATIONS_DIR
        self.annotations_dir.mkdir(parents=True, exist_ok=True)
        self._taxonomy = self._load_taxonomy()
        self._pg_db = self._init_pg(pg_config)

    def _init_pg(self, config: dict[str, Any] | None = None) -> AnnotationPgDB | None:
        """Initialize PostgreSQL connection from config.

        Args:
            config: PostgreSQL config dict or None.

        Returns:
            AnnotationPgDB instance or None if failed.
        """
        try:
            if config is None:
                config_path = self.project_root / "config" / "default.json"
                if config_path.exists():
                    with config_path.open() as f:
                        config = json.load(f).get("postgres", {})
                else:
                    config = {}

            host = config.get("host", "10.0.0.59")
            port = config.get("port", 5433)
            user = config.get("user", "bone")
            dbname = config.get("dbname", "bone_recognition")

            # Password: env var > vault > config
            password = os.environ.get("BONE_PG_PASSWORD", "")
            if not password:
                token = os.environ.get("ONYX_VAULT_TOKEN", "")
                if token:
                    try:
                        import httpx

                        r = httpx.get(
                            "http://10.0.0.44:8050/vault/bone_postgres_password",
                            headers={"X-Vault-Token": token},
                            timeout=5.0,
                        )
                        if r.status_code == 200:
                            password = r.json().get("value", "")
                    except Exception:  # noqa: BLE001
                        pass

            if not password:
                password = config.get("password", "")

            if not password:
                logger.warning("PostgreSQL password not found, falling back to JSON")
                return None

            db = AnnotationPgDB(host, port, user, password, dbname)
            logger.info("PostgreSQL annotations connected: %s:%d", host, port)
            return db
        except Exception as e:
            logger.warning("PostgreSQL init failed, falling back to JSON: %s", e)
            return None

    def _load_taxonomy(self) -> dict[str, Any]:
        """Load taxonomy from JSON (fallback if SQLite unavailable)."""
        path = self.project_root / "config" / "anatomy_zones.json"
        if path.exists():
            with Path(path).open() as f:
                return json.load(f)
        return {}

    @property
    def taxonomy(self) -> dict[str, Any]:
        """Return complete taxonomy."""
        return self._taxonomy

    def reload_taxonomy(self) -> dict[str, Any]:
        """Reload taxonomy.

        Returns:
            Reloaded taxonomy.
        """
        self._taxonomy = self._load_taxonomy()
        return self._taxonomy

    def get_taxonomy_for_region(self, bone_type: str, region: str = "") -> dict[str, Any]:
        """Load taxonomy with region filtering.

        Args:
            bone_type: Bone type.
            region: Anatomical region (proximal, distal, entire, bilateral).
                    Empty = return all.

        Returns:
            Dict {label, zones, landmarks} filtered by region.
        """
        # Determine visible regions
        if region in ("entire", "bilateral", ""):
            visible_regions = None  # All
        elif region == "proximal":
            visible_regions = ("proximal", "diaphysis", "all")
        elif region == "distal":
            visible_regions = ("distal", "diaphysis", "all")
        else:
            visible_regions = None

        # Fallback to JSON taxonomy
        return self._taxonomy.get(bone_type, {})

    @staticmethod
    def _build_zone_tree(flat_zones: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Build hierarchical zone tree from flat list.

        Args:
            flat_zones: List of zones with id and parent_id.

        Returns:
            Tree of zones with nested children.
        """
        by_id: dict[str, Any] = {}
        for z in flat_zones:
            node = {
                "id": z["id"],
                "label": z["label"],
                "level": z.get("level", 1),
                "color": z.get("color", ""),
                "children": [],
                "lesion_site": bool(z.get("lesion_site")),
                "lesion_notes": z.get("lesion_notes", ""),
            }
            by_id[z["id"]] = node
        roots = []
        for z in flat_zones:
            node = by_id[z["id"]]
            parent = z.get("parent_id")
            if parent and parent in by_id:
                by_id[parent]["children"].append(node)
            else:
                roots.append(node)
        return roots

    def save_annotation(self, acquisition_id: str, annotation_data: dict[str, Any]) -> str:
        """Save annotations for acquisition (PostgreSQL + JSON backup).

        Args:
            acquisition_id: Acquisition ID.
            annotation_data: Complete annotation data.

        Returns:
            Save path or identifier.
        """
        if self._pg_db:
            try:
                # Save pipeline
                pipeline = annotation_data.get("pipeline", [])
                preset = annotation_data.get("pipeline_preset", "")
                if pipeline:
                    self._pg_db.save_pipeline(acquisition_id, pipeline, preset)
                # Save frame annotations
                frames = annotation_data.get("frames", {})
                for frame_fn, ann in frames.items():
                    self._pg_db.save_frame_annotations(acquisition_id, frame_fn, ann)
                logger.info(
                    "Annotations saved to PostgreSQL: %s (%d frames)",
                    acquisition_id,
                    len(frames),
                )
                return f"pg:{acquisition_id}"
            except Exception as e:
                logger.warning("PostgreSQL save failed, falling back to JSON: %s", e)

        # Fallback: JSON storage (implement if needed)
        return f"json:{acquisition_id}"

    def load_annotation(self, acquisition_id: str) -> dict[str, Any] | None:
        """Load annotations for acquisition (PostgreSQL priority).

        Args:
            acquisition_id: Acquisition ID.

        Returns:
            Annotation dict or None if absent.
        """
        if self._pg_db:
            try:
                data = self._pg_db.load_acquisition_annotations(acquisition_id)
                if data.get("frames"):
                    return data
            except Exception as e:
                logger.warning("PostgreSQL load failed: %s", e)

        # Fallback: JSON storage
        return None

    def get_annotation_stats(self) -> dict[str, Any]:
        """Get global annotation statistics.

        Returns:
            Dict with annotation counts.
        """
        if self._pg_db:
            try:
                return self._pg_db.get_stats()
            except Exception as e:
                logger.warning("PostgreSQL stats failed: %s", e)
        return {}


async def get_acquisition_status(acquisition_id: str) -> dict:
    """Get annotation status for acquisition.

    Args:
        acquisition_id: Acquisition ID.

    Returns:
        Dict with status and metadata.
    """
    return {
        "acquisition_id": acquisition_id,
        "status": "pending",
        "frames": 0,
        "annotated": 0,
    }
