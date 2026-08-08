"""CVAT annotation synchronization.

Manages bidirectional sync of annotations between local storage and CVAT.
"""

import logging
from typing import Any

from .client import CVATClient
from .format import convert_from_cvat_xml, convert_to_cvat_xml

logger = logging.getLogger(__name__)


class CVATSync:
    """Manages synchronization with CVAT server."""

    def __init__(self, client: CVATClient) -> None:
        """Initialize synchronizer.

        Args:
            client: CVATClient instance.
        """
        self.client = client
        self.local_state: dict[int, dict[str, Any]] = {}

    async def pull_annotations(self, task_id: int) -> dict[str, Any] | None:
        """Pull annotations from CVAT.

        Args:
            task_id: CVAT task ID.

        Returns:
            Converted annotations or None.
        """
        try:
            annotations = await self.client.get_annotations(task_id)
            if annotations is None:
                return None

            # Store raw for change tracking
            self.local_state[task_id] = annotations

            # Convert to internal format
            return convert_from_cvat_xml(annotations.get("data", ""))
        except Exception as e:
            logger.error("Error pulling annotations for task %d: %s", task_id, e)
            return None

    async def push_annotations(
        self,
        task_id: int,
        annotations: dict[str, Any],
    ) -> bool:
        """Push annotations to CVAT.

        Args:
            task_id: CVAT task ID.
            annotations: Internal annotations.

        Returns:
            True if successful.
        """
        try:
            # Convert to CVAT format
            cvat_xml = convert_to_cvat_xml(annotations)

            # Push to server
            cvat_format = {"data": cvat_xml}
            success = await self.client.update_annotations(task_id, cvat_format)

            if success:
                self.local_state[task_id] = cvat_format
                logger.info("Annotations pushed for task %d", task_id)

            return success
        except Exception as e:
            logger.error("Error pushing annotations for task %d: %s", task_id, e)
            return False

    async def sync_bidirectional(
        self,
        task_id: int,
        local_annotations: dict[str, Any],
        strategy: str = "local_wins",
    ) -> dict[str, Any] | None:
        """Synchronize local and CVAT annotations.

        Args:
            task_id: CVAT task ID.
            local_annotations: Local annotation state.
            strategy: Conflict resolution ('local_wins', 'remote_wins', 'merge').

        Returns:
            Resolved annotations or None.
        """
        try:
            # Get remote state
            remote = await self.pull_annotations(task_id)
            if remote is None:
                logger.warning("Could not fetch remote annotations for task %d", task_id)
                return local_annotations

            # Check for conflicts
            if strategy == "local_wins":
                result = local_annotations
            elif strategy == "remote_wins":
                result = remote
            elif strategy == "merge":
                result = self._merge_annotations(local_annotations, remote)
            else:
                logger.warning("Unknown sync strategy: %s", strategy)
                result = local_annotations

            # Push resolved state
            await self.push_annotations(task_id, result)
            return result
        except Exception as e:
            logger.error("Error in bidirectional sync: %s", e)
            return local_annotations

    def _merge_annotations(
        self,
        local: dict[str, Any],
        remote: dict[str, Any],
    ) -> dict[str, Any]:
        """Merge local and remote annotations.

        Args:
            local: Local annotations.
            remote: Remote annotations.

        Returns:
            Merged annotations.
        """
        try:
            merged: dict[str, Any] = {"images": []}

            # Get all image IDs
            local_imgs = {img.get("id"): img for img in local.get("images", [])}
            remote_imgs = {img.get("id"): img for img in remote.get("images", [])}

            all_ids = set(local_imgs.keys()) | set(remote_imgs.keys())

            for img_id in all_ids:
                local_img = local_imgs.get(img_id, {})
                remote_img = remote_imgs.get(img_id, {})

                if img_id in local_imgs and img_id in remote_imgs:
                    # Image in both: merge shapes and landmarks
                    merged_img = {
                        "id": img_id,
                        "name": local_img.get("name") or remote_img.get("name"),
                        "width": local_img.get("width") or remote_img.get("width"),
                        "height": local_img.get("height") or remote_img.get("height"),
                        "shapes": self._merge_lists(
                            local_img.get("shapes", []),
                            remote_img.get("shapes", []),
                        ),
                        "landmarks": self._merge_lists(
                            local_img.get("landmarks", []),
                            remote_img.get("landmarks", []),
                        ),
                    }
                    merged["images"].append(merged_img)
                elif img_id in local_imgs:
                    # Image only in local
                    merged["images"].append(local_img)
                else:
                    # Image only in remote
                    merged["images"].append(remote_img)

            return merged
        except Exception as e:
            logger.error("Error merging annotations: %s", e)
            return local

    def _merge_lists(
        self,
        local_list: list,
        remote_list: list,
    ) -> list:
        """Merge two lists (simple union).

        Args:
            local_list: Local list.
            remote_list: Remote list.

        Returns:
            Merged list.
        """
        # Simple strategy: keep all from both
        merged = list(local_list)
        for item in remote_list:
            if item not in merged:
                merged.append(item)
        return merged
