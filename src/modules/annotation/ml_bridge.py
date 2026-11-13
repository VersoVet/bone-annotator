"""Bridge to bone-ml for pre-annotation and training triggers."""

import logging
from typing import Any

import httpx

from src.config import get_bone_ml_config
from src.modules.boneseg.gpu import check_gpu_available

logger = logging.getLogger(__name__)


def _is_success_status(status: str) -> bool:
    """Return True when a bone-ml status indicates real annotations were produced."""
    if not status:
        return False
    lowered = status.lower()
    if lowered.startswith("error") or lowered.startswith("deferred"):
        return False
    if "no boneseg model" in lowered or "not found" in lowered:
        return False
    # "started" alone is not proof that shapes were pushed.
    if lowered in {"started", "unknown", "queued"}:
        return False
    return True


async def call_bone_ml_annotate(
    cvat_task_id: int,
    bone_type: str | None = None,
    objective: str | None = None,
) -> str:
    """Call bone-ml to pre-annotate a CVAT task.

    Tries BoneSeg first, then multitask, then YOLO fallback.
    Returns a status string; callers must treat non-success as fallback trigger.

    Args:
        cvat_task_id: CVAT task identifier.
        bone_type: Optional bone type for model routing.
        objective: Optional objective for model routing.

    Returns:
        Status string from bone-ml or error/deferred descriptor.
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
                    if "error" not in data and "detail" not in data:
                        status = str(data.get("status", "ok_boneseg"))
                        if _is_success_status(status):
                            return status
                        logger.info("BoneSeg annotate non-final status: %s", data)
                    else:
                        logger.info("BoneSeg annotate rejected: %s", data)
                else:
                    logger.info("BoneSeg annotate HTTP %s: %s", resp.status_code, resp.text[:200])
            except Exception as e:
                logger.info("BoneSeg annotate unavailable: %s", e)

            # 2. Multitask endpoint if bone_type is provided
            if bone_type:
                try:
                    resp = await client.post(
                        f"{ml_config['base_url']}/api/multitask/annotate",
                        json={"task_id": cvat_task_id, "bone_type": bone_type},
                        timeout=60.0,
                    )
                    if resp.status_code == 200:
                        status = str(resp.json().get("status", "multitask_ok"))
                        if _is_success_status(status):
                            return status
                    else:
                        logger.info("Multitask annotate HTTP %s", resp.status_code)
                except Exception as e:
                    logger.info("Multitask annotate unavailable: %s", e)

            # 3. YOLO fallback — defer if GPU is busy with training
            gpu = await check_gpu_available()
            if not gpu.available:
                return f"deferred:{gpu.reason or 'gpu_unavailable'}"

            try:
                status_resp = await client.get(
                    f"{ml_config['base_url']}/api/training/status",
                    timeout=5.0,
                )
                if status_resp.status_code == 200:
                    if status_resp.json().get("status", "") in ("running", "training"):
                        return "deferred:training_active"
            except Exception:
                pass

            resp = await client.post(
                f"{ml_config['base_url']}/api/cvat/annotate",
                json={"task_id": cvat_task_id},
                timeout=30.0,
            )
            if resp.status_code != 200:
                return f"error:yolo_http_{resp.status_code}"
            status = str(resp.json().get("status", "unknown"))
            if _is_success_status(status):
                return status
            # bone-ml often returns {"status":"started"} without pushing shapes
            return f"error:yolo_nonfinal:{status}"
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
