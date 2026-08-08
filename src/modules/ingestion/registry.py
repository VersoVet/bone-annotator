"""SQLite ingestion registry for acquisition tracking.

Tracks each acquisition from BoneStore: status, processed frames,
extracted metadata. Enables incremental ingestion (never reprocesses
completed acquisitions).
"""

import json
import logging
import sqlite3
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path
from typing import Any

from src.modules.ingestion.registry_utils import (
    load_acquisition_metadata,
)

logger = logging.getLogger(__name__)

DB_NAME = "ingestion_registry.db"


class IngestionStatus(StrEnum):
    """Acquisition status in pipeline."""

    DISCOVERED = "discovered"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class IngestionRegistry:
    """SQLite registry for acquisition tracking.

    Stored in skill data/ directory. Each acquisition identified
    by its relative path on BoneStore.

    Args:
        db_path: Path to SQLite file. If None, uses skill data/.
    """

    def __init__(self, db_path: str | Path | None = None) -> None:
        """Initialize ingestion registry."""
        if db_path is None:
            project_root = Path(__file__).resolve().parent.parent.parent.parent
            db_path = project_root / "data" / DB_NAME
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self) -> None:
        """Create tables if they don't exist."""
        with self._connect() as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS acquisitions (
                    acquisition_id TEXT PRIMARY KEY,
                    bone_type TEXT NOT NULL,
                    side TEXT NOT NULL,
                    region TEXT NOT NULL,
                    session_id TEXT,
                    source_path TEXT NOT NULL,
                    total_frames INTEGER DEFAULT 0,
                    processed_frames INTEGER DEFAULT 0,
                    selected_frames INTEGER DEFAULT 0,
                    status TEXT DEFAULT 'discovered',
                    error_message TEXT,
                    metadata_json TEXT,
                    discovered_at TEXT NOT NULL,
                    started_at TEXT,
                    completed_at TEXT,
                    training_run_id TEXT
                );

                CREATE TABLE IF NOT EXISTS processed_frames (
                    frame_id TEXT PRIMARY KEY,
                    acquisition_id TEXT NOT NULL,
                    frame_index INTEGER NOT NULL,
                    angle_deg REAL,
                    output_path TEXT,
                    image_hash TEXT,
                    processed_at TEXT NOT NULL,
                    FOREIGN KEY (acquisition_id)
                        REFERENCES acquisitions(acquisition_id)
                );

                CREATE INDEX IF NOT EXISTS idx_acq_status
                    ON acquisitions(status);
                CREATE INDEX IF NOT EXISTS idx_acq_bone
                    ON acquisitions(bone_type, side, region);
                CREATE INDEX IF NOT EXISTS idx_frames_acq
                    ON processed_frames(acquisition_id);
            """)

    def _connect(self) -> sqlite3.Connection:
        """Open SQLite connection with row_factory."""
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        return conn

    def discover_acquisitions(self, bonestore_root: str | Path) -> int:
        """Scan BoneStore and register new acquisitions.

        Args:
            bonestore_root: NFS mount path (e.g., /mnt/bonestore).

        Returns:
            Number of new acquisitions discovered.
        """
        root = Path(bonestore_root)
        new_count = 0
        now = datetime.now(UTC).isoformat()

        with self._connect() as conn:
            for category_dir in sorted(root.iterdir()):
                if not category_dir.is_dir():
                    continue

                # Parse category (e.g., "humerus_left_proximal")
                parts = category_dir.name.split("_")
                if len(parts) < 3:
                    logger.warning("Unrecognized category: %s", category_dir.name)
                    continue

                bone_type = parts[0]
                side = parts[1]
                region = parts[2]

                for acq_dir in sorted(category_dir.iterdir()):
                    if not acq_dir.is_dir():
                        continue

                    acq_id = acq_dir.name
                    existing = conn.execute(
                        "SELECT 1 FROM acquisitions WHERE acquisition_id = ?",
                        (acq_id,),
                    ).fetchone()
                    if existing:
                        continue

                    raw_dir = acq_dir / "raw"
                    frame_count = len(list(raw_dir.glob("*.b2nd"))) if raw_dir.exists() else 0

                    metadata = load_acquisition_metadata(acq_dir)

                    conn.execute(
                        """INSERT INTO acquisitions
                        (acquisition_id, bone_type, side, region, session_id,
                         source_path, total_frames, status, metadata_json,
                         discovered_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (
                            acq_id,
                            bone_type,
                            side,
                            region,
                            metadata.get("session_id"),
                            str(acq_dir),
                            frame_count,
                            IngestionStatus.DISCOVERED,
                            json.dumps(metadata, default=str),
                            now,
                        ),
                    )
                    new_count += 1

        logger.info("Discovered %d new acquisitions", new_count)
        return new_count

    def mark_started(self, acquisition_id: str) -> None:
        """Mark acquisition as in-progress."""
        now = datetime.now(UTC).isoformat()
        with self._connect() as conn:
            conn.execute(
                """UPDATE acquisitions
                SET status = ?, started_at = ?
                WHERE acquisition_id = ?""",
                (IngestionStatus.IN_PROGRESS, now, acquisition_id),
            )

    def mark_completed(self, acquisition_id: str, processed: int, selected: int) -> None:
        """Mark acquisition as completed.

        Args:
            acquisition_id: Acquisition ID.
            processed: Total frames processed.
            selected: Frames retained for training.
        """
        now = datetime.now(UTC).isoformat()
        with self._connect() as conn:
            conn.execute(
                """UPDATE acquisitions
                SET status = ?, completed_at = ?,
                    processed_frames = ?, selected_frames = ?
                WHERE acquisition_id = ?""",
                (IngestionStatus.COMPLETED, now, processed, selected, acquisition_id),
            )

    def mark_failed(self, acquisition_id: str, error: str) -> None:
        """Mark acquisition as failed."""
        now = datetime.now(UTC).isoformat()
        with self._connect() as conn:
            conn.execute(
                """UPDATE acquisitions
                SET status = ?, completed_at = ?, error_message = ?
                WHERE acquisition_id = ?""",
                (IngestionStatus.FAILED, now, error, acquisition_id),
            )

    def register_frame(
        self,
        acquisition_id: str,
        frame_index: int,
        angle_deg: float | None,
        output_path: str,
        image_hash: str,
    ) -> None:
        """Register a processed frame.

        Args:
            acquisition_id: Acquisition ID.
            frame_index: Frame index.
            angle_deg: Rotation angle in degrees.
            output_path: Path to saved .npy.
            image_hash: Image hash for deduplication.
        """
        now = datetime.now(UTC).isoformat()
        frame_id = f"{acquisition_id}_{frame_index}"
        with self._connect() as conn:
            conn.execute(
                """INSERT OR REPLACE INTO processed_frames
                (frame_id, acquisition_id, frame_index, angle_deg,
                 output_path, image_hash, processed_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (frame_id, acquisition_id, frame_index, angle_deg, output_path, image_hash, now),
            )

    def get_pending(self, limit: int = 0) -> list[dict[str, Any]]:
        """Get acquisitions pending processing.

        Args:
            limit: Max acquisitions to return (0 = all).

        Returns:
            List of acquisition dicts.
        """
        with self._connect() as conn:
            query = """SELECT * FROM acquisitions
                       WHERE status IN (?, ?)
                       ORDER BY discovered_at"""
            params = [IngestionStatus.DISCOVERED, IngestionStatus.FAILED]

            if limit > 0:
                query += " LIMIT ?"
                params.append(limit)

            rows = conn.execute(query, params).fetchall()
            return [dict(row) for row in rows]

    def get_stats(self) -> dict[str, Any]:
        """Get ingestion statistics.

        Returns:
            Dict with counters by status.
        """
        with self._connect() as conn:
            stats = {}
            for status in IngestionStatus:
                count = conn.execute(
                    "SELECT COUNT(*) as c FROM acquisitions WHERE status = ?",
                    (status,),
                ).fetchone()
                stats[status.value] = count["c"] if count else 0

            total_frames = conn.execute(
                "SELECT SUM(selected_frames) as c FROM acquisitions WHERE status = ?",
                (IngestionStatus.COMPLETED,),
            ).fetchone()

            return {
                "by_status": stats,
                "total_selected_frames": total_frames["c"] if total_frames else 0,
            }
