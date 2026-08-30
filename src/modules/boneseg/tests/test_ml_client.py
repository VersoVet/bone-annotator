"""Tests for bone-ml API client helpers."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.modules.boneseg.ml_client import DEFAULT_AL_BONE, fetch_al_suggest, fetch_catalog_stats


@pytest.mark.asyncio
async def test_fetch_al_suggest_uses_n_suggest() -> None:
    """AL suggest sends bone-ml compatible body."""
    client = AsyncMock()
    response = MagicMock(status_code=200)
    response.json.return_value = {"suggestions": [{"acquisition_id": "A1"}], "strategy": "hybrid"}
    client.post.return_value = response

    data = await fetch_al_suggest(client, bone_type="humerus", n_suggest=5)
    assert len(data["suggestions"]) == 1
    client.post.assert_called_once()
    body = client.post.call_args.kwargs["json"]
    assert body == {"bone_type": "humerus", "n_suggest": 5}


@pytest.mark.asyncio
async def test_fetch_al_suggest_default_bone() -> None:
    """Default bone type when none provided."""
    client = AsyncMock()
    response = MagicMock(status_code=200)
    response.json.return_value = {"suggestions": []}
    client.post.return_value = response

    await fetch_al_suggest(client, n_suggest=3)
    body = client.post.call_args.kwargs["json"]
    assert body["bone_type"] == DEFAULT_AL_BONE


@pytest.mark.asyncio
@patch("src.modules.boneseg.ml_client.get_bone_ml_config")
async def test_fetch_catalog_stats(mock_cfg: MagicMock) -> None:
    """Catalog stats returns dict from bone-ml."""
    mock_cfg.return_value = {"base_url": "http://bone-ml:9463"}
    client = AsyncMock()
    response = MagicMock(status_code=200)
    response.json.return_value = {"total": 312, "by_status": {"new": 312}}
    client.get.return_value = response

    stats = await fetch_catalog_stats(client)
    assert stats["total"] == 312
