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
        return cfg.get("medsam2", {}).get("gpu_direct", "http://10.0.0.73:9473")
    except Exception:
        return "http://10.0.0.73:9473"


async def propagate(
    cvat_client: Any,
    task: dict[str, Any],
    seed_frame_idx: int = 0,
    label_ids: list[int] | None = None,
) -> dict[str, Any]:
    """Propagate seed masks across all frames via MedSAM2.

    Supports multi-label: each label on the seed frame is propagated
    sequentially (one GPU pass per label).

    Args:
        cvat_client: Authenticated CVATClient instance.
        task: Task dict from task_db (needs cvat_task_id, dataset_path).
        seed_frame_idx: Frame index with the seed annotation.
        label_ids: Optional list of label IDs to propagate. None = all.

    Returns:
        Dict with propagation stats.

    Raises:
        ValueError: If dataset images are missing or seed frame index is out of range.
    """
    cvat_task_id = task["cvat_task_id"]
    images_dir = Path(task["dataset_path"]) / "images"

    if not images_dir.exists():
        msg = f"Dataset images not found: {images_dir}"
        raise ValueError(msg)

    # 1. Pull seed annotations from CVAT
    annotations = await cvat_client.get_annotations(cvat_task_id)

    frame_files = sorted(images_dir.glob("*.png"))
    if seed_frame_idx >= len(frame_files):
        raise ValueError(f"Seed frame {seed_frame_idx} is outside the image series")

    # Group seed shapes by label_id
    seed_shapes: dict[int, dict[str, Any]] = {}
    if annotations and annotations.get("shapes"):
        for shape in annotations["shapes"]:
            if shape.get("frame") != seed_frame_idx:
                continue
            lid = shape.get("label_id", 0)
            if lid in seed_shapes:
                continue
            seed_shapes[lid] = shape

    if not seed_shapes:
        msg = (
            f"No annotation found on frame {seed_frame_idx} in CVAT task {cvat_task_id}. "
            "Annotate at least one frame first."
        )
        raise ValueError(msg)

    # Filter to requested label_ids if provided
    if label_ids:
        seed_shapes = {lid: s for lid, s in seed_shapes.items() if lid in label_ids}
        if not seed_shapes:
            raise ValueError(f"None of the requested label_ids {label_ids} found on frame {seed_frame_idx}")

    # Resolve image size
    with Image.open(frame_files[0]) as img:
        image_size = img.size

    medsam2_url = _load_medsam2_url()
    all_cvat_shapes: list[dict[str, Any]] = []

    # 2. Propagate each label sequentially (one GPU, one mask at a time)
    for label_id, shape in seed_shapes.items():
        logger.info("Propagating label_id=%d on %d frames...", label_id, len(frame_files))

        if shape.get("type") == "mask":
            seed_mask = _cvat_mask_to_binary(shape, image_size)
        elif shape.get("type") in ("polygon", "rectangle"):
            seed_mask = _cvat_shape_to_binary(shape, images_dir)
        else:
            logger.warning("Unsupported shape type %s for label %d", shape.get("type"), label_id)
            continue

        if seed_mask is None:
            continue

        mask_pil = Image.fromarray((seed_mask * 255).astype(np.uint8))
        buf = io.BytesIO()
        mask_pil.save(buf, format="PNG")
        seed_mask_b64 = base64.b64encode(buf.getvalue()).decode()

        propagated_masks = await _propagate_all_frames(
            medsam2_url,
            frame_files,
            seed_frame_idx,
            seed_mask_b64,
            mask_format="rle",
        )
        mask_fmt = propagated_masks.pop("_format", "png")
        logger.info("MedSAM2 returned %d masks (fmt=%s) for label %d", len(propagated_masks), mask_fmt, label_id)

        for frame_idx, mask_data in propagated_masks.items():
            if not isinstance(frame_idx, int):
                continue
            # Seed frame mask is always PNG b64 regardless of server format
            fmt = "png" if frame_idx == seed_frame_idx else mask_fmt
            binary = _decode_propagated_mask(mask_data, fmt)
            if binary is None or binary.max() == 0:
                continue
            rle = _binary_mask_to_rle(binary)
            if rle:
                all_cvat_shapes.append(
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

    # 3. Push all propagated masks to CVAT
    if all_cvat_shapes:
        payload = {"version": 0, "shapes": all_cvat_shapes, "tracks": [], "tags": []}
        await cvat_client.update_annotations(cvat_task_id, payload)
        logger.info(
            "Pushed %d MedSAM2 masks (%d labels) to CVAT task %d", len(all_cvat_shapes), len(seed_shapes), cvat_task_id
        )

    return {
        "task_id": task["id"],
        "cvat_task_id": cvat_task_id,
        "total_frames": len(frame_files),
        "labels_propagated": len(seed_shapes),
        "propagated_masks": len(all_cvat_shapes),
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
        cv2.fillPoly(mask, [points], 1)  # type: ignore[call-overload]

    return mask


def _cvat_mask_to_binary(
    shape: dict[str, Any],
    image_size: tuple[int, int],
) -> np.ndarray | None:
    """Convert a CVAT crop RLE to a full-image binary mask.

    Args:
        shape: CVAT mask shape containing crop RLE and left/top bounds.
        image_size: Full image size as ``(width, height)``.

    Returns:
        Binary mask array of shape ``(height, width)``, or None if shape data is invalid.

    Raises:
        ValueError: If mask bounds exceed the source image dimensions.
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


def _decode_propagated_mask(mask_data: str, fmt: str) -> np.ndarray | None:
    """Decode a mask returned by MedSAM2 server.

    Args:
        mask_data: Encoded mask string (RLE or PNG base64).
        fmt: Format identifier — ``"rle"`` or ``"png"``.

    Returns:
        Binary numpy mask, or None on decode failure.
    """
    if fmt == "rle":
        return _decode_rle(mask_data)
    # PNG base64 fallback
    mask_bytes = base64.b64decode(mask_data)
    mask_arr = np.array(Image.open(io.BytesIO(mask_bytes)))
    return (mask_arr > 128).astype(np.uint8)


def _decode_rle(rle_str: str) -> np.ndarray | None:
    """Decode server RLE format ``"h,w|run0,run1,..."`` to binary mask.

    Args:
        rle_str: RLE-encoded mask string from MedSAM2 server.

    Returns:
        Binary numpy mask of shape ``(h, w)``, or None on parse error.
    """
    try:
        header, runs_str = rle_str.split("|", 1)
        h, w = (int(x) for x in header.split(","))
        flat = np.zeros(h * w, dtype=np.uint8)
        pos, val = 0, 0
        for run in runs_str.split(","):
            length = int(run)
            end = min(pos + length, len(flat))
            flat[pos:end] = val
            pos = end
            val = 1 - val
        return flat.reshape(h, w)
    except Exception:
        logger.warning("Failed to decode RLE mask (len=%d)", len(rle_str))
        return None


async def _read_frames_b64(frame_files: list[Path]) -> list[str]:
    """Read frame files and encode as base64 off the event loop.

    Args:
        frame_files: Ordered list of PNG frame paths.

    Returns:
        List of base64-encoded file contents.
    """
    import asyncio

    def _read_all() -> list[str]:
        return [base64.b64encode(p.read_bytes()).decode() for p in frame_files]

    return await asyncio.to_thread(_read_all)


async def _propagate_all_frames(
    medsam2_url: str,
    frame_files: list[Path],
    seed_frame_idx: int,
    seed_mask_b64: str,
    batch_size: int = 64,
    mask_format: str = "rle",
) -> dict[int, Any]:
    """Propagate forward and backward in bounded batches.

    Each batch overlaps the previous batch at its seed frame. Returned masks
    are mapped to their original CVAT frame indices, so no sampling occurs.

    Args:
        medsam2_url: MedSAM2 server URL.
        frame_files: All frame file paths in order.
        seed_frame_idx: Index of the seed frame.
        seed_mask_b64: PNG base64 seed mask (always PNG for the seed).
        batch_size: Max frames per GPU batch.
        mask_format: Encoding for returned masks — ``"rle"`` or ``"png"``.

    Returns:
        Dict mapping frame index to encoded mask string, plus ``_format`` key.
    """
    import time

    result: dict[int, Any] = {seed_frame_idx: seed_mask_b64, "_format": mask_format}
    t_total = time.monotonic()
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
                frames_b64 = await _read_frames_b64(frames)
                t_batch = time.monotonic()
                response = await client.post(
                    f"{medsam2_url}/propagate",
                    json={
                        "frames": frames_b64,
                        "seed_frame_idx": 0,
                        "seed_mask": current_mask,
                        "score_threshold": 0.0,
                        "mask_format": mask_format,
                    },
                    timeout=300.0,
                )
                if response.status_code != 200:
                    raise RuntimeError(f"MedSAM2 propagation failed: {response.text[:200]}")
                data = response.json()
                actual_format = data.get("mask_format", "png")
                masks = data.get("masks", [])
                if len(masks) != len(indices):
                    raise RuntimeError("MedSAM2 returned an incomplete batch")
                server_elapsed = data.get("elapsed_seconds", 0)
                server_fps = data.get("fps", 0)
                logger.info(
                    "Batch %d frames (dir=%+d, %s): server %.1fs (%.1f fps), roundtrip %.1fs",
                    len(indices),
                    direction,
                    actual_format,
                    server_elapsed,
                    server_fps,
                    time.monotonic() - t_batch,
                )
                result["_format"] = actual_format
                for index, mask in zip(indices, masks):
                    result[index] = mask
                # Seed mask for next batch: last mask of this batch (always PNG for server input)
                if actual_format == "rle":
                    last_binary = _decode_rle(masks[-1])
                    if last_binary is not None:
                        pil = Image.fromarray((last_binary * 255).astype(np.uint8))
                        buf = io.BytesIO()
                        pil.save(buf, format="PNG")
                        current_mask = base64.b64encode(buf.getvalue()).decode()
                    else:
                        current_mask = masks[-1]
                else:
                    current_mask = masks[-1]
                current_idx = indices[-1]
    logger.info("Total propagation: %d frames in %.1fs", len(result) - 1, time.monotonic() - t_total)
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
