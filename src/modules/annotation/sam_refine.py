"""SAM box-prompt refinement for zone masks.

Sends CPU-generated zone bounding boxes to SAM on Cortex and converts
the refined masks back to CVAT RLE format. Falls back to original CPU
masks when SAM is unreachable.
"""

from __future__ import annotations

import base64
import io
import logging
from collections import defaultdict
from pathlib import Path
from typing import Any

import httpx
import numpy as np
from PIL import Image

from .cpu_preannotate import binary_mask_to_rle, mask_to_bbox_points

logger = logging.getLogger(__name__)


def _image_to_base64(image_path: Path) -> str:
    """Read an image file and return base64-encoded PNG.

    Args:
        image_path: Path to PNG file.

    Returns:
        Base64-encoded string.
    """
    return base64.b64encode(image_path.read_bytes()).decode("ascii")


def _decode_mask_b64(mask_b64: str, shape: tuple[int, int]) -> np.ndarray | None:
    """Decode a base64-encoded mask image to binary numpy array.

    Args:
        mask_b64: Base64-encoded PNG mask.
        shape: Expected (H, W) of the output.

    Returns:
        Binary uint8 mask or None on failure.
    """
    try:
        raw = base64.b64decode(mask_b64)
        img = Image.open(io.BytesIO(raw)).convert("L")
        arr = np.array(img.resize((shape[1], shape[0]), Image.Resampling.NEAREST))
        return (arr > 128).astype(np.uint8)
    except Exception as e:
        logger.warning("Failed to decode SAM mask: %s", e)
        return None


async def refine_zone_with_sam(
    sam_url: str,
    image_b64: str,
    bbox: list[float],
    image_shape: tuple[int, int],
    *,
    timeout: float = 30.0,
) -> np.ndarray | None:
    """Send a box prompt to SAM and return the refined binary mask.

    Args:
        sam_url: SAM GPU server URL.
        image_b64: Base64-encoded frame PNG.
        bbox: Bounding box [x1, y1, x2, y2].
        image_shape: (H, W) of the image for mask decoding.
        timeout: Request timeout.

    Returns:
        Binary mask (H, W) uint8, or None if SAM fails.
    """
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{sam_url}/api/interact",
                json={"image": image_b64, "box": bbox},
                timeout=timeout,
            )
            if resp.status_code != 200:
                logger.warning("SAM interact HTTP %d", resp.status_code)
                return None
            data = resp.json()
            # Handle both response formats: {mask: b64} or {masks: [b64, ...]}
            mask_b64 = data.get("mask") or (data.get("masks", [None])[0])
            if not mask_b64:
                return None
            return _decode_mask_b64(mask_b64, image_shape)
    except (httpx.ConnectError, httpx.TimeoutException) as e:
        logger.warning("SAM unreachable: %s", e)
        return None
    except Exception as e:
        logger.warning("SAM refinement failed: %s", e)
        return None


def _shape_payload(shape_type: str, frame: int, label_id: int, points: list[float]) -> dict[str, Any]:
    """Build a CVAT shape dict."""
    return {
        "type": shape_type,
        "frame": frame,
        "label_id": label_id,
        "points": points,
        "occluded": False,
        "z_order": 0,
        "attributes": [],
    }


async def refine_all_seed_shapes(
    sam_url: str,
    frame_files: list[Path],
    shapes: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Refine all seed shapes across frames using SAM box prompts.

    Groups shapes by frame, reads each image once, and sends box prompts
    sequentially. If SAM is completely unreachable, returns original shapes.

    Args:
        sam_url: SAM GPU server URL.
        frame_files: Sorted PNG paths (index = frame number).
        shapes: CVAT shape dicts with 'frame', 'label_id', 'points'.

    Returns:
        Refined shapes (or originals if SAM down).
    """
    if not shapes:
        return shapes

    # Quick connectivity check.
    try:
        async with httpx.AsyncClient() as client:
            await client.get(f"{sam_url}/health", timeout=5.0)
    except Exception:
        logger.info("SAM unreachable at %s — keeping CPU masks", sam_url)
        return shapes

    by_frame: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for s in shapes:
        by_frame[int(s["frame"])].append(s)

    refined: list[dict[str, Any]] = []
    for frame_idx, frame_shapes in sorted(by_frame.items()):
        if frame_idx >= len(frame_files):
            refined.extend(frame_shapes)
            continue

        image_path = frame_files[frame_idx]
        image_b64 = _image_to_base64(image_path)
        with Image.open(image_path) as img:
            image_shape = (img.height, img.width)

        for shape in frame_shapes:
            bbox = mask_to_bbox_points(
                np.ones(image_shape, dtype=np.uint8)  # dummy for bbox extraction
            )
            # Extract bbox from the mask RLE points (last 4 values).
            pts = shape.get("points", [])
            if shape.get("type") == "mask" and len(pts) >= 4:
                bbox = [pts[-4], pts[-3], pts[-2], pts[-1]]
            elif shape.get("type") == "rectangle" and len(pts) >= 4:
                bbox = pts[:4]
            else:
                refined.append(shape)
                continue

            sam_mask = await refine_zone_with_sam(sam_url, image_b64, bbox, image_shape)
            if sam_mask is not None and sam_mask.any():
                rle = binary_mask_to_rle(sam_mask)
                if rle:
                    refined.append(_shape_payload("mask", frame_idx, shape["label_id"], rle))
                    continue
            # SAM failed for this zone — keep original.
            refined.append(shape)

    logger.info("SAM refinement: %d/%d shapes refined", len(refined), len(shapes))
    return refined
