"""Tests for admin module."""


def test_admin_routes_import() -> None:
    """Admin router loads with expected prefix."""
    from src.modules.admin.routes import router

    assert router.prefix == "/api/admin"


def test_imaging_config_defaults() -> None:
    """Imaging config includes imaging-sdk paths."""
    from src.config import get_imaging_config

    cfg = get_imaging_config()
    assert "user_dir" in cfg
    assert "default_treatment" in cfg
    assert cfg["default_treatment"] == "os_nu_medsam_user"
