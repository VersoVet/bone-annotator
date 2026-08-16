"""Utility functions for YOLO dataset export.

Provides zone-to-YOLO conversion, frame file lookup, and dimension reading.
"""

import logging
import os
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

BONESTORE_ROOT = Path(os.getenv("BONESTORE_ROOT", "/mnt/bonestore"))


def zone_to_yolo_line(
    zone: dict[str, Any],
    labels_mapping: dict[str, int],
    img_w: int,
    img_h: int,
) -> str | None:
    """Convert a zone annotation to a YOLO label line.

    YOLO format: class_id x_center y_center width height (all normalized 0-1).

    Args:
        zone: Zone dict with label and bbox/x/y/width/height.
        labels_mapping: Mapping of zone label to class ID.
        img_w: Image width in pixels.
        img_h: Image height in pixels.

    Returns:
        YOLO format string or None if label not in mapping.
    """
    label = zone.get("label", zone.get("name", ""))
    class_id = labels_mapping.get(label)
    if class_id is None:
        return None

    # Support both bbox dict and flat keys
    bbox = zone.get("bbox", zone)
    x = float(bbox.get("x", 0))
    y = float(bbox.get("y", 0))
    w = float(bbox.get("width", 0))
    h = float(bbox.get("height", 0))

    if w <= 0 or h <= 0:
        return None

    # Convert to YOLO normalized center format
    x_center = (x + w / 2) / img_w
    y_center = (y + h / 2) / img_h
    norm_w = w / img_w
    norm_h = h / img_h

    return f"{class_id} {x_center:.6f} {y_center:.6f} {norm_w:.6f} {norm_h:.6f}"


def find_frame_image(acq_id: str, frame_filename: str) -> Path | None:
    """Locate the frame image file in BoneStore.

    Args:
        acq_id: Acquisition ID.
        frame_filename: Frame filename (e.g. frame_042.b2nd).

    Returns:
        Path to frame file or None if not found.
    """
    direct = BONESTORE_ROOT / acq_id / frame_filename
    if direct.exists():
        return direct

    # Glob search as fallback
    matches = list(BONESTORE_ROOT.glob(f"**/{acq_id}/{frame_filename}"))
    return matches[0] if matches else None


def get_frame_dimensions(frame_path: Path) -> tuple[int, int]:
    """Get image dimensions from a frame file.

    Args:
        frame_path: Path to image or .b2nd file.

    Returns:
        Tuple of (width, height).
    """
    if frame_path.suffix == ".b2nd":
        from src.modules.imaging.imaging import _read_b2nd_frame

        arr = _read_b2nd_frame(frame_path)
        return arr.shape[1], arr.shape[0]  # (w, h)
    else:
        from PIL import Image

        with Image.open(frame_path) as img:
            return img.size  # (w, h)
