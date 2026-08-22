"""SAM proxy — forwards segmentation requests to ml-compute Ray cluster."""

import logging

import httpx
from fastapi import APIRouter, HTTPException, Request

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/sam", tags=["sam"])

ML_COMPUTE_SAM_URL = "http://10.0.0.44:9469/api/serve/sam"


@router.get("/status")
async def sam_status() -> dict:
    """Check SAM GPU service status via ml-compute."""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{ML_COMPUTE_SAM_URL}/status", timeout=5.0)
            return resp.json()
    except Exception as e:
        logger.error("SAM status check failed: %s", e)
        raise HTTPException(status_code=503, detail="SAM service unavailable")


@router.post("/segment")
async def sam_segment(request: Request) -> dict:
    """Segment an image using SAM via ml-compute GPU cluster."""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{ML_COMPUTE_SAM_URL}/interact",
                json=await request.json(),
                timeout=30.0,
            )
            return resp.json()
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="SAM inference timeout")
    except Exception as e:
        logger.error("SAM segment failed: %s", e)
        raise HTTPException(status_code=503, detail="SAM service unavailable")
