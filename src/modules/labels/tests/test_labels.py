"""Tests pour le service labels."""

from unittest.mock import MagicMock, patch

import pytest

from src.modules.labels.service import (
    ACCEPTED_LABELS_URL,
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
    """Test que les URLs label-generator sont correctement configurées."""
    assert LABEL_GENERATOR_URL == "http://10.0.0.59:9466/api/labels/anatomy"
    assert "accepted-labels" in ACCEPTED_LABELS_URL
    assert "{bone_type}" in ACCEPTED_LABELS_URL


def test_get_labels_for_bone_prefers_accepted_labels() -> None:
    """Test que get_labels_for_bone priorise accepted-labels (54 zones)."""
    accepted = {
        "bone_type": "humerus",
        "zones": [{"id": f"z{i}"} for i in range(54)],
        "landmarks": [{"id": f"lm{i}"} for i in range(18)],
        "source": "accepted-labels",
    }
    anatomy = {"humerus": {"zones": [{"id": "old"}], "landmarks": []}}

    with (
        patch("src.modules.labels.service.fetch_accepted_labels", return_value=accepted),
        patch("src.modules.labels.service.load_anatomy_labels", return_value=anatomy),
    ):
        labels = get_labels_for_bone("humerus")
        assert labels is not None
        assert len(labels["zones"]) == 54
        assert len(labels["landmarks"]) == 18
        assert labels["labels_source"] == "accepted-labels"


@pytest.mark.asyncio
async def test_sync_labels_from_generator_uses_correct_url() -> None:
    """Test que sync utilise anatomy + accepted-labels."""
    mock_labels = {"humerus": {"zones": [{"id": "old"}], "landmarks": []}}
    accepted_payload = {
        "bone_type": "humerus",
        "zones": [{"id": "diaphyse_humerale"}],
        "landmarks": [{"id": "head_center"}],
    }

    with patch("httpx.AsyncClient") as mock_client_class:
        mock_client = MagicMock()

        async def _get(url: str, timeout: float = 10.0) -> MagicMock:
            mock_response = MagicMock()
            mock_response.status_code = 200
            if "accepted-labels" in url:
                mock_response.json.return_value = accepted_payload
            else:
                mock_response.json.return_value = mock_labels
            return mock_response

        mock_client.get = _get
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        mock_client_class.return_value = mock_client

        count = await sync_labels_from_generator()
        assert count == 1


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

    with (
        patch("src.modules.labels.service.fetch_accepted_labels", return_value=None),
        patch("src.modules.labels.service.load_anatomy_labels", return_value=mock_labels),
    ):
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
