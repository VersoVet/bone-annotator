"""Label service for bone anatomy annotations.

Manages anatomical labels, caching, and integration with label-generator.
Provides hierarchical label structures for zone, landmark, and lesion annotations.
Uses label-generator API as primary source with local JSON cache fallback.
"""

import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

# Configuration
LABEL_GENERATOR_URL = "http://10.0.0.59:9466/api/labels/anatomy"
CACHE_PATH = Path(__file__).resolve().parent.parent.parent.parent / "config" / "anatomy_zones.json"

# Cache local pour les labels anatomiques
_label_cache: dict[str, Any] = {}
_cache_loaded: bool = False


def load_anatomy_labels(config_path: str | Path | None = None) -> dict[str, Any]:
    """Charger les labels anatomiques depuis label-generator API ou cache JSON.

    Stratégie:
    1. Tenter de charger depuis API label-generator (http://10.0.0.59:9466/api/labels/anatomy)
    2. Si API répond, sauvegarder en cache JSON local
    3. Si API échoue, utiliser le cache JSON local

    Args:
        config_path: Chemin vers le fichier de configuration anatomique (fallback).
                    Si None, utilise config/anatomy_zones.json par défaut.

    Returns:
        Dict avec structure {bone_type: {zones, landmarks, morphometric_criteria, ...}}.
    """
    global _label_cache, _cache_loaded

    if _cache_loaded and _label_cache:
        return _label_cache

    # Étape 1: Tenter de charger depuis label-generator API
    labels = _load_from_api()
    if labels:
        _label_cache = labels
        _cache_loaded = True
        # Sauvegarder en cache pour fallback
        _save_cache(labels, config_path)
        return _label_cache

    # Étape 2: Fallback sur cache JSON local
    if config_path is None:
        config_path = CACHE_PATH
    else:
        config_path = Path(config_path)

    try:
        if config_path.exists():
            with config_path.open() as f:
                _label_cache = json.load(f)
                _cache_loaded = True
                logger.info("Anatomy labels loaded from cache: %s", config_path)
                return _label_cache
        else:
            logger.warning("Anatomy cache not found at %s", config_path)
            return {}
    except Exception as e:
        logger.error("Failed to load anatomy labels from cache: %s", e)
        return {}


def _load_from_api() -> dict[str, Any] | None:
    """Charger les labels depuis label-generator API.

    Returns:
        Dict avec labels ou None si échoue.
    """
    try:
        # Utiliser synchrone pour compatibilité
        import urllib.request

        with urllib.request.urlopen(LABEL_GENERATOR_URL, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                logger.info("Anatomy labels loaded from API: %s", LABEL_GENERATOR_URL)
                return data
            else:
                logger.warning("API returned status %d", response.status)
                return None
    except Exception as e:
        logger.warning("Failed to load labels from API (%s): %s", LABEL_GENERATOR_URL, e)
        return None


def _save_cache(labels: dict[str, Any], config_path: str | Path | None = None) -> None:
    """Sauvegarder les labels en cache JSON local.

    Args:
        labels: Dict de labels à sauvegarder.
        config_path: Chemin de sauvegarde (utilise CACHE_PATH par défaut).
    """
    if config_path is None:
        config_path = CACHE_PATH
    else:
        config_path = Path(config_path)

    try:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with config_path.open("w") as f:
            json.dump(labels, f, indent=2, default=str)
        logger.info("Labels cached to %s", config_path)
    except Exception as e:
        logger.warning("Failed to save labels cache: %s", e)


def get_labels_for_bone(bone_type: str) -> dict[str, Any] | None:
    """Obtenir les labels pour un type d'os spécifique.

    Args:
        bone_type: Type d'os (humerus, radius, etc.).

    Returns:
        Dict avec zones, landmarks, lesions ou None si non trouvé.
    """
    labels = load_anatomy_labels()
    return labels.get(bone_type)


def get_zones(bone_type: str, region: str = "") -> list[dict[str, Any]]:
    """Obtenir les zones anatomiques pour un os et région.

    Args:
        bone_type: Type d'os.
        region: Région (proximal, distal, entire, bilateral). Vide = tous.

    Returns:
        Liste des zones applicables.
    """
    labels = get_labels_for_bone(bone_type)
    if not labels:
        return []

    zones = labels.get("zones", [])
    if not region or region == "entire":
        return zones

    # Filtrer par région si applicable
    filtered = [z for z in zones if z.get("region") in ("entire", region)]
    return filtered


def get_landmarks(bone_type: str) -> list[dict[str, Any]]:
    """Obtenir les points de repère anatomiques.

    Args:
        bone_type: Type d'os.

    Returns:
        Liste des landmarks.
    """
    labels = get_labels_for_bone(bone_type)
    if not labels:
        return []
    return labels.get("landmarks", [])


def get_lesion_criteria(bone_type: str) -> dict[str, Any]:
    """Obtenir les critères de lésion pour un os.

    Args:
        bone_type: Type d'os.

    Returns:
        Dict avec types de lésion et critères.
    """
    labels = get_labels_for_bone(bone_type)
    if not labels:
        return {}
    return labels.get("lesion_criteria", {})


def validate_zone_annotation(
    bone_type: str,
    zone_id: str,
    region: str = "",
) -> bool:
    """Valider qu'une zone est applicale pour un os et région.

    Args:
        bone_type: Type d'os.
        zone_id: ID de la zone.
        region: Région.

    Returns:
        True si la zone est valide pour cette combinaison.
    """
    zones = get_zones(bone_type, region)
    return any(z.get("id") == zone_id for z in zones)


def validate_landmark_annotation(bone_type: str, landmark_id: str) -> bool:
    """Valider qu'un landmark est applicable pour un os.

    Args:
        bone_type: Type d'os.
        landmark_id: ID du landmark.

    Returns:
        True si le landmark est valide.
    """
    landmarks = get_landmarks(bone_type)
    return any(lm.get("id") == landmark_id for lm in landmarks)


def get_label_hierarchy(bone_type: str) -> dict[str, Any]:
    """Obtenir la hiérarchie complète des labels pour un os.

    Args:
        bone_type: Type d'os.

    Returns:
        Dict avec structure hiérarchique de tous les labels.
    """
    labels = get_labels_for_bone(bone_type)
    if not labels:
        return {"bone_type": bone_type, "error": "not_found"}

    return {
        "bone_type": bone_type,
        "zones": labels.get("zones", []),
        "landmarks": labels.get("landmarks", []),
        "lesion_criteria": labels.get("lesion_criteria", {}),
        "regions": labels.get("regions", []),
    }


async def sync_labels_from_generator() -> int:
    """Synchroniser les labels depuis label-generator skill.

    Récupère les labels anatomiques du service label-generator
    et met à jour le cache local.

    Returns:
        Nombre de labels synchronisés.
    """
    try:
        import httpx

        async with httpx.AsyncClient() as client:
            response = await client.get(
                LABEL_GENERATOR_URL,
                timeout=10.0,
            )
            if response.status_code == 200:
                labels = response.json()
                _label_cache.update(labels)
                _cache_loaded = True
                logger.info("Labels synchronized from label-generator: %d types", len(labels))
                return len(labels)
            else:
                logger.warning("label-generator returned status %d", response.status_code)
                return 0
    except Exception as e:
        logger.error("Failed to sync labels from generator: %s", e)
        return 0


async def get_status() -> dict[str, Any]:
    """Obtenir l'état du service labels.

    Returns:
        Statut du cache et des labels chargés.
    """
    labels = load_anatomy_labels()
    return {
        "service": "labels",
        "cache_loaded": _cache_loaded,
        "bone_types_available": list(labels.keys()),
        "total_zones": sum(len(labels.get(bt, {}).get("zones", [])) for bt in labels),
        "total_landmarks": sum(len(labels.get(bt, {}).get("landmarks", [])) for bt in labels),
    }
