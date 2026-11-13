"""Tests for anatomical zone subdivision."""

import numpy as np

from src.modules.annotation.zone_subdivision import (
    ZONE_LABEL_MAP,
    ZONE_RATIOS,
    compute_vertical_profile,
    find_split_points,
    resolve_zone_label_id,
    subdivide_bone_mask,
)


def _make_bone_mask(h: int = 200, w: int = 100, bone_width: int = 30) -> np.ndarray:
    """Create a synthetic vertical bone mask with narrow neck."""
    mask = np.zeros((h, w), dtype=np.uint8)
    cx = w // 2
    for r in range(20, 180):
        # Wide at top (proximal) and bottom (distal), narrow in middle.
        if r < 50:
            half = bone_width // 2
        elif r < 60:
            half = bone_width // 4  # neck constriction
        elif r < 140:
            half = bone_width // 3  # diaphysis
        elif r < 150:
            half = bone_width // 4  # second constriction
        else:
            half = bone_width // 2  # distal
        mask[r, cx - half : cx + half] = 1
    return mask


def test_vertical_profile_shape() -> None:
    """Profile has same height as mask."""
    mask = _make_bone_mask()
    profile = compute_vertical_profile(mask)
    assert profile.shape == (200,)
    assert profile[0] == 0  # no bone at top
    assert profile[100] > 0  # bone in middle


def test_find_split_points_with_constrictions() -> None:
    """Profile-based splitting finds constrictions."""
    mask = _make_bone_mask()
    profile = compute_vertical_profile(mask)
    splits = find_split_points(profile, "humerus")
    assert len(splits) == 2
    assert splits[0] < splits[1]
    # First split should be near the neck (row ~55).
    assert 40 < splits[0] < 80
    # Second split near the distal constriction (~145).
    assert 120 < splits[1] < 170


def test_find_split_points_ratio_fallback() -> None:
    """Uniform width bone falls back to ratio-based splitting."""
    mask = np.zeros((200, 100), dtype=np.uint8)
    mask[20:180, 40:60] = 1  # uniform rectangular bone
    profile = compute_vertical_profile(mask)
    splits = find_split_points(profile, "humerus")
    assert len(splits) == 2
    # With humerus ratios (20% prox, 50% dia), first split near row 52.
    bone_h = 160
    expected_s1 = 20 + int(bone_h * 0.20)
    assert abs(splits[0] - expected_s1) < 5


def test_subdivide_returns_three_zones() -> None:
    """Subdivision produces proximal, diaphysis, distal zones."""
    mask = _make_bone_mask()
    zones = subdivide_bone_mask(mask, "humerus")
    names = [z[0] for z in zones]
    assert "proximal" in names
    assert "diaphysis" in names
    assert "distal" in names


def test_zone_masks_are_disjoint() -> None:
    """Zone masks don't overlap and cover the original bone."""
    mask = _make_bone_mask()
    zones = subdivide_bone_mask(mask, "humerus")
    combined = np.zeros_like(mask)
    for _, zmask in zones:
        # No overlap with previously accumulated zones.
        assert np.logical_and(combined > 0, zmask > 0).sum() == 0
        combined += zmask
    # All bone pixels are covered.
    assert (combined > 0).sum() == (mask > 0).sum()


def test_subdivide_horizontal_bone() -> None:
    """Horizontal bone (width > height) is handled via transpose."""
    mask = np.zeros((80, 300), dtype=np.uint8)
    mask[30:50, 20:280] = 1  # wide horizontal bone
    zones = subdivide_bone_mask(mask, "humerus")
    assert len(zones) == 3
    for _, zmask in zones:
        assert zmask.shape == mask.shape


def test_subdivide_empty_mask() -> None:
    """Empty mask returns no zones."""
    mask = np.zeros((100, 100), dtype=np.uint8)
    zones = subdivide_bone_mask(mask, "humerus")
    assert zones == []


def test_resolve_zone_label_id_exact_match() -> None:
    """Exact label name match returns correct id."""
    labels = [
        {"id": 10, "name": "diaphyse_humerale"},
        {"id": 20, "name": "epiphyse_proximale"},
        {"id": 30, "name": "epiphyse_distale_hum"},
    ]
    result = resolve_zone_label_id("proximal", "humerus", labels)
    assert result is not None
    assert result == (20, "epiphyse_proximale")


def test_resolve_zone_label_id_fallback_order() -> None:
    """First candidate in ZONE_LABEL_MAP takes priority."""
    labels = [
        {"id": 1, "name": "tete_humerale"},
        {"id": 2, "name": "epiphyse_proximale"},
    ]
    result = resolve_zone_label_id("proximal", "humerus", labels)
    assert result is not None
    # epiphyse_proximale is first in the candidate list.
    assert result[1] == "epiphyse_proximale"


def test_resolve_zone_label_id_no_match() -> None:
    """Unknown bone type with no matching labels returns None."""
    labels = [{"id": 1, "name": "unrelated_label"}]
    result = resolve_zone_label_id("proximal", "unknown_bone", labels)
    assert result is None


def test_subdivide_portion_proximal() -> None:
    """Proximal portion excludes distal zone."""
    mask = _make_bone_mask()
    zones = subdivide_bone_mask(mask, "humerus", portion="proximal")
    names = [z[0] for z in zones]
    assert "distal" not in names
    assert "proximal" in names
    assert "diaphysis" in names


def test_subdivide_portion_distal() -> None:
    """Distal portion excludes proximal zone."""
    mask = _make_bone_mask()
    zones = subdivide_bone_mask(mask, "humerus", portion="distal")
    names = [z[0] for z in zones]
    assert "proximal" not in names
    assert "distal" in names
    assert "diaphysis" in names


def test_subdivide_portion_entire() -> None:
    """Entire portion keeps all zones."""
    mask = _make_bone_mask()
    zones = subdivide_bone_mask(mask, "humerus", portion="entire")
    names = [z[0] for z in zones]
    assert len(names) == 3


def test_zone_ratios_sum_to_one() -> None:
    """All bone type ratios sum to approximately 1.0."""
    for bone, ratios in ZONE_RATIOS.items():
        total = sum(ratios.values())
        assert abs(total - 1.0) < 0.01, f"{bone} ratios sum to {total}"


def test_zone_label_map_covers_ratios() -> None:
    """Every bone in ZONE_RATIOS has a ZONE_LABEL_MAP entry."""
    for bone in ZONE_RATIOS:
        if bone in ZONE_LABEL_MAP:
            for region in ZONE_RATIOS[bone]:
                assert region in ZONE_LABEL_MAP[bone], f"{bone}/{region} missing in ZONE_LABEL_MAP"
