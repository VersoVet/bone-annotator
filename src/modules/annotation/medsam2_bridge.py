"""MedSAM2 temporal propagation bridge.

Handles the full flow: pull seed mask from CVAT → call MedSAM2 GPU →
convert results → push propagated masks back to CVAT.
"""

import base64
import io
import logging
from pathlib import Path
from typing import Any

import httpx
import numpy as np
import yaml
from PIL import Image

logger = logging.getLogger(__name__)

_SKILL_ROOT = Path(__file__).parent.parent.parent.parent


def _load_medsam2_url() -> str:
    """Load MedSAM2 URL from sources.yaml."""
    try:
        with open(_SKILL_ROOT / "config" / "sources.yaml") as f:
            cfg = yaml.safe_load(f)
        return cfg.get("medsam2", {}).get("gpu_direct", "http://10.0.0.26:9473")
    except Exception:
        return "http://10.0.0.26:9473"


async def propagate(
    cvat_client: Any,
    task: dict[str, Any],
    seed_frame_idx: int = 0,
) -> dict[str, Any]:
    """Propagate a seed mask across all frames via MedSAM2.

    Args:
        cvat_client: Authenticated CVATClient instance.
        task: Task dict from task_db (needs cvat_task_id, dataset_path).
        seed_frame_idx: Frame index with the seed annotation.

    Returns:
        Dict with propagation stats.
    """
    cvat_task_id = task["cvat_task_id"]
    images_dir = Path(task["dataset_path"]) / "images"

    if not images_dir.exists():
        msg = f"Dataset images not found: {images_dir}"
        raise ValueError(msg)

    # 1. Pull seed mask from CVAT
    annotations = await cvat_client.get_annotations(cvat_task_id)

    seed_mask = None
    image_size: tuple[int, int] | None = None
    if annotations and annotations.get("shapes"):
        for shape in annotations["shapes"]:
            if shape.get("frame") == seed_frame_idx:
                if shape.get("type") == "mask":
                    image_files = sorted(images_dir.glob("*.png"))
                    if not image_files:
                        raise ValueError(f"No images found in {images_dir}")
                    with Image.open(image_files[0]) as image:
                        image_size = image.size
                    seed_mask = _cvat_mask_to_binary(shape, image_size)
                    break
                elif shape.get("type") in ("polygon", "rectangle"):
                    seed_mask = _cvat_shape_to_binary(shape, images_dir)
                    break

    if seed_mask is None:
        msg = (
            f"No annotation found on frame {seed_frame_idx} in CVAT task {cvat_task_id}. "
            "Annotate at least one frame first."
        )
        raise ValueError(msg)

    # 2. Load every frame. MedSAM2 propagation is chunked below to avoid
    # silently dropping frames while keeping the original CVAT indices.
    frame_files = sorted(images_dir.glob("*.png"))
    if seed_frame_idx >= len(frame_files):
        raise ValueError(f"Seed frame {seed_frame_idx} is outside the image series")

    mask_pil = Image.fromarray((seed_mask * 255).astype(np.uint8))
    buf = io.BytesIO()
    mask_pil.save(buf, format="PNG")
    seed_mask_b64 = base64.b64encode(buf.getvalue()).decode()

    # 3. Call MedSAM2
    medsam2_url = _load_medsam2_url()
    propagated_masks = await _propagate_all_frames(
        medsam2_url,
        frame_files,
        seed_frame_idx,
        seed_mask_b64,
    )
    logger.info("MedSAM2 returned %d masks", len(propagated_masks))

    # 4. Convert to CVAT shapes and push
    label_id = _get_bone_label_id(annotations)
    cvat_shapes = []

    for frame_idx, mask_b64 in propagated_masks.items():
        mask_bytes = base64.b64decode(mask_b64)
        mask_arr = np.array(Image.open(io.BytesIO(mask_bytes)))
        if mask_arr.max() == 0:
            continue
        binary = (mask_arr > 128).astype(np.uint8)
        rle = _binary_mask_to_rle(binary)
        if rle:
            cvat_shapes.append(
                {
                    "type": "mask",
                    "frame": frame_idx,
                    "label_id": label_id,
                    "points": rle,
                    "occluded": False,
                    "z_order": 0,
                    "attributes": [],
                }
            )

    if cvat_shapes:
        payload = {"version": 0, "shapes": cvat_shapes, "tracks": [], "tags": []}
        await cvat_client.update_annotations(cvat_task_id, payload)
        logger.info("Pushed %d MedSAM2 masks to CVAT task %d", len(cvat_shapes), cvat_task_id)

    return {
        "task_id": task["id"],
        "cvat_task_id": cvat_task_id,
        "total_frames": len(frame_files),
        "sampled_frames": len(frame_files),
        "propagated_masks": len(cvat_shapes),
        "seed_frame": seed_frame_idx,
    }


# --- Mask conversion helpers ---


def _cvat_shape_to_binary(shape: dict[str, Any], images_dir: Path) -> np.ndarray:
    """Convert a CVAT polygon/rectangle to binary mask."""
    first_frame = sorted(images_dir.glob("*.png"))[0]
    img = Image.open(first_frame)
    h, w = img.size[1], img.size[0]

    mask = np.zeros((h, w), dtype=np.uint8)
    pts = shape.get("points", [])

    if shape["type"] == "rectangle" and len(pts) >= 4:
        x1, y1, x2, y2 = int(pts[0]), int(pts[1]), int(pts[2]), int(pts[3])
        mask[y1:y2, x1:x2] = 1
    elif shape["type"] == "polygon" and len(pts) >= 6:
        import cv2

        points = np.array([(int(pts[i]), int(pts[i + 1])) for i in range(0, len(pts), 2)])
        cv2.fillPoly(mask, [points], 1)

    return mask


def _cvat_mask_to_binary(
    shape: dict[str, Any],
    image_size: tuple[int, int],
) -> np.ndarray | None:
    """Convert a CVAT crop RLE to a full-image binary mask.

    Args:
        shape: CVAT mask shape containing crop RLE and left/top bounds.
        image_size: Full image size as ``(width, height)``.
    """
    pts = shape.get("points", [])
    if len(pts) < 5:
        return None
    rle = pts[:-4]
    left, top, right, bottom = int(pts[-4]), int(pts[-3]), int(pts[-2]), int(pts[-1])
    w, h = right - left, bottom - top
    image_width, image_height = image_size
    if w <= 0 or h <= 0 or left < 0 or top < 0:
        return None
    if right > image_width or bottom > image_height:
        raise ValueError("CVAT mask bounds exceed the source image")

    mask_crop = np.zeros(h * w, dtype=np.uint8)
    pos, val = 0, 0
    for run_len in rle:
        run_len = int(run_len)
        end = min(pos + run_len, len(mask_crop))
        mask_crop[pos:end] = val
        pos = end
        val = 1 - val

    mask = np.zeros((image_height, image_width), dtype=np.uint8)
    mask[top:bottom, left:right] = mask_crop.reshape(h, w)
    return mask


async def _propagate_all_frames(
    medsam2_url: str,
    frame_files: list[Path],
    seed_frame_idx: int,
    seed_mask_b64: str,
    batch_size: int = 64,
) -> dict[int, str]:
    """Propagate forward and backward in bounded batches.

    Each batch overlaps the previous batch at its seed frame. Returned masks
    are mapped to their original CVAT frame indices, so no sampling occurs.
    """
    result: dict[int, str] = {seed_frame_idx: seed_mask_b64}
    async with httpx.AsyncClient() as client:
        for direction in (1, -1):
            current_idx = seed_frame_idx
            current_mask = seed_mask_b64
            while 0 <= current_idx + direction < len(frame_files):
                if direction == 1:
                    end = min(len(frame_files) - 1, current_idx + batch_size - 1)
                    indices = list(range(current_idx, end + 1))
                else:
                    end = max(0, current_idx - batch_size + 1)
                    indices = list(range(current_idx, end - 1, -1))
                frames = [frame_files[index] for index in indices]
                response = await client.post(
                    f"{medsam2_url}/propagate",
                    json={
                        "frames": [base64.b64encode(path.read_bytes()).decode() for path in frames],
                        "seed_frame_idx": 0,
                        "seed_mask": current_mask,
                        "score_threshold": 0.0,
                    },
                    timeout=300.0,
                )
                if response.status_code != 200:
                    raise RuntimeError(f"MedSAM2 propagation failed: {response.text[:200]}")
                masks = response.json().get("masks", [])
                if len(masks) != len(indices):
                    raise RuntimeError("MedSAM2 returned an incomplete batch")
                for index, mask in zip(indices, masks):
                    result[index] = mask
                current_idx = indices[-1]
                current_mask = masks[-1]
    return result


def _binary_mask_to_rle(mask: np.ndarray) -> list[float]:
    """Convert binary mask to CVAT RLE format (values + bounds)."""
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    if not rows.any():
        return []
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]

    crop = mask[rmin : rmax + 1, cmin : cmax + 1].flatten()

    rle: list[float] = []
    current_val, count = 0, 0
    for val in crop:
        if val == current_val:
            count += 1
        else:
            rle.append(count)
            current_val = val
            count = 1
    rle.append(count)
    rle.extend([float(cmin), float(rmin), float(cmax + 1), float(rmax + 1)])
    return rle


def _get_bone_label_id(annotations: dict[str, Any]) -> int:
    """Get the first label ID from existing annotations."""
    for shape in annotations.get("shapes", []):
        if "label_id" in shape:
            return shape["label_id"]
    return 0
