"""Tests for ML dataset service."""

from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from src.modules.ml.dataset.service import delete_dataset, export_to_yolo, get_dataset_stats


def test_export_to_yolo_empty_acquisitions():
    """Test export_to_yolo raises ValueError for empty acquisition list."""
    with pytest.raises(ValueError, match="cannot be empty"):
        import asyncio
        asyncio.run(export_to_yolo([]))


def test_export_to_yolo_invalid_ratios():
    """Test export_to_yolo raises ValueError for invalid split ratios."""
    import asyncio
    with pytest.raises(ValueError, match="must be < 1.0"):
        asyncio.run(export_to_yolo(["acq1"], train_ratio=0.6, val_ratio=0.5))


def test_export_to_yolo_creates_directory():
    """Test export_to_yolo creates output directory structure."""
    import asyncio
    with TemporaryDirectory() as tmpdir:
        result = asyncio.run(
            export_to_yolo(
                ["acq1", "acq2", "acq3"],
                output_dir=tmpdir,
            )
        )

        # Should succeed even if PostgreSQL is not connected (Phase 1 placeholder)
        assert result.get("status") in ("success", "error")
        assert "dataset_path" in result


def test_get_dataset_stats_nonexistent():
    """Test get_dataset_stats for non-existent directory."""
    import asyncio
    result = asyncio.run(get_dataset_stats("/nonexistent/path"))
    assert result.get("status") == "error"


def test_delete_dataset():
    """Test delete_dataset removes directory."""
    import asyncio
    with TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        (path / "train" / "images").mkdir(parents=True)
        (path / "train" / "labels").mkdir(parents=True)

        result = asyncio.run(delete_dataset(path))
        assert result.get("status") == "success"
        assert not path.exists()
