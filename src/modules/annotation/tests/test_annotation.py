"""Tests for annotation workflow models and format conversion."""


class TestAnnotationModels:
    """Tests for annotation Pydantic models."""

    def test_create_task_request_defaults(self) -> None:
        """Test CreateTaskRequest with defaults."""
        from src.modules.annotation.models import CreateTaskRequest

        req = CreateTaskRequest(acquisition_id="acq_001", bone_type="humerus")
        assert req.source_name == "bonestore"
        assert req.region == "entire"
        assert req.pipeline_preset is None
        assert req.pre_annotate is False
        assert req.assignee is None

    def test_create_task_request_full(self) -> None:
        """Test CreateTaskRequest with all fields."""
        from src.modules.annotation.models import CreateTaskRequest

        req = CreateTaskRequest(
            source_name="bonestore",
            acquisition_id="acq_002",
            bone_type="radius",
            region="proximal",
            assignee="user1",
            pipeline_preset="high_contrast",
            pre_annotate=True,
        )
        assert req.bone_type == "radius"
        assert req.pre_annotate is True
        assert req.assignee == "user1"

    def test_validate_request(self) -> None:
        """Test ValidateRequest model."""
        from src.modules.annotation.models import ValidateRequest

        req = ValidateRequest(validated_by="reviewer1", decision="validated", notes="LGTM")
        assert req.decision == "validated"
        assert req.notes == "LGTM"

    def test_task_response_serialization(self) -> None:
        """Test TaskResponse model_dump."""
        from src.modules.annotation.models import TaskProgress, TaskResponse

        resp = TaskResponse(
            id=1,
            acquisition_id="acq_001",
            status="preparing",
            bone_type="humerus",
            frame_count=120,
            progress=TaskProgress(step="preparing", detail="Preparing dataset..."),
        )
        d = resp.model_dump()
        assert d["id"] == 1
        assert d["status"] == "preparing"
        assert d["progress"]["step"] == "preparing"
        assert d["cvat_task_id"] is None

    def test_build_task_progress(self) -> None:
        """Test status/notes mapping for async task polling."""
        from src.modules.annotation.service import _build_task_progress

        assert _build_task_progress("preparing", "Preparing dataset...").step == "preparing"
        assert _build_task_progress("uploading", "Uploading 120 frames").detail == "Uploading 120 frames"
        assert _build_task_progress("created", "Ready") is None
        assert _build_task_progress("failed", "CVAT timeout").step == "failed"

    def test_sync_result(self) -> None:
        """Test SyncResult model."""
        from src.modules.annotation.models import SyncResult

        result = SyncResult(task_id=1, synced_frames=10, zones_count=5, landmarks_count=3, author="user1")
        assert result.synced_frames == 10
        assert result.author == "user1"

    def test_pre_annotate_response(self) -> None:
        """Test PreAnnotateResponse model."""
        from src.modules.annotation.models import PreAnnotateResponse

        resp = PreAnnotateResponse(task_id=1, cvat_task_id=42, status="requested", bone_ml_status="accepted")
        assert resp.cvat_task_id == 42


class TestCvatFormatLabels:
    """Tests for label-generator to CVAT format conversion."""

    def test_zones_to_cvat(self) -> None:
        """Test zone labels conversion."""
        from src.modules.cvat.format import labels_to_cvat_format

        anatomy = {
            "zones": [
                {"id": "metaphysis", "label": "Metaphysis", "color": "#00FF00"},
                {"id": "diaphysis", "label": "Diaphysis", "color": "#0000FF"},
            ],
            "landmarks": [],
        }
        labels = labels_to_cvat_format(anatomy)
        assert len(labels) == 2
        assert labels[0]["name"] == "metaphysis"
        assert labels[0]["type"] == "any"

    def test_landmarks_to_cvat(self) -> None:
        """Test landmark labels conversion."""
        from src.modules.cvat.format import labels_to_cvat_format

        anatomy = {
            "zones": [],
            "landmarks": [
                {"id": "greater_tubercle", "label": "Greater Tubercle"},
            ],
        }
        labels = labels_to_cvat_format(anatomy)
        assert len(labels) == 1
        assert labels[0]["type"] == "points"

    def test_no_duplicates(self) -> None:
        """Test duplicate labels are filtered."""
        from src.modules.cvat.format import labels_to_cvat_format

        anatomy = {
            "zones": [{"id": "zone_a"}, {"id": "zone_a"}],
            "landmarks": [{"id": "zone_a"}],
        }
        labels = labels_to_cvat_format(anatomy)
        assert len(labels) == 1
