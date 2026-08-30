"""Learning progress milestones per bone type (from PROMPT_MAJ)."""

MILESTONES = [500, 2000, 5000, 10000]

MILESTONE_LABELS = {
    500: "Calibration des règles",
    2000: "Premier modèle (nnU-Net v0)",
    5000: "Modèle exploitable",
    10000: "Très bon segmentateur",
}

DEFAULT_BONE_TYPES = ["humerus", "radius", "ulna", "femur", "tibia", "fibula", "scapula"]


def next_milestone(gold_count: int) -> tuple[int, str]:
    """Return next milestone target and label for a gold count."""
    for m in MILESTONES:
        if gold_count < m:
            return m, MILESTONE_LABELS.get(m, f"Jalon {m}")
    return MILESTONES[-1], MILESTONE_LABELS[MILESTONES[-1]]
