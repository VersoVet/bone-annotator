"""Anatomical zone subdivision of bone masks.

Splits a whole-bone binary mask into proximal/diaphysis/distal zones
using vertical projection profile analysis and configurable ratios.
"""

from __future__ import annotations

import logging
from typing import Any

import numpy as np

logger = logging.getLogger(__name__)

# Default anatomical proportions (fraction of bone length per region).
ZONE_RATIOS: dict[str, dict[str, float]] = {
    "humerus": {"proximal": 0.20, "diaphysis": 0.50, "distal": 0.30},
    "radius": {"proximal": 0.25, "diaphysis": 0.50, "distal": 0.25},
    "ulna": {"proximal": 0.30, "diaphysis": 0.45, "distal": 0.25},
    "femur": {"proximal": 0.20, "diaphysis": 0.50, "distal": 0.30},
    "tibia": {"proximal": 0.25, "diaphysis": 0.50, "distal": 0.25},
    "scapula": {"proximal": 0.35, "diaphysis": 0.35, "distal": 0.30},
}

# Maps (bone_type, region) → candidate label-generator zone IDs (priority order).
ZONE_LABEL_MAP: dict[str, dict[str, list[str]]] = {
    "humerus": {
        "proximal": ["epiphyse_proximale", "tete_humerale", "grand_tubercule"],
        "diaphysis": ["diaphyse_humerale", "corps_diaphysaire"],
        "distal": ["epiphyse_distale_hum", "capitulum", "condyle_humeral"],
    },
    "radius": {
        "proximal": ["epiphyse_proximale_rad", "tete_radiale"],
        "diaphysis": ["diaphyse_radiale", "corps_diaphysaire_rad"],
        "distal": ["epiphyse_distale_rad"],
    },
    "ulna": {
        "proximal": ["epiphyse_proximale_uln", "olecrane"],
        "diaphysis": ["diaphyse_ulnaire", "corps_diaphysaire_uln"],
        "distal": ["epiphyse_distale_uln", "processus_styloidien"],
    },
    "femur": {
        "proximal": ["epiphyse_proximale_fem", "tete_femorale", "grand_trochanter"],
        "diaphysis": ["diaphyse_femorale", "corps_diaphysaire_fem"],
        "distal": ["epiphyse_distale_fem", "condyle_femoral"],
    },
    "tibia": {
        "proximal": ["epiphyse_proximale_tib", "plateau_tibial"],
        "diaphysis": ["diaphyse_tibiale", "corps_diaphysaire_tib"],
        "distal": ["epiphyse_distale_tib", "malleole_mediale"],
    },
}


def compute_vertical_profile(mask: np.ndarray) -> np.ndarray:
    """Compute vertical projection profile of a bone mask.

    Args:
        mask: Binary uint8 mask (H, W) with 1=bone.

    Returns:
        1D float array of per-row bone pixel counts, length = H.
    """
    return mask.astype(np.float64).sum(axis=1)


def _smooth(profile: np.ndarray, window: int) -> np.ndarray:
    """Smooth a 1D profile with a moving average.

    Args:
        profile: 1D array.
        window: Kernel width (odd preferred).

    Returns:
        Smoothed 1D array (same length, edges padded).
    """
    if window < 3 or len(profile) < window:
        return profile.copy()
    kernel = np.ones(window) / window
    return np.convolve(profile, kernel, mode="same")


def find_split_points(
    profile: np.ndarray,
    bone_type: str,
    *,
    ratios: dict[str, float] | None = None,
) -> list[int]:
    """Find row indices splitting the profile into 3 anatomical zones.

    Tries to detect natural constrictions (local minima) first.
    Falls back to ratio-based splitting.

    Args:
        profile: Vertical projection profile (from compute_vertical_profile).
        bone_type: Bone type for default ratios.
        ratios: Override zone proportions.

    Returns:
        Two row indices [split1, split2] dividing proximal/diaphysis/distal.
    """
    rows_with_bone = np.where(profile > 0)[0]
    if len(rows_with_bone) < 10:
        mid = len(profile) // 2
        return [mid // 2, mid + mid // 2]

    r_min, r_max = int(rows_with_bone[0]), int(rows_with_bone[-1])
    bone_height = r_max - r_min + 1

    # Try profile-based splitting: find local minima in smoothed profile.
    window = max(3, bone_height // 20)
    smoothed = _smooth(profile[r_min : r_max + 1], window)
    peak_val = float(smoothed.max())

    if peak_val > 0:
        # Find all local minima (value < 70% of peak and < both neighbours).
        minima: list[tuple[float, int]] = []
        for i in range(1, len(smoothed) - 1):
            if smoothed[i] < smoothed[i - 1] and smoothed[i] < smoothed[i + 1]:
                if smoothed[i] < 0.7 * peak_val:
                    minima.append((float(smoothed[i]), i))

        if len(minima) >= 2:
            # Take the two deepest minima, sorted by position.
            minima.sort(key=lambda x: x[0])
            top2 = sorted([m[1] for m in minima[:2]])
            return [r_min + top2[0], r_min + top2[1]]

    # Fallback: ratio-based splitting.
    r = ratios or ZONE_RATIOS.get(bone_type, {"proximal": 0.25, "diaphysis": 0.50, "distal": 0.25})
    prox_frac = r.get("proximal", 0.25)
    dia_frac = r.get("diaphysis", 0.50)
    split1 = r_min + int(bone_height * prox_frac)
    split2 = r_min + int(bone_height * (prox_frac + dia_frac))
    return [split1, split2]


def subdivide_bone_mask(
    mask: np.ndarray,
    bone_type: str,
    *,
    ratios: dict[str, float] | None = None,
    portion: str = "entire",
) -> list[tuple[str, np.ndarray]]:
    """Split a whole-bone mask into anatomical zone masks.

    Handles both vertical and horizontal bone orientations by checking
    the aspect ratio of the bone bounding box.

    Args:
        mask: Binary uint8 mask (H, W) with 1=bone.
        bone_type: Bone type for ratio defaults and label mapping.
        ratios: Override zone proportions.
        portion: Acquisition portion (proximal, distal, entire). Filters
            out zones that cannot appear in this portion.

    Returns:
        List of (region_name, zone_mask) tuples. Each zone_mask has the
        same shape as input, with pixels outside the zone zeroed.
    """
    if mask.max() == 0:
        return []

    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    r_min, r_max = int(np.where(rows)[0][[0, -1]][0]), int(np.where(rows)[0][[0, -1]][1])
    c_min, c_max = int(np.where(cols)[0][[0, -1]][0]), int(np.where(cols)[0][[0, -1]][1])
    bone_h = r_max - r_min + 1
    bone_w = c_max - c_min + 1

    # If bone is wider than tall, transpose for analysis then transpose back.
    transposed = bone_w > bone_h * 1.3
    work_mask = mask.T if transposed else mask

    profile = compute_vertical_profile(work_mask)
    split1, split2 = find_split_points(profile, bone_type, ratios=ratios)

    regions = [
        ("proximal", 0, split1),
        ("diaphysis", split1, split2),
        ("distal", split2, work_mask.shape[0]),
    ]

    # Determine which zones to keep based on acquisition portion.
    allowed_zones = _allowed_zones_for_portion(portion)

    result: list[tuple[str, np.ndarray]] = []
    for name, row_start, row_end in regions:
        if allowed_zones and name not in allowed_zones:
            continue
        zone = work_mask.copy()
        zone[:row_start, :] = 0
        zone[row_end:, :] = 0
        if transposed:
            zone = zone.T
        if zone.any():
            result.append((name, zone))

    return result


def _allowed_zones_for_portion(portion: str) -> set[str]:
    """Return the subdivision zone names valid for a given acquisition portion.

    Args:
        portion: Acquisition portion (proximal, distal, entire, bilateral).

    Returns:
        Set of allowed zone names, or empty set (= all allowed).
    """
    if not portion or portion in ("entire", "bilateral"):
        return set()  # all zones
    if portion == "proximal":
        return {"proximal", "diaphysis"}
    if portion == "distal":
        return {"diaphysis", "distal"}
    return set()


def resolve_zone_label_id(
    zone_region: str,
    bone_type: str,
    cvat_labels: list[dict[str, Any]],
) -> tuple[int, str] | None:
    """Map a zone region name to a CVAT label_id.

    Tries candidate label names from ZONE_LABEL_MAP in priority order,
    returns the first match found in the CVAT task labels.

    Args:
        zone_region: Region name (proximal, diaphysis, distal).
        bone_type: Bone type.
        cvat_labels: CVAT task label list with 'id' and 'name' keys.

    Returns:
        (label_id, label_name) or None if no match.
    """
    candidates = ZONE_LABEL_MAP.get(bone_type, {}).get(zone_region, [])
    label_by_name = {str(lbl.get("name", "")): int(lbl["id"]) for lbl in cvat_labels if "id" in lbl}

    for candidate in candidates:
        if candidate in label_by_name:
            return label_by_name[candidate], candidate

    # Fuzzy fallback: partial match on region keyword.
    keyword = zone_region[:4]  # "prox", "diap", "dist"
    for name, lid in label_by_name.items():
        if keyword in name.lower():
            return lid, name

    return None
