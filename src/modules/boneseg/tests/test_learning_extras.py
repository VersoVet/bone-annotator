"""Tests for learning dashboard sections 8-12."""

from src.modules.boneseg.alerts import build_alerts, recommend_next_bone


def test_build_regression_alert() -> None:
    """Regression alerts are included in build_alerts output."""
    regression = [
        {
            "type": "regression_dice",
            "severity": "warning",
            "bone_type": "humerus",
            "message": "test_dice drop",
            "drop": 0.05,
        }
    ]
    alerts = build_alerts(
        gold_by_bone={"humerus": 100},
        quality={"ml_correction_rate": 0.25},
        regression_alerts=regression,
        catalog_new_count=0,
        training_history=[],
        test_sets={},
    )
    assert any(a["type"] == "regression_dice" for a in alerts)


def test_pseudo_labeling_ready_alert() -> None:
    """Low ML correction rate triggers pseudo-labeling alert."""
    alerts = build_alerts(
        gold_by_bone={"humerus": 600},
        quality={"ml_correction_rate": 0.08},
        regression_alerts=[],
        catalog_new_count=0,
        training_history=[],
        test_sets={"humerus": {"count": 10}},
    )
    assert any(a["type"] == "pseudo_labeling_ready" for a in alerts)


def test_recommend_next_bone() -> None:
    """Recommend bone with lowest gold below first milestone."""
    assert recommend_next_bone({"humerus": 400, "femur": 600}) == "humerus"
    assert recommend_next_bone({}) == "humerus"


def test_weekly_report_markdown() -> None:
    """Weekly report formatter produces markdown sections."""
    from src.modules.boneseg.weekly_report import _format_report

    md = _format_report(
        {
            "velocity": {"week": 10, "prev_week": 8, "month": 40, "per_day": 1.4},
            "tiers": {"gold": 5, "silver": 3, "pseudo": 2},
            "training_history": [{"generation": 1, "bone_type": "humerus", "test_dice": 0.65, "status": "completed"}],
            "quality": {"ml_correction_rate": 0.12},
            "alerts": [],
            "model_comparison": {"items": []},
        },
        "humerus",
    )
    assert "Rapport hebdomadaire" in md
    assert "humerus" in md


def test_migrations_include_learning_decisions() -> None:
    """Learning decisions table is registered in migrations."""
    from src.modules.storage.task_db import _MIGRATIONS

    sql = "\n".join(_MIGRATIONS)
    assert "learning_decisions" in sql
