"""Dashboard service for SSE streaming and monitoring.

Orchestrates event bus, pipeline state, and performance monitoring.
"""

import logging
from collections.abc import AsyncGenerator
from typing import Any

from .events import EventBus
from .monitoring import get_monitor

logger = logging.getLogger(__name__)


class DashboardService:
    """Service for dashboard operations and SSE streaming."""

    def __init__(self) -> None:
        self.event_bus = EventBus()
        self.monitor = get_monitor()
        logger.info("DashboardService initialized")

    def publish_event(self, event_type: str, data: dict) -> None:
        """Publish an event to all subscribers.

        Args:
            event_type: Type of event.
            data: Event data.
        """
        self.event_bus.publish(event_type, data)

    async def subscribe_events(self) -> AsyncGenerator[str, None]:
        """Subscribe to event stream.

        Yields:
            SSE-formatted strings.
        """
        async for event in self.event_bus.subscribe():
            yield event

    def get_pipeline_state(self) -> dict[str, dict]:
        """Get current pipeline state.

        Returns:
            Dict of all stage states.
        """
        return self.event_bus.state.get_snapshot()

    def get_event_history(self, limit: int = 200) -> list[dict]:
        """Get recent events.

        Args:
            limit: Max number of events to return.

        Returns:
            List of event dicts.
        """
        return self.event_bus.get_history(limit)

    def start_monitoring(self, stage: str) -> None:
        """Start monitoring a stage.

        Args:
            stage: Stage name.
        """
        self.monitor.start_stage(stage)
        self.publish_event(
            "stage",
            {
                "script": stage,
                "stage": stage,
                "status": "started",
                "message": f"Started {stage}",
            },
        )

    def end_monitoring(self, stage: str | None = None) -> None:
        """End monitoring a stage.

        Args:
            stage: Stage name or None for current.
        """
        metrics = self.monitor.end_stage(stage)
        if metrics:
            self.publish_event(
                "stage",
                {
                    "script": metrics.stage,
                    "stage": metrics.stage,
                    "status": "completed",
                    "message": f"Completed {metrics.stage}",
                    "metrics": metrics.to_dict(),
                },
            )

    def record_progress(
        self,
        stage: str,
        step: int,
        total: int,
        message: str = "",
        metrics: dict | None = None,
    ) -> None:
        """Record progress in a stage.

        Args:
            stage: Stage name.
            step: Current step.
            total: Total steps.
            message: Progress message.
            metrics: Additional metrics.
        """
        data: dict[str, Any] = {
            "script": stage,
            "step": step,
            "total": total,
        }
        if message:
            data["message"] = message
        if metrics:
            data["metrics"] = metrics

        self.publish_event("progress", data)

    def get_metrics(self, stage: str | None = None) -> dict:
        """Get performance metrics.

        Args:
            stage: Stage name or None for all.

        Returns:
            Performance metrics dict.
        """
        return self.monitor.get_metrics(stage)

    async def status(self) -> dict[str, Any]:
        """Get service status.

        Returns:
            Status dict.
        """
        return {
            "status": "ready",
            "pipeline_state": self.get_pipeline_state(),
            "subscribers": len(self.event_bus._subscribers),
            "history_size": len(self.event_bus._history),
        }


# Module-level instance
_service: DashboardService | None = None


def get_service() -> DashboardService:
    """Get or create the dashboard service instance."""
    global _service
    if _service is None:
        _service = DashboardService()
    return _service
