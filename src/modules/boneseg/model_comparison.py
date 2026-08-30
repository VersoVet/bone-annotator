"""Model vs human comparison — bone-ml catalog with local uncertainty fallback."""

import logging
from typing import Any

import httpx

from src.config import get_bone_ml_config, get_postgres_config
from src.modules.storage.learning_db import create_learning_db

from .ml_client import DEFAULT_AL_BONE, fetch_catalog_new

logger = logging.getLogger(__name__)


def _catalog_entry_to_case(entry: dict[str, Any]) -> dict[str, Any]:
    """Normalize bone-ml catalog entry to comparison grid item."""
    return {
        "acquisition_id": entry.get("acquisition_id") or entry.get("id", ""),
        "bone_type": entry.get("bone_type"),
        "uncertainty": entry.get("uncertainty_score") or entry.get("uncertainty"),
        "projection": entry.get("category"),
        "ml_status": entry.get("ml_status", "new"),
    }


async def get_model_comparison(
    bone_type: str | None = None,
    limit: int = 12,
) -> dict[str, Any]:
    """Fetch comparison grid from local scores or bone-ml catalog."""
    learning_db = create_learning_db(**get_postgres_config())
    local_cases = learning_db.get_uncertainty_cases(bone_type, limit)
    source = "bonestore_catalog"

    if not local_cases:
        async with httpx.AsyncClient() as client:
            remote = await fetch_catalog_new(client, bone_type=bone_type or DEFAULT_AL_BONE, limit=limit)
        local_cases = [_catalog_entry_to_case(e) for e in remote if e.get("acquisition_id")]
        source = "bone_ml_catalog"

    ml_config = get_bone_ml_config()
    enriched: list[dict[str, Any]] = []

    async with httpx.AsyncClient() as client:
        for case in local_cases[:limit]:
            item = {**case, "model_mask_url": None, "human_mask_url": None, "dice_gap": None}
            acq_id = case.get("acquisition_id")
            if not acq_id or acq_id == "—":
                enriched.append(item)
                continue
            try:
                resp = await client.post(
                    f"{ml_config['base_url']}/api/boneseg/predict",
                    json={"acquisition_id": acq_id, "return_uncertainty": True},
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
                logger.debug("Predict failed for %s: %s", acq_id, e)
            enriched.append(item)

    if not enriched:
        enriched = [
            {
                "acquisition_id": "—",
                "bone_type": bone_type or DEFAULT_AL_BONE,
                "uncertainty": None,
                "projection": None,
                "ml_status": "no_data",
                "note": "Catalogue bone-ml vide — vérifier sync BoneStore",
            }
        ]

    return {"bone_type": bone_type, "total": len(enriched), "items": enriched, "source": f"{source}+predict"}
