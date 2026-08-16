"""Annotation workflow service — orchestrates CVAT, labels, preparation, and storage."""

import asyncio
import logging
from typing import Any

import httpx

from src.config import get_bone_ml_config, get_cvat_config, get_postgres_config
from src.modules.cvat.client import CVATClient
from src.modules.cvat.format import labels_to_cvat_format
from src.modules.cvat.sync import CVATSync
from src.modules.labels.service import get_labels_for_bone
from src.modules.preparation.service import get_service as get_prep_service
from src.modules.sources.service import get_service as get_source_service
from src.modules.storage.task_db import AnnotationTaskDB, create_task_db

from .models import (
    CreateTaskRequest,
    PreAnnotateResponse,
    SyncResult,
    TaskListResponse,
    TaskResponse,
    ValidateRequest,
)

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
        # 1. Get acquisition path
        acq_path = source_svc.get_acquisition_path(request.source_name, request.acquisition_id)
        if acq_path is None:
            msg = f"Acquisition not found: {request.acquisition_id}"
            raise ValueError(msg)

        # 2. Prepare dataset (imaging-sdk pipeline → PNG 16-bit)
        dataset = await prep_svc.prepare_dataset(
            acquisition_path=acq_path,
            acquisition_id=request.acquisition_id,
            bone_type=request.bone_type,
            pipeline_preset=request.pipeline_preset,
        )

        # 3. Fetch labels from label-generator
        anatomy = get_labels_for_bone(request.bone_type)
        cvat_labels = labels_to_cvat_format(anatomy) if anatomy else []

        # 4. Create CVAT task
        await self.cvat.authenticate()
        task_name = f"{request.acquisition_id}_{request.bone_type}_{request.region}"
        cvat_task = await self.cvat.create_task(task_name)
        if not cvat_task:
            msg = "Failed to create CVAT task"
            raise RuntimeError(msg)
        cvat_task_id = cvat_task["id"]
        cvat_url = f"{self.cvat.base_url}/tasks/{cvat_task_id}"

        # 5. Set labels + upload images (delete CVAT task on failure)
        try:
            if cvat_labels:
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

        # 7. Save task to PostgreSQL (offloaded to thread for sync psycopg)
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

        # 8. Request ML pre-annotations if asked
        if request.pre_annotate and cvat_task_id:
            await self._call_bone_ml_annotate(cvat_task_id)
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
        task = self.task_db.get_task(task_id)
        if not task:
            return None
        return TaskResponse(
            id=task["id"],
            acquisition_id=task["acquisition_id"],
            cvat_task_id=task.get("cvat_task_id"),
            cvat_url=task.get("cvat_url"),
            status=task.get("status", "unknown"),
            bone_type=task["bone_type"],
            region=task.get("region", "entire"),
            frame_count=task.get("frame_count", 0),
            annotated_frames=task.get("annotated_frames", 0),
            author=task.get("author", "unknown"),
            assignee=task.get("assignee"),
            has_pre_annotations=task.get("has_pre_annotations", False),
            pipeline_preset=task.get("pipeline_preset"),
            dataset_path=task.get("dataset_path"),
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
        # Serialize datetimes
        for t in tasks:
            for key in ("created_at", "updated_at", "validated_at"):
                if t.get(key):
                    t[key] = str(t[key])
        return TaskListResponse(tasks=tasks, total=total, limit=limit, offset=offset)

    async def sync_task(self, task_id: int) -> SyncResult:
        """Sync annotations from CVAT to PostgreSQL."""
        task = self.task_db.get_task(task_id)
        if not task or not task.get("cvat_task_id"):
            msg = f"Task {task_id} not found or no CVAT task"
            raise ValueError(msg)

        cvat_task_id = task["cvat_task_id"]
        await self.cvat.authenticate()

        # Get assignee from CVAT jobs
        jobs = await self.cvat.get_task_jobs(cvat_task_id)
        author = "unknown"
        if jobs:
            assignee_info = jobs[0].get("assignee")
            if assignee_info and isinstance(assignee_info, dict):
                author = assignee_info.get("username", "unknown")
            elif isinstance(assignee_info, str):
                author = assignee_info

        # Pull annotations via sync module
        sync = CVATSync(self.cvat)
        annotations = await sync.pull_annotations(cvat_task_id)

        zones_count = 0
        landmarks_count = 0
        synced_frames = 0

        if annotations and "images" in annotations:
            from src.modules.storage.pg_db import AnnotationPgDB

            pg_config = get_postgres_config()
            db = AnnotationPgDB(**pg_config)
            for img in annotations["images"]:
                frame_fn = img.get("name", "")
                frame_anns: dict[str, list[Any]] = {"zones": [], "landmarks": []}
                for shape in img.get("shapes", []):
                    frame_anns["zones"].append(shape)
                    zones_count += 1
                for lm in img.get("landmarks", []):
                    frame_anns["landmarks"].append(lm)
                    landmarks_count += 1
                if frame_anns["zones"] or frame_anns["landmarks"]:
                    db.save_frame_annotations(task["acquisition_id"], frame_fn, frame_anns)
                    synced_frames += 1
            db.close()

        self.task_db.update_task(
            task_id,
            status="reviewing",
            annotated_frames=synced_frames,
        )
        logger.info(
            "Task %d synced: %d frames, %d zones, %d landmarks", task_id, synced_frames, zones_count, landmarks_count
        )

        return SyncResult(
            task_id=task_id,
            synced_frames=synced_frames,
            zones_count=zones_count,
            landmarks_count=landmarks_count,
            author=author,
        )

    async def validate_task(self, task_id: int, request: ValidateRequest) -> TaskResponse:
        """Validate or reject a task."""
        self.task_db.validate_task(task_id, request.validated_by, request.decision)
        if request.notes:
            self.task_db.update_task(task_id, notes=request.notes)
        result = await self.get_task(task_id)
        if result is None:
            msg = f"Task {task_id} not found"
            raise ValueError(msg)
        return result

    async def request_pre_annotation(self, task_id: int) -> PreAnnotateResponse:
        """Request ML pre-annotations from bone-ml."""
        task = self.task_db.get_task(task_id)
        if not task or not task.get("cvat_task_id"):
            msg = f"Task {task_id} not found or no CVAT task"
            raise ValueError(msg)

        cvat_task_id = task["cvat_task_id"]
        ml_status = await self._call_bone_ml_annotate(cvat_task_id)
        self.task_db.update_task(task_id, has_pre_annotations=True, status="annotating")

        return PreAnnotateResponse(
            task_id=task_id,
            cvat_task_id=cvat_task_id,
            status="pre_annotation_requested",
            bone_ml_status=ml_status,
        )

    async def _call_bone_ml_annotate(self, cvat_task_id: int) -> str:
        """Call bone-ml to pre-annotate a CVAT task."""
        ml_config = get_bone_ml_config()
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    f"{ml_config['base_url']}/api/cvat/annotate",
                    json={"task_id": cvat_task_id},
                    timeout=30.0,
                )
                data = resp.json()
                return data.get("status", "unknown")
        except Exception as e:
            logger.error("bone-ml pre-annotation failed: %s", e)
            return f"error: {e}"

    def _load_prepared_images(self, images_dir: Any) -> list[tuple[str, bytes]]:
        """Load prepared PNG images from directory."""
        from pathlib import Path

        return [(p.name, p.read_bytes()) for p in sorted(Path(images_dir).glob("*.png"))]


# Module singleton
_service: AnnotationWorkflowService | None = None


def get_service() -> AnnotationWorkflowService:
    """Get or create the annotation workflow service singleton."""
    global _service
    if _service is None:
        _service = AnnotationWorkflowService()
    return _service
