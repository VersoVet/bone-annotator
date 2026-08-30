"""bone-ml BoneSeg API helpers — request bodies aligned with deployed OpenAPI."""

import logging
from typing import Any

import httpx

from src.config import get_bone_ml_config

logger = logging.getLogger(__name__)

DEFAULT_AL_BONE = "humerus"


async def fetch_catalog_stats(client: httpx.AsyncClient, bone_type: str | None = None) -> dict[str, Any]:
    """Fetch BoneSeg catalog statistics from bone-ml."""
    url = f"{get_bone_ml_config()['base_url']}/api/boneseg/catalog/stats"
    if bone_type:
        url += f"?bone_type={bone_type}"
    try:
        resp = await client.get(url, timeout=15.0)
        if resp.status_code == 200:
            data = resp.json()
            return data if isinstance(data, dict) else {}
    except Exception as e:
        logger.debug("catalog stats failed: %s", e)
    return {}


async def fetch_catalog_new(
    client: httpx.AsyncClient,
    *,
    bone_type: str | None = None,
    limit: int = 12,
) -> list[dict[str, Any]]:
    """Fetch new catalog acquisitions from bone-ml."""
    url = f"{get_bone_ml_config()['base_url']}/api/boneseg/catalog/new?limit={limit}"
    if bone_type:
        url += f"&bone_type={bone_type}"
    try:
        resp = await client.get(url, timeout=15.0)
        if resp.status_code == 200:
            data = resp.json()
            return data if isinstance(data, list) else data.get("acquisitions", [])
    except Exception as e:
        logger.debug("catalog new failed: %s", e)
    return []


async def fetch_al_suggest(
    client: httpx.AsyncClient,
    *,
    bone_type: str | None = None,
    n_suggest: int = 50,
) -> dict[str, Any]:
    """Fetch active learning suggestions and pool stats from bone-ml."""
    body = {"bone_type": bone_type or DEFAULT_AL_BONE, "n_suggest": n_suggest}
    try:
        resp = await client.post(
            f"{get_bone_ml_config()['base_url']}/api/boneseg/active-learning/suggest",
            json=body,
            timeout=60.0,
        )
        if resp.status_code == 200:
            data = resp.json()
            return data if isinstance(data, dict) else {"suggestions": data}
    except Exception as e:
        logger.debug("AL suggest failed: %s", e)
    return {}


async def mark_catalog_status(
    client: httpx.AsyncClient,
    acquisition_id: str,
    status: str,
    *,
    task_id: int | None = None,
) -> None:
    """Update bonestore_catalog status and current_task_id on bone-ml."""
    body: dict[str, Any] = {
        "acquisition_ids": [acquisition_id],
        "status": status,
    }
    if task_id is not None:
        body["task_id"] = task_id
    try:
        resp = await client.post(
            f"{get_bone_ml_config()['base_url']}/api/boneseg/catalog/mark-status",
            json=body,
            timeout=15.0,
        )
        if resp.status_code in (404, 405):
            await client.post(
                f"{get_bone_ml_config()['base_url']}/api/boneseg/catalog/mark_status",
                json={"acquisition_id": acquisition_id, "status": status, "task_id": task_id},
                timeout=15.0,
            )
    except Exception as e:
        logger.debug("mark_status skipped for %s: %s", acquisition_id, e)
