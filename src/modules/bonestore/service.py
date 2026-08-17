"""BoneStore traversal helpers for acquisition management.

Provides functions for listing acquisitions, finding directories,
and loading rotation timecodes.
"""

import json
import logging
import os
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

BONESTORE_ROOT = os.getenv("BONESTORE_ROOT", "/mnt/bonestore")


def list_acquisitions(
    bonestore_root: str | Path | None = None,
) -> list[dict[str, Any]]:
    """List all acquisitions in BoneStore.

    Args:
        bonestore_root: BoneStore mount point. If None, uses env var.

    Returns:
        List of dicts with id, bone_type, side, region, frame_count.
    """
    acquisitions = []
    if bonestore_root is None:
        bonestore_root = Path(BONESTORE_ROOT)
    else:
        bonestore_root = Path(bonestore_root)

    if not bonestore_root.exists():
        logger.warning("BoneStore not mounted: %s", bonestore_root)
        return acquisitions

    for category_dir in sorted(bonestore_root.iterdir()):
        if not category_dir.is_dir():
            continue

        # Parse category: "ANONYMOUS^Humerus_Left_Proximal" or "humerus_left_proximal"
        cat_name = category_dir.name
        if "^" in cat_name:
            cat_name = cat_name.split("^", 1)[1]  # Strip prefix before ^
        parts = cat_name.lower().split("_")
        if len(parts) < 2:
            continue

        bone_type = parts[0]
        side = parts[1] if len(parts) > 1 else "unknown"
        region = parts[2] if len(parts) > 2 else "entire"

        for acq_dir in sorted(category_dir.iterdir()):
            if not acq_dir.is_dir():
                continue

            raw_dir = acq_dir / "raw"
            frame_count = len(list(raw_dir.glob("*.b2nd"))) if raw_dir.exists() else 0
            has_timecodes = (acq_dir / "frame_timecodes.json").exists()

            acquisitions.append(
                {
                    "id": acq_dir.name,
                    "category": category_dir.name,
                    "bone_type": bone_type,
                    "side": side,
                    "region": region,
                    "frame_count": frame_count,
                    "has_timecodes": has_timecodes,
                    "path": str(acq_dir),
                }
            )

    return acquisitions


def find_acquisition(
    bonestore_root: str | Path | None,
    acquisition_id: str,
) -> Path | None:
    """Find acquisition directory by ID.

    Args:
        bonestore_root: BoneStore mount point.
        acquisition_id: Acquisition ID to search for.

    Returns:
        Path to acquisition directory or None if not found.
    """
    if bonestore_root is None:
        bonestore_root = Path(BONESTORE_ROOT)
    else:
        bonestore_root = Path(bonestore_root)

    for category_dir in bonestore_root.iterdir():
        if not category_dir.is_dir():
            continue
        acq_dir = category_dir / acquisition_id
        if acq_dir.exists():
            return acq_dir
    return None


def load_timecodes(acq_dir: Path) -> list[dict[str, Any]] | None:
    """Load rotation timecodes for acquisition.

    Args:
        acq_dir: Acquisition directory.

    Returns:
        List of {index, angle_deg} or None if absent/invalid.
    """
    tc_path = acq_dir / "frame_timecodes.json"
    if not tc_path.exists():
        return None
    try:
        with Path(tc_path).open() as f:
            data = json.load(f)
        frames = data.get("frames", [])
        if frames and "angle_deg" in frames[0]:
            return frames
    except (json.JSONDecodeError, KeyError):
        pass
    return None


def get_acquisition_frames(acq_dir: Path) -> list[dict[str, Any]]:
    """Get list of frames with angles for acquisition.

    Args:
        acq_dir: Acquisition directory.

    Returns:
        List of {index, filename, angle_deg, position}.
    """
    raw_dir = acq_dir / "raw"
    frame_files = sorted(raw_dir.glob("*.b2nd")) if raw_dir.exists() else []

    timecodes = load_timecodes(acq_dir)
    tc_by_index: dict[int, float] = {}
    if timecodes:
        for tc in timecodes:
            tc_by_index[tc.get("index", -1)] = tc.get("angle_deg", 0.0)

    frames = []
    for i, fp in enumerate(frame_files):
        # Extract frame index from filename (e.g., "frame_0123.b2nd" → 123)
        idx = _extract_frame_index(fp.stem)
        angle: float = tc_by_index.get(idx, (i / max(len(frame_files) - 1, 1)) * 360.0)
        frames.append(
            {
                "index": idx,
                "filename": fp.name,
                "angle_deg": round(angle, 2),
                "position": i,
            }
        )

    return frames


def _extract_frame_index(stem: str) -> int:
    """Extract frame index from filename stem.

    Args:
        stem: Filename stem (e.g., "frame_0123").

    Returns:
        Frame index as integer.
    """
    parts = stem.split("_")
    if len(parts) > 1 and parts[-1].isdigit():
        return int(parts[-1])
    return 0
