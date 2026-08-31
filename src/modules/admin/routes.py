"""Admin operations — reset, tracking, and task lifecycle management."""

import asyncio
import logging
from typing import Any

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.config import get_bone_ml_config, get_dashboard_config, get_imaging_config, get_postgres_config
from src.core import __version__
from src.modules.annotation.service import get_service as get_annotation_service
from src.modules.storage.learning_db import create_learning_db

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/admin", tags=["admin"])


class ResetRequest(BaseModel):
    """Request to reset annotation data."""

    confirm: str = Field(..., description="Must be 'RESET' to confirm")
    include_annotations: bool = Field(default=True, description="Also delete frame_annotations")


@router.get("/settings")
async def get_settings() -> dict[str, Any]:
    """Return editable dashboard and imaging settings from YAML config."""
    return {
        "status": "ok",
        "version": __version__,
        "dashboard": get_dashboard_config(),
        "imaging": get_imaging_config(),
    }


@router.get("/tracking")
async def tracking_overview() -> dict[str, Any]:
    """Annotation tracking stats (local PG + bone-ml catalog when available)."""
    learning_db = create_learning_db(**get_postgres_config())
    local = learning_db.get_tracking_stats()
    catalog: dict[str, Any] = {}
    try:
        ml_config = get_bone_ml_config()
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                f"{ml_config['base_url']}/api/boneseg/catalog/stats",
                timeout=10.0,
            )
            if resp.status_code == 200:
                catalog = resp.json()
    except Exception as e:
        logger.debug("bone-ml catalog stats unavailable: %s", e)
        catalog = {"error": "bone-ml unavailable", "local_catalog_total": local.get("catalog_total", 0)}

    return {"status": "ok", "local": local, "catalog": catalog}


@router.post("/reset")
async def reset_annotations(request: ResetRequest) -> dict[str, Any]:
    """Reset annotation tasks and optionally stored annotations."""
    if request.confirm != "RESET":
        raise HTTPException(status_code=400, detail="confirm must be 'RESET'")
    learning_db = create_learning_db(**get_postgres_config())
    deleted = learning_db.reset_annotation_data(include_annotations=request.include_annotations)
    return {"status": "ok", **deleted}


@router.post("/task/{task_id}/cancel")
async def cancel_task(task_id: int) -> dict[str, Any]:
    """Cancel a stuck or failed task, allowing re-creation on same acquisition.

    Only tasks in preparing, uploading, or failed status can be cancelled.

    Args:
        task_id: Internal task ID.

    Returns:
        Updated task status.

    Raises:
        HTTPException: If task not found or not cancellable.
    """
    service = get_annotation_service()
    task = await service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    cancellable = {"preparing", "uploading", "failed"}
    if task.status not in cancellable:
        raise HTTPException(
            status_code=400,
            detail=f"Task {task_id} status '{task.status}' not cancellable (need {cancellable})",
        )
    service.task_db.update_task(task_id, status="failed", notes="Cancelled by user")
    return {"status": "cancelled", "task_id": task_id}


@router.post("/task/{task_id}/retry")
async def retry_task(task_id: int) -> dict[str, Any]:
    """Retry a failed task by re-launching background preparation.

    Resets the task to 'preparing' and starts dataset prep + CVAT upload.

    Args:
        task_id: Internal task ID.

    Returns:
        Updated task info.

    Raises:
        HTTPException: If task not found or not retryable.
    """
    service = get_annotation_service()
    task_row = service.task_db.get_task(task_id)
    if not task_row:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    if task_row.get("status") != "failed":
        raise HTTPException(
            status_code=400,
            detail=f"Task {task_id} status '{task_row.get('status')}' must be 'failed' to retry",
        )

    service.task_db.update_task(task_id, status="preparing", notes="Retrying...", cvat_task_id=None, cvat_url=None)

    from src.modules.annotation.background import prepare_and_upload
    from src.modules.annotation.models import CreateTaskRequest

    req = CreateTaskRequest(
        source_name=task_row.get("source_name", "bonestore"),
        acquisition_id=task_row["acquisition_id"],
        bone_type=task_row["bone_type"],
        region=task_row.get("region", "entire"),
        pipeline_preset=task_row.get("pipeline_preset"),
        pre_annotate=task_row.get("has_pre_annotations", False),
        assignee=task_row.get("assignee"),
    )
    asyncio.create_task(prepare_and_upload(task_id, req, service.task_db))
    logger.info("Task %d retried", task_id)

    result = await service.get_task(task_id)
    return {"status": "retrying", "task": result.model_dump() if result else {"id": task_id}}
