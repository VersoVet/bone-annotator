"""Admin operations — reset and tracking overview."""

import logging
from typing import Any

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.config import get_bone_ml_config, get_dashboard_config, get_imaging_config, get_postgres_config
from src.core import __version__
from src.modules.storage.task_db import create_task_db

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/admin", tags=["admin"])


class ResetRequest(BaseModel):
    """Request to reset annotation data."""

    confirm: str = Field(..., description="Must be 'RESET' to confirm")
    include_annotations: bool = Field(default=True, description="Also delete frame_annotations")


@router.get("/settings")
async def get_settings() -> dict[str, Any]:
    """Return editable dashboard and imaging settings from YAML config."""
    return {
        "status": "ok",
        "version": __version__,
        "dashboard": get_dashboard_config(),
        "imaging": get_imaging_config(),
    }


@router.get("/tracking")
async def tracking_overview() -> dict[str, Any]:
    """Annotation tracking stats (local PG + bone-ml catalog when available)."""
    task_db = create_task_db(**get_postgres_config())
    local = task_db.get_tracking_stats()
    catalog: dict[str, Any] = {}
    try:
        ml_config = get_bone_ml_config()
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                f"{ml_config['base_url']}/api/boneseg/catalog/stats",
                timeout=10.0,
            )
            if resp.status_code == 200:
                catalog = resp.json()
    except Exception as e:
        logger.debug("bone-ml catalog stats unavailable: %s", e)
        catalog = {"error": "bone-ml unavailable", "local_catalog_total": local.get("catalog_total", 0)}

    return {"status": "ok", "local": local, "catalog": catalog}


@router.post("/reset")
async def reset_annotations(request: ResetRequest) -> dict[str, Any]:
    """Reset annotation tasks and optionally stored annotations."""
    if request.confirm != "RESET":
        raise HTTPException(status_code=400, detail="confirm must be 'RESET'")
    task_db = create_task_db(**get_postgres_config())
    deleted = task_db.reset_annotation_data(include_annotations=request.include_annotations)
    return {"status": "ok", **deleted}
