"""SAM proxy — forwards segmentation requests to ml-compute GPU cluster.

Supports multiple SAM models (vit_b, vit_l, vit_h, medsam).
ml-compute manages GPU allocation via Nomad.
"""

import logging

import httpx
from fastapi import APIRouter, HTTPException, Request

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/sam", tags=["sam"])

ML_COMPUTE_SAM = "http://10.0.0.44:9469/api/serve/sam"
SAM_GPU_DIRECT = "http://10.0.0.26:9470"


@router.get("/status")
async def sam_status() -> dict:
    """Check SAM GPU service status via ml-compute."""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{ML_COMPUTE_SAM}/status", timeout=5.0)
            return resp.json()
    except Exception as e:
        logger.error("SAM status failed: %s", e)
        raise HTTPException(status_code=503, detail="SAM unavailable")


@router.post("/embed")
async def sam_embed(request: Request) -> dict:
    """Get SAM image embeddings (CVAT interactor protocol).

    CVAT sends {"image": "<base64>"}, returns {"blob": "<base64 embeddings>"}.
    """
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{SAM_GPU_DIRECT}/api/embed",
                json=await request.json(),
                timeout=30.0,
            )
            return resp.json()
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="SAM embed timeout")
    except Exception as e:
        logger.error("SAM embed failed: %s", e)
        raise HTTPException(status_code=503, detail="SAM unavailable")


@router.post("/segment")
async def sam_segment(request: Request) -> dict:
    """Full SAM segmentation (points → mask)."""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{SAM_GPU_DIRECT}/api/interact",
                json=await request.json(),
                timeout=30.0,
            )
            return resp.json()
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="SAM segment timeout")
    except Exception as e:
        logger.error("SAM segment failed: %s", e)
        raise HTTPException(status_code=503, detail="SAM unavailable")


@router.get("/models")
async def sam_models() -> dict:
    """List available SAM models."""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{ML_COMPUTE_SAM}/models", timeout=5.0)
            return resp.json()
    except Exception:
        return {
            "models": [
                {"name": "vit_b", "description": "SAM ViT-B (fast)", "active": True},
                {"name": "vit_l", "description": "SAM ViT-L (balanced)"},
                {"name": "vit_h", "description": "SAM ViT-H (best quality)"},
                {"name": "medsam", "description": "MedSAM (medical imaging)"},
            ]
        }
