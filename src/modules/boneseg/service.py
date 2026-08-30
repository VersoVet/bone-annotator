"""BoneSeg orchestration — active learning, test set, GPU coordination."""

import logging
from typing import Any

import httpx

from src.config import get_bone_ml_config, get_imaging_config, get_postgres_config
from src.modules.annotation.models import CreateTaskRequest
from src.modules.annotation.service import get_service as get_annotation_service
from src.modules.storage.learning_db import create_learning_db

from .gpu import check_gpu_available
from .models import ActiveLearningResult

logger = logging.getLogger(__name__)

__all__ = ["check_gpu_available", "run_active_learning", "add_test_set", "list_test_set"]


async def run_active_learning(
    *,
    bone_type: str | None = None,
    limit: int = 5,
    pipeline_preset: str | None = None,
    pre_annotate: bool = True,
) -> ActiveLearningResult:
    """Run one active learning cycle: sync catalog, suggest, create CVAT tasks.

    Args:
        bone_type: Optional bone type filter for suggestions.
        limit: Maximum number of annotation tasks to create.
        pipeline_preset: Imaging pipeline for prepared datasets.
        pre_annotate: Whether to request ML pre-annotation on new tasks.

    Returns:
        ActiveLearningResult with sync stats and created tasks.
    """
    if pipeline_preset is None:
        pipeline_preset = get_imaging_config()["default_treatment"]
    ml_config = get_bone_ml_config()
    learning_db = create_learning_db(**get_postgres_config())
    annotation_svc = get_annotation_service()
    result = ActiveLearningResult()

    async with httpx.AsyncClient() as client:
        sync_resp = await client.post(
            f"{ml_config['base_url']}/api/boneseg/catalog/sync",
            timeout=120.0,
        )
        if sync_resp.status_code == 200:
            result.synced = sync_resp.json()

        suggest_body: dict[str, Any] = {"limit": limit}
        if bone_type:
            suggest_body["bone_type"] = bone_type
        suggest_resp = await client.post(
            f"{ml_config['base_url']}/api/boneseg/active-learning/suggest",
            json=suggest_body,
            timeout=60.0,
        )
        if suggest_resp.status_code != 200:
            logger.warning("Active learning suggest failed: %s", suggest_resp.text[:200])
            return result

        suggestions = suggest_resp.json()
        if isinstance(suggestions, dict):
            items = suggestions.get("suggestions", suggestions.get("acquisitions", []))
        else:
            items = suggestions
        result.suggestions = items if isinstance(items, list) else []

        for item in result.suggestions[:limit]:
            acq_id = item.get("acquisition_id") or item.get("id", "")
            item_bone = item.get("bone_type") or bone_type or "unknown"
            if not acq_id:
                continue
            if learning_db.is_in_test_set(item_bone, acq_id):
                result.skipped.append(f"{acq_id}:in_test_set")
                continue

            try:
                task = await annotation_svc.create_task(
                    CreateTaskRequest(
                        acquisition_id=acq_id,
                        bone_type=item_bone,
                        region="entire",
                        assignee=None,
                        pipeline_preset=pipeline_preset,
                        pre_annotate=pre_annotate,
                    )
                )
                result.tasks_created.append({"task_id": task.id, "acquisition_id": acq_id, "bone_type": item_bone})
                await client.post(
                    f"{ml_config['base_url']}/api/boneseg/catalog/mark_status",
                    json={"acquisition_id": acq_id, "status": "annotating"},
                    timeout=15.0,
                )
            except Exception as e:
                logger.warning("Failed to create AL task for %s: %s", acq_id, e)
                result.skipped.append(f"{acq_id}:{e}")

    return result


def add_test_set(bone_type: str, acquisition_ids: list[str]) -> dict[str, Any]:
    """Add acquisitions to the frozen test set.

    Args:
        bone_type: Bone type partition.
        acquisition_ids: Acquisition IDs to freeze.

    Returns:
        Dict with inserted count and total entries for the bone type.
    """
    learning_db = create_learning_db(**get_postgres_config())
    inserted = learning_db.add_test_set_entries(bone_type, acquisition_ids)
    entries = learning_db.list_test_set(bone_type)
    return {"inserted": inserted, "bone_type": bone_type, "total": len(entries)}


def list_test_set(bone_type: str | None = None) -> list[dict[str, Any]]:
    """List frozen test set acquisitions."""
    learning_db = create_learning_db(**get_postgres_config())
    return learning_db.list_test_set(bone_type)
