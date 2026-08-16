"""Tests for CVAT format conversion and label generation."""

from typing import Any


class TestLabelsToSvat:
    """Tests for label-generator taxonomy to CVAT format conversion."""

    def test_zones_only(self) -> None:
        """Test conversion with zones only."""
        from src.modules.cvat.format import labels_to_cvat_format

        anatomy: dict[str, Any] = {
            "zones": [
                {"id": "metaphysis", "color": "#00FF00"},
                {"id": "diaphysis", "color": "#0000FF"},
            ],
            "landmarks": [],
        }
        labels = labels_to_cvat_format(anatomy)
        assert len(labels) == 2
        assert labels[0]["name"] == "metaphysis"
        assert labels[0]["type"] == "rectangle"
        assert labels[0]["color"] == "#00FF00"

    def test_landmarks_only(self) -> None:
        """Test conversion with landmarks only."""
        from src.modules.cvat.format import labels_to_cvat_format

        anatomy: dict[str, Any] = {
            "zones": [],
            "landmarks": [{"id": "greater_tubercle"}, {"id": "lesser_tubercle"}],
        }
        labels = labels_to_cvat_format(anatomy)
        assert len(labels) == 2
        assert all(lbl["type"] == "points" for lbl in labels)

    def test_mixed(self) -> None:
        """Test conversion with both zones and landmarks."""
        from src.modules.cvat.format import labels_to_cvat_format

        anatomy: dict[str, Any] = {
            "zones": [{"id": "proximal"}],
            "landmarks": [{"id": "epicondyle"}],
        }
        labels = labels_to_cvat_format(anatomy)
        assert len(labels) == 2
        types = {lbl["name"]: lbl["type"] for lbl in labels}
        assert types["proximal"] == "rectangle"
        assert types["epicondyle"] == "points"

    def test_dedup(self) -> None:
        """Test duplicate names are filtered."""
        from src.modules.cvat.format import labels_to_cvat_format

        anatomy: dict[str, Any] = {
            "zones": [{"id": "dup"}, {"id": "dup"}],
            "landmarks": [{"id": "dup"}],
        }
        assert len(labels_to_cvat_format(anatomy)) == 1

    def test_empty(self) -> None:
        """Test empty anatomy returns empty list."""
        from src.modules.cvat.format import labels_to_cvat_format

        assert labels_to_cvat_format({"zones": [], "landmarks": []}) == []

    def test_label_fallback(self) -> None:
        """Test fallback to 'label' key when 'id' is missing."""
        from src.modules.cvat.format import labels_to_cvat_format

        anatomy: dict[str, Any] = {
            "zones": [{"label": "cortex"}],
            "landmarks": [],
        }
        labels = labels_to_cvat_format(anatomy)
        assert len(labels) == 1
        assert labels[0]["name"] == "cortex"


class TestConvertToXml:
    """Tests for internal → CVAT XML conversion."""

    def test_empty_annotations(self) -> None:
        """Test empty annotations produce valid XML."""
        from src.modules.cvat.format import convert_to_cvat_xml

        xml = convert_to_cvat_xml({"images": []})
        assert '<?xml version="1.0"' in xml
        assert "<annotations>" in xml

    def test_box_annotation(self) -> None:
        """Test box shape is rendered correctly."""
        from src.modules.cvat.format import convert_to_cvat_xml

        annotations = {
            "images": [
                {
                    "id": "0",
                    "name": "frame_0.png",
                    "width": 512,
                    "height": 512,
                    "shapes": [{"type": "box", "label": "bone", "x1": 10, "y1": 20, "x2": 100, "y2": 200}],
                    "landmarks": [],
                }
            ],
        }
        xml = convert_to_cvat_xml(annotations)
        assert 'label="bone"' in xml
        assert 'xtl="10"' in xml

    def test_point_annotation(self) -> None:
        """Test landmark point is rendered."""
        from src.modules.cvat.format import convert_to_cvat_xml

        annotations = {
            "images": [
                {
                    "id": "0",
                    "name": "f.png",
                    "width": 100,
                    "height": 100,
                    "shapes": [],
                    "landmarks": [{"name": "epicondyle", "x": 50, "y": 75}],
                }
            ],
        }
        xml = convert_to_cvat_xml(annotations)
        assert 'label="epicondyle"' in xml


class TestConvertFromXml:
    """Tests for CVAT XML → internal format conversion."""

    def test_parse_box(self) -> None:
        """Test parsing box from XML."""
        from src.modules.cvat.format import convert_from_cvat_xml

        xml = """<?xml version="1.0"?>
        <annotations>
          <image id="0" name="test.png" width="512" height="512">
            <box label="bone" xtl="10" ytl="20" xbr="100" ybr="200" />
          </image>
        </annotations>"""
        result = convert_from_cvat_xml(xml)
        assert len(result["images"]) == 1
        assert len(result["images"][0]["shapes"]) == 1
        assert result["images"][0]["shapes"][0]["label"] == "bone"

    def test_parse_point(self) -> None:
        """Test parsing point (landmark) from XML."""
        from src.modules.cvat.format import convert_from_cvat_xml

        xml = """<?xml version="1.0"?>
        <annotations>
          <image id="0" name="test.png" width="100" height="100">
            <point label="tip" x="50" y="75" />
          </image>
        </annotations>"""
        result = convert_from_cvat_xml(xml)
        assert len(result["images"][0]["landmarks"]) == 1
        assert result["images"][0]["landmarks"][0]["name"] == "tip"

    def test_invalid_xml(self) -> None:
        """Test invalid XML returns empty."""
        from src.modules.cvat.format import convert_from_cvat_xml

        result = convert_from_cvat_xml("not xml")
        assert result == {"images": []}
