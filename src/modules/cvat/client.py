"""CVAT REST API client wrapper.

Handles authentication, request routing, and error handling for CVAT operations.
"""

import logging
from typing import Any

import httpx

logger = logging.getLogger(__name__)


class CVATClient:
    """CVAT REST API client (supports v2.x)."""

    def __init__(self, host: str, port: int, username: str, password: str) -> None:
        """Initialize CVAT client.

        Args:
            host: CVAT server host.
            port: CVAT server port.
            username: CVAT username.
            password: CVAT password.
        """
        self.base_url = f"http://{host}:{port}"
        self.api_base = f"{self.base_url}/api"
        self.username = username
        self.password = password
        self.client = None
        logger.info("CVATClient initialized for %s:%d", host, port)

    async def authenticate(self) -> bool:
        """Authenticate with CVAT server via login then use session token."""
        try:
            # Login to get session token
            tmp = httpx.AsyncClient(timeout=30.0)
            resp = await tmp.post(
                f"{self.api_base}/auth/login",
                json={"username": self.username, "password": self.password},
            )
            await tmp.aclose()
            if resp.status_code == 200:
                token = resp.json().get("key", "")
                self.client = httpx.AsyncClient(
                    headers={"Authorization": f"Token {token}"},
                    timeout=30.0,
                )
                logger.info("CVAT authentication successful (token)")
                return True
            logger.error("CVAT authentication failed: %s", resp.status_code)
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
            response = await self.client.get(f"{self.api_base}/tasks?limit={limit}")
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
            response = await self.client.get(f"{self.api_base}/tasks/{task_id}")
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
                f"{self.api_base}/tasks",
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
            response = await self.client.get(f"{self.api_base}/tasks/{task_id}/annotations")
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
                f"{self.api_base}/tasks/{task_id}/annotations",
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

    async def upload_images(
        self,
        task_id: int,
        images: list[tuple[str, bytes]],
    ) -> bool:
        """Upload images to a CVAT task.

        Args:
            task_id: Task ID.
            images: List of (filename, png_bytes) tuples.

        Returns:
            True if successful.
        """
        try:
            if self.client is None:
                return False
            files = [(f"client_files[{i}]", (name, data, "image/png")) for i, (name, data) in enumerate(images)]
            response = await self.client.post(
                f"{self.api_base}/tasks/{task_id}/data",
                files=files,
                data={"image_quality": 95},
                timeout=120.0,
            )
            if response.status_code in (200, 201, 202):
                logger.info("Uploaded %d images to task %d", len(images), task_id)
                return True
            logger.error("Upload failed: %s", response.status_code)
            return False
        except Exception as e:
            logger.error("Error uploading images to task %d: %s", task_id, e)
            return False

    async def set_labels(
        self,
        task_id: int,
        labels: list[dict[str, Any]],
    ) -> bool:
        """Set labels on a CVAT task.

        Args:
            task_id: Task ID.
            labels: List of CVAT label dicts.

        Returns:
            True if successful.
        """
        try:
            if self.client is None:
                return False
            response = await self.client.patch(
                f"{self.api_base}/tasks/{task_id}",
                json={"labels": labels},
            )
            if response.status_code == 200:
                logger.info("Labels set on task %d (%d labels)", task_id, len(labels))
                return True
            logger.error("Set labels failed: %s", response.status_code)
            return False
        except Exception as e:
            logger.error("Error setting labels on task %d: %s", task_id, e)
            return False

    async def get_task_jobs(self, task_id: int) -> list[dict[str, Any]]:
        """Get jobs for a CVAT task (includes assignee info).

        Args:
            task_id: Task ID.

        Returns:
            List of job dicts.
        """
        try:
            if self.client is None:
                return []
            response = await self.client.get(f"{self.api_base}/tasks/{task_id}/jobs")
            if response.status_code == 200:
                data = response.json()
                return data.get("results", data) if isinstance(data, dict) else data
            return []
        except Exception as e:
            logger.error("Error fetching jobs for task %d: %s", task_id, e)
            return []

    async def get_users(self) -> list[dict[str, Any]]:
        """Get all CVAT users."""
        try:
            if self.client is None:
                return []
            response = await self.client.get(f"{self.api_base}/users")
            if response.status_code == 200:
                data = response.json()
                return data.get("results", []) if isinstance(data, dict) else data
            return []
        except Exception as e:
            logger.error("Error fetching users: %s", e)
            return []

    async def close(self) -> None:
        """Close client session."""
        if self.client:
            await self.client.aclose()
