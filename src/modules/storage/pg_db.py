"""PostgreSQL client for bone annotation storage.

Stores annotations on Synapse PostgreSQL (configurable) in the
bone_annotations schema. Each annotation is linked to a frame of an
acquisition, with type (zone, landmark, measurement, lesion) and
JSONB data.

Security note: F-string SQL uses SCHEMA constant (hardcoded
"bone_annotations"), not user input.
"""

import json
import logging
from typing import Any

import psycopg

from src.modules.storage.pg_utils import compute_quality_tier

logger = logging.getLogger(__name__)

SCHEMA = "bone_annotations"


class AnnotationPgDB:
    """PostgreSQL client for annotations.

    Args:
        host: PostgreSQL server address.
        port: PostgreSQL port.
        user: Database user.
        password: Database password.
        dbname: Database name.
    """

    def __init__(self, host: str, port: int, user: str, password: str, dbname: str) -> None:
        """Initialize PostgreSQL connection parameters."""
        self._conninfo = f"host={host} port={port} user={user} password={password} dbname={dbname}"
        self._conn: psycopg.Connection | None = None

    def _get_conn(self) -> psycopg.Connection:
        """Return a connection, creating if necessary."""
        if self._conn is None or self._conn.closed:
            self._conn = psycopg.connect(self._conninfo, autocommit=True)
        return self._conn

    def ensure_acquisition(
        self,
        acq_id: str,
        category: str,
        bone_type: str,
        side: str,
        region: str,
        frame_count: int = 0,
        has_timecodes: bool = False,
        source_path: str = "",
    ) -> None:
        """Insert or update an acquisition.

        Args:
            acq_id: Unique acquisition identifier.
            category: BoneStore category.
            bone_type: Bone type.
            side: Side (left, right, bilateral).
            region: Region (proximal, distal, entire).
            frame_count: Number of frames.
            has_timecodes: Whether timecodes are available.
            source_path: NFS source path.
        """
        conn = self._get_conn()
        conn.execute(
            """INSERT INTO bone_annotations.acquisitions
            (id, category, bone_type, side, region, frame_count,
             has_timecodes, source_path)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE SET
                bone_type=EXCLUDED.bone_type, side=EXCLUDED.side,
                region=EXCLUDED.region, updated_at=NOW()""",
            (
                acq_id,
                category,
                bone_type,
                side,
                region,
                frame_count,
                has_timecodes,
                source_path,
            ),
        )

    def save_pipeline(
        self,
        acq_id: str,
        pipeline_config: list[dict],
        preset: str = "",
    ) -> None:
        """Save imaging-sdk pipeline for an acquisition.

        Args:
            acq_id: Acquisition ID.
            pipeline_config: List of filters.
            preset: Preset name.
        """
        conn = self._get_conn()
        conn.execute(
            """UPDATE bone_annotations.acquisitions
            SET pipeline_config=%s, pipeline_preset=%s, updated_at=NOW()
            WHERE id=%s""",
            (json.dumps(pipeline_config), preset, acq_id),
        )

    def save_frame_annotations(
        self,
        acq_id: str,
        frame_filename: str,
        annotations: dict[str, Any],
        *,
        task_id: int | None = None,
        author: str = "unknown",
        source: str = "manual",
        confidence: float | None = None,
        model_version: str | None = None,
        validated_by: str | None = None,
    ) -> int:
        """Save annotations for a frame using soft-replace.

        Marks existing rows as superseded, then inserts new ones
        with provenance tracking.

        Args:
            acq_id: Acquisition ID.
            frame_filename: Frame filename (.b2nd).
            annotations: Dict {zones: [...], landmarks: [...], ...}.
            task_id: Annotation task ID (links to annotation_tasks).
            author: Who created these annotations.
            source: Origin ('manual', 'ml', 'import').
            confidence: ML confidence score (None for manual).
            model_version: ML model version (None for manual).
            validated_by: Validator if annotation was reviewed.

        Returns:
            Number of annotations inserted.
        """
        conn = self._get_conn()
        # Soft-replace: mark existing as superseded (scoped by task_id if provided)
        if task_id:
            conn.execute(
                """UPDATE bone_annotations.frame_annotations
                SET source = source || '_superseded'
                WHERE acquisition_id=%s AND frame_filename=%s AND task_id=%s
                AND source NOT LIKE '%%_superseded'""",
                (acq_id, frame_filename, task_id),
            )
        else:
            conn.execute(
                """UPDATE bone_annotations.frame_annotations
                SET source = source || '_superseded'
                WHERE acquisition_id=%s AND frame_filename=%s
                AND source NOT LIKE '%%_superseded'""",
                (acq_id, frame_filename),
            )
        count = 0
        for ann_type in ("zones", "landmarks", "measurements", "lesions"):
            for item in annotations.get(ann_type, []):
                ann_id = item.get("id", f"{ann_type}_{count}")
                label = item.get("label", item.get("name", ""))
                item_conf = item.get("confidence", confidence)
                item_source = item.get("source", source)
                item_model = item.get("model_version", model_version)
                tier = compute_quality_tier(item_source, validated_by)
                conn.execute(
                    """INSERT INTO bone_annotations.frame_annotations
                    (acquisition_id, frame_filename, annotation_type,
                     annotation_id, label, data, author, source,
                     confidence, model_version, task_id, quality_tier)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (
                        acq_id,
                        frame_filename,
                        ann_type.rstrip("s"),
                        ann_id,
                        label,
                        json.dumps(item),
                        author,
                        item_source,
                        item_conf,
                        item_model,
                        task_id,
                        tier,
                    ),
                )
                count += 1
        return count

    def load_frame_annotations(
        self,
        acq_id: str,
        frame_filename: str,
    ) -> dict[str, Any]:
        """Load annotations for a frame.

        Args:
            acq_id: Acquisition ID.
            frame_filename: Frame filename.

        Returns:
            Dict {zones: [...], landmarks: [...], ...}.
        """
        conn = self._get_conn()
        rows = conn.execute(
            """SELECT annotation_type, data FROM bone_annotations.frame_annotations
            WHERE acquisition_id=%s AND frame_filename=%s
            ORDER BY id""",
            (acq_id, frame_filename),
        ).fetchall()
        result: dict[str, list] = {
            "zones": [],
            "landmarks": [],
            "measurements": [],
            "lesions": [],
        }
        for row in rows:
            ann_type = row[0] + "s"  # zone → zones
            if ann_type in result:
                data = row[1] if isinstance(row[1], dict) else json.loads(row[1])
                result[ann_type].append(data)
        return result

    def load_acquisition_annotations(self, acq_id: str) -> dict[str, Any]:
        """Load all annotations for an acquisition.

        Args:
            acq_id: Acquisition ID.

        Returns:
            Dict {frame_filename: {zones, landmarks, ...}, ...} + pipeline.
        """
        conn = self._get_conn()
        # Pipeline
        acq = conn.execute(
            "SELECT pipeline_config, pipeline_preset FROM bone_annotations.acquisitions WHERE id=%s",
            (acq_id,),
        ).fetchone()
        pipeline = acq[0] if isinstance(acq[0], list) else json.loads(acq[0]) if acq and acq[0] else []
        preset = acq[1] if acq else ""

        # Annotations by frame
        rows = conn.execute(
            """SELECT frame_filename, annotation_type, data
            FROM bone_annotations.frame_annotations
            WHERE acquisition_id=%s ORDER BY frame_filename, id""",
            (acq_id,),
        ).fetchall()
        frames: dict[str, Any] = {}
        for row in rows:
            fn = row[0]
            if fn not in frames:
                frames[fn] = {
                    "zones": [],
                    "landmarks": [],
                    "measurements": [],
                    "lesions": [],
                }
            ann_type = row[1] + "s"
            if ann_type in frames[fn]:
                d = row[2] if isinstance(row[2], dict) else json.loads(row[2])
                frames[fn][ann_type].append(d)

        return {
            "acquisition_id": acq_id,
            "frames": frames,
            "pipeline": pipeline,
            "pipeline_preset": preset,
        }

    def get_annotated_acquisitions(self) -> list[str]:
        """Return IDs of acquisitions with annotations.

        Returns:
            List of acquisition IDs.
        """
        conn = self._get_conn()
        rows = conn.execute("SELECT DISTINCT acquisition_id FROM bone_annotations.frame_annotations").fetchall()
        return [r[0] for r in rows]

    def get_stats(self) -> dict[str, Any]:
        """Global annotation statistics.

        Returns:
            Dict with counters by type and bone.
        """
        conn = self._get_conn()
        rows = conn.execute("SELECT * FROM bone_annotations.stats").fetchall()
        cols = [desc[0] for desc in conn.execute("SELECT * FROM bone_annotations.stats LIMIT 0").description]
        stats = [dict(zip(cols, row, strict=False)) for row in rows]
        total = {
            "acquisitions": sum(s.get("acquisitions", 0) for s in stats),
            "annotated_frames": sum(s.get("annotated_frames", 0) for s in stats),
            "total_annotations": sum(s.get("total_annotations", 0) for s in stats),
            "zones": sum(s.get("zones", 0) for s in stats),
            "landmarks": sum(s.get("landmarks", 0) for s in stats),
            "by_bone": stats,
        }
        return total

    def close(self) -> None:
        """Close the connection."""
        if self._conn and not self._conn.closed:
            self._conn.close()
