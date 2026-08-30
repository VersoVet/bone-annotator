"""Notify bone-ml bonestore_catalog of annotation task status changes."""

import logging

import httpx

from src.config import get_bone_ml_config

logger = logging.getLogger(__name__)


async def notify_catalog_task_status(
    acquisition_id: str,
    task_id: int,
    status: str = "annotating",
) -> None:
    """Update current_task_id in bone-ml bonestore_catalog.

    Args:
        acquisition_id: BoneStore acquisition identifier.
        task_id: Internal annotation_tasks.id.
        status: Catalog ml_status value (e.g. annotating).
    """
    ml_config = get_bone_ml_config()
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{ml_config['base_url']}/api/boneseg/catalog/mark-status",
                json={
                    "acquisition_ids": [acquisition_id],
                    "status": status,
                    "task_id": task_id,
                },
                timeout=15.0,
            )
            if resp.status_code not in (200, 201):
                logger.debug(
                    "catalog mark-status %s for task %d: HTTP %s",
                    acquisition_id,
                    task_id,
                    resp.status_code,
                )
    except Exception as e:
        logger.debug("catalog mark-status failed for task %d: %s", task_id, e)
