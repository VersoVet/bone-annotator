"""LRU frame cache for imaging operations.

Thread-safe cache for raw and processed image frames.
"""

import logging
from collections import OrderedDict

logger = logging.getLogger(__name__)


class LRUCache:
    """Thread-safe LRU cache for frame data.

    Args:
        maxsize: Maximum number of cached items.
    """

    def __init__(self, maxsize: int = 100) -> None:
        self._cache: OrderedDict = OrderedDict()
        self._maxsize = maxsize

    def get(self, key: str) -> object | None:
        """Get an item from cache.

        Args:
            key: Cache key.

        Returns:
            Cached value or None if not found.
        """
        if key in self._cache:
            self._cache.move_to_end(key)
            return self._cache[key]
        return None

    def put(self, key: str, value: object) -> None:
        """Insert an item into cache.

        Args:
            key: Cache key.
            value: Value to store.
        """
        if key in self._cache:
            self._cache.move_to_end(key)
        else:
            if len(self._cache) >= self._maxsize:
                self._cache.popitem(last=False)
        self._cache[key] = value

    @property
    def size(self) -> int:
        """Get current cache size."""
        return len(self._cache)

    def clear(self) -> None:
        """Clear all cached items."""
        self._cache.clear()
