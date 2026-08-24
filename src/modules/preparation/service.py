"""Dataset preparation service — raw .b2nd to annotation-ready PNG 16-bit.

Applies imaging-sdk pipelines to convert raw fluoroscopy frames into
enhanced images suitable for annotation in CVAT.
"""

import json
import logging
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import numpy as np
import yaml

from src.modules.imaging.imaging import _read_b2nd_frame

logger = logging.getLogger(__name__)

_SKILL_ROOT = Path(__file__).parent.parent.parent.parent


def _load_pipeline_dir() -> Path:
    """Load pipeline_dir from config/sources.yaml or use default.

    Returns:
        Path to the pipeline directory.
    """
    config_path = _SKILL_ROOT / "config" / "sources.yaml"
    try:
        with open(config_path) as f:
            config = yaml.safe_load(f)
        pipeline_dir = config.get("imaging", {}).get("pipeline_dir")
        if pipeline_dir:
            return Path(pipeline_dir)
    except Exception:
        pass
    # Fallback: local data/pipelines
    fallback = _SKILL_ROOT / "data" / "pipelines"
    fallback.mkdir(parents=True, exist_ok=True)
    return fallback


def _get_pipeline_manager() -> Any:
    """Lazy-load imaging-sdk JSONPipelineManager.

    Uses pipeline_dir from config (vet-fluoro-studio) to access
    pipelines created by the studio app.

    Returns:
        JSONPipelineManager instance or None if unavailable.
    """
    try:
        from imaging_sdk import JSONPipelineManager

        pipeline_dir = _load_pipeline_dir()
        return JSONPipelineManager(pipeline_dir=pipeline_dir)
    except ImportError:
        logger.warning("imaging_sdk not available, raw conversion only")
        return None


def _save_png_16bit(image: np.ndarray, output_path: Path) -> None:
    """Save numpy array as 16-bit PNG.

    Args:
        image: Image array (uint16 or float).
        output_path: Output file path.
    """
    from PIL import Image

    if image.dtype in (np.float32, np.float64):
        image = (np.clip(image, 0, 1) * 65535).astype(np.uint16)
    elif image.dtype != np.uint16:
        image = image.astype(np.uint16)

    pil_img = Image.fromarray(image)
    pil_img.save(str(output_path), format="PNG")


class PreparedDataset:
    """Result of dataset preparation."""

    def __init__(
        self,
        dataset_id: str,
        path: Path,
        frame_count: int,
        pipeline_preset: str,
        pipeline_config: list[dict[str, Any]],
        bone_type: str,
        acquisition_id: str,
    ) -> None:
        """Initialize prepared dataset descriptor."""
        self.dataset_id = dataset_id
        self.path = path
        self.frame_count = frame_count
        self.pipeline_preset = pipeline_preset
        self.pipeline_config = pipeline_config
        self.bone_type = bone_type
        self.acquisition_id = acquisition_id

    def to_dict(self) -> dict[str, Any]:
        """Serialize to dict."""
        return {
            "dataset_id": self.dataset_id,
            "path": str(self.path),
            "frame_count": self.frame_count,
            "pipeline_preset": self.pipeline_preset,
            "bone_type": self.bone_type,
            "acquisition_id": self.acquisition_id,
        }


class DatasetPreparationService:
    """Prepares annotation-ready datasets from raw acquisitions."""

    def __init__(self, storage_root: Path | None = None) -> None:
        """Initialize preparation service."""
        self.storage_root = storage_root or Path("data/annotation-datasets")
        self.storage_root.mkdir(parents=True, exist_ok=True)
        self._manager = None

    @property
    def manager(self) -> Any:
        """Lazy-loaded imaging-sdk pipeline manager."""
        if self._manager is None:
            self._manager = _get_pipeline_manager()
        return self._manager

    async def prepare_dataset(
        self,
        acquisition_path: Path,
        acquisition_id: str,
        bone_type: str,
        pipeline_preset: str = "replay_membre",
        custom_pipeline: list[dict[str, Any]] | None = None,
        image_size: int | None = None,
    ) -> PreparedDataset:
        """Prepare annotation dataset from raw .b2nd frames.

        Args:
            acquisition_path: Path to acquisition directory.
            acquisition_id: Acquisition identifier.
            bone_type: Bone type for anatomy-aware processing.
            pipeline_preset: Imaging-sdk preset name.
            custom_pipeline: Custom pipeline config (overrides preset).
            image_size: Optional resize (None = keep original).

        Returns:
            PreparedDataset with path and metadata.
        """
        timestamp = datetime.now(tz=UTC).strftime("%Y%m%d_%H%M%S")
        dataset_id = f"{acquisition_id}_{pipeline_preset}_{timestamp}"
        output_dir = self.storage_root / dataset_id / "images"
        output_dir.mkdir(parents=True, exist_ok=True)

        raw_dir = acquisition_path / "raw"
        frame_files = sorted(raw_dir.glob("*.b2nd")) if raw_dir.exists() else []

        if not frame_files:
            msg = f"No .b2nd frames found in {raw_dir}"
            raise ValueError(msg)

        # Resolve pipeline config
        pipeline_config = custom_pipeline or self._load_preset(pipeline_preset, bone_type)

        # Process frames
        count = 0
        for frame_path in frame_files:
            try:
                raw = _read_b2nd_frame(frame_path)
                processed = self._apply_pipeline(
                    raw, pipeline_config,
                    context=pipeline_preset, bone_type=bone_type,
                )
                if image_size:
                    processed = self._resize(processed, image_size)
                out_path = output_dir / f"{frame_path.stem}.png"
                _save_png_16bit(processed, out_path)
                count += 1
            except Exception as e:
                logger.warning("Failed to process %s: %s", frame_path.name, e)

        # Save metadata
        metadata = {
            "dataset_id": dataset_id,
            "acquisition_id": acquisition_id,
            "bone_type": bone_type,
            "pipeline_preset": pipeline_preset,
            "pipeline_config": pipeline_config,
            "frame_count": count,
            "created_at": datetime.now(tz=UTC).isoformat(),
            "image_format": "png_16bit",
        }
        meta_path = self.storage_root / dataset_id / "metadata.json"
        meta_path.write_text(json.dumps(metadata, indent=2))

        logger.info("Dataset prepared: %s (%d frames)", dataset_id, count)
        return PreparedDataset(
            dataset_id=dataset_id,
            path=output_dir.parent,
            frame_count=count,
            pipeline_preset=pipeline_preset,
            pipeline_config=pipeline_config,
            bone_type=bone_type,
            acquisition_id=acquisition_id,
        )

    def _load_preset(self, preset_name: str, bone_type: str) -> list[dict[str, Any]]:
        """Load imaging-sdk preset configuration.

        Args:
            preset_name: Pipeline context name (e.g. replay_membre).
            bone_type: Bone type for anatomy-aware selection.

        Returns:
            Pipeline filter config list, or fallback if unavailable.
        """
        if self.manager:
            try:
                pipeline = self.manager.load_pipeline(preset_name)
                if pipeline and isinstance(pipeline, dict):
                    return pipeline.get("filters", [])
            except Exception as e:
                logger.warning("Failed to load pipeline %s: %s", preset_name, e)

        # Fallback: basic enhancement pipeline (no imaging-sdk)
        return [
            {"name": "window_level", "enabled": True, "params": {"width": 4000, "center": 2000}},
            {"name": "clahe", "enabled": True, "params": {"clip_limit": 2.0, "grid_size": 8}},
        ]

    def _apply_pipeline(
        self,
        image: np.ndarray,
        pipeline_config: list[dict[str, Any]],
        context: str = "replay_membre",
        bone_type: str | None = None,
    ) -> np.ndarray:
        """Apply imaging-sdk pipeline to a frame.

        Args:
            image: Raw uint16 frame.
            pipeline_config: Pipeline filter config (for logging/metadata).
            context: imaging-sdk context name for apply_pipeline().
            bone_type: Optional anatomy hint for pipeline optimization.

        Returns:
            Processed image array.
        """
        if self.manager:
            try:
                return self.manager.apply_pipeline(
                    image, context, anatomy=bone_type,
                )
            except Exception as e:
                logger.warning("Pipeline %s failed, returning raw: %s", context, e)
        return image

    def _resize(self, image: np.ndarray, size: int) -> np.ndarray:
        """Resize image to square dimensions."""
        from PIL import Image

        pil = Image.fromarray(image)
        pil = pil.resize((size, size), Image.LANCZOS)
        return np.array(pil)

    def list_datasets(self) -> list[dict[str, Any]]:
        """List all prepared datasets."""
        datasets = []
        for meta_path in sorted(self.storage_root.glob("*/metadata.json")):
            try:
                data = json.loads(meta_path.read_text())
                data["path"] = str(meta_path.parent)
                datasets.append(data)
            except Exception as e:
                logger.warning("Failed to read %s: %s", meta_path, e)
        return datasets

    def get_presets(self, bone_type: str) -> list[dict[str, Any]]:
        """List available imaging-sdk presets for a bone type.

        Args:
            bone_type: Bone type for preset recommendation.

        Returns:
            List of preset descriptors from imaging-sdk.
        """
        pipelines = self.list_all_pipelines()
        limb_bones = {"humerus", "radius", "ulna", "femur", "tibia", "fibula"}
        spine_bones = {"vertebra", "rachis", "spine", "cervical", "lumbar", "thoracic"}
        for p in pipelines:
            if bone_type in limb_bones:
                p["recommended"] = p["name"] == "replay_membre"
            elif bone_type in spine_bones:
                p["recommended"] = p["name"] == "replay_rachis"
            else:
                p["recommended"] = p["name"] == "replay"
        return pipelines

    def list_all_pipelines(self) -> list[dict[str, Any]]:
        """List all available pipelines from imaging-sdk + vet-fluoro-studio.

        Returns:
            List of pipeline descriptors with name, description, filters count.
        """
        if not self.manager:
            return [{"name": "replay_membre", "description": "Standard (fallback)", "filters": 2}]

        pipelines = []
        for name in self.manager.list_pipelines():
            try:
                info = self.manager.load_pipeline(name)
                pipelines.append({
                    "name": name,
                    "display_name": info.get("name", name) if info else name,
                    "description": info.get("description", "") if info else "",
                    "filters": len(info.get("filters", [])) if info else 0,
                    "context": info.get("context", name) if info else name,
                })
            except Exception as e:
                logger.warning("Failed to load pipeline %s: %s", name, e)
                pipelines.append({"name": name, "description": "", "filters": 0})
        return pipelines


# Module singleton
_service: DatasetPreparationService | None = None


def get_service(storage_root: Path | None = None) -> DatasetPreparationService:
    """Get or create the preparation service singleton."""
    global _service
    if _service is None:
        _service = DatasetPreparationService(storage_root)
    return _service
