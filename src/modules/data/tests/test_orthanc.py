"""Tests Orthanc PACS client."""


def test_orthanc_client_import():
    """Test import Orthanc client."""
    from src.modules.data.orthanc_client import OrthancClient  # noqa: F401

    assert True
