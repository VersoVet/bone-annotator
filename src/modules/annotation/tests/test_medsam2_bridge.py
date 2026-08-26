"""Tests for MedSAM2 mask and frame-index conversions."""

import asyncio
import base64
import io
from pathlib import Path
from unittest.mock import AsyncMock, patch

import numpy as np
from PIL import Image

from src.modules.annotation.medsam2_bridge import (
    _binary_mask_to_rle,
    _cvat_mask_to_binary,
    _cvat_shape_to_binary,
    _get_bone_label_id,
    _propagate_all_frames,
    propagate,
)


def test_cvat_mask_to_binary_restores_crop_offset() -> None:
    """Restore a crop RLE into a full image at its CVAT offset."""
    crop = np.array([[0, 1], [1, 1]], dtype=np.uint8)
    rle = _binary_mask_to_rle(crop)
    shape = {"points": rle[:-4] + [3, 4, 5, 6]}

    result = _cvat_mask_to_binary(shape, (8, 9))

    assert result.shape == (9, 8)
    assert np.array_equal(result[4:6, 3:5], crop)
    assert int(result.sum()) == 3


def test_binary_mask_to_rle_preserves_bounds() -> None:
    """Encode a mask with bounds and decode it back to the crop."""
    mask = np.zeros((6, 7), dtype=np.uint8)
    mask[2:4, 3:6] = 1

    encoded = _binary_mask_to_rle(mask)
    decoded = _cvat_mask_to_binary({"points": encoded}, (7, 6))

    assert np.array_equal(decoded, mask)


def test_shape_and_label_helpers() -> None:
    """Convert primitive CVAT shapes and select an existing label."""
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as directory:
        images_dir = Path(directory)
        Image.new("L", (8, 8), 0).save(images_dir / "000.png")
        rectangle = _cvat_shape_to_binary(
            {"type": "rectangle", "points": [2, 3, 6, 7]},
            images_dir,
        )
        assert int(rectangle.sum()) == 16
        polygon = _cvat_shape_to_binary(
            {"type": "polygon", "points": [1, 1, 6, 1, 1, 6]},
            images_dir,
        )
        assert int(polygon.sum()) > 0
        assert _get_bone_label_id({"shapes": [{"label_id": 9}]}) == 9
        assert _get_bone_label_id({"shapes": []}) == 0


def test_mask_helpers_reject_invalid_or_empty_masks() -> None:
    """Reject malformed crop bounds and empty output masks."""
    assert _binary_mask_to_rle(np.zeros((2, 2), dtype=np.uint8)) == []
    assert _cvat_mask_to_binary({"points": [1, 0, 2, 2, 1]}, (4, 4)) is None


def test_propagation_batches_keep_original_indices(tmp_path: Path) -> None:
    """Process all frames in batches without changing CVAT indices."""
    files = []
    for index in range(5):
        path = tmp_path / f"{index:03d}.png"
        Image.new("L", (2, 2), index).save(path)
        files.append(path)

    mask = base64.b64encode(b"seed").decode()
    responses = [
        {"masks": [mask, mask, mask], "frame_count": 3},
        {"masks": [mask, mask, mask], "frame_count": 3},
    ]

    class Response:
        status_code = 200

        def __init__(self, payload: dict[str, object]) -> None:
            self.payload = payload

        def json(self) -> dict[str, object]:
            return self.payload

        text = ""

    client = AsyncMock()
    client.post.side_effect = [Response(payload) for payload in responses]

    class ClientContext:
        async def __aenter__(self) -> AsyncMock:
            return client

        async def __aexit__(self, *args: object) -> None:
            return None

    async def run() -> dict[int, str]:
        with patch(
            "src.modules.annotation.medsam2_bridge.httpx.AsyncClient",
            return_value=ClientContext(),
        ):
            return await _propagate_all_frames("http://medsam2", files, 2, mask, batch_size=3)

    result = asyncio.run(run())

    assert sorted(result) == [0, 1, 2, 3, 4]
    assert client.post.call_count == 2


def test_propagate_pushes_masks_with_true_frame_indices(tmp_path: Path) -> None:
    """Bridge a complete response back to CVAT without resampling indices."""
    images_dir = tmp_path / "images"
    images_dir.mkdir()
    for index in range(2):
        Image.new("L", (4, 4), 255).save(images_dir / f"{index:03d}.png")
    seed = np.zeros((4, 4), dtype=np.uint8)
    seed[1:3, 1:3] = 1
    seed_rle = _binary_mask_to_rle(seed)
    mask_buffer = io.BytesIO()
    Image.fromarray(seed * 255).save(mask_buffer, format="PNG")
    mask_b64 = base64.b64encode(mask_buffer.getvalue()).decode()

    class FakeCvat:
        async def get_annotations(self, task_id: int) -> dict[str, object]:
            return {"shapes": [{"frame": 0, "type": "mask", "points": seed_rle, "label_id": 7}]}

        async def update_annotations(self, task_id: int, payload: dict[str, object]) -> bool:
            self.payload = payload
            return True

    cvat = FakeCvat()
    task = {"id": 11, "cvat_task_id": 22, "dataset_path": str(tmp_path)}

    async def run() -> dict[str, object]:
        with patch(
            "src.modules.annotation.medsam2_bridge._propagate_all_frames",
            new=AsyncMock(return_value={0: mask_b64, 1: mask_b64}),
        ):
            return await propagate(cvat, task, seed_frame_idx=0)

    result = asyncio.run(run())

    assert result["total_frames"] == 2
    assert [shape["frame"] for shape in cvat.payload["shapes"]] == [0, 1]
