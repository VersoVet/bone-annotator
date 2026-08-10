"""Core module for bone-annotator.

Contains version management and shared utilities.
"""

import json
import logging
from pathlib import Path

logger = logging.getLogger("bone-annotator")


def _load_version() -> str:
    """Load version from manifest.json.

    Returns:
        Version string.
    """
    try:
        manifest_path = Path(__file__).resolve().parent.parent.parent / "manifest.json"
        with manifest_path.open() as f:
            manifest = json.load(f)
            return manifest.get("version", "0.1.0")
    except Exception:
        return "0.1.0"


__version__ = _load_version()
