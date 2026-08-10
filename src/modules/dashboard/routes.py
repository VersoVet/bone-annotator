"""FastAPI routes for dashboard monitoring and SSE streaming.

Provides real-time event streaming and pipeline state monitoring
for the annotation workflow.
"""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from .service import get_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("/events")
async def stream_events() -> StreamingResponse:
    """Stream pipeline events via Server-Sent Events (SSE).

    Returns real-time updates on:
    - Annotation task progress
    - Ingestion status
    - Training job updates
    - Inference results
    - System metrics

    Returns:
        SSE StreamingResponse with event stream.
    """
    try:
        service = get_service()

        async def event_generator():
            """Generate SSE stream from event bus."""
            async for event in service.subscribe_events():
                yield event

        return StreamingResponse(
            event_generator(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )
    except Exception as e:
        logger.error("Error streaming events: %s", e)
        raise HTTPException(status_code=500, detail="Failed to stream events")


@router.get("/state")
async def pipeline_state() -> dict[str, Any]:
    """Get current pipeline state snapshot.

    Returns status of all stages:
    - ingestion (BoneStore sync)
    - preprocessing (frame loading)
    - prediction (YOLO inference)
    - annotation (CVAT tasks)
    - training (ML jobs)

    Returns:
        Current state of all pipeline stages.

    Raises:
        HTTPException: If state query fails.
    """
    try:
        service = get_service()
        state = service.get_pipeline_state()

        return {
            "status": "success",
            "timestamp": __import__("datetime").datetime.utcnow().isoformat(),
            "pipeline_state": state,
        }
    except Exception as e:
        logger.error("Error fetching pipeline state: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch pipeline state")


@router.get("/history")
async def event_history(limit: int = 200) -> dict[str, Any]:
    """Get recent event history.

    Args:
        limit: Max events to return (default 200, max 1000).

    Returns:
        List of recent events with metadata.

    Raises:
        HTTPException: If history query fails.
    """
    try:
        if limit > 1000:
            limit = 1000

        service = get_service()
        history = service.get_event_history(limit)

        return {
            "status": "success",
            "total": len(history),
            "limit": limit,
            "events": history,
        }
    except Exception as e:
        logger.error("Error fetching event history: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch event history")


@router.get("/metrics")
async def performance_metrics(stage: str | None = None) -> dict[str, Any]:
    """Get performance metrics for pipeline stages.

    Args:
        stage: Optional specific stage to query.

    Returns:
        Performance metrics with timing and resource usage.

    Raises:
        HTTPException: If metrics query fails.
    """
    try:
        service = get_service()
        metrics = service.get_metrics(stage)

        return {
            "status": "success",
            "stage": stage or "all",
            "metrics": metrics,
        }
    except Exception as e:
        logger.error("Error fetching metrics: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch metrics")


@router.get("/status")
async def dashboard_status() -> dict[str, Any]:
    """Get dashboard service status.

    Returns:
        Service health, active subscribers, and queue stats.

    Raises:
        HTTPException: If status query fails.
    """
    try:
        service = get_service()
        status = await service.status()

        return {
            "status": "ready",
            "service": "dashboard",
            "components": status,
        }
    except Exception as e:
        logger.error("Error fetching dashboard status: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch dashboard status")


@router.post("/event")
async def publish_event(
    event_type: str,
    data: dict[str, Any],
) -> dict[str, Any]:
    """Publish a custom event to the event bus.

    Used for manual monitoring and testing.

    Args:
        event_type: Type of event (e.g., 'custom', 'test').
        data: Event payload.

    Returns:
        Confirmation of event publication.

    Raises:
        HTTPException: If publication fails.
    """
    try:
        if not event_type:
            raise ValueError("event_type cannot be empty")

        service = get_service()
        service.publish_event(event_type, data)

        return {
            "status": "published",
            "event_type": event_type,
            "data": data,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Error publishing event: %s", e)
        raise HTTPException(status_code=500, detail="Failed to publish event")


@router.get("/logs")
async def recent_logs(limit: int = 100) -> dict[str, Any]:
    """Get recent log entries (application events).

    Alias for event history with common default.

    Args:
        limit: Max log entries (default 100).

    Returns:
        Recent log events.

    Raises:
        HTTPException: If log query fails.
    """
    try:
        service = get_service()
        logs = service.get_event_history(min(limit, 500))

        return {
            "status": "success",
            "total": len(logs),
            "logs": logs,
        }
    except Exception as e:
        logger.error("Error fetching logs: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch logs")
