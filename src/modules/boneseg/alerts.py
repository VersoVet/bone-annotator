"""Learning alerts — milestones, regressions, catalog and training signals."""

from typing import Any

from src.modules.boneseg.milestones import MILESTONES, next_milestone


def build_alerts(
    *,
    gold_by_bone: dict[str, int],
    quality: dict[str, Any],
    regression_alerts: list[dict[str, Any]],
    catalog_new_count: int,
    training_history: list[dict[str, Any]],
    test_sets: dict[str, Any],
    new_acquisitions_threshold: int = 100,
    ml_ready_threshold: float = 0.10,
) -> list[dict[str, Any]]:
    """Build active alert list for dashboard section 8."""
    alerts: list[dict[str, Any]] = list(regression_alerts)

    for bone, gold in gold_by_bone.items():
        if gold <= 0:
            continue
        target, label = next_milestone(gold)
        if gold >= target:
            alerts.append(
                {
                    "type": "milestone_reached",
                    "severity": "info",
                    "bone_type": bone,
                    "message": f"Jalon atteint — {bone}: {gold} GOLD ({label})",
                    "gold_count": gold,
                    "milestone": target,
                }
            )
        elif target - gold <= max(25, int(target * 0.05)):
            alerts.append(
                {
                    "type": "milestone_near",
                    "severity": "info",
                    "bone_type": bone,
                    "message": f"Proche du jalon {target} — {bone}: {gold} GOLD",
                    "gold_count": gold,
                    "milestone": target,
                }
            )
        if bone in ("humerus", "femur") and not test_sets.get(bone):
            alerts.append(
                {
                    "type": "test_set_missing",
                    "severity": "warning",
                    "bone_type": bone,
                    "message": f"Test set {bone} non défini — gel recommandé avant training",
                }
            )

    rate = quality.get("ml_correction_rate")
    if rate is not None:
        if rate < ml_ready_threshold:
            alerts.append(
                {
                    "type": "pseudo_labeling_ready",
                    "severity": "info",
                    "message": f"Taux correction ML {rate * 100:.0f}% — pseudo-labeling à grande échelle possible",
                    "ml_correction_rate": rate,
                }
            )
        elif rate > 0.30:
            alerts.append(
                {
                    "type": "ml_correction_high",
                    "severity": "warning",
                    "message": f"Taux correction ML élevé ({rate * 100:.0f}%) — modèle pas encore fiable",
                    "ml_correction_rate": rate,
                }
            )

    if catalog_new_count >= new_acquisitions_threshold:
        alerts.append(
            {
                "type": "new_acquisitions",
                "severity": "info",
                "message": f"{catalog_new_count} nouvelles acquisitions BoneStore détectées",
                "count": catalog_new_count,
            }
        )

    completed = [r for r in training_history if r.get("status") == "completed"]
    if completed:
        latest = completed[0]
        dice = latest.get("test_dice") or latest.get("best_dice")
        alerts.append(
            {
                "type": "training_completed",
                "severity": "info",
                "bone_type": latest.get("bone_type"),
                "message": (
                    f"Modèle gen {latest.get('generation', '?')} prêt"
                    + (f" — test Dice {dice:.3f}" if dice is not None else "")
                ),
                "generation": latest.get("generation"),
                "test_dice": dice,
            }
        )

    severity_order = {"critical": 0, "warning": 1, "info": 2}
    alerts.sort(key=lambda a: severity_order.get(a.get("severity", "info"), 9))
    return alerts


def recommend_next_bone(gold_by_bone: dict[str, int]) -> str:
    """Suggest which bone type to prioritize next."""
    if not gold_by_bone:
        return "humerus"
    candidates = [(b, g) for b, g in gold_by_bone.items() if g > 0]
    if not candidates:
        return "humerus"
    below_first = [(b, g) for b, g in candidates if g < MILESTONES[0]]
    if below_first:
        return min(below_first, key=lambda x: x[1])[0]
    below_second = [(b, g) for b, g in candidates if g < MILESTONES[1]]
    if below_second:
        return min(below_second, key=lambda x: x[1])[0]
    return min(candidates, key=lambda x: x[1])[0]
