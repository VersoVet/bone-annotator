"""CPU pre-annotation fallback (no GPU / no bone-ml model).

Generates whole-bone seed masks via Otsu + morphology and pushes them
to CVAT so an annotator (or MedSAM2) can refine zone labels.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image

logger = logging.getLogger(__name__)

# Prefer a stable anatomical zone for the silhouette seed.
_PREFERRED_SEED_LABELS = (
    "diaphyse_humerale",
    "corps_diaphysaire",
    "epiphyse_proximale",
    "tete_humerale",
)

def otsu_threshold(gray: np.ndarray) -> int:
    """Compute Otsu threshold for a uint8 grayscale image.

    Args:
        gray: 2D uint8 array.

    Returns:
        Threshold in [0, 255].
    """
    hist = np.bincount(gray.ravel(), minlength=256).astype(np.float64)
    total = float(gray.size)
    if total <= 0:
        return 128
    sum_total = float(np.dot(np.arange(256), hist))
    sum_b = 0.0
    weight_b = 0.0
    max_var = -1.0
    threshold = 128
    for t in range(256):
        weight_b += hist[t]
        if weight_b == 0:
            continue
        weight_f = total - weight_b
        if weight_f == 0:
            break
        sum_b += t * hist[t]
        mean_b = sum_b / weight_b
        mean_f = (sum_total - sum_b) / weight_f
        var_between = weight_b * weight_f * (mean_b - mean_f) ** 2
        if var_between > max_var:
            max_var = var_between
            threshold = t
    return int(threshold)

def bone_mask_from_frame(image_path: Path) -> np.ndarray:
    """Build a binary bone mask from a prepared PNG frame.

    Uses Otsu thresholding. Prefers the brighter foreground (fluoro bone)
    and falls back to the darker component if needed. Applies a light
    morphological close via max/min filters (no OpenCV required).

    Args:
        image_path: Path to PNG frame.

    Returns:
        Binary uint8 mask (H, W) with 1 = bone.
    """
    with Image.open(image_path) as img:
        gray = np.array(img.convert("L"), dtype=np.uint8)

    thr = otsu_threshold(gray)
    bright = gray > thr
    dark = gray <= thr
    # Prefer the component that is neither empty nor almost full.
    candidates: list[tuple[float, np.ndarray]] = []
    for component in (bright, dark):
        ratio = float(component.mean())
        if 0.02 < ratio < 0.95:
            candidates.append((abs(ratio - 0.35), component.astype(np.uint8)))
    result: np.ndarray
    if not candidates:
        result = bright.astype(np.uint8) if bright.mean() <= dark.mean() else dark.astype(np.uint8)
    else:
        candidates.sort(key=lambda item: item[0])
        result = candidates[0][1]

    # Morphological close (dilate then erode) with a 5x5 window.
    result = _dilate(result, 5)
    result = _erode(result, 5)
    return result

def _dilate(mask: np.ndarray, k: int) -> np.ndarray:
    """Binary dilation with a square kernel."""
    from numpy.lib.stride_tricks import sliding_window_view

    pad = k // 2
    padded = np.pad(mask, pad, mode="constant")
    windows = sliding_window_view(padded, (k, k))
    return windows.max(axis=(-2, -1)).astype(np.uint8)

def _erode(mask: np.ndarray, k: int) -> np.ndarray:
    """Binary erosion with a square kernel."""
    from numpy.lib.stride_tricks import sliding_window_view

    pad = k // 2
    padded = np.pad(mask, pad, mode="constant", constant_values=1)
    windows = sliding_window_view(padded, (k, k))
    return windows.min(axis=(-2, -1)).astype(np.uint8)

def binary_mask_to_rle(mask: np.ndarray) -> list[float]:
    """Convert binary mask to CVAT RLE (run lengths + bounds).

    Args:
        mask: Binary uint8 mask.

    Returns:
        CVAT points list, empty if mask is empty.
    """
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    if not rows.any() or not cols.any():
        return []
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]
    crop = mask[rmin : rmax + 1, cmin : cmax + 1].flatten()
    rle: list[float] = []
    current_val, count = 0, 0
    for val in crop:
        if int(val) == current_val:
            count += 1
        else:
            rle.append(float(count))
            current_val = int(val)
            count = 1
    rle.append(float(count))
    rle.extend([float(cmin), float(rmin), float(cmax + 1), float(rmax + 1)])
    return rle

def mask_to_bbox_points(mask: np.ndarray) -> list[float] | None:
    """Convert binary mask to CVAT rectangle points [x1,y1,x2,y2].

    Args:
        mask: Binary uint8 mask.

    Returns:
        Rectangle points or None if empty.
    """
    ys, xs = np.where(mask > 0)
    if len(xs) == 0:
        return None
    return [float(xs.min()), float(ys.min()), float(xs.max()), float(ys.max())]

def _strip_shape_ids(shape: dict[str, Any]) -> dict[str, Any]:
    """Return a CVAT shape dict safe for PUT (no server ids)."""
    cleaned = {k: v for k, v in shape.items() if k not in {"id", "elements"}}
    return cleaned


def pick_seed_label_id(labels: list[dict[str, Any]]) -> tuple[int, str]:
    """Pick the CVAT label id used for the silhouette seed.

    Args:
        labels: CVAT task labels.

    Returns:
        (label_id, label_name).

    Raises:
        ValueError: If no labels are available.
    """
    by_name = {str(lbl.get("name", "")): int(lbl["id"]) for lbl in labels if "id" in lbl}
    for preferred in _PREFERRED_SEED_LABELS:
        if preferred in by_name:
            return by_name[preferred], preferred
    if not labels:
        raise ValueError("No CVAT labels on task — sync accepted-labels first")
    first = labels[0]
    return int(first["id"]), str(first.get("name", "zone"))

def enhanced_bone_mask_from_frame(image_path: Path) -> np.ndarray:
    """Build bone mask using imaging-sdk auto_bone_mask, fallback to Otsu.

    imaging-sdk keeps only the largest connected component and removes
    collimator artefacts — significantly better than raw Otsu.

    Args:
        image_path: Path to PNG frame.

    Returns:
        Binary uint8 mask (H, W) with 1=bone.
    """
    try:
        from imaging_sdk.filters.core.geometric.auto_bone_mask import (
            threshold_bone_mask,
        )

        with Image.open(image_path) as img:
            gray = np.array(img.convert("L"), dtype=np.uint8)
        result = threshold_bone_mask(gray, method="otsu", invert=True, kernel_size=15, min_area_ratio=0.05)
        if result is not None:
            return (result > 0).astype(np.uint8)
    except ImportError:
        logger.debug("imaging-sdk auto_bone_mask not available, using Otsu")
    except Exception as e:
        logger.warning("auto_bone_mask failed, using Otsu: %s", e)
    return bone_mask_from_frame(image_path)


def build_zone_seed_shapes(
    frame_files: list[Path],
    seed_frames: list[int],
    labels: list[dict[str, Any]],
    bone_type: str,
    portion: str = "entire",
) -> list[dict[str, Any]]:
    """Create multi-zone CVAT seed shapes from bone mask subdivision.

    For each seed frame, builds a bone mask, subdivides it into anatomical
    zones, and maps each zone to a CVAT label. Produces multiple shapes
    per frame (one per detected zone).

    Args:
        frame_files: Sorted PNG paths.
        seed_frames: Frame indices to seed.
        labels: CVAT task labels with 'id' and 'name'.
        bone_type: Bone type for zone splitting ratios.
        portion: Acquisition portion for filtering impossible zones.

    Returns:
        List of CVAT shape dicts with different label_ids per zone.
    """
    from .zone_subdivision import resolve_zone_label_id, subdivide_bone_mask

    shapes: list[dict[str, Any]] = []
    for frame_idx in seed_frames:
        if frame_idx < 0 or frame_idx >= len(frame_files):
            continue
        mask = enhanced_bone_mask_from_frame(frame_files[frame_idx])
        zones = subdivide_bone_mask(mask, bone_type, portion=portion)
        for region_name, zone_mask in zones:
            resolved = resolve_zone_label_id(region_name, bone_type, labels)
            if resolved is None:
                continue
            label_id, _ = resolved
            rle = binary_mask_to_rle(zone_mask)
            if rle:
                shapes.append(_shape_payload("mask", frame_idx, label_id, rle))
    return shapes


def resolve_seed_frames(n_frames: int, max_seeds: int) -> list[int]:
    """Spread seed indices across a frame series (includes first and last).

    Args:
        n_frames: Total number of frames.
        max_seeds: Maximum seeds to place.

    Returns:
        Sorted unique frame indices.
    """
    if n_frames <= 0:
        return []
    if n_frames <= max_seeds:
        return list(range(n_frames))
    return sorted({int(round(i * (n_frames - 1) / (max_seeds - 1))) for i in range(max_seeds)})


def _shape_payload(shape_type: str, frame_idx: int, label_id: int, points: list[float]) -> dict[str, Any]:
    """Build a CVAT shape dict without undeclared attributes or ids."""
    return {
        "type": shape_type,
        "frame": int(frame_idx),
        "label_id": label_id,
        "points": points,
        "occluded": False,
        "z_order": 0,
        "attributes": [],
    }


def build_seed_shapes(
    frame_files: list[Path],
    seed_frames: list[int],
    label_id: int,
    *,
    use_mask: bool = True,
) -> list[dict[str, Any]]:
    """Create CVAT seed shapes from Otsu masks on selected frames.

    Args:
        frame_files: Sorted PNG paths.
        seed_frames: Frame indices to seed.
        label_id: CVAT label id.
        use_mask: Prefer mask RLE over rectangles.

    Returns:
        List of CVAT shape dicts.
    """
    shapes: list[dict[str, Any]] = []
    for frame_idx in seed_frames:
        if frame_idx < 0 or frame_idx >= len(frame_files):
            continue
        mask = bone_mask_from_frame(frame_files[frame_idx])
        if use_mask:
            rle = binary_mask_to_rle(mask)
            if rle:
                shapes.append(_shape_payload("mask", frame_idx, label_id, rle))
            continue
        bbox = mask_to_bbox_points(mask)
        if bbox:
            shapes.append(_shape_payload("rectangle", frame_idx, label_id, bbox))
    return shapes


def rectangles_from_masks(
    frame_files: list[Path],
    mask_shapes: list[dict[str, Any]],
    label_id: int,
) -> list[dict[str, Any]]:
    """Convert mask seed shapes to rectangle fallbacks.

    Args:
        frame_files: Sorted PNG paths.
        mask_shapes: Previously built mask shapes.
        label_id: CVAT label id.

    Returns:
        Rectangle shape dicts.
    """
    rects: list[dict[str, Any]] = []
    for shape in mask_shapes:
        frame_idx = int(shape["frame"])
        if frame_idx >= len(frame_files):
            continue
        bbox = mask_to_bbox_points(bone_mask_from_frame(frame_files[frame_idx]))
        if bbox:
            rects.append(_shape_payload("rectangle", frame_idx, label_id, bbox))
    return rects


async def _merge_push_shapes(
    cvat_client: Any,
    cvat_task_id: int,
    new_shapes: list[dict[str, Any]],
) -> tuple[bool, list[dict[str, Any]]]:
    """Merge new shapes with existing CVAT annotations and PUT.

    Args:
        cvat_client: Authenticated CVAT client.
        cvat_task_id: CVAT task id.
        new_shapes: Shapes to append.

    Returns:
        (ok, existing_shapes_stripped).
    """
    existing = await cvat_client.get_annotations(int(cvat_task_id)) or {}
    existing_shapes = [_strip_shape_ids(s) for s in (existing.get("shapes") or [])]
    payload = {
        "version": existing.get("version", 0),
        "shapes": existing_shapes + new_shapes,
        "tracks": existing.get("tracks") or [],
        "tags": existing.get("tags") or [],
    }
    ok = await cvat_client.update_annotations(int(cvat_task_id), payload)
    return ok, existing_shapes


async def push_cpu_seeds(
    cvat_client: Any,
    task: dict[str, Any],
    *,
    seed_frames: list[int] | None = None,
    max_seeds: int = 5,
    use_mask: bool = True,
) -> dict[str, Any]:
    """Generate Otsu bone seeds and push them to CVAT.

    Args:
        cvat_client: Authenticated CVATClient.
        task: Annotation task row (needs cvat_task_id, dataset_path).
        seed_frames: Optional explicit frame indices.
        max_seeds: Max seed frames when seed_frames is None (spread across series).
        use_mask: Push CVAT mask shapes when True, else rectangles.

    Returns:
        Status dict with shapes_pushed and label used.

    Raises:
        ValueError: If task paths/labels are missing.
        RuntimeError: If CVAT rejects both mask and rectangle pushes.
    """
    cvat_task_id = task.get("cvat_task_id")
    dataset_path = task.get("dataset_path")
    if not cvat_task_id or not dataset_path:
        raise ValueError("Task missing cvat_task_id or dataset_path")

    images_dir = Path(dataset_path) / "images"
    frame_files = sorted(images_dir.glob("*.png"))
    if not frame_files:
        raise ValueError(f"No PNG frames in {images_dir}")

    labels = await cvat_client.get_task_labels(int(cvat_task_id))
    label_id, label_name = pick_seed_label_id(labels)
    if seed_frames is None:
        seed_frames = resolve_seed_frames(len(frame_files), max_seeds)

    shapes = build_seed_shapes(frame_files, seed_frames, label_id, use_mask=use_mask)
    if not shapes:
        return {
            "status": "cpu_empty",
            "shapes_pushed": 0,
            "label_id": label_id,
            "label_name": label_name,
            "seed_frames": seed_frames,
        }

    ok, existing_shapes = await _merge_push_shapes(cvat_client, int(cvat_task_id), shapes)
    if not ok and use_mask:
        logger.warning("Mask push failed for CVAT #%s — retrying with rectangles", cvat_task_id)
        shapes = rectangles_from_masks(frame_files, shapes, label_id)
        ok, _ = await _merge_push_shapes(cvat_client, int(cvat_task_id), shapes)
    if not ok:
        raise RuntimeError(f"Failed to push CPU seeds to CVAT task {cvat_task_id}")

    logger.info(
        "CPU pre-annotate: %d seeds on CVAT #%s label=%s",
        len(shapes),
        cvat_task_id,
        label_name,
    )
    return {
        "status": "cpu_ok",
        "shapes_pushed": len(shapes),
        "label_id": label_id,
        "label_name": label_name,
        "seed_frames": seed_frames,
        "mode": "mask" if use_mask else "rectangle",
    }
