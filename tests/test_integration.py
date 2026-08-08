"""Tests intégration bone-annotator."""


def test_root(client):
    """Test endpoint racine."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "bone-annotator"


def test_health(client):
    """Test health check."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_ready(client):
    """Test readiness check."""
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"


def test_api_status(client):
    """Test statut API."""
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "bone-annotator"
    assert "dependencies" in data
