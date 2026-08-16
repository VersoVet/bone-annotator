"""Tests for ingestion registry."""

from pathlib import Path
from tempfile import TemporaryDirectory


class TestIngestionStatus:
    """Tests for IngestionStatus enum."""

    def test_status_values(self) -> None:
        """Test status enum values exist."""
        from src.modules.ingestion.registry import IngestionStatus

        assert IngestionStatus.DISCOVERED == "discovered"
        assert IngestionStatus.IN_PROGRESS == "in_progress"
        assert IngestionStatus.COMPLETED == "completed"
        assert IngestionStatus.FAILED == "failed"


class TestIngestionRegistry:
    """Tests for IngestionRegistry SQLite operations."""

    def test_init_creates_db(self) -> None:
        """Test registry creates SQLite database."""
        from src.modules.ingestion.registry import IngestionRegistry

        with TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test_registry.db"
            registry = IngestionRegistry(db_path)
            assert db_path.exists()
            assert registry is not None

    def test_get_stats_empty(self) -> None:
        """Test stats on empty registry."""
        from src.modules.ingestion.registry import IngestionRegistry

        with TemporaryDirectory() as tmpdir:
            registry = IngestionRegistry(Path(tmpdir) / "test.db")
            stats = registry.get_stats()
            assert stats["by_status"]["discovered"] == 0
            assert stats["by_status"]["completed"] == 0

    def test_get_pending_empty(self) -> None:
        """Test pending list on empty registry."""
        from src.modules.ingestion.registry import IngestionRegistry

        with TemporaryDirectory() as tmpdir:
            registry = IngestionRegistry(Path(tmpdir) / "test.db")
            pending = registry.get_pending()
            assert pending == []

    def test_discover_empty_bonestore(self) -> None:
        """Test discover on empty directory."""
        from src.modules.ingestion.registry import IngestionRegistry

        with TemporaryDirectory() as tmpdir:
            registry = IngestionRegistry(Path(tmpdir) / "test.db")
            bs_dir = Path(tmpdir) / "bonestore"
            bs_dir.mkdir()
            count = registry.discover_acquisitions(bs_dir)
            assert count == 0

    def test_mark_started(self) -> None:
        """Test marking acquisition as started."""
        from src.modules.ingestion.registry import IngestionRegistry

        with TemporaryDirectory() as tmpdir:
            registry = IngestionRegistry(Path(tmpdir) / "test.db")
            # Create a category + acquisition in bonestore
            bs_dir = Path(tmpdir) / "bonestore"
            cat = bs_dir / "humerus_left_proximal"
            acq = cat / "acq_test" / "raw"
            acq.mkdir(parents=True)
            (acq / "frame_0000.b2nd").touch()
            registry.discover_acquisitions(bs_dir)
            registry.mark_started("acq_test")
            stats = registry.get_stats()
            assert stats["by_status"]["in_progress"] >= 0

    def test_mark_completed(self) -> None:
        """Test marking acquisition as completed."""
        from src.modules.ingestion.registry import IngestionRegistry

        with TemporaryDirectory() as tmpdir:
            registry = IngestionRegistry(Path(tmpdir) / "test.db")
            bs_dir = Path(tmpdir) / "bonestore"
            cat = bs_dir / "humerus_left_proximal"
            acq = cat / "acq_done" / "raw"
            acq.mkdir(parents=True)
            (acq / "frame_0000.b2nd").touch()
            registry.discover_acquisitions(bs_dir)
            registry.mark_started("acq_done")
            registry.mark_completed("acq_done", processed=1, selected=1)
            stats = registry.get_stats()
            assert stats["by_status"]["completed"] >= 1
