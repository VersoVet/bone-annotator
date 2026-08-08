"""PostgreSQL utility functions for annotation queries.

Helper functions for label studio table operations.
"""

from typing import Any

SCHEMA = "bone_annotations"


def ensure_ls_tables_sql() -> str:
    """Generate SQL for Label Studio tables creation.

    Returns:
        SQL script to create ls_projects and ls_sync tables.
    """
    return f"""
        CREATE TABLE IF NOT EXISTS {SCHEMA}.ls_projects (
            bone_type TEXT PRIMARY KEY,
            project_id INTEGER NOT NULL,
            project_title TEXT NOT NULL,
            created_at TIMESTAMPTZ DEFAULT NOW()
        );
        CREATE TABLE IF NOT EXISTS {SCHEMA}.ls_sync (
            acquisition_id TEXT PRIMARY KEY
                REFERENCES {SCHEMA}.acquisitions(id) ON DELETE CASCADE,
            project_id INTEGER NOT NULL,
            task_count INTEGER NOT NULL DEFAULT 0,
            imported_at TIMESTAMPTZ DEFAULT NOW()
        );
    """


def parse_acquisition_result(row: Any) -> dict[str, Any]:
    """Parse acquisition row from database.

    Args:
        row: Database row object.

    Returns:
        Dict with acquisition data.
    """
    return {
        "bone_type": row[0] if len(row) > 0 else "",
        "project_id": row[1] if len(row) > 1 else 0,
        "project_title": row[2] if len(row) > 2 else "",
        "synced_count": row[3] if len(row) > 3 else 0,
        "last_import": row[4] if len(row) > 4 else None,
    }
