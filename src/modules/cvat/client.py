"""CVAT REST API client wrapper.

Handles authentication, request routing, and error handling for CVAT operations.
"""

import logging
from typing import Any

logger = logging.getLogger(__name__)


class CVATClient:
    """CVAT REST API client."""

    def __init__(self, host: str, port: int, username: str, password: str) -> None:
        """Initialize CVAT client.

        Args:
            host: CVAT server host.
            port: CVAT server port.
            username: CVAT username.
            password: CVAT password.
        """
        self.base_url = f"http://{host}:{port}"
        self.username = username
        self.password = password
        self.session = None
        logger.info("CVATClient initialized for %s:%d", host, port)

    async def authenticate(self) -> bool:
        """Authenticate with CVAT server.

        Returns:
            True if authentication successful.
        """
        try:
            import aiohttp

            self.session = aiohttp.ClientSession()
            auth = aiohttp.BasicAuth(self.username, self.password)
            async with self.session.get(f"{self.base_url}/api/v1/auth/login", auth=auth) as resp:
                if resp.status == 200:
                    logger.info("CVAT authentication successful")
                    return True
                logger.error("CVAT authentication failed: %s", resp.status)
                return False
        except Exception as e:
            logger.error("CVAT authentication error: %s", e)
            return False

    async def get_tasks(self, limit: int = 100) -> list[dict[str, Any]]:
        """Get list of CVAT tasks.

        Args:
            limit: Max tasks to return.

        Returns:
            List of task dicts.
        """
        try:
            if self.session is None:
                return []
            async with self.session.get(f"{self.base_url}/api/v1/tasks?limit={limit}") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get("results", [])
                return []
        except Exception as e:
            logger.error("Error fetching tasks: %s", e)
            return []

    async def get_task(self, task_id: int) -> dict[str, Any] | None:
        """Get task details.

        Args:
            task_id: Task ID.

        Returns:
            Task dict or None.
        """
        try:
            if self.session is None:
                return None
            async with self.session.get(f"{self.base_url}/api/v1/tasks/{task_id}") as resp:
                if resp.status == 200:
                    return await resp.json()
                return None
        except Exception as e:
            logger.error("Error fetching task %d: %s", task_id, e)
            return None

    async def create_task(
        self,
        name: str,
        project_id: int | None = None,
    ) -> dict[str, Any] | None:
        """Create a new CVAT task.

        Args:
            name: Task name.
            project_id: Optional project ID.

        Returns:
            Created task dict or None.
        """
        try:
            if self.session is None:
                return None
            payload: dict[str, Any] = {"name": name}
            if project_id:
                payload["project_id"] = project_id

            async with self.session.post(
                f"{self.base_url}/api/v1/tasks",
                json=payload,
            ) as resp:
                if resp.status == 201:
                    return await resp.json()
                logger.error("Error creating task: %s", resp.status)
                return None
        except Exception as e:
            logger.error("Error creating task: %s", e)
            return None

    async def get_annotations(self, task_id: int) -> dict[str, Any] | None:
        """Get task annotations.

        Args:
            task_id: Task ID.

        Returns:
            Annotations dict or None.
        """
        try:
            if self.session is None:
                return None
            async with self.session.get(f"{self.base_url}/api/v1/tasks/{task_id}/annotations") as resp:
                if resp.status == 200:
                    return await resp.json()
                return None
        except Exception as e:
            logger.error("Error fetching annotations for task %d: %s", task_id, e)
            return None

    async def update_annotations(
        self,
        task_id: int,
        annotations: dict[str, Any],
    ) -> bool:
        """Update task annotations.

        Args:
            task_id: Task ID.
            annotations: Annotation data.

        Returns:
            True if successful.
        """
        try:
            if self.session is None:
                return False
            async with self.session.put(
                f"{self.base_url}/api/v1/tasks/{task_id}/annotations",
                json=annotations,
            ) as resp:
                if resp.status in (200, 201):
                    logger.info("Annotations updated for task %d", task_id)
                    return True
                logger.error("Error updating annotations: %s", resp.status)
                return False
        except Exception as e:
            logger.error("Error updating annotations: %s", e)
            return False

    async def close(self) -> None:
        """Close client session."""
        if self.session:
            await self.session.close()
