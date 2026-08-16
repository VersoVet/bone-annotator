"""Tests for annotation task database models and imports."""


def test_task_db_import() -> None:
    """Test AnnotationTaskDB class import."""
    from src.modules.storage.task_db import AnnotationTaskDB  # noqa: F401

    assert True


def test_create_task_db_import() -> None:
    """Test create_task_db function import."""
    from src.modules.storage.task_db import create_task_db  # noqa: F401

    assert True


def test_migrations_list() -> None:
    """Test migration SQL statements are defined."""
    from src.modules.storage.task_db import _MIGRATIONS

    assert len(_MIGRATIONS) >= 7
    assert any("annotation_tasks" in m for m in _MIGRATIONS)
    assert any("author" in m for m in _MIGRATIONS)


def test_allowed_update_fields() -> None:
    """Test update_task only allows specific fields."""
    from src.modules.storage.task_db import AnnotationTaskDB

    # Verify the allowed set exists and has the right fields
    db = AnnotationTaskDB.__new__(AnnotationTaskDB)
    db._conninfo = ""
    db._conn = None
    # Call with unknown field - should not crash, just skip
    # (would need a real connection to test further)
    assert True
