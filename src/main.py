"""Point d'entrée FastAPI pour bone-annotator.

Service d'annotation d'images osseuses avec pré-annotation YOLO automatique.
Gère l'accès à BoneStore (NFS), PostgreSQL annotations, CVAT, et ml-compute.
"""

import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

try:
    from onyx_sdk import OnyxClient
except ImportError:
    OnyxClient = None  # type: ignore

from src.core import __version__
from src.core.routes import router as core_router
from src.core.routes import set_app_state

# Configure logging
logger = logging.getLogger("bone-annotator")
logging.basicConfig(level=logging.INFO)


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

    # Charger les credentials PACS depuis le Vault
    from src.config import (
        check_bonestore,
        check_cvat,
        check_postgres,
        check_qdrant,
        load_pacs_credentials_from_vault,
    )

    try:
        await load_pacs_credentials_from_vault()
    except Exception as e:
        logger.warning("Failed to load PACS credentials from Vault: %s", e)

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

    # Run annotation task schema migrations if PostgreSQL is ready
    if app_state.postgres_ready:
        try:
            from src.config import get_postgres_config
            from src.modules.storage.task_db import create_task_db

            pg_cfg = get_postgres_config()
            task_db = create_task_db(**pg_cfg)
            task_db.run_migrations()
            task_db.close()
            logger.info("✓ Annotation task migrations completed")
        except Exception as e:
            logger.warning("⚠ Task migrations failed: %s", e)

    # Inject app_state into core routes
    set_app_state(app_state)

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

# Include core routes (health, status, config)
app.include_router(core_router)
logger.info("✓ Core routes registered")

# Include module routers
_module_routers = [
    ("annotation", "src.modules.annotation.routes"),
    ("ml", "src.modules.ml.routes"),
    ("predict", "src.modules.ml.predict.routes"),
    ("ingestion", "src.modules.ingestion.routes"),
    ("bonestore", "src.modules.bonestore.routes"),
    ("embeddings", "src.modules.embeddings.routes"),
    ("dashboard", "src.modules.dashboard.routes"),
    ("sources", "src.modules.sources.routes"),
    ("preparation", "src.modules.preparation.routes"),
    ("imaging", "src.modules.imaging.routes"),
    ("analysis", "src.modules.analysis.routes"),
    ("cvat", "src.modules.cvat.routes"),
    ("labels", "src.modules.labels.routes"),
]

for module_name, module_path in _module_routers:
    try:
        module = __import__(module_path, fromlist=["router"])
        app.include_router(module.router)
        logger.info(f"✓ {module_name} routes registered")
    except ImportError as e:
        logger.warning(f"Could not load {module_name} routes: {e}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=9468,
        reload=False,
        log_level="info",
    )
