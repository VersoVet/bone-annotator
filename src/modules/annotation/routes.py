"""FastAPI routes for annotation workflow orchestration.

Manages task creation, CVAT sync, validation, and ML pre-annotation.
"""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException, Query

from .exceptions import ActiveTaskExistsError
from .models import CreateTaskRequest
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
    except ActiveTaskExistsError as e:
        existing = e.existing
        existing_task = await service.get_task(existing["id"])
        raise HTTPException(
            status_code=409,
            detail={
                "status": "active_task_exists",
                "error": "active_task_exists",
                "existing_task_id": existing["id"],
                "task_status": existing.get("status"),
                "hint": f"Utilisez POST /api/annotation/re-annotate/{existing['id']} pour re-annoter",
                "task": existing_task.model_dump() if existing_task else existing,
            },
        )
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


@router.delete("/task/{task_id}")
async def delete_annotation_task(task_id: int) -> dict[str, Any]:
    """Delete an annotation task and its CVAT counterpart.

    Args:
        task_id: Internal task ID.

    Returns:
        Deletion status.

    Raises:
        HTTPException: If task not found.
    """
    try:
        service = get_service()
        result = await service.delete_task(task_id)
        return {"status": "deleted", **result}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error("Error deleting task %d: %s", task_id, e)
        raise HTTPException(status_code=500, detail="Failed to delete task")


@router.delete("/tasks/failed")
async def delete_failed_tasks() -> dict[str, Any]:
    """Delete all annotation tasks with status ``failed``.

    Useful from the dashboard to clean orphaned/broken campaigns.
    Does not delete validated or in-progress tasks.

    Returns:
        Counts of deleted tasks.
    """
    service = get_service()
    listing = await service.list_tasks(limit=500, status="failed")
    deleted: list[int] = []
    errors: list[dict[str, Any]] = []
    for task in listing.tasks:
        tid = int(task["id"])
        try:
            await service.delete_task(tid)
            deleted.append(tid)
        except Exception as e:
            errors.append({"id": tid, "error": str(e)})
    return {"status": "ok", "deleted": deleted, "count": len(deleted), "errors": errors}


@router.get("/task/{task_id}/cvat-exists")
async def check_cvat_exists(task_id: int) -> dict[str, Any]:
    """Check if the CVAT task still exists for a given task.

    Args:
        task_id: Internal task ID.

    Returns:
        CVAT existence status.

    Raises:
        HTTPException: 404 if task not found or has no CVAT task.
    """
    service = get_service()
    exists = await service.check_cvat_exists(task_id)
    if exists is None:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found or no CVAT task")
    return {"task_id": task_id, "cvat_exists": exists}


def _profiles_config_path() -> Any:
    """Return path to the active annotation-profiles YAML."""
    from pathlib import Path

    from src.config import _CFG

    config_dir = Path(__file__).parent.parent.parent.parent / "config"
    filename = _CFG.get("annotation", {}).get("profile_schema", "annotation-profiles.yaml")
    return config_dir / filename


@router.get("/profiles/schema")
async def get_profiles_schema() -> dict[str, Any]:
    """Return annotation profiles from active YAML config."""
    import yaml

    config_path = _profiles_config_path()
    try:
        with open(config_path) as f:
            data = yaml.safe_load(f)
        return {"profiles": data.get("profiles", []), "schema_file": config_path.name}
    except Exception as e:
        logger.error("Failed to load profiles: %s", e)
        return {"profiles": [], "schema_file": config_path.name}


@router.put("/profiles/schema")
async def save_profiles_schema(profiles: list[dict[str, Any]]) -> dict[str, Any]:
    """Save annotation profiles to active YAML config."""
    import yaml

    config_path = _profiles_config_path()
    try:
        data = {"profiles": profiles}
        with open(config_path, "w") as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        logger.info("Profiles schema saved: %d profiles to %s", len(profiles), config_path.name)
        return {"status": "saved", "count": len(profiles), "schema_file": config_path.name}
    except Exception as e:
        logger.error("Failed to save profiles: %s", e)
        raise HTTPException(status_code=500, detail=f"Failed to save: {e}")


@router.get("/profiles/schemas")
async def list_profile_schemas() -> dict[str, Any]:
    """List available profile schema files in config/."""
    from pathlib import Path

    config_dir = Path(__file__).parent.parent.parent.parent / "config"
    files = sorted(config_dir.glob("*-profiles*.yaml")) + sorted(config_dir.glob("profiles-*.yaml"))
    active = _profiles_config_path().name
    return {
        "schemas": [{"name": f.name, "active": f.name == active} for f in files],
        "active": active,
    }


@router.get("/acquisition/{acquisition_id}/profiles")
async def get_acquisition_profiles(
    acquisition_id: str,
    bone_type: str = Query(..., description="Bone type"),
) -> dict[str, Any]:
    """Get profile status for an acquisition — which exist, which are missing."""

    import yaml

    service = get_service()

    # Load schema
    config_path = _profiles_config_path()
    try:
        with open(config_path) as f:
            schema_profiles = yaml.safe_load(f).get("profiles", [])
    except Exception:
        schema_profiles = []

    # Get existing profiles from DB
    existing = service.task_db.get_acquisition_profiles(acquisition_id, bone_type)
    existing_map = {p["profile_id"]: p for p in existing}

    # Check CVAT existence for each
    profiles = []
    for sp in schema_profiles:
        pid = sp["id"]
        ex = existing_map.get(pid)
        status = "missing"
        cvat_exists = None
        if ex:
            status = ex["status"]
            if ex.get("cvat_task_id"):
                try:
                    await service.cvat.authenticate()
                    cvat_exists = await service.cvat.task_exists(ex["cvat_task_id"])
                    if not cvat_exists:
                        status = "cvat_missing"
                except Exception:
                    pass
        profiles.append(
            {
                **sp,
                "status": status,
                "task_id": ex["task_id"] if ex else None,
                "cvat_task_id": ex["cvat_task_id"] if ex else None,
                "cvat_exists": cvat_exists,
            }
        )

    return {
        "acquisition_id": acquisition_id,
        "bone_type": bone_type,
        "profiles": profiles,
        "total": len(schema_profiles),
        "created": sum(1 for p in profiles if p["status"] not in ("missing", "cvat_missing")),
    }


@router.get("/acquisition-profile-counts")
async def get_acquisition_profile_counts() -> dict[str, Any]:
    """Get profile count per acquisition for dropdown display."""
    service = get_service()
    counts = service.task_db.get_acquisition_profile_counts()
    return {"counts": counts}


@router.get("/tasks")
async def list_annotation_tasks(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    status: str | None = Query(None, description="Filter by status"),
    bone_type: str | None = Query(None, description="Filter by bone type"),
    profile_id: str | None = Query(None, description="Filter by annotation profile"),
    region: str | None = Query(None, description="Filter by portion (proximal, distal, entire)"),
) -> dict[str, Any]:
    """List annotation tasks with filtering.

    Args:
        limit: Max results.
        offset: Pagination offset.
        status: Optional status filter.
        bone_type: Optional bone type filter.
        profile_id: Optional annotation profile filter.
        region: Optional portion filter.

    Returns:
        Paginated task list.

    Raises:
        HTTPException: 500 if listing fails.
    """
    try:
        service = get_service()
        result = await service.list_tasks(limit, offset, status, bone_type, profile_id, region)
        return {"status": "ok", **result.model_dump()}
    except Exception as e:
        logger.error("Error listing tasks: %s", e)
        raise HTTPException(status_code=500, detail="Failed to list tasks")
