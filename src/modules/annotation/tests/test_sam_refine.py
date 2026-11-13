"""Tests for SAM box-prompt refinement."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest
from PIL import Image

from src.modules.annotation.sam_refine import (
    _decode_mask_b64,
    _image_to_base64,
    refine_all_seed_shapes,
    refine_zone_with_sam,
)


@pytest.fixture()
def tmp_png(tmp_path: Path) -> Path:
    """Create a temporary grayscale PNG."""
    img = Image.fromarray(np.random.randint(0, 255, (64, 64), dtype=np.uint8), mode="L")
    p = tmp_path / "frame_0000.png"
    img.save(str(p))
    return p


def test_image_to_base64(tmp_png: Path) -> None:
    """Base64 encoding produces non-empty string."""
    b64 = _image_to_base64(tmp_png)
    assert isinstance(b64, str)
    assert len(b64) > 100


def test_decode_mask_b64_valid() -> None:
    """Valid base64 mask decodes to binary array."""
    import base64
    import io

    mask = np.zeros((32, 32), dtype=np.uint8)
    mask[10:20, 10:20] = 255
    buf = io.BytesIO()
    Image.fromarray(mask, mode="L").save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")

    result = _decode_mask_b64(b64, (32, 32))
    assert result is not None
    assert result.shape == (32, 32)
    assert result[15, 15] == 1
    assert result[0, 0] == 0


def test_decode_mask_b64_invalid() -> None:
    """Invalid base64 returns None."""
    result = _decode_mask_b64("not_valid_base64!!!", (32, 32))
    assert result is None


@pytest.mark.asyncio
async def test_refine_zone_sam_unreachable() -> None:
    """SAM connection error returns None."""
    result = await refine_zone_with_sam(
        "http://127.0.0.1:1",  # unreachable
        "fake_b64",
        [10, 10, 50, 50],
        (64, 64),
        timeout=1.0,
    )
    assert result is None


@pytest.mark.asyncio
async def test_refine_all_sam_down_returns_originals(tmp_png: Path) -> None:
    """When SAM is down, original shapes are returned unchanged."""
    shapes = [
        {"type": "mask", "frame": 0, "label_id": 1, "points": [1.0, 2.0, 0.0, 0.0, 64.0, 64.0]},
    ]
    result = await refine_all_seed_shapes(
        "http://127.0.0.1:1",  # unreachable
        [tmp_png],
        shapes,
    )
    assert len(result) == len(shapes)
    assert result[0]["label_id"] == 1


@pytest.mark.asyncio
async def test_refine_all_empty_shapes() -> None:
    """Empty shape list returns empty."""
    result = await refine_all_seed_shapes("http://unused", [], [])
    assert result == []
