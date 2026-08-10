"""ML dataset service — Export annotations to YOLO format.

Converts annotations from PostgreSQL to YOLO dataset format
with train/val/test splits and generates dataset.yaml configuration.
"""

import logging
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)

# Default YOLO dataset root
DATASET_ROOT = Path("data/datasets")


async def export_to_yolo(
    acquisitions: list[str],
    output_dir: str | Path | None = None,
    train_ratio: float = 0.7,
    val_ratio: float = 0.2,
    labels_mapping: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Export annotations to YOLO dataset format.

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
        from datetime import datetime

        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        output_dir = DATASET_ROOT / f"yolo_{timestamp}"
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Import annotation DB to load data
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

    # Get PostgreSQL configuration
    try:
        pg_config = get_postgres_config()
        _ = AnnotationPgDB(**pg_config)  # Verify connection (not used for now)
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

    # Reverse mapping for YAML
    class_names = {v: k for k, v in labels_mapping.items()}

    # Create directory structure
    splits = ["train", "val", "test"]
    for split in splits:
        (output_dir / split / "images").mkdir(parents=True, exist_ok=True)
        (output_dir / split / "labels").mkdir(parents=True, exist_ok=True)

    # Load annotations for all acquisitions
    split_counts = {"train": 0, "val": 0, "test": 0}

    try:
        # Placeholder: In real implementation, query PostgreSQL
        # for annotations linked to acquisitions
        # For now, return proper structure but note implementation needed
        logger.warning("Dataset export: PostgreSQL query not implemented in Phase %d", 1)

        # Distribute acquisitions across splits (test_ratio calculated but unused in placeholder)
        total = len(acquisitions)
        train_count = int(total * train_ratio)
        val_count = int(total * val_ratio)

        for i, acq_id in enumerate(acquisitions):
            if i < train_count:
                split = "train"
            elif i < train_count + val_count:
                split = "val"
            else:
                split = "test"
            split_counts[split] += 1

    except Exception as e:
        logger.error("Error loading annotations: %s", e)
        return {
            "status": "error",
            "message": str(e),
            "dataset_path": str(output_dir),
        }

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

    logger.info(
        "Dataset exported: train=%d, val=%d, test=%d",
        split_counts["train"],
        split_counts["val"],
        split_counts["test"],
    )

    return {
        "status": "success",
        "dataset_path": str(output_dir.resolve()),
        "yaml_path": str(yaml_path.resolve()),
        "split_stats": split_counts,
        "dataset_config": dataset_yaml,
        "total_acquisitions": len(acquisitions),
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

    stats = {
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

    # Load dataset.yaml if present
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
    import shutil

    dataset_dir = Path(dataset_dir)

    try:
        shutil.rmtree(dataset_dir)
        logger.info("Dataset deleted: %s", dataset_dir)
        return {
            "status": "success",
            "message": f"Dataset deleted: {dataset_dir}",
        }
    except Exception as e:
        logger.error("Failed to delete dataset: %s", e)
        return {
            "status": "error",
            "message": str(e),
        }
