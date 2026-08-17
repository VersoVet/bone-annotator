"""CVAT service orchestrator.

Manages CVAT client, synchronization, and annotation workflow.
"""

import logging
from typing import Any

from .client import CVATClient
from .sync import CVATSync

logger = logging.getLogger(__name__)


class CVATService:
    """Service for CVAT integration."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 8080,
        username: str = "admin",
        password: str = "password",
    ) -> None:
        """Initialize CVAT service.

        Args:
            host: CVAT server host.
            port: CVAT server port.
            username: CVAT username.
            password: CVAT password.
        """
        self.client = CVATClient(host, port, username, password)
        self.sync = CVATSync(self.client)
        self.authenticated = False
        logger.info("CVATService initialized for %s:%d", host, port)

    async def connect(self) -> bool:
        """Connect and authenticate with CVAT.

        Returns:
            True if successful.
        """
        self.authenticated = await self.client.authenticate()
        return self.authenticated

    async def disconnect(self) -> None:
        """Disconnect from CVAT."""
        await self.client.close()

    async def get_tasks(self, limit: int = 100) -> list[dict[str, Any]]:
        """Get CVAT tasks.

        Args:
            limit: Max tasks to return.

        Returns:
            List of task dicts.
        """
        if not self.authenticated:
            logger.warning("Not authenticated with CVAT")
            return []
        return await self.client.get_tasks(limit)

    async def get_task(self, task_id: int) -> dict[str, Any] | None:
        """Get task details.

        Args:
            task_id: Task ID.

        Returns:
            Task dict or None.
        """
        if not self.authenticated:
            return None
        return await self.client.get_task(task_id)

    async def create_task(
        self,
        name: str,
        project_id: int | None = None,
    ) -> dict[str, Any] | None:
        """Create a task.

        Args:
            name: Task name.
            project_id: Optional project ID.

        Returns:
            Created task dict or None.
        """
        if not self.authenticated:
            return None
        return await self.client.create_task(name, project_id)

    async def pull_annotations(self, task_id: int) -> dict[str, Any] | None:
        """Pull annotations from CVAT.

        Args:
            task_id: Task ID.

        Returns:
            Annotations or None.
        """
        if not self.authenticated:
            return None
        return await self.sync.pull_annotations(task_id)

    async def push_annotations(
        self,
        task_id: int,
        annotations: dict[str, Any],
    ) -> bool:
        """Push annotations to CVAT.

        Args:
            task_id: Task ID.
            annotations: Annotations to push.

        Returns:
            True if successful.
        """
        if not self.authenticated:
            return False
        return await self.sync.push_annotations(task_id, annotations)

    async def sync_annotations(
        self,
        task_id: int,
        local_annotations: dict[str, Any],
        strategy: str = "local_wins",
    ) -> dict[str, Any] | None:
        """Synchronize annotations.

        Args:
            task_id: Task ID.
            local_annotations: Local annotations.
            strategy: Sync strategy.

        Returns:
            Resolved annotations or None.
        """
        if not self.authenticated:
            return None
        return await self.sync.sync_bidirectional(task_id, local_annotations, strategy)

    async def status(self) -> dict[str, Any]:
        """Get service status.

        Returns:
            Status dict.
        """
        return {
            "status": "connected" if self.authenticated else "disconnected",
            "authenticated": self.authenticated,
        }


# Module-level instance
_service: CVATService | None = None


def get_service() -> CVATService:
    """Get or create the CVAT service instance (config from src.config)."""
    global _service
    if _service is None:
        from src.config import get_cvat_config

        cfg = get_cvat_config()
        _service = CVATService(cfg["host"], cfg["port"], cfg["username"], cfg["password"])
    return _service
