"""FastAPI routes for annotation workflow orchestration.

Manages task creation, CVAT sync, validation, and ML pre-annotation.
"""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException, Query

from .models import CreateTaskRequest, ValidateRequest
from .service import get_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/annotation", tags=["annotation"])


@router.post("/task")
async def create_annotation_task(request: CreateTaskRequest) -> dict[str, Any]:
    """Create a new annotation task with CVAT integration.

    Prepares dataset, creates CVAT task, configures labels,
    and optionally triggers ML pre-annotations.

    Args:
        request: Task creation parameters.

    Returns:
        Task info with CVAT URL.

    Raises:
        HTTPException: If creation fails.
    """
    try:
        service = get_service()
        result = await service.create_task(request)
        return {"status": "created", "task": result.model_dump()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Error creating annotation task: %s", e)
        raise HTTPException(status_code=500, detail="Failed to create task")


@router.get("/task/{task_id}")
async def get_annotation_task(task_id: int) -> dict[str, Any]:
    """Get annotation task status.

    Args:
        task_id: Internal task ID.

    Returns:
        Task status and metadata.

    Raises:
        HTTPException: If task not found.
    """
    service = get_service()
    result = await service.get_task(task_id)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return {"status": "ok", "task": result.model_dump()}


@router.get("/tasks")
async def list_annotation_tasks(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    status: str | None = Query(None, description="Filter by status"),
    bone_type: str | None = Query(None, description="Filter by bone type"),
) -> dict[str, Any]:
    """List annotation tasks with filtering.

    Args:
        limit: Max results.
        offset: Pagination offset.
        status: Optional status filter.
        bone_type: Optional bone type filter.

    Returns:
        Paginated task list.
    """
    try:
        service = get_service()
        result = await service.list_tasks(limit, offset, status, bone_type)
        return {"status": "ok", **result.model_dump()}
    except Exception as e:
        logger.error("Error listing tasks: %s", e)
        raise HTTPException(status_code=500, detail="Failed to list tasks")


@router.post("/sync/{task_id}")
async def sync_task_annotations(task_id: int) -> dict[str, Any]:
    """Sync annotations from CVAT back to PostgreSQL.

    Pulls annotations, identifies CVAT assignee as author,
    and stores in frame_annotations.

    Args:
        task_id: Internal task ID.

    Returns:
        Sync result with counts.

    Raises:
        HTTPException: If sync fails.
    """
    try:
        service = get_service()
        result = await service.sync_task(task_id)
        return {"status": "synced", **result.model_dump()}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error("Error syncing task %d: %s", task_id, e)
        raise HTTPException(status_code=500, detail="Failed to sync annotations")


@router.post("/validate/{task_id}")
async def validate_task(task_id: int, request: ValidateRequest) -> dict[str, Any]:
    """Validate or reject a task's annotations.

    Args:
        task_id: Internal task ID.
        request: Validation decision and notes.

    Returns:
        Updated task status.

    Raises:
        HTTPException: If validation fails.
    """
    try:
        if request.decision not in ("validated", "rejected"):
            raise HTTPException(status_code=400, detail="Decision must be 'validated' or 'rejected'")
        service = get_service()
        result = await service.validate_task(task_id, request)
        return {"status": request.decision, "task": result.model_dump()}
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error("Error validating task %d: %s", task_id, e)
        raise HTTPException(status_code=500, detail="Failed to validate task")


@router.post("/pre-annotate/{task_id}")
async def request_pre_annotation(task_id: int) -> dict[str, Any]:
    """Request ML pre-annotations from bone-ml for a task.

    Calls bone-ml /api/cvat/annotate to run YOLO inference
    and push predictions to the CVAT task.

    Args:
        task_id: Internal task ID.

    Returns:
        Pre-annotation request status.

    Raises:
        HTTPException: If request fails.
    """
    try:
        service = get_service()
        result = await service.request_pre_annotation(task_id)
        return {"status": "requested", **result.model_dump()}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error("Error requesting pre-annotation for task %d: %s", task_id, e)
        raise HTTPException(status_code=500, detail="Failed to request pre-annotation")


@router.post("/export")
async def export_annotations(
    task_ids: list[int] | None = None,
    export_format: str = "yolo",
) -> dict[str, Any]:
    """Export validated annotations to training format.

    Args:
        task_ids: Task IDs to export (None = all validated).
        export_format: Export format (yolo).

    Returns:
        Export result with dataset path.

    Raises:
        HTTPException: If export fails.
    """
    try:
        service = get_service()
        # Get acquisition IDs from validated tasks
        result = await service.list_tasks(limit=1000, status="validated")
        acq_ids = [t["acquisition_id"] for t in result.tasks]

        if task_ids:
            filtered = []
            for tid in task_ids:
                task = await service.get_task(tid)
                if task:
                    filtered.append(task.acquisition_id)
            acq_ids = filtered

        if not acq_ids:
            return {"status": "warning", "message": "No validated tasks to export"}

        from src.modules.ml.dataset.service import export_to_yolo

        export = await export_to_yolo(acq_ids)
        return {"status": "ok", "export": export}
    except Exception as e:
        logger.error("Error exporting annotations: %s", e)
        raise HTTPException(status_code=500, detail="Failed to export")
