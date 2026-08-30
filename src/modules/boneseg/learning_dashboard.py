"""Learning dashboard — aggregate bone-ml, ml-compute and local PG stats."""

import logging
from datetime import UTC, datetime
from typing import Any

import httpx

from src.config import get_bone_ml_config, get_learning_config, get_ml_compute_config, get_postgres_config
from src.modules.dashboard.service import get_service as get_dashboard_service
from src.modules.storage.decisions_db import create_decisions_db
from src.modules.storage.learning_db import create_learning_db

from .alerts import build_alerts, recommend_next_bone
from .gpu import check_gpu_available
from .milestones import DEFAULT_BONE_TYPES, next_milestone
from .ml_client import DEFAULT_AL_BONE, fetch_al_suggest, fetch_catalog_stats
from .model_comparison import get_model_comparison

logger = logging.getLogger(__name__)


async def _fetch_json(client: httpx.AsyncClient, url: str, **kwargs: Any) -> dict[str, Any] | list[Any] | None:
    """Fetch JSON from URL, return None on failure."""
    try:
        resp = await client.get(url, timeout=15.0, **kwargs)
        if resp.status_code == 200:
            return resp.json()
    except Exception as e:
        logger.debug("Fetch failed %s: %s", url, e)
    return None


def _build_progress_bars(gold_by_bone: dict[str, int], last_by_bone: dict[str, str | None]) -> list[dict[str, Any]]:
    """Build milestone progress bars per bone type."""
    bars = []
    for bone, gold in gold_by_bone.items():
        if gold == 0 and bone not in last_by_bone:
            continue
        target, label = next_milestone(gold)
        pct = min(100, round(gold / target * 100, 1)) if target else 0
        bars.append(
            {
                "bone_type": bone,
                "gold_count": gold,
                "milestone_target": target,
                "milestone_label": label,
                "percent": pct,
                "last_annotation": last_by_bone.get(bone),
            }
        )
    bars.sort(key=lambda x: x["gold_count"], reverse=True)
    return bars


def _estimate_days_to_milestone(gold: int, per_day: float, target: int) -> int | None:
    """Estimate days to reach milestone at current velocity."""
    if per_day <= 0 or gold >= target:
        return None
    return int((target - gold) / per_day)


def _publish_alerts(alerts: list[dict[str, Any]]) -> None:
    """Push learning alerts to SSE event bus for live dashboard."""
    if not alerts:
        return
    try:
        bus = get_dashboard_service()
        for alert in alerts[:10]:
            bus.publish_event("learning_alert", alert)
    except Exception as e:
        logger.debug("Could not publish learning alerts: %s", e)


async def get_learning_dashboard(bone_type: str | None = None) -> dict[str, Any]:
    """Aggregate all learning dashboard sections (1-12).

    Args:
        bone_type: Optional filter for bone-specific sections.

    Returns:
        Dashboard payload for the /annotate/learning UI.
    """
    learning_cfg = get_learning_config()
    learning_db = create_learning_db(**get_postgres_config())
    decisions_db = create_decisions_db(**get_postgres_config())
    bones = [bone_type] if bone_type else DEFAULT_BONE_TYPES
    local = learning_db.get_learning_stats(bones)
    quality = learning_db.get_quality_metrics()
    regression_alerts = learning_db.get_regression_alerts(learning_cfg["regression_threshold"])

    ml_config = get_bone_ml_config()
    compute_config = get_ml_compute_config()
    catalog_stats: dict[str, Any] = {}
    train_history: list[dict[str, Any]] = []
    catalog_new_count = 0
    al_suggest: dict[str, Any] = {}
    ml_dashboard: dict[str, Any] = {}
    ml_jobs: list[Any] = []

    async with httpx.AsyncClient() as client:
        catalog_stats = await fetch_catalog_stats(client, bone_type)

        hist_url = f"{ml_config['base_url']}/api/boneseg/train/history"
        if bone_type:
            hist_url += f"?bone_type={bone_type}"
        raw_hist = await _fetch_json(client, hist_url)
        if isinstance(raw_hist, list):
            train_history = raw_hist
        elif isinstance(raw_hist, dict):
            train_history = raw_hist.get("runs", raw_hist.get("history", []))

        new_url = f"{ml_config['base_url']}/api/boneseg/catalog/new?limit=1"
        raw_new = await _fetch_json(client, new_url)
        by_status = catalog_stats.get("by_status", {})
        catalog_new_count = catalog_stats.get("total", 0) or by_status.get("new", 0)
        if isinstance(raw_new, list) and not catalog_new_count:
            catalog_new_count = len(raw_new)
        elif isinstance(raw_new, dict) and not catalog_new_count:
            catalog_new_count = raw_new.get("count", raw_new.get("total", 0))

        al_suggest = await fetch_al_suggest(client, bone_type=bone_type or DEFAULT_AL_BONE, n_suggest=50)

        raw_ml = await _fetch_json(client, f"{ml_config['base_url']}/api/dashboard/stats")
        if isinstance(raw_ml, dict):
            ml_dashboard = raw_ml

        raw_jobs = await _fetch_json(
            client,
            f"http://{compute_config['host']}:{compute_config['port']}/api/jobs",
            params={"status": "running"},
        )
        if isinstance(raw_jobs, list):
            ml_jobs = raw_jobs
        elif isinstance(raw_jobs, dict):
            ml_jobs = raw_jobs.get("jobs", raw_jobs.get("results", []))

    gpu = await check_gpu_available()
    comparison = await get_model_comparison(bone_type, limit=12)
    tiers = local["tiers"]
    velocity = local["velocity"]
    per_day = velocity.get("per_day", 0)
    gold_by_bone = local["gold_by_bone"]
    primary_bone = bone_type or (max(gold_by_bone, key=gold_by_bone.get) if gold_by_bone else "humerus")
    gold_primary = gold_by_bone.get(primary_bone, 0)
    target, _ = next_milestone(gold_primary)

    week = velocity.get("week", 0)
    prev = velocity.get("prev_week", 0)
    week_delta = round((week - prev) / prev * 100, 1) if prev else None

    training = train_history or local.get("local_training", [])
    alerts = build_alerts(
        gold_by_bone=gold_by_bone,
        quality=quality,
        regression_alerts=regression_alerts,
        catalog_new_count=catalog_new_count,
        training_history=training if isinstance(training, list) else [],
        test_sets=local["test_sets"],
        new_acquisitions_threshold=learning_cfg["new_acquisitions_alert_threshold"],
        ml_ready_threshold=learning_cfg["ml_correction_ready_threshold"],
    )
    _publish_alerts(alerts)
    recommendation = recommend_next_bone(gold_by_bone)
    decisions = decisions_db.list_decisions(limit=30, bone_type=bone_type)

    return {
        "generated_at": datetime.now(tz=UTC).isoformat(),
        "bone_type_filter": bone_type,
        "progress": _build_progress_bars(gold_by_bone, local["last_annotation_by_bone"]),
        "tiers": {
            "gold": tiers.get("gold", 0),
            "silver": tiers.get("silver", 0),
            "pseudo": tiers.get("pseudo", 0),
            "total_annotated": sum(tiers.values()),
            "total_acquisitions": local.get("total_acquisitions", 0),
            "catalog": catalog_stats.get("by_tier", catalog_stats),
        },
        "training_history": training,
        "active_learning": {
            "new_acquisitions": catalog_new_count,
            "catalog_by_status": catalog_stats.get("by_status", {}),
            "suggestions_count": len(al_suggest.get("suggestions", [])),
            "strategy": al_suggest.get("strategy", "hybrid"),
            "pool_stats": al_suggest.get("pool_stats", {}),
            "model_version": al_suggest.get("model_version"),
        },
        "gpu": {
            "available": gpu.available,
            "boneseg_running": gpu.boneseg_running,
            "ml_compute_jobs": gpu.ml_compute_jobs,
            "reason": gpu.reason,
            "fleet": ml_dashboard.get("gpu", ml_dashboard.get("system", {})),
            "running_jobs": ml_jobs,
        },
        "test_sets": local["test_sets"],
        "velocity": {
            **velocity,
            "week_delta_pct": week_delta,
            "estimated_days_to_milestone": _estimate_days_to_milestone(gold_primary, per_day, target),
            "milestone_target": target,
            "primary_bone": primary_bone,
        },
        "alerts": alerts,
        "quality": quality,
        "decisions": decisions,
        "model_comparison": comparison,
        "recommendation": recommendation,
    }
