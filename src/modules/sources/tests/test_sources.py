"""Tests for image sources module."""

from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
import yaml


class TestSourceConfig:
    """Tests for YAML source configuration loading."""

    def test_load_valid_config(self) -> None:
        """Test loading a valid sources.yaml."""
        from src.modules.sources.service import SourceConfig

        with TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "sources.yaml"
            config_path.write_text(
                yaml.dump(
                    {
                        "sources": {
                            "test": {"type": "nfs", "enabled": True, "root": "/tmp/test"},
                        },
                        "dataset_pacs": {"host": "10.0.0.90", "port": 8042},
                        "dataset_storage_fallback": {"root": "/tmp/fallback"},
                    }
                )
            )
            cfg = SourceConfig(config_path)
            assert "test" in cfg.sources
            assert cfg.sources["test"]["type"] == "nfs"
            assert cfg.dataset_pacs["host"] == "10.0.0.90"
            assert cfg.dataset_storage_fallback == "/tmp/fallback"

    def test_missing_config(self) -> None:
        """Test loading with missing config file."""
        from src.modules.sources.service import SourceConfig

        cfg = SourceConfig(Path("/nonexistent/sources.yaml"))
        assert cfg.sources == {}


class TestSourceService:
    """Tests for SourceService."""

    def test_list_sources(self) -> None:
        """Test listing enabled sources."""
        from src.modules.sources.service import SourceConfig, SourceService

        with TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "sources.yaml"
            config_path.write_text(
                yaml.dump(
                    {
                        "sources": {
                            "enabled_src": {"type": "nfs", "enabled": True, "root": "/tmp"},
                            "disabled_src": {"type": "nfs", "enabled": False, "root": "/tmp"},
                        },
                    }
                )
            )
            cfg = SourceConfig(config_path)
            svc = SourceService(cfg)
            sources = svc.list_sources()
            assert len(sources) == 1
            assert sources[0]["name"] == "enabled_src"

    def test_list_acquisitions_unknown_source(self) -> None:
        """Test listing from unknown source raises ValueError."""
        from src.modules.sources.service import SourceConfig, SourceService

        cfg = SourceConfig(Path("/nonexistent"))
        svc = SourceService(cfg)
        with pytest.raises(ValueError, match="not found"):
            svc.list_acquisitions("nonexistent")
