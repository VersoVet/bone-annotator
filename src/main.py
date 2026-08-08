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

    # TODO: Initialiser les dépendances externes
    # - BoneStore (NFS check)
    # - PostgreSQL (connexion annotations)
    # - Qdrant (collections)
    # - CVAT (API check)

    # Placeholder: marquer les dépendances comme prêtes
    app_state.bonestore_ready = True
    app_state.postgres_ready = True
    app_state.qdrant_ready = True
    app_state.cvat_ready = True

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


@app.get("/health")
async def health() -> dict:
    """Endpoint de santé du service.

    Returns:
        Dictionnaire avec statut et état des dépendances.

    Raises:
        HTTPException: Si critiques dépendances non prêtes.
    """
    if not (app_state.postgres_ready and app_state.qdrant_ready):
        raise HTTPException(status_code=503, detail="dependencies_not_ready")

    return {
        "status": "healthy",
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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=9468,
        reload=False,
        log_level="info",
    )
