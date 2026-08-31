"""Remote preprocessing client — delegates batch processing to Glia."""

import asyncio
import logging
from collections.abc import Callable
from typing import Any

import httpx

logger = logging.getLogger(__name__)


async def prepare_remote(
    config: dict[str, Any],
    acquisition_path: str,
    pipeline_preset: str,
    output_dir: str,
    bone_type: str,
    on_progress: Callable[[int, int], None] | None = None,
    crop_params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Submit preprocessing to remote service and poll until done.

    Args:
        config: Preprocessing config (host, port, workers, timeout).
        acquisition_path: Path to raw/ directory with .b2nd files.
        pipeline_preset: Pipeline context name.
        output_dir: Shared NFS output directory for PNG files.
        bone_type: Bone type for anatomy-aware processing.
        on_progress: Optional callback(current, total).
        crop_params: Optional crop bbox from parent task.

    Returns:
        Result dict with frame_count, duration_seconds, pipeline_config.

    Raises:
        httpx.ConnectError: If remote service unreachable.
        httpx.TimeoutException: If processing exceeds timeout.
        RuntimeError: If remote job fails.
    """
    host = config["remote_host"]
    port = config["remote_port"]
    timeout = config["timeout_seconds"]
    base_url = f"http://{host}:{port}"

    async with httpx.AsyncClient(timeout=httpx.Timeout(timeout)) as client:
        # Submit job
        payload: dict[str, Any] = {
            "acquisition_path": acquisition_path,
            "pipeline_preset": pipeline_preset,
            "output_dir": output_dir,
            "bone_type": bone_type,
            "n_workers": config.get("n_workers", 12),
        }
        if crop_params:
            payload["crop"] = {
                "bbox": crop_params["bbox"],
                "padding_percent": crop_params.get("padding_percent", 10),
            }
        resp = await client.post(f"{base_url}/api/preprocess", json=payload)
        resp.raise_for_status()
        job = resp.json()
        job_id = job["job_id"]
        logger.info("Remote job %s submitted (%d frames)", job_id, job.get("total_frames", 0))

        # Poll until done
        while True:
            await asyncio.sleep(2.0)
            status_resp = await client.get(f"{base_url}/api/preprocess/{job_id}/status")
            status = status_resp.json()

            if on_progress and status.get("total", 0) > 0:
                on_progress(status["progress"], status["total"])

            if status["status"] == "completed":
                logger.info("Remote job %s completed", job_id)
                return status.get("result", {})

            if status["status"] == "failed":
                error = status.get("error", "Unknown error")
                raise RuntimeError(f"Remote preprocessing failed: {error}")
