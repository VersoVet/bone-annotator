"""MedSAM2 temporal propagation proxy.

Forwards propagation requests to MedSAM2 GPU server on OnyxCortex.
Used for bone annotation: annotate 1 frame, propagate to entire series.
"""

import logging
from pathlib import Path
from typing import Any

import httpx
import yaml
from fastapi import APIRouter, HTTPException, Request

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/medsam2", tags=["medsam2"])


def _load_medsam2_url() -> str:
    """Load MedSAM2 URL from sources.yaml."""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "sources.yaml"
    try:
        with open(config_path) as f:
            config = yaml.safe_load(f)
        return config.get("medsam2", {}).get("gpu_direct", "http://10.0.0.26:9473")
    except Exception:
        return "http://10.0.0.26:9473"


MEDSAM2_URL = _load_medsam2_url()


@router.get("/status")
async def medsam2_status() -> dict[str, Any]:
    """Check MedSAM2 server status."""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{MEDSAM2_URL}/health", timeout=5.0)
            return resp.json()
    except Exception as e:
        logger.error("MedSAM2 status failed: %s", e)
        raise HTTPException(status_code=503, detail="MedSAM2 unavailable")


@router.post("/propagate")
async def propagate(request: Request) -> dict[str, Any]:
    """Propagate a seed mask across all frames in a series.

    Proxy to MedSAM2 server /propagate endpoint.

    Body: {frames: [base64...], seed_frame_idx: int, seed_mask: base64}
    Returns: {masks: [base64...], frame_count: int}
    """
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{MEDSAM2_URL}/propagate",
                json=await request.json(),
                timeout=300.0,  # Propagation can take minutes for large series
            )
            if resp.status_code != 200:
                raise HTTPException(status_code=resp.status_code, detail=resp.text[:200])
            return resp.json()
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="MedSAM2 propagation timeout")
    except HTTPException:
        raise
    except Exception as e:
        logger.error("MedSAM2 propagation failed: %s", e)
        raise HTTPException(status_code=503, detail="MedSAM2 unavailable")


@router.post("/segment")
async def segment(request: Request) -> dict[str, Any]:
    """Single-frame segmentation with MedSAM2 (medical-tuned).

    Body: {image: base64, points: [[x,y],...], box: [x1,y1,x2,y2]}
    Returns: {mask: base64, mask_area: int}
    """
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{MEDSAM2_URL}/segment",
                json=await request.json(),
                timeout=30.0,
            )
            return resp.json()
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="MedSAM2 segment timeout")
    except Exception as e:
        logger.error("MedSAM2 segment failed: %s", e)
        raise HTTPException(status_code=503, detail="MedSAM2 unavailable")
