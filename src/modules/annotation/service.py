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

            # Ensure acquisition exists in DB before saving annotations
            db.ensure_acquisition(
                acq_id=task["acquisition_id"],
                category=task.get("bone_type", ""),
                bone_type=task.get("bone_type", ""),
                side=task.get("region", "entire"),
                region=task.get("region", "entire"),
                frame_count=task.get("frame_count", 0),
            )

            # Resolve label IDs to names (CVAT v2: labels are at /api/labels?task_id=N)
            label_map: dict[int, str] = {}
            if self.cvat.client:
                lbl_resp = await self.cvat.client.get(f"{self.cvat.api_base}/labels?task_id={cvat_task_id}")
                if lbl_resp.status_code == 200:
                    for lbl in lbl_resp.json().get("results", []):
                        label_map[lbl["id"]] = lbl["name"]

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

    async def propagate_medsam2(
        self,
        task_id: int,
        seed_frame_idx: int = 0,
    ) -> dict[str, Any]:
        """Propagate bone mask with MedSAM2 temporal propagation.

        Flow:
        1. Get task info (dataset_path, cvat_task_id)
        2. Pull seed mask from CVAT (first annotated frame)
        3. Load frames from prepared dataset
        4. Call MedSAM2 /propagate
        5. Push propagated masks back to CVAT

        Args:
            task_id: Internal annotation task ID.
            seed_frame_idx: Frame index with the seed mask.

        Returns:
            Propagation result with frame count.
        """
        import base64
        import io
        from pathlib import Path

        import httpx
        import yaml
        from PIL import Image

        task = self.task_db.get_task(task_id)
        if not task or not task.get("cvat_task_id"):
            msg = f"Task {task_id} not found or no CVAT task"
            raise ValueError(msg)

        cvat_task_id = task["cvat_task_id"]
        dataset_path = task.get("dataset_path")
        if not dataset_path:
            msg = f"Task {task_id} has no dataset_path"
            raise ValueError(msg)

        images_dir = Path(dataset_path) / "images"
        if not images_dir.exists():
            msg = f"Dataset images not found: {images_dir}"
            raise ValueError(msg)

        # 1. Pull seed mask from CVAT
        await self.cvat.authenticate()
        annotations = await self.cvat.get_annotations(cvat_task_id)

        seed_mask = None
        if annotations and annotations.get("shapes"):
            # Find a mask or polygon shape on the seed frame
            for shape in annotations["shapes"]:
                if shape.get("frame") == seed_frame_idx:
                    if shape.get("type") == "mask":
                        # CVAT mask format: RLE + bounds
                        seed_mask = self._cvat_mask_to_binary(shape, task.get("frame_count", 0))
                        break
                    elif shape.get("type") in ("polygon", "rectangle"):
                        # Convert polygon/rect to binary mask
                        seed_mask = self._cvat_shape_to_binary(shape, images_dir, seed_frame_idx)
                        break

        if seed_mask is None:
            msg = f"No annotation found on frame {seed_frame_idx} in CVAT task {cvat_task_id}. Annotate at least one frame first."
            raise ValueError(msg)

        # 2. Load frames from dataset (sample for large series)
        frame_files = sorted(images_dir.glob("*.png"))
        max_frames = 100  # Limit for MedSAM2 memory
        step = max(1, len(frame_files) // max_frames)
        sampled_files = frame_files[::step]
        sampled_seed_idx = seed_frame_idx // step

        frames_b64 = []
        for fp in sampled_files:
            frames_b64.append(base64.b64encode(fp.read_bytes()).decode())

        # Encode seed mask as PNG base64
        mask_pil = Image.fromarray((seed_mask * 255).astype("uint8"))
        buf = io.BytesIO()
        mask_pil.save(buf, format="PNG")
        seed_mask_b64 = base64.b64encode(buf.getvalue()).decode()

        # 3. Call MedSAM2 /propagate
        config_path = Path(__file__).parent.parent.parent.parent / "config" / "sources.yaml"
        medsam2_url = "http://10.0.0.26:9473"
        try:
            with open(config_path) as f:
                cfg = yaml.safe_load(f)
            medsam2_url = cfg.get("medsam2", {}).get("gpu_direct", medsam2_url)
        except Exception:
            pass

        logger.info(
            "MedSAM2 propagate: %d frames (sampled %d), seed=%d", len(frame_files), len(sampled_files), sampled_seed_idx
        )

        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{medsam2_url}/propagate",
                json={
                    "frames": frames_b64,
                    "seed_frame_idx": sampled_seed_idx,
                    "seed_mask": seed_mask_b64,
                    "score_threshold": 0.0,
                },
                timeout=300.0,
            )

        if resp.status_code != 200:
            msg = f"MedSAM2 propagation failed: {resp.text[:200]}"
            raise RuntimeError(msg)

        result = resp.json()
        propagated_masks = result.get("masks", [])
        logger.info("MedSAM2 returned %d masks", len(propagated_masks))

        # 4. Convert masks to CVAT polygon shapes and push
        import numpy as np
        from PIL import Image as PILImage

        cvat_shapes = []
        for i, mask_b64 in enumerate(propagated_masks):
            mask_bytes = base64.b64decode(mask_b64)
            mask_arr = np.array(PILImage.open(io.BytesIO(mask_bytes)))
            if mask_arr.max() == 0:
                continue
            # Convert mask to CVAT RLE format
            binary = (mask_arr > 128).astype(np.uint8)
            rle = self._binary_mask_to_rle(binary)
            if rle:
                # Map sampled index back to original frame index
                original_frame_idx = i * step
                cvat_shapes.append(
                    {
                        "type": "mask",
                        "frame": original_frame_idx,
                        "label_id": self._get_bone_label_id(annotations),
                        "points": rle,
                        "occluded": False,
                        "z_order": 0,
                        "attributes": [
                            {"spec_id": None, "name": "source", "value": "medsam2"},
                            {"spec_id": None, "name": "model_version", "value": "MedSAM2_latest"},
                        ],
                    }
                )

        if cvat_shapes:
            payload = {"version": 0, "shapes": cvat_shapes, "tracks": [], "tags": []}
            await self.cvat.update_annotations(cvat_task_id, payload)
            logger.info("Pushed %d MedSAM2 masks to CVAT task %d", len(cvat_shapes), cvat_task_id)

        self.task_db.update_task(task_id, has_pre_annotations=True, status="annotating")

        return {
            "task_id": task_id,
            "cvat_task_id": cvat_task_id,
            "total_frames": len(frame_files),
            "sampled_frames": len(sampled_files),
            "propagated_masks": len(cvat_shapes),
            "seed_frame": seed_frame_idx,
        }

    def _cvat_shape_to_binary(self, shape: dict, images_dir: Any, frame_idx: int) -> Any:
        """Convert a CVAT polygon/rectangle to binary mask."""
        from pathlib import Path

        import numpy as np
        from PIL import Image

        # Get image dimensions from first frame
        first_frame = sorted(Path(images_dir).glob("*.png"))[0]
        img = Image.open(first_frame)
        h, w = img.size[1], img.size[0]

        mask = np.zeros((h, w), dtype=np.uint8)
        pts = shape.get("points", [])

        if shape["type"] == "rectangle" and len(pts) >= 4:
            x1, y1, x2, y2 = int(pts[0]), int(pts[1]), int(pts[2]), int(pts[3])
            mask[y1:y2, x1:x2] = 1
        elif shape["type"] == "polygon" and len(pts) >= 6:
            import cv2

            points = np.array([(int(pts[i]), int(pts[i + 1])) for i in range(0, len(pts), 2)])
            cv2.fillPoly(mask, [points], 1)

        return mask

    def _cvat_mask_to_binary(self, shape: dict, frame_count: int) -> Any:
        """Convert CVAT RLE mask to binary numpy array."""
        import numpy as np

        pts = shape.get("points", [])
        if len(pts) < 5:
            return None
        # CVAT mask format: RLE values followed by [left, top, right, bottom]
        rle = pts[:-4]
        left, top, right, bottom = int(pts[-4]), int(pts[-3]), int(pts[-2]), int(pts[-1])
        w = right - left
        h = bottom - top

        mask_crop = np.zeros(h * w, dtype=np.uint8)
        pos = 0
        val = 0
        for run_len in rle:
            run_len = int(run_len)
            if pos + run_len > len(mask_crop):
                run_len = len(mask_crop) - pos
            mask_crop[pos : pos + run_len] = val
            pos += run_len
            val = 1 - val

        return mask_crop.reshape(h, w)

    def _binary_mask_to_rle(self, mask: Any) -> list[float]:
        """Convert binary mask to CVAT RLE format (values + bounds)."""
        import numpy as np

        # Find bounding box
        rows = np.any(mask, axis=1)
        cols = np.any(mask, axis=0)
        if not rows.any():
            return []
        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]

        # Crop mask to bounding box
        crop = mask[rmin : rmax + 1, cmin : cmax + 1].flatten()

        # RLE encode
        rle = []
        current_val = 0  # Start with 0 (background)
        count = 0
        for val in crop:
            if val == current_val:
                count += 1
            else:
                rle.append(count)
                current_val = val
                count = 1
        rle.append(count)

        # Append bounds [left, top, right, bottom]
        rle.extend([float(cmin), float(rmin), float(cmax + 1), float(rmax + 1)])
        return rle

    def _get_bone_label_id(self, annotations: dict) -> int:
        """Get the first label ID from existing annotations (for bone label)."""
        for shape in annotations.get("shapes", []):
            if "label_id" in shape:
                return shape["label_id"]
        return 0

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
