"""Tests for annotation traceability guards."""

from unittest.mock import MagicMock, patch

import pytest

from src.modules.annotation.exceptions import ActiveTaskExistsError


def test_active_task_exists_error() -> None:
    """ActiveTaskExistsError carries existing task metadata."""
    err = ActiveTaskExistsError({"id": 7, "status": "annotating"})
    assert err.existing["id"] == 7


def test_find_active_task_query() -> None:
    """find_active_task filters on active statuses only."""
    from src.modules.storage.task_db import ACTIVE_TASK_STATUSES, AnnotationTaskDB

    db = AnnotationTaskDB.__new__(AnnotationTaskDB)
    mock_conn = MagicMock()
    mock_conn.execute.return_value.fetchone.return_value = (3, "annotating", 42, "ACQ1", "humerus")
    db._get_conn = MagicMock(return_value=mock_conn)  # type: ignore[method-assign]

    row = db.find_active_task("ACQ1", "humerus")
    assert row is not None
    assert row["id"] == 3
    sql = mock_conn.execute.call_args[0][0]
    for status in ACTIVE_TASK_STATUSES:
        assert status in sql or status in str(mock_conn.execute.call_args)


def test_save_frame_annotations_requires_task_id() -> None:
    """frame_annotations insert rejects missing task_id."""
    from src.modules.storage.pg_db import AnnotationPgDB

    db = AnnotationPgDB.__new__(AnnotationPgDB)
    db._get_conn = MagicMock()  # type: ignore[method-assign]

    with pytest.raises(ValueError, match="task_id is required"):
        db.save_frame_annotations("ACQ1", "frame_0001.png", {"zones": []})


@patch("src.modules.storage.task_db.psycopg.connect")
def test_validate_task_scopes_by_task_id(mock_connect: MagicMock) -> None:
    """Validation UPDATE includes task_id filter."""
    from src.modules.storage.task_db import AnnotationTaskDB

    conn = MagicMock()
    conn.closed = False
    executed_sql: list[str] = []
    cols = [("id",), ("acquisition_id",), ("bone_type",)]

    def _execute(sql: str, params: tuple | None = None) -> MagicMock:
        executed_sql.append(sql)
        cur = MagicMock()
        if "WHERE id=%s" in sql:
            cur.fetchone.return_value = (1, "ACQ1", "humerus")
            cur.description = cols
        elif "LIMIT 0" in sql:
            cur.description = cols
        return cur

    conn.execute.side_effect = _execute
    mock_connect.return_value = conn

    AnnotationTaskDB("host=x").validate_task(1, "reviewer1", "validated")
    frame_updates = [s for s in executed_sql if "frame_annotations" in s and "UPDATE" in s]
    assert frame_updates
    assert "task_id" in frame_updates[0]
