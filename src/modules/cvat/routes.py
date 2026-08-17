"""FastAPI routes for CVAT integration.

Provides endpoints for task management, annotation synchronization,
and CVAT workflow orchestration.
"""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .service import get_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/cvat", tags=["cvat"])


class TaskCreateRequest(BaseModel):
    """Request to create a CVAT task."""

    name: str
    project_id: int | None = None


class AnnotationPushRequest(BaseModel):
    """Request to push annotations to CVAT."""

    task_id: int
    annotations: dict[str, Any]


class AnnotationSyncRequest(BaseModel):
    """Request to synchronize annotations."""

    task_id: int
    local_annotations: dict[str, Any]
    strategy: str = "local_wins"


@router.post("/connect")
async def connect_cvat() -> dict[str, Any]:
    """Connect and authenticate with CVAT server.

    Returns:
        Connection status.

    Raises:
        HTTPException: If connection fails.
    """
    try:
        service = get_service()
        authenticated = await service.connect()

        if not authenticated:
            raise HTTPException(status_code=503, detail="CVAT authentication failed")

        return {
            "status": "connected",
            "authenticated": authenticated,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error connecting to CVAT: %s", e)
        raise HTTPException(status_code=503, detail="Failed to connect to CVAT")


@router.get("/tasks")
async def list_tasks(limit: int = 100) -> dict[str, Any]:
    """List all CVAT tasks.

    Args:
        limit: Maximum number of tasks (default 100).

    Returns:
        List of tasks with metadata.

    Raises:
        HTTPException: If task retrieval fails.
    """
    try:
        if limit > 500:
            limit = 500

        service = get_service()
        tasks = await service.get_tasks(limit)

        return {
            "status": "success",
            "total": len(tasks),
            "limit": limit,
            "tasks": tasks,
        }
    except Exception as e:
        logger.error("Error listing CVAT tasks: %s", e)
        raise HTTPException(status_code=500, detail="Failed to list tasks")


@router.get("/tasks/{task_id}")
async def get_task(task_id: int) -> dict[str, Any]:
    """Get details of a specific CVAT task.

    Args:
        task_id: Task ID.

    Returns:
        Task details and metadata.

    Raises:
        HTTPException: If task not found or retrieval fails.
    """
    try:
        service = get_service()
        task = await service.get_task(task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        return {
            "status": "success",
            "task": task,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error retrieving task %d: %s", task_id, e)
        raise HTTPException(status_code=500, detail="Failed to retrieve task")


@router.post("/tasks")
async def create_task(request: TaskCreateRequest) -> dict[str, Any]:
    """Create a new CVAT task.

    Args:
        request: Task creation parameters.

    Returns:
        Created task information.

    Raises:
        HTTPException: If task creation fails.
    """
    try:
        if not request.name:
            raise HTTPException(status_code=400, detail="Task name is required")

        service = get_service()
        task = await service.create_task(request.name, request.project_id)

        if not task:
            raise HTTPException(status_code=503, detail="Failed to create task on CVAT")

        return {
            "status": "created",
            "task": task,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error creating CVAT task: %s", e)
        raise HTTPException(status_code=500, detail="Failed to create task")


@router.get("/tasks/{task_id}/annotations")
async def pull_annotations(task_id: int) -> dict[str, Any]:
    """Pull annotations from a CVAT task.

    Args:
        task_id: Task ID.

    Returns:
        Annotations in internal format.

    Raises:
        HTTPException: If pull fails.
    """
    try:
        service = get_service()
        annotations = await service.pull_annotations(task_id)

        if annotations is None:
            raise HTTPException(status_code=404, detail="Task not found or no annotations")

        return {
            "status": "success",
            "task_id": task_id,
            "annotations": annotations,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error pulling annotations from task %d: %s", task_id, e)
        raise HTTPException(status_code=500, detail="Failed to pull annotations")


@router.post("/tasks/{task_id}/annotations")
async def push_annotations(task_id: int, request: AnnotationPushRequest) -> dict[str, Any]:
    """Push annotations to a CVAT task.

    Args:
        task_id: Task ID.
        request: Annotations to push.

    Returns:
        Confirmation of push operation.

    Raises:
        HTTPException: If push fails.
    """
    try:
        if task_id != request.task_id:
            raise HTTPException(status_code=400, detail="Task ID mismatch")

        if not request.annotations:
            raise HTTPException(status_code=400, detail="Annotations cannot be empty")

        service = get_service()
        success = await service.push_annotations(task_id, request.annotations)

        if not success:
            raise HTTPException(status_code=503, detail="Failed to push annotations to CVAT")

        return {
            "status": "pushed",
            "task_id": task_id,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error pushing annotations to task %d: %s", task_id, e)
        raise HTTPException(status_code=500, detail="Failed to push annotations")


@router.post("/tasks/{task_id}/sync")
async def sync_annotations(task_id: int, request: AnnotationSyncRequest) -> dict[str, Any]:
    """Synchronize annotations bidirectionally.

    Args:
        task_id: Task ID.
        request: Local annotations and sync strategy.

    Returns:
        Resolved annotations after synchronization.

    Raises:
        HTTPException: If sync fails.
    """
    try:
        if task_id != request.task_id:
            raise HTTPException(status_code=400, detail="Task ID mismatch")

        if request.strategy not in ("local_wins", "remote_wins", "merge"):
            raise HTTPException(status_code=400, detail="Invalid sync strategy")

        service = get_service()
        resolved = await service.sync_annotations(
            task_id,
            request.local_annotations,
            request.strategy,
        )

        if resolved is None:
            raise HTTPException(status_code=503, detail="Sync failed")

        return {
            "status": "synced",
            "task_id": task_id,
            "strategy": request.strategy,
            "annotations": resolved,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error syncing annotations for task %d: %s", task_id, e)
        raise HTTPException(status_code=500, detail="Failed to sync annotations")


@router.get("/users")
async def list_cvat_users() -> dict[str, Any]:
    """List all CVAT users for assignee selection."""
    try:
        service = get_service()
        await service.connect()
        users = await service.client.get_users()
        return {
            "status": "ok",
            "users": [{"username": u.get("username", ""), "id": u.get("id")} for u in users],
        }
    except Exception as e:
        logger.error("Error listing CVAT users: %s", e)
        raise HTTPException(status_code=500, detail="Failed to list CVAT users")


@router.get("/status")
async def cvat_status() -> dict[str, Any]:
    """Get CVAT service status.

    Returns:
        Service health and connection status.

    Raises:
        HTTPException: If status check fails.
    """
    try:
        service = get_service()
        status = await service.status()

        return {
            "status": "ready",
            "service": "cvat",
            "components": status,
        }
    except Exception as e:
        logger.error("Error fetching CVAT status: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch CVAT status")
