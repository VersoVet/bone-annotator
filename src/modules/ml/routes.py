"""FastAPI routes for ML operations (datasets, training).

Provides endpoints for dataset export, training job management,
and inference operations.
"""

import logging
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException

from .dataset.service import delete_dataset, export_to_yolo, get_dataset_stats
from .training.service import cancel_training, get_training_status, list_training_jobs

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/ml", tags=["ml"])


# ========== Dataset Endpoints ==========


@router.post("/dataset/export")
async def export_dataset(
    acquisitions: list[str],
    output_dir: str | None = None,
    train_ratio: float = 0.7,
    val_ratio: float = 0.2,
) -> dict[str, Any]:
    """Export annotations to YOLO dataset format.

    Args:
        acquisitions: List of acquisition IDs to export.
        output_dir: Optional output directory path.
        train_ratio: Training split ratio (default 0.7).
        val_ratio: Validation split ratio (default 0.2).

    Returns:
        Dataset export result with paths and statistics.

    Raises:
        HTTPException: If export fails.
    """
    try:
        result = await export_to_yolo(
            acquisitions=acquisitions,
            output_dir=output_dir,
            train_ratio=train_ratio,
            val_ratio=val_ratio,
        )

        if result.get("status") == "error":
            raise HTTPException(status_code=400, detail=result.get("message"))

        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Error exporting dataset: %s", e)
        raise HTTPException(status_code=500, detail="Failed to export dataset")


@router.get("/dataset/{dataset_id}/stats")
async def get_dataset_statistics(dataset_id: str) -> dict[str, Any]:
    """Get statistics for a dataset.

    Args:
        dataset_id: Dataset identifier or path suffix.

    Returns:
        Dataset statistics with split information.

    Raises:
        HTTPException: If dataset not found.
    """
    try:
        # Resolve dataset path
        dataset_path = Path("data/datasets") / dataset_id
        if not dataset_path.exists():
            # Try as full path
            dataset_path = Path(dataset_id)

        result = await get_dataset_stats(dataset_path)

        if result.get("status") == "error":
            raise HTTPException(status_code=404, detail=result.get("message"))

        return result
    except Exception as e:
        logger.error("Error fetching dataset stats: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch statistics")


@router.delete("/dataset/{dataset_id}")
async def delete_dataset_endpoint(dataset_id: str) -> dict[str, Any]:
    """Delete a dataset.

    Args:
        dataset_id: Dataset identifier or path suffix.

    Returns:
        Deletion status.

    Raises:
        HTTPException: If deletion fails.
    """
    try:
        # Resolve dataset path
        dataset_path = Path("data/datasets") / dataset_id
        if not dataset_path.exists():
            # Try as full path
            dataset_path = Path(dataset_id)

        result = await delete_dataset(dataset_path)

        if result.get("status") == "error":
            raise HTTPException(status_code=500, detail=result.get("message"))

        return result
    except Exception as e:
        logger.error("Error deleting dataset: %s", e)
        raise HTTPException(status_code=500, detail="Failed to delete dataset")


# ========== Training Endpoints ==========


@router.get("/training/status")
async def training_status(job_id: str | None = None) -> dict[str, Any]:
    """Get training job status.

    Args:
        job_id: Optional specific job ID to query.

    Returns:
        Training job status or list of all active jobs.
    """
    try:
        result = await get_training_status(job_id)
        return result
    except Exception as e:
        logger.error("Error fetching training status: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch training status")


@router.get("/training/jobs")
async def list_jobs(limit: int = 50) -> dict[str, Any]:
    """List training jobs.

    Args:
        limit: Maximum jobs to return (default 50).

    Returns:
        List of training jobs with metadata.
    """
    try:
        result = await list_training_jobs(limit)
        return result
    except Exception as e:
        logger.error("Error listing training jobs: %s", e)
        raise HTTPException(status_code=500, detail="Failed to list training jobs")


@router.post("/training/{job_id}/cancel")
async def cancel_job(job_id: str) -> dict[str, Any]:
    """Cancel a training job.

    Args:
        job_id: Job ID to cancel.

    Returns:
        Cancellation status.

    Raises:
        HTTPException: If cancellation fails.
    """
    try:
        success = await cancel_training(job_id)

        if not success:
            raise HTTPException(status_code=400, detail="Failed to cancel job")

        return {"status": "cancelled", "job_id": job_id}
    except Exception as e:
        logger.error("Error cancelling training job: %s", e)
        raise HTTPException(status_code=500, detail="Failed to cancel job")
