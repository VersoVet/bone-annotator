"""Ingestion utility functions for frame selection and preprocessing."""

import hashlib
from pathlib import Path
from typing import Any

import numpy as np


def select_frames(
    frame_files: list[Path],
    timecodes: list[dict[str, Any]] | None,
    angle_step_deg: float,
) -> list[tuple[Path, float | None]]:
    """Select frames by angular spacing.

    Args:
        frame_files: List of .b2nd frame paths.
        timecodes: Timecode list or None.
        angle_step_deg: Angular step.

    Returns:
        List of (path, angle_deg) tuples.
    """
    if not timecodes:
        # Fallback: stride-based selection
        stride = max(1, len(frame_files) // (360 // int(angle_step_deg)))
        return [(fp, None) for fp in frame_files[::stride]]

    # Angle-based selection
    tc_by_idx: dict[int, float] = {}
    for tc in timecodes:
        idx = tc.get("index", -1)
        angle = tc.get("angle_deg", 0.0)
        tc_by_idx[idx] = angle

    selected = []
    current_angle = 0.0
    for fp in frame_files:
        idx = extract_frame_index(fp.stem)
        angle = tc_by_idx.get(idx, (len(selected) / max(len(frame_files) - 1, 1)) * 360)
        if angle - current_angle >= angle_step_deg or len(selected) == 0:
            selected.append((fp, angle))
            current_angle = angle

    return selected


def read_b2nd_frame(frame_path: Path) -> np.ndarray:
    """Read .b2nd frame file.

    Args:
        frame_path: Path to .b2nd file.

    Returns:
        Image as uint16 numpy array.
    """
    try:
        import blosc2

        arr = blosc2.open(str(frame_path))[:]
        return np.asarray(arr, dtype=np.uint16)
    except Exception:
        import logging

        logger = logging.getLogger(__name__)
        logger.error("Failed to read %s", frame_path)
        raise


def preprocess_image(image: np.ndarray, target_size: int) -> np.ndarray:
    """Simple preprocessing: resize to target size.

    Args:
        image: Input uint16 image.
        target_size: Target size.

    Returns:
        Resized float32 image.
    """
    from PIL import Image

    pil_img = Image.fromarray(image)
    pil_img = pil_img.resize((target_size, target_size), Image.LANCZOS)
    return np.asarray(pil_img, dtype=np.float32)


def image_hash(image: np.ndarray) -> str:
    """Compute image hash for deduplication.

    Args:
        image: numpy array.

    Returns:
        Hex hash string.
    """
    return hashlib.md5(image.tobytes(), usedforsecurity=False).hexdigest()


def extract_frame_index(stem: str) -> int:
    """Extract frame index from filename stem.

    Args:
        stem: Filename stem.

    Returns:
        Frame index.
    """
    parts = stem.split("_")
    if len(parts) > 1 and parts[-1].isdigit():
        return int(parts[-1])
    return 0
