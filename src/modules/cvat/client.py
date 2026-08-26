"""CVAT REST API client wrapper.

Handles authentication, request routing, and error handling for CVAT operations.
"""

import asyncio
import logging
from contextlib import ExitStack
from pathlib import Path
from typing import Any, BinaryIO

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
        """Get list of CVAT tasks."""
        try:
            if self.client is None:
                return []
            response = await self.client.get(f"{self.api_base}/tasks?limit={limit}")
            if response.status_code == 200:
                return response.json().get("results", [])
            return []
        except Exception as e:
            logger.error("Error fetching tasks: %s", e)
            return []

    async def get_task(self, task_id: int) -> dict[str, Any] | None:
        """Get task details by ID."""
        try:
            if self.client is None:
                return None
            response = await self.client.get(f"{self.api_base}/tasks/{task_id}")
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            logger.error("Error fetching task %d: %s", task_id, e)
            return None

    async def create_task(self, name: str, project_id: int | None = None) -> dict[str, Any] | None:
        """Create a new CVAT task, optionally in a project."""
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
        """Get task annotations."""
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

    async def update_annotations(self, task_id: int, annotations: dict[str, Any]) -> bool:
        """Update task annotations."""
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

    async def upload_images(self, task_id: int, images: list[tuple[str, bytes]]) -> bool:
        """Upload images to a CVAT task."""
        try:
            if self.client is None:
                return False
            files = [
                (f"client_files[{index}]", (name, data, "image/png"))
                for index, (name, data) in enumerate(images)
            ]
            return await self._post_image_files(task_id, files, len(images))
        except Exception as e:
            logger.error("Error uploading images to task %d: %s", task_id, e)
            return False

    async def upload_image_paths(self, task_id: int, image_paths: list[Path]) -> bool:
        """Upload images directly from disk without buffering them in memory.

        Args:
            task_id: CVAT task ID.
            image_paths: PNG files to upload.

        Returns:
            True when CVAT accepts the upload.
        """
        if self.client is None:
            return False
        try:
            batch_size = 50
            for batch_start in range(0, len(image_paths), batch_size):
                batch = image_paths[batch_start : batch_start + batch_size]
                with ExitStack() as stack:
                    files = [
                        (
                            f"client_files[{index}]",
                            (path.name, stack.enter_context(path.open("rb")), "image/png"),
                        )
                        for index, path in enumerate(batch)
                    ]
                    if not await self._post_image_files(task_id, files, len(batch)):
                        return False
                if not await self._wait_for_task_size(task_id, batch_start + len(batch)):
                    return False
            return True
        except Exception as e:
            logger.error("Error uploading image files to task %d: %s", task_id, e)
            return False

    async def _post_image_files(
        self,
        task_id: int,
        files: list[tuple[str, tuple[str, bytes | BinaryIO, str]]],
        image_count: int,
    ) -> bool:
        """Send a prepared multipart image request to CVAT."""
        if self.client is None:
            return False
        response = await self.client.post(
            f"{self.api_base}/tasks/{task_id}/data",
            files=files,
            data={"image_quality": 95},
            timeout=300.0,
        )
        if response.status_code in (200, 201, 202):
            logger.info("Uploaded %d images to task %d", image_count, task_id)
            return True
        logger.error("Upload failed: %s", response.status_code)
        return False

    async def _wait_for_task_size(self, task_id: int, expected_size: int) -> bool:
        """Wait until CVAT finishes processing an asynchronous upload batch."""
        for _ in range(180):
            task = await self.get_task(task_id)
            if task and int(task.get("size") or 0) >= expected_size:
                return True
            await asyncio.sleep(2.0)
        logger.error("Timed out waiting for CVAT task %d to reach size %d", task_id, expected_size)
        return False

    async def set_labels(self, task_id: int, labels: list[dict[str, Any]]) -> bool:
        """Set labels on a CVAT task."""
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
        """Get jobs for a CVAT task (includes assignee info)."""
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

    async def get_projects(self) -> list[dict[str, Any]]:
        """List all CVAT projects."""
        try:
            if self.client is None:
                return []
            response = await self.client.get(f"{self.api_base}/projects?page_size=100")
            if response.status_code == 200:
                return response.json().get("results", [])
            return []
        except Exception as e:
            logger.error("Error fetching projects: %s", e)
            return []

    async def get_or_create_project(
        self,
        bone_type: str,
        labels: list[dict[str, Any]],
    ) -> int | None:
        """Get or create a CVAT project for a bone type.

        Args:
            bone_type: Bone type (used as project name: bone_{type}).
            labels: CVAT labels to set on creation.

        Returns:
            Project ID, or None if failed.
        """
        project_name = f"bone_{bone_type}"
        try:
            if self.client is None:
                return None
            # Search existing
            resp = await self.client.get(f"{self.api_base}/projects?search={project_name}")
            if resp.status_code == 200:
                for p in resp.json().get("results", []):
                    if p.get("name") == project_name:
                        return p["id"]
            # Create new
            resp = await self.client.post(
                f"{self.api_base}/projects",
                json={"name": project_name, "labels": labels},
            )
            if resp.status_code == 201:
                pid = resp.json()["id"]
                logger.info("Created CVAT project %s (id=%d)", project_name, pid)
                return pid
            logger.error("Failed to create project %s: %s", project_name, resp.status_code)
            return None
        except Exception as e:
            logger.error("Error in get_or_create_project: %s", e)
            return None

    async def sync_project_labels(
        self,
        project_id: int,
        labels: list[dict[str, Any]],
    ) -> int:
        """Sync labels on a CVAT project (add-only, never delete).

        Args:
            project_id: CVAT project ID.
            labels: Desired labels from label-generator.

        Returns:
            Number of labels added.
        """
        try:
            if self.client is None:
                return 0
            resp = await self.client.get(f"{self.api_base}/projects/{project_id}")
            if resp.status_code != 200:
                return 0
            existing = {lbl["name"] for lbl in resp.json().get("labels", [])}
            new_labels = [lbl for lbl in labels if lbl["name"] not in existing]
            if not new_labels:
                return 0
            # PATCH: add new labels to existing
            all_labels = resp.json().get("labels", []) + new_labels
            await self.client.patch(
                f"{self.api_base}/projects/{project_id}",
                json={"labels": all_labels},
            )
            logger.info("Added %d labels to project %d", len(new_labels), project_id)
            return len(new_labels)
        except Exception as e:
            logger.error("Error syncing project labels: %s", e)
            return 0

    async def close(self) -> None:
        """Close client session."""
        if self.client:
            await self.client.aclose()
