"""Tests for ingestion routes imports."""


def test_ingestion_routes_import() -> None:
    """Test ingestion routes module import."""
    from src.modules.ingestion.routes import router  # noqa: F401

    assert router is not None


def test_ingestion_registry_import() -> None:
    """Test IngestionRegistry import."""
    from src.modules.ingestion.registry import IngestionRegistry  # noqa: F401

    assert IngestionRegistry is not None


def test_ingestion_status_enum() -> None:
    """Test IngestionStatus has expected members."""
    from src.modules.ingestion.registry import IngestionStatus

    members = [s.value for s in IngestionStatus]
    assert "discovered" in members
    assert "completed" in members
    assert "failed" in members
