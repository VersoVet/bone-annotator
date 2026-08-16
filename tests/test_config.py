"""Tests for centralized configuration."""


def test_postgres_config() -> None:
    """Test get_postgres_config returns expected keys."""
    from src.config import get_postgres_config

    cfg = get_postgres_config()
    assert "host" in cfg
    assert "port" in cfg
    assert "user" in cfg
    assert "dbname" in cfg


def test_cvat_config() -> None:
    """Test get_cvat_config returns expected keys."""
    from src.config import get_cvat_config

    cfg = get_cvat_config()
    assert "host" in cfg
    assert "port" in cfg
    assert "username" in cfg


def test_bone_ml_config() -> None:
    """Test get_bone_ml_config returns expected keys."""
    from src.config import get_bone_ml_config

    cfg = get_bone_ml_config()
    assert "host" in cfg
    assert "port" in cfg
    assert "base_url" in cfg
    assert "10.0.0.86" in cfg["base_url"]


def test_dataset_pacs_config() -> None:
    """Test get_dataset_pacs_config returns PACS info."""
    from src.config import get_dataset_pacs_config

    cfg = get_dataset_pacs_config()
    assert "host" in cfg
    assert "port" in cfg
    assert "base_url" in cfg


def test_redis_config() -> None:
    """Test get_redis_config returns expected keys."""
    from src.config import get_redis_config

    cfg = get_redis_config()
    assert "host" in cfg
    assert "port" in cfg
    assert "db" in cfg


def test_qdrant_config() -> None:
    """Test get_qdrant_config returns expected keys."""
    from src.config import get_qdrant_config

    cfg = get_qdrant_config()
    assert "host" in cfg
    assert "collections" in cfg
    assert isinstance(cfg["collections"], list)
