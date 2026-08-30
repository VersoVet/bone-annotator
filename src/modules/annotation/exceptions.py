"""Exceptions for annotation workflow."""


class ActiveTaskExistsError(Exception):
    """Raised when an active task already exists for acquisition+bone_type."""

    def __init__(self, existing: dict) -> None:
        """Store the existing active task row."""
        self.existing = existing
        task_id = existing.get("id", "?")
        super().__init__(f"Active task {task_id} already exists for this acquisition")
