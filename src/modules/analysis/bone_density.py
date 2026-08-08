"""Bone density analysis module.

Analyzes density zones (cortical, spongy, medullary) from model predictions
and computes angular density profiles across 360° rotations.
"""

import logging

import numpy as np

logger = logging.getLogger(__name__)

# Density class names - import from config when available
DENSITY_CLASSES = ["background", "cortical", "spongy", "medullary"]


def analyze_density_map(
    density_mask: np.ndarray,
    image_float: np.ndarray,
) -> dict:
    """Analyze a predicted density segmentation mask.

    Args:
        density_mask: (H, W) with values 0=bg, 1=cortical, 2=spongy, 3=medullary.
        image_float: Normalized [0,1] image for intensity analysis.

    Returns:
        Dict with per-zone statistics.
    """
    bone_area = np.sum(density_mask > 0)
    if bone_area == 0:
        return {"zones": [], "total_bone_area": 0}

    zones = []
    for cls_idx, cls_name in enumerate(DENSITY_CLASSES):
        if cls_idx == 0:  # Skip background
            continue
        mask = density_mask == cls_idx
        area = int(np.sum(mask))
        if area == 0:
            zones.append(
                {
                    "name": cls_name,
                    "area_pixels": 0,
                    "ratio": 0.0,
                    "mean_intensity": 0.0,
                    "std_intensity": 0.0,
                }
            )
            continue

        intensities = image_float[mask]
        zones.append(
            {
                "name": cls_name,
                "area_pixels": area,
                "ratio": float(area / bone_area),
                "mean_intensity": float(np.mean(intensities)),
                "std_intensity": float(np.std(intensities)),
                "min_intensity": float(np.min(intensities)),
                "max_intensity": float(np.max(intensities)),
            }
        )

    return {
        "zones": zones,
        "total_bone_area": int(bone_area),
        "cortical_ratio": zones[0]["ratio"] if zones else 0.0,
        "spongy_ratio": zones[1]["ratio"] if len(zones) > 1 else 0.0,
        "medullary_ratio": zones[2]["ratio"] if len(zones) > 2 else 0.0,
    }


def compute_angular_density_profile(
    density_maps: list[np.ndarray],
    angles: list[float],
) -> dict:
    """Compute density ratios as function of rotation angle.

    Used to identify angle-dependent density variations vs true pathology.

    Args:
        density_maps: List of density masks across rotation angles.
        angles: Corresponding angles in degrees.

    Returns:
        Per-zone density ratio profile and angular statistics.
    """
    profiles: dict[str, list] = {
        "cortical": [],
        "spongy": [],
        "medullary": [],
        "angles": [],
    }

    for mask, angle in zip(density_maps, angles, strict=False):
        bone_area = np.sum(mask > 0)
        if bone_area == 0:
            continue
        profiles["angles"].append(angle)
        for cls_idx, name in [(1, "cortical"), (2, "spongy"), (3, "medullary")]:
            ratio = float(np.sum(mask == cls_idx) / bone_area)
            profiles[name].append(ratio)

    # Compute statistics
    stats: dict[str, dict[str, float]] = {}
    for name in ["cortical", "spongy", "medullary"]:
        values = np.array(profiles[name]) if profiles[name] else np.array([0.0])
        stats[name] = {
            "mean": float(np.mean(values)),
            "std": float(np.std(values)),
            "min": float(np.min(values)),
            "max": float(np.max(values)),
            "range": float(np.max(values) - np.min(values)),
        }

    return {
        "profiles": profiles,
        "statistics": stats,
    }


def compute_median_density_map(
    density_maps: list[np.ndarray],
) -> np.ndarray:
    """Compute median density map across all rotation angles.

    Identifies stable density zones vs angle-dependent artifacts.
    A zone that changes class across angles is unreliable and may indicate
    normal angle-dependent variation rather than pathology.
    """
    if not density_maps:
        return np.zeros((128, 128), dtype=np.uint8)

    stacked = np.stack(density_maps, axis=0)  # (N, H, W)
    # Mode (most frequent class) across angles
    from scipy import stats as sp_stats

    mode_result = sp_stats.mode(stacked, axis=0, keepdims=False)
    median_map = mode_result.mode.astype(np.uint8)

    return median_map


def detect_density_anomalies(
    density_stats: dict,
    reference_stats: dict | None = None,
) -> list[dict]:
    """Detect density anomalies compared to population reference.

    Args:
        density_stats: Current specimen density statistics.
        reference_stats: Population mean/std per zone (from atlas).

    Returns:
        List of anomaly flags.
    """
    if reference_stats is None:
        # Default reference values for canine long bones
        reference_stats = {
            "cortical": {"mean_ratio": 0.25, "std_ratio": 0.05},
            "spongy": {"mean_ratio": 0.45, "std_ratio": 0.08},
            "medullary": {"mean_ratio": 0.30, "std_ratio": 0.06},
        }

    anomalies: list[dict] = []
    zone_map = {
        "cortical": "cortical_ratio",
        "spongy": "spongy_ratio",
        "medullary": "medullary_ratio",
    }

    for zone, key in zone_map.items():
        value = density_stats.get(key, 0.0)
        ref = reference_stats.get(zone, {})
        ref_mean = ref.get("mean_ratio", 0.0)
        ref_std = ref.get("std_ratio", 1.0)

        z_score = abs(value - ref_mean) / ref_std if ref_std > 0 else 0.0

        if z_score > 3.0:
            anomalies.append(
                {
                    "zone": zone,
                    "severity": "severe",
                    "z_score": float(z_score),
                    "value": value,
                    "expected": ref_mean,
                    "message": (f"{zone} ratio {value:.2f} is {z_score:.1f}σ from expected {ref_mean:.2f}"),
                }
            )
        elif z_score > 2.0:
            anomalies.append(
                {
                    "zone": zone,
                    "severity": "moderate",
                    "z_score": float(z_score),
                    "value": value,
                    "expected": ref_mean,
                    "message": (f"{zone} ratio {value:.2f} is {z_score:.1f}σ from expected {ref_mean:.2f}"),
                }
            )

    return anomalies
