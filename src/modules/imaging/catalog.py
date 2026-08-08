"""Catalog of imaging filters and bone anatomical taxonomy.

Provides access to available imaging filters and parsing of BoneStore categories.
"""

import logging

logger = logging.getLogger(__name__)


def get_filter_catalog() -> dict:
    """Get available imaging filters catalog.

    Returns:
        Dict mapping filter names to their properties.
    """
    # Placeholder: imaging_sdk import handled dynamically
    # when available
    try:
        from imaging_sdk import list_available_filters

        catalog = {}
        for name, filt in sorted(list_available_filters().items()):
            params = [
                {
                    "name": p.name,
                    "default": p.default,
                    "type": p.type_.__name__,
                    "min": p.min_value,
                    "max": p.max_value,
                    "label": p.ui_label or p.name,
                    "step": p.ui_step,
                    "choices": p.choices,
                    "description": p.description or "",
                }
                for p in filt.params_schema
            ]
            catalog[name] = {
                "category": getattr(filt, "category", ""),
                "description": getattr(filt, "description", ""),
                "gpu": getattr(filt, "gpu_capable", False),
                "params": params,
            }
        return catalog
    except ImportError:
        logger.warning("imaging_sdk not available, returning empty catalog")
        return {}


def parse_category(dirname: str) -> tuple[str | None, str, str]:
    """Parse BoneStore category directory name.

    Args:
        dirname: Directory name (e.g., "001^humerus_left_proximal").

    Returns:
        Tuple of (bone_type, side, region). bone_type is None if not recognized.
    """
    known_bones = {"humerus", "radius", "ulna", "femur", "scapula", "fibula"}
    known_sides = {"left", "right", "bilateral"}
    known_regions = {"proximal", "distal", "entire"}

    name = dirname.split("^", 1)[-1] if "^" in dirname else dirname
    parts = name.lower().split("_")

    bone = next((p for p in parts if p in known_bones), None)
    side = next((p for p in parts if p in known_sides), "unknown")
    region = next((p for p in parts if p in known_regions), "entire")
    return bone, side, region
