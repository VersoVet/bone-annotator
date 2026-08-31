"""Batch frame processing with imaging-sdk — multi-threaded on Glia.

Reads .b2nd frames, applies imaging pipeline with auto-adjust,
and saves as 16-bit PNG. Uses ThreadPoolExecutor for parallelism.
"""

import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Callable

import blosc2
import numpy as np
from PIL import Image

logger = logging.getLogger(__name__)

# Auto-adjust params cached across frames (recompute every N frames)
_OPTIMIZER_INTERVAL = 30


def _read_b2nd_frame(path: Path) -> np.ndarray:
    """Read a blosc2 compressed frame as numpy array."""
    raw = blosc2.open(str(path))
    data = raw[:]
    if isinstance(data, bytes):
        arr = np.frombuffer(data, dtype=np.uint16)
        side = int(np.sqrt(len(arr)))
        if side * side == len(arr):
            return arr.reshape(side, side)
        return arr
    return np.asarray(data)


def _save_png_16bit(image: np.ndarray, output_path: Path) -> None:
    """Save numpy array as 16-bit PNG."""
    if image.dtype in (np.float32, np.float64):
        image = (np.clip(image, 0, 1) * 65535).astype(np.uint16)
    elif image.dtype != np.uint16:
        image = image.astype(np.uint16)
    pil_img = Image.fromarray(image)
    pil_img.save(str(output_path), format="PNG")


def _process_single_frame(
    frame_path: Path,
    output_dir: Path,
    manager: Any,
    pipeline_dict: dict[str, Any],
    pipeline_preset: str,
    bone_type: str,
    optimized_params: dict[str, dict[str, Any]],
) -> bool:
    """Process a single frame: read, apply pipeline with auto-adjust, save PNG."""
    try:
        raw = _read_b2nd_frame(frame_path)

        from imaging_sdk import get_filter

        result = raw.copy()
        for fspec in pipeline_dict.get("filters", []):
            fname = fspec.get("name", "")
            if not fname or not fspec.get("enabled", True):
                continue
            fobj = get_filter(fname)
            if fobj is None:
                continue
            params = dict(fspec.get("params", {}))
            if fname in optimized_params:
                params.update(optimized_params[fname])
            try:
                if hasattr(fobj, "validate_params"):
                    params = fobj.validate_params(params)
                result = fobj(result, params)
            except Exception as e:
                logger.warning("Filter %s failed on %s: %s", fname, frame_path.name, e)

        out_path = output_dir / f"{frame_path.stem}.png"
        _save_png_16bit(result, out_path)
        return True
    except Exception as e:
        logger.error("Failed to process %s: %s", frame_path.name, e)
        return False


def process_acquisition(
    raw_dir: str,
    pipeline_preset: str,
    pipeline_dir: str,
    output_dir: str,
    bone_type: str = "humerus",
    n_workers: int = 12,
    on_progress: Callable[[int, int], None] | None = None,
) -> dict[str, Any]:
    """Process all .b2nd frames in parallel with imaging-sdk.

    Args:
        raw_dir: Path to directory containing .b2nd files.
        pipeline_preset: Pipeline context name (e.g. os_nu_medsam_user).
        pipeline_dir: Path to imaging-sdk pipeline JSON directory.
        output_dir: Output directory for PNG files.
        bone_type: Bone type for anatomy-aware processing.
        n_workers: Number of parallel workers.
        on_progress: Optional callback(current, total).

    Returns:
        Dict with frame_count, duration, errors.
    """
    import time

    from imaging_sdk import JSONPipelineManager

    t0 = time.monotonic()
    raw_path = Path(raw_dir)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    frame_files = sorted(raw_path.glob("*.b2nd"))
    if not frame_files:
        raise ValueError(f"No .b2nd frames in {raw_dir}")

    total = len(frame_files)
    logger.info("Processing %d frames with %d workers", total, n_workers)

    # Load pipeline config
    manager = JSONPipelineManager(pipeline_dir=Path(pipeline_dir))
    pipeline_dict = manager.load_pipeline(pipeline_preset)
    if not pipeline_dict:
        raise ValueError(f"Pipeline '{pipeline_preset}' not found in {pipeline_dir}")

    # Compute auto-adjust params on first frame
    optimized_params: dict[str, dict[str, Any]] = {}
    try:
        from imaging_sdk.auto_adjust_optimizer import AutoAdjustOptimizer

        sample = _read_b2nd_frame(frame_files[0])
        optimizer = AutoAdjustOptimizer(verbose=False)
        optimized_params = optimizer.optimize(sample, pipeline_dict, {})
        logger.info("Auto-adjust params: %s", optimized_params)
    except Exception as e:
        logger.warning("Auto-adjust failed, using static params: %s", e)

    # Process frames in parallel
    success_count = 0
    error_count = 0

    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        futures = {}
        for i, fp in enumerate(frame_files):
            # Re-compute auto-adjust every N frames
            if i > 0 and i % _OPTIMIZER_INTERVAL == 0:
                try:
                    sample = _read_b2nd_frame(fp)
                    optimized_params = optimizer.optimize(sample, pipeline_dict, {})
                except Exception:
                    pass  # Keep previous params

            future = executor.submit(
                _process_single_frame,
                fp, out_path, manager, pipeline_dict,
                pipeline_preset, bone_type, optimized_params,
            )
            futures[future] = i

        for future in as_completed(futures):
            idx = futures[future]
            if future.result():
                success_count += 1
            else:
                error_count += 1
            done = success_count + error_count
            if on_progress and (done % 20 == 0 or done == total):
                on_progress(done, total)

    duration = time.monotonic() - t0
    logger.info("Done: %d/%d frames in %.1fs (%.0f ms/frame)",
                success_count, total, duration, duration / max(total, 1) * 1000)

    return {
        "frame_count": success_count,
        "total_frames": total,
        "errors": error_count,
        "duration_seconds": round(duration, 2),
        "ms_per_frame": round(duration / max(total, 1) * 1000, 1),
        "pipeline_config": pipeline_dict.get("filters", []),
    }
