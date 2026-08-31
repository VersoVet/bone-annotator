"""PostgreSQL client for annotation task management.

Manages the annotation_tasks table and author/validation columns
on frame_annotations. Runs migrations on startup.
"""

import json
import logging
from typing import Any

import psycopg

logger = logging.getLogger(__name__)

SCHEMA = "bone_annotations"

ACTIVE_TASK_STATUSES = ("preparing", "uploading", "created", "annotating", "reviewing")

_MIGRATIONS = [
    # Add author/validation columns to frame_annotations
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS author VARCHAR(100) DEFAULT 'unknown'""",
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS source VARCHAR(20) DEFAULT 'manual'""",
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS confidence FLOAT""",
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS validated_by VARCHAR(100)""",
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS validated_at TIMESTAMPTZ""",
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS created_at TIMESTAMPTZ DEFAULT NOW()""",
    # model_version on frame_annotations
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS model_version VARCHAR(200)""",
    # Create annotation_tasks table
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.annotation_tasks (
        id SERIAL PRIMARY KEY,
        acquisition_id VARCHAR(100) NOT NULL,
        cvat_task_id INTEGER,
        source_name VARCHAR(50) DEFAULT 'bonestore',
        bone_type VARCHAR(50) NOT NULL,
        region VARCHAR(50) DEFAULT 'entire',
        status VARCHAR(20) DEFAULT 'created',
        assignee VARCHAR(100),
        author VARCHAR(100) NOT NULL DEFAULT 'system',
        has_pre_annotations BOOLEAN DEFAULT FALSE,
        frame_count INTEGER DEFAULT 0,
        annotated_frames INTEGER DEFAULT 0,
        cvat_url VARCHAR(500),
        dataset_path VARCHAR(500),
        pipeline_preset VARCHAR(100),
        pipeline_config JSONB,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        validated_at TIMESTAMPTZ,
        validated_by VARCHAR(100),
        notes TEXT
    )""",
    # parent_task_id for re-annotation chains
    f"""ALTER TABLE {SCHEMA}.annotation_tasks
        ADD COLUMN IF NOT EXISTS parent_task_id INTEGER""",
    # Multi-objective annotation profiles
    f"""ALTER TABLE {SCHEMA}.annotation_tasks
        ADD COLUMN IF NOT EXISTS profile_id VARCHAR(50)""",
    f"""ALTER TABLE {SCHEMA}.annotation_tasks
        ADD COLUMN IF NOT EXISTS objective VARCHAR(50)""",
    f"""ALTER TABLE {SCHEMA}.annotation_tasks
        ADD COLUMN IF NOT EXISTS labels_filter JSONB""",
    f"""ALTER TABLE {SCHEMA}.annotation_tasks
        ADD COLUMN IF NOT EXISTS crop_from_task_id INTEGER""",
    f"""ALTER TABLE {SCHEMA}.annotation_tasks
        ADD COLUMN IF NOT EXISTS crop_params JSONB""",
    # training_runs table for active learning
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.training_runs (
        id SERIAL PRIMARY KEY,
        run_name VARCHAR(200) NOT NULL UNIQUE,
        generation INTEGER NOT NULL DEFAULT 1,
        parent_run_id INTEGER,
        model_base VARCHAR(500) NOT NULL,
        model_output_path VARCHAR(500),
        dataset_path VARCHAR(500) NOT NULL,
        dataset_hash VARCHAR(64),
        label_map JSONB NOT NULL,
        bone_type VARCHAR(50) NOT NULL,
        epochs INTEGER NOT NULL,
        imgsz INTEGER NOT NULL DEFAULT 1408,
        batch_size INTEGER NOT NULL DEFAULT 4,
        map50 FLOAT, map50_95 FLOAT,
        precision_score FLOAT, recall_score FLOAT,
        total_images INTEGER,
        status VARCHAR(20) DEFAULT 'pending',
        started_at TIMESTAMPTZ, completed_at TIMESTAMPTZ,
        created_at TIMESTAMPTZ DEFAULT NOW()
    )""",
    # --- Multi-pipeline traceability migrations ---
    # Link frame_annotations to the task that produced them
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS task_id INTEGER""",
    # Link training_runs to the tasks used for training
    f"""ALTER TABLE {SCHEMA}.training_runs
        ADD COLUMN IF NOT EXISTS task_ids INTEGER[]""",
    f"""ALTER TABLE {SCHEMA}.training_runs
        ADD COLUMN IF NOT EXISTS pipeline_preset VARCHAR(100)""",
    # CVAT projects cache (bone_type → project_id)
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.cvat_projects (
        bone_type TEXT PRIMARY KEY,
        cvat_project_id INTEGER NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW()
    )""",
    # --- BoneSeg integration ---
    f"""ALTER TABLE {SCHEMA}.frame_annotations
        ADD COLUMN IF NOT EXISTS quality_tier VARCHAR(10) DEFAULT 'silver'""",
    f"""UPDATE {SCHEMA}.frame_annotations
        SET quality_tier = 'gold'
        WHERE source = 'manual' AND validated_by IS NOT NULL""",
    f"""UPDATE {SCHEMA}.frame_annotations
        SET quality_tier = 'silver'
        WHERE source = 'corrected_ml' AND validated_by IS NOT NULL""",
    f"""UPDATE {SCHEMA}.frame_annotations
        SET quality_tier = 'pseudo'
        WHERE source = 'ml' AND validated_by IS NULL""",
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.test_sets (
        id SERIAL PRIMARY KEY,
        bone_type VARCHAR(50) NOT NULL,
        acquisition_id VARCHAR(100) NOT NULL,
        added_at TIMESTAMP DEFAULT NOW(),
        UNIQUE(bone_type, acquisition_id)
    )""",
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.bonestore_catalog (
        id SERIAL PRIMARY KEY,
        acquisition_id VARCHAR(100) NOT NULL UNIQUE,
        bone_type VARCHAR(50),
        category VARCHAR(100),
        frame_count INT DEFAULT 0,
        source_path VARCHAR(500),
        first_seen TIMESTAMP DEFAULT NOW(),
        ml_status VARCHAR(20) DEFAULT 'new',
        uncertainty_score FLOAT,
        uncertainty_model VARCHAR(200),
        scored_at TIMESTAMP,
        annotation_tier VARCHAR(10),
        in_test_set BOOLEAN DEFAULT FALSE,
        last_trained_gen INT,
        notes VARCHAR(500)
    )""",
    f"""CREATE INDEX IF NOT EXISTS idx_catalog_status
        ON {SCHEMA}.bonestore_catalog(ml_status)""",
    f"""CREATE INDEX IF NOT EXISTS idx_catalog_bone
        ON {SCHEMA}.bonestore_catalog(bone_type)""",
    f"""CREATE INDEX IF NOT EXISTS idx_catalog_score
        ON {SCHEMA}.bonestore_catalog(uncertainty_score DESC)""",
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.boneseg_training_runs (
        id SERIAL PRIMARY KEY,
        run_name VARCHAR(200) NOT NULL,
        bone_type VARCHAR(50) NOT NULL,
        generation INT DEFAULT 1,
        parent_run_id INT REFERENCES {SCHEMA}.boneseg_training_runs(id),
        model_backend VARCHAR(50) DEFAULT 'smp_unet',
        bone_classes JSONB NOT NULL,
        tiers_used JSONB NOT NULL,
        train_count INT, val_count INT, test_count INT,
        epochs INT, best_dice FLOAT,
        per_class_dice JSONB,
        test_dice FLOAT,
        model_output_path VARCHAR(500),
        status VARCHAR(20) DEFAULT 'running',
        started_at TIMESTAMP DEFAULT NOW(),
        completed_at TIMESTAMP
    )""",
    f"""CREATE TABLE IF NOT EXISTS {SCHEMA}.learning_decisions (
        id SERIAL PRIMARY KEY,
        decided_at TIMESTAMPTZ DEFAULT NOW(),
        action VARCHAR(50) NOT NULL,
        bone_type VARCHAR(50),
        generation INT,
        gold_count INT,
        silver_count INT,
        trigger_source VARCHAR(50) DEFAULT 'system',
        payload JSONB,
        notes TEXT
    )""",
    f"""CREATE INDEX IF NOT EXISTS idx_learning_decisions_at
        ON {SCHEMA}.learning_decisions(decided_at DESC)""",
]


class AnnotationTaskDB:
    """PostgreSQL client for annotation tasks.

    Args:
        conninfo: psycopg connection string.
    """

    def __init__(self, conninfo: str) -> None:
        """Initialize with connection string."""
        self._conninfo = conninfo
        self._conn: psycopg.Connection | None = None

    def _get_conn(self) -> psycopg.Connection:
        """Return a connection, creating if necessary."""
        if self._conn is None or self._conn.closed:
            self._conn = psycopg.connect(self._conninfo, autocommit=True)
        return self._conn

    def run_migrations(self) -> None:
        """Run schema migrations (idempotent)."""
        conn = self._get_conn()
        for sql in _MIGRATIONS:
            try:
                conn.execute(sql)
            except Exception as e:
                logger.warning("Migration statement skipped: %s", str(e)[:100])
        logger.info("Annotation task migrations completed")

    def save_task(
        self,
        acquisition_id: str,
        bone_type: str,
        author: str,
        *,
        cvat_task_id: int | None = None,
        source_name: str = "bonestore",
        region: str = "entire",
        status: str = "created",
        assignee: str | None = None,
        frame_count: int = 0,
        dataset_path: str | None = None,
        pipeline_preset: str | None = None,
        pipeline_config: list[dict[str, Any]] | None = None,
        has_pre_annotations: bool = False,
        cvat_url: str | None = None,
        profile_id: str | None = None,
        objective: str | None = None,
        labels_filter: list[str] | None = None,
        crop_from_task_id: int | None = None,
    ) -> int:
        """Insert a new annotation task.

        Returns:
            Created task ID.
        """
        conn = self._get_conn()
        row = conn.execute(
            f"""INSERT INTO {SCHEMA}.annotation_tasks
            (acquisition_id, bone_type, author, cvat_task_id, source_name,
             region, status, assignee, frame_count, dataset_path, pipeline_preset,
             pipeline_config, has_pre_annotations, cvat_url,
             profile_id, objective, labels_filter, crop_from_task_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s)
            RETURNING id""",
            (
                acquisition_id,
                bone_type,
                author,
                cvat_task_id,
                source_name,
                region,
                status,
                assignee,
                frame_count,
                dataset_path,
                pipeline_preset,
                json.dumps(pipeline_config) if pipeline_config else None,
                has_pre_annotations,
                cvat_url,
                profile_id,
                objective,
                json.dumps(labels_filter) if labels_filter else None,
                crop_from_task_id,
            ),
        ).fetchone()
        return row[0] if row else 0

    def update_task(self, task_id: int, **kwargs: Any) -> None:
        """Update task fields.

        Args:
            task_id: Task ID.
            **kwargs: Fields to update (status, assignee, cvat_task_id, etc.).
        """
        allowed = {
            "status",
            "assignee",
            "cvat_task_id",
            "cvat_url",
            "has_pre_annotations",
            "annotated_frames",
            "validated_by",
            "validated_at",
            "notes",
            "frame_count",
            "dataset_path",
            "pipeline_config",
            "parent_task_id",
            "profile_id",
            "objective",
            "labels_filter",
            "crop_from_task_id",
            "crop_params",
        }
        updates = {k: v for k, v in kwargs.items() if k in allowed}
        if not updates:
            return
        conn = self._get_conn()
        set_clauses = ", ".join(f"{k}=%s" for k in updates)
        json_fields = {"pipeline_config", "labels_filter", "crop_params"}
        values = [
            json.dumps(value) if key in json_fields and value is not None else value for key, value in updates.items()
        ] + [task_id]
        conn.execute(
            f"UPDATE {SCHEMA}.annotation_tasks SET {set_clauses}, updated_at=NOW() WHERE id=%s",
            values,
        )

    def get_task(self, task_id: int) -> dict[str, Any] | None:
        """Get a single task by ID.

        Args:
            task_id: Task ID.

        Returns:
            Task dict or None.
        """
        conn = self._get_conn()
        row = conn.execute(f"SELECT * FROM {SCHEMA}.annotation_tasks WHERE id=%s", (task_id,)).fetchone()
        if not row:
            return None
        cols = [d[0] for d in conn.execute(f"SELECT * FROM {SCHEMA}.annotation_tasks LIMIT 0").description]
        return dict(zip(cols, row, strict=False))

    def delete_task(self, task_id: int) -> bool:
        """Delete a task from the database.

        Args:
            task_id: Task ID.

        Returns:
            True if deleted.
        """
        conn = self._get_conn()
        conn.execute(f"DELETE FROM {SCHEMA}.annotation_tasks WHERE id=%s", (task_id,))
        return True

    def list_tasks(
        self,
        limit: int = 50,
        offset: int = 0,
        status: str | None = None,
        bone_type: str | None = None,
        profile_id: str | None = None,
    ) -> tuple[list[dict[str, Any]], int]:
        """List annotation tasks with filters.

        Args:
            limit: Max results.
            offset: Pagination offset.
            status: Filter by status.
            bone_type: Filter by bone type.
            profile_id: Filter by annotation profile.

        Returns:
            Tuple of (task list, total count).
        """
        conn = self._get_conn()
        where_parts: list[str] = []
        params: list[Any] = []
        if status:
            where_parts.append("status=%s")
            params.append(status)
        if bone_type:
            where_parts.append("bone_type=%s")
            params.append(bone_type)
        if profile_id:
            where_parts.append("profile_id=%s")
            params.append(profile_id)
        where = ("WHERE " + " AND ".join(where_parts)) if where_parts else ""

        total = conn.execute(f"SELECT COUNT(*) FROM {SCHEMA}.annotation_tasks {where}", params).fetchone()[0]

        rows = conn.execute(
            f"SELECT * FROM {SCHEMA}.annotation_tasks {where} ORDER BY created_at DESC LIMIT %s OFFSET %s",
            [*params, limit, offset],
        ).fetchall()
        cols = [d[0] for d in conn.execute(f"SELECT * FROM {SCHEMA}.annotation_tasks LIMIT 0").description]
        tasks = [dict(zip(cols, row, strict=False)) for row in rows]
        return tasks, total

    def find_active_task(
        self,
        acquisition_id: str,
        bone_type: str,
        profile_id: str | None = None,
    ) -> dict[str, Any] | None:
        """Find an active annotation task for acquisition+bone_type+profile.

        Active statuses block duplicate task creation. Terminal statuses
        (validated, rejected, failed) allow re-creation.

        Args:
            acquisition_id: Acquisition identifier.
            bone_type: Bone type partition.
            profile_id: Annotation profile (None = legacy tasks without profile).

        Returns:
            Task row dict or None if no active task exists.
        """
        conn = self._get_conn()
        placeholders = ", ".join(["%s"] * len(ACTIVE_TASK_STATUSES))
        if profile_id:
            row = conn.execute(
                f"""SELECT id, status, cvat_task_id, acquisition_id, bone_type, profile_id
                    FROM {SCHEMA}.annotation_tasks
                    WHERE acquisition_id=%s AND bone_type=%s AND profile_id=%s
                    AND status IN ({placeholders})
                    ORDER BY id DESC LIMIT 1""",
                (acquisition_id, bone_type, profile_id, *ACTIVE_TASK_STATUSES),
            ).fetchone()
        else:
            row = conn.execute(
                f"""SELECT id, status, cvat_task_id, acquisition_id, bone_type, profile_id
                    FROM {SCHEMA}.annotation_tasks
                    WHERE acquisition_id=%s AND bone_type=%s
                    AND profile_id IS NULL
                    AND status IN ({placeholders})
                    ORDER BY id DESC LIMIT 1""",
                (acquisition_id, bone_type, *ACTIVE_TASK_STATUSES),
            ).fetchone()
        if not row:
            return None
        return {
            "id": row[0],
            "status": row[1],
            "cvat_task_id": row[2],
            "acquisition_id": row[3],
            "bone_type": row[4],
            "profile_id": row[5] if len(row) > 5 else None,
        }

    def validate_task(self, task_id: int, validated_by: str, decision: str) -> None:
        """Validate or reject a task and its annotations.

        Args:
            task_id: Task ID.
            validated_by: Validator identifier.
            decision: 'validated' or 'rejected'.
        """
        conn = self._get_conn()
        conn.execute(
            f"""UPDATE {SCHEMA}.annotation_tasks
            SET status=%s, validated_by=%s, validated_at=NOW(), updated_at=NOW()
            WHERE id=%s""",
            (decision, validated_by, task_id),
        )
        if decision == "validated":
            task = self.get_task(task_id)
            if task:
                conn.execute(
                    f"""UPDATE {SCHEMA}.frame_annotations
                    SET validated_by=%s, validated_at=NOW(),
                        quality_tier = CASE
                            WHEN source = 'manual' THEN 'gold'
                            WHEN source IN ('corrected_ml', 'import') THEN 'silver'
                            ELSE quality_tier
                        END
                    WHERE acquisition_id=%s AND task_id=%s AND validated_by IS NULL""",
                    (validated_by, task["acquisition_id"], task_id),
                )

    def recover_orphaned_tasks(self) -> int:
        """Mark stuck preparing/uploading tasks as failed on startup.

        Tasks in 'preparing' or 'uploading' status have no running
        background coroutine after a service restart, so they must be
        marked as failed to unblock the acquisition for a new task.

        Returns:
            Number of recovered (failed) tasks.
        """
        conn = self._get_conn()
        result = conn.execute(
            f"""UPDATE {SCHEMA}.annotation_tasks
            SET status='failed', notes='Orphaned after service restart', updated_at=NOW()
            WHERE status IN ('preparing', 'uploading')
            RETURNING id""",
        )
        rows = result.fetchall()
        count = len(rows)
        if count:
            ids = [r[0] for r in rows]
            logger.warning("Recovered %d orphaned tasks: %s", count, ids)
        return count

    def save_project_mapping(self, bone_type: str, project_id: int) -> None:
        """Cache bone_type → CVAT project_id in PostgreSQL."""
        try:
            self._get_conn().execute(
                f"""INSERT INTO {SCHEMA}.cvat_projects (bone_type, cvat_project_id)
                VALUES (%s, %s) ON CONFLICT (bone_type) DO UPDATE SET cvat_project_id = %s""",
                (bone_type, project_id, project_id),
            )
        except Exception as e:
            logger.warning("Failed to save project mapping: %s", e)

    def close(self) -> None:
        """Close the connection."""
        if self._conn and not self._conn.closed:
            self._conn.close()


def create_task_db(host: str, port: int, user: str, password: str, dbname: str, **kwargs: Any) -> AnnotationTaskDB:
    """Create AnnotationTaskDB from connection parameters.

    Args:
        host: PostgreSQL host.
        port: PostgreSQL port.
        user: Database user.
        password: Database password.
        dbname: Database name.
        **kwargs: Extra params (schema, etc.) ignored for conninfo.

    Returns:
        AnnotationTaskDB instance.
    """
    conninfo = f"host={host} port={port} user={user} password={password} dbname={dbname}"
    return AnnotationTaskDB(conninfo)
