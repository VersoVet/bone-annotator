"""Tests for BoneSeg integration."""

from src.modules.storage.pg_utils import compute_quality_tier


def test_quality_tier_manual_validated() -> None:
    """Manual validated annotations are gold tier."""
    assert compute_quality_tier("manual", "reviewer1") == "gold"


def test_quality_tier_manual_unvalidated() -> None:
    """Manual unvalidated annotations default to silver."""
    assert compute_quality_tier("manual", None) == "silver"


def test_quality_tier_ml() -> None:
    """ML annotations are pseudo tier."""
    assert compute_quality_tier("ml", None) == "pseudo"
    assert compute_quality_tier("ml", "reviewer1") == "pseudo"


def test_quality_tier_corrected_ml() -> None:
    """Corrected ML validated annotations are silver."""
    assert compute_quality_tier("corrected_ml", "reviewer1") == "silver"
    assert compute_quality_tier("corrected_ml", None) == "silver"


def test_quality_tier_superseded_source() -> None:
    """Superseded suffix is stripped before tier computation."""
    assert compute_quality_tier("manual_superseded", "reviewer1") == "gold"


def test_boneseg_module_imports() -> None:
    """BoneSeg module imports cleanly."""
    from src.modules.boneseg.gpu import check_gpu_available  # noqa: F401
    from src.modules.boneseg.routes import router  # noqa: F401

    assert router.prefix == "/api/boneseg"


def test_migrations_include_boneseg() -> None:
    """BoneSeg migrations are registered."""
    from src.modules.storage.task_db import _MIGRATIONS

    sql = "\n".join(_MIGRATIONS)
    assert "quality_tier" in sql
    assert "test_sets" in sql
    assert "bonestore_catalog" in sql
    assert "boneseg_training_runs" in sql
