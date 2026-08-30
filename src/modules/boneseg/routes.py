"""FastAPI routes for BoneSeg orchestration."""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException, Query

from src.config import get_bone_ml_config, get_postgres_config
from src.modules.storage.decisions_db import create_decisions_db

from .decisions import log_learning_decision
from .gpu import check_gpu_available
from .learning_dashboard import get_learning_dashboard
from .model_comparison import get_model_comparison
from .models import ActiveLearningRequest, DecisionLogRequest, GpuStatus, TestSetRequest, WeeklyReportRequest
from .service import add_test_set, list_test_set, run_active_learning
from .weekly_report import generate_weekly_report

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/boneseg", tags=["boneseg"])


@router.get("/learning-dashboard")
async def learning_dashboard(
    bone_type: str | None = Query(None, description="Filter by bone type"),
) -> dict[str, Any]:
    """Full learning progress dashboard (sections 1-12)."""
    try:
        data = await get_learning_dashboard(bone_type)
        return {"status": "ok", **data}
    except Exception as e:
        logger.error("Learning dashboard failed: %s", e)
        raise HTTPException(status_code=500, detail="Learning dashboard unavailable")


@router.get("/model-comparison")
async def model_comparison(
    bone_type: str | None = Query(None),
    limit: int = Query(12, ge=1, le=48),
) -> dict[str, Any]:
    """Model vs human comparison grid (section 11)."""
    try:
        data = await get_model_comparison(bone_type, limit)
        return {"status": "ok", **data}
    except Exception as e:
        logger.error("Model comparison failed: %s", e)
        raise HTTPException(status_code=500, detail="Model comparison unavailable")


@router.get("/decisions")
async def list_decisions(
    bone_type: str | None = Query(None),
    limit: int = Query(50, ge=1, le=200),
) -> dict[str, Any]:
    """Learning decision history (section 10)."""
    db = create_decisions_db(**get_postgres_config())
    entries = db.list_decisions(limit=limit, bone_type=bone_type)
    return {"status": "ok", "entries": entries, "total": len(entries)}


@router.post("/decisions")
async def create_decision(request: DecisionLogRequest) -> dict[str, Any]:
    """Log a manual learning decision."""
    row_id = log_learning_decision(
        request.action,
        bone_type=request.bone_type,
        generation=request.generation,
        trigger_source="manual",
        payload=request.payload,
        notes=request.notes,
    )
    return {"status": "ok", "id": row_id}


@router.post("/weekly-report")
async def weekly_report(request: WeeklyReportRequest) -> dict[str, Any]:
    """Generate weekly Markdown report; optionally email (section 12)."""
    try:
        return await generate_weekly_report(send_email=request.send_email)
    except Exception as e:
        logger.error("Weekly report failed: %s", e)
        raise HTTPException(status_code=500, detail="Weekly report failed")


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
        raise HTTPException(status_code=500, detail="Failed to fetch catalog stats")
