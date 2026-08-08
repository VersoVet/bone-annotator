"""Stub tests for CVAT module."""

import pytest


class TestCVATModule:
    """Tests for CVAT module."""

    def test_import_client(self) -> None:
        """Test client module import."""
        from ..client import CVATClient

        assert CVATClient is not None

    def test_import_sync(self) -> None:
        """Test sync module import."""
        from ..sync import CVATSync

        assert CVATSync is not None

    def test_import_format(self) -> None:
        """Test format module import."""
        from ..format import convert_to_cvat_xml

        assert convert_to_cvat_xml is not None

    def test_service_import(self) -> None:
        """Test service module import."""
        from ..service import CVATService

        assert CVATService is not None

    @pytest.mark.asyncio
    async def test_service_status(self) -> None:
        """Test service status."""
        from ..service import get_service

        service = get_service()
        status = await service.status()
        assert "status" in status
