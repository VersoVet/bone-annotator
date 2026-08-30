"""PostgreSQL queries for learning dashboard, test sets and resets."""

import logging
from typing import Any

import psycopg

from src.modules.storage.task_db import SCHEMA

logger = logging.getLogger(__name__)


class LearningStatsDB:
    """Learning progress and test set operations."""

    def __init__(self, conninfo: str) -> None:
        """Initialize with PostgreSQL connection string."""
        self._conninfo = conninfo
        self._conn: psycopg.Connection | None = None

    def _get_conn(self) -> psycopg.Connection:
        if self._conn is None or self._conn.closed:
            self._conn = psycopg.connect(self._conninfo, autocommit=True)
        return self._conn

    def add_test_set_entries(self, bone_type: str, acquisition_ids: list[str]) -> int:
        """Add acquisitions to the frozen test set."""
        conn = self._get_conn()
        inserted = 0
        for acq_id in acquisition_ids:
            row = conn.execute(
                f"""INSERT INTO {SCHEMA}.test_sets (bone_type, acquisition_id)
                VALUES (%s, %s) ON CONFLICT (bone_type, acquisition_id) DO NOTHING
                RETURNING id""",
                (bone_type, acq_id),
            ).fetchone()
            if row:
                inserted += 1
                conn.execute(
                    f"""UPDATE {SCHEMA}.bonestore_catalog
                    SET in_test_set=TRUE WHERE acquisition_id=%s""",
                    (acq_id,),
                )
        return inserted

    def list_test_set(self, bone_type: str | None = None) -> list[dict[str, Any]]:
        """List frozen test set acquisitions."""
        conn = self._get_conn()
        if bone_type:
            rows = conn.execute(
                f"""SELECT id, bone_type, acquisition_id, added_at
                FROM {SCHEMA}.test_sets WHERE bone_type=%s ORDER BY added_at""",
                (bone_type,),
            ).fetchall()
        else:
            rows = conn.execute(
                f"""SELECT id, bone_type, acquisition_id, added_at
                FROM {SCHEMA}.test_sets ORDER BY bone_type, added_at"""
            ).fetchall()
        return [
            {"id": r[0], "bone_type": r[1], "acquisition_id": r[2], "added_at": r[3].isoformat() if r[3] else None}
            for r in rows
        ]

    def is_in_test_set(self, bone_type: str, acquisition_id: str) -> bool:
        """Check whether an acquisition belongs to the frozen test set."""
        conn = self._get_conn()
        row = conn.execute(
            f"""SELECT 1 FROM {SCHEMA}.test_sets
            WHERE bone_type=%s AND acquisition_id=%s""",
            (bone_type, acquisition_id),
        ).fetchone()
        return row is not None

    def get_tracking_stats(self) -> dict[str, Any]:
        """Aggregate annotation tracking stats for dashboard."""
        conn = self._get_conn()
        task_rows = conn.execute(
            f"""SELECT status, COUNT(*) FROM {SCHEMA}.annotation_tasks GROUP BY status"""
        ).fetchall()
        tier_rows = conn.execute(
            f"""SELECT quality_tier, COUNT(*) FROM {SCHEMA}.frame_annotations
            WHERE source NOT LIKE '%%_superseded' GROUP BY quality_tier"""
        ).fetchall()
        catalog_total = conn.execute(f"SELECT COUNT(*) FROM {SCHEMA}.bonestore_catalog").fetchone()
        test_total = conn.execute(f"SELECT COUNT(*) FROM {SCHEMA}.test_sets").fetchone()
        training_rows = conn.execute(
            f"""SELECT status, COUNT(*) FROM {SCHEMA}.boneseg_training_runs GROUP BY status"""
        ).fetchall()
        return {
            "tasks_by_status": {r[0]: r[1] for r in task_rows},
            "annotations_by_tier": {r[0] or "unknown": r[1] for r in tier_rows},
            "catalog_total": catalog_total[0] if catalog_total else 0,
            "test_set_total": test_total[0] if test_total else 0,
            "training_by_status": {r[0]: r[1] for r in training_rows},
        }

    def get_learning_stats(self, bone_types: list[str] | None = None) -> dict[str, Any]:
        """Learning dashboard stats from PostgreSQL."""
        conn = self._get_conn()
        active_bones = bone_types or ["humerus", "radius", "ulna", "femur", "tibia"]

        tier_rows = conn.execute(
            f"""SELECT quality_tier, COUNT(*) FROM {SCHEMA}.frame_annotations
            WHERE source NOT LIKE '%%_superseded' GROUP BY quality_tier"""
        ).fetchall()
        tiers = {r[0] or "unknown": r[1] for r in tier_rows}

        gold_by_bone: dict[str, int] = {}
        for bone in active_bones:
            row = conn.execute(
                f"""SELECT COUNT(DISTINCT fa.frame_filename || fa.acquisition_id)
                FROM {SCHEMA}.frame_annotations fa
                JOIN {SCHEMA}.acquisitions a ON a.id = fa.acquisition_id
                WHERE fa.quality_tier = 'gold' AND fa.source NOT LIKE '%%_superseded'
                AND a.bone_type = %s""",
                (bone,),
            ).fetchone()
            gold_by_bone[bone] = row[0] if row else 0

        last_ann = conn.execute(
            f"""SELECT a.bone_type, MAX(fa.validated_at) as last_at
            FROM {SCHEMA}.frame_annotations fa
            JOIN {SCHEMA}.acquisitions a ON a.id = fa.acquisition_id
            WHERE fa.validated_at IS NOT NULL AND fa.source NOT LIKE '%%_superseded'
            GROUP BY a.bone_type"""
        ).fetchall()
        last_by_bone = {r[0]: r[1].isoformat() if r[1] else None for r in last_ann}

        week_count = conn.execute(
            f"""SELECT COUNT(*) FROM {SCHEMA}.frame_annotations
            WHERE validated_at >= NOW() - INTERVAL '7 days'
            AND source NOT LIKE '%%_superseded'"""
        ).fetchone()
        prev_week = conn.execute(
            f"""SELECT COUNT(*) FROM {SCHEMA}.frame_annotations
            WHERE validated_at >= NOW() - INTERVAL '14 days'
            AND validated_at < NOW() - INTERVAL '7 days'
            AND source NOT LIKE '%%_superseded'"""
        ).fetchone()
        month_count = conn.execute(
            f"""SELECT COUNT(*) FROM {SCHEMA}.frame_annotations
            WHERE validated_at >= NOW() - INTERVAL '30 days'
            AND source NOT LIKE '%%_superseded'"""
        ).fetchone()

        test_rows = conn.execute(
            f"""SELECT bone_type, COUNT(*), MIN(added_at) FROM {SCHEMA}.test_sets
            GROUP BY bone_type"""
        ).fetchall()
        test_sets = {r[0]: {"count": r[1], "since": r[2].isoformat() if r[2] else None} for r in test_rows}

        training_rows = conn.execute(
            f"""SELECT id, run_name, bone_type, generation, best_dice, test_dice,
                       status, started_at, completed_at, per_class_dice
                FROM {SCHEMA}.boneseg_training_runs
                ORDER BY started_at DESC LIMIT 20"""
        ).fetchall()
        local_training = [
            {
                "id": r[0],
                "run_name": r[1],
                "bone_type": r[2],
                "generation": r[3],
                "best_dice": r[4],
                "test_dice": r[5],
                "status": r[6],
                "started_at": r[7].isoformat() if r[7] else None,
                "completed_at": r[8].isoformat() if r[8] else None,
                "per_class_dice": r[9],
            }
            for r in training_rows
        ]

        total_acq = conn.execute(f"SELECT COUNT(*) FROM {SCHEMA}.acquisitions").fetchone()

        return {
            "tiers": tiers,
            "gold_by_bone": gold_by_bone,
            "last_annotation_by_bone": last_by_bone,
            "velocity": {
                "week": week_count[0] if week_count else 0,
                "prev_week": prev_week[0] if prev_week else 0,
                "month": month_count[0] if month_count else 0,
                "per_day": round((week_count[0] if week_count else 0) / 7, 1),
            },
            "test_sets": test_sets,
            "local_training": local_training,
            "total_acquisitions": total_acq[0] if total_acq else 0,
        }

    def reset_annotation_data(self, *, include_annotations: bool = True) -> dict[str, int]:
        """Clear all annotation tasks and optionally frame annotations."""
        conn = self._get_conn()
        tasks = conn.execute(f"DELETE FROM {SCHEMA}.annotation_tasks").rowcount or 0
        frames = 0
        if include_annotations:
            frames = conn.execute(f"DELETE FROM {SCHEMA}.frame_annotations").rowcount or 0
        conn.execute(f"ALTER SEQUENCE {SCHEMA}.annotation_tasks_id_seq RESTART WITH 1")
        return {"tasks_deleted": tasks, "annotations_deleted": frames}

    def close(self) -> None:
        """Close the connection."""
        if self._conn and not self._conn.closed:
            self._conn.close()


def create_learning_db(host: str, port: int, user: str, password: str, dbname: str, **kwargs: Any) -> LearningStatsDB:
    """Create LearningStatsDB from connection parameters."""
    conninfo = f"host={host} port={port} user={user} password={password} dbname={dbname}"
    return LearningStatsDB(conninfo)
