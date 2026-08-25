"""Annotation workflow service — orchestrates CVAT, labels, preparation, and storage."""

import asyncio
import logging
from typing import Any

from src.config import get_cvat_config, get_postgres_config
from src.modules.cvat.client import CVATClient
from src.modules.cvat.format import labels_to_cvat_format
from src.modules.labels.service import get_labels_for_bone
from src.modules.preparation.service import get_service as get_prep_service
from src.modules.sources.service import get_service as get_source_service
from src.modules.storage.task_db import AnnotationTaskDB, create_task_db

from .models import CreateTaskRequest, PreAnnotateResponse, SyncResult, TaskListResponse, TaskResponse, ValidateRequest

logger = logging.getLogger(__name__)


class AnnotationWorkflowService:
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
        """Create annotation task: prepare dataset, create CVAT task, configure labels."""
        source_svc = get_source_service()
        prep_svc = get_prep_service()
        acq_path = source_svc.get_acquisition_path(request.source_name, request.acquisition_id)
        if acq_path is None:
            msg = f"Acquisition not found: {request.acquisition_id}"
            raise ValueError(msg)

        # Prepare dataset
        dataset = await prep_svc.prepare_dataset(
            acquisition_path=acq_path,
            acquisition_id=request.acquisition_id,
            bone_type=request.bone_type,
            pipeline_preset=request.pipeline_preset,
        )

        # Labels (must exist in label-generator)
        anatomy = get_labels_for_bone(request.bone_type)
        if not anatomy:
            raise ValueError(f"No labels found for bone_type '{request.bone_type}' in label-generator")
        cvat_labels = labels_to_cvat_format(anatomy)

        await self.cvat.authenticate()
        project_id = await self.cvat.get_or_create_project(request.bone_type, cvat_labels)
        if project_id:
            await self.cvat.sync_project_labels(project_id, cvat_labels)
            self.task_db.save_project_mapping(request.bone_type, project_id)

        task_name = f"{request.acquisition_id}_{request.bone_type}_{request.region}"
        cvat_task = await self.cvat.create_task(task_name, project_id=project_id)
        if not cvat_task:
            raise RuntimeError("Failed to create CVAT task")
        cvat_task_id = cvat_task["id"]
        cvat_url = f"{self.cvat.base_url}/tasks/{cvat_task_id}"

        try:
            if not project_id and cvat_labels:
                await self.cvat.set_labels(cvat_task_id, cvat_labels)
            images = await asyncio.to_thread(self._load_prepared_images, dataset.path / "images")
            if images:
                await self.cvat.upload_images(cvat_task_id, images)
        except Exception:
            logger.error("CVAT setup failed, deleting task %d", cvat_task_id)
            try:
                if self.cvat.client:
                    await self.cvat.client.delete(f"{self.cvat.api_base}/tasks/{cvat_task_id}")
            except Exception as cleanup_err:
                logger.warning("CVAT cleanup failed: %s", cleanup_err)
            raise

        # Save to DB
        task_id = await asyncio.to_thread(
            self.task_db.save_task,
            acquisition_id=request.acquisition_id,
            bone_type=request.bone_type,
            author=request.assignee or "system",
            cvat_task_id=cvat_task_id,
            source_name=request.source_name,
            region=request.region,
            assignee=request.assignee,
            frame_count=dataset.frame_count,
            dataset_path=str(dataset.path),
            pipeline_preset=request.pipeline_preset,
            pipeline_config=dataset.pipeline_config,
            cvat_url=cvat_url,
        )

        # ML pre-annotations
        if request.pre_annotate and cvat_task_id:
            from .ml_bridge import call_bone_ml_annotate

            await call_bone_ml_annotate(cvat_task_id, request.bone_type)
            self.task_db.update_task(task_id, has_pre_annotations=True, status="annotating")

        logger.info("Task %d created: %s (CVAT %s)", task_id, task_name, cvat_task_id)
        return TaskResponse(
            id=task_id,
            acquisition_id=request.acquisition_id,
            cvat_task_id=cvat_task_id,
            cvat_url=cvat_url,
            status="annotating" if request.pre_annotate else "created",
            bone_type=request.bone_type,
            region=request.region,
            frame_count=dataset.frame_count,
            author=request.assignee or "system",
            assignee=request.assignee,
            has_pre_annotations=request.pre_annotate,
            pipeline_preset=request.pipeline_preset,
            dataset_path=str(dataset.path),
        )

    async def get_task(self, task_id: int) -> TaskResponse | None:
        """Get task status from local DB."""
        t = self.task_db.get_task(task_id)
        if not t:
            return None
        return TaskResponse(
            id=t["id"],
            acquisition_id=t["acquisition_id"],
            cvat_task_id=t.get("cvat_task_id"),
            cvat_url=t.get("cvat_url"),
            status=t.get("status", "unknown"),
            bone_type=t["bone_type"],
            region=t.get("region", "entire"),
            frame_count=t.get("frame_count", 0),
            annotated_frames=t.get("annotated_frames", 0),
            author=t.get("author", "unknown"),
            assignee=t.get("assignee"),
            has_pre_annotations=t.get("has_pre_annotations", False),
            pipeline_preset=t.get("pipeline_preset"),
            dataset_path=t.get("dataset_path"),
        )

    async def list_tasks(
        self,
        limit: int = 50,
        offset: int = 0,
        status: str | None = None,
        bone_type: str | None = None,
    ) -> TaskListResponse:
        """List annotation tasks with optional filters."""
        tasks, total = self.task_db.list_tasks(limit, offset, status, bone_type)
        for t in tasks:
            for key in ("created_at", "updated_at", "validated_at"):
                if t.get(key):
                    t[key] = str(t[key])
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

    async def re_annotate_task(self, task_id: int, pre_annotate: bool = True) -> TaskResponse:
        """Create a re-annotation task from a validated parent."""
        parent = self.task_db.get_task(task_id)
        if not parent:
            raise ValueError(f"Task {task_id} not found")
        if parent.get("status") != "validated":
            raise ValueError(f"Task {task_id} not validated (status={parent.get('status')})")

        from .models import CreateTaskRequest

        request = CreateTaskRequest(
            source_name=parent.get("source_name", "bonestore"),
            acquisition_id=parent["acquisition_id"],
            bone_type=parent["bone_type"],
            region=parent.get("region", "entire"),
            pipeline_preset=parent.get("pipeline_preset", "replay_membre"),
            pre_annotate=False,
        )
        result = await self.create_task(request)
        self.task_db.update_task(result.id, parent_task_id=task_id)

        # Copy validated annotations from parent into new CVAT task
        if result.cvat_task_id and parent.get("cvat_task_id"):
            await self._copy_parent_annotations(parent["cvat_task_id"], result.cvat_task_id)

        # Optionally request ML pre-annotations on top
        if pre_annotate and result.cvat_task_id:
            from .ml_bridge import call_bone_ml_annotate

            await call_bone_ml_annotate(result.cvat_task_id, parent.get("bone_type"))
            self.task_db.update_task(result.id, has_pre_annotations=True)

        return result

    async def _copy_parent_annotations(self, parent_cvat_id: int, new_cvat_id: int) -> None:
        """Copy annotations from parent CVAT task to new task."""
        try:
            parent_anns = await self.cvat.get_annotations(parent_cvat_id)
            if parent_anns and parent_anns.get("shapes"):
                payload = {"version": 0, "shapes": parent_anns["shapes"], "tracks": [], "tags": []}
                await self.cvat.update_annotations(new_cvat_id, payload)
        except Exception as e:
            logger.warning("Failed to copy parent annotations: %s", e)

    async def request_pre_annotation(self, task_id: int) -> PreAnnotateResponse:
        """Request ML pre-annotations from bone-ml."""
        from .ml_bridge import call_bone_ml_annotate

        task = self.task_db.get_task(task_id)
        if not task or not task.get("cvat_task_id"):
            raise ValueError(f"Task {task_id} not found or no CVAT task")
        ml_status = await call_bone_ml_annotate(task["cvat_task_id"], task.get("bone_type"))
        self.task_db.update_task(task_id, has_pre_annotations=True, status="annotating")
        return PreAnnotateResponse(
            task_id=task_id,
            cvat_task_id=task["cvat_task_id"],
            status="pre_annotation_requested",
            bone_ml_status=ml_status,
        )

    async def _maybe_trigger_training(self, bone_type: str) -> None:
        """Trigger fine-tuning if enough validated tasks."""
        from .ml_bridge import maybe_trigger_training

        await maybe_trigger_training(self.task_db._get_conn(), bone_type)

    async def propagate_medsam2(self, task_id: int, seed_frame_idx: int = 0) -> dict[str, Any]:
        """Propagate bone mask with MedSAM2 temporal propagation."""
        from .medsam2_bridge import propagate

        task = self.task_db.get_task(task_id)
        if not task or not task.get("cvat_task_id"):
            raise ValueError(f"Task {task_id} not found or no CVAT task")
        if not task.get("dataset_path"):
            raise ValueError(f"Task {task_id} has no dataset_path")
        await self.cvat.authenticate()
        result = await propagate(self.cvat, task, seed_frame_idx)
        self.task_db.update_task(task_id, has_pre_annotations=True, status="annotating")
        return result

    def _load_prepared_images(self, images_dir: Any) -> list[tuple[str, bytes]]:
        """Load prepared PNG images from directory."""
        from pathlib import Path

        return [(p.name, p.read_bytes()) for p in sorted(Path(images_dir).glob("*.png"))]


_service: AnnotationWorkflowService | None = None


def get_service() -> AnnotationWorkflowService:
    """Get or create the annotation workflow service singleton."""
    global _service
    if _service is None:
        _service = AnnotationWorkflowService()
    return _service
