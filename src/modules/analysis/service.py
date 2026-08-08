"""Analysis service orchestrator.

Coordinates bone density analysis, landmark extraction, and conformation analysis.
"""

import logging
from typing import Any

import numpy as np

from .bone_density import analyze_density_map, detect_density_anomalies
from .conformation import ConformationAnalyzer
from .landmarks import compute_bone_axis_from_landmarks

logger = logging.getLogger(__name__)


class AnalysisService:
    """Orchestrates analysis modules for bone specimens."""

    def __init__(self, models_dir: str | None = None) -> None:
        self.conformation = ConformationAnalyzer(models_dir)
        logger.info("AnalysisService initialized")

    async def analyze_density(
        self,
        density_mask: np.ndarray,
        image_float: np.ndarray,
    ) -> dict[str, Any]:
        """Analyze bone density from segmentation mask.

        Args:
            density_mask: Segmentation mask (0=bg, 1=cortical, etc).
            image_float: Normalized [0,1] image.

        Returns:
            Density analysis results.
        """
        return analyze_density_map(density_mask, image_float)

    async def analyze_conformation(
        self,
        bone_type: str,
        landmarks: list[dict],
        image_size: int = 512,
    ) -> dict[str, Any]:
        """Analyze bone conformation from landmarks.

        Args:
            bone_type: Type of bone.
            landmarks: List of landmark dicts.
            image_size: Image coordinate space.

        Returns:
            Conformation analysis results.
        """
        return self.conformation.analyze(bone_type, landmarks, image_size)

    async def detect_anomalies(
        self,
        density_stats: dict,
        reference_stats: dict | None = None,
    ) -> list[dict[str, Any]]:
        """Detect density anomalies.

        Args:
            density_stats: Density statistics.
            reference_stats: Reference population statistics.

        Returns:
            List of anomalies.
        """
        return detect_density_anomalies(density_stats, reference_stats)

    async def analyze_bone_axis(
        self,
        landmarks: list[dict],
        bone_type: str,
    ) -> dict[str, Any] | None:
        """Compute principal bone axis from landmarks.

        Args:
            landmarks: List of landmark dicts.
            bone_type: Type of bone.

        Returns:
            Axis information or None if insufficient landmarks.
        """
        return compute_bone_axis_from_landmarks(landmarks, bone_type)

    async def status(self) -> dict[str, Any]:
        """Get service status.

        Returns:
            Status dict with model information.
        """
        return {
            "status": "ready",
            "conformation_models": list(self.conformation.models.keys()),
        }


# Module-level instance
_service: AnalysisService | None = None


def get_service(models_dir: str | None = None) -> AnalysisService:
    """Get or create the analysis service instance."""
    global _service
    if _service is None:
        _service = AnalysisService(models_dir)
    return _service
