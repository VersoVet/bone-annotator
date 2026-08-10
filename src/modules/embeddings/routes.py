"""FastAPI routes for semantic search on bone annotations.

Provides endpoints for querying the Qdrant vector store
and performing similarity search on bone atlas and annotations.
"""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException

from .service import get_similar_bones, search_bone_atlas

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/embeddings", tags=["embeddings"])


@router.post("/search/bone-atlas")
async def search_atlas(
    embedding: list[float],
    limit: int = 10,
    min_confidence: float = 0.3,
) -> dict[str, Any]:
    """Search bone atlas with semantic embedding vector.

    Find similar bones from the atlas using vector similarity.

    Args:
        embedding: Query embedding vector (512D).
        limit: Max results to return (default 10).
        min_confidence: Minimum confidence score (default 0.3).

    Returns:
        List of similar bones with distances and metadata.

    Raises:
        HTTPException: If search fails.
    """
    try:
        if len(embedding) != 512:
            raise ValueError("Embedding must be 512D vector")

        results = await search_bone_atlas(embedding, limit, min_confidence)
        return {
            "status": "success",
            "query_vector_size": len(embedding),
            "results": results,
            "total": len(results),
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Search failed: %s", e)
        raise HTTPException(status_code=500, detail="Search failed")


@router.get("/similar/{bone_id}")
async def get_similar(
    bone_id: str,
    limit: int = 10,
) -> dict[str, Any]:
    """Find similar bones to a reference bone.

    Args:
        bone_id: Reference bone ID in atlas.
        limit: Max similar bones to return.

    Returns:
        List of similar bones ranked by distance.

    Raises:
        HTTPException: If query fails or bone not found.
    """
    try:
        results = await get_similar_bones(bone_id, limit)

        if not results:
            raise HTTPException(status_code=404, detail=f"Bone {bone_id} not found")

        return {
            "status": "success",
            "reference_bone_id": bone_id,
            "similar_bones": results,
            "total": len(results),
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error finding similar bones: %s", e)
        raise HTTPException(status_code=500, detail="Failed to find similar bones")


@router.get("/stats")
async def embedding_stats() -> dict[str, Any]:
    """Get statistics about embeddings collections.

    Returns:
        Stats on bone_atlas and bone_annotations collections.

    Raises:
        HTTPException: If stat collection fails.
    """
    try:
        return {
            "status": "ready",
            "collections": {
                "bone_atlas": {
                    "vector_size": 512,
                    "distance_metric": "cosine",
                    "description": "Reference bone anatomy embeddings",
                },
                "bone_annotations": {
                    "vector_size": 768,
                    "distance_metric": "cosine",
                    "description": "Annotation labels and criteria embeddings",
                },
            },
            "note": "Point counts loaded from Qdrant on query",
        }
    except Exception as e:
        logger.error("Error fetching embedding stats: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch statistics")


@router.post("/index/refresh")
async def refresh_embeddings() -> dict[str, Any]:
    """Refresh embedding indexes (recompute if needed).

    Returns:
        Refresh status.

    Raises:
        HTTPException: If refresh fails.
    """
    try:
        # TODO: Implement in Phase 7+ after Qdrant integration is complete
        return {
            "status": "pending_implementation",
            "message": "Embedding refresh coming in Phase 7+",
        }
    except Exception as e:
        logger.error("Error refreshing embeddings: %s", e)
        raise HTTPException(status_code=500, detail="Refresh failed")
