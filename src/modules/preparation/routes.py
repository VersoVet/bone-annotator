"""FastAPI routes for dataset preparation.

Provides endpoints to prepare annotation datasets from raw acquisitions
using imaging-sdk pipelines.
"""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field

from src.modules.sources.service import get_service as get_source_service

from .service import get_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/preparation", tags=["preparation"])


class PrepareRequest(BaseModel):
    """Request to prepare an annotation dataset."""

    source_name: str = Field(default="bonestore", description="Image source name")
    acquisition_id: str = Field(..., description="Acquisition ID")
    bone_type: str = Field(..., description="Bone type")
    pipeline_preset: str = Field(default="replay_membre", description="Imaging-sdk preset")
    custom_pipeline: list[dict[str, Any]] | None = Field(None, description="Custom pipeline config")
    image_size: int | None = Field(None, ge=64, le=4096, description="Optional resize")


@router.post("/prepare")
async def prepare_dataset(request: PrepareRequest) -> dict[str, Any]:
    """Prepare an annotation dataset from raw acquisition frames.

    Applies imaging-sdk pipeline to convert .b2nd to PNG 16-bit.

    Args:
        request: Preparation parameters.

    Returns:
        Prepared dataset info with path, frame count, pipeline used.

    Raises:
        HTTPException: If acquisition not found or preparation fails.
    """
    try:
        source_service = get_source_service()
        acq_path = source_service.get_acquisition_path(request.source_name, request.acquisition_id)
        if acq_path is None:
            raise HTTPException(status_code=404, detail=f"Acquisition not found: {request.acquisition_id}")

        service = get_service()
        dataset = await service.prepare_dataset(
            acquisition_path=acq_path,
            acquisition_id=request.acquisition_id,
            bone_type=request.bone_type,
            pipeline_preset=request.pipeline_preset,
            custom_pipeline=request.custom_pipeline,
            image_size=request.image_size,
        )
        return {"status": "success", "dataset": dataset.to_dict()}
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Error preparing dataset: %s", e)
        raise HTTPException(status_code=500, detail="Failed to prepare dataset")


@router.get("/datasets")
async def list_datasets() -> dict[str, Any]:
    """List all prepared annotation datasets.

    Returns:
        List of dataset metadata.
    """
    service = get_service()
    datasets = service.list_datasets()
    return {"status": "ok", "datasets": datasets, "count": len(datasets)}


@router.get("/presets/{bone_type}")
async def list_presets(bone_type: str) -> dict[str, Any]:
    """List available imaging-sdk presets for a bone type.

    Args:
        bone_type: Bone type for preset suggestions.

    Returns:
        List of preset descriptors.
    """
    service = get_service()
    presets = service.get_presets(bone_type)
    return {"status": "ok", "bone_type": bone_type, "presets": presets}


@router.get("/datasets/{dataset_id}/preview/{frame_name}")
async def preview_frame(dataset_id: str, frame_name: str) -> Response:
    """Preview a prepared frame as PNG.

    Args:
        dataset_id: Dataset identifier.
        frame_name: Frame filename (without extension).

    Returns:
        PNG image bytes.

    Raises:
        HTTPException: If frame not found.
    """
    service = get_service()
    frame_path = service.storage_root / dataset_id / "images" / f"{frame_name}.png"
    if not frame_path.exists():
        raise HTTPException(status_code=404, detail=f"Frame not found: {frame_name}")
    return Response(content=frame_path.read_bytes(), media_type="image/png")
