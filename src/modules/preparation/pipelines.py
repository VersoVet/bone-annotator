"""Imaging treatment pipeline discovery via imaging-sdk."""

import logging
from pathlib import Path
from typing import Any

from src.config import get_imaging_config

logger = logging.getLogger(__name__)


def get_pipeline_manager() -> Any | None:
    """Create imaging-sdk JSONPipelineManager for user pipeline directory."""
    try:
        from imaging_sdk import JSONPipelineManager

        user_dir = Path(get_imaging_config()["user_dir"])
        user_dir.mkdir(parents=True, exist_ok=True)
        return JSONPipelineManager(pipeline_dir=user_dir)
    except ImportError:
        logger.warning("imaging_sdk not available")
        return None


def _pipeline_source(name: str, user_dir: Path, bundled_dir: Path) -> str:
    """Classify pipeline origin for UI grouping."""
    if (user_dir / f"{name}_user.json").exists() or (user_dir / f"{name}.json").exists():
        if name.endswith("_user") and (user_dir / f"{name}.json").exists():
            return "user"
        if (user_dir / f"{name}_user.json").exists():
            return "user"
    if (bundled_dir / "clinical" / f"{name}.json").exists():
        return "clinical"
    if (bundled_dir / "defaults" / f"{name}.json").exists() or (bundled_dir / f"{name}.json").exists():
        return "bundled"
    return "custom"


def list_imaging_treatments() -> list[dict[str, Any]]:
    """List all imaging treatments from imaging-sdk (bundled + users).

    Returns:
        Pipeline descriptors with name, display_name, source, filters count.
    """
    cfg = get_imaging_config()
    user_dir = Path(cfg["user_dir"])
    bundled_dir = Path(cfg["bundled_dir"])
    manager = get_pipeline_manager()
    if not manager:
        return [
            {
                "name": cfg["default_treatment"],
                "display_name": cfg["default_treatment_label"],
                "description": "Fallback (imaging-sdk unavailable)",
                "source": "bundled",
                "filters": 0,
                "is_default": True,
            }
        ]

    # Collect all pipeline names, then deduplicate: if X_user exists, skip X
    user_overrides = {f.stem.removesuffix("_user") for f in user_dir.glob("*_user.json")}

    seen: set[str] = set()
    pipelines: list[dict[str, Any]] = []

    for item in manager.list_pipelines_with_description():
        name = item["name"]
        if name in seen:
            continue
        # Skip base pipeline when a _user override exists
        if not name.endswith("_user") and name in user_overrides:
            continue
        seen.add(name)
        info = manager.load_pipeline(name)
        source = _pipeline_source(name, user_dir, bundled_dir)
        display = info.get("name", name) if info else item.get("description", name)
        if source == "user" and "[USER]" not in display:
            display = f"{display} [USER]"
        pipelines.append(
            {
                "name": name,
                "display_name": display,
                "description": item.get("description", ""),
                "description_long": item.get("description_long", ""),
                "source": source,
                "filters": len(info.get("filters", [])) if info else 0,
                "context": info.get("context", name) if info else name,
                "is_default": name == cfg["default_treatment"],
            }
        )

    # User-only files not yet discovered by the manager
    for json_file in sorted(user_dir.glob("*_user.json")):
        name = json_file.stem
        if name in seen:
            continue
        info = manager.load_pipeline(name)
        if not info:
            continue
        seen.add(name)
        display = info.get("name", name)
        if "[USER]" not in display:
            display = f"{display} [USER]"
        pipelines.append(
            {
                "name": name,
                "display_name": display,
                "description": info.get("description", ""),
                "description_long": info.get("description_long", ""),
                "source": "user",
                "filters": len(info.get("filters", [])),
                "context": info.get("context", name),
                "is_default": name == cfg["default_treatment"],
            }
        )

    pipelines.sort(key=lambda p: (p["source"] != "user", p["display_name"]))
    return pipelines
