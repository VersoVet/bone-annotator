"""Helper to log learning decisions with current tier snapshot."""

from src.config import get_postgres_config
from src.modules.storage.decisions_db import create_decisions_db
from src.modules.storage.learning_db import create_learning_db


def log_learning_decision(
    action: str,
    *,
    bone_type: str | None = None,
    generation: int | None = None,
    trigger_source: str = "system",
    payload: dict | None = None,
    notes: str | None = None,
) -> int:
    """Log a decision with current GOLD/SILVER counts."""
    learning_db = create_learning_db(**get_postgres_config())
    gold, silver = learning_db.get_tier_counts()
    decisions_db = create_decisions_db(**get_postgres_config())
    return decisions_db.log_decision(
        action,
        bone_type=bone_type,
        generation=generation,
        gold_count=gold,
        silver_count=silver,
        trigger_source=trigger_source,
        payload=payload,
        notes=notes,
    )
