"""Background task preparation — async dataset prep + CVAT upload.

Runs in background via asyncio.create_task() so the API returns immediately.
Updates task status in PostgreSQL as it progresses.
"""

import asyncio
import logging
from pathlib import Path
from typing import Any

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
        # --- STEP 1: Prepare dataset (0-40%) ---
        task_db.update_task(task_id, status="preparing", notes="[5%] Loading acquisition...")
        source_svc = get_source_service()
        prep_svc = get_prep_service()

        acq_path = source_svc.get_acquisition_path(request.source_name, request.acquisition_id)
        if acq_path is None:
            task_db.update_task(task_id, status="failed", notes="Acquisition not found")
            return

        task_db.update_task(task_id, notes="[10%] Preparing dataset (pipeline + frames)...")
        pipeline = request.pipeline_preset or get_imaging_config()["default_treatment"]

        # Resolve crop params from parent task if requested
        crop_params = None
        if request.crop_from_task_id:
            task_db.update_task(task_id, notes="[8%] Resolving crop from parent task...")
            crop_params = await _resolve_crop_params(task_db, request.crop_from_task_id)
            if crop_params:
                task_db.update_task(task_id, crop_params=crop_params)
                logger.info(
                    "Task %d: crop from parent #%d bbox=%s", task_id, request.crop_from_task_id, crop_params.get("bbox")
                )

        def _on_frame_progress(current: int, total: int) -> None:
            pct = 10 + int(30 * current / max(total, 1))
            task_db.update_task(task_id, notes=f"[{pct}%] Processing frame {current}/{total}...")

        dataset = await prep_svc.prepare_dataset(
            acquisition_path=acq_path,
            acquisition_id=request.acquisition_id,
            bone_type=request.bone_type,
            pipeline_preset=pipeline,
            on_progress=_on_frame_progress,
            crop_params=crop_params,
        )
        task_db.update_task(
            task_id,
            frame_count=dataset.frame_count,
            dataset_path=str(dataset.path),
            pipeline_config=dataset.pipeline_config,
            notes=f"[40%] Dataset ready: {dataset.frame_count} frames",
        )
        logger.info("Task %d: dataset prepared (%d frames)", task_id, dataset.frame_count)

        # --- STEP 2: Create CVAT task + upload (40-90%) ---
        task_db.update_task(task_id, status="uploading", notes="[45%] Authenticating CVAT...")

        anatomy = get_labels_for_bone(request.bone_type)
        if anatomy and request.labels_filter:
            anatomy = dict(anatomy)
            anatomy["zones"] = [
                z
                for z in anatomy.get("zones", [])
                if z.get("id") in request.labels_filter or z.get("label") in request.labels_filter
            ]
            anatomy["landmarks"] = [
                lm
                for lm in anatomy.get("landmarks", [])
                if lm.get("id") in request.labels_filter or lm.get("label") in request.labels_filter
            ]
            logger.info(
                "Task %d: labels filtered to %d zones + %d landmarks",
                task_id,
                len(anatomy.get("zones", [])),
                len(anatomy.get("landmarks", [])),
            )
        cvat_labels = labels_to_cvat_format(anatomy) if anatomy else []

        cfg = get_cvat_config()
        cvat = CVATClient(cfg["host"], cfg["port"], cfg["username"], cfg["password"])
        await cvat.authenticate()

        task_db.update_task(task_id, notes="[50%] Creating CVAT project/task...")

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

        # Upload images (55-90%)
        task_db.update_task(task_id, notes=f"[55%] Uploading {dataset.frame_count} frames to CVAT...")
        image_paths = await asyncio.to_thread(_list_images, dataset.path / "images")
        if image_paths:
            if not await cvat.upload_image_paths(cvat_task_id, image_paths):
                raise RuntimeError(f"CVAT image upload failed for task {cvat_task_id}")

        task_db.update_task(task_id, notes="[90%] Upload complete, finalizing...")
        await cvat.close()

        # --- STEP 3: Done (90-100%) ---
        task_db.update_task(
            task_id,
            status="created",
            notes=f"[100%] Ready: {dataset.frame_count} frames in CVAT #{cvat_task_id}",
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


async def _resolve_crop_params(
    task_db: AnnotationTaskDB,
    crop_from_task_id: int,
    padding_percent: int = 10,
) -> dict[str, Any] | None:
    """Extract crop bounding box from a parent task's CVAT annotations.

    Pulls all shapes from frame 0 of the parent task, computes the
    enclosing bounding box, and adds padding.

    Args:
        task_db: Task database instance.
        crop_from_task_id: Parent task ID to crop from.
        padding_percent: Padding around the bounding box (default 10%).

    Returns:
        Crop params dict or None if parent has no annotations.
    """

    parent = task_db.get_task(crop_from_task_id)
    if not parent or not parent.get("cvat_task_id"):
        logger.warning("Crop parent task %d not found or no CVAT task", crop_from_task_id)
        return None

    cfg = get_cvat_config()
    cvat = CVATClient(cfg["host"], cfg["port"], cfg["username"], cfg["password"])
    await cvat.authenticate()

    annotations = await cvat.get_annotations(parent["cvat_task_id"])
    if not annotations or not annotations.get("shapes"):
        logger.warning("Crop parent task %d has no annotations", crop_from_task_id)
        return None

    # Find bounding box enclosing all shapes on frame 0
    x_coords: list[float] = []
    y_coords: list[float] = []

    for shape in annotations["shapes"]:
        if shape.get("frame") != 0:
            continue
        pts = shape.get("points", [])
        if shape["type"] == "rectangle" and len(pts) >= 4:
            x_coords.extend([pts[0], pts[2]])
            y_coords.extend([pts[1], pts[3]])
        elif shape["type"] == "polygon" and len(pts) >= 6:
            x_coords.extend(pts[i] for i in range(0, len(pts), 2))
            y_coords.extend(pts[i] for i in range(1, len(pts), 2))
        elif shape["type"] == "mask" and len(pts) >= 4:
            # Mask RLE: last 4 values are left, top, right, bottom
            x_coords.extend([pts[-4], pts[-2]])
            y_coords.extend([pts[-3], pts[-1]])

    if not x_coords:
        logger.warning("No shapes on frame 0 of parent task %d", crop_from_task_id)
        return None

    x1, y1 = int(min(x_coords)), int(min(y_coords))
    x2, y2 = int(max(x_coords)), int(max(y_coords))

    await cvat.close()

    return {
        "bbox": [x1, y1, x2, y2],
        "padding_percent": padding_percent,
        "parent_task_id": crop_from_task_id,
    }
