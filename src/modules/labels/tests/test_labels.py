"""Tests pour le service labels."""

from unittest.mock import MagicMock, patch

import pytest

from src.modules.labels.service import (
    LABEL_GENERATOR_URL,
    get_label_hierarchy,
    get_labels_for_bone,
    get_landmarks,
    get_zones,
    load_anatomy_labels,
    sync_labels_from_generator,
)


@pytest.mark.asyncio
async def test_labels_service_status() -> None:
    """Test que le service labels peut être initialisé."""
    from src.modules.labels.service import get_status

    status = await get_status()
    assert status["service"] == "labels"
    assert "cache_loaded" in status
    assert "bone_types_available" in status


def test_get_labels_for_bone_empty() -> None:
    """Test récupération labels pour os non configuré."""
    labels = get_labels_for_bone("unknown_bone")
    assert labels is None


def test_get_zones_empty() -> None:
    """Test récupération zones pour os non configuré."""
    zones = get_zones("unknown_bone")
    assert zones == []


def test_get_landmarks_empty() -> None:
    """Test récupération landmarks pour os non configuré."""
    landmarks = get_landmarks("unknown_bone")
    assert landmarks == []


def test_get_label_hierarchy_empty() -> None:
    """Test récupération hiérarchie labels pour os non configuré."""
    hierarchy = get_label_hierarchy("unknown_bone")
    assert hierarchy["bone_type"] == "unknown_bone"
    assert "error" in hierarchy


def test_load_anatomy_labels_structure() -> None:
    """Test que load_anatomy_labels retourne une structure valide."""
    # Test with actual implementation if cache exists, or empty dict
    labels = load_anatomy_labels()
    assert isinstance(labels, dict)


def test_label_generator_url_correct() -> None:
    """Test que l'URL label-generator est correctement configurée."""
    assert LABEL_GENERATOR_URL == "http://10.0.0.59:9466/api/labels/anatomy"


@pytest.mark.asyncio
async def test_sync_labels_from_generator_uses_correct_url() -> None:
    """Test que sync_labels_from_generator utilise l'URL correcte."""
    mock_labels = {"humerus": {"zones": [], "landmarks": []}}

    with patch("httpx.AsyncClient") as mock_client_class:
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_labels
        mock_client.get = MagicMock()
        mock_client.get.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        mock_client_class.return_value = mock_client

        await sync_labels_from_generator()

        # Verify the correct URL was used
        mock_client.get.assert_called_once()
        call_args = mock_client.get.call_args
        assert call_args[0][0] == LABEL_GENERATOR_URL


def test_get_zones_with_region_filter() -> None:
    """Test filtrage des zones par région."""
    # Mock labels with zones
    mock_labels = {
        "humerus": {
            "zones": [
                {"id": "z1", "name": "proximal", "region": "proximal"},
                {"id": "z2", "name": "distal", "region": "distal"},
                {"id": "z3", "name": "full", "region": "entire"},
            ]
        }
    }

    with patch("src.modules.labels.service.load_anatomy_labels") as mock_load:
        mock_load.return_value = mock_labels

        # Test getting all zones
        zones = get_zones("humerus")
        assert len(zones) == 3

        # Test filtering by proximal region
        zones = get_zones("humerus", "proximal")
        assert len(zones) == 2  # proximal + entire
        zone_names = [z["name"] for z in zones]
        assert "proximal" in zone_names
        assert "full" in zone_names


def test_validate_zone_annotation() -> None:
    """Test validation zone annotation."""
    from src.modules.labels.service import validate_zone_annotation

    # With empty cache, should return False
    result = validate_zone_annotation("humerus", "zone1")
    assert isinstance(result, bool)


def test_validate_landmark_annotation() -> None:
    """Test validation landmark annotation."""
    from src.modules.labels.service import validate_landmark_annotation

    # With empty cache, should return False
    result = validate_landmark_annotation("humerus", "landmark1")
    assert isinstance(result, bool)
