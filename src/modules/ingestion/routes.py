"""FastAPI routes for BoneStore ingestion orchestration.

Manages periodic sync of BoneStore acquisitions into annotation registry.
"""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException

from .service import get_ingestion_status, get_pending_acquisitions, sync_acquisitions

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/ingestion", tags=["ingestion"])


@router.post("/sync")
async def sync_bonestore() -> dict[str, Any]:
    """Synchronize BoneStore to ingestion registry.

    Discovers new acquisitions from BoneStore NFS mount and registers them
    in the ingestion tracking database for annotation processing.

    Returns:
        Sync result with counts of new/pending acquisitions.

    Raises:
        HTTPException: If sync fails.
    """
    try:
        result = await sync_acquisitions()

        if result.get("status") == "error":
            raise HTTPException(status_code=500, detail=result.get("message"))

        return result
    except Exception as e:
        logger.error("Error syncing BoneStore: %s", e)
        raise HTTPException(status_code=500, detail="Failed to sync BoneStore")


@router.get("/pending")
async def list_pending(
    limit: int = 100,
    offset: int = 0,
) -> dict[str, Any]:
    """List pending acquisitions waiting for annotation.

    Args:
        limit: Max acquisitions to return (default 100).
        offset: Pagination offset (default 0).

    Returns:
        List of pending acquisition IDs with metadata.

    Raises:
        HTTPException: If query fails.
    """
    try:
        acquisitions = await get_pending_acquisitions(limit, offset)
        return {
            "acquisitions": acquisitions,
            "total": len(acquisitions),
            "limit": limit,
            "offset": offset,
        }
    except Exception as e:
        logger.error("Error fetching pending acquisitions: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch pending acquisitions")


@router.get("/status")
async def ingestion_status() -> dict[str, Any]:
    """Get ingestion status and statistics.

    Returns:
        Ingestion status with registry stats and last sync timestamp.

    Raises:
        HTTPException: If query fails.
    """
    try:
        status = await get_ingestion_status()
        return status
    except Exception as e:
        logger.error("Error fetching ingestion status: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch ingestion status")


@router.post("/retry/{acquisition_id}")
async def retry_acquisition(acquisition_id: str) -> dict[str, Any]:
    """Retry ingestion for a failed acquisition.

    Args:
        acquisition_id: Acquisition ID to retry.

    Returns:
        Retry status.

    Raises:
        HTTPException: If retry fails.
    """
    try:
        # TODO: Implement retry logic in ingestion service
        return {
            "status": "pending_implementation",
            "acquisition_id": acquisition_id,
            "message": "Retry logic coming in Phase 7+",
        }
    except Exception as e:
        logger.error("Error retrying acquisition: %s", e)
        raise HTTPException(status_code=500, detail="Failed to retry acquisition")
