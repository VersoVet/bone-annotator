"""Unified storage service for annotations and embeddings.

Provides a high-level interface for persisting and retrieving
annotations from PostgreSQL and embeddings from pgvector.
"""

import logging
from typing import Any

from src.modules.storage.pg_db import AnnotationPgDB

logger = logging.getLogger(__name__)


class StorageService:
    """Unified storage for annotations and embeddings.

    Coordinates PostgreSQL operations for annotations and pgvector
    for semantic search on vectorized annotations.

    Args:
        pg_db: PostgreSQL database client.
    """

    def __init__(
        self,
        pg_db: AnnotationPgDB,
    ) -> None:
        """Initialize storage service."""
        self._pg_db = pg_db

    # ========== PostgreSQL Operations ==========

    async def save_annotation(
        self,
        acquisition_id: str,
        frame_id: str,
        annotation_type: str,
        data: dict[str, Any],
    ) -> bool:
        """Save an annotation to PostgreSQL.

        Args:
            acquisition_id: Acquisition ID.
            frame_id: Frame identifier.
            annotation_type: Type (zone, landmark, measurement, lesion).
            data: JSONB annotation data.

        Returns:
            True if successful.
        """
        try:
            self._pg_db.save_annotation(
                acquisition_id=acquisition_id,
                frame_id=frame_id,
                annotation_type=annotation_type,
                data=data,
            )
            return True
        except Exception as e:
            logger.error("Failed to save annotation: %s", e)
            return False

    async def get_annotations(
        self,
        acquisition_id: str,
        annotation_type: str | None = None,
    ) -> list[dict[str, Any]]:
        """Get annotations for an acquisition.

        Args:
            acquisition_id: Acquisition ID.
            annotation_type: Filter by type (optional).

        Returns:
            List of annotation dicts.
        """
        try:
            annotations = self._pg_db.get_annotations(acquisition_id, annotation_type)
            return annotations if annotations else []
        except Exception as e:
            logger.error("Failed to fetch annotations: %s", e)
            return []

    async def delete_annotation(self, annotation_id: str) -> bool:
        """Delete an annotation.

        Args:
            annotation_id: Annotation ID.

        Returns:
            True if successful.
        """
        try:
            self._pg_db.delete_annotation(annotation_id)
            return True
        except Exception as e:
            logger.error("Failed to delete annotation: %s", e)
            return False

    async def get_acquisition(self, acquisition_id: str) -> dict[str, Any] | None:
        """Get acquisition metadata.

        Args:
            acquisition_id: Acquisition ID.

        Returns:
            Acquisition dict or None.
        """
        try:
            return self._pg_db.get_acquisition(acquisition_id)
        except Exception as e:
            logger.error("Failed to fetch acquisition: %s", e)
            return None

    # ========== pgvector Operations (via embeddings module) ==========

    async def status(self) -> dict[str, Any]:
        """Get storage service status.

        Returns:
            Status dict with component health.
        """
        return {
            "status": "ready",
            "postgres": "connected" if self._pg_db else "unavailable",
            "pgvector": "available (via embeddings module)",
        }


# Module-level instance
_service: StorageService | None = None


def get_service(
    pg_db: AnnotationPgDB | None = None,
) -> StorageService:
    """Get or create the storage service instance.

    Args:
        pg_db: PostgreSQL client (cached if already initialized).

    Returns:
        StorageService instance.
    """
    global _service
    if _service is None:
        if pg_db is None:
            from src.config import get_postgres_config

            pg_config = get_postgres_config()
            pg_db = AnnotationPgDB(**pg_config)
        _service = StorageService(pg_db)
    return _service
