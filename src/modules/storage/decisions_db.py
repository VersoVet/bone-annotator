"""PostgreSQL storage for structured learning decision history."""

import json
import logging
from typing import Any

import psycopg

from src.modules.storage.task_db import SCHEMA

logger = logging.getLogger(__name__)


class LearningDecisionsDB:
    """Append-only log of training and annotation strategy decisions."""

    def __init__(self, conninfo: str) -> None:
        """Initialize with PostgreSQL connection string."""
        self._conninfo = conninfo
        self._conn: psycopg.Connection | None = None

    def _get_conn(self) -> psycopg.Connection:
        if self._conn is None or self._conn.closed:
            self._conn = psycopg.connect(self._conninfo, autocommit=True)
        return self._conn

    def log_decision(
        self,
        action: str,
        *,
        bone_type: str | None = None,
        generation: int | None = None,
        gold_count: int | None = None,
        silver_count: int | None = None,
        trigger_source: str = "system",
        payload: dict[str, Any] | None = None,
        notes: str | None = None,
    ) -> int:
        """Record a learning decision event.

        Args:
            action: Decision type (training_started, test_set_added, ...).
            bone_type: Related bone type if any.
            generation: Model generation if applicable.
            gold_count: GOLD tier count at decision time.
            silver_count: SILVER tier count at decision time.
            trigger_source: Origin (manual, cron, system, api).
            payload: Extra structured metadata.
            notes: Free-text explanation.

        Returns:
            Inserted row id.
        """
        conn = self._get_conn()
        row = conn.execute(
            f"""INSERT INTO {SCHEMA}.learning_decisions
            (action, bone_type, generation, gold_count, silver_count,
             trigger_source, payload, notes)
            VALUES (%s, %s, %s, %s, %s, %s, %s::jsonb, %s)
            RETURNING id""",
            (
                action,
                bone_type,
                generation,
                gold_count,
                silver_count,
                trigger_source,
                json.dumps(payload or {}),
                notes,
            ),
        ).fetchone()
        return row[0] if row else 0

    def list_decisions(self, limit: int = 50, bone_type: str | None = None) -> list[dict[str, Any]]:
        """List recent learning decisions."""
        conn = self._get_conn()
        if bone_type:
            rows = conn.execute(
                f"""SELECT id, decided_at, action, bone_type, generation,
                           gold_count, silver_count, trigger_source, payload, notes
                    FROM {SCHEMA}.learning_decisions
                    WHERE bone_type = %s
                    ORDER BY decided_at DESC LIMIT %s""",
                (bone_type, limit),
            ).fetchall()
        else:
            rows = conn.execute(
                f"""SELECT id, decided_at, action, bone_type, generation,
                           gold_count, silver_count, trigger_source, payload, notes
                    FROM {SCHEMA}.learning_decisions
                    ORDER BY decided_at DESC LIMIT %s""",
                (limit,),
            ).fetchall()
        return [
            {
                "id": r[0],
                "decided_at": r[1].isoformat() if r[1] else None,
                "action": r[2],
                "bone_type": r[3],
                "generation": r[4],
                "gold_count": r[5],
                "silver_count": r[6],
                "trigger_source": r[7],
                "payload": r[8] or {},
                "notes": r[9],
            }
            for r in rows
        ]

    def close(self) -> None:
        """Close the connection."""
        if self._conn and not self._conn.closed:
            self._conn.close()


def create_decisions_db(
    host: str, port: int, user: str, password: str, dbname: str, **kwargs: Any
) -> LearningDecisionsDB:
    """Create LearningDecisionsDB from connection parameters."""
    conninfo = f"host={host} port={port} user={user} password={password} dbname={dbname}"
    return LearningDecisionsDB(conninfo)
