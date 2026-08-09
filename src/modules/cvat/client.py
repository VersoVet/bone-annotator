"""CVAT REST API client wrapper.

Handles authentication, request routing, and error handling for CVAT operations.
"""

import logging
from typing import Any

import httpx

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
        self.client = None
        logger.info("CVATClient initialized for %s:%d", host, port)

    async def authenticate(self) -> bool:
        """Authenticate with CVAT server.

        Returns:
            True if authentication successful.
        """
        try:
            self.client = httpx.AsyncClient(auth=(self.username, self.password), timeout=30.0)
            response = await self.client.get(f"{self.base_url}/api/v1/auth/login")
            if response.status_code == 200:
                logger.info("CVAT authentication successful")
                return True
            logger.error("CVAT authentication failed: %s", response.status_code)
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
            if self.client is None:
                return []
            response = await self.client.get(f"{self.base_url}/api/v1/tasks?limit={limit}")
            if response.status_code == 200:
                data = response.json()
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
            if self.client is None:
                return None
            response = await self.client.get(f"{self.base_url}/api/v1/tasks/{task_id}")
            if response.status_code == 200:
                return response.json()
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
            if self.client is None:
                return None
            payload: dict[str, Any] = {"name": name}
            if project_id:
                payload["project_id"] = project_id

            response = await self.client.post(
                f"{self.base_url}/api/v1/tasks",
                json=payload,
            )
            if response.status_code == 201:
                return response.json()
            logger.error("Error creating task: %s", response.status_code)
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
            if self.client is None:
                return None
            response = await self.client.get(f"{self.base_url}/api/v1/tasks/{task_id}/annotations")
            if response.status_code == 200:
                return response.json()
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
            if self.client is None:
                return False
            response = await self.client.put(
                f"{self.base_url}/api/v1/tasks/{task_id}/annotations",
                json=annotations,
            )
            if response.status_code in (200, 201):
                logger.info("Annotations updated for task %d", task_id)
                return True
            logger.error("Error updating annotations: %s", response.status_code)
            return False
        except Exception as e:
            logger.error("Error updating annotations: %s", e)
            return False

    async def close(self) -> None:
        """Close client session."""
        if self.client:
            await self.client.aclose()
