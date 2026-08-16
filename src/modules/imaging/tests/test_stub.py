"""Tests for imaging module — frame cache, catalog, PNG conversion."""

import numpy as np
import pytest


class TestLRUCache:
    """Tests for LRU frame cache."""

    def test_put_and_get(self) -> None:
        """Test basic cache put/get."""
        from ..frame_cache import LRUCache

        cache = LRUCache(maxsize=3)
        cache.put("a", 1)
        assert cache.get("a") == 1

    def test_cache_miss_returns_none(self) -> None:
        """Test cache miss returns None."""
        from ..frame_cache import LRUCache

        cache = LRUCache(maxsize=3)
        assert cache.get("missing") is None

    def test_eviction_on_full(self) -> None:
        """Test LRU eviction when cache is full."""
        from ..frame_cache import LRUCache

        cache = LRUCache(maxsize=2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)  # Should evict "a"
        assert cache.get("a") is None
        assert cache.get("b") == 2
        assert cache.get("c") == 3

    def test_access_refreshes_lru_order(self) -> None:
        """Test that accessing an item moves it to end (prevents eviction)."""
        from ..frame_cache import LRUCache

        cache = LRUCache(maxsize=2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.get("a")  # Refresh "a"
        cache.put("c", 3)  # Should evict "b", not "a"
        assert cache.get("a") == 1
        assert cache.get("b") is None

    def test_size_property(self) -> None:
        """Test size property reflects current cache size."""
        from ..frame_cache import LRUCache

        cache = LRUCache(maxsize=5)
        assert cache.size == 0
        cache.put("a", 1)
        assert cache.size == 1
        cache.put("b", 2)
        assert cache.size == 2

    def test_clear(self) -> None:
        """Test clear empties the cache."""
        from ..frame_cache import LRUCache

        cache = LRUCache(maxsize=5)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.clear()
        assert cache.size == 0
        assert cache.get("a") is None

    def test_update_existing_key(self) -> None:
        """Test updating an existing key replaces value."""
        from ..frame_cache import LRUCache

        cache = LRUCache(maxsize=3)
        cache.put("a", 1)
        cache.put("a", 99)
        assert cache.get("a") == 99
        assert cache.size == 1


class TestCatalog:
    """Tests for bone category parsing."""

    def test_parse_full_category(self) -> None:
        """Test parsing a complete category directory name."""
        from ..catalog import parse_category

        bone, side, region = parse_category("001^humerus_left_proximal")
        assert bone == "humerus"
        assert side == "left"
        assert region == "proximal"

    def test_parse_right_distal(self) -> None:
        """Test parsing right distal femur."""
        from ..catalog import parse_category

        bone, side, region = parse_category("femur_right_distal")
        assert bone == "femur"
        assert side == "right"
        assert region == "distal"

    def test_parse_unknown_bone(self) -> None:
        """Test parsing unrecognized bone returns None."""
        from ..catalog import parse_category

        bone, side, region = parse_category("042^mystery_left")
        assert bone is None
        assert side == "left"
        assert region == "entire"

    def test_parse_minimal_name(self) -> None:
        """Test parsing minimal directory name."""
        from ..catalog import parse_category

        bone, side, region = parse_category("radius")
        assert bone == "radius"
        assert side == "unknown"
        assert region == "entire"

    def test_parse_with_caret_prefix(self) -> None:
        """Test that caret prefix is stripped correctly."""
        from ..catalog import parse_category

        bone, side, _ = parse_category("123^ulna_bilateral")
        assert bone == "ulna"
        assert side == "bilateral"


class TestPngConversion:
    """Tests for frame to PNG conversion."""

    def test_uint16_to_png(self) -> None:
        """Test uint16 image produces valid PNG bytes."""
        from ..imaging import frame_to_png

        image = np.random.randint(0, 65535, size=(100, 100), dtype=np.uint16)
        png = frame_to_png(image, size=64)
        assert isinstance(png, bytes)
        assert png[:4] == b"\x89PNG"

    def test_float_to_png(self) -> None:
        """Test float32 image produces valid PNG bytes."""
        from ..imaging import frame_to_png

        image = np.random.rand(100, 100).astype(np.float32)
        png = frame_to_png(image, size=64)
        assert isinstance(png, bytes)
        assert png[:4] == b"\x89PNG"

    def test_zeros_image(self) -> None:
        """Test all-zero uint16 image does not crash."""
        from ..imaging import frame_to_png

        image = np.zeros((50, 50), dtype=np.uint16)
        png = frame_to_png(image, size=32)
        assert isinstance(png, bytes)
        assert len(png) > 0


class TestFrameIndex:
    """Tests for frame index extraction."""

    def test_extract_numeric_suffix(self) -> None:
        """Test extracting frame index from numeric suffix."""
        from ..imaging import _extract_frame_index

        assert _extract_frame_index("frame_042") == 42

    def test_extract_no_number(self) -> None:
        """Test extracting from non-numeric stem returns 0."""
        from ..imaging import _extract_frame_index

        assert _extract_frame_index("nodigits") == 0

    def test_extract_multiple_numbers(self) -> None:
        """Test last numeric part is returned."""
        from ..imaging import _extract_frame_index

        assert _extract_frame_index("acq_001_frame_007") == 7


class TestImagingService:
    """Tests for ImagingService wrapper."""

    @pytest.mark.asyncio
    async def test_service_status(self) -> None:
        """Test service status returns ready."""
        from ..service import get_service

        service = get_service()
        status = await service.status()
        assert status["status"] == "ready"
        assert "cache_stats" in status

    @pytest.mark.asyncio
    async def test_parse_category_via_service(self) -> None:
        """Test category parsing through service layer."""
        from ..service import get_service

        service = get_service()
        result = await service.parse_category("001^humerus_left_proximal")
        assert result["bone_type"] == "humerus"
        assert result["side"] == "left"

    @pytest.mark.asyncio
    async def test_cache_stats_via_service(self) -> None:
        """Test cache stats through service layer."""
        from ..service import get_service

        service = get_service()
        stats = await service.get_cache_stats()
        assert "raw_cache_size" in stats
        assert "processed_cache_size" in stats
