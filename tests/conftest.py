"""Fixtures pytest pour bone-annotator."""

import pytest


@pytest.fixture
def app():
    """FastAPI app instance pour tests."""
    from src.main import app
    return app


@pytest.fixture
def client(app):
    """Test client FastAPI."""
    from fastapi.testclient import TestClient
    return TestClient(app)
