"""REST client for Orthanc PACS server to fetch DICOM bone images.

Provides study/series/instance discovery and DICOM image retrieval.
"""

import io
import logging
import os
from dataclasses import dataclass
from typing import Any

import httpx
import numpy as np

logger = logging.getLogger(__name__)

# Mapping French labels to English
BONE_MAP_FR = {
    "humerus": "humerus",
    "humérus": "humerus",
    "radius": "radius",
    "ulna": "ulna",
    "cubitus": "ulna",
    "femur": "femur",
    "fémur": "femur",
    "scapula": "scapula",
    "omoplate": "scapula",
    "tibia": "tibia",
}
SIDE_MAP_FR = {
    "gauche": "left",
    "left": "left",
    "g": "left",
    "droit": "right",
    "right": "right",
    "d": "right",
}
REGION_MAP_FR = {
    "proximal": "proximal",
    "prox": "proximal",
    "distal": "distal",
    "dist": "distal",
    "diaphyse": "diaphysis",
    "diaphysis": "diaphysis",
}


@dataclass
class BoneStudy:
    """Represents a bone study from Orthanc PACS.

    Attributes:
        study_id: Study identifier.
        species: Animal species.
        bone_type: Type of bone.
        side: Anatomical side (left, right, bilateral).
        region: Anatomical region.
        description: Study description.
        date: Study date.
        series_ids: List of series IDs.
    """

    study_id: str
    species: str
    bone_type: str
    side: str
    region: str
    description: str
    date: str = ""
    series_ids: list[str] | None = None

    def __post_init__(self) -> None:
        """Post-init processing."""
        if self.series_ids is None:
            self.series_ids = []


@dataclass
class BoneInstance:
    """Represents a single DICOM instance within a bone series.

    Attributes:
        instance_id: Instance identifier.
        series_id: Parent series ID.
        study_id: Parent study ID.
        index_in_series: Position in series.
        total_in_series: Total instances in series.
    """

    instance_id: str
    series_id: str
    study_id: str
    index_in_series: int
    total_in_series: int

    @property
    def angle_degrees(self) -> float:
        """Compute rotation angle in degrees based on series position.

        Returns:
            Angle in degrees.
        """
        if self.total_in_series <= 1:
            return 0.0
        return (self.index_in_series / self.total_in_series) * 360.0

    @property
    def angle_radians(self) -> float:
        """Compute rotation angle in radians.

        Returns:
            Angle in radians.
        """
        return np.radians(self.angle_degrees)


def _parse_description(desc: str) -> dict[str, str]:
    """Parse study/series description to extract bone metadata.

    Supports multiple formats:
      - "Bone Research - Humerus Right Proximal"
      - "chien_Humerus_droit_proximal_Rotation360_20241018"

    Args:
        desc: Description string.

    Returns:
        Dict {species, bone_type, side, region}.
    """
    # Normalize: lowercase, split on any separator
    normalized = desc.lower().replace("-", " ").replace("_", " ")
    parts = normalized.split()
    result = {"species": "", "bone_type": "", "side": "", "region": ""}

    for part in parts:
        p = part.strip()
        if p in ("chien", "canis", "dog"):
            result["species"] = "canis_familiaris"
        elif p in BONE_MAP_FR:
            result["bone_type"] = BONE_MAP_FR[p]
        elif p in SIDE_MAP_FR:
            result["side"] = SIDE_MAP_FR[p]
        elif p in REGION_MAP_FR:
            result["region"] = REGION_MAP_FR[p]

    return result


class OrthancClient:
    """Client for Orthanc PACS REST API.

    Args:
        base_url: Orthanc server URL.
        username: Optional username for authentication.
        password: Optional password for authentication.
    """

    def __init__(
        self,
        base_url: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ) -> None:
        """Initialize Orthanc client."""
        self.base_url = base_url or os.getenv("ORTHANC_URL", "http://10.0.0.59:8042")
        if username is None:
            username = os.getenv("ORTHANC_USER", "")
        if password is None:
            password = os.getenv("ORTHANC_PASSWORD", "")

        self._auth = None
        if username and password:
            self._auth = (username, password)

        self._client = httpx.Client(
            base_url=self.base_url,
            auth=self._auth,
            timeout=30.0,
        )

    def close(self) -> None:
        """Close HTTP client."""
        self._client.close()

    def __enter__(self) -> "OrthancClient":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def _get(self, path: str, **kwargs: Any) -> httpx.Response:
        """Make GET request."""
        resp = self._client.get(path, **kwargs)
        resp.raise_for_status()
        return resp

    def _get_json(self, path: str) -> Any:
        """Make GET request and return JSON."""
        return self._get(path).json()

    def list_studies(self) -> list[str]:
        """Return all study IDs.

        Returns:
            List of study IDs.
        """
        return self._get_json("/studies")

    def get_study(self, study_id: str) -> dict[str, Any]:
        """Get study details.

        Args:
            study_id: Study ID.

        Returns:
            Study info dict.
        """
        return self._get_json(f"/studies/{study_id}")

    def list_series(self, study_id: str) -> list[str]:
        """List series in study.

        Args:
            study_id: Study ID.

        Returns:
            List of series IDs.
        """
        study = self.get_study(study_id)
        return study.get("Series", [])

    def get_series(self, series_id: str) -> dict[str, Any]:
        """Get series details.

        Args:
            series_id: Series ID.

        Returns:
            Series info dict.
        """
        return self._get_json(f"/series/{series_id}")

    def list_instances(self, series_id: str) -> list[str]:
        """List instances in series.

        Args:
            series_id: Series ID.

        Returns:
            List of instance IDs.
        """
        series = self.get_series(series_id)
        return series.get("Instances", [])

    def get_instance(self, instance_id: str) -> dict[str, Any]:
        """Get instance details.

        Args:
            instance_id: Instance ID.

        Returns:
            Instance info dict.
        """
        return self._get_json(f"/instances/{instance_id}")

    def get_image_pixels(self, instance_id: str) -> np.ndarray:
        """Download DICOM and extract pixel array.

        Args:
            instance_id: Instance ID.

        Returns:
            Pixel array as uint16 numpy array.
        """
        from PIL import Image
        from pydicom import dcmread

        # Get DICOM file
        dicom_bytes = self._get(f"/instances/{instance_id}/file").content

        # Parse with pydicom
        dcm = dcmread(io.BytesIO(dicom_bytes))

        # Extract pixel array
        if hasattr(dcm, "pixel_array"):
            return np.asarray(dcm.pixel_array, dtype=np.uint16)

        # Fallback: convert via PIL
        img = Image.open(io.BytesIO(dicom_bytes))
        return np.asarray(img, dtype=np.uint16)
