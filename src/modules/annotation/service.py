"""Annotation workflow service — orchestrates CVAT, labels, preparation, and storage."""

import asyncio
import logging
from typing import Any

from src.config import get_cvat_config, get_imaging_config, get_postgres_config
from src.modules.cvat.client import CVATClient
from src.modules.labels.service import get_labels_for_bone
from src.modules.sources.service import get_service as get_source_service
from src.modules.storage.task_db import AnnotationTaskDB, create_task_db

from .exceptions import ActiveTaskExistsError
from .models import (
    CreateTaskRequest,
    SyncResult,
    TaskListResponse,
    TaskProgress,
    TaskResponse,
    ValidateRequest,
)
from .workflow_ops import AnnotationWorkflowOps

logger = logging.getLogger(__name__)


def _build_task_progress(status: str, notes: str | None) -> TaskProgress | None:
    """Map DB status/notes to a TaskProgress for polling clients.

    Notes may embed a percentage as "[42%] Some detail".
    """
    if status in ("created", "annotating", "validated", "rejected"):
        return None
    step = status if status in ("preparing", "uploading", "failed") else "preparing"
    percent = 0
    detail = notes or ""
    if detail.startswith("[") and "%]" in detail:
        try:
            pct_str = detail[1 : detail.index("%]")]
            percent = int(pct_str)
            detail = detail[detail.index("%]") + 2 :].strip()
        except (ValueError, IndexError):
            pass
    return TaskProgress(step=step, detail=detail, percent=percent)


def _task_row_to_response(row: dict[str, Any]) -> TaskResponse:
    """Convert a DB task row to TaskResponse."""
    status = row.get("status", "unknown")
    return TaskResponse(
        id=row["id"],
        acquisition_id=row["acquisition_id"],
        cvat_task_id=row.get("cvat_task_id"),
        cvat_url=row.get("cvat_url"),
        status=status,
        bone_type=row["bone_type"],
        region=row.get("region", "entire"),
        frame_count=row.get("frame_count", 0),
        annotated_frames=row.get("annotated_frames", 0),
        author=row.get("author", "unknown"),
        assignee=row.get("assignee"),
        has_pre_annotations=row.get("has_pre_annotations", False),
        pipeline_preset=row.get("pipeline_preset"),
        dataset_path=row.get("dataset_path"),
        profile_id=row.get("profile_id"),
        objective=row.get("objective"),
        progress=_build_task_progress(status, row.get("notes")),
    )


class AnnotationWorkflowService(AnnotationWorkflowOps):
    """Orchestrates the complete annotation workflow."""

    def __init__(self) -> None:
        """Initialize workflow service with lazy-loaded dependencies."""
        self._cvat_client: CVATClient | None = None
        self._task_db: AnnotationTaskDB | None = None

    @property
    def cvat(self) -> CVATClient:
        """Lazy-loaded CVAT client."""
        if self._cvat_client is None:
            cfg = get_cvat_config()
            self._cvat_client = CVATClient(cfg["host"], cfg["port"], cfg["username"], cfg["password"])
        return self._cvat_client

    @property
    def task_db(self) -> AnnotationTaskDB:
        """Lazy-loaded task database."""
        if self._task_db is None:
            self._task_db = create_task_db(**get_postgres_config())
        return self._task_db

    async def create_task(self, request: CreateTaskRequest) -> TaskResponse:
        """Create annotation task asynchronously.

        Returns immediately with status="preparing". The actual dataset
        preparation and CVAT upload happen in background.
        """
        # Validate inputs synchronously
        source_svc = get_source_service()
        acq_path = source_svc.get_acquisition_path(request.source_name, request.acquisition_id)
        if acq_path is None:
            raise ValueError(f"Acquisition not found: {request.acquisition_id}")
        anatomy = get_labels_for_bone(request.bone_type)
        if not anatomy:
            raise ValueError(f"No labels for bone_type '{request.bone_type}' in label-generator")

        existing = await asyncio.to_thread(
            self.task_db.find_active_task,
            request.acquisition_id,
            request.bone_type,
            request.profile_id,
        )
        if existing:
            raise ActiveTaskExistsError(existing)

        pipeline = request.pipeline_preset or get_imaging_config()["default_treatment"]
        # Create DB entry immediately (status="preparing")
        task_id = await asyncio.to_thread(
            self.task_db.save_task,
            acquisition_id=request.acquisition_id,
            bone_type=request.bone_type,
            author=request.assignee or "system",
            source_name=request.source_name,
            region=request.region,
            assignee=request.assignee,
            pipeline_preset=pipeline,
            status="preparing",
            profile_id=request.profile_id,
            objective=request.objective,
            labels_filter=request.labels_filter,
            crop_from_task_id=request.crop_from_task_id,
        )

        # Launch background preparation
        from .background import prepare_and_upload

        asyncio.create_task(prepare_and_upload(task_id, request, self.task_db))
        logger.info("Task %d queued for preparation", task_id)

        return TaskResponse(
            id=task_id,
            acquisition_id=request.acquisition_id,
            status="preparing",
            bone_type=request.bone_type,
            region=request.region,
            author=request.assignee or "system",
            assignee=request.assignee,
            pipeline_preset=pipeline,
            cvat_task_id=None,
            cvat_url=None,
            dataset_path=None,
            profile_id=request.profile_id,
            objective=request.objective,
            progress=None,
        )

    async def get_task(self, task_id: int) -> TaskResponse | None:
        """Get task status from local DB."""
        t = self.task_db.get_task(task_id)
        if not t:
            return None
        return _task_row_to_response(t)

    async def delete_task(self, task_id: int) -> dict[str, Any]:
        """Delete a task and its CVAT counterpart.

        Args:
            task_id: Local annotation task ID to delete.

        Returns:
            Dict with deletion status and warnings.

        Raises:
            ValueError: If task not found.
        """
        task = self.task_db.get_task(task_id)
        if not task:
            raise ValueError(f"Task {task_id} not found")

        cvat_deleted = False
        cvat_warning = None
        cvat_task_id = task.get("cvat_task_id")

        if cvat_task_id:
            # Do not destroy a CVAT task still referenced by another annotation task.
            others = [
                t
                for t in (await self.list_tasks(limit=500)).tasks
                if t.get("cvat_task_id") == cvat_task_id and int(t["id"]) != task_id
            ]
            if others:
                cvat_warning = f"CVAT #{cvat_task_id} kept (still used by task {[t['id'] for t in others]})"
            else:
                try:
                    await self.cvat.authenticate()
                    cvat_deleted = await self.cvat.delete_task(cvat_task_id)
                except Exception as e:
                    cvat_warning = f"CVAT delete failed: {e}"
                    logger.warning("Failed to delete CVAT task %d: %s", cvat_task_id, e)

        self.task_db.delete_task(task_id)
        logger.info("Deleted task %d (CVAT %s)", task_id, cvat_task_id)

        result: dict[str, Any] = {
            "task_id": task_id,
            "cvat_task_id": cvat_task_id,
            "cvat_deleted": cvat_deleted,
        }
        if cvat_warning:
            result["warning"] = cvat_warning
        return result

    async def check_cvat_exists(self, task_id: int) -> bool | None:
        """Check if the CVAT task for a given task still exists.

        Args:
            task_id: Local annotation task ID to check.

        Returns:
            True/False, or None if task not found.
        """
        task = self.task_db.get_task(task_id)
        if not task or not task.get("cvat_task_id"):
            return None
        await self.cvat.authenticate()
        return await self.cvat.task_exists(task["cvat_task_id"])

    async def list_tasks(
        self,
        limit: int = 50,
        offset: int = 0,
        status: str | None = None,
        bone_type: str | None = None,
        profile_id: str | None = None,
        region: str | None = None,
    ) -> TaskListResponse:
        """List annotation tasks with optional filters."""
        tasks, total = self.task_db.list_tasks(limit, offset, status, bone_type, profile_id, region)
        for t in tasks:
            for key in ("created_at", "updated_at", "validated_at"):
                if t.get(key):
                    t[key] = str(t[key])
            progress = _build_task_progress(t.get("status", ""), t.get("notes"))
            if progress:
                t["progress"] = progress.model_dump()
        return TaskListResponse(tasks=tasks, total=total, limit=limit, offset=offset)

    async def sync_task(self, task_id: int) -> SyncResult:
        """Sync annotations from CVAT JSON REST API to PostgreSQL."""
        from .cvat_sync import sync_from_cvat

        task = self.task_db.get_task(task_id)
        if not task or not task.get("cvat_task_id"):
            msg = f"Task {task_id} not found or no CVAT task"
            raise ValueError(msg)

        await self.cvat.authenticate()
        result = await sync_from_cvat(self.cvat, task)

        self.task_db.update_task(
            task_id,
            status="reviewing",
            annotated_frames=result["synced_frames"],
        )

        return SyncResult(task_id=task_id, **result)

    async def validate_task(self, task_id: int, request: ValidateRequest) -> TaskResponse:
        """Validate or reject a task. Triggers training if enough validated."""
        self.task_db.validate_task(task_id, request.validated_by, request.decision)
        if request.notes:
            self.task_db.update_task(task_id, notes=request.notes)
        result = await self.get_task(task_id)
        if not result:
            raise ValueError(f"Task {task_id} not found")
        if request.decision == "validated" and result.bone_type:
            await self._maybe_trigger_training(result.bone_type)
        return result

_service: AnnotationWorkflowService | None = None


def get_service() -> AnnotationWorkflowService:
    """Get or create the annotation workflow service singleton."""
    global _service
    if _service is None:
        _service = AnnotationWorkflowService()
    return _service
