"""FastAPI routes for BoneSeg orchestration."""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException, Query

from src.config import get_bone_ml_config

from .gpu import check_gpu_available
from .learning_dashboard import get_learning_dashboard
from .models import ActiveLearningRequest, GpuStatus, TestSetRequest
from .service import add_test_set, list_test_set, run_active_learning

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/boneseg", tags=["boneseg"])


@router.get("/learning-dashboard")
async def learning_dashboard(
    bone_type: str | None = Query(None, description="Filter by bone type"),
) -> dict[str, Any]:
    """Full learning progress dashboard (sections 1-7)."""
    try:
        data = await get_learning_dashboard(bone_type)
        return {"status": "ok", **data}
    except Exception as e:
        logger.error("Learning dashboard failed: %s", e)
        raise HTTPException(status_code=500, detail="Learning dashboard unavailable")


@router.get("/gpu-status")
async def gpu_status() -> GpuStatus:
    """Check shared GPU availability before training or uncertainty scoring."""
    return await check_gpu_available()


@router.post("/active-learning/run")
async def active_learning_run(request: ActiveLearningRequest) -> dict[str, Any]:
    """Sync BoneStore catalog, suggest acquisitions, and create CVAT tasks."""
    gpu = await check_gpu_available()
    if not gpu.available and gpu.boneseg_running:
        raise HTTPException(status_code=409, detail=f"GPU busy: {gpu.reason}")
    try:
        result = await run_active_learning(
            bone_type=request.bone_type,
            limit=request.limit,
            pipeline_preset=request.pipeline_preset,
            pre_annotate=request.pre_annotate,
        )
        return {"status": "ok", **result.model_dump()}
    except Exception as e:
        logger.error("Active learning run failed: %s", e)
        raise HTTPException(status_code=500, detail="Active learning failed")


@router.post("/test-set")
async def create_test_set(request: TestSetRequest) -> dict[str, Any]:
    """Add acquisitions to the frozen test set (never used for training)."""
    try:
        result = add_test_set(request.bone_type, request.acquisition_ids)
        return {"status": "ok", **result}
    except Exception as e:
        logger.error("Test set update failed: %s", e)
        raise HTTPException(status_code=500, detail="Failed to update test set")


@router.get("/test-set")
async def get_test_set(
    bone_type: str | None = Query(None, description="Filter by bone type"),
) -> dict[str, Any]:
    """List frozen test set acquisitions."""
    entries = list_test_set(bone_type)
    return {"status": "ok", "entries": entries, "total": len(entries)}


@router.post("/catalog/sync")
async def catalog_sync(bone_type: str | None = None) -> dict[str, Any]:
    """Proxy BoneStore catalog sync to bone-ml."""
    import httpx

    ml_config = get_bone_ml_config()
    try:
        async with httpx.AsyncClient() as client:
            url = f"{ml_config['base_url']}/api/boneseg/catalog/sync"
            params = {"bone_type": bone_type} if bone_type else None
            resp = await client.post(url, params=params, timeout=120.0)
            if resp.status_code != 200:
                raise HTTPException(status_code=502, detail="bone-ml catalog sync failed")
            return {"status": "ok", **resp.json()}
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Catalog sync failed: %s", e)
        raise HTTPException(status_code=502, detail="Catalog sync failed")


@router.get("/catalog/stats")
async def catalog_stats() -> dict[str, Any]:
    """Proxy BoneSeg catalog statistics from bone-ml."""
    import httpx

    ml_config = get_bone_ml_config()
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                f"{ml_config['base_url']}/api/boneseg/catalog/stats",
                timeout=15.0,
            )
            if resp.status_code != 200:
                raise HTTPException(status_code=502, detail="bone-ml catalog stats unavailable")
            return {"status": "ok", "stats": resp.json()}
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Catalog stats proxy failed: %s", e)
        raise HTTPException(status_code=502, detail="Failed to fetch catalog stats")
