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

FRAME_CACHE_SIZE = 500
RAW_CACHE_SIZE = 200

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
    pil_img = pil_img.resize((size, size), Image.Resampling.LANCZOS)
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
        return cached  # type: ignore[return-value]
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


def load_frame_as_png(path: str, size: int = 768) -> bytes:
    """Load a frame and return cached PNG bytes.

    Combines raw loading and PNG conversion with two-level caching:
    raw array cache and processed PNG cache.

    Args:
        path: Path to .b2nd frame file.
        size: Output size in pixels.

    Returns:
        PNG bytes.
    """
    cache_key = f"{path}:{size}"
    cached_png = _processed_cache.get(cache_key)
    if cached_png is not None:
        return cached_png  # type: ignore[return-value]
    raw = load_frame(path)
    png = _raw_to_png(raw, size)
    _processed_cache.put(cache_key, png)
    return png


def preload_frames(paths: list[str], size: int = 768) -> int:
    """Preload multiple frames into both raw and PNG caches.

    Args:
        paths: List of .b2nd file paths.
        size: Output size in pixels.

    Returns:
        Number of frames successfully loaded.
    """
    loaded = 0
    for path in paths:
        try:
            load_frame_as_png(path, size)
            loaded += 1
        except Exception as e:
            logger.warning("Preload failed for %s: %s", path, e)
    logger.info("Preloaded %d/%d frames (size=%d)", loaded, len(paths), size)
    return loaded


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
