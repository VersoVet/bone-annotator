"""Imaging service for frame operations and catalog management.

Orchestrates frame loading, caching, and format conversion.
"""

import logging
from typing import Any

import numpy as np

from .catalog import get_filter_catalog, parse_category
from .imaging import (
    clear_frame_cache,
    frame_to_png,
    get_cache_stats,
    load_frame,
)

logger = logging.getLogger(__name__)


class ImagingService:
    """Service for imaging operations."""

    async def load_frame(self, path: str) -> np.ndarray:
        """Load a frame from file with caching.

        Args:
            path: Path to frame file.

        Returns:
            numpy array.
        """
        return load_frame(path)

    async def frame_to_png(
        self,
        image: np.ndarray,
        size: int = 768,
    ) -> bytes:
        """Convert frame to PNG format.

        Args:
            image: Image array.
            size: Output size in pixels.

        Returns:
            PNG bytes.
        """
        return frame_to_png(image, size)

    async def get_filter_catalog(self) -> dict[str, Any]:
        """Get available imaging filters.

        Returns:
            Catalog of filters.
        """
        return get_filter_catalog()

    async def parse_category(self, dirname: str) -> dict[str, str | None]:
        """Parse bone category from directory name.

        Args:
            dirname: Directory name.

        Returns:
            Dict with bone_type, side, region.
        """
        bone, side, region = parse_category(dirname)
        return {"bone_type": bone, "side": side, "region": region}

    async def clear_cache(self) -> None:
        """Clear all frame caches."""
        clear_frame_cache()

    async def get_cache_stats(self) -> dict[str, int]:
        """Get cache statistics.

        Returns:
            Dict with cache sizes.
        """
        return get_cache_stats()

    async def status(self) -> dict[str, Any]:
        """Get service status.

        Returns:
            Status dict.
        """
        return {
            "status": "ready",
            "cache_stats": await self.get_cache_stats(),
        }


# Module-level instance
_service: ImagingService | None = None


def get_service() -> ImagingService:
    """Get or create the imaging service instance."""
    global _service
    if _service is None:
        _service = ImagingService()
    return _service
