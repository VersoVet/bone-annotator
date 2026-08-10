"""FastAPI routes for ML prediction endpoints.

Provides inference endpoints for YOLO bone detection and segmentation.
"""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException

from .service import get_model_info, predict_task

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/predict", tags=["predict"])


@router.get("/model-info")
async def model_info() -> dict[str, Any]:
    """Get current model information.

    Returns:
        Model version, type, and load status.
    """
    try:
        info = await get_model_info()
        return info
    except Exception as e:
        logger.error("Error fetching model info: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch model info")


@router.post("/task")
async def predict_on_task(
    task: dict[str, Any],
    model_version: str | None = None,
) -> dict[str, Any]:
    """Run prediction on a task.

    Loads image from BoneStore, applies YOLO inference,
    and returns detections.

    Args:
        task: Task dict with image reference.
        model_version: Optional model version to use.

    Returns:
        Prediction results with bounding boxes and confidence scores.

    Raises:
        HTTPException: If prediction fails.
    """
    try:
        result = await predict_task(task, model_version)

        if "error" in result:
            logger.warning("Prediction error: %s", result.get("error"))
            # Return partial result even with error
            return result

        return result
    except Exception as e:
        logger.error("Error running prediction: %s", e)
        raise HTTPException(status_code=500, detail="Prediction failed")


@router.post("/batch")
async def predict_batch(
    tasks: list[dict[str, Any]],
    model_version: str | None = None,
) -> dict[str, Any]:
    """Run batch predictions on multiple tasks.

    Args:
        tasks: List of task dicts.
        model_version: Optional model version.

    Returns:
        Dict with predictions dict keyed by task ID.

    Raises:
        HTTPException: If batch prediction fails.
    """
    try:
        predictions: dict[str, Any] = {}

        for task in tasks:
            task_id = task.get("id", "unknown")
            try:
                result = await predict_task(task, model_version)
                predictions[task_id] = result
            except Exception as e:
                logger.error("Batch prediction failed for task %s: %s", task_id, e)
                predictions[task_id] = {"error": str(e)[:100], "result": []}

        return {
            "status": "completed",
            "total_tasks": len(tasks),
            "predictions": predictions,
        }
    except Exception as e:
        logger.error("Batch prediction error: %s", e)
        raise HTTPException(status_code=500, detail="Batch prediction failed")
