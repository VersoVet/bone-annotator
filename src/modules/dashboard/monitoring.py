"""Monitoring and performance metrics collection.

Tracks pipeline execution metrics, resource usage, and performance statistics.
"""

import logging
import time
from dataclasses import dataclass, field
from typing import ClassVar

logger = logging.getLogger(__name__)


@dataclass
class PerformanceMetrics:
    """Performance metrics for a stage execution."""

    stage: str
    start_time: float = 0.0
    end_time: float = 0.0
    duration_seconds: float = 0.0
    items_processed: int = 0
    items_per_second: float = 0.0
    peak_memory_mb: float = 0.0
    errors: int = 0
    warnings: int = 0
    custom_metrics: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "stage": self.stage,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration_seconds": self.duration_seconds,
            "items_processed": self.items_processed,
            "items_per_second": self.items_per_second,
            "peak_memory_mb": self.peak_memory_mb,
            "errors": self.errors,
            "warnings": self.warnings,
            "custom_metrics": self.custom_metrics,
        }


class Monitor:
    """Monitors pipeline execution and collects metrics."""

    TRACKED_STAGES: ClassVar[list[str]] = [
        "generate_pseudo_labels",
        "train",
        "populate_qdrant",
        "build_shape_model",
    ]

    def __init__(self) -> None:
        self.metrics: dict[str, PerformanceMetrics] = {}
        self.current_stage: str | None = None

    def start_stage(self, stage: str) -> None:
        """Start monitoring a stage.

        Args:
            stage: Stage name.
        """
        if stage not in self.TRACKED_STAGES:
            logger.warning("Untracked stage: %s", stage)
        self.current_stage = stage
        self.metrics[stage] = PerformanceMetrics(
            stage=stage,
            start_time=time.time(),
        )
        logger.info("Started monitoring stage: %s", stage)

    def end_stage(self, stage: str | None = None) -> PerformanceMetrics | None:
        """End monitoring a stage.

        Args:
            stage: Stage name (uses current if None).

        Returns:
            PerformanceMetrics or None if stage not found.
        """
        if stage is None:
            stage = self.current_stage
        if stage is None or stage not in self.metrics:
            return None

        metrics = self.metrics[stage]
        metrics.end_time = time.time()
        metrics.duration_seconds = metrics.end_time - metrics.start_time

        if metrics.duration_seconds > 0 and metrics.items_processed > 0:
            metrics.items_per_second = metrics.items_processed / metrics.duration_seconds

        logger.info(
            "Ended monitoring stage: %s (%.2fs, %d items)",
            stage,
            metrics.duration_seconds,
            metrics.items_processed,
        )
        return metrics

    def add_metric(
        self,
        stage: str,
        key: str,
        value: object,
    ) -> None:
        """Add a custom metric.

        Args:
            stage: Stage name.
            key: Metric key.
            value: Metric value.
        """
        if stage not in self.metrics:
            self.metrics[stage] = PerformanceMetrics(stage=stage)
        self.metrics[stage].custom_metrics[key] = value

    def record_items(self, stage: str, count: int) -> None:
        """Record items processed.

        Args:
            stage: Stage name.
            count: Number of items processed.
        """
        if stage not in self.metrics:
            self.metrics[stage] = PerformanceMetrics(stage=stage)
        self.metrics[stage].items_processed = count

    def record_error(self, stage: str) -> None:
        """Record an error in a stage.

        Args:
            stage: Stage name.
        """
        if stage not in self.metrics:
            self.metrics[stage] = PerformanceMetrics(stage=stage)
        self.metrics[stage].errors += 1

    def record_warning(self, stage: str) -> None:
        """Record a warning in a stage.

        Args:
            stage: Stage name.
        """
        if stage not in self.metrics:
            self.metrics[stage] = PerformanceMetrics(stage=stage)
        self.metrics[stage].warnings += 1

    def get_metrics(self, stage: str | None = None) -> dict:
        """Get metrics for a stage.

        Args:
            stage: Stage name or None for all stages.

        Returns:
            Dict of metrics.
        """
        if stage is None:
            return {s: m.to_dict() for s, m in self.metrics.items()}
        if stage in self.metrics:
            return self.metrics[stage].to_dict()
        return {}

    def reset(self) -> None:
        """Reset all metrics."""
        self.metrics.clear()
        self.current_stage = None


# Module-level instance
_monitor: Monitor | None = None


def get_monitor() -> Monitor:
    """Get or create the monitor instance."""
    global _monitor
    if _monitor is None:
        _monitor = Monitor()
    return _monitor
