"""Embeddings service for vector storage and similarity search.

Manages pgvector collection on OnyxPlex, embeddings storage,
and bone atlas operations with 1024D bge-m3 vectors.
"""

import logging
from typing import Any

from .pg_store import BoneAtlasStore

logger = logging.getLogger(__name__)


class EmbeddingsService:
    """Service for embeddings and vector operations."""

    def __init__(
        self,
        host: str = "10.0.0.8",
        port: int = 5432,
        database: str = "onyx_vectors",
        user: str = "onyx",
        password: str = "",
        collection: str = "bone_atlas",
        vector_size: int = 1024,
    ) -> None:
        """Initialize embeddings service.

        Args:
            host: PostgreSQL host (OnyxPlex).
            port: PostgreSQL port.
            database: Database name.
            user: Database user.
            password: Database password.
            collection: Collection name.
            vector_size: Embedding dimension (1024 for bge-m3).
        """
        self.store = BoneAtlasStore(host, port, database, user, password, collection, vector_size)
        self.store.ensure_collection()
        logger.info("EmbeddingsService initialized (pgvector)")

    async def upsert_bone(
        self,
        point_id: str,
        embedding: list[float],
        payload: dict[str, Any],
    ) -> None:
        """Store a bone embedding in the atlas.

        Args:
            point_id: Unique point ID.
            embedding: 512D vector.
            payload: Metadata dict.
        """
        self.store.upsert_bone(point_id, embedding, payload)

    async def upsert_batch(
        self,
        points: list[dict[str, Any]],
    ) -> None:
        """Batch store bone embeddings.

        Args:
            points: List of {id, embedding, payload} dicts.
        """
        self.store.upsert_batch(points)

    async def search_similar(
        self,
        embedding: list[float],
        bone_type: str | None = None,
        side: str | None = None,
        region: str | None = None,
        limit: int = 10,
        score_threshold: float = 0.0,
    ) -> list[dict[str, Any]]:
        """Search for similar bones.

        Args:
            embedding: Query vector.
            bone_type: Optional filter.
            side: Optional filter.
            region: Optional filter.
            limit: Max results.
            score_threshold: Min similarity score.

        Returns:
            List of similar bones.
        """
        return self.store.search_similar(embedding, bone_type, side, region, limit, score_threshold)

    async def find_atypical(
        self,
        bone_type: str,
        mahalanobis_threshold: float = 2.0,
        limit: int = 50,
    ) -> list[dict[str, Any]]:
        """Find atypical specimens.

        Args:
            bone_type: Bone type.
            mahalanobis_threshold: Distance threshold.
            limit: Max results.

        Returns:
            List of atypical bones.
        """
        return self.store.find_atypical(bone_type, mahalanobis_threshold, limit)

    async def get_population_stats(
        self,
        bone_type: str | None = None,
    ) -> dict[str, int]:
        """Get population statistics.

        Args:
            bone_type: Optional bone type filter.

        Returns:
            Statistics dict.
        """
        return self.store.get_population_stats(bone_type)

    async def delete_collection(self) -> None:
        """Delete the atlas collection."""
        self.store.delete_collection()

    async def build_payload(
        self,
        bone_type: str,
        side: str,
        region: str,
        confidence: dict[str, Any],
        source: dict[str, Any],
        angle: dict[str, Any],
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Build a rich payload for a bone entry.

        Args:
            bone_type: Bone type.
            side: Side.
            region: Region.
            confidence: Confidence metrics.
            source: Source info.
            angle: Angle info.
            **kwargs: Additional fields.

        Returns:
            Complete payload dict.
        """
        return self.store.build_payload(bone_type, side, region, confidence, source, angle, **kwargs)

    async def status(self) -> dict[str, Any]:
        """Get service status.

        Returns:
            Status dict.
        """
        return {
            "status": "ready",
            "backend": "pgvector",
            "collection": self.store.collection,
            "vector_size": self.store.vector_size,
        }


# Module-level instance
_service: EmbeddingsService | None = None


def get_service() -> EmbeddingsService:
    """Get or create the embeddings service from config."""
    global _service
    if _service is None:
        from src.config import (
            PGVECTOR_COLLECTION,
            PGVECTOR_DATABASE,
            PGVECTOR_HOST,
            PGVECTOR_PORT,
            PGVECTOR_USER,
            PGVECTOR_VECTOR_SIZE,
            POSTGRES_PASSWORD,
        )

        _service = EmbeddingsService(
            host=PGVECTOR_HOST,
            port=PGVECTOR_PORT,
            database=PGVECTOR_DATABASE,
            user=PGVECTOR_USER,
            password=POSTGRES_PASSWORD,
            collection=PGVECTOR_COLLECTION,
            vector_size=PGVECTOR_VECTOR_SIZE,
        )
    return _service


# ========== Async API Wrappers ==========


async def search_bone_atlas(
    embedding: list[float],
    limit: int = 10,
    min_confidence: float = 0.3,
) -> list[dict[str, Any]]:
    """Search bone atlas with embedding vector.

    Args:
        embedding: Query embedding (1024D vector for bge-m3).
        limit: Max results.
        min_confidence: Min similarity score.

    Returns:
        List of similar bones with metadata.
    """
    try:
        service = get_service()
        results = await service.search_similar(
            embedding=embedding,
            limit=limit,
            score_threshold=min_confidence,
        )
        return results
    except Exception as e:
        logger.error("Search failed: %s", e)
        return []


async def get_similar_bones(
    bone_id: str,
    limit: int = 10,
) -> list[dict[str, Any]]:
    """Find bones similar to a reference bone.

    Args:
        bone_id: Reference bone ID.
        limit: Max similar bones.

    Returns:
        List of similar bones or empty if not found.
    """
    try:
        logger.warning("Similar bones query not fully implemented (Phase 7+)")
        return []
    except Exception as e:
        logger.error("Similar bones query failed: %s", e)
        return []
