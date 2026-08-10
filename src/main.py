"""Point d'entrée FastAPI pour bone-annotator.

Service d'annotation d'images osseuses avec pré-annotation YOLO automatique.
Gère l'accès à BoneStore (NFS), PostgreSQL annotations, CVAT, et ml-compute.
"""

import asyncio
import json
import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException

try:
    from onyx_sdk import OnyxClient
except ImportError:
    OnyxClient = None  # type: ignore

# Configure logging
logger = logging.getLogger("bone-annotator")
logging.basicConfig(level=logging.INFO)


# Load version from manifest.json
def _load_version() -> str:
    """Load version from manifest.json."""
    try:
        manifest_path = Path(__file__).resolve().parent.parent / "manifest.json"
        with manifest_path.open() as f:
            manifest = json.load(f)
            return manifest.get("version", "0.1.0")
    except Exception:
        return "0.1.0"


__version__ = _load_version()


# Dépendances globales (à initialiser au démarrage)
class AppState:
    """État global de l'application."""

    bonestore_ready: bool = False
    postgres_ready: bool = False
    qdrant_ready: bool = False
    cvat_ready: bool = False
    redis_ready: bool = False
    onyx_client: object | None = None


app_state = AppState()


async def wait_for_dependency(
    name: str,
    check_fn,
    *,
    retries: int = 5,
    base_delay: float = 1.0,
    max_delay: float = 30.0,
) -> bool:
    """Attend qu'une dépendance soit prête avec backoff exponentiel.

    Args:
        name: Nom de la dépendance (pour logs).
        check_fn: Fonction async retournant True si prêt.
        retries: Nombre de tentatives.
        base_delay: Délai initial en secondes.
        max_delay: Délai maximal en secondes.

    Returns:
        True si dépendance prête, False après timeout.
    """
    for attempt in range(retries):
        try:
            if await check_fn():
                logger.info(f"✓ {name} ready")
                return True
        except Exception as e:
            logger.warning(f"✗ {name} check failed (attempt {attempt + 1}): {e}")
        if attempt < retries - 1:
            delay = min(base_delay * (2**attempt), max_delay)
            await asyncio.sleep(delay)
    logger.error(f"✗ {name} failed to initialize after {retries} retries")
    return False


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gère le cycle de vie de l'application."""
    logger.info("🚀 bone-annotator starting...")

    # Initialiser OnyxClient pour intégration Onyx Dashboard
    if OnyxClient:
        try:
            app_state.onyx_client = OnyxClient()
            await app_state.onyx_client.start()  # Signal UP au Dashboard
            await app_state.onyx_client.working()  # Signal WORKING en cours
            app_state.redis_ready = True
            logger.info("✓ OnyxClient initialized")
        except Exception as e:
            logger.warning(f"⚠ OnyxClient failed: {e}")
            app_state.redis_ready = False
    else:
        logger.warning("⚠ onyx_sdk not available")
        app_state.redis_ready = False

    # Vérifier les dépendances externes avec backoff exponentiel
    from src.config import (
        check_bonestore,
        check_cvat,
        check_postgres,
        check_qdrant,
    )

    logger.info("Initializing external dependencies...")
    app_state.bonestore_ready = await wait_for_dependency(
        "BoneStore NFS",
        check_bonestore,
        retries=3,
        base_delay=1.0,
    )
    app_state.postgres_ready = await wait_for_dependency(
        "PostgreSQL",
        check_postgres,
        retries=3,
        base_delay=1.0,
    )
    app_state.qdrant_ready = await wait_for_dependency(
        "Qdrant",
        check_qdrant,
        retries=3,
        base_delay=1.0,
    )
    app_state.cvat_ready = await wait_for_dependency(
        "CVAT API",
        check_cvat,
        retries=2,
        base_delay=1.0,
    )

    logger.info("✓ All dependencies initialized")

    yield

    logger.info("🛑 bone-annotator shutting down...")
    if app_state.onyx_client:
        try:
            await app_state.onyx_client.stop()  # Signal DOWN au Dashboard
        except Exception as e:
            logger.warning(f"⚠ Failed to publish shutdown status: {e}")
    logger.info("✓ Shutdown complete")


app = FastAPI(
    title="bone-annotator",
    description="Annotation des images osseuses fluoroscopie 360°",
    version=__version__,
    lifespan=lifespan,
)

# Include annotation module routes
try:
    from src.modules.annotation.routes import router as annotation_router

    app.include_router(annotation_router)
    logger.info("✓ Annotation routes registered")
except ImportError as e:
    logger.warning("Could not load annotation routes: %s", e)


@app.get("/health")
async def health() -> dict:
    """Endpoint de santé du service.

    Returns:
        Dictionnaire avec statut et état des dépendances.
    """
    # Toutes les dépendances manquantes → unhealthy
    if not (app_state.postgres_ready or app_state.qdrant_ready or app_state.bonestore_ready):
        raise HTTPException(status_code=503, detail="no_dependencies_ready")

    status = "healthy"

    # Au moins une dépendance critique manquante → degraded
    if not (app_state.postgres_ready and app_state.qdrant_ready):
        status = "degraded"

    return {
        "status": status,
        "version": __version__,
        "dependencies": {
            "bonestore": app_state.bonestore_ready,
            "postgres": app_state.postgres_ready,
            "qdrant": app_state.qdrant_ready,
            "cvat": app_state.cvat_ready,
            "redis": app_state.redis_ready,
        },
    }


@app.get("/ready")
async def ready() -> dict:
    """Endpoint de readiness pour orchestration.

    Returns:
        Statut de disponibilité du service.
    """
    all_ready = all(
        [
            app_state.bonestore_ready,
            app_state.postgres_ready,
            app_state.qdrant_ready,
        ]
    )
    status = "ready" if all_ready else "not_ready"
    return {"status": status}


@app.get("/api/status")
async def status() -> dict:
    """Endpoint de statut détaillé.

    Returns:
        État détaillé de l'application et des modules.
    """
    return {
        "service": "bone-annotator",
        "version": __version__,
        "status": "development",
        "dependencies": {
            "bonestore": "✓" if app_state.bonestore_ready else "✗",
            "postgres": "✓" if app_state.postgres_ready else "✗",
            "qdrant": "✓" if app_state.qdrant_ready else "✗",
            "cvat": "✓" if app_state.cvat_ready else "✗",
            "redis": "✓" if app_state.redis_ready else "✗",
        },
    }


@app.get("/")
async def root() -> dict:
    """Endpoint racine — informations générales du service."""
    return {
        "service": "bone-annotator",
        "version": __version__,
        "description": "Annotation des images d'os nus (fluoroscopie 360°)",
        "docs": "/docs",
        "status": "/api/status",
    }


@app.post("/api/working")
async def working_signal() -> dict:
    """Signal un traitement en cours pour le Dashboard Onyx.

    Returns:
        Confirmation du signal WORKING.
    """
    if app_state.onyx_client:
        try:
            await app_state.onyx_client.working()
        except Exception as e:
            logger.warning(f"⚠ Failed to send WORKING signal: {e}")

    return {"status": "working_signaled"}


@app.get("/cron")
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


@app.get("/api/config")
async def config_endpoint() -> dict:
    """Endpoint de configuration des dépendances externes.

    Returns:
        Dictionnaire avec configuration de toutes les dépendances.
    """
    from src.config import (
        BONESTORE_ROOT,
        get_cvat_config,
        get_ml_compute_config,
        get_postgres_config,
        get_qdrant_config,
        get_redis_config,
    )

    return {
        "service": "bone-annotator",
        "version": __version__,
        "bonestore": {"root": BONESTORE_ROOT},
        "postgres": get_postgres_config(),
        "qdrant": get_qdrant_config(),
        "cvat": {**get_cvat_config(), "password": "***"},
        "ml_compute": get_ml_compute_config(),
        "redis": get_redis_config(),
    }


@app.get("/api/dependencies")
async def dependencies_endpoint() -> dict:
    """Endpoint détaillé de l'état de toutes les dépendances.

    Returns:
        État de chaque dépendance avec détails.
    """
    from src.config import check_all_dependencies

    deps_status = await check_all_dependencies()
    critical = ["postgres", "qdrant"]
    critical_ready = all(deps_status.get(dep) for dep in critical)

    return {
        "service": "bone-annotator",
        "timestamp": __import__("datetime").datetime.utcnow().isoformat(),
        "dependencies": {
            "bonestore": {"ready": app_state.bonestore_ready, "critical": False},
            "postgres": {"ready": app_state.postgres_ready, "critical": True},
            "qdrant": {"ready": app_state.qdrant_ready, "critical": True},
            "cvat": {"ready": app_state.cvat_ready, "critical": False},
            "redis": {"ready": app_state.redis_ready, "critical": False},
        },
        "critical_ready": critical_ready,
        "overall_health": "healthy" if critical_ready else "degraded",
    }


@app.get("/annotate/")
async def annotate_page() -> str:
    """Dashboard principal d'annotation.

    Returns:
        Contenu HTML du dashboard.
    """
    try:
        from pathlib import Path

        index_path = Path(__file__).resolve().parent.parent / "static" / "index.html"
        with index_path.open() as f:
            return f.read()
    except Exception as e:
        logger.error("Failed to load index.html: %s", e)
        return "<html><body>Dashboard not available</body></html>"


@app.get("/api/training/status")
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


@app.get("/api/annotations")
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


@app.get("/api/events")
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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=9468,
        reload=False,
        log_level="info",
    )
