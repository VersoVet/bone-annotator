"""Background task preparation — async dataset prep + CVAT upload.

Runs in background via asyncio.create_task() so the API returns immediately.
Updates task status in PostgreSQL as it progresses.
"""

import asyncio
import logging
from pathlib import Path

from src.config import get_cvat_config, get_imaging_config
from src.modules.cvat.client import CVATClient
from src.modules.cvat.format import labels_to_cvat_format
from src.modules.labels.service import get_labels_for_bone
from src.modules.preparation.service import get_service as get_prep_service
from src.modules.sources.service import get_service as get_source_service
from src.modules.storage.task_db import AnnotationTaskDB

from .models import CreateTaskRequest

logger = logging.getLogger(__name__)


async def prepare_and_upload(
    task_id: int,
    request: CreateTaskRequest,
    task_db: AnnotationTaskDB,
) -> None:
    """Background coroutine: prepare dataset + create CVAT task + upload images.

    Updates task status in PostgreSQL throughout:
    preparing → uploading → created (or failed).

    Args:
        task_id: Internal task ID (already created in DB).
        request: Original task creation request.
        task_db: Task database instance.
    """
    try:
        # --- STEP 1: Prepare dataset ---
        task_db.update_task(task_id, status="preparing", notes="Preparing dataset...")
        source_svc = get_source_service()
        prep_svc = get_prep_service()

        acq_path = source_svc.get_acquisition_path(request.source_name, request.acquisition_id)
        if acq_path is None:
            task_db.update_task(task_id, status="failed", notes="Acquisition not found")
            return

        pipeline = request.pipeline_preset or get_imaging_config()["default_treatment"]
        dataset = await prep_svc.prepare_dataset(
            acquisition_path=acq_path,
            acquisition_id=request.acquisition_id,
            bone_type=request.bone_type,
            pipeline_preset=pipeline,
        )
        task_db.update_task(
            task_id,
            frame_count=dataset.frame_count,
            dataset_path=str(dataset.path),
            pipeline_config=dataset.pipeline_config,
            notes=f"Dataset ready: {dataset.frame_count} frames",
        )
        logger.info("Task %d: dataset prepared (%d frames)", task_id, dataset.frame_count)

        # --- STEP 2: Create CVAT task + upload ---
        task_db.update_task(task_id, status="uploading", notes="Creating CVAT task...")

        anatomy = get_labels_for_bone(request.bone_type)
        cvat_labels = labels_to_cvat_format(anatomy) if anatomy else []

        cfg = get_cvat_config()
        cvat = CVATClient(cfg["host"], cfg["port"], cfg["username"], cfg["password"])
        await cvat.authenticate()

        # Project
        project_id = await cvat.get_or_create_project(request.bone_type, cvat_labels)
        if project_id:
            await cvat.sync_project_labels(project_id, cvat_labels)
            task_db.save_project_mapping(request.bone_type, project_id)

        task_name = f"{request.acquisition_id}_{request.bone_type}_{request.region}"
        cvat_task = await cvat.create_task(task_name, project_id=project_id)
        if not cvat_task:
            task_db.update_task(task_id, status="failed", notes="CVAT task creation failed")
            await cvat.close()
            return

        cvat_task_id = cvat_task["id"]
        cvat_url = f"{cvat.base_url}/tasks/{cvat_task_id}"
        task_db.update_task(task_id, cvat_task_id=cvat_task_id, cvat_url=cvat_url)

        # Labels (only if no project)
        if not project_id and cvat_labels:
            await cvat.set_labels(cvat_task_id, cvat_labels)

        # Upload images

        task_db.update_task(task_id, notes=f"Uploading {dataset.frame_count} frames to CVAT...")
        image_paths = await asyncio.to_thread(_list_images, dataset.path / "images")
        if image_paths:
            if not await cvat.upload_image_paths(cvat_task_id, image_paths):
                raise RuntimeError(f"CVAT image upload failed for task {cvat_task_id}")

        await cvat.close()

        # --- STEP 3: Done ---
        task_db.update_task(
            task_id,
            status="created",
            notes=f"Ready: {dataset.frame_count} frames in CVAT #{cvat_task_id}",
        )
        logger.info("Task %d: created (CVAT %d, %d frames)", task_id, cvat_task_id, dataset.frame_count)

        # ML pre-annotations if requested
        if request.pre_annotate and cvat_task_id:
            from .catalog_notify import notify_catalog_task_status
            from .ml_bridge import call_bone_ml_annotate

            await call_bone_ml_annotate(cvat_task_id, request.bone_type)
            task_db.update_task(task_id, has_pre_annotations=True, status="annotating")
            await notify_catalog_task_status(request.acquisition_id, task_id, "annotating")

    except Exception as e:
        logger.error("Task %d preparation failed: %s", task_id, e, exc_info=True)
        task_db.update_task(task_id, status="failed", notes=str(e)[:500])


def _list_images(images_dir: Path) -> list[Path]:
    """List prepared PNG images in deterministic order."""
    return sorted(images_dir.glob("*.png"))
