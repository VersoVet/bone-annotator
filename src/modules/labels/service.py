"""Label service for bone anatomy annotations.

Manages anatomical labels, caching, and integration with label-generator.
Provides hierarchical label structures for zone, landmark, and lesion annotations.
Uses accepted-labels (zones/landmarks GOLD) as primary source, anatomy as fallback.
"""

import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

# Configuration
LABEL_GENERATOR_URL = "http://10.0.0.59:9466/api/labels/anatomy"
ACCEPTED_LABELS_URL = "http://10.0.0.59:9466/labels/api/accepted-labels/{bone_type}"
CACHE_PATH = Path(__file__).resolve().parent.parent.parent.parent / "config" / "anatomy_zones.json"

# Cache local pour les labels anatomiques
_label_cache: dict[str, Any] = {}
_cache_loaded: bool = False
_accepted_cache: dict[str, dict[str, Any]] = {}


def load_anatomy_labels(config_path: str | Path | None = None) -> dict[str, Any]:
    """Charger les labels anatomiques depuis label-generator API ou cache JSON.

    Stratégie:
    1. Tenter de charger depuis API label-generator anatomy
    2. Enrichir chaque os avec accepted-labels (source GOLD zones/landmarks)
    3. Si API répond, sauvegarder en cache JSON local
    4. Si API échoue, utiliser le cache JSON local

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
        _enrich_with_accepted_labels(labels)
        _label_cache = labels
        _cache_loaded = True
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
        logger.warning("Anatomy cache not found at %s", config_path)
        return {}
    except Exception as e:
        logger.error("Failed to load anatomy labels from cache: %s", e)
        return {}


def _load_from_api() -> dict[str, Any] | None:
    """Charger les labels depuis label-generator API anatomy.

    Returns:
        Dict avec labels ou None si échoue.
    """
    try:
        import urllib.request

        with urllib.request.urlopen(LABEL_GENERATOR_URL, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                logger.info("Anatomy labels loaded from API: %s", LABEL_GENERATOR_URL)
                return data
            logger.warning("API returned status %d", response.status)
            return None
    except Exception as e:
        logger.warning("Failed to load labels from API (%s): %s", LABEL_GENERATOR_URL, e)
        return None


def fetch_accepted_labels(bone_type: str, *, use_cache: bool = True) -> dict[str, Any] | None:
    """Fetch accepted zones/landmarks for one bone from label-generator.

    Args:
        bone_type: Bone type (e.g. humerus).
        use_cache: Reuse in-memory accepted cache when True.

    Returns:
        Dict with zones and landmarks, or None if unavailable.
    """
    key = bone_type.strip().lower()
    if not key:
        return None
    if use_cache and key in _accepted_cache:
        return _accepted_cache[key]

    url = ACCEPTED_LABELS_URL.format(bone_type=key)
    try:
        import urllib.request

        with urllib.request.urlopen(url, timeout=15) as response:
            if response.status != 200:
                logger.warning("Accepted-labels returned status %d for %s", response.status, key)
                return None
            data = json.loads(response.read().decode())
    except Exception as e:
        logger.warning("Failed to load accepted-labels for %s (%s): %s", key, url, e)
        return None

    result = {
        "bone_type": data.get("bone_type", key),
        "zones": data.get("zones", []) or [],
        "landmarks": data.get("landmarks", []) or [],
        "source": "accepted-labels",
    }
    _accepted_cache[key] = result
    logger.info(
        "Accepted labels loaded for %s: %d zones + %d landmarks",
        key,
        len(result["zones"]),
        len(result["landmarks"]),
    )
    return result


def _enrich_with_accepted_labels(labels: dict[str, Any]) -> None:
    """Overwrite zones/landmarks from accepted-labels when available.

    Args:
        labels: Anatomy dict keyed by bone type (mutated in place).
    """
    for bone_type in list(labels.keys()):
        accepted = fetch_accepted_labels(str(bone_type))
        if not accepted:
            continue
        entry = labels.get(bone_type)
        if not isinstance(entry, dict):
            entry = {}
            labels[bone_type] = entry
        if accepted.get("zones"):
            entry["zones"] = accepted["zones"]
        if accepted.get("landmarks"):
            entry["landmarks"] = accepted["landmarks"]
        entry["labels_source"] = "accepted-labels"


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

    Prefers live accepted-labels (zones = seg classes) then anatomy cache.

    Args:
        bone_type: Type d'os (humerus, radius, etc.).

    Returns:
        Dict avec zones, landmarks, lesions ou None si non trouvé.
    """
    key = bone_type.strip().lower()
    accepted = fetch_accepted_labels(key)
    base = load_anatomy_labels().get(key)
    if accepted and (accepted.get("zones") or accepted.get("landmarks")):
        merged: dict[str, Any] = dict(base) if isinstance(base, dict) else {}
        merged["zones"] = accepted.get("zones", [])
        merged["landmarks"] = accepted.get("landmarks", [])
        merged["labels_source"] = "accepted-labels"
        return merged
    return base if isinstance(base, dict) else None


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
    """Valider qu'une zone est applicable pour un os et région.

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
        "labels_source": labels.get("labels_source", "anatomy"),
    }


async def sync_labels_from_generator() -> int:
    """Synchroniser les labels depuis label-generator skill.

    Charge anatomy puis écrase zones/landmarks avec accepted-labels.

    Returns:
        Nombre de bone types synchronisés.
    """
    global _label_cache, _cache_loaded, _accepted_cache

    try:
        import httpx

        async with httpx.AsyncClient() as client:
            response = await client.get(LABEL_GENERATOR_URL, timeout=10.0)
            if response.status_code != 200:
                logger.warning("label-generator returned status %d", response.status_code)
                return 0
            labels = response.json()
            if not isinstance(labels, dict):
                logger.warning("Unexpected anatomy payload type: %s", type(labels))
                return 0

            _accepted_cache.clear()
            for bone_type in list(labels.keys()):
                url = ACCEPTED_LABELS_URL.format(bone_type=str(bone_type).lower())
                try:
                    acc_resp = await client.get(url, timeout=15.0)
                    if acc_resp.status_code != 200:
                        continue
                    data = acc_resp.json()
                    entry = labels.get(bone_type) if isinstance(labels.get(bone_type), dict) else {}
                    if not isinstance(entry, dict):
                        entry = {}
                        labels[bone_type] = entry
                    zones = data.get("zones") or []
                    landmarks = data.get("landmarks") or []
                    if zones:
                        entry["zones"] = zones
                    if landmarks:
                        entry["landmarks"] = landmarks
                    entry["labels_source"] = "accepted-labels"
                    _accepted_cache[str(bone_type).lower()] = {
                        "bone_type": str(bone_type).lower(),
                        "zones": zones,
                        "landmarks": landmarks,
                        "source": "accepted-labels",
                    }
                except Exception as e:
                    logger.warning("Accepted-labels sync failed for %s: %s", bone_type, e)

            _label_cache = labels
            _cache_loaded = True
            _save_cache(labels)
            logger.info("Labels synchronized from label-generator: %d types", len(labels))
            return len(labels)
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
        "accepted_labels_url": ACCEPTED_LABELS_URL,
    }
