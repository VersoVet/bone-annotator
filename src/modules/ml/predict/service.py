"""ML predict service — YOLO inference on bone images.

Provides model loading, inference, and Label Studio result formatting.
"""

import asyncio
import logging
import os
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import httpx

logger = logging.getLogger(__name__)

# Allowed hosts for external URLs (SSRF prevention)
ALLOWED_URL_HOSTS = {"10.0.0.59", "localhost", "127.0.0.1"}

# Lazy-loaded model with thread-safe access
_model: Any = None
_model_version = "none"
_model_lock = asyncio.Lock()


async def get_model_info() -> dict[str, Any]:
    """Get current model information.

    Returns:
        Dict with model version, type, and status.
    """
    return {
        "model_version": _model_version,
        "model_loaded": _model is not None,
        "model_type": "yolov8",
    }


async def _load_model(model_version: str | None = None) -> Any:
    """Load YOLO model (lazy, cached) with thread-safe locking.

    Prevents race conditions when multiple concurrent requests
    request different model versions.

    Args:
        model_version: Specific version to load, or None for default.

    Returns:
        Loaded YOLO model.
    """
    global _model, _model_version
    from ultralytics import YOLO

    models_dir = Path(os.getenv("ML_MODELS_DIR", "/opt/onyx/skills/bone-ml/models"))
    if model_version:
        model_path = models_dir / f"{model_version}.pt"
    else:
        # Find latest model
        pts = sorted(models_dir.glob("*.pt"), key=lambda p: p.stat().st_mtime)
        model_path = pts[-1] if pts else models_dir / "yolov8n.pt"

    async with _model_lock:
        # Double-check pattern to avoid redundant loads
        if _model is None or _model_version != str(model_path):
            logger.info("Loading model: %s", model_path)

            def _load_yolo() -> Any:
                return YOLO(str(model_path))

            _model = await asyncio.to_thread(_load_yolo)
            _model_version = str(model_path)

    return _model


async def predict_task(task: dict[str, Any], model_version: str | None = None) -> dict[str, Any]:
    """Run prediction on a Label Studio task.

    Loads image from BoneStore, applies preprocessing,
    runs YOLO inference, and formats results as Label Studio annotations.

    Args:
        task: Label Studio task dict with image data reference.
        model_version: Optional model version to use.

    Returns:
        Dict with prediction results in Label Studio format.
    """
    try:
        from onyx_sdk import get_client

        onyx = get_client()
        if onyx:
            onyx.status("WORKING", detail="Inference in progress")
    except Exception:  # noqa: BLE001
        pass

    task_id = task.get("id", 0)
    data = task.get("data", {})
    image_ref = data.get("image", data.get("path", ""))

    if not image_ref:
        return {"result": [], "score": 0.0}

    try:
        model = await _load_model(model_version)
        image = _load_image(image_ref)

        def _run_predict() -> list[Any]:
            return model.predict(image, conf=0.25, verbose=False)

        results = await asyncio.to_thread(_run_predict)

        annotations = _format_annotations(results[0]) if results else []
        score = _avg_confidence(results[0]) if results else 0.0

        logger.info(
            "Task %s: %d predictions (score=%.2f)",
            task_id,
            len(annotations),
            score,
        )
        return {"result": annotations, "score": score}

    except Exception as e:
        logger.error("Prediction failed for task %s: %s", task_id, e)
        return {"result": [], "score": 0.0, "error": str(e)[:100]}


def _load_image(image_ref: str) -> Any:
    """Load image from BoneStore or URL with validation.

    Validates paths to prevent traversal attacks and restricts
    external URLs to whitelist (SSRF prevention).

    Args:
        image_ref: Image path (relative/absolute) or whitelisted URL.

    Returns:
        Image as numpy array.

    Raises:
        ValueError: If path escapes BoneStore or URL not whitelisted.
    """
    import io

    import numpy as np
    from PIL import Image

    bonestore = Path(os.getenv("BONESTORE_ROOT", "/mnt/bonestore")).resolve()

    # Handle URLs
    if image_ref.startswith("http://") or image_ref.startswith("https://"):
        parsed = urlparse(image_ref)
        host = parsed.hostname or ""
        if host not in ALLOWED_URL_HOSTS:
            msg = f"URL host not whitelisted: {host}. Allowed: {ALLOWED_URL_HOSTS}"
            raise ValueError(msg)

        resp = httpx.get(image_ref, timeout=30.0, follow_redirects=False)
        resp.raise_for_status()
        return np.array(Image.open(io.BytesIO(resp.content)))

    # Handle filesystem paths
    if image_ref.startswith("/"):
        # Absolute path — validate it's under /mnt/bonestore
        path = Path(image_ref).resolve()
    else:
        # Relative path — resolve relative to bonestore
        path = (bonestore / image_ref).resolve()

    # Security: ensure resolved path is under bonestore
    try:
        path.relative_to(bonestore)
    except ValueError:
        msg = f"Path traversal detected: {image_ref} resolves to {path} outside {bonestore}"
        raise ValueError(msg)

    # Load from BoneStore (.b2nd via imaging-sdk or standard image)
    if path.suffix == ".b2nd":
        try:
            import blosc2

            arr = blosc2.open(str(path))[:]
            return np.asarray(arr, dtype=np.uint16)
        except Exception as e:
            logger.error("Failed to load .b2nd: %s", e)
            raise
    else:
        return np.array(Image.open(path))


def _format_annotations(result: Any) -> list[dict[str, Any]]:
    """Convert YOLO results to Label Studio annotation format.

    Args:
        result: Single YOLO result object.

    Returns:
        List of Label Studio annotation dicts.
    """
    annotations: list[dict[str, Any]] = []
    boxes = result.boxes if result.boxes is not None else []
    img_h, img_w = result.orig_shape

    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = result.names.get(cls_id, f"class_{cls_id}")

        annotations.append(
            {
                "type": "rectanglelabels",
                "value": {
                    "x": (x1 / img_w) * 100,
                    "y": (y1 / img_h) * 100,
                    "width": ((x2 - x1) / img_w) * 100,
                    "height": ((y2 - y1) / img_h) * 100,
                    "rectanglelabels": [label],
                },
                "score": conf,
                "from_name": "label",
                "to_name": "image",
            }
        )

    # Keypoints if available
    if hasattr(result, "keypoints") and result.keypoints is not None:
        for kp_set in result.keypoints:
            for i, (x, y, conf) in enumerate(kp_set.data[0].tolist()):
                if conf > 0.3:
                    annotations.append(
                        {
                            "type": "keypointlabels",
                            "value": {
                                "x": (x / img_w) * 100,
                                "y": (y / img_h) * 100,
                                "keypointlabels": [f"kp_{i}"],
                            },
                            "score": conf,
                            "from_name": "keypoint",
                            "to_name": "image",
                        }
                    )

    return annotations


def _avg_confidence(result: Any) -> float:
    """Average confidence of all detections.

    Args:
        result: YOLO result object.

    Returns:
        Mean confidence score.
    """
    if result.boxes is None or len(result.boxes) == 0:
        return 0.0
    return float(result.boxes.conf.mean())
