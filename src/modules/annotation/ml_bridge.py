"""Bridge to bone-ml for pre-annotation and training triggers."""

import logging
from typing import Any

import httpx

from src.config import get_bone_ml_config
from src.modules.boneseg.gpu import check_gpu_available

logger = logging.getLogger(__name__)


async def call_bone_ml_annotate(
    cvat_task_id: int,
    bone_type: str | None = None,
    objective: str | None = None,
) -> str:
    """Call bone-ml to pre-annotate a CVAT task.

    Tries BoneSeg first, then multitask, then YOLO fallback.

    Args:
        cvat_task_id: CVAT task identifier.
        bone_type: Optional bone type for model routing.
        objective: Optional objective for model routing (segmentation, measurement, classification).

    Returns:
        Status string from bone-ml or error descriptor.
    """
    ml_config = get_bone_ml_config()
    try:
        async with httpx.AsyncClient() as client:
            # 1. BoneSeg segmentation (preferred when model exists)
            try:
                boneseg_body: dict[str, Any] = {"cvat_task_id": cvat_task_id}
                if bone_type:
                    boneseg_body["bone_type"] = bone_type
                if objective:
                    boneseg_body["objective"] = objective
                resp = await client.post(
                    f"{ml_config['base_url']}/api/boneseg/annotate",
                    json=boneseg_body,
                    timeout=120.0,
                )
                if resp.status_code == 200:
                    data = resp.json()
                    if "error" not in data:
                        return data.get("status", "ok_boneseg")
            except Exception:
                pass

            # 2. Multitask endpoint if bone_type is provided
            if bone_type:
                try:
                    resp = await client.post(
                        f"{ml_config['base_url']}/api/multitask/annotate",
                        json={"task_id": cvat_task_id, "bone_type": bone_type},
                        timeout=60.0,
                    )
                    if resp.status_code == 200:
                        return resp.json().get("status", "multitask_ok")
                except Exception:
                    pass

            # 3. YOLO fallback — defer if GPU is busy with training
            gpu = await check_gpu_available()
            if not gpu.available:
                return f"deferred:{gpu.reason}"

            status_resp = await client.get(
                f"{ml_config['base_url']}/api/training/status",
                timeout=5.0,
            )
            if status_resp.status_code == 200:
                if status_resp.json().get("status", "") in ("running", "training"):
                    return "deferred:training_active"

            resp = await client.post(
                f"{ml_config['base_url']}/api/cvat/annotate",
                json={"task_id": cvat_task_id},
                timeout=30.0,
            )
            return resp.json().get("status", "unknown")
    except Exception as e:
        logger.error("bone-ml pre-annotation failed: %s", e)
        return f"error: {e}"


async def maybe_trigger_training(
    conn: Any,
    bone_type: str,
    threshold: int = 10,
) -> None:
    """Trigger fine-tuning if enough validated tasks since last training run."""
    gpu = await check_gpu_available()
    if not gpu.available:
        logger.info("Training deferred for %s: %s", bone_type, gpu.reason)
        return

    try:
        last_run = conn.execute(
            """SELECT MAX(completed_at) FROM bone_annotations.training_runs
            WHERE bone_type=%s AND status='completed'""",
            (bone_type,),
        ).fetchone()
        since = last_run[0] if last_run and last_run[0] else None
        if since:
            count = conn.execute(
                """SELECT COUNT(*) FROM bone_annotations.annotation_tasks
                WHERE bone_type=%s AND status='validated' AND validated_at > %s""",
                (bone_type, since),
            ).fetchone()[0]
        else:
            count = conn.execute(
                """SELECT COUNT(*) FROM bone_annotations.annotation_tasks
                WHERE bone_type=%s AND status='validated'""",
                (bone_type,),
            ).fetchone()[0]
        if count >= threshold:
            ml_config = get_bone_ml_config()
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    f"{ml_config['base_url']}/api/training/fine-tune",
                    json={"bone_type": bone_type},
                    timeout=10.0,
                )
                data = resp.json()
                logger.info("Training triggered for %s: %s", bone_type, data.get("status"))
    except Exception as e:
        logger.warning("Training trigger check failed: %s", e)
