"""Tests annotation workflow service imports."""


def test_annotation_service_import() -> None:
    """Test import annotation workflow service."""
    from src.modules.annotation.service import AnnotationWorkflowService  # noqa: F401

    assert True


def test_annotation_models_import() -> None:
    """Test import annotation models."""
    from src.modules.annotation.models import (  # noqa: F401
        CreateTaskRequest,
        TaskResponse,
        ValidateRequest,
    )

    assert True
