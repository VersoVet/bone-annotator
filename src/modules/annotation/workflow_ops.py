"""Annotation workflow operations (pre-annotate, re-annotate, MedSAM2)."""

from __future__ import annotations

import logging
from typing import Any

from src.config import get_imaging_config

from .models import CreateTaskRequest, PreAnnotateResponse

logger = logging.getLogger(__name__)


class AnnotationWorkflowOps:
    """Mixin-style ops for AnnotationWorkflowService."""

    async def re_annotate_task(self, task_id: int, pre_annotate: bool = True) -> Any:
        """Create a re-annotation task from a validated parent."""
        parent = self.task_db.get_task(task_id)  # type: ignore[attr-defined]
        if not parent:
            raise ValueError(f"Task {task_id} not found")
        if parent.get("status") != "validated":
            raise ValueError(f"Task {task_id} not validated (status={parent.get('status')})")

        request = CreateTaskRequest(
            source_name=parent.get("source_name", "bonestore"),
            acquisition_id=parent["acquisition_id"],
            bone_type=parent["bone_type"],
            region=parent.get("region", "entire"),
            assignee=None,
            pipeline_preset=parent.get("pipeline_preset") or get_imaging_config()["default_treatment"],
            pre_annotate=False,
        )
        result = await self.create_task(request)  # type: ignore[attr-defined]
        self.task_db.update_task(result.id, parent_task_id=task_id)  # type: ignore[attr-defined]

        if result.cvat_task_id and parent.get("cvat_task_id"):
            await self._copy_parent_annotations(parent["cvat_task_id"], result.cvat_task_id)

        if pre_annotate and result.cvat_task_id:
            from .ml_bridge import call_bone_ml_annotate

            await call_bone_ml_annotate(result.cvat_task_id, parent.get("bone_type"))
            self.task_db.update_task(result.id, has_pre_annotations=True, status="annotating")  # type: ignore[attr-defined]
            from .catalog_notify import notify_catalog_task_status

            await notify_catalog_task_status(parent["acquisition_id"], result.id, "annotating")

        return result

    async def _copy_parent_annotations(self, parent_cvat_id: int, new_cvat_id: int) -> None:
        """Copy annotations from parent CVAT task to new task."""
        try:
            parent_anns = await self.cvat.get_annotations(parent_cvat_id)  # type: ignore[attr-defined]
            if parent_anns and parent_anns.get("shapes"):
                payload = {"version": 0, "shapes": parent_anns["shapes"], "tracks": [], "tags": []}
                await self.cvat.update_annotations(new_cvat_id, payload)  # type: ignore[attr-defined]
        except Exception as e:
            logger.warning("Failed to copy parent annotations: %s", e)

    async def request_pre_annotation(
        self,
        task_id: int,
        *,
        mode: str = "auto",
        propagate: bool = True,
    ) -> PreAnnotateResponse:
        """Request pre-annotations (bone-ml, else CPU Otsu seeds)."""
        from .catalog_notify import notify_catalog_task_status
        from .cpu_preannotate import push_cpu_seeds
        from .ml_bridge import _is_success_status, call_bone_ml_annotate

        task = self.task_db.get_task(task_id)  # type: ignore[attr-defined]
        if not task or not task.get("cvat_task_id"):
            raise ValueError(f"Task {task_id} not found or no CVAT task")

        ml_status = "skipped"
        final_status = "pre_annotation_failed"
        success = False

        if mode in ("auto", "ml"):
            ml_status = await call_bone_ml_annotate(
                task["cvat_task_id"],
                task.get("bone_type"),
                task.get("objective"),
            )
            success = _is_success_status(ml_status)
            if success:
                final_status = "pre_annotation_ml"

        if not success and mode in ("auto", "cpu"):
            await self.cvat.authenticate()  # type: ignore[attr-defined]

            # Step 2: Zone subdivision + SAM refinement (multi-label).
            zone_result = await self._zone_preannotate(task, propagate=propagate)
            if zone_result and int(zone_result.get("shapes_pushed") or 0) > 0:
                success = True
                final_status = zone_result.get("status", "pre_annotation_zones")
                ml_status = f"{ml_status}|zones:{zone_result.get('shapes_pushed')}"
            else:
                # Step 3: Fallback to original Otsu single-label.
                cpu_result = await push_cpu_seeds(self.cvat, task)  # type: ignore[attr-defined]
                ml_status = f"{ml_status}|cpu:{cpu_result.get('status')}:{cpu_result.get('shapes_pushed', 0)}"
                success = int(cpu_result.get("shapes_pushed") or 0) > 0
                if success:
                    final_status = "pre_annotation_cpu"
                    if propagate and cpu_result.get("seed_frames"):
                        try:
                            seed = int(cpu_result["seed_frames"][0])
                            label_id = cpu_result.get("label_id")
                            prop = await self.propagate_medsam2(
                                task_id,
                                seed,
                                [int(label_id)] if label_id is not None else None,
                            )
                            ml_status = f"{ml_status}|medsam2:{prop.get('propagated_masks', 0)}"
                            final_status = "pre_annotation_cpu_medsam2"
                        except Exception as e:
                            logger.warning("MedSAM2 propagate after CPU seeds failed: %s", e)
                            ml_status = f"{ml_status}|medsam2_error:{e}"

        if success:
            self.task_db.update_task(task_id, has_pre_annotations=True, status="annotating")  # type: ignore[attr-defined]
            await notify_catalog_task_status(task["acquisition_id"], task_id, "annotating")
        else:
            self.task_db.update_task(  # type: ignore[attr-defined]
                task_id,
                notes=f"Pre-annotation failed: {ml_status}"[:500],
            )

        return PreAnnotateResponse(
            task_id=task_id,
            cvat_task_id=task["cvat_task_id"],
            status=final_status,
            bone_ml_status=ml_status,
        )

    async def _zone_preannotate(
        self,
        task: dict[str, Any],
        *,
        propagate: bool = True,
    ) -> dict[str, Any] | None:
        """Run zone subdivision + optional SAM refinement + MedSAM2 propagation.

        Args:
            task: Annotation task row from DB.
            propagate: Enable MedSAM2 temporal propagation after seeding.

        Returns:
            Status dict with shapes_pushed, or None on failure.
        """
        from pathlib import Path

        from .cpu_preannotate import (
            _merge_push_shapes,
            build_zone_seed_shapes,
            resolve_seed_frames,
        )
        from .sam_proxy import SAM_GPU_URL
        from .sam_refine import refine_all_seed_shapes

        cvat_task_id = task.get("cvat_task_id")
        dataset_path = task.get("dataset_path")
        bone_type = task.get("bone_type", "")
        portion = task.get("region", "entire")
        if not cvat_task_id or not dataset_path:
            return None

        images_dir = Path(dataset_path) / "images"
        frame_files = sorted(images_dir.glob("*.png"))
        if not frame_files:
            return None

        labels = await self.cvat.get_task_labels(int(cvat_task_id))  # type: ignore[attr-defined]
        seed_frames = resolve_seed_frames(len(frame_files), 5)

        try:
            shapes = build_zone_seed_shapes(frame_files, seed_frames, labels, bone_type, portion)
        except Exception as e:
            logger.warning("Zone seed shapes failed: %s", e)
            return None

        if not shapes:
            logger.info("Zone subdivision produced no shapes for task CVAT#%s", cvat_task_id)
            return None

        # SAM refinement (best-effort, falls back to CPU masks).
        try:
            shapes = await refine_all_seed_shapes(SAM_GPU_URL, frame_files, shapes)
        except Exception as e:
            logger.warning("SAM refinement error (keeping CPU masks): %s", e)

        ok, _ = await _merge_push_shapes(self.cvat, int(cvat_task_id), shapes)  # type: ignore[attr-defined]
        if not ok:
            logger.warning("Failed to push zone shapes to CVAT#%s", cvat_task_id)
            return None

        status = "pre_annotation_zones_sam"
        label_ids = list({s["label_id"] for s in shapes})

        # MedSAM2 propagation for each zone label.
        if propagate and seed_frames:
            try:
                prop = await self.propagate_medsam2(
                    task["id"], seed_frames[0], label_ids,
                )
                status = "pre_annotation_zones_sam_medsam2"
                logger.info("Zone+SAM+MedSAM2: %d masks propagated", prop.get("propagated_masks", 0))
            except Exception as e:
                logger.warning("MedSAM2 after zone+SAM failed: %s", e)

        return {"status": status, "shapes_pushed": len(shapes), "label_ids": label_ids}

    async def _maybe_trigger_training(self, bone_type: str) -> None:
        """Trigger fine-tuning if enough validated tasks."""
        from .ml_bridge import maybe_trigger_training

        await maybe_trigger_training(self.task_db._get_conn(), bone_type)  # type: ignore[attr-defined]

    async def propagate_medsam2(
        self,
        task_id: int,
        seed_frame_idx: int = 0,
        label_ids: list[int] | None = None,
    ) -> dict[str, Any]:
        """Propagate bone masks with MedSAM2 temporal propagation."""
        from .catalog_notify import notify_catalog_task_status
        from .medsam2_bridge import propagate

        task = self.task_db.get_task(task_id)  # type: ignore[attr-defined]
        if not task or not task.get("cvat_task_id"):
            raise ValueError(f"Task {task_id} not found or no CVAT task")
        if not task.get("dataset_path"):
            raise ValueError(f"Task {task_id} has no dataset_path")
        await self.cvat.authenticate()  # type: ignore[attr-defined]
        result = await propagate(self.cvat, task, seed_frame_idx, label_ids)  # type: ignore[attr-defined]
        self.task_db.update_task(task_id, has_pre_annotations=True, status="annotating")  # type: ignore[attr-defined]
        await notify_catalog_task_status(task["acquisition_id"], task_id, "annotating")
        return result
