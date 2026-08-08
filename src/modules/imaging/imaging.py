"""Imaging utilities for frame loading and pipeline execution.

Contains frame loading from Blosc2, PNG conversion, and pipeline execution.
"""

import io
import logging
import math
from pathlib import Path

import blosc2
import numpy as np
from PIL import Image

from .frame_cache import LRUCache

logger = logging.getLogger(__name__)

FRAME_CACHE_SIZE = 100
RAW_CACHE_SIZE = 50

# Global caches
_raw_cache = LRUCache(RAW_CACHE_SIZE)
_processed_cache = LRUCache(FRAME_CACHE_SIZE)


def _read_b2nd_frame(path: Path) -> np.ndarray:
    """Read a Blosc2 frame and return as numpy uint16 array.

    Args:
        path: Path to .b2nd file.

    Returns:
        2D numpy uint16 array.

    Raises:
        ValueError: If pixel count cannot reshape to 2D.
    """
    schunk = blosc2.open(str(path))
    raw_bytes = schunk[:]
    data = np.frombuffer(raw_bytes, dtype=np.uint16)
    n_pixels = len(data)
    side = math.isqrt(n_pixels)
    if side * side == n_pixels:
        return data.reshape(side, side)
    for h in [1380, 1350, 1024, 2048, 1536, 768]:
        w = n_pixels // h
        if h * w == n_pixels:
            return data.reshape(h, w)
    msg = f"Cannot reshape {n_pixels} pixels into 2D image"
    raise ValueError(msg)


def _extract_frame_index(stem: str) -> int:
    """Extract numeric frame index from filename.

    Args:
        stem: Filename without extension (e.g., "frame_042").

    Returns:
        Integer index or 0 if not found.
    """
    parts = stem.split("_")
    for part in reversed(parts):
        if part.isdigit():
            return int(part)
    return 0


def _raw_to_png(image: np.ndarray, size: int = 768) -> bytes:
    """Convert uint16 image to PNG bytes.

    Args:
        image: uint16 or float numpy array.
        size: Output size in pixels.

    Returns:
        PNG bytes.
    """
    if image.dtype == np.uint16:
        mask = image > 0
        if mask.any():
            p1 = np.percentile(image[mask], 1)
            p99 = np.percentile(image[mask], 99)
            normalized = np.clip((image.astype(np.float32) - p1) / max(p99 - p1, 1), 0, 1)
        else:
            normalized = np.zeros_like(image, dtype=np.float32)
        img_u8 = (normalized * 255).astype(np.uint8)
    elif image.dtype in (np.float32, np.float64):
        img_u8 = (np.clip(image, 0, 1) * 255).astype(np.uint8)
    else:
        img_u8 = image.astype(np.uint8)

    pil_img = Image.fromarray(img_u8, mode="L")
    pil_img = pil_img.resize((size, size), Image.LANCZOS)
    buf = io.BytesIO()
    pil_img.save(buf, format="PNG")
    return buf.getvalue()


def load_frame(path: str) -> np.ndarray:
    """Load a frame from .b2nd file with caching.

    Args:
        path: Path to frame file.

    Returns:
        numpy uint16 array.
    """
    cached = _raw_cache.get(path)
    if cached is not None:
        return cached
    frame = _read_b2nd_frame(Path(path))
    _raw_cache.put(path, frame)
    return frame


def frame_to_png(image: np.ndarray, size: int = 768) -> bytes:
    """Convert frame to PNG representation.

    Args:
        image: Image array (uint16 or float).
        size: Output size in pixels.

    Returns:
        PNG bytes.
    """
    return _raw_to_png(image, size)


def clear_frame_cache() -> None:
    """Clear all frame caches."""
    _raw_cache.clear()
    _processed_cache.clear()
    logger.info("Frame caches cleared")


def get_cache_stats() -> dict[str, int]:
    """Get cache statistics.

    Returns:
        Dict with cache sizes.
    """
    return {
        "raw_cache_size": _raw_cache.size,
        "processed_cache_size": _processed_cache.size,
    }
