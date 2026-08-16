"""Tests for Pydantic models."""


class TestIngestionModels:
    """Tests for ingestion models."""

    def test_ingestion_sync_response(self) -> None:
        """Test IngestionSyncResponse model."""
        from src.models import IngestionSyncResponse

        resp = IngestionSyncResponse(synced=5, new=2, pending=12, timestamp="2026-08-16T00:00:00Z")
        assert resp.synced == 5
        assert resp.new == 2


class TestAnnotationModels:
    """Tests for annotation task models."""

    def test_annotation_task_request(self) -> None:
        """Test AnnotationTaskRequest model."""
        from src.models import AnnotationTaskRequest

        req = AnnotationTaskRequest(acquisition_id="acq_001", bone_type="humerus")
        assert req.acquisition_id == "acq_001"
        assert req.frames_sample is None

    def test_annotation_task_response(self) -> None:
        """Test AnnotationTaskResponse model."""
        from src.models import AnnotationTaskResponse

        resp = AnnotationTaskResponse(
            task_id="t1",
            acquisition_id="acq_001",
            status="created",
            frame_count=120,
            url="http://cvat/tasks/1",
        )
        assert resp.status == "created"


class TestPredictionModels:
    """Tests for prediction models."""

    def test_bounding_box(self) -> None:
        """Test BoundingBox validation."""
        from src.models import BoundingBox

        bb = BoundingBox(x=10.0, y=20.0, width=100.0, height=50.0)
        assert bb.width == 100.0

    def test_zone(self) -> None:
        """Test Zone model."""
        from src.models import BoundingBox, Zone

        z = Zone(
            class_name="metaphysis",
            confidence=0.95,
            bbox=BoundingBox(x=10, y=20, width=100, height=50),
        )
        assert z.confidence == 0.95

    def test_landmark(self) -> None:
        """Test Landmark model."""
        from src.models import Landmark

        lm = Landmark(landmark_type="epicondyle", confidence=0.88, x=100.0, y=200.0)
        assert lm.landmark_type == "epicondyle"

    def test_frame_prediction(self) -> None:
        """Test FramePrediction model."""
        from src.models import FramePrediction

        fp = FramePrediction(frame_idx=0)
        assert fp.zones == []
        assert fp.landmarks == []


class TestTrainingModels:
    """Tests for training models."""

    def test_training_submit_request(self) -> None:
        """Test TrainingSubmitRequest defaults."""
        from src.models import TrainingSubmitRequest

        req = TrainingSubmitRequest(dataset_yaml="/path/to/dataset.yaml")
        assert req.epochs == 100
        assert req.model == "yolov8m"

    def test_dataset_export_request(self) -> None:
        """Test DatasetExportRequest defaults."""
        from src.models import DatasetExportRequest

        req = DatasetExportRequest(acquisitions=["a1", "a2"])
        assert req.augmentation is False

    def test_health_response(self) -> None:
        """Test HealthResponse model."""
        from src.models import HealthResponse

        resp = HealthResponse(status="healthy", version="0.2.0", dependencies={"pg": True})
        assert resp.status == "healthy"
