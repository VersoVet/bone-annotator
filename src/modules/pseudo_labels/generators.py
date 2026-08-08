"""Pseudo-label generation for training data.

Generates training labels automatically from image analysis without manual annotation.
"""

import logging

import cv2
import numpy as np
from scipy import ndimage

logger = logging.getLogger(__name__)


def generate_density_mask(
    image_float: np.ndarray,
    bone_mask: np.ndarray,
    n_clusters: int = 3,
    use_spatial_prior: bool = True,
) -> np.ndarray:
    """Generate density segmentation pseudo-labels using K-means clustering.

    Args:
        image_float: Normalized [0,1] image.
        bone_mask: Binary mask (255 = bone).
        n_clusters: Number of intensity clusters (default 3).
        use_spatial_prior: Apply anatomical spatial prior.

    Returns:
        Label mask: 0=background, 1=cortical, 2=spongy, 3=medullary.
    """
    h, w = image_float.shape[:2]
    label_mask = np.zeros((h, w), dtype=np.uint8)
    binary = (bone_mask > 127).astype(np.uint8)
    bone_pixels = image_float[binary > 0]
    if len(bone_pixels) < 100:
        return label_mask

    # K-means clustering on intensity values
    pixels_f32 = bone_pixels.astype(np.float32).reshape(-1, 1)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.01)
    _, labels_km, centers = cv2.kmeans(pixels_f32, n_clusters, None, criteria, 10, cv2.KMEANS_PP_CENTERS)
    labels_km = labels_km.flatten()
    centers = centers.flatten()

    # Sort clusters by intensity: highest = cortical, lowest = medullary
    order = np.argsort(centers)[::-1]  # descending
    cluster_to_density: dict[int, int] = {}
    for new_idx, old_idx in enumerate(order):
        cluster_to_density[old_idx] = new_idx + 1  # 1=cortical, 2=spongy, 3=medullary

    # Map clusters back to image
    bone_coords = np.where(binary > 0)
    for i, (r, c) in enumerate(zip(bone_coords[0], bone_coords[1], strict=False)):
        label_mask[r, c] = cluster_to_density[labels_km[i]]

    # Apply spatial prior if requested
    if use_spatial_prior:
        label_mask = _apply_spatial_prior(label_mask, binary)

    # Morphological cleanup
    label_mask = _morphological_cleanup(label_mask)
    return label_mask


def _apply_spatial_prior(label_mask: np.ndarray, bone_binary: np.ndarray) -> np.ndarray:
    """Refine density labels using anatomical spatial prior.

    Cortical bone is expected near the periphery, medullary near the center.
    Uses distance transform from the bone contour to modulate labels.
    """
    # Distance transform from bone boundary (inward)
    dist = ndimage.distance_transform_edt(bone_binary)
    if dist.max() < 1:
        return label_mask
    dist = dist / dist.max()
    refined = label_mask.copy()

    # Peripheral zone (distance < 25th percentile of bone distances)
    bone_distances = dist[bone_binary > 0]
    if len(bone_distances) == 0:
        return label_mask
    p25 = np.percentile(bone_distances[bone_distances > 0], 25) if np.any(bone_distances > 0) else 1.0
    p75 = np.percentile(bone_distances[bone_distances > 0], 75) if np.any(bone_distances > 0) else 2.0
    peripheral = (dist > 0) & (dist <= p25)
    central = dist >= p75

    # Boost cortical confidence at periphery
    refined[(peripheral) & (label_mask == 2)] = 1  # spongy -> cortical at periphery
    # Boost medullary confidence at center
    refined[(central) & (label_mask == 2)] = 3  # spongy -> medullary at center
    return refined


def _morphological_cleanup(label_mask: np.ndarray) -> np.ndarray:
    """Clean up density mask with morphological operations per class."""
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    cleaned = label_mask.copy()
    for cls in [1, 2, 3]:
        binary = (label_mask == cls).astype(np.uint8) * 255
        binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        # Only update where we had some class (don't overwrite background)
        cleaned[(binary > 127) & (label_mask > 0)] = cls
    return cleaned
