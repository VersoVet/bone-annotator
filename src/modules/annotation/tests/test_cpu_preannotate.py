"""Tests for CPU Otsu pre-annotation helpers."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

from src.modules.annotation.cpu_preannotate import (
    _strip_shape_ids,
    binary_mask_to_rle,
    bone_mask_from_frame,
    build_seed_shapes,
    mask_to_bbox_points,
    otsu_threshold,
    pick_seed_label_id,
    resolve_seed_frames,
)
from src.modules.annotation.ml_bridge import _is_success_status


def test_otsu_threshold_separates_bimodal() -> None:
    """Otsu finds a threshold between two intensity peaks."""
    dark = np.full((80, 80), 30, dtype=np.uint8)
    bright = np.full((80, 80), 220, dtype=np.uint8)
    img = np.concatenate([dark, bright], axis=1)
    thr = otsu_threshold(img)
    assert 30 <= thr <= 220
    assert (img > thr).mean() > 0.2
    assert (img > thr).mean() < 0.8


def test_bone_mask_from_frame(tmp_path: Path) -> None:
    """Bone mask is non-empty on a synthetic fluoro-like PNG."""
    arr = np.zeros((64, 64), dtype=np.uint8)
    arr[16:48, 16:48] = 220
    path = tmp_path / "frame.png"
    Image.fromarray(arr, mode="L").save(path)
    mask = bone_mask_from_frame(path)
    assert mask.shape == (64, 64)
    assert mask.sum() > 0
    bbox = mask_to_bbox_points(mask)
    assert bbox is not None
    assert bbox[2] > bbox[0]


def test_binary_mask_to_rle_roundtrip_bounds() -> None:
    """RLE ends with crop bounds."""
    mask = np.zeros((20, 20), dtype=np.uint8)
    mask[5:15, 4:12] = 1
    rle = binary_mask_to_rle(mask)
    assert len(rle) >= 5
    assert rle[-4:] == [4.0, 5.0, 12.0, 15.0]


def test_pick_seed_label_prefers_diaphyse() -> None:
    """Preferred anatomical zone is selected when present."""
    labels = [
        {"id": 1, "name": "test_zone"},
        {"id": 2, "name": "diaphyse_humerale"},
    ]
    label_id, name = pick_seed_label_id(labels)
    assert label_id == 2
    assert name == "diaphyse_humerale"


def test_ml_success_status_rejects_started() -> None:
    """bone-ml 'started' alone is not treated as success."""
    assert _is_success_status("ok_boneseg") is True
    assert _is_success_status("started") is False
    assert _is_success_status("error:no model") is False
    assert _is_success_status("deferred:gpu_unavailable") is False


def test_resolve_seed_frames_spreads() -> None:
    """Seed indices include endpoints and stay within bounds."""
    frames = resolve_seed_frames(929, 5)
    assert frames[0] == 0
    assert frames[-1] == 928
    assert len(frames) == 5
    assert resolve_seed_frames(3, 5) == [0, 1, 2]


def test_strip_shape_ids_removes_server_fields() -> None:
    """CVAT PUT payload must not retain shape id/elements."""
    cleaned = _strip_shape_ids({"id": 12, "type": "mask", "elements": [], "frame": 0})
    assert "id" not in cleaned
    assert "elements" not in cleaned
    assert cleaned["type"] == "mask"


def test_build_seed_shapes_mask(tmp_path: Path) -> None:
    """build_seed_shapes emits mask RLE for synthetic frames."""
    paths: list[Path] = []
    for i in range(3):
        arr = np.zeros((32, 32), dtype=np.uint8)
        arr[8:24, 8:24] = 200
        p = tmp_path / f"f{i}.png"
        Image.fromarray(arr, mode="L").save(p)
        paths.append(p)
    shapes = build_seed_shapes(paths, [0, 2], label_id=393, use_mask=True)
    assert len(shapes) == 2
    assert shapes[0]["type"] == "mask"
    assert shapes[0]["label_id"] == 393
    assert len(shapes[0]["points"]) >= 5
