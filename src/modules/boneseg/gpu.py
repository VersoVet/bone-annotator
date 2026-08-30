"""GPU availability checks for BoneSeg workloads."""

import logging
from typing import Any

import httpx

from src.config import get_bone_ml_config, get_ml_compute_config

from .models import GpuStatus

logger = logging.getLogger(__name__)


async def check_gpu_available() -> GpuStatus:
    """Check whether the shared GPU can accept a new BoneSeg job.

    Returns:
        GpuStatus with availability and blocking reasons.
    """
    ml_config = get_bone_ml_config()
    compute_config = get_ml_compute_config()
    boneseg_running = False
    ml_jobs = 0

    try:
        async with httpx.AsyncClient() as client:
            history_resp = await client.get(
                f"{ml_config['base_url']}/api/boneseg/train/history",
                timeout=10.0,
            )
            if history_resp.status_code == 200:
                runs = history_resp.json()
                items: list[dict[str, Any]] = []
                if isinstance(runs, list):
                    items = [r for r in runs if isinstance(r, dict)]
                    boneseg_running = any(r.get("status") == "running" for r in items)
                elif isinstance(runs, dict):
                    raw_items = runs.get("runs", runs.get("history", []))
                    items = [r for r in raw_items if isinstance(r, dict)] if isinstance(raw_items, list) else []
                    boneseg_running = any(r.get("status") == "running" for r in items)

            jobs_resp = await client.get(
                f"http://{compute_config['host']}:{compute_config['port']}/api/jobs",
                params={"status": "running"},
                timeout=10.0,
            )
            if jobs_resp.status_code == 200:
                jobs_data = jobs_resp.json()
                job_list: list[Any] = []
                if isinstance(jobs_data, list):
                    job_list = jobs_data
                elif isinstance(jobs_data, dict):
                    raw_jobs = jobs_data.get("jobs", jobs_data.get("results", []))
                    job_list = raw_jobs if isinstance(raw_jobs, list) else []
                ml_jobs = len(job_list)
    except Exception as e:
        logger.warning("GPU status check failed: %s", e)
        return GpuStatus(available=False, reason=f"check_failed: {e}")

    if boneseg_running:
        return GpuStatus(
            available=False,
            boneseg_running=True,
            ml_compute_jobs=ml_jobs,
            reason="boneseg_training_running",
        )
    if ml_jobs > 0:
        return GpuStatus(
            available=False,
            boneseg_running=False,
            ml_compute_jobs=ml_jobs,
            reason="ml_compute_jobs_running",
        )
    return GpuStatus(available=True, boneseg_running=False, ml_compute_jobs=0)
