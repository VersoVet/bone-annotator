"""ML module (coordonne predict, training, dataset, evaluation)."""

from typing import Any


async def ml_status() -> dict[str, Any]:
    """ML module status.

    Returns:
        Status dict with sub-modules.
    """
    return {
        "status": "initialized",
        "sub_modules": ["predict", "training", "dataset", "evaluation"],
    }
