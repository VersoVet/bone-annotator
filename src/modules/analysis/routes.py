"""FastAPI routes for post-annotation analysis.

Provides endpoints for bone density analysis, conformation assessment,
and anomaly detection on annotated specimens.
"""

import logging
from typing import Any

import numpy as np
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .service import get_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/analysis", tags=["analysis"])


class DensityAnalysisRequest(BaseModel):
    """Request for density analysis."""

    density_mask: list[list[int]]
    image_data: list[list[float]]


class ConformationAnalysisRequest(BaseModel):
    """Request for conformation analysis."""

    bone_type: str
    landmarks: list[dict[str, Any]]
    image_size: int = 512


class AnomalyDetectionRequest(BaseModel):
    """Request for anomaly detection."""

    density_stats: dict[str, Any]
    reference_stats: dict[str, Any] | None = None


class AxisAnalysisRequest(BaseModel):
    """Request for bone axis analysis."""

    landmarks: list[dict[str, Any]]
    bone_type: str


@router.get("/status")
async def analysis_status() -> dict[str, Any]:
    """Get analysis service status.

    Returns:
        Service status with available models.
    """
    try:
        service = get_service()
        status = await service.status()

        return {
            "status": "ready",
            "service": "analysis",
            "components": status,
        }
    except Exception as e:
        logger.error("Error fetching analysis status: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch analysis status")


@router.post("/density")
async def analyze_density(request: DensityAnalysisRequest) -> dict[str, Any]:
    """Analyze bone density from segmentation mask.

    Args:
        request: Density mask and image data.

    Returns:
        Density analysis results with statistics.

    Raises:
        HTTPException: If analysis fails.
    """
    try:
        service = get_service()
        density_mask = np.array(request.density_mask, dtype=np.uint8)
        image_float = np.array(request.image_data, dtype=np.float32)

        result = await service.analyze_density(density_mask, image_float)

        return {
            "status": "success",
            "analysis": result,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Error analyzing density: %s", e)
        raise HTTPException(status_code=500, detail="Failed to analyze density")


@router.post("/conformation")
async def analyze_conformation(request: ConformationAnalysisRequest) -> dict[str, Any]:
    """Analyze bone conformation from landmarks.

    Args:
        request: Bone type, landmarks, and image size.

    Returns:
        Conformation analysis results.

    Raises:
        HTTPException: If analysis fails.
    """
    try:
        service = get_service()

        result = await service.analyze_conformation(
            request.bone_type,
            request.landmarks,
            request.image_size,
        )

        return {
            "status": "success",
            "bone_type": request.bone_type,
            "analysis": result,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Error analyzing conformation: %s", e)
        raise HTTPException(status_code=500, detail="Failed to analyze conformation")


@router.post("/anomalies")
async def detect_anomalies(request: AnomalyDetectionRequest) -> dict[str, Any]:
    """Detect density anomalies.

    Args:
        request: Density statistics and optional reference statistics.

    Returns:
        List of detected anomalies with severity.

    Raises:
        HTTPException: If detection fails.
    """
    try:
        service = get_service()

        anomalies = await service.detect_anomalies(
            request.density_stats,
            request.reference_stats,
        )

        return {
            "status": "success",
            "anomalies": anomalies,
            "count": len(anomalies),
        }
    except Exception as e:
        logger.error("Error detecting anomalies: %s", e)
        raise HTTPException(status_code=500, detail="Failed to detect anomalies")


@router.post("/axis")
async def analyze_bone_axis(request: AxisAnalysisRequest) -> dict[str, Any]:
    """Compute principal bone axis from landmarks.

    Args:
        request: Landmarks and bone type.

    Returns:
        Axis information with angle and direction.

    Raises:
        HTTPException: If analysis fails.
    """
    try:
        service = get_service()

        result = await service.analyze_bone_axis(
            request.landmarks,
            request.bone_type,
        )

        if result is None:
            return {
                "status": "insufficient_data",
                "message": "Not enough landmarks for axis computation",
            }

        return {
            "status": "success",
            "bone_type": request.bone_type,
            "axis": result,
        }
    except Exception as e:
        logger.error("Error analyzing bone axis: %s", e)
        raise HTTPException(status_code=500, detail="Failed to analyze bone axis")
