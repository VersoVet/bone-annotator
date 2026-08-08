"""Pseudo-label service for automatic training label generation.

Generates training labels from image analysis for density and landmark detection.
"""

import logging
from typing import Any

import numpy as np

from .generators import generate_density_mask

logger = logging.getLogger(__name__)


class PseudoLabelService:
    """Service for pseudo-label generation."""

    async def generate_density_labels(
        self,
        image_float: np.ndarray,
        bone_mask: np.ndarray,
        n_clusters: int = 3,
        use_spatial_prior: bool = True,
    ) -> np.ndarray:
        """Generate density segmentation pseudo-labels.

        Args:
            image_float: Normalized [0,1] image.
            bone_mask: Binary mask.
            n_clusters: Number of clusters.
            use_spatial_prior: Use anatomical prior.

        Returns:
            Label mask.
        """
        return generate_density_mask(image_float, bone_mask, n_clusters, use_spatial_prior)

    async def compute_density_stats(
        self,
        image_float: np.ndarray,
        density_mask: np.ndarray,
    ) -> dict[str, float]:
        """Compute density statistics from segmented image.

        Args:
            image_float: Image array.
            density_mask: Density segmentation mask.

        Returns:
            Dict of statistics.
        """
        bone_area = np.sum(density_mask > 0)
        if bone_area == 0:
            return {
                "cortical_ratio": 0.0,
                "spongy_ratio": 0.0,
                "medullary_ratio": 0.0,
                "mean_cortical_intensity": 0.0,
                "mean_spongy_intensity": 0.0,
                "mean_medullary_intensity": 0.0,
            }

        stats: dict[str, float] = {}
        for cls, name in [(1, "cortical"), (2, "spongy"), (3, "medullary")]:
            mask = density_mask == cls
            count = np.sum(mask)
            stats[f"{name}_ratio"] = float(count / bone_area)
            if count > 0:
                # Scale back to uint16 range for intensity
                stats[f"mean_{name}_intensity"] = float(np.mean(image_float[mask]) * 65535)
            else:
                stats[f"mean_{name}_intensity"] = 0.0

        return stats

    async def batch_generate_labels(
        self,
        images: list[np.ndarray],
        masks: list[np.ndarray],
    ) -> list[np.ndarray]:
        """Generate labels for multiple images.

        Args:
            images: List of image arrays.
            masks: List of bone masks.

        Returns:
            List of label masks.
        """
        labels: list[np.ndarray] = []
        for img, mask in zip(images, masks, strict=False):
            label = await self.generate_density_labels(img, mask)
            labels.append(label)
        return labels

    async def status(self) -> dict[str, Any]:
        """Get service status.

        Returns:
            Status dict.
        """
        return {"status": "ready"}
