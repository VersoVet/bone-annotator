"""Streaming ingestion pipeline from BoneStore (NFS).

Processes acquisitions one by one from NFS mount,
selects key frames (angular sampling), preprocesses,
and saves locally in compact .npy format.
"""

import json
import logging
import os
from pathlib import Path
from typing import Any

import numpy as np

from src.modules.bonestore.service import load_timecodes
from src.modules.ingestion.ingest_utils import (
    extract_frame_index,
    image_hash,
    preprocess_image,
    read_b2nd_frame,
    select_frames,
)
from src.modules.ingestion.registry import IngestionRegistry

logger = logging.getLogger(__name__)

# Selection: one frame every N degrees (360/10° = 36 frames per acquisition)
DEFAULT_ANGLE_STEP_DEG = 10.0
# Fallback if no timecodes: take 1 frame per N
DEFAULT_FRAME_STRIDE = 25


def ingest_acquisition(
    acq_dir: Path,
    output_dir: Path,
    registry: IngestionRegistry,
    acquisition_id: str,
    bone_type: str,
    side: str,
    region: str,
    angle_step_deg: float = DEFAULT_ANGLE_STEP_DEG,
    target_size: int = 512,
) -> int:
    """Ingest complete acquisition from BoneStore.

    Reads .b2nd frames via NFS, selects by angle,
    preprocesses and saves as .npy + .json sidecar.

    Args:
        acq_dir: Acquisition directory on NFS.
        output_dir: Local output directory (data/processed/train/).
        registry: Ingestion registry for tracking.
        acquisition_id: Unique acquisition ID.
        bone_type: Bone type (humerus, radius, etc.).
        side: Side (left, right, bilateral).
        region: Region (proximal, distal, entire).
        angle_step_deg: Angular spacing between selected frames.
        target_size: Output image size.

    Returns:
        Number of saved frames.
    """
    raw_dir = acq_dir / "raw"
    if not raw_dir.exists():
        logger.error("No raw/ folder in %s", acq_dir)
        registry.mark_failed(acquisition_id, "No raw/ directory")
        return 0

    registry.mark_started(acquisition_id)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load timecodes if available
    timecodes = load_timecodes(acq_dir)
    frame_files = sorted(raw_dir.glob("*.b2nd"))

    if not frame_files:
        registry.mark_failed(acquisition_id, "No .b2nd frames found")
        return 0

    # Select frames by angle or stride
    selected = select_frames(frame_files, timecodes, angle_step_deg)
    logger.info(
        "%s: %d/%d frames selected (step=%.0f°)",
        acquisition_id,
        len(selected),
        len(frame_files),
        angle_step_deg,
    )

    saved_count = 0
    seen_hashes: set[str] = set()

    for frame_path, angle_deg in selected:
        try:
            raw_image = read_b2nd_frame(frame_path)
            img_hash = image_hash(raw_image)

            # Deduplication within acquisition
            if img_hash in seen_hashes:
                continue
            seen_hashes.add(img_hash)

            # Simple preprocessing: resize
            image = preprocess_image(raw_image, target_size)

            # Filename: {acquisition}_{angle:03d}.npy
            angle_int = round(angle_deg) if angle_deg is not None else saved_count
            out_name = f"{acquisition_id}_{angle_int:03d}"
            npy_path = output_dir / f"{out_name}.npy"
            meta_path = output_dir / f"{out_name}.json"

            np.save(str(npy_path), image.astype(np.float32))

            frame_index = extract_frame_index(frame_path.stem)
            metadata = {
                "acquisition_id": acquisition_id,
                "bone_type": bone_type,
                "side": side,
                "region": region,
                "angle_deg": angle_deg,
                "frame_index": frame_index,
                "source_file": frame_path.name,
                "original_shape": list(raw_image.shape),
                "output_shape": list(image.shape),
                "image_hash": img_hash,
            }
            with Path(meta_path).open("w") as f:
                json.dump(metadata, f, indent=2)

            registry.register_frame(
                acquisition_id=acquisition_id,
                frame_index=frame_index,
                angle_deg=angle_deg,
                output_path=str(npy_path),
                image_hash=img_hash,
            )
            saved_count += 1

        except Exception as e:
            logger.warning("Frame %s failed: %s", frame_path.name, e)
            continue

    if saved_count > 0:
        registry.mark_completed(acquisition_id, len(frame_files), saved_count)
    else:
        registry.mark_failed(acquisition_id, "No frames successfully processed")

    return saved_count


def run_ingestion(
    source_root: str | Path | None = None,
    output_root: str | Path = "data/processed",
    angle_step_deg: float = DEFAULT_ANGLE_STEP_DEG,
    target_size: int = 512,
    limit: int = 0,
    db_path: str | Path | None = None,
) -> dict[str, Any]:
    """Run complete incremental ingestion.

    Scans BoneStore, discovers new acquisitions,
    processes pending ones.

    Args:
        source_root: BoneStore NFS mount. If None, uses env var.
        output_root: Local output directory.
        angle_step_deg: Angular step for selection.
        target_size: Output size.
        limit: Max acquisitions to process (0 = all).
        db_path: SQLite database path.

    Returns:
        Dict with ingestion statistics.
    """
    if source_root is None:
        source_root = os.getenv("BONESTORE_ROOT", "/mnt/bonestore")

    source = Path(source_root)
    output = Path(output_root)
    registry = IngestionRegistry(db_path)

    # Phase 1: discovery
    new_count = registry.discover_acquisitions(source)
    logger.info("Discovery phase: %d new acquisitions", new_count)

    # Phase 2: processing
    pending = registry.get_pending(limit=limit)
    logger.info("Processing phase: %d acquisitions pending", len(pending))

    total_frames = 0
    processed_acq = 0
    failed_acq = 0
    train_dir = output / "train"

    for acq in pending:
        acq_id = acq["acquisition_id"]
        acq_dir = Path(acq["source_path"])
        logger.info(
            "Processing [%d/%d]: %s (%s %s %s, %d frames)",
            processed_acq + 1,
            len(pending),
            acq_id,
            acq["bone_type"],
            acq["side"],
            acq["region"],
            acq["total_frames"],
        )

        try:
            saved = ingest_acquisition(
                acq_dir=acq_dir,
                output_dir=train_dir,
                registry=registry,
                acquisition_id=acq_id,
                bone_type=acq["bone_type"],
                side=acq["side"],
                region=acq["region"],
                angle_step_deg=angle_step_deg,
                target_size=target_size,
            )
            total_frames += saved
            processed_acq += 1
        except Exception as e:
            logger.error("Ingestion failed for %s: %s", acq_id, e)
            registry.mark_failed(acq_id, str(e))
            failed_acq += 1

    return {
        "total_acquisitions": len(pending),
        "processed": processed_acq,
        "failed": failed_acq,
        "total_frames": total_frames,
    }


# ========== Async API Wrappers ==========


async def sync_acquisitions() -> dict[str, Any]:
    """Synchronize BoneStore to ingestion registry (async wrapper).

    Returns:
        Sync result with acquisition counts.
    """
    try:
        from src.modules.bonestore.service import list_acquisitions

        # Get acquisitions from BoneStore
        acqs = list_acquisitions()
        registry = IngestionRegistry()

        new_count = 0
        for acq in acqs:
            acq_id = acq.get("id")
            if not registry.is_ingested(acq_id):
                # Register as pending
                registry.add_acquisition(
                    acq_id,
                    status="pending",
                    bone_type=acq.get("bone_type"),
                    side=acq.get("side"),
                    region=acq.get("region"),
                    total_frames=acq.get("frame_count", 0),
                )
                new_count += 1

        pending = registry.get_pending()
        return {
            "status": "success",
            "synced": len(acqs),
            "new": new_count,
            "pending": len(pending),
            "timestamp": __import__("datetime").datetime.utcnow().isoformat(),
        }
    except Exception as e:
        logger.error("Sync failed: %s", e)
        return {
            "status": "error",
            "message": str(e),
        }


async def get_pending_acquisitions(
    limit: int = 100,
    offset: int = 0,
) -> list[dict[str, Any]]:
    """Get pending acquisitions awaiting ingestion.

    Args:
        limit: Max acquisitions to return.
        offset: Pagination offset.

    Returns:
        List of pending acquisition dicts.
    """
    try:
        registry = IngestionRegistry()
        pending = registry.get_pending()
        return pending[offset : offset + limit]
    except Exception as e:
        logger.error("Error fetching pending acquisitions: %s", e)
        return []


async def get_ingestion_status() -> dict[str, Any]:
    """Get overall ingestion status and statistics.

    Returns:
        Ingestion status with registry stats.
    """
    try:
        registry = IngestionRegistry()
        pending = registry.get_pending()
        total = len(registry.db)

        return {
            "status": "ready",
            "total_acquisitions": total,
            "pending": len(pending),
            "last_sync": "2026-08-10T00:00:00Z",  # TODO: track from registry
        }
    except Exception as e:
        logger.error("Error fetching ingestion status: %s", e)
        return {
            "status": "error",
            "message": str(e),
        }
