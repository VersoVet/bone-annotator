"""Image source manager — configurable multi-source access.

Loads source configuration from YAML and provides unified access
to image acquisitions from BoneStore, PACS, or local directories.
"""

import logging
from pathlib import Path
from typing import Any

import yaml

from src.modules.bonestore.service import (
    find_acquisition,
    get_acquisition_frames,
)
from src.modules.bonestore.service import (
    list_acquisitions as bs_list_acquisitions,
)

logger = logging.getLogger(__name__)

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parent.parent.parent.parent / "config" / "sources.yaml"


class SourceConfig:
    """Parsed source configuration from YAML."""

    def __init__(self, config_path: Path | None = None) -> None:
        """Load configuration from YAML file.

        Args:
            config_path: Path to sources.yaml. Uses default if None.
        """
        self.config_path = config_path or DEFAULT_CONFIG_PATH
        self._raw: dict[str, Any] = {}
        self.sources: dict[str, dict[str, Any]] = {}
        self.dataset_pacs: dict[str, Any] = {}
        self.dataset_storage_fallback: str = ""
        self._load()

    def _load(self) -> None:
        """Load and parse YAML config."""
        if not self.config_path.exists():
            logger.warning("Sources config not found: %s", self.config_path)
            return
        with self.config_path.open() as f:
            self._raw = yaml.safe_load(f) or {}
        self.sources = self._raw.get("sources", {})
        self.dataset_pacs = self._raw.get("dataset_pacs", {})
        fb = self._raw.get("dataset_storage_fallback", {})
        self.dataset_storage_fallback = fb.get("root", "") if isinstance(fb, dict) else str(fb)


class SourceService:
    """Unified access to image sources."""

    def __init__(self, config: SourceConfig | None = None) -> None:
        """Initialize source service.

        Args:
            config: Source configuration. Loads default if None.
        """
        self.config = config or SourceConfig()

    def list_sources(self) -> list[dict[str, Any]]:
        """List all configured and enabled sources.

        Returns:
            List of source descriptors.
        """
        result = []
        for name, src in self.config.sources.items():
            if src.get("enabled", True):
                result.append(
                    {
                        "name": name,
                        "type": src.get("type", "unknown"),
                        "root": src.get("root", ""),
                        "description": src.get("description", ""),
                        "enabled": True,
                    }
                )
        return result

    def list_acquisitions(
        self,
        source_name: str,
        bone_type: str | None = None,
        side: str | None = None,
    ) -> list[dict[str, Any]]:
        """List acquisitions from a source with optional filters.

        Args:
            source_name: Source name from config.
            bone_type: Filter by bone type.
            side: Filter by side (left, right).

        Returns:
            List of acquisition dicts.

        Raises:
            ValueError: If source not found or not enabled.
        """
        src = self.config.sources.get(source_name)
        if not src or not src.get("enabled", True):
            msg = f"Source not found or disabled: {source_name}"
            raise ValueError(msg)

        src_type = src.get("type", "nfs")
        if src_type == "nfs":
            acqs = bs_list_acquisitions(src.get("root"))
        else:
            logger.warning("Source type not supported: %s", src_type)
            return []

        if bone_type:
            acqs = [a for a in acqs if a.get("bone_type") == bone_type]
        if side:
            acqs = [a for a in acqs if a.get("side") == side]
        return acqs

    def get_frames(
        self,
        source_name: str,
        acquisition_id: str,
    ) -> list[dict[str, Any]]:
        """Get frame list for an acquisition.

        Args:
            source_name: Source name.
            acquisition_id: Acquisition ID.

        Returns:
            List of frame dicts with index, filename, angle_deg.

        Raises:
            ValueError: If source or acquisition not found.
        """
        src = self.config.sources.get(source_name)
        if not src:
            msg = f"Source not found: {source_name}"
            raise ValueError(msg)

        acq_dir = find_acquisition(src.get("root"), acquisition_id)
        if acq_dir is None:
            msg = f"Acquisition not found: {acquisition_id}"
            raise ValueError(msg)

        return get_acquisition_frames(acq_dir)

    def get_acquisition_path(self, source_name: str, acquisition_id: str) -> Path | None:
        """Get filesystem path for an acquisition.

        Args:
            source_name: Source name.
            acquisition_id: Acquisition ID.

        Returns:
            Path to acquisition directory or None.
        """
        src = self.config.sources.get(source_name)
        if not src:
            return None
        return find_acquisition(src.get("root"), acquisition_id)

    def get_dataset_storage_path(self) -> Path:
        """Get path for storing prepared datasets.

        Returns fallback local path if PACS not configured.

        Returns:
            Path for dataset storage.
        """
        fallback = self.config.dataset_storage_fallback
        if fallback:
            path = Path(fallback)
            path.mkdir(parents=True, exist_ok=True)
            return path
        return Path("data/annotation-datasets")

    def get_dataset_pacs_config(self) -> dict[str, Any]:
        """Get PACS configuration for dataset storage.

        Returns:
            Dict with host, port, name or empty if not configured.
        """
        return self.config.dataset_pacs


# Module singleton
_service: SourceService | None = None


def get_service() -> SourceService:
    """Get or create the source service singleton."""
    global _service
    if _service is None:
        _service = SourceService()
    return _service
