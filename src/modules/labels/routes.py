"""FastAPI routes for anatomical label management.

Provides endpoints for accessing bone anatomy labels, zones, landmarks,
and lesion criteria from label-generator service.
"""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException

from . import service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/labels", tags=["labels"])


@router.get("/status")
async def labels_status() -> dict[str, Any]:
    """Get label service status.

    Returns:
        Service status with available bone types and label counts.
    """
    try:
        status = await service.get_status()

        return {
            "status": "ready",
            "service": "labels",
            "components": status,
        }
    except Exception as e:
        logger.error("Error fetching labels status: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch labels status")


@router.get("/anatomy")
async def get_all_labels() -> dict[str, Any]:
    """Get all anatomical labels for all bone types.

    Returns:
        Complete label hierarchy keyed by bone type.
    """
    try:
        labels = service.load_anatomy_labels()

        return {
            "status": "success",
            "bone_types": list(labels.keys()),
            "labels": labels,
        }
    except Exception as e:
        logger.error("Error loading anatomy labels: %s", e)
        raise HTTPException(status_code=500, detail="Failed to load anatomy labels")


@router.get("/bones/{bone_type}")
async def get_bone_labels(bone_type: str) -> dict[str, Any]:
    """Get labels for a specific bone type.

    Args:
        bone_type: Type of bone (humerus, radius, ulna, etc.).

    Returns:
        Label hierarchy for the bone type.

    Raises:
        HTTPException: If bone type not found.
    """
    try:
        if not bone_type or not bone_type.strip():
            raise HTTPException(status_code=400, detail="bone_type is required")

        hierarchy = service.get_label_hierarchy(bone_type)

        if hierarchy.get("error") == "not_found":
            raise HTTPException(
                status_code=404,
                detail=f"Labels not found for bone type: {bone_type}",
            )

        return {
            "status": "success",
            "bone_type": bone_type,
            "labels": hierarchy,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error fetching labels for %s: %s", bone_type, e)
        raise HTTPException(status_code=500, detail="Failed to fetch bone labels")


@router.get("/bones/{bone_type}/zones")
async def get_bone_zones(bone_type: str, region: str = "") -> dict[str, Any]:
    """Get anatomical zones for a bone type and optional region.

    Args:
        bone_type: Type of bone.
        region: Optional region filter (proximal, distal, entire).

    Returns:
        List of applicable anatomical zones.

    Raises:
        HTTPException: If bone type not found.
    """
    try:
        if not bone_type or not bone_type.strip():
            raise HTTPException(status_code=400, detail="bone_type is required")

        zones = service.get_zones(bone_type, region)

        if not zones:
            raise HTTPException(
                status_code=404,
                detail=f"No zones found for bone type: {bone_type}",
            )

        return {
            "status": "success",
            "bone_type": bone_type,
            "region": region or "all",
            "zones": zones,
            "count": len(zones),
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error fetching zones for %s: %s", bone_type, e)
        raise HTTPException(status_code=500, detail="Failed to fetch zones")


@router.get("/bones/{bone_type}/landmarks")
async def get_bone_landmarks(bone_type: str) -> dict[str, Any]:
    """Get anatomical landmarks for a bone type.

    Args:
        bone_type: Type of bone.

    Returns:
        List of anatomical landmarks.

    Raises:
        HTTPException: If bone type not found.
    """
    try:
        if not bone_type or not bone_type.strip():
            raise HTTPException(status_code=400, detail="bone_type is required")

        landmarks = service.get_landmarks(bone_type)

        if not landmarks:
            raise HTTPException(
                status_code=404,
                detail=f"No landmarks found for bone type: {bone_type}",
            )

        return {
            "status": "success",
            "bone_type": bone_type,
            "landmarks": landmarks,
            "count": len(landmarks),
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error fetching landmarks for %s: %s", bone_type, e)
        raise HTTPException(status_code=500, detail="Failed to fetch landmarks")


@router.get("/bones/{bone_type}/lesion-criteria")
async def get_bone_lesion_criteria(bone_type: str) -> dict[str, Any]:
    """Get lesion criteria and pathology classification for a bone type.

    Args:
        bone_type: Type of bone.

    Returns:
        Lesion criteria and severity levels.

    Raises:
        HTTPException: If bone type not found.
    """
    try:
        if not bone_type or not bone_type.strip():
            raise HTTPException(status_code=400, detail="bone_type is required")

        criteria = service.get_lesion_criteria(bone_type)

        if not criteria:
            raise HTTPException(
                status_code=404,
                detail=f"No lesion criteria found for bone type: {bone_type}",
            )

        return {
            "status": "success",
            "bone_type": bone_type,
            "criteria": criteria,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error fetching lesion criteria for %s: %s", bone_type, e)
        raise HTTPException(status_code=500, detail="Failed to fetch lesion criteria")


@router.post("/validate/zone")
async def validate_zone(
    bone_type: str,
    zone_id: str,
    region: str = "",
) -> dict[str, Any]:
    """Validate that a zone annotation is applicable for bone type and region.

    Args:
        bone_type: Type of bone.
        zone_id: Zone identifier.
        region: Optional region (proximal, distal, entire).

    Returns:
        Validation result.
    """
    try:
        if not bone_type or not zone_id:
            raise HTTPException(status_code=400, detail="bone_type and zone_id required")

        valid = service.validate_zone_annotation(bone_type, zone_id, region)

        return {
            "status": "success",
            "valid": valid,
            "bone_type": bone_type,
            "zone_id": zone_id,
            "region": region or "any",
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error validating zone: %s", e)
        raise HTTPException(status_code=500, detail="Failed to validate zone")


@router.post("/validate/landmark")
async def validate_landmark(bone_type: str, landmark_id: str) -> dict[str, Any]:
    """Validate that a landmark annotation is applicable for bone type.

    Args:
        bone_type: Type of bone.
        landmark_id: Landmark identifier.

    Returns:
        Validation result.
    """
    try:
        if not bone_type or not landmark_id:
            raise HTTPException(status_code=400, detail="bone_type and landmark_id required")

        valid = service.validate_landmark_annotation(bone_type, landmark_id)

        return {
            "status": "success",
            "valid": valid,
            "bone_type": bone_type,
            "landmark_id": landmark_id,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error validating landmark: %s", e)
        raise HTTPException(status_code=500, detail="Failed to validate landmark")


@router.post("/sync")
async def sync_labels() -> dict[str, Any]:
    """Synchronize labels from label-generator service.

    Returns:
        Number of bone types synchronized.

    Raises:
        HTTPException: If sync fails.
    """
    try:
        count = await service.sync_labels_from_generator()

        return {
            "status": "synced",
            "bone_types_updated": count,
        }
    except Exception as e:
        logger.error("Error syncing labels: %s", e)
        raise HTTPException(status_code=500, detail="Failed to sync labels")
