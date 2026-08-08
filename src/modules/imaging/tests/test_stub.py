"""Stub tests for imaging module."""

import pytest


class TestImagingModule:
    """Tests for imaging module."""

    def test_import_frame_cache(self) -> None:
        """Test frame_cache module import."""
        from ..frame_cache import LRUCache

        assert LRUCache is not None

    def test_import_imaging(self) -> None:
        """Test imaging module import."""
        from ..imaging import load_frame

        assert load_frame is not None

    def test_import_catalog(self) -> None:
        """Test catalog module import."""
        from ..catalog import get_filter_catalog

        assert get_filter_catalog is not None

    def test_service_import(self) -> None:
        """Test service module import."""
        from ..service import ImagingService

        assert ImagingService is not None

    @pytest.mark.asyncio
    async def test_service_status(self) -> None:
        """Test service status."""
        from ..service import get_service

        service = get_service()
        status = await service.status()
        assert status["status"] == "ready"
