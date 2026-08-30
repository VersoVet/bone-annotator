"""FastAPI routes for BoneSeg orchestration."""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException, Query

from src.config import get_bone_ml_config

from .gpu import check_gpu_available
from .models import ActiveLearningRequest, GpuStatus, TestSetRequest
from .service import add_test_set, list_test_set, run_active_learning

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/boneseg", tags=["boneseg"])


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
