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

from .models import (
    CreateTaskRequest,
    PreAnnotateResponse,
    SyncResult,
    TaskListResponse,
    TaskResponse,
    ValidateRequest,
)

logger = logging.getLogger(__name__)

_PROVENANCE_KEYS = {"source", "confidence", "model_version"}


def _extract_shape_provenance(attributes: list[dict[str, Any]]) -> dict[str, Any]:
    """Extract provenance fields from CVAT shape attributes JSON."""
    result: dict[str, Any] = {}
    for attr in attributes:
        name = attr.get("name", "")
        value = attr.get("value", "")
        if name == "confidence":
            try:
                result["confidence"] = float(value)
            except (ValueError, TypeError):
                pass
        elif name in _PROVENANCE_KEYS:
            result[name] = value
    return result


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
            from .ml_bridge import call_bone_ml_annotate

            await call_bone_ml_annotate(cvat_task_id)
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
        """Sync annotations from CVAT JSON REST API to PostgreSQL."""
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

        # Pull annotations as JSON (not XML)
        raw_annotations = await self.cvat.get_annotations(cvat_task_id)

        zones_count = 0
        landmarks_count = 0
        synced_frames = 0

        if raw_annotations and "shapes" in raw_annotations:
            from src.modules.storage.pg_db import AnnotationPgDB

            pg_config = get_postgres_config()
            db = AnnotationPgDB(**pg_config)

            # Resolve label IDs to names from task metadata
            cvat_task_data = await self.cvat.get_task(cvat_task_id)
            label_map = {lbl["id"]: lbl["name"] for lbl in (cvat_task_data.get("labels", []) if cvat_task_data else [])}

            # Group shapes by frame number
            frames: dict[int, dict[str, list[Any]]] = {}
            for shape in raw_annotations.get("shapes", []):
                frame_num = shape.get("frame", 0)
                if frame_num not in frames:
                    frames[frame_num] = {"zones": [], "landmarks": []}
                # Extract provenance from CVAT attributes
                provenance = _extract_shape_provenance(shape.get("attributes", []))
                label_name = label_map.get(shape.get("label_id"), str(shape.get("label_id", "")))
                shape_data = {
                    "label": label_name,
                    "type": shape.get("type", "rectangle"),
                    **provenance,
                }
                if shape.get("type") == "points":
                    pts = shape.get("points", [])
                    if len(pts) >= 2:
                        shape_data["x"] = pts[0]
                        shape_data["y"] = pts[1]
                    frames[frame_num]["landmarks"].append(shape_data)
                    landmarks_count += 1
                else:
                    pts = shape.get("points", [])
                    if len(pts) >= 4:
                        shape_data["x"] = pts[0]
                        shape_data["y"] = pts[1]
                        shape_data["width"] = pts[2] - pts[0]
                        shape_data["height"] = pts[3] - pts[1]
                    frames[frame_num]["zones"].append(shape_data)
                    zones_count += 1

            # Save each frame's annotations
            for frame_num, anns in frames.items():
                frame_fn = f"frame_{frame_num:04d}.png"
                first = (anns["zones"] or anns["landmarks"])[0]
                db.save_frame_annotations(
                    task["acquisition_id"],
                    frame_fn,
                    anns,
                    author=author,
                    source=first.get("source", "manual"),
                    confidence=first.get("confidence"),
                    model_version=first.get("model_version"),
                )
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
        """Validate or reject a task. Triggers training if enough validated tasks."""
        self.task_db.validate_task(task_id, request.validated_by, request.decision)
        if request.notes:
            self.task_db.update_task(task_id, notes=request.notes)
        result = await self.get_task(task_id)
        if result is None:
            msg = f"Task {task_id} not found"
            raise ValueError(msg)
        # Auto-trigger training if enough validated tasks
        if request.decision == "validated" and result.bone_type:
            await self._maybe_trigger_training(result.bone_type)
        return result

    async def re_annotate_task(self, task_id: int, pre_annotate: bool = True) -> TaskResponse:
        """Create a re-annotation task pre-populated with parent annotations."""
        parent = self.task_db.get_task(task_id)
        if not parent:
            msg = f"Task {task_id} not found"
            raise ValueError(msg)
        if parent.get("status") != "validated":
            msg = f"Task {task_id} is not validated (status={parent.get('status')})"
            raise ValueError(msg)

        from .models import CreateTaskRequest

        request = CreateTaskRequest(
            source_name=parent.get("source_name", "bonestore"),
            acquisition_id=parent["acquisition_id"],
            bone_type=parent["bone_type"],
            region=parent.get("region", "entire"),
            pipeline_preset=parent.get("pipeline_preset", "replay_membre"),
            pre_annotate=False,  # We'll push parent annotations instead
        )
        result = await self.create_task(request)
        self.task_db.update_task(result.id, parent_task_id=task_id)

        # Copy validated annotations from parent into new CVAT task
        if result.cvat_task_id and parent.get("cvat_task_id"):
            await self._copy_parent_annotations(parent["cvat_task_id"], result.cvat_task_id)

        # Optionally request ML pre-annotations on top
        if pre_annotate and result.cvat_task_id:
            from .ml_bridge import call_bone_ml_annotate

            await call_bone_ml_annotate(result.cvat_task_id)
            self.task_db.update_task(result.id, has_pre_annotations=True)

        return result

    async def _copy_parent_annotations(self, parent_cvat_id: int, new_cvat_id: int) -> None:
        """Copy annotations from parent CVAT task to new task."""
        try:
            parent_anns = await self.cvat.get_annotations(parent_cvat_id)
            if parent_anns and parent_anns.get("shapes"):
                payload = {"version": 0, "shapes": parent_anns["shapes"], "tracks": [], "tags": []}
                await self.cvat.update_annotations(new_cvat_id, payload)
                logger.info(
                    "Copied %d shapes from CVAT %d to %d", len(parent_anns["shapes"]), parent_cvat_id, new_cvat_id
                )
        except Exception as e:
            logger.warning("Failed to copy parent annotations: %s", e)

    async def request_pre_annotation(self, task_id: int) -> PreAnnotateResponse:
        """Request ML pre-annotations from bone-ml."""
        from .ml_bridge import call_bone_ml_annotate

        task = self.task_db.get_task(task_id)
        if not task or not task.get("cvat_task_id"):
            msg = f"Task {task_id} not found or no CVAT task"
            raise ValueError(msg)

        cvat_task_id = task["cvat_task_id"]
        ml_status = await call_bone_ml_annotate(cvat_task_id)
        self.task_db.update_task(task_id, has_pre_annotations=True, status="annotating")

        return PreAnnotateResponse(
            task_id=task_id,
            cvat_task_id=cvat_task_id,
            status="pre_annotation_requested",
            bone_ml_status=ml_status,
        )

    async def _maybe_trigger_training(self, bone_type: str) -> None:
        """Trigger fine-tuning if enough validated tasks since last run."""
        from .ml_bridge import maybe_trigger_training

        conn = self.task_db._get_conn()
        await maybe_trigger_training(conn, bone_type)

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
