"""Tests for dataset preparation module."""

from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np


class TestPngSave:
    """Tests for PNG 16-bit saving."""

    def test_save_uint16_png(self) -> None:
        """Test saving uint16 array as PNG."""
        from src.modules.preparation.service import _save_png_16bit

        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "test.png"
            image = np.random.randint(0, 65535, (64, 64), dtype=np.uint16)
            _save_png_16bit(image, path)
            assert path.exists()
            assert path.stat().st_size > 0

    def test_save_float_png(self) -> None:
        """Test saving float32 array as PNG (converted to uint16)."""
        from src.modules.preparation.service import _save_png_16bit

        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "test.png"
            image = np.random.rand(64, 64).astype(np.float32)
            _save_png_16bit(image, path)
            assert path.exists()


class TestPreparedDataset:
    """Tests for PreparedDataset model."""

    def test_to_dict(self) -> None:
        """Test serialization to dict."""
        from src.modules.preparation.service import PreparedDataset

        ds = PreparedDataset(
            dataset_id="test_123",
            path=Path("/tmp/test"),
            frame_count=10,
            pipeline_preset="replay_membre",
            pipeline_config=[{"name": "clahe"}],
            bone_type="humerus",
            acquisition_id="acq_001",
        )
        d = ds.to_dict()
        assert d["dataset_id"] == "test_123"
        assert d["frame_count"] == 10
        assert d["bone_type"] == "humerus"


class TestDatasetPreparationService:
    """Tests for DatasetPreparationService."""

    def test_list_datasets_empty(self) -> None:
        """Test listing datasets on empty storage."""
        from src.modules.preparation.service import DatasetPreparationService

        with TemporaryDirectory() as tmpdir:
            svc = DatasetPreparationService(Path(tmpdir))
            assert svc.list_datasets() == []

    def test_get_presets(self) -> None:
        """Test listing pipeline presets."""
        from src.modules.preparation.service import DatasetPreparationService

        with TemporaryDirectory() as tmpdir:
            svc = DatasetPreparationService(Path(tmpdir))
            presets = svc.get_presets("humerus")
            assert len(presets) >= 3
            names = [p["name"] for p in presets]
            assert "replay_membre" in names

    def test_get_presets_spine(self) -> None:
        """Test presets for non-limb bone type."""
        from src.modules.preparation.service import DatasetPreparationService

        with TemporaryDirectory() as tmpdir:
            svc = DatasetPreparationService(Path(tmpdir))
            presets = svc.get_presets("vertebra")
            assert len(presets) >= 3
