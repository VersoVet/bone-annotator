"""Embeddings service for vector storage and similarity search.

Manages Qdrant collection, embeddings storage, and bone atlas operations.
"""

import logging
from typing import Any

from .qdrant_store import BoneAtlasStore

logger = logging.getLogger(__name__)


class EmbeddingsService:
    """Service for embeddings and vector operations."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 6333,
        collection: str = "bone_atlas",
        vector_size: int = 512,
    ) -> None:
        """Initialize embeddings service.

        Args:
            host: Qdrant host.
            port: Qdrant port.
            collection: Collection name.
            vector_size: Embedding dimension.
        """
        self.store = BoneAtlasStore(host, port, collection, vector_size)
        self.store.ensure_collection()
        logger.info("EmbeddingsService initialized")

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
            "collection": self.store.collection,
            "vector_size": self.store.vector_size,
        }


# Module-level instance
_service: EmbeddingsService | None = None


def get_service(
    host: str = "localhost",
    port: int = 6333,
    collection: str = "bone_atlas",
    vector_size: int = 512,
) -> EmbeddingsService:
    """Get or create the embeddings service instance."""
    global _service
    if _service is None:
        _service = EmbeddingsService(host, port, collection, vector_size)
    return _service
