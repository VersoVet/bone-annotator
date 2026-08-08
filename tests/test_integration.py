"""Integration tests pour bone-annotator.

Tests du flux complet: BoneStore → configuration → monitoring.
"""

import pytest


@pytest.mark.asyncio
async def test_service_startup() -> None:
    """Test que le service démarre sans erreur."""
    from src.main import app

    assert app is not None
    assert app.title == "bone-annotator"


@pytest.mark.asyncio
async def test_health_endpoint() -> None:
    """Test l'endpoint de health check."""
    from fastapi.testclient import TestClient
    from src.main import app

    client = TestClient(app)
    response = client.get("/health")

    # Health endpoint returns 200 (healthy/degraded) or 503 (no dependencies)
    assert response.status_code in (200, 503)
    if response.status_code == 200:
        data = response.json()
        assert "status" in data
        assert "version" in data
        assert "dependencies" in data


@pytest.mark.asyncio
async def test_api_config_endpoint() -> None:
    """Test l'endpoint de configuration."""
    from fastapi.testclient import TestClient
    from src.main import app

    client = TestClient(app)
    response = client.get("/api/config")

    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "bone-annotator"
    assert "bonestore" in data
    assert "postgres" in data
    assert "qdrant" in data


@pytest.mark.asyncio
async def test_api_dependencies_endpoint() -> None:
    """Test l'endpoint de dépendances."""
    from fastapi.testclient import TestClient
    from src.main import app

    client = TestClient(app)
    response = client.get("/api/dependencies")

    assert response.status_code == 200
    data = response.json()
    assert "dependencies" in data
    assert "critical_ready" in data
    assert "overall_health" in data


@pytest.mark.asyncio
async def test_training_status_endpoint() -> None:
    """Test l'endpoint de status training."""
    from fastapi.testclient import TestClient
    from src.main import app

    client = TestClient(app)
    response = client.get("/api/training/status")

    assert response.status_code == 200
    data = response.json()
    assert "jobs" in data
    assert isinstance(data["jobs"], list)


@pytest.mark.asyncio
async def test_annotations_endpoint() -> None:
    """Test l'endpoint d'annotations."""
    from fastapi.testclient import TestClient
    from src.main import app

    client = TestClient(app)
    response = client.get("/api/annotations?limit=10")

    assert response.status_code == 200
    data = response.json()
    assert "annotations" in data
    assert "total" in data
    assert data["limit"] == 10


def test_config_loads() -> None:
    """Test que la configuration charge sans erreur."""
    from src import config

    assert config.BONESTORE_ROOT is not None
    assert config.POSTGRES_HOST is not None
    assert config.QDRANT_HOST is not None


def test_labels_module() -> None:
    """Test que le module labels charge sans erreur."""
    from src.modules.labels import service

    assert service is not None
    assert hasattr(service, "load_anatomy_labels")
    assert hasattr(service, "get_zones")
    assert hasattr(service, "validate_zone_annotation")
