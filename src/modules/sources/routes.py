"""FastAPI routes for image source management.

Provides endpoints to list sources, acquisitions, and frames.
"""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException, Query

from .service import get_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/sources", tags=["sources"])


@router.get("")
async def list_sources() -> dict[str, Any]:
    """List all configured and enabled image sources.

    Returns:
        List of source descriptors with name, type, description.
    """
    service = get_service()
    sources = service.list_sources()
    return {"status": "ok", "sources": sources, "count": len(sources)}


@router.get("/{source_name}/acquisitions")
async def list_acquisitions(
    source_name: str,
    bone_type: str | None = Query(None, description="Filter by bone type"),
    side: str | None = Query(None, description="Filter by side"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
) -> dict[str, Any]:
    """List acquisitions from a specific source.

    Args:
        source_name: Source name from config.
        bone_type: Optional bone type filter.
        side: Optional side filter.
        limit: Max results.
        offset: Pagination offset.

    Returns:
        List of acquisitions with metadata.

    Raises:
        HTTPException: If source not found.
    """
    try:
        service = get_service()
        acqs = service.list_acquisitions(source_name, bone_type, side)
        total = len(acqs)
        page = acqs[offset : offset + limit]
        return {
            "status": "ok",
            "source": source_name,
            "acquisitions": page,
            "total": total,
            "limit": limit,
            "offset": offset,
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error("Error listing acquisitions: %s", e)
        raise HTTPException(status_code=500, detail="Failed to list acquisitions")


@router.get("/{source_name}/acquisitions/{acquisition_id}/frames")
async def list_frames(
    source_name: str,
    acquisition_id: str,
    with_paths: bool = Query(False, description="Include full .b2nd file paths"),
) -> dict[str, Any]:
    """List frames for a specific acquisition.

    Args:
        source_name: Source name.
        acquisition_id: Acquisition ID.
        with_paths: Include full filesystem paths for direct imaging access.

    Returns:
        Frame list with index, filename, angle.

    Raises:
        HTTPException: If source or acquisition not found.
    """
    try:
        service = get_service()
        frames = service.get_frames(source_name, acquisition_id)
        if with_paths:
            acq_path = service.get_acquisition_path(source_name, acquisition_id)
            if acq_path:
                raw_dir = acq_path / "raw"
                for f in frames:
                    f["path"] = str(raw_dir / f["filename"])
        return {
            "status": "ok",
            "source": source_name,
            "acquisition_id": acquisition_id,
            "frames": frames,
            "frame_count": len(frames),
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error("Error listing frames: %s", e)
        raise HTTPException(status_code=500, detail="Failed to list frames")
