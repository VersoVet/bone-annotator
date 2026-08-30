"""Configuration centralisée pour bone-annotator.

Charge la config depuis config/bone-annotator.yaml, avec fallback
sur les variables d'environnement et le Vault pour les secrets.
"""

import logging
import os
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)

_SKILL_ROOT = Path(__file__).parent.parent
_CONFIG_PATH = _SKILL_ROOT / "config" / "bone-annotator.yaml"


def _load_yaml_config() -> dict[str, Any]:
    """Load configuration from YAML file."""
    try:
        with open(_CONFIG_PATH) as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        logger.warning("Cannot load config YAML: %s", e)
        return {}


_CFG = _load_yaml_config()


def _get(section: str, key: str, env_var: str, default: Any = "") -> Any:
    """Get config value: env var > yaml > default."""
    env = os.getenv(env_var)
    if env is not None:
        return env
    return _CFG.get(section, {}).get(key, default)


# ===== CONFIGURATION =====

BONESTORE_ROOT = _get("bonestore", "root", "BONESTORE_ROOT", "/mnt/bonestore")

POSTGRES_HOST = _get("postgres", "host", "POSTGRES_HOST", "10.0.0.59")
POSTGRES_PORT = int(_get("postgres", "port", "POSTGRES_PORT", 5432))
POSTGRES_USER = _get("postgres", "user", "POSTGRES_USER", "bone")
POSTGRES_DBNAME = _get("postgres", "dbname", "POSTGRES_DBNAME", "bone_recognition")
POSTGRES_PASSWORD = _get("postgres", "password", "POSTGRES_PASSWORD", "")
POSTGRES_SCHEMA = _get("postgres", "schema", "POSTGRES_SCHEMA", "bone_annotations")

QDRANT_HOST = _get("qdrant", "host", "QDRANT_HOST", "10.0.0.59")
QDRANT_PORT = int(_get("qdrant", "port", "QDRANT_PORT", 6333))
QDRANT_COLLECTIONS = _CFG.get("qdrant", {}).get("collections", ["bone_atlas", "bone_annotations"])

CVAT_HOST = _get("cvat", "host", "CVAT_HOST", "10.0.0.59")
CVAT_PORT = int(_get("cvat", "port", "CVAT_PORT", 8080))
CVAT_USERNAME = _get("cvat", "username", "CVAT_USERNAME", "admin")
CVAT_PASSWORD = _get("cvat", "password", "CVAT_PASSWORD", "")

ML_COMPUTE_HOST = _get("ml_compute", "host", "ML_COMPUTE_HOST", "10.0.0.44")
ML_COMPUTE_PORT = int(_get("ml_compute", "port", "ML_COMPUTE_PORT", 9469))

BONE_ML_HOST = _get("bone_ml", "host", "BONE_ML_HOST", "10.0.0.59")
BONE_ML_PORT = int(_get("bone_ml", "port", "BONE_ML_PORT", 9463))

DATASET_PACS_HOST = _get("dataset_pacs", "host", "DATASET_PACS_HOST", "10.0.0.90")
DATASET_PACS_PORT = int(_get("dataset_pacs", "port", "DATASET_PACS_PORT", 8042))
DATASET_PACS_USER = _get("dataset_pacs", "user", "DATASET_PACS_USER", "")
DATASET_PACS_PASSWORD = _get("dataset_pacs", "password", "DATASET_PACS_PASSWORD", "")

REDIS_HOST = _get("redis", "host", "REDIS_HOST", "10.0.0.44")
REDIS_PORT = int(_get("redis", "port", "REDIS_PORT", 6379))
REDIS_DB = int(_get("redis", "db", "REDIS_DB", 0))

VAULT_URL = _get("vault", "url", "ONYX_VAULT_URL", "http://10.0.0.44:8050")
VAULT_TOKEN = os.getenv("ONYX_VAULT_TOKEN", "")

IMAGING_BUNDLED_DIR = _get(
    "imaging", "bundled_dir", "IMAGING_BUNDLED_DIR", "/opt/onyx/imaging-sdk/pipelines"
)
IMAGING_USER_DIR = _get(
    "imaging", "user_dir", "IMAGING_USER_DIR", "/opt/onyx/imaging-sdk/pipelines/users"
)
IMAGING_DEFAULT_TREATMENT = _get(
    "imaging", "default_treatment", "IMAGING_DEFAULT_TREATMENT", "os_nu_medsam_user"
)
IMAGING_DEFAULT_TREATMENT_LABEL = _get(
    "imaging",
    "default_treatment_label",
    "IMAGING_DEFAULT_TREATMENT_LABEL",
    "Os nu — MedSAM [USER]",
)
IMAGING_DEFAULT_PRE_ANNOTATE = bool(
    _CFG.get("imaging", {}).get("default_pre_annotate", False)
)
DASHBOARD_TITLE = _get("dashboard", "title", "DASHBOARD_TITLE", "Gestion des Annotations")
DASHBOARD_POLL_MS = int(_get("dashboard", "poll_interval_ms", "DASHBOARD_POLL_MS", 5000))


# ===== CHECK FUNCTIONS =====


async def check_bonestore() -> bool:
    """Vérifier que BoneStore NFS est montée et accessible."""
    try:
        path = Path(BONESTORE_ROOT)
        if not path.exists() or not path.is_dir():
            logger.error("BoneStore not mounted at %s", BONESTORE_ROOT)
            return False
        list(path.iterdir())
        logger.info("✓ BoneStore mounted: %s", BONESTORE_ROOT)
        return True
    except Exception as e:
        logger.error("BoneStore check failed: %s", e)
        return False


async def check_postgres() -> bool:
    """Vérifier la connexion à PostgreSQL."""
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
    """Vérifier la connexion à Qdrant."""
    try:
        from qdrant_client import QdrantClient

        client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT, timeout=5)
        collections = [c.name for c in client.get_collections().collections]
        logger.info("✓ Qdrant connected: %s:%d (%d collections)", QDRANT_HOST, QDRANT_PORT, len(collections))
        return True
    except Exception as e:
        logger.error("Qdrant check failed: %s", e)
        return False


async def check_cvat() -> bool:
    """Vérifier la connexion à CVAT API."""
    try:
        import httpx

        url = f"http://{CVAT_HOST}:{CVAT_PORT}/api/server/about"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5.0)
            if response.status_code in (200, 401, 403):
                logger.info("✓ CVAT API accessible: %s:%d", CVAT_HOST, CVAT_PORT)
                return True
            logger.error("CVAT API check failed: status %d", response.status_code)
            return False
    except Exception as e:
        logger.error("CVAT check failed: %s", e)
        return False


async def check_ml_compute() -> bool:
    """Vérifier la connexion à ml-compute Ray API."""
    try:
        import httpx

        url = f"http://{ML_COMPUTE_HOST}:{ML_COMPUTE_PORT}/health"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5.0)
            if response.status_code == 200:
                logger.info("✓ ml-compute accessible: %s:%d", ML_COMPUTE_HOST, ML_COMPUTE_PORT)
                return True
            logger.warning("ml-compute health check failed: status %d", response.status_code)
            return False
    except Exception as e:
        logger.error("ml-compute check failed: %s", e)
        return False


async def check_redis() -> bool:
    """Vérifier la connexion à Redis."""
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
    """Charger un secret depuis OnyxVault."""
    if not VAULT_TOKEN:
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
            return None
    except Exception as e:
        logger.error("Vault lookup failed for %s: %s", key, e)
        return None


def get_postgres_config() -> dict[str, Any]:
    """Obtenir la configuration PostgreSQL complète."""
    return {
        "host": POSTGRES_HOST,
        "port": POSTGRES_PORT,
        "user": POSTGRES_USER,
        "dbname": POSTGRES_DBNAME,
        "password": POSTGRES_PASSWORD,
        "schema": POSTGRES_SCHEMA,
    }


def get_qdrant_config() -> dict[str, Any]:
    """Obtenir la configuration Qdrant complète."""
    return {"host": QDRANT_HOST, "port": QDRANT_PORT, "collections": QDRANT_COLLECTIONS}


def get_cvat_config() -> dict[str, Any]:
    """Obtenir la configuration CVAT complète."""
    return {"host": CVAT_HOST, "port": CVAT_PORT, "username": CVAT_USERNAME, "password": CVAT_PASSWORD}


def get_ml_compute_config() -> dict[str, Any]:
    """Obtenir la configuration ml-compute."""
    return {"host": ML_COMPUTE_HOST, "port": ML_COMPUTE_PORT}


def get_redis_config() -> dict[str, Any]:
    """Obtenir la configuration Redis."""
    return {"host": REDIS_HOST, "port": REDIS_PORT, "db": REDIS_DB}


def get_bone_ml_config() -> dict[str, Any]:
    """Obtenir la configuration bone-ml."""
    return {"host": BONE_ML_HOST, "port": BONE_ML_PORT, "base_url": f"http://{BONE_ML_HOST}:{BONE_ML_PORT}"}


def get_imaging_config() -> dict[str, Any]:
    """Obtenir la configuration imaging treatment (imaging-sdk)."""
    return {
        "bundled_dir": IMAGING_BUNDLED_DIR,
        "user_dir": IMAGING_USER_DIR,
        "default_treatment": IMAGING_DEFAULT_TREATMENT,
        "default_treatment_label": IMAGING_DEFAULT_TREATMENT_LABEL,
        "default_pre_annotate": IMAGING_DEFAULT_PRE_ANNOTATE,
    }


def get_dashboard_config() -> dict[str, Any]:
    """Obtenir la configuration dashboard UI."""
    return {
        "title": DASHBOARD_TITLE,
        "poll_interval_ms": DASHBOARD_POLL_MS,
    }


def get_dataset_pacs_config() -> dict[str, Any]:
    """Obtenir la configuration PACS dataset training."""
    return {
        "host": DATASET_PACS_HOST,
        "port": DATASET_PACS_PORT,
        "user": DATASET_PACS_USER,
        "password": DATASET_PACS_PASSWORD,
        "base_url": f"http://{DATASET_PACS_HOST}:{DATASET_PACS_PORT}",
    }


async def load_credentials_from_vault() -> None:
    """Load credentials from Vault for services not configured in YAML."""
    global CVAT_PASSWORD, DATASET_PACS_USER, DATASET_PACS_PASSWORD
    if not CVAT_PASSWORD:
        cvat_pass = await load_vault_secret("cvat_admin_password")
        if cvat_pass:
            CVAT_PASSWORD = cvat_pass
            logger.info("CVAT password loaded from Vault")
    if not DATASET_PACS_USER:
        user = await load_vault_secret("orthanc_training_user")
        if user:
            DATASET_PACS_USER = user
    if not DATASET_PACS_PASSWORD:
        password = await load_vault_secret("orthanc_training_password")
        if password:
            DATASET_PACS_PASSWORD = password
    if DATASET_PACS_USER and DATASET_PACS_PASSWORD:
        logger.info("PACS credentials loaded from Vault")


async def check_all_dependencies() -> dict[str, bool]:
    """Vérifier toutes les dépendances."""
    return {
        "bonestore": await check_bonestore(),
        "postgres": await check_postgres(),
        "qdrant": await check_qdrant(),
        "cvat": await check_cvat(),
        "ml_compute": await check_ml_compute(),
        "redis": await check_redis(),
    }
