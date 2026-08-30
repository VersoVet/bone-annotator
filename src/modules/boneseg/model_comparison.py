"""Model vs human comparison — proxy bone-ml predict with local fallback."""

import logging
from typing import Any

import httpx

from src.config import get_bone_ml_config, get_postgres_config
from src.modules.storage.learning_db import create_learning_db

logger = logging.getLogger(__name__)


async def get_model_comparison(
    bone_type: str | None = None,
    limit: int = 12,
) -> dict[str, Any]:
    """Fetch comparison grid: uncertain cases + optional bone-ml predictions.

    Args:
        bone_type: Optional bone filter.
        limit: Max grid items.

    Returns:
        Grid items with uncertainty and prediction metadata.
    """
    learning_db = create_learning_db(**get_postgres_config())
    local_cases = learning_db.get_uncertainty_cases(bone_type, limit)
    ml_config = get_bone_ml_config()
    enriched: list[dict[str, Any]] = []

    async with httpx.AsyncClient() as client:
        for case in local_cases:
            item = {**case, "model_mask_url": None, "human_mask_url": None, "dice_gap": None}
            try:
                resp = await client.post(
                    f"{ml_config['base_url']}/api/boneseg/predict",
                    json={
                        "acquisition_id": case["acquisition_id"],
                        "return_uncertainty": True,
                    },
                    timeout=30.0,
                )
                if resp.status_code == 200:
                    pred = resp.json()
                    item["dice_gap"] = pred.get("dice_vs_human") or pred.get("uncertainty")
                    item["model_mask_url"] = pred.get("prediction_url") or pred.get("mask_url")
                    item["human_mask_url"] = pred.get("human_url") or pred.get("annotation_url")
                    if pred.get("uncertainty") is not None:
                        item["uncertainty"] = pred["uncertainty"]
            except Exception as e:
                logger.debug("Predict failed for %s: %s", case["acquisition_id"], e)
            enriched.append(item)

    if not enriched and not local_cases:
        enriched = [
            {
                "acquisition_id": "—",
                "bone_type": bone_type or "—",
                "uncertainty": None,
                "projection": None,
                "ml_status": "no_data",
                "note": "Catalogue vide — lancer sync BoneStore et scoring incertitude",
            }
        ]

    return {
        "bone_type": bone_type,
        "total": len(enriched),
        "items": enriched,
        "source": "bonestore_catalog+predict" if enriched else "empty",
    }
