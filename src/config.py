"""Configuration centralisée et checks de dépendances pour bone-annotator.

Gère les configurations de BoneStore, PostgreSQL, Qdrant, CVAT, ml-compute
et fournit des fonctions de vérification pour le lifespan.
"""

import logging
import os
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

# ===== CONFIGURATION ENV/DEFAULT =====

BONESTORE_ROOT = os.getenv("BONESTORE_ROOT", "/mnt/bonestore")

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "10.0.0.44")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
POSTGRES_USER = os.getenv("POSTGRES_USER", "bone")
POSTGRES_DBNAME = os.getenv("POSTGRES_DBNAME", "bone_annotations")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")

QDRANT_HOST = os.getenv("QDRANT_HOST", "10.0.0.59")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))
QDRANT_COLLECTIONS = ["bone_atlas", "bone_annotations"]

CVAT_HOST = os.getenv("CVAT_HOST", "10.0.0.59")
CVAT_PORT = int(os.getenv("CVAT_PORT", "8080"))
CVAT_USERNAME = os.getenv("CVAT_USERNAME", "admin")
CVAT_PASSWORD = os.getenv("CVAT_PASSWORD", "")

ML_COMPUTE_HOST = os.getenv("ML_COMPUTE_HOST", "10.0.0.44")
ML_COMPUTE_PORT = int(os.getenv("ML_COMPUTE_PORT", "9469"))

REDIS_HOST = os.getenv("REDIS_HOST", "10.0.0.44")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))

VAULT_URL = os.getenv("ONYX_VAULT_URL", "http://10.0.0.44:8050")
VAULT_TOKEN = os.getenv("ONYX_VAULT_TOKEN", "")


# ===== CHECK FUNCTIONS =====


async def check_bonestore() -> bool:
    """Vérifier que BoneStore NFS est montée et accessible.

    Returns:
        True si BoneStore est prêt.
    """
    try:
        path = Path(BONESTORE_ROOT)
        if not path.exists() or not path.is_dir():
            logger.error("BoneStore not mounted at %s", BONESTORE_ROOT)
            return False
        # Test read access
        list(path.iterdir())
        logger.info("✓ BoneStore mounted: %s", BONESTORE_ROOT)
        return True
    except Exception as e:
        logger.error("BoneStore check failed: %s", e)
        return False


async def check_postgres() -> bool:
    """Vérifier la connexion à PostgreSQL.

    Returns:
        True si PostgreSQL est accessible.
    """
    try:
        import psycopg

        conninfo = f"host={POSTGRES_HOST} port={POSTGRES_PORT} user={POSTGRES_USER} dbname={POSTGRES_DBNAME}"
        if POSTGRES_PASSWORD:
            conninfo += f" password={POSTGRES_PASSWORD}"
        conn = psycopg.connect(conninfo, connect_timeout=5)
        conn.close()
        logger.info("✓ PostgreSQL connected: %s:%d", POSTGRES_HOST, POSTGRES_PORT)
        return True
    except Exception as e:
        logger.error("PostgreSQL check failed: %s", e)
        return False


async def check_qdrant() -> bool:
    """Vérifier la connexion à Qdrant.

    Returns:
        True si Qdrant est accessible.
    """
    try:
        from qdrant_client import QdrantClient

        client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT, timeout=5)
        # Try to get collection info
        collections = [c.name for c in client.get_collections().collections]
        logger.info("✓ Qdrant connected: %s:%d (%d collections)", QDRANT_HOST, QDRANT_PORT, len(collections))
        return True
    except Exception as e:
        logger.error("Qdrant check failed: %s", e)
        return False


async def check_cvat() -> bool:
    """Vérifier la connexion à CVAT API.

    Returns:
        True si CVAT est accessible.
    """
    try:
        import httpx

        url = f"http://{CVAT_HOST}:{CVAT_PORT}/api/v1/auth/login"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5.0)
            if response.status_code == 401:  # 401 means API is up but auth failed
                logger.info("✓ CVAT API accessible: %s:%d", CVAT_HOST, CVAT_PORT)
                return True
            elif response.status_code == 200:
                logger.info("✓ CVAT API accessible: %s:%d", CVAT_HOST, CVAT_PORT)
                return True
            else:
                logger.error("CVAT API check failed: status %d", response.status_code)
                return False
    except Exception as e:
        logger.error("CVAT check failed: %s", e)
        return False


async def check_ml_compute() -> bool:
    """Vérifier la connexion à ml-compute Ray API.

    Returns:
        True si ml-compute est accessible.
    """
    try:
        import httpx

        url = f"http://{ML_COMPUTE_HOST}:{ML_COMPUTE_PORT}/health"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5.0)
            if response.status_code == 200:
                logger.info("✓ ml-compute accessible: %s:%d", ML_COMPUTE_HOST, ML_COMPUTE_PORT)
                return True
            else:
                logger.warning("ml-compute health check failed: status %d", response.status_code)
                return False
    except Exception as e:
        logger.error("ml-compute check failed: %s", e)
        return False


async def check_redis() -> bool:
    """Vérifier la connexion à Redis.

    Returns:
        True si Redis est accessible.
    """
    try:
        import redis

        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, socket_connect_timeout=5)
        r.ping()
        logger.info("✓ Redis connected: %s:%d", REDIS_HOST, REDIS_PORT)
        return True
    except Exception as e:
        logger.error("Redis check failed: %s", e)
        return False


async def load_vault_secret(key: str) -> str | None:
    """Charger un secret depuis OnyxVault.

    Args:
        key: Clé du secret.

    Returns:
        Valeur du secret ou None si échoué.
    """
    if not VAULT_TOKEN:
        logger.warning("VAULT_TOKEN not set, skipping vault lookup")
        return None

    try:
        import httpx

        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{VAULT_URL}/vault/{key}",
                headers={"X-Vault-Token": VAULT_TOKEN},
                timeout=5.0,
            )
            if response.status_code == 200:
                return response.json().get("value")
            else:
                logger.warning("Vault lookup failed for %s: status %d", key, response.status_code)
                return None
    except Exception as e:
        logger.error("Vault lookup failed for %s: %s", key, e)
        return None


def get_postgres_config() -> dict[str, Any]:
    """Obtenir la configuration PostgreSQL complète.

    Returns:
        Dict avec host, port, user, dbname, password.
    """
    return {
        "host": POSTGRES_HOST,
        "port": POSTGRES_PORT,
        "user": POSTGRES_USER,
        "dbname": POSTGRES_DBNAME,
        "password": POSTGRES_PASSWORD,
    }


def get_qdrant_config() -> dict[str, Any]:
    """Obtenir la configuration Qdrant complète.

    Returns:
        Dict avec host, port, collections.
    """
    return {
        "host": QDRANT_HOST,
        "port": QDRANT_PORT,
        "collections": QDRANT_COLLECTIONS,
    }


def get_cvat_config() -> dict[str, Any]:
    """Obtenir la configuration CVAT complète.

    Returns:
        Dict avec host, port, username, password.
    """
    return {
        "host": CVAT_HOST,
        "port": CVAT_PORT,
        "username": CVAT_USERNAME,
        "password": CVAT_PASSWORD,
    }


def get_ml_compute_config() -> dict[str, Any]:
    """Obtenir la configuration ml-compute.

    Returns:
        Dict avec host, port.
    """
    return {
        "host": ML_COMPUTE_HOST,
        "port": ML_COMPUTE_PORT,
    }


def get_redis_config() -> dict[str, Any]:
    """Obtenir la configuration Redis.

    Returns:
        Dict avec host, port, db.
    """
    return {
        "host": REDIS_HOST,
        "port": REDIS_PORT,
        "db": REDIS_DB,
    }


async def check_all_dependencies() -> dict[str, bool]:
    """Vérifier toutes les dépendances.

    Returns:
        Dict avec status de chaque dépendance.
    """
    return {
        "bonestore": await check_bonestore(),
        "postgres": await check_postgres(),
        "qdrant": await check_qdrant(),
        "cvat": await check_cvat(),
        "ml_compute": await check_ml_compute(),
        "redis": await check_redis(),
    }
