"""FastAPI routes for imaging operations.

Provides endpoints for frame loading, PNG conversion,
cache management, and bone taxonomy catalog.
"""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import Response
from pydantic import BaseModel, Field

from .service import get_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/imaging", tags=["imaging"])


class FrameLoadRequest(BaseModel):
    """Request to load a frame from BoneStore."""

    path: str = Field(..., description="Path to .b2nd frame file")


class FrameToPngRequest(BaseModel):
    """Request to convert a frame to PNG."""

    path: str = Field(..., description="Path to .b2nd frame file")
    size: int = Field(default=768, ge=64, le=4096, description="Output size in pixels")


class ParseCategoryRequest(BaseModel):
    """Request to parse a bone category from directory name."""

    dirname: str = Field(..., description="Directory name (e.g. '001^humerus_left_proximal')")


@router.get("/status")
async def imaging_status() -> dict[str, Any]:
    """Get imaging service status.

    Returns:
        Service status with cache statistics.
    """
    try:
        service = get_service()
        status = await service.status()
        return {"status": "ready", "service": "imaging", **status}
    except Exception as e:
        logger.error("Error fetching imaging status: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch imaging status")


@router.get("/cache/stats")
async def cache_stats() -> dict[str, Any]:
    """Get frame cache statistics.

    Returns:
        Cache sizes for raw and processed caches.
    """
    service = get_service()
    stats = await service.get_cache_stats()
    return {"status": "ok", "cache": stats}


@router.post("/cache/clear")
async def clear_cache() -> dict[str, str]:
    """Clear all frame caches.

    Returns:
        Confirmation message.
    """
    service = get_service()
    await service.clear_cache()
    return {"status": "ok", "message": "Caches cleared"}


@router.post("/frame/png")
async def frame_to_png(request: FrameToPngRequest) -> Response:
    """Load a frame and return as PNG image.

    Args:
        request: Path to frame and output size.

    Returns:
        PNG image bytes.

    Raises:
        HTTPException: If frame loading or conversion fails.
    """
    try:
        service = get_service()
        frame = await service.load_frame(request.path)
        png_bytes = await service.frame_to_png(frame, request.size)
        return Response(content=png_bytes, media_type="image/png")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Frame not found: {request.path}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Error converting frame to PNG: %s", e)
        raise HTTPException(status_code=500, detail="Failed to convert frame")


@router.get("/catalog")
async def get_catalog() -> dict[str, Any]:
    """Get available imaging filters catalog.

    Returns:
        Dict of filter names to their properties and parameters.
    """
    service = get_service()
    catalog = await service.get_filter_catalog()
    return {"status": "ok", "filters": catalog, "count": len(catalog)}


@router.post("/parse-category")
async def parse_category(request: ParseCategoryRequest) -> dict[str, Any]:
    """Parse bone category from BoneStore directory name.

    Args:
        request: Directory name to parse.

    Returns:
        Parsed bone type, side, and region.
    """
    service = get_service()
    result = await service.parse_category(request.dirname)
    return {"status": "ok", **result}


@router.get("/frame/info")
async def frame_info(
    path: str = Query(..., description="Path to .b2nd frame file"),
) -> dict[str, Any]:
    """Get frame metadata without full loading.

    Args:
        path: Path to frame file.

    Returns:
        Frame dimensions and dtype.

    Raises:
        HTTPException: If frame cannot be read.
    """
    try:
        service = get_service()
        frame = await service.load_frame(path)
        return {
            "status": "ok",
            "path": path,
            "shape": list(frame.shape),
            "dtype": str(frame.dtype),
            "size_bytes": int(frame.nbytes),
        }
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Frame not found: {path}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Error reading frame info: %s", e)
        raise HTTPException(status_code=500, detail="Failed to read frame info")
