"""Registry utility functions for acquisition metadata loading."""

import json
from pathlib import Path
from typing import Any


def load_acquisition_metadata(acq_dir: Path) -> dict[str, Any]:
    """Load metadata from acquisition directory.

    Args:
        acq_dir: Acquisition directory path.

    Returns:
        Metadata dictionary.
    """
    metadata: dict[str, Any] = {"session_id": ""}

    # Try to load metadata.json if present
    meta_path = acq_dir / "metadata.json"
    if meta_path.exists():
        try:
            with meta_path.open() as f:
                loaded = json.load(f)
                metadata.update(loaded)
        except json.JSONDecodeError:
            pass

    return metadata


def parse_category(category_name: str) -> tuple[str, str, str] | tuple[None, None, None]:
    """Parse category directory name to extract bone metadata.

    Args:
        category_name: Category directory name (e.g., "humerus_left_proximal").

    Returns:
        Tuple of (bone_type, side, region) or (None, None, None) if invalid.
    """
    parts = category_name.split("_")
    if len(parts) < 3:
        return None, None, None

    bone_type = parts[0]
    side = parts[1] if len(parts) > 1 else ""
    region = parts[2] if len(parts) > 2 else ""

    return bone_type, side, region
