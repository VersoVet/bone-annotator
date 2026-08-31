"""Pydantic models for annotation workflow.

Request/response schemas for task creation, sync, and validation.
"""

from typing import Any

from pydantic import BaseModel, Field


class CreateTaskRequest(BaseModel):
    """Request to create an annotation task."""

    source_name: str = Field(default="bonestore", description="Image source")
    acquisition_id: str = Field(..., description="Acquisition ID")
    bone_type: str = Field(..., description="Bone type (humerus, radius, etc.)")
    region: str = Field(default="entire", description="Anatomical region")
    assignee: str | None = Field(None, description="CVAT user to assign")
    pipeline_preset: str | None = Field(default=None, description="Imaging treatment preset")
    pre_annotate: bool = Field(default=False, description="Request ML pre-annotations")


class TaskProgress(BaseModel):
    """Task preparation progress."""

    step: str = Field(default="", description="Current step")
    detail: str = Field(default="")
    percent: int = Field(default=0, ge=0, le=100, description="Completion percentage")


class TaskResponse(BaseModel):
    """Annotation task response."""

    id: int = Field(..., description="Internal task ID")
    acquisition_id: str = Field(..., description="Acquisition ID")
    cvat_task_id: int | None = Field(None, description="CVAT task ID")
    cvat_url: str | None = Field(None, description="CVAT task URL")
    status: str = Field(..., description="Task status")
    bone_type: str = Field(..., description="Bone type")
    region: str = Field(default="entire")
    frame_count: int = Field(default=0)
    annotated_frames: int = Field(default=0)
    author: str = Field(default="system")
    assignee: str | None = Field(None)
    has_pre_annotations: bool = Field(default=False)
    pipeline_preset: str | None = Field(None)
    dataset_path: str | None = Field(None)
    progress: TaskProgress | None = Field(None, description="Preparation progress")


class TaskListResponse(BaseModel):
    """Paginated task list response."""

    tasks: list[dict[str, Any]] = Field(default_factory=list)
    total: int = Field(default=0)
    limit: int = Field(default=50)
    offset: int = Field(default=0)


class SyncResult(BaseModel):
    """Result of syncing annotations from CVAT."""

    task_id: int = Field(..., description="Internal task ID")
    synced_frames: int = Field(default=0, description="Frames synced")
    zones_count: int = Field(default=0)
    landmarks_count: int = Field(default=0)
    author: str = Field(default="unknown", description="CVAT assignee")


class ValidateRequest(BaseModel):
    """Request to validate or reject a task."""

    validated_by: str = Field(..., description="Validator identifier")
    decision: str = Field(..., description="'validated' or 'rejected'")
    notes: str | None = Field(None, description="Validation notes")


class PreAnnotateResponse(BaseModel):
    """Response from ML pre-annotation request."""

    task_id: int = Field(..., description="Internal task ID")
    cvat_task_id: int = Field(..., description="CVAT task ID")
    status: str = Field(..., description="Pre-annotation status")
    bone_ml_status: str | None = Field(None, description="bone-ml response status")
