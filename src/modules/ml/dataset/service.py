"""ML dataset service — Export annotations to YOLO format.

Converts annotations from PostgreSQL to YOLO dataset format
with train/val/test splits and generates dataset.yaml configuration.
"""

import logging
import random
import shutil
from pathlib import Path
from typing import Any

import yaml

from .utils import find_frame_image, get_frame_dimensions, zone_to_yolo_line

logger = logging.getLogger(__name__)

# Default YOLO dataset root
DATASET_ROOT = Path("data/datasets")

# Keep old names importable for tests
_zone_to_yolo_line = zone_to_yolo_line


async def export_to_yolo(
    acquisitions: list[str],
    output_dir: str | Path | None = None,
    train_ratio: float = 0.7,
    val_ratio: float = 0.2,
    labels_mapping: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Export annotations to YOLO dataset format.

    Fetches annotations from PostgreSQL, converts zones to YOLO .txt labels,
    and copies corresponding frame images into train/val/test splits.

    Args:
        acquisitions: List of acquisition IDs to export.
        output_dir: Output directory for dataset (default: data/datasets/{timestamp}).
        train_ratio: Fraction for training split (default 0.7).
        val_ratio: Fraction for validation split (default 0.2).
        labels_mapping: Optional mapping of zone names to class IDs.

    Returns:
        Dict with dataset_path, split_stats, and yaml_config.

    Raises:
        ValueError: If acquisition list empty or split ratios invalid.
    """
    if not acquisitions:
        raise ValueError("acquisitions list cannot be empty")

    if train_ratio + val_ratio >= 1.0:
        raise ValueError("train_ratio + val_ratio must be < 1.0")

    # Setup output directory
    if output_dir is None:
        from datetime import UTC, datetime

        timestamp = datetime.now(tz=UTC).strftime("%Y%m%d_%H%M%S")
        output_dir = DATASET_ROOT / f"yolo_{timestamp}"
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Import annotation DB
    try:
        from src.config import get_postgres_config
        from src.modules.storage.pg_db import AnnotationPgDB
    except ImportError as e:
        logger.error("Cannot import PostgreSQL client: %s", e)
        return {
            "status": "error",
            "message": "PostgreSQL client not available",
            "dataset_path": str(output_dir),
        }

    # Connect to PostgreSQL
    try:
        pg_config = get_postgres_config()
        db = AnnotationPgDB(**pg_config)
    except Exception as e:
        logger.error("Failed to initialize PostgreSQL client: %s", e)
        return {
            "status": "error",
            "message": str(e),
            "dataset_path": str(output_dir),
        }

    # Default labels mapping (zones → class IDs)
    if labels_mapping is None:
        labels_mapping = {
            "proximal_humerus": 0,
            "distal_humerus": 1,
            "proximal_radius": 2,
            "distal_radius": 3,
            "proximal_ulna": 4,
            "distal_ulna": 5,
        }

    class_names = {v: k for k, v in labels_mapping.items()}

    # Create directory structure
    for split in ["train", "val", "test"]:
        (output_dir / split / "images").mkdir(parents=True, exist_ok=True)
        (output_dir / split / "labels").mkdir(parents=True, exist_ok=True)

    # Collect annotated frames from PostgreSQL
    all_frames: list[tuple[str, str, dict[str, Any]]] = []
    try:
        for acq_id in acquisitions:
            acq_data = db.load_acquisition_annotations(acq_id)
            for fname, anns in acq_data.get("frames", {}).items():
                if anns.get("zones"):
                    all_frames.append((acq_id, fname, anns))
    except Exception as e:
        logger.error("Error loading annotations from PostgreSQL: %s", e)
        db.close()
        return {
            "status": "error",
            "message": f"Failed to load annotations: {e}",
            "dataset_path": str(output_dir),
        }

    if not all_frames:
        db.close()
        return {
            "status": "warning",
            "message": "No annotated frames found for given acquisitions",
            "dataset_path": str(output_dir),
            "total_frames": 0,
        }

    # Shuffle and distribute across splits
    random.shuffle(all_frames)
    total = len(all_frames)
    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)

    split_counts = {"train": 0, "val": 0, "test": 0}
    skipped = 0

    for i, (acq_id, frame_filename, annotations) in enumerate(all_frames):
        split = "train" if i < train_end else ("val" if i < val_end else "test")

        frame_path = find_frame_image(acq_id, frame_filename)
        if frame_path is None:
            logger.warning("Frame not found: %s/%s", acq_id, frame_filename)
            skipped += 1
            continue

        img_w, img_h = get_frame_dimensions(frame_path)

        yolo_lines = [
            line
            for zone in annotations.get("zones", [])
            if (line := zone_to_yolo_line(zone, labels_mapping, img_w, img_h))
        ]

        if not yolo_lines:
            skipped += 1
            continue

        # Write YOLO label file
        label_name = f"{acq_id}_{frame_path.stem}.txt"
        (output_dir / split / "labels" / label_name).write_text("\n".join(yolo_lines) + "\n")

        # Copy frame image
        image_dest = output_dir / split / "images" / f"{acq_id}_{frame_path.name}"
        if not image_dest.exists():
            shutil.copy2(frame_path, image_dest)

        split_counts[split] += 1

    db.close()

    # Generate dataset.yaml
    dataset_yaml = {
        "path": str(output_dir.resolve()),
        "train": "train/images",
        "val": "val/images",
        "test": "test/images",
        "nc": len(class_names),
        "names": class_names,
    }

    yaml_path = output_dir / "dataset.yaml"
    with yaml_path.open("w") as f:
        yaml.dump(dataset_yaml, f, default_flow_style=False)

    total_exported = sum(split_counts.values())
    logger.info(
        "Dataset exported: %d frames (train=%d, val=%d, test=%d, skipped=%d)",
        total_exported,
        split_counts["train"],
        split_counts["val"],
        split_counts["test"],
        skipped,
    )

    return {
        "status": "success",
        "dataset_path": str(output_dir.resolve()),
        "yaml_path": str(yaml_path.resolve()),
        "split_stats": split_counts,
        "dataset_config": dataset_yaml,
        "total_acquisitions": len(acquisitions),
        "total_frames_exported": total_exported,
        "skipped_frames": skipped,
    }


async def get_dataset_stats(dataset_dir: str | Path) -> dict[str, Any]:
    """Get statistics for an existing YOLO dataset.

    Args:
        dataset_dir: Path to dataset root directory.

    Returns:
        Dict with file counts per split and classes.
    """
    dataset_dir = Path(dataset_dir)

    if not dataset_dir.exists():
        return {
            "status": "error",
            "message": f"Dataset directory not found: {dataset_dir}",
        }

    stats: dict[str, Any] = {
        "dataset_dir": str(dataset_dir.resolve()),
        "splits": {},
        "total_images": 0,
        "total_labels": 0,
    }

    for split in ["train", "val", "test"]:
        img_dir = dataset_dir / split / "images"
        lbl_dir = dataset_dir / split / "labels"
        img_count = len(list(img_dir.glob("*"))) if img_dir.exists() else 0
        lbl_count = len(list(lbl_dir.glob("*.txt"))) if lbl_dir.exists() else 0
        stats["splits"][split] = {"images": img_count, "labels": lbl_count}
        stats["total_images"] += img_count
        stats["total_labels"] += lbl_count

    yaml_path = dataset_dir / "dataset.yaml"
    if yaml_path.exists():
        with yaml_path.open() as f:
            stats["config"] = yaml.safe_load(f)

    return stats


async def delete_dataset(dataset_dir: str | Path) -> dict[str, Any]:
    """Delete a dataset directory.

    Args:
        dataset_dir: Path to dataset to delete.

    Returns:
        Status dict.
    """
    dataset_dir = Path(dataset_dir)
    try:
        shutil.rmtree(dataset_dir)
        logger.info("Dataset deleted: %s", dataset_dir)
        return {"status": "success", "message": f"Dataset deleted: {dataset_dir}"}
    except Exception as e:
        logger.error("Failed to delete dataset: %s", e)
        return {"status": "error", "message": str(e)}
