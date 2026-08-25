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
        assignee: str | None = None,
        frame_count: int = 0,
        dataset_path: str | None = None,
        pipeline_preset: str | None = None,
        pipeline_config: list[dict[str, Any]] | None = None,
        has_pre_annotations: bool = False,
        cvat_url: str | None = None,
    ) -> int:
        """Insert a new annotation task.

        Args:
            acquisition_id: Acquisition ID.
            bone_type: Bone type.
            author: Task creator.
            cvat_task_id: CVAT task ID.
            source_name: Image source name.
            region: Anatomical region.
            assignee: Assigned annotator.
            frame_count: Number of frames.
            dataset_path: Path to prepared dataset.
            pipeline_preset: Imaging-sdk preset used.
            pipeline_config: Pipeline configuration.
            has_pre_annotations: Whether ML pre-annotations applied.
            cvat_url: CVAT task URL.

        Returns:
            Created task ID.
        """
        conn = self._get_conn()
        row = conn.execute(
            f"""INSERT INTO {SCHEMA}.annotation_tasks
            (acquisition_id, bone_type, author, cvat_task_id, source_name,
             region, assignee, frame_count, dataset_path, pipeline_preset,
             pipeline_config, has_pre_annotations, cvat_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id""",
            (
                acquisition_id,
                bone_type,
                author,
                cvat_task_id,
                source_name,
                region,
                assignee,
                frame_count,
                dataset_path,
                pipeline_preset,
                json.dumps(pipeline_config) if pipeline_config else None,
                has_pre_annotations,
                cvat_url,
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
            "dataset_path",
            "parent_task_id",
        }
        updates = {k: v for k, v in kwargs.items() if k in allowed}
        if not updates:
            return
        conn = self._get_conn()
        set_clauses = ", ".join(f"{k}=%s" for k in updates)
        values = list(updates.values()) + [task_id]
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

    def list_tasks(
        self,
        limit: int = 50,
        offset: int = 0,
        status: str | None = None,
        bone_type: str | None = None,
    ) -> tuple[list[dict[str, Any]], int]:
        """List annotation tasks with filters.

        Args:
            limit: Max results.
            offset: Pagination offset.
            status: Filter by status.
            bone_type: Filter by bone type.

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
        where = ("WHERE " + " AND ".join(where_parts)) if where_parts else ""

        total = conn.execute(f"SELECT COUNT(*) FROM {SCHEMA}.annotation_tasks {where}", params).fetchone()[0]

        rows = conn.execute(
            f"SELECT * FROM {SCHEMA}.annotation_tasks {where} ORDER BY created_at DESC LIMIT %s OFFSET %s",
            [*params, limit, offset],
        ).fetchall()
        cols = [d[0] for d in conn.execute(f"SELECT * FROM {SCHEMA}.annotation_tasks LIMIT 0").description]
        tasks = [dict(zip(cols, row, strict=False)) for row in rows]
        return tasks, total

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
                    SET validated_by=%s, validated_at=NOW()
                    WHERE acquisition_id=%s AND validated_by IS NULL""",
                    (validated_by, task["acquisition_id"]),
                )

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
