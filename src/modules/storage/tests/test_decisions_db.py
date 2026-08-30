"""Tests for learning decisions PostgreSQL storage."""

from unittest.mock import MagicMock, patch

from src.modules.storage.decisions_db import LearningDecisionsDB, create_decisions_db


@patch("src.modules.storage.decisions_db.psycopg.connect")
def test_log_decision(mock_connect: MagicMock) -> None:
    """log_decision inserts and returns row id."""
    conn = MagicMock()
    conn.closed = False
    conn.execute.return_value = MagicMock(fetchone=lambda: (42,))
    mock_connect.return_value = conn

    row_id = LearningDecisionsDB("host=x").log_decision(
        "training_started",
        bone_type="humerus",
        generation=2,
        gold_count=500,
        notes="test",
    )
    assert row_id == 42


def test_create_decisions_db() -> None:
    """Factory returns LearningDecisionsDB instance."""
    db = create_decisions_db(host="localhost", port=5432, user="u", password="p", dbname="d")
    assert isinstance(db, LearningDecisionsDB)
