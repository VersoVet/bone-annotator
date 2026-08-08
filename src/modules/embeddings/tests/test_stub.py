"""Stub tests for embeddings module."""

import pytest


class TestEmbeddingsModule:
    """Tests for embeddings module."""

    def test_import_qdrant_store(self) -> None:
        """Test qdrant_store module import."""
        from ..qdrant_store import BoneAtlasStore

        assert BoneAtlasStore is not None

    def test_service_import(self) -> None:
        """Test service module import."""
        from ..service import EmbeddingsService

        assert EmbeddingsService is not None

    @pytest.mark.asyncio
    async def test_service_status(self) -> None:
        """Test service status."""
        from ..service import get_service

        service = get_service()
        status = await service.status()
        assert status["status"] == "ready"

    def test_bone_atlas_store(self) -> None:
        """Test BoneAtlasStore initialization."""
        from ..qdrant_store import BoneAtlasStore

        store = BoneAtlasStore()
        assert store.collection == "bone_atlas"
        assert store.vector_size == 512
