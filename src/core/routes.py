"""Core FastAPI routes for health, status, and configuration.

Provides service health checks, dependency status, and configuration endpoints.
"""

import asyncio
import logging
from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

logger = logging.getLogger(__name__)
router = APIRouter()

# Import app state from main
# This will be injected by the app initialization
_app_state: Any = None


def set_app_state(app_state: Any) -> None:
    """Set the app state reference for use in routes.

    Args:
        app_state: The AppState instance from main.py
    """
    global _app_state
    _app_state = app_state


@router.get("/health")
async def health() -> dict:
    """Endpoint de santé du service.

    Returns:
        Dictionnaire avec statut et état des dépendances.
    """
    if not _app_state:
        raise HTTPException(status_code=503, detail="app_state_not_initialized")

    # Toutes les dépendances manquantes → unhealthy
    if not (_app_state.postgres_ready or _app_state.qdrant_ready or _app_state.bonestore_ready):
        raise HTTPException(status_code=503, detail="no_dependencies_ready")

    status = "healthy"

    # Au moins une dépendance critique manquante → degraded
    if not (_app_state.postgres_ready and _app_state.qdrant_ready):
        status = "degraded"

    from . import __version__

    return {
        "status": status,
        "version": __version__,
        "dependencies": {
            "bonestore": _app_state.bonestore_ready,
            "postgres": _app_state.postgres_ready,
            "qdrant": _app_state.qdrant_ready,
            "cvat": _app_state.cvat_ready,
            "redis": _app_state.redis_ready,
        },
    }


@router.get("/ready")
async def ready() -> dict:
    """Endpoint de readiness pour orchestration.

    Returns:
        Statut de disponibilité du service.
    """
    if not _app_state:
        raise HTTPException(status_code=503, detail="app_state_not_initialized")

    all_ready = all(
        [
            _app_state.bonestore_ready,
            _app_state.postgres_ready,
            _app_state.qdrant_ready,
        ]
    )
    status = "ready" if all_ready else "not_ready"
    return {"status": status}


@router.get("/api/status")
async def status() -> dict:
    """Endpoint de statut détaillé.

    Returns:
        État détaillé de l'application et des modules.
    """
    if not _app_state:
        raise HTTPException(status_code=503, detail="app_state_not_initialized")

    from . import __version__

    return {
        "service": "bone-annotator",
        "version": __version__,
        "status": "development",
        "dependencies": {
            "bonestore": "✓" if _app_state.bonestore_ready else "✗",
            "postgres": "✓" if _app_state.postgres_ready else "✗",
            "qdrant": "✓" if _app_state.qdrant_ready else "✗",
            "cvat": "✓" if _app_state.cvat_ready else "✗",
            "redis": "✓" if _app_state.redis_ready else "✗",
        },
    }


@router.get("/")
async def root() -> dict:
    """Endpoint racine — informations générales du service."""
    from . import __version__

    return {
        "service": "bone-annotator",
        "version": __version__,
        "description": "Annotation des images d'os nus (fluoroscopie 360°)",
        "docs": "/docs",
        "status": "/api/status",
    }


@router.post("/api/working")
async def working_signal() -> dict:
    """Signal un traitement en cours pour le Dashboard Onyx.

    Returns:
        Confirmation du signal WORKING.
    """
    if not _app_state:
        raise HTTPException(status_code=503, detail="app_state_not_initialized")

    if _app_state.onyx_client:
        try:
            await _app_state.onyx_client.working()
        except Exception as e:
            logger.warning("⚠ Failed to send WORKING signal: %s", e)

    return {"status": "working_signaled"}


@router.get("/cron")
async def cron_tasks() -> dict:
    """Endpoint GET /cron — Liste et statut des tâches cron.

    Returns:
        Configuration des tâches cron définies dans cron.json.
    """
    return {
        "tasks": [
            {
                "id": "daily-health-check",
                "name": "Daily Health Check",
                "schedule": "0 0 * * *",
                "enabled": True,
                "description": "Vérification quotidienne de la santé du skill",
            },
            {
                "id": "hourly-sync-ingestion",
                "name": "Hourly Ingestion Sync",
                "schedule": "0 * * * *",
                "enabled": True,
                "description": "Synchronisation toutes les heures du registre d'ingestion",
            },
        ],
        "total": 2,
        "enabled": 2,
    }


@router.get("/api/config")
async def config_endpoint() -> dict:
    """Endpoint de configuration des dépendances externes.

    Returns:
        Dictionnaire avec configuration de toutes les dépendances.
    """
    from src.config import (
        BONESTORE_ROOT,
        get_cvat_config,
        get_dashboard_config,
        get_imaging_config,
        get_ml_compute_config,
        get_postgres_config,
        get_qdrant_config,
        get_redis_config,
    )

    from . import __version__

    return {
        "service": "bone-annotator",
        "version": __version__,
        "bonestore": {"root": BONESTORE_ROOT},
        "postgres": get_postgres_config(),
        "qdrant": get_qdrant_config(),
        "cvat": {**get_cvat_config(), "password": "***"},
        "ml_compute": get_ml_compute_config(),
        "redis": get_redis_config(),
        "imaging": get_imaging_config(),
        "dashboard": get_dashboard_config(),
    }


@router.get("/api/dependencies")
async def dependencies_endpoint() -> dict:
    """Endpoint détaillé de l'état de toutes les dépendances.

    Returns:
        État de chaque dépendance avec détails.
    """
    if not _app_state:
        raise HTTPException(status_code=503, detail="app_state_not_initialized")

    from src.config import check_all_dependencies

    deps_status = await check_all_dependencies()
    critical = ["postgres", "qdrant"]
    critical_ready = all(deps_status.get(dep) for dep in critical)

    return {
        "service": "bone-annotator",
        "timestamp": __import__("datetime").datetime.utcnow().isoformat(),
        "dependencies": {
            "bonestore": {"ready": _app_state.bonestore_ready, "critical": False},
            "postgres": {"ready": _app_state.postgres_ready, "critical": True},
            "qdrant": {"ready": _app_state.qdrant_ready, "critical": True},
            "cvat": {"ready": _app_state.cvat_ready, "critical": False},
            "redis": {"ready": _app_state.redis_ready, "critical": False},
        },
        "critical_ready": critical_ready,
        "overall_health": "healthy" if critical_ready else "degraded",
    }


@router.get("/annotate/")
async def annotate_page() -> HTMLResponse:
    """Dashboard principal d'annotation."""
    try:
        from pathlib import Path

        index_path = Path(__file__).resolve().parent.parent.parent / "static" / "index.html"
        return HTMLResponse(content=index_path.read_text())
    except Exception as e:
        logger.error("Failed to load index.html: %s", e)
        return HTMLResponse(content="<html><body>Dashboard not available</body></html>")


@router.get("/annotate/learning")
async def learning_page() -> HTMLResponse:
    """Learning progress dashboard (BoneSeg suivi)."""
    try:
        from pathlib import Path

        path = Path(__file__).resolve().parent.parent.parent / "static" / "learning.html"
        return HTMLResponse(content=path.read_text())
    except Exception as e:
        logger.error("Failed to load learning.html: %s", e)
        return HTMLResponse(content="<html><body>Learning dashboard unavailable</body></html>")


@router.get("/annotate/settings")
async def settings_page() -> HTMLResponse:
    """Settings page for imaging treatment and dashboard config."""
    try:
        from pathlib import Path

        path = Path(__file__).resolve().parent.parent.parent / "static" / "settings.html"
        return HTMLResponse(content=path.read_text())
    except Exception as e:
        logger.error("Failed to load settings.html: %s", e)
        return HTMLResponse(content="<html><body>Settings not available</body></html>")


@router.get("/annotate/annotations")
async def annotations_page() -> HTMLResponse:
    """Page de gestion des taches d'annotation."""
    try:
        from pathlib import Path

        path = Path(__file__).resolve().parent.parent.parent / "static" / "annotations.html"
        return HTMLResponse(content=path.read_text())
    except Exception as e:
        logger.error("Failed to load annotations.html: %s", e)
        return HTMLResponse(content="<html><body>Page not available</body></html>")


@router.get("/api/training/status")
async def training_status() -> dict:
    """État des tâches de training en cours.

    Returns:
        Dict avec liste des jobs de training.
    """
    # Placeholder - intégration avec ml-compute en Phase suivante
    return {
        "jobs": [],
        "total_running": 0,
        "total_completed": 0,
    }


@router.get("/api/annotations")
async def list_annotations(limit: int = 100, offset: int = 0) -> dict:
    """Lister les annotations avec filtrage.

    Args:
        limit: Nombre d'annotations max à retourner.
        offset: Décalage pour pagination.

    Returns:
        Liste des annotations et statuts.
    """
    # Placeholder - intégration avec PostgreSQL en Phase suivante
    return {
        "annotations": [],
        "total": 0,
        "limit": limit,
        "offset": offset,
    }


@router.get("/api/events")
async def events_stream():
    """Stream d'événements SSE pour updates en temps réel.

    Returns:
        Streaming Response avec événements.
    """
    from fastapi.responses import StreamingResponse

    async def event_generator():
        # Placeholder - implémentation réelle en Phase 4
        while True:
            data = (
                f'data: {{"type": "ping", "timestamp": "{__import__("datetime").datetime.utcnow().isoformat()}"}}\n\n'
            )
            yield data
            await asyncio.sleep(10)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache"},
    )
