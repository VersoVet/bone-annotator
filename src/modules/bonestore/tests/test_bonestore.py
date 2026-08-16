"""Tests for BoneStore service functions."""

from pathlib import Path
from tempfile import TemporaryDirectory


class TestListAcquisitions:
    """Tests for acquisition listing."""

    def test_empty_bonestore(self) -> None:
        """Test listing on empty directory."""
        from src.modules.bonestore.service import list_acquisitions

        with TemporaryDirectory() as tmpdir:
            result = list_acquisitions(tmpdir)
            assert result == []

    def test_nonexistent_path(self) -> None:
        """Test listing on nonexistent path."""
        from src.modules.bonestore.service import list_acquisitions

        result = list_acquisitions("/nonexistent/path")
        assert result == []

    def test_valid_structure(self) -> None:
        """Test listing with valid category/acquisition structure."""
        from src.modules.bonestore.service import list_acquisitions

        with TemporaryDirectory() as tmpdir:
            cat = Path(tmpdir) / "humerus_left_proximal"
            acq = cat / "acq_001" / "raw"
            acq.mkdir(parents=True)
            (acq / "frame_0000.b2nd").touch()
            (acq / "frame_0001.b2nd").touch()

            result = list_acquisitions(tmpdir)
            assert len(result) == 1
            assert result[0]["bone_type"] == "humerus"
            assert result[0]["side"] == "left"
            assert result[0]["frame_count"] == 2


class TestFindAcquisition:
    """Tests for acquisition finding."""

    def test_found(self) -> None:
        """Test finding an existing acquisition."""
        from src.modules.bonestore.service import find_acquisition

        with TemporaryDirectory() as tmpdir:
            cat = Path(tmpdir) / "humerus_left_proximal"
            acq = cat / "acq_001"
            acq.mkdir(parents=True)

            result = find_acquisition(tmpdir, "acq_001")
            assert result is not None
            assert result.name == "acq_001"

    def test_not_found(self) -> None:
        """Test finding nonexistent acquisition."""
        from src.modules.bonestore.service import find_acquisition

        with TemporaryDirectory() as tmpdir:
            result = find_acquisition(tmpdir, "nonexistent")
            assert result is None


class TestGetAcquisitionFrames:
    """Tests for frame listing."""

    def test_no_raw_dir(self) -> None:
        """Test frames from acquisition without raw dir."""
        from src.modules.bonestore.service import get_acquisition_frames

        with TemporaryDirectory() as tmpdir:
            result = get_acquisition_frames(Path(tmpdir))
            assert result == []

    def test_with_frames(self) -> None:
        """Test frames listing with .b2nd files."""
        from src.modules.bonestore.service import get_acquisition_frames

        with TemporaryDirectory() as tmpdir:
            raw = Path(tmpdir) / "raw"
            raw.mkdir()
            (raw / "frame_0000.b2nd").touch()
            (raw / "frame_0001.b2nd").touch()
            (raw / "frame_0002.b2nd").touch()

            result = get_acquisition_frames(Path(tmpdir))
            assert len(result) == 3
            assert result[0]["filename"] == "frame_0000.b2nd"


class TestExtractFrameIndex:
    """Tests for frame index extraction."""

    def test_standard_format(self) -> None:
        """Test extracting from standard filename."""
        from src.modules.bonestore.service import _extract_frame_index

        assert _extract_frame_index("frame_0042") == 42

    def test_no_number(self) -> None:
        """Test extracting from non-numeric filename."""
        from src.modules.bonestore.service import _extract_frame_index

        assert _extract_frame_index("nodigits") == 0

    def test_zero_index(self) -> None:
        """Test extracting zero index."""
        from src.modules.bonestore.service import _extract_frame_index

        assert _extract_frame_index("frame_0000") == 0
