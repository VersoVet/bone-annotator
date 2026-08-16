"""Tests for ML predict module — annotation formatting, validation, confidence."""

from unittest.mock import MagicMock

import pytest


class TestFormatAnnotations:
    """Tests for YOLO result to Label Studio format conversion."""

    def _make_mock_result(
        self,
        boxes: list[tuple[float, float, float, float, int, float]],
        img_shape: tuple[int, int] = (512, 512),
    ) -> MagicMock:
        """Create a mock YOLO result.

        Args:
            boxes: List of (x1, y1, x2, y2, cls_id, conf).
            img_shape: Original image shape (h, w).

        Returns:
            Mock YOLO result object.
        """
        import numpy as np

        mock_boxes = []
        for x1, y1, x2, y2, cls_id, conf in boxes:
            box = MagicMock()
            box.xyxy = [np.array([x1, y1, x2, y2])]
            box.cls = [np.array(cls_id)]
            box.conf = [np.array(conf)]
            mock_boxes.append(box)

        result = MagicMock()
        result.boxes = mock_boxes if mock_boxes else None
        result.orig_shape = img_shape
        result.names = {0: "proximal_humerus", 1: "distal_humerus", 2: "shaft"}
        result.keypoints = None
        return result

    def test_single_box(self) -> None:
        """Test formatting a single bounding box."""
        from ..service import _format_annotations

        result = self._make_mock_result(
            [(100, 100, 200, 200, 0, 0.95)],
            img_shape=(512, 512),
        )
        annotations = _format_annotations(result)
        assert len(annotations) == 1
        ann = annotations[0]
        assert ann["type"] == "rectanglelabels"
        assert ann["score"] == pytest.approx(0.95)
        assert ann["value"]["rectanglelabels"] == ["proximal_humerus"]
        # Check percentages
        assert ann["value"]["x"] == pytest.approx((100 / 512) * 100)
        assert ann["value"]["y"] == pytest.approx((100 / 512) * 100)

    def test_multiple_boxes(self) -> None:
        """Test formatting multiple bounding boxes."""
        from ..service import _format_annotations

        result = self._make_mock_result(
            [
                (10, 20, 100, 120, 0, 0.9),
                (200, 300, 400, 450, 1, 0.7),
            ]
        )
        annotations = _format_annotations(result)
        assert len(annotations) == 2
        assert annotations[0]["value"]["rectanglelabels"] == ["proximal_humerus"]
        assert annotations[1]["value"]["rectanglelabels"] == ["distal_humerus"]

    def test_no_boxes(self) -> None:
        """Test formatting with no detections."""
        from ..service import _format_annotations

        result = self._make_mock_result([])
        annotations = _format_annotations(result)
        assert annotations == []

    def test_unknown_class_id(self) -> None:
        """Test formatting with unknown class ID uses fallback name."""
        from ..service import _format_annotations

        result = self._make_mock_result([(0, 0, 50, 50, 99, 0.5)])
        annotations = _format_annotations(result)
        assert annotations[0]["value"]["rectanglelabels"] == ["class_99"]


class TestAvgConfidence:
    """Tests for average confidence calculation."""

    def test_single_detection(self) -> None:
        """Test average confidence with one detection."""
        import numpy as np

        from ..service import _avg_confidence

        result = MagicMock()
        result.boxes = MagicMock()
        result.boxes.__len__ = lambda self: 1
        result.boxes.conf = MagicMock()
        result.boxes.conf.mean = MagicMock(return_value=np.float32(0.85))
        assert _avg_confidence(result) == pytest.approx(0.85, abs=1e-5)

    def test_no_detections(self) -> None:
        """Test average confidence with no detections."""
        from ..service import _avg_confidence

        result = MagicMock()
        result.boxes = None
        assert _avg_confidence(result) == 0.0

    def test_empty_boxes(self) -> None:
        """Test average confidence with empty boxes list."""
        from ..service import _avg_confidence

        result = MagicMock()
        result.boxes = MagicMock()
        result.boxes.__len__ = lambda self: 0
        assert _avg_confidence(result) == 0.0


class TestLoadImageValidation:
    """Tests for image loading security validation."""

    def test_url_host_not_whitelisted(self) -> None:
        """Test that non-whitelisted URL hosts are rejected."""
        from ..service import _load_image

        with pytest.raises(ValueError, match="not whitelisted"):
            _load_image("http://evil.com/image.png")

    def test_path_traversal_rejected(self) -> None:
        """Test that path traversal attempts are rejected."""
        from ..service import _load_image

        with pytest.raises((ValueError, FileNotFoundError)):
            _load_image("../../etc/passwd")

    def test_absolute_path_outside_bonestore_rejected(self) -> None:
        """Test that absolute paths outside BoneStore are rejected."""
        from ..service import _load_image

        with pytest.raises((ValueError, FileNotFoundError)):
            _load_image("/tmp/evil.png")


class TestModelInfo:
    """Tests for model info endpoint."""

    @pytest.mark.asyncio
    async def test_model_info_default(self) -> None:
        """Test model info returns expected structure."""
        from ..service import get_model_info

        info = await get_model_info()
        assert "model_version" in info
        assert "model_loaded" in info
        assert info["model_type"] == "yolov8"
