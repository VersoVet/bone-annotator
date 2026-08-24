"""SAM proxy — forwards segmentation requests to SAM GPU server on OnyxCortex.

Supports multiple SAM models (vit_b, vit_l, vit_h, medsam).
Model switching is handled by the SAM server at runtime.
"""

import logging
from pathlib import Path
from typing import Any

import httpx
import yaml
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/sam", tags=["sam"])


def _load_sam_config() -> dict[str, Any]:
    """Load SAM config from sources.yaml."""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "sources.yaml"
    try:
        with open(config_path) as f:
            config = yaml.safe_load(f)
        return config.get("sam", {})
    except Exception:
        logger.warning("Cannot load SAM config, using defaults")
        return {}


_sam_config = _load_sam_config()
SAM_GPU_URL = _sam_config.get("gpu_direct", "http://10.0.0.26:9470")
SAM_DEFAULT_MODEL = _sam_config.get("default_model", "vit_b")


class SwitchModelRequest(BaseModel):
    """Request to switch SAM model."""

    model: str


@router.get("/status")
async def sam_status() -> dict[str, Any]:
    """Check SAM GPU service status."""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{SAM_GPU_URL}/health", timeout=5.0)
            return resp.json()
    except Exception as e:
        logger.error("SAM status failed: %s", e)
        raise HTTPException(status_code=503, detail="SAM unavailable")


@router.post("/embed")
async def sam_embed(request: Request, model: str | None = None) -> dict[str, Any]:
    """Get SAM image embeddings (CVAT interactor protocol).

    Args:
        request: Raw request with image data.
        model: Optional model name to use (switches if needed).

    Returns:
        Embeddings blob.
    """
    await _ensure_model(model)
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{SAM_GPU_URL}/api/embed",
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
async def sam_segment(request: Request, model: str | None = None) -> dict[str, Any]:
    """Full SAM segmentation (points/box -> mask).

    Args:
        request: Raw request with image and prompts.
        model: Optional model name to use (switches if needed).

    Returns:
        Segmentation masks and scores.
    """
    await _ensure_model(model)
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{SAM_GPU_URL}/api/interact",
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
async def sam_models() -> dict[str, Any]:
    """List available SAM models from GPU server."""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{SAM_GPU_URL}/models", timeout=5.0)
            return resp.json()
    except Exception:
        return {
            "models": [
                {"name": "vit_b", "description": "SAM ViT-B (fast)"},
                {"name": "medsam", "description": "MedSAM (medical imaging)"},
            ],
            "note": "SAM server unreachable, showing defaults",
        }


@router.post("/switch-model")
async def sam_switch_model(request: SwitchModelRequest) -> dict[str, Any]:
    """Switch the active SAM model on GPU server.

    Args:
        request: Model name to switch to.

    Returns:
        Switch result with new active model.
    """
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{SAM_GPU_URL}/switch-model",
                json={"model": request.model},
                timeout=60.0,
            )
            if resp.status_code != 200:
                raise HTTPException(
                    status_code=resp.status_code,
                    detail=resp.json().get("detail", "Switch failed"),
                )
            return resp.json()
    except HTTPException:
        raise
    except Exception as e:
        logger.error("SAM switch-model failed: %s", e)
        raise HTTPException(status_code=503, detail="SAM unavailable")


async def _ensure_model(model: str | None) -> None:
    """Switch SAM model if a specific model is requested.

    Args:
        model: Model name, or None to keep current.
    """
    if model is None:
        return
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{SAM_GPU_URL}/switch-model",
                json={"model": model},
                timeout=60.0,
            )
            if resp.status_code == 200:
                logger.info("SAM model switched to %s", model)
    except Exception as e:
        logger.warning("Could not switch SAM model to %s: %s", model, e)
