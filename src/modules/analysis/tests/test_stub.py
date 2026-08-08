"""Stub tests for analysis module."""

import pytest


class TestAnalysisModule:
    """Tests for analysis module."""

    def test_import_bone_density(self) -> None:
        """Test bone_density module import."""
        from ..bone_density import analyze_density_map

        assert analyze_density_map is not None

    def test_import_landmarks(self) -> None:
        """Test landmarks module import."""
        from ..landmarks import normalize_landmarks

        assert normalize_landmarks is not None

    def test_import_conformation(self) -> None:
        """Test conformation module import."""
        from ..conformation import ShapeModel

        assert ShapeModel is not None

    def test_service_import(self) -> None:
        """Test service module import."""
        from ..service import AnalysisService

        assert AnalysisService is not None

    @pytest.mark.asyncio
    async def test_service_status(self) -> None:
        """Test service status."""
        from ..service import get_service

        service = get_service()
        status = await service.status()
        assert status["status"] == "ready"
