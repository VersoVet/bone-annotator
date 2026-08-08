"""ML training service — YOLOv8 training orchestration.

Manages model training runs with background task execution.
"""

import asyncio
import logging
import os
import shutil
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

MODELS_DIR = Path(os.getenv("ML_MODELS_DIR", "/opt/onyx/skills/bone-ml/models"))
RUNS_DIR = Path(os.getenv("ML_RUNS_DIR", "/opt/onyx/skills/bone-ml/runs"))

_active_run: dict[str, Any] | None = None


async def start_training(req: Any) -> dict[str, Any]:
    """Start YOLOv8 training run in background.

    Args:
        req: TrainRequest with dataset, model, epochs, etc.

    Returns:
        Dict with run ID and status.
    """
    global _active_run

    if _active_run and _active_run.get("running"):
        return {"status": "already_running", "run": _active_run.get("name")}

    run_name = req.name or f"{req.task}_{req.model_base.replace('.pt', '')}"
    _active_run = {
        "name": run_name,
        "running": True,
        "epochs": req.epochs,
        "current_epoch": 0,
        "dataset": req.dataset_path,
        "task": req.task,
    }

    asyncio.create_task(_run_training(req, run_name))
    return {"status": "started", "run_name": run_name, "epochs": req.epochs}


async def _run_training(req: Any, run_name: str) -> None:
    """Execute training in background (async-safe).

    Runs blocking YOLO training in thread pool to avoid
    blocking FastAPI event loop.

    Args:
        req: Training request parameters.
        run_name: Name for this training run.
    """
    global _active_run
    try:
        from ultralytics import YOLO

        def _train_model() -> Any:
            model = YOLO(req.model_base)
            RUNS_DIR.mkdir(parents=True, exist_ok=True)
            model.train(
                data=req.dataset_path,
                epochs=req.epochs,
                imgsz=req.imgsz,
                batch=req.batch,
                project=str(RUNS_DIR),
                name=run_name,
                device=0,
            )
            return model

        await asyncio.to_thread(_train_model)

        # Save best model
        best_path = RUNS_DIR / run_name / "weights" / "best.pt"
        if best_path.exists():
            MODELS_DIR.mkdir(parents=True, exist_ok=True)
            dest = MODELS_DIR / f"{run_name}_best.pt"
            shutil.copy2(best_path, dest)
            logger.info("Model saved: %s", dest)

        _active_run = {"name": run_name, "running": False, "completed": True}
    except Exception as e:
        logger.error("Training failed: %s", e)
        _active_run = {"name": run_name, "running": False, "error": str(e)}


async def get_training_status() -> dict[str, Any]:
    """Get current training run status.

    Returns:
        Dict with run info or idle status.
    """
    if _active_run:
        return _active_run
    return {"running": False, "status": "idle"}


async def list_models() -> dict[str, Any]:
    """List available trained models.

    Returns:
        Dict with models list.
    """
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    models = []
    for pt in sorted(MODELS_DIR.glob("*.pt"), key=lambda p: p.stat().st_mtime, reverse=True):
        models.append(
            {
                "name": pt.stem,
                "path": str(pt),
                "size_mb": round(pt.stat().st_size / 1024 / 1024, 1),
            }
        )
    return {"models": models, "count": len(models)}
