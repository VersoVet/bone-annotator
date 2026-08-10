"""FastAPI routes for BoneStore acquisition browsing.

Provides endpoints for listing acquisitions and querying metadata
from the NFS BoneStore mount.
"""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException

from .service import (
    find_acquisition,
    get_acquisition_frames,
    list_acquisitions,
    load_timecodes,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/bonestore", tags=["bonestore"])


@router.get("/acquisitions")
async def acquisitions(
    bone_type: str | None = None,
    side: str | None = None,
    limit: int = 100,
) -> dict[str, Any]:
    """List acquisitions from BoneStore NFS.

    Args:
        bone_type: Filter by bone type (optional).
        side: Filter by side (optional).
        limit: Max acquisitions (default 100).

    Returns:
        List of acquisitions with metadata.

    Raises:
        HTTPException: If listing fails.
    """
    try:
        all_acqs = list_acquisitions()

        # Apply filters
        if bone_type:
            all_acqs = [a for a in all_acqs if a.get("bone_type") == bone_type]
        if side:
            all_acqs = [a for a in all_acqs if a.get("side") == side]

        # Apply limit
        acquisitions = all_acqs[:limit]

        return {
            "acquisitions": acquisitions,
            "total": len(all_acqs),
            "filtered": len(acquisitions),
            "limit": limit,
        }
    except Exception as e:
        logger.error("Error listing acquisitions: %s", e)
        raise HTTPException(status_code=500, detail="Failed to list acquisitions")


@router.get("/acquisitions/{acquisition_id}")
async def get_acquisition_metadata(acquisition_id: str) -> dict[str, Any]:
    """Get metadata and frames for an acquisition.

    Args:
        acquisition_id: Acquisition ID.

    Returns:
        Acquisition metadata with frame list.

    Raises:
        HTTPException: If acquisition not found.
    """
    try:
        acq_dir = find_acquisition(None, acquisition_id)

        if not acq_dir:
            raise HTTPException(status_code=404, detail="Acquisition not found")

        frames = get_acquisition_frames(acq_dir)
        timecodes = load_timecodes(acq_dir)

        return {
            "acquisition_id": acquisition_id,
            "path": str(acq_dir),
            "frame_count": len(frames),
            "frames": frames,
            "timecodes_available": timecodes is not None,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error fetching acquisition %s: %s", acquisition_id, e)
        raise HTTPException(status_code=500, detail="Failed to fetch acquisition")


@router.get("/stats")
async def bonestore_stats() -> dict[str, Any]:
    """Get BoneStore statistics (storage, acquisition counts).

    Returns:
        BoneStore stats with acquisition breakdown by bone type.

    Raises:
        HTTPException: If stat collection fails.
    """
    try:
        acquisitions = list_acquisitions()

        # Group by bone type
        by_bone: dict[str, int] = {}
        for acq in acquisitions:
            bone = acq.get("bone_type", "unknown")
            by_bone[bone] = by_bone.get(bone, 0) + 1

        # Count with/without timecodes
        with_tc = sum(1 for a in acquisitions if a.get("has_timecodes"))
        total_frames = sum(a.get("frame_count", 0) for a in acquisitions)

        return {
            "total_acquisitions": len(acquisitions),
            "total_frames": total_frames,
            "acquisitions_by_bone_type": by_bone,
            "acquisitions_with_timecodes": with_tc,
            "acquisitions_without_timecodes": len(acquisitions) - with_tc,
        }
    except Exception as e:
        logger.error("Error collecting BoneStore stats: %s", e)
        raise HTTPException(status_code=500, detail="Failed to collect statistics")
