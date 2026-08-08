"""Server-Sent Events (SSE) bus and pipeline state management."""

import asyncio
import json
import logging
import time
from collections import deque
from collections.abc import AsyncGenerator
from dataclasses import dataclass, field
from typing import ClassVar

logger = logging.getLogger(__name__)


@dataclass
class StageState:
    """State of a single pipeline stage."""

    script: str
    stage: str = ""
    status: str = "idle"  # idle, started, running, completed, failed
    resource: str = ""
    message: str = ""
    step: int = 0
    total: int = 0
    percent: float = 0.0
    metrics: dict = field(default_factory=dict)
    started_at: float = 0.0
    updated_at: float = 0.0

    def to_dict(self) -> dict:
        """Return stage state as a dictionary."""
        return {
            "script": self.script,
            "stage": self.stage,
            "status": self.status,
            "resource": self.resource,
            "message": self.message,
            "step": self.step,
            "total": self.total,
            "percent": self.percent,
            "metrics": self.metrics,
            "started_at": self.started_at,
            "updated_at": self.updated_at,
        }


class PipelineState:
    """Aggregated state of all pipeline stages."""

    SCRIPTS: ClassVar[list[str]] = [
        "generate_pseudo_labels",
        "train",
        "populate_qdrant",
        "build_shape_model",
    ]

    def __init__(self) -> None:
        self.stages: dict[str, StageState] = {s: StageState(script=s) for s in self.SCRIPTS}

    def update_stage(self, script: str, **kwargs: object) -> None:
        """Update a pipeline stage with the given keyword arguments."""
        if script not in self.stages:
            self.stages[script] = StageState(script=script)
        state = self.stages[script]
        for k, v in kwargs.items():
            if hasattr(state, k):
                setattr(state, k, v)
        state.updated_at = time.time()

    def get_snapshot(self) -> dict[str, dict]:
        """Return a snapshot of all pipeline stages."""
        return {name: s.to_dict() for name, s in self.stages.items()}


class EventBus:
    """Async fan-out event bus for SSE streaming.

    Each connected client gets its own asyncio.Queue.
    Events are published to all queues and stored in history.
    """

    def __init__(self, history_size: int = 200) -> None:
        self._subscribers: list[asyncio.Queue] = []
        self._history: deque = deque(maxlen=history_size)
        self.state = PipelineState()
        self._lock = asyncio.Lock()

    def publish(self, event_type: str, data: dict) -> None:
        """Publish an event to all subscribers and update state."""
        event: dict = {"event": event_type, "data": data, "timestamp": time.time()}
        self._history.append(event)

        # Update pipeline state based on event type
        script = data.get("script", "")
        if event_type == "stage":
            self.state.update_stage(
                script,
                stage=data.get("stage", ""),
                status=data.get("status", ""),
                resource=data.get("resource", ""),
                message=data.get("message", ""),
            )
            if data.get("status") == "started":
                self.state.update_stage(script, started_at=time.time())
        elif event_type == "progress":
            step = data.get("step", 0)
            total = data.get("total", 0)
            percent = (step / total * 100) if total > 0 else 0.0
            self.state.update_stage(
                script,
                status="running",
                step=step,
                total=total,
                percent=round(percent, 1),
                message=data.get("message", ""),
                metrics=data.get("metrics", {}),
            )

        # Fan out to all subscribers
        sse_str = self._format_sse(event_type, data)
        dead = []
        for q in self._subscribers:
            try:
                q.put_nowait(sse_str)
            except asyncio.QueueFull:
                dead.append(q)
        for q in dead:
            self._subscribers.remove(q)

    def _format_sse(self, event_type: str, data: dict) -> str:
        """Format event as SSE string."""
        payload = json.dumps(data, default=str)
        return f"event: {event_type}\ndata: {payload}\n\n"

    async def subscribe(self) -> AsyncGenerator[str, None]:
        """Subscribe to the event stream.

        Yields:
            SSE-formatted strings for each event.
        """
        q: asyncio.Queue = asyncio.Queue(maxsize=256)
        self._subscribers.append(q)
        try:
            while True:
                yield await q.get()
        except asyncio.CancelledError:
            pass
        finally:
            if q in self._subscribers:
                self._subscribers.remove(q)

    def get_history(self, limit: int = 200) -> list[dict]:
        """Return the most recent events from history."""
        return list(self._history)[-limit:]

    async def heartbeat_loop(self, interval: float = 15.0) -> None:
        """Send periodic heartbeat events."""
        while True:
            await asyncio.sleep(interval)
            self.publish("heartbeat", {"timestamp": time.time()})
