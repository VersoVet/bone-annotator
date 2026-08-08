"""Tests pour le service labels."""

import pytest

from src.modules.labels.service import (
    get_label_hierarchy,
    get_labels_for_bone,
    get_landmarks,
    get_zones,
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
