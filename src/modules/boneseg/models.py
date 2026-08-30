"""Pydantic models for BoneSeg orchestration endpoints."""

from typing import Any

from pydantic import BaseModel, Field


class TestSetRequest(BaseModel):
    """Request to add acquisitions to the frozen test set."""

    bone_type: str = Field(..., description="Bone type partition")
    acquisition_ids: list[str] = Field(..., min_length=1, description="Acquisition IDs to freeze")


class ActiveLearningRequest(BaseModel):
    """Request to run an active learning cycle."""

    bone_type: str | None = Field(None, description="Limit suggestions to one bone type")
    limit: int = Field(default=5, ge=1, le=50, description="Max tasks to create")
    pipeline_preset: str | None = Field(default=None, description="Imaging treatment preset")
    pre_annotate: bool = Field(default=True, description="Run ML pre-annotation on new tasks")


class WeeklyReportRequest(BaseModel):
    """Request weekly report generation."""

    send_email: bool = Field(default=False, description="Send report via email skill")


class DecisionLogRequest(BaseModel):
    """Manual learning decision log entry."""

    action: str = Field(..., description="Decision action type")
    bone_type: str | None = None
    generation: int | None = None
    notes: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)


class ActiveLearningResult(BaseModel):
    """Result of an active learning orchestration run."""

    synced: dict[str, Any] = Field(default_factory=dict)
    suggestions: list[dict[str, Any]] = Field(default_factory=list)
    tasks_created: list[dict[str, Any]] = Field(default_factory=list)
    skipped: list[str] = Field(default_factory=list)


class GpuStatus(BaseModel):
    """GPU availability for BoneSeg workloads."""

    available: bool = Field(..., description="True if GPU is free for a new job")
    boneseg_running: bool = Field(default=False)
    ml_compute_jobs: int = Field(default=0)
    reason: str = Field(default="")
