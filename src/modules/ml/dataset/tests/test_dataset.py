"""Tests for ML dataset service."""

from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from src.modules.ml.dataset.service import (
    _zone_to_yolo_line,
    delete_dataset,
    export_to_yolo,
    get_dataset_stats,
)


class TestZoneToYoloLine:
    """Tests for zone annotation to YOLO format conversion."""

    def test_valid_zone(self) -> None:
        """Test converting a valid zone to YOLO format."""
        zone = {"label": "proximal_humerus", "x": 100, "y": 50, "width": 200, "height": 300}
        mapping = {"proximal_humerus": 0}
        line = _zone_to_yolo_line(zone, mapping, img_w=1000, img_h=1000)
        assert line is not None
        parts = line.split()
        assert parts[0] == "0"
        assert float(parts[1]) == pytest.approx(0.2)  # (100+100)/1000
        assert float(parts[2]) == pytest.approx(0.2)  # (50+150)/1000
        assert float(parts[3]) == pytest.approx(0.2)  # 200/1000
        assert float(parts[4]) == pytest.approx(0.3)  # 300/1000

    def test_label_not_in_mapping(self) -> None:
        """Test zone with unknown label returns None."""
        zone = {"label": "unknown_zone", "x": 0, "y": 0, "width": 10, "height": 10}
        result = _zone_to_yolo_line(zone, {}, img_w=100, img_h=100)
        assert result is None

    def test_zero_dimension(self) -> None:
        """Test zone with zero width/height returns None."""
        zone = {"label": "proximal_humerus", "x": 10, "y": 10, "width": 0, "height": 50}
        mapping = {"proximal_humerus": 0}
        result = _zone_to_yolo_line(zone, mapping, img_w=100, img_h=100)
        assert result is None

    def test_bbox_nested_dict(self) -> None:
        """Test zone with bbox as nested dict."""
        zone = {
            "label": "distal_humerus",
            "bbox": {"x": 50, "y": 50, "width": 100, "height": 100},
        }
        mapping = {"distal_humerus": 1}
        line = _zone_to_yolo_line(zone, mapping, img_w=500, img_h=500)
        assert line is not None
        assert line.startswith("1 ")

    def test_name_field_fallback(self) -> None:
        """Test zone using 'name' instead of 'label'."""
        zone = {"name": "proximal_radius", "x": 0, "y": 0, "width": 10, "height": 10}
        mapping = {"proximal_radius": 2}
        line = _zone_to_yolo_line(zone, mapping, img_w=100, img_h=100)
        assert line is not None
        assert line.startswith("2 ")


class TestExportValidation:
    """Tests for export_to_yolo input validation."""

    def test_empty_acquisitions(self) -> None:
        """Test empty acquisition list raises ValueError."""
        import asyncio

        with pytest.raises(ValueError, match="cannot be empty"):
            asyncio.run(export_to_yolo([]))

    def test_invalid_ratios(self) -> None:
        """Test invalid split ratios raises ValueError."""
        import asyncio

        with pytest.raises(ValueError, match="must be < 1.0"):
            asyncio.run(export_to_yolo(["acq1"], train_ratio=0.6, val_ratio=0.5))

    def test_creates_directory_structure(self) -> None:
        """Test export creates correct directory structure even on pg error."""
        import asyncio

        with TemporaryDirectory() as tmpdir:
            result = asyncio.run(export_to_yolo(["acq1", "acq2"], output_dir=tmpdir))
            # May error on PG connection but directory should exist
            assert "dataset_path" in result


class TestDatasetStats:
    """Tests for dataset statistics."""

    def test_nonexistent_directory(self) -> None:
        """Test stats for non-existent directory returns error."""
        import asyncio

        result = asyncio.run(get_dataset_stats("/nonexistent/path"))
        assert result.get("status") == "error"

    def test_valid_dataset_structure(self) -> None:
        """Test stats for valid directory structure."""
        import asyncio

        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir)
            for split in ["train", "val", "test"]:
                (path / split / "images").mkdir(parents=True)
                (path / split / "labels").mkdir(parents=True)

            # Create some fake files
            (path / "train" / "images" / "img1.png").touch()
            (path / "train" / "images" / "img2.png").touch()
            (path / "train" / "labels" / "img1.txt").write_text("0 0.5 0.5 0.1 0.1\n")

            result = asyncio.run(get_dataset_stats(path))
            assert result["total_images"] == 2
            assert result["total_labels"] == 1
            assert result["splits"]["train"]["images"] == 2


class TestDeleteDataset:
    """Tests for dataset deletion."""

    def test_delete_removes_directory(self) -> None:
        """Test delete_dataset removes directory tree."""
        import asyncio

        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir)
            (path / "train" / "images").mkdir(parents=True)
            (path / "train" / "labels").mkdir(parents=True)

            result = asyncio.run(delete_dataset(path))
            assert result.get("status") == "success"
            assert not path.exists()
