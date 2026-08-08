"""Landmark extraction and normalization for anatomical analysis.

Handles coordinate normalization, alignment, and per-bone landmark
sets for downstream conformation analysis.
"""

import logging

import numpy as np

logger = logging.getLogger(__name__)

# Landmark names per bone type - import from config when available
LANDMARK_NAMES: dict[str, list[str]] = {
    "femur": ["femoral_head_center", "intercondylar_fossa"],
    "humerus": ["head_center", "trochlea"],
}


def normalize_landmarks(
    landmarks: list[dict],
    image_size: int = 512,
) -> np.ndarray:
    """Normalize landmark coordinates to [0, 1] range.

    Args:
        landmarks: List of dicts with 'x', 'y', 'confidence'.
        image_size: Coordinate space size.

    Returns:
        Array of shape (N, 2) with normalized coordinates.
    """
    coords = np.array(
        [[lm["x"] / image_size, lm["y"] / image_size] for lm in landmarks],
        dtype=np.float64,
    )
    return coords


def align_landmarks(
    landmarks: np.ndarray,
    reference: np.ndarray | None = None,
) -> np.ndarray:
    """Procrustes alignment of landmarks.

    Centering, uniform scaling, and rotation alignment.
    If reference is provided, aligns to it. Otherwise, centers and scales only.

    Args:
        landmarks: (N, 2) coordinates.
        reference: Optional (N, 2) reference to align to.

    Returns:
        Aligned (N, 2) coordinates.
    """
    # Center
    centroid = landmarks.mean(axis=0)
    centered = landmarks - centroid

    # Scale to unit size
    scale = np.sqrt(np.sum(centered**2))
    if scale < 1e-8:
        return centered
    normalized = centered / scale

    if reference is None:
        return normalized

    # Align to reference using Procrustes rotation
    ref_centered = reference - reference.mean(axis=0)
    ref_scale = np.sqrt(np.sum(ref_centered**2))
    if ref_scale < 1e-8:
        return normalized
    ref_norm = ref_centered / ref_scale

    # SVD for optimal rotation
    H = normalized.T @ ref_norm
    U, _S, Vt = np.linalg.svd(H)
    R = Vt.T @ U.T

    # Ensure proper rotation (det = +1)
    if np.linalg.det(R) < 0:
        Vt[-1, :] *= -1
        R = Vt.T @ U.T

    aligned = normalized @ R
    return aligned


def flatten_landmarks(landmarks: np.ndarray) -> np.ndarray:
    """Flatten (N, 2) landmarks to (2N,) vector for PCA."""
    return landmarks.flatten()


def unflatten_landmarks(vector: np.ndarray, n_landmarks: int) -> np.ndarray:
    """Unflatten (2N,) vector back to (N, 2) landmarks."""
    return vector.reshape(n_landmarks, 2)


def extract_landmarks_for_bone(
    all_landmarks: list[dict],
    bone_type: str,
) -> list[dict]:
    """Extract and filter landmarks relevant to a specific bone type.

    Only keeps landmarks with sufficient confidence.
    """
    expected = LANDMARK_NAMES.get(bone_type, [])
    n_expected = len(expected)
    relevant = all_landmarks[:n_expected]

    filtered: list[dict] = []
    for lm in relevant:
        if lm.get("confidence", 0.0) > 0.1:
            filtered.append(lm)
        else:
            filtered.append({"name": lm.get("name", ""), "x": 0, "y": 0, "confidence": 0.0})

    return filtered


def compute_inter_landmark_distances(
    landmarks: list[dict],
) -> dict[str, float]:
    """Compute pairwise distances between landmarks.

    Useful for ratio-based measurements that are scale-invariant.
    """
    n = len(landmarks)
    distances: dict[str, float] = {}

    for i in range(n):
        for j in range(i + 1, n):
            li = landmarks[i]
            lj = landmarks[j]
            if li["confidence"] < 0.1 or lj["confidence"] < 0.1:
                continue
            d = np.hypot(li["x"] - lj["x"], li["y"] - lj["y"])
            key = f"{li.get('name', i)}_to_{lj.get('name', j)}"
            distances[key] = float(d)

    return distances


def compute_bone_axis_from_landmarks(
    landmarks: list[dict],
    bone_type: str,
) -> dict | None:
    """Compute the principal bone axis from detected landmarks.

    Uses proximal and distal reference landmarks specific to each bone type.
    """
    axis_landmarks = {
        "femur": ("femoral_head_center", "intercondylar_fossa"),
        "humerus": ("head_center", "trochlea"),
        "radius": ("radial_head", "radial_styloid"),
        "ulna": ("olecranon_apex", "ulnar_styloid"),
        "scapula": ("glenoid_cavity", "dorsal_border_mid"),
    }

    if bone_type not in axis_landmarks:
        return None

    prox_name, dist_name = axis_landmarks[bone_type]
    prox = None
    dist = None

    for lm in landmarks:
        name = lm.get("name", "")
        if name == prox_name and lm["confidence"] > 0.2:
            prox = np.array([lm["x"], lm["y"]])
        elif name == dist_name and lm["confidence"] > 0.2:
            dist = np.array([lm["x"], lm["y"]])

    if prox is None or dist is None:
        return None

    axis = dist - prox
    length = np.linalg.norm(axis)
    if length < 1e-6:
        return None

    direction = axis / length
    midpoint = (prox + dist) / 2

    return {
        "proximal": prox.tolist(),
        "distal": dist.tolist(),
        "direction": direction.tolist(),
        "length": float(length),
        "midpoint": midpoint.tolist(),
    }
