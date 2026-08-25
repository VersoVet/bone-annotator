"""CVAT annotation sync — pull annotations from CVAT to PostgreSQL."""

import logging
from typing import Any

from src.config import get_postgres_config

logger = logging.getLogger(__name__)

_PROVENANCE_KEYS = {"source", "confidence", "model_version"}


def _extract_shape_provenance(attributes: list[dict[str, Any]]) -> dict[str, Any]:
    """Extract provenance fields from CVAT shape attributes JSON."""
    result: dict[str, Any] = {}
    for attr in attributes:
        name = attr.get("name", "")
        value = attr.get("value", "")
        if name == "confidence":
            try:
                result["confidence"] = float(value)
            except (ValueError, TypeError):
                pass
        elif name in _PROVENANCE_KEYS:
            result[name] = value
    return result


async def sync_from_cvat(
    cvat_client: Any,
    task: dict[str, Any],
) -> dict[str, Any]:
    """Sync annotations from CVAT JSON REST API to PostgreSQL.

    Args:
        cvat_client: Authenticated CVATClient instance.
        task: Task dict from task_db.

    Returns:
        Dict with synced_frames, zones_count, landmarks_count, author.
    """
    cvat_task_id = task["cvat_task_id"]

    # Get assignee from CVAT jobs
    jobs = await cvat_client.get_task_jobs(cvat_task_id)
    author = "unknown"
    if jobs:
        assignee_info = jobs[0].get("assignee")
        if assignee_info and isinstance(assignee_info, dict):
            author = assignee_info.get("username", "unknown")
        elif isinstance(assignee_info, str):
            author = assignee_info

    # Pull annotations as JSON
    raw_annotations = await cvat_client.get_annotations(cvat_task_id)

    zones_count = 0
    landmarks_count = 0
    synced_frames = 0

    if raw_annotations and "shapes" in raw_annotations:
        from src.modules.storage.pg_db import AnnotationPgDB

        pg_config = get_postgres_config()
        db = AnnotationPgDB(**pg_config)

        db.ensure_acquisition(
            acq_id=task["acquisition_id"],
            category=task.get("bone_type", ""),
            bone_type=task.get("bone_type", ""),
            side=task.get("region", "entire"),
            region=task.get("region", "entire"),
            frame_count=task.get("frame_count", 0),
        )

        # Resolve label IDs to names
        label_map: dict[int, str] = {}
        if cvat_client.client:
            lbl_resp = await cvat_client.client.get(
                f"{cvat_client.api_base}/labels?task_id={cvat_task_id}"
            )
            if lbl_resp.status_code == 200:
                for lbl in lbl_resp.json().get("results", []):
                    label_map[lbl["id"]] = lbl["name"]

        # Group shapes by frame
        frames: dict[int, dict[str, list[Any]]] = {}
        for shape in raw_annotations.get("shapes", []):
            frame_num = shape.get("frame", 0)
            if frame_num not in frames:
                frames[frame_num] = {"zones": [], "landmarks": []}

            provenance = _extract_shape_provenance(shape.get("attributes", []))
            label_name = label_map.get(shape.get("label_id"), str(shape.get("label_id", "")))
            shape_data = {
                "label": label_name,
                "type": shape.get("type", "rectangle"),
                **provenance,
            }
            if shape.get("type") == "points":
                pts = shape.get("points", [])
                if len(pts) >= 2:
                    shape_data["x"] = pts[0]
                    shape_data["y"] = pts[1]
                frames[frame_num]["landmarks"].append(shape_data)
                landmarks_count += 1
            else:
                pts = shape.get("points", [])
                if len(pts) >= 4:
                    shape_data["x"] = pts[0]
                    shape_data["y"] = pts[1]
                    shape_data["width"] = pts[2] - pts[0]
                    shape_data["height"] = pts[3] - pts[1]
                frames[frame_num]["zones"].append(shape_data)
                zones_count += 1

        # Save each frame
        for frame_num, anns in frames.items():
            frame_fn = f"frame_{frame_num:04d}.png"
            first = (anns["zones"] or anns["landmarks"])[0]
            db.save_frame_annotations(
                task["acquisition_id"],
                frame_fn,
                anns,
                task_id=task.get("id"),
                author=author,
                source=first.get("source", "manual"),
                confidence=first.get("confidence"),
                model_version=first.get("model_version"),
            )
            synced_frames += 1
        db.close()

    logger.info(
        "Task %s synced: %d frames, %d zones, %d landmarks",
        task.get("id"), synced_frames, zones_count, landmarks_count,
    )

    return {
        "synced_frames": synced_frames,
        "zones_count": zones_count,
        "landmarks_count": landmarks_count,
        "author": author,
    }
