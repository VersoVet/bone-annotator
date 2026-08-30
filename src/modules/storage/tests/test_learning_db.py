"""Tests for learning stats PostgreSQL helpers."""

from unittest.mock import MagicMock, patch

from src.modules.storage.learning_db import LearningStatsDB, create_learning_db


@patch("src.modules.storage.learning_db.psycopg.connect")
def test_create_learning_db(mock_connect: MagicMock) -> None:
    """Factory builds LearningStatsDB with conninfo."""
    db = create_learning_db(host="localhost", port=5432, user="u", password="p", dbname="bone")
    assert isinstance(db, LearningStatsDB)
    mock_connect.assert_not_called()


@patch("src.modules.storage.learning_db.psycopg.connect")
def test_get_tracking_stats(mock_connect: MagicMock) -> None:
    """Tracking stats aggregate task, tier and catalog counts."""
    conn = MagicMock()
    conn.closed = False
    conn.execute.side_effect = [
        MagicMock(fetchall=lambda: [("pending", 3), ("done", 7)]),
        MagicMock(fetchall=lambda: [("gold", 12), ("silver", 5)]),
        MagicMock(fetchone=lambda: (42,)),
        MagicMock(fetchone=lambda: (8,)),
        MagicMock(fetchall=lambda: [("completed", 2)]),
    ]
    mock_connect.return_value = conn

    stats = LearningStatsDB("host=x").get_tracking_stats()
    assert stats["tasks_by_status"]["pending"] == 3
    assert stats["annotations_by_tier"]["gold"] == 12
    assert stats["catalog_total"] == 42
    assert stats["test_set_total"] == 8


@patch("src.modules.storage.learning_db.psycopg.connect")
def test_is_in_test_set(mock_connect: MagicMock) -> None:
    """Test set membership check."""
    conn = MagicMock()
    conn.closed = False
    conn.execute.return_value = MagicMock(fetchone=lambda: (1,))
    mock_connect.return_value = conn

    assert LearningStatsDB("host=x").is_in_test_set("humerus", "acq-1") is True


@patch("src.modules.storage.learning_db.psycopg.connect")
def test_get_learning_stats_velocity(mock_connect: MagicMock) -> None:
    """Learning stats include velocity and gold counts."""
    conn = MagicMock()
    conn.closed = False
    conn.execute.side_effect = [
        MagicMock(fetchall=lambda: [("gold", 10)]),
        MagicMock(fetchone=lambda: (5,)),
        MagicMock(fetchall=lambda: [("humerus", None)]),
        MagicMock(fetchone=lambda: (14,)),
        MagicMock(fetchone=lambda: (7,)),
        MagicMock(fetchone=lambda: (30,)),
        MagicMock(fetchall=lambda: []),
        MagicMock(fetchall=lambda: []),
        MagicMock(fetchone=lambda: (100,)),
    ]
    mock_connect.return_value = conn

    stats = LearningStatsDB("host=x").get_learning_stats(["humerus"])
    assert stats["velocity"]["week"] == 14
    assert stats["velocity"]["per_day"] == 2.0
    assert stats["gold_by_bone"]["humerus"] == 5


@patch("src.modules.storage.learning_db.psycopg.connect")
def test_reset_annotation_data(mock_connect: MagicMock) -> None:
    """Reset deletes tasks and annotations."""
    conn = MagicMock()
    conn.closed = False
    conn.execute.side_effect = [
        MagicMock(rowcount=4),
        MagicMock(rowcount=20),
        MagicMock(),
    ]
    mock_connect.return_value = conn

    result = LearningStatsDB("host=x").reset_annotation_data(include_annotations=True)
    assert result == {"tasks_deleted": 4, "annotations_deleted": 20}
