"""Tests module annotation."""

import pytest


@pytest.mark.asyncio
async def test_get_acquisition_status():
    """Test récupération statut acquisition."""
    from src.modules.annotation.service import get_acquisition_status

    result = await get_acquisition_status("acq_001")
    assert result["acquisition_id"] == "acq_001"
    assert "status" in result
