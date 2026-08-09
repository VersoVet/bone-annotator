"""ML training service — YOLOv8 training orchestration via ml-compute.

Manages model training runs through Ray Jobs API on ml-compute service.
"""

import asyncio
import logging
from typing import Any

import httpx

logger = logging.getLogger(__name__)

# ml-compute Ray Jobs API endpoint
ML_COMPUTE_URL = "http://10.0.0.44:9469/api"
_active_jobs: dict[str, dict[str, Any]] = {}


async def start_training(req: Any) -> dict[str, Any]:
    """Submit YOLOv8 training job to ml-compute Ray Jobs.

    Args:
        req: TrainRequest with dataset, model, epochs, etc.

    Returns:
        Dict with job ID and status.
    """
    try:
        job_name = req.name or f"{req.task}_{req.model_base.replace('.pt', '')}"

        # Prepare training config for Ray Job
        training_config = {
            "task": req.task,
            "model_base": req.model_base,
            "dataset_path": req.dataset_path,
            "epochs": req.epochs,
            "imgsz": getattr(req, "imgsz", 640),
            "batch": getattr(req, "batch", 16),
        }

        # Submit to ml-compute
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{ML_COMPUTE_URL}/jobs/submit",
                json={
                    "name": job_name,
                    "job_type": "training",
                    "config": training_config,
                    "timeout_seconds": 3600,
                },
                timeout=30.0,
            )

            if response.status_code in (200, 201):
                job_data = response.json()
                job_id = job_data.get("job_id")
                _active_jobs[job_id] = {
                    "name": job_name,
                    "job_id": job_id,
                    "status": "submitted",
                    "epochs": req.epochs,
                    "submitted_at": job_data.get("submitted_at"),
                }
                logger.info("Training job submitted: %s (ID: %s)", job_name, job_id)
                return {"status": "submitted", "job_id": job_id, "job_name": job_name}

            logger.error("Failed to submit job: %s", response.status_code)
            return {"status": "error", "message": "Failed to submit training job"}
    except Exception as e:
        logger.error("Error submitting training job: %s", e)
        return {"status": "error", "message": str(e)}


async def get_training_status(job_id: str | None = None) -> dict[str, Any]:
    """Get training job status from ml-compute.

    Args:
        job_id: Optional job ID. If None, returns all active jobs.

    Returns:
        Dict with job status(es).
    """
    try:
        async with httpx.AsyncClient() as client:
            if job_id:
                # Get single job status
                response = await client.get(f"{ML_COMPUTE_URL}/jobs/{job_id}", timeout=10.0)
                if response.status_code == 200:
                    job_data = response.json()
                    _active_jobs[job_id] = job_data
                    return job_data
                return {"status": "not_found", "job_id": job_id}
            else:
                # Get all active jobs
                response = await client.get(f"{ML_COMPUTE_URL}/jobs", timeout=10.0)
                if response.status_code == 200:
                    jobs = response.json().get("jobs", [])
                    # Update cache
                    for job in jobs:
                        _active_jobs[job.get("job_id", "")] = job
                    return {"jobs": jobs, "total": len(jobs)}
                return {"jobs": [], "total": 0}
    except Exception as e:
        logger.error("Error fetching training status: %s", e)
        return {"status": "error", "message": str(e)}


async def cancel_training(job_id: str) -> bool:
    """Cancel an active training job.

    Args:
        job_id: Job ID to cancel.

    Returns:
        True if cancellation successful.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{ML_COMPUTE_URL}/jobs/{job_id}/cancel",
                timeout=10.0,
            )
            if response.status_code == 200:
                logger.info("Training job cancelled: %s", job_id)
                if job_id in _active_jobs:
                    _active_jobs[job_id]["status"] = "cancelled"
                return True
            return False
    except Exception as e:
        logger.error("Error cancelling training job: %s", e)
        return False


async def get_job_metrics(job_id: str) -> dict[str, Any]:
    """Get training metrics for a job.

    Args:
        job_id: Job ID.

    Returns:
        Dict with training metrics (loss, accuracy, etc.).
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{ML_COMPUTE_URL}/jobs/{job_id}/metrics",
                timeout=10.0,
            )
            if response.status_code == 200:
                return response.json()
            return {}
    except Exception as e:
        logger.error("Error fetching job metrics: %s", e)
        return {}


async def list_training_jobs(limit: int = 50) -> dict[str, Any]:
    """List training jobs from ml-compute.

    Args:
        limit: Max jobs to return.

    Returns:
        Dict with jobs list.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{ML_COMPUTE_URL}/jobs?limit={limit}&job_type=training",
                timeout=10.0,
            )
            if response.status_code == 200:
                return response.json()
            return {"jobs": [], "total": 0}
    except Exception as e:
        logger.error("Error listing training jobs: %s", e)
        return {"jobs": [], "total": 0}


async def poll_job_status(job_id: str, interval: float = 5.0, max_wait: float = 3600.0) -> dict[str, Any]:
    """Poll job status until completion.

    Args:
        job_id: Job ID to poll.
        interval: Polling interval in seconds.
        max_wait: Max wait time in seconds.

    Returns:
        Final job status.
    """
    try:
        elapsed = 0.0
        while elapsed < max_wait:
            status = await get_training_status(job_id)
            state = status.get("status", "unknown")

            if state in ("completed", "failed", "cancelled"):
                return status

            await asyncio.sleep(interval)
            elapsed += interval

        logger.warning("Job polling timeout for %s after %.0f seconds", job_id, max_wait)
        return {"status": "timeout", "job_id": job_id}
    except Exception as e:
        logger.error("Error polling job status: %s", e)
        return {"status": "error", "job_id": job_id, "message": str(e)}
