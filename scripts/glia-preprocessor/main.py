"""Bone preprocessing microservice — runs on OnyxGlia (10.0.0.8).

Accepts preprocessing requests from bone-annotator, processes frames
in parallel using imaging-sdk, and writes output to shared NFS.
"""

import asyncio
import logging
import time
import uuid
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from worker import process_acquisition

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bone-preprocessor")

app = FastAPI(
    title="bone-preprocessor",
    description="Multi-threaded frame preprocessing for bone-annotator",
    version="0.1.0",
)

# In-memory job tracking
_jobs: dict[str, dict[str, Any]] = {}

# Defaults
DEFAULT_PIPELINE_DIR = "/opt/onyx/imaging-sdk/pipelines/users"
DEFAULT_N_WORKERS = 12


class PreprocessRequest(BaseModel):
    """Request to preprocess an acquisition."""

    acquisition_path: str = Field(..., description="Path to raw/ directory with .b2nd files")
    pipeline_preset: str = Field(default="os_nu_medsam_user", description="Pipeline context name")
    output_dir: str = Field(..., description="Output directory for PNG files")
    bone_type: str = Field(default="humerus", description="Bone type")
    n_workers: int = Field(default=DEFAULT_N_WORKERS, ge=1, le=24)
    pipeline_dir: str = Field(default=DEFAULT_PIPELINE_DIR)


class JobStatus(BaseModel):
    """Job status response."""

    job_id: str
    status: str
    progress: int = 0
    total: int = 0
    percent: int = 0
    result: dict[str, Any] | None = None
    error: str | None = None


@app.get("/health")
async def health() -> dict[str, Any]:
    """Service health check."""
    import os

    return {
        "status": "ok",
        "service": "bone-preprocessor",
        "version": "0.1.0",
        "hostname": os.uname().nodename,
        "default_workers": DEFAULT_N_WORKERS,
        "pipeline_dir": DEFAULT_PIPELINE_DIR,
        "pipelines_accessible": Path(DEFAULT_PIPELINE_DIR).exists(),
        "bonestore_accessible": Path("/mnt/bonestore").is_dir()
        and any(Path("/mnt/bonestore").iterdir()),
    }


@app.post("/api/preprocess")
async def preprocess(request: PreprocessRequest) -> dict[str, Any]:
    """Start preprocessing job in background.

    Returns immediately with job_id for progress polling.
    """
    # Validate paths
    raw_path = Path(request.acquisition_path)
    if not raw_path.exists():
        raise HTTPException(status_code=400, detail=f"Path not found: {request.acquisition_path}")

    b2nd_files = list(raw_path.glob("*.b2nd"))
    if not b2nd_files:
        raise HTTPException(status_code=400, detail=f"No .b2nd files in {request.acquisition_path}")

    job_id = str(uuid.uuid4())[:8]
    _jobs[job_id] = {
        "status": "running",
        "progress": 0,
        "total": len(b2nd_files),
        "percent": 0,
        "started_at": time.time(),
        "result": None,
        "error": None,
    }

    asyncio.create_task(_run_job(job_id, request))
    logger.info("Job %s started: %d frames, %d workers", job_id, len(b2nd_files), request.n_workers)

    return {"job_id": job_id, "total_frames": len(b2nd_files), "status": "running"}


async def _run_job(job_id: str, request: PreprocessRequest) -> None:
    """Run preprocessing in a thread pool."""

    def _on_progress(current: int, total: int) -> None:
        _jobs[job_id]["progress"] = current
        _jobs[job_id]["total"] = total
        _jobs[job_id]["percent"] = int(100 * current / max(total, 1))

    try:
        result = await asyncio.to_thread(
            process_acquisition,
            raw_dir=request.acquisition_path,
            pipeline_preset=request.pipeline_preset,
            pipeline_dir=request.pipeline_dir,
            output_dir=request.output_dir,
            bone_type=request.bone_type,
            n_workers=request.n_workers,
            on_progress=_on_progress,
        )
        _jobs[job_id]["status"] = "completed"
        _jobs[job_id]["percent"] = 100
        _jobs[job_id]["result"] = result
        logger.info("Job %s completed: %d frames in %.1fs",
                     job_id, result["frame_count"], result["duration_seconds"])
    except Exception as e:
        _jobs[job_id]["status"] = "failed"
        _jobs[job_id]["error"] = str(e)[:500]
        logger.error("Job %s failed: %s", job_id, e, exc_info=True)


@app.get("/api/preprocess/{job_id}/status")
async def job_status(job_id: str) -> JobStatus:
    """Get job progress."""
    if job_id not in _jobs:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")
    job = _jobs[job_id]
    return JobStatus(
        job_id=job_id,
        status=job["status"],
        progress=job["progress"],
        total=job["total"],
        percent=job["percent"],
        result=job.get("result"),
        error=job.get("error"),
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9480, log_level="info")
