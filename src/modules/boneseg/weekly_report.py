"""Weekly learning report — Markdown summary and optional email delivery."""

import logging
from datetime import UTC, datetime
from typing import Any

import httpx

from src.config import get_email_config, get_learning_config, get_postgres_config
from src.modules.boneseg.alerts import recommend_next_bone
from src.modules.boneseg.learning_dashboard import get_learning_dashboard
from src.modules.storage.decisions_db import create_decisions_db

logger = logging.getLogger(__name__)


def _format_report(data: dict[str, Any], recommendation: str) -> str:
    """Build Markdown weekly report from dashboard payload."""
    v = data.get("velocity", {})
    t = data.get("tiers", {})
    lines = [
        f"# Rapport hebdomadaire BoneSeg — {datetime.now(tz=UTC).strftime('%Y-%m-%d')}",
        "",
        "## Annotations",
        f"- Cette semaine: **{v.get('week', 0)}** frames validées",
        f"- Semaine précédente: {v.get('prev_week', 0)}",
        f"- Ce mois: {v.get('month', 0)}",
        f"- Rythme: ~{v.get('per_day', 0)} frames/jour",
        "",
        "## Tiers",
        f"- GOLD: {t.get('gold', 0)} · SILVER: {t.get('silver', 0)} · PSEUDO: {t.get('pseudo', 0)}",
        "",
        "## Modèle",
    ]
    runs = data.get("training_history") or []
    if runs:
        latest = runs[0]
        dice = latest.get("test_dice") or latest.get("best_dice")
        lines.append(
            f"- Dernier run: gen {latest.get('generation', '?')} ({latest.get('bone_type', '?')})"
            + (f" — Dice {dice:.3f}" if dice is not None else "")
        )
    else:
        lines.append("- Aucun entraînement enregistré cette période")

    quality = data.get("quality") or {}
    rate = quality.get("ml_correction_rate")
    if rate is not None:
        lines.extend(["", "## Qualité ML", f"- Taux correction à validation: **{rate * 100:.1f}%**"])

    alerts = data.get("alerts") or []
    if alerts:
        lines.extend(["", "## Alertes actives"])
        for a in alerts[:8]:
            lines.append(f"- [{a.get('severity', 'info')}] {a.get('message', '')}")

    comp = data.get("model_comparison") or {}
    uncertain = comp.get("items") or []
    if uncertain and uncertain[0].get("acquisition_id") != "—":
        lines.extend(["", "## Cas les plus incertains"])
        for c in uncertain[:5]:
            u = c.get("uncertainty")
            lines.append(
                f"- {c.get('acquisition_id')} ({c.get('bone_type')}) — incertitude {u:.3f}"
                if u
                else f"- {c.get('acquisition_id')}"
            )

    lines.extend(["", "## Recommandation", f"Prioriser les annotations **{recommendation}**.", ""])
    return "\n".join(lines)


async def generate_weekly_report(*, send_email: bool = False) -> dict[str, Any]:
    """Generate weekly Markdown report; optionally email via email skill.

    Args:
        send_email: When True, POST report to email service.

    Returns:
        Report body and delivery status.
    """
    dashboard = await get_learning_dashboard()
    recommendation = recommend_next_bone({p["bone_type"]: p["gold_count"] for p in dashboard.get("progress", [])})
    markdown = _format_report(dashboard, recommendation)

    result: dict[str, Any] = {
        "status": "ok",
        "generated_at": datetime.now(tz=UTC).isoformat(),
        "markdown": markdown,
        "recommendation": recommendation,
        "email_sent": False,
    }

    if send_email:
        email_cfg = get_email_config()
        learning_cfg = get_learning_config()
        recipient = learning_cfg.get("report_email_to") or email_cfg.get("default_to")
        if not recipient:
            result["email_error"] = "No report_email_to configured"
        else:
            try:
                async with httpx.AsyncClient() as client:
                    resp = await client.post(
                        f"{email_cfg['base_url']}/api/send",
                        json={
                            "to": recipient,
                            "subject": f"[BoneSeg] Rapport hebdomadaire — {datetime.now(tz=UTC).strftime('%Y-%m-%d')}",
                            "body": markdown,
                        },
                        timeout=30.0,
                    )
                    result["email_sent"] = resp.status_code == 200
                    if resp.status_code != 200:
                        result["email_error"] = resp.text[:200]
            except Exception as e:
                logger.warning("Weekly report email failed: %s", e)
                result["email_error"] = str(e)

    decisions_db = create_decisions_db(**get_postgres_config())
    gold, silver = dashboard.get("tiers", {}).get("gold", 0), dashboard.get("tiers", {}).get("silver", 0)
    decisions_db.log_decision(
        "weekly_report_generated",
        gold_count=gold,
        silver_count=silver,
        trigger_source="cron" if send_email else "api",
        payload={"recommendation": recommendation, "email_sent": result.get("email_sent", False)},
        notes="Rapport hebdomadaire auto-généré",
    )
    return result
