"""FastAPI routes for imaging operations.

Provides endpoints for frame loading, PNG conversion,
cache management, preloading, and bone taxonomy catalog.
"""

import logging
from typing import Any

from fastapi import APIRouter, BackgroundTasks, HTTPException, Query
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

    Raises:
        HTTPException: If status cannot be fetched.
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


@router.get("/frame.png")
async def get_frame_png(
    path: str = Query(..., description="Path to .b2nd frame file"),
    size: int = Query(default=768, ge=64, le=4096, description="Output size in pixels"),
) -> Response:
    """Serve a frame as PNG via GET (usable as img src).

    Uses two-level cache (raw + PNG) for fast repeated access.

    Args:
        path: Path to .b2nd frame file on BoneStore.
        size: Output size in pixels.

    Returns:
        PNG image bytes with cache headers.

    Raises:
        HTTPException: If frame loading fails.
    """
    try:
        service = get_service()
        png_bytes = await service.load_frame_as_png(path, size)
        return Response(
            content=png_bytes,
            media_type="image/png",
            headers={"Cache-Control": "public, max-age=3600"},
        )
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Frame not found: {path}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Error serving frame PNG: %s", e)
        raise HTTPException(status_code=500, detail="Failed to load frame")


class PreloadRequest(BaseModel):
    """Request to preload frames for an acquisition."""

    acquisition_id: str = Field(..., description="Acquisition ID")
    source_name: str = Field(default="bonestore", description="Image source")
    size: int = Field(default=512, ge=64, le=4096, description="PNG output size")


@router.post("/preload")
async def preload_acquisition(
    request: PreloadRequest,
    background_tasks: BackgroundTasks,
) -> dict[str, Any]:
    """Preload all frames for an acquisition into cache.

    Runs in background so the caller gets an immediate response.
    Subsequent GET /frame.png calls for these frames will be instant.

    Args:
        request: Acquisition and size parameters.
        background_tasks: FastAPI background task scheduler.

    Returns:
        Acknowledgement with frame count to preload.

    Raises:
        HTTPException: If acquisition not found.
    """
    from src.modules.sources.service import get_service as get_source_service

    try:
        source_svc = get_source_service()
        frames = source_svc.get_frames(request.source_name, request.acquisition_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    acq_path = source_svc.get_acquisition_path(request.source_name, request.acquisition_id)
    if acq_path is None:
        raise HTTPException(status_code=404, detail="Acquisition not found")

    raw_dir = acq_path / "raw"
    paths = [str(raw_dir / f["filename"]) for f in frames]

    service = get_service()

    async def _do_preload() -> None:
        loaded = await service.preload_acquisition(paths, request.size)
        logger.info(
            "Preload complete: %s — %d/%d frames cached",
            request.acquisition_id, loaded, len(paths),
        )

    background_tasks.add_task(_do_preload)

    return {
        "status": "preloading",
        "acquisition_id": request.acquisition_id,
        "frame_count": len(paths),
        "size": request.size,
    }


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
