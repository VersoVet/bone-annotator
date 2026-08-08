"""Format conversion for CVAT annotations.

Converts between bone-annotator internal formats and CVAT XML/JSON formats.
"""

import logging
from typing import Any

logger = logging.getLogger(__name__)


def convert_to_cvat_xml(annotations: dict[str, Any]) -> str:
    """Convert bone annotations to CVAT XML format.

    Args:
        annotations: Internal annotation dict.

    Returns:
        CVAT XML string.
    """
    try:
        lines: list[str] = ['<?xml version="1.0" encoding="utf-8"?>']
        lines.append("<annotations>")

        # Add version
        lines.append("  <version>1.1</version>")

        # Add meta if present
        if "meta" in annotations:
            lines.append("  <meta>")
            meta = annotations["meta"]
            if "task" in meta:
                lines.append(f"    <task>{meta['task']}</task>")
            lines.append("  </meta>")

        # Add images
        if "images" in annotations:
            for img in annotations["images"]:
                img_id = img.get("id", "")
                img_name = img.get("name", "")
                lines.append(
                    f'  <image id="{img_id}" name="{img_name}" width="{img.get("width", "")}" '
                    f'height="{img.get("height", "")}">'
                )

                # Add shapes (boxes, polygons, etc)
                if "shapes" in img:
                    for shape in img["shapes"]:
                        shape_type = shape.get("type", "box")
                        label = shape.get("label", "bone")

                        if shape_type == "box":
                            x1 = shape.get("x1", 0)
                            y1 = shape.get("y1", 0)
                            x2 = shape.get("x2", 0)
                            y2 = shape.get("y2", 0)
                            lines.append(f'    <box label="{label}" xtl="{x1}" ytl="{y1}" xbr="{x2}" ybr="{y2}" />')
                        elif shape_type == "polygon":
                            points = shape.get("points", [])
                            points_str = ";".join(f"{p['x']},{p['y']}" for p in points)
                            lines.append(f'    <polygon label="{label}" points="{points_str}" />')

                # Add landmarks as points
                if "landmarks" in img:
                    for lm in img["landmarks"]:
                        name = lm.get("name", "")
                        x = lm.get("x", 0)
                        y = lm.get("y", 0)
                        lines.append(f'    <point label="{name}" x="{x}" y="{y}" />')

                lines.append("  </image>")

        lines.append("</annotations>")
        return "\n".join(lines)
    except Exception as e:
        logger.error("Error converting to CVAT XML: %s", e)
        return ""


def convert_from_cvat_xml(xml_string: str) -> dict[str, Any]:
    """Convert CVAT XML to bone annotations format.

    Args:
        xml_string: CVAT XML string.

    Returns:
        Internal annotation dict.
    """
    try:
        import xml.etree.ElementTree as ET

        root = ET.fromstring(xml_string)
        annotations: dict[str, Any] = {"images": []}

        # Parse images
        for img_elem in root.findall("image"):
            img: dict[str, Any] = {
                "id": img_elem.get("id", ""),
                "name": img_elem.get("name", ""),
                "width": int(img_elem.get("width", "0")),
                "height": int(img_elem.get("height", "0")),
                "shapes": [],
                "landmarks": [],
            }

            # Parse boxes
            for box in img_elem.findall("box"):
                img["shapes"].append(
                    {
                        "type": "box",
                        "label": box.get("label", ""),
                        "x1": int(float(box.get("xtl", "0"))),
                        "y1": int(float(box.get("ytl", "0"))),
                        "x2": int(float(box.get("xbr", "0"))),
                        "y2": int(float(box.get("ybr", "0"))),
                    }
                )

            # Parse polygons
            for poly in img_elem.findall("polygon"):
                points_str = poly.get("points", "")
                points = [
                    {
                        "x": float(p.split(",")[0]),
                        "y": float(p.split(",")[1]),
                    }
                    for p in points_str.split(";")
                    if p
                ]
                img["shapes"].append(
                    {
                        "type": "polygon",
                        "label": poly.get("label", ""),
                        "points": points,
                    }
                )

            # Parse points (landmarks)
            for point in img_elem.findall("point"):
                img["landmarks"].append(
                    {
                        "name": point.get("label", ""),
                        "x": float(point.get("x", "0")),
                        "y": float(point.get("y", "0")),
                        "confidence": 1.0,
                    }
                )

            annotations["images"].append(img)

        return annotations
    except Exception as e:
        logger.error("Error converting from CVAT XML: %s", e)
        return {"images": []}
