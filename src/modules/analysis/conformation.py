"""Conformation analysis via PCA shape models.

Builds statistical shape models from landmark data across specimens,
enabling detection of morphological deviations (dysplasia, deformities).
"""

import json
import logging
from pathlib import Path

import numpy as np
from scipy.spatial.distance import mahalanobis

from .landmarks import (
    align_landmarks,
    flatten_landmarks,
    normalize_landmarks,
    unflatten_landmarks,
)

logger = logging.getLogger(__name__)

# Bone types and landmark names - import from config when available
BONE_TYPES = ["femur", "humerus", "radius", "ulna", "scapula", "fibula"]
LANDMARK_NAMES: dict[str, list[str]] = {
    "femur": ["femoral_head_center", "intercondylar_fossa"],
    "humerus": ["head_center", "trochlea"],
    "radius": ["radial_head", "styloid_process"],
    "ulna": ["olecranon", "ulnar_styloid"],
    "scapula": ["glenoid_center", "acromion"],
    "fibula": ["fibular_head", "lateral_malleolus"],
}


class ShapeModel:
    """PCA-based statistical shape model for a single bone type.

    Built from aligned landmark coordinates across multiple specimens.
    Each principal component captures an axis of morphological variation.
    """

    def __init__(self, bone_type: str, n_components: int = 10) -> None:
        self.bone_type = bone_type
        self.n_components = n_components
        self.n_landmarks = len(LANDMARK_NAMES.get(bone_type, []))
        self.vector_dim = self.n_landmarks * 2

        # PCA results (populated by fit())
        self.mean_shape: np.ndarray | None = None  # (2N,)
        self.components: np.ndarray | None = None  # (K, 2N)
        self.explained_variance: np.ndarray | None = None  # (K,)
        self.explained_variance_ratio: np.ndarray | None = None
        self.cov_inv: np.ndarray | None = None  # For Mahalanobis
        self.n_specimens: int = 0

    def fit(self, specimens: list[np.ndarray]) -> None:
        """Fit PCA shape model from aligned landmark vectors.

        Args:
            specimens: List of (2N,) flattened landmark vectors,
                       already normalized and aligned.
        """
        if len(specimens) < 3:
            logger.warning(
                "ShapeModel(%s): only %d specimens, need ≥3 for PCA",
                self.bone_type,
                len(specimens),
            )
            return

        data = np.stack(specimens)  # (M, 2N)
        self.n_specimens = len(specimens)

        # Center
        self.mean_shape = data.mean(axis=0)
        centered = data - self.mean_shape

        # PCA via SVD
        _, S, Vt = np.linalg.svd(centered, full_matrices=False)
        n_comp = min(self.n_components, len(S))

        self.components = Vt[:n_comp]  # (K, 2N)
        total_var = np.sum(S**2) / (len(specimens) - 1)
        self.explained_variance = (S[:n_comp] ** 2) / (len(specimens) - 1)
        self.explained_variance_ratio = self.explained_variance / total_var if total_var > 1e-12 else np.zeros(n_comp)

        # Covariance inverse for Mahalanobis distance (pinv for singular matrices)
        shape_codes = centered @ self.components.T  # (M, K)
        cov = np.cov(shape_codes.T)
        if cov.ndim == 0:
            cov = np.array([[cov]])
        self.cov_inv = np.linalg.pinv(cov)

        logger.info(
            "ShapeModel(%s): fitted on %d specimens, %d components, %.1f%% variance explained",
            self.bone_type,
            self.n_specimens,
            n_comp,
            float(np.sum(self.explained_variance_ratio)) * 100,
        )

    def project(self, shape_vector: np.ndarray) -> np.ndarray:
        """Project a shape into PCA space (shape code).

        Args:
            shape_vector: (2N,) aligned landmark vector.

        Returns:
            (K,) shape code.

        Raises:
            RuntimeError: If model not fitted (mean_shape is None).
        """
        if self.mean_shape is None:
            msg = "Model not fitted"
            raise RuntimeError(msg)
        if shape_vector.shape != self.mean_shape.shape:
            msg = f"Shape mismatch: got {shape_vector.shape}, expected {self.mean_shape.shape}"
            raise ValueError(msg)
        centered = shape_vector - self.mean_shape
        return centered @ self.components.T

    def reconstruct(self, shape_code: np.ndarray) -> np.ndarray:
        """Reconstruct a shape from PCA code.

        Args:
            shape_code: (K,) PCA coefficients.

        Returns:
            (2N,) reconstructed shape vector.

        Raises:
            RuntimeError: If model not fitted.
        """
        if self.mean_shape is None:
            msg = "Model not fitted"
            raise RuntimeError(msg)
        return self.mean_shape + shape_code @ self.components

    def mahalanobis_distance(self, shape_vector: np.ndarray) -> float:
        """Compute Mahalanobis distance of a shape from the population mean.

        High values indicate unusual morphology.

        Raises:
            RuntimeError: If model not fitted.
        """
        if self.cov_inv is None:
            msg = "Model not fitted"
            raise RuntimeError(msg)
        code = self.project(shape_vector)
        mean_code = np.zeros_like(code)
        return float(mahalanobis(code, mean_code, self.cov_inv))

    def detect_deviation(self, shape_vector: np.ndarray) -> dict:
        """Analyze a specimen for morphological deviations.

        Returns:
            Dict with shape_code, Mahalanobis distance, flags, and
            per-component deviations.

        Raises:
            RuntimeError: If model not fitted.
        """
        if self.mean_shape is None:
            msg = "Model not fitted"
            raise RuntimeError(msg)

        code = self.project(shape_vector)
        m_dist = self.mahalanobis_distance(shape_vector)

        # Per-component z-scores
        component_deviations: list[dict] = []
        if self.explained_variance is not None:
            stds = np.sqrt(self.explained_variance)
            for i, (c, s) in enumerate(zip(code, stds, strict=False)):
                z = abs(c) / s if s > 1e-8 else 0.0
                component_deviations.append(
                    {
                        "component": i,
                        "value": float(c),
                        "z_score": float(z),
                        "variance_explained": float(self.explained_variance_ratio[i]),
                    }
                )

        # Flags
        flags: list[str] = []
        if m_dist > 3.0:
            flags.append("severe_deviation")
        elif m_dist > 2.0:
            flags.append("moderate_deviation")

        # Check individual components for extreme deviations
        flags.extend(
            f"extreme_pc{cd['component']}"
            for cd in component_deviations
            if cd["z_score"] > 3.0 and cd["variance_explained"] > 0.05
        )

        return {
            "shape_code": code.tolist(),
            "mahalanobis_distance": m_dist,
            "flags": flags,
            "component_deviations": component_deviations,
        }

    def summary(self) -> dict:
        """Return a summary of the shape model."""
        return {
            "bone_type": self.bone_type,
            "n_specimens": self.n_specimens,
            "n_landmarks": self.n_landmarks,
            "n_components": len(self.explained_variance) if self.explained_variance is not None else 0,
            "variance_explained_total": float(np.sum(self.explained_variance_ratio))
            if self.explained_variance_ratio is not None
            else 0.0,
            "variance_per_component": self.explained_variance_ratio.tolist()
            if self.explained_variance_ratio is not None
            else [],
        }

    def save(self, path: str) -> None:
        """Save model to JSON file."""
        data = {
            "bone_type": self.bone_type,
            "n_components": self.n_components,
            "n_landmarks": self.n_landmarks,
            "n_specimens": self.n_specimens,
            "mean_shape": self.mean_shape.tolist() if self.mean_shape is not None else None,
            "components": self.components.tolist() if self.components is not None else None,
            "explained_variance": self.explained_variance.tolist() if self.explained_variance is not None else None,
            "explained_variance_ratio": self.explained_variance_ratio.tolist()
            if self.explained_variance_ratio is not None
            else None,
            "cov_inv": self.cov_inv.tolist() if self.cov_inv is not None else None,
        }
        with Path(path).open("w") as f:
            json.dump(data, f, indent=2)
        logger.info("Shape model saved: %s", path)

    @classmethod
    def load(cls, path: str) -> "ShapeModel":
        """Load model from JSON file."""
        with Path(path).open() as f:
            data = json.load(f)
        model = cls(data["bone_type"], data["n_components"])
        model.n_landmarks = data["n_landmarks"]
        model.n_specimens = data["n_specimens"]
        if data["mean_shape"] is not None:
            model.mean_shape = np.array(data["mean_shape"])
            model.components = np.array(data["components"])
            model.explained_variance = np.array(data["explained_variance"])
            model.explained_variance_ratio = np.array(data["explained_variance_ratio"])
            model.cov_inv = np.array(data["cov_inv"])
        return model


class ConformationAnalyzer:
    """Manages shape models for all bone types and performs conformation analysis."""

    def __init__(self, models_dir: str | None = None) -> None:
        self.models: dict[str, ShapeModel] = {}
        if models_dir:
            self._load_models(models_dir)

    def _load_models(self, models_dir: str) -> None:
        d = Path(models_dir)
        for bone in BONE_TYPES:
            path = d / f"shape_model_{bone}.json"
            if path.exists():
                self.models[bone] = ShapeModel.load(str(path))
                logger.info("Loaded shape model for %s", bone)

    def build_model(
        self,
        bone_type: str,
        specimens_landmarks: list[list[dict]],
        image_size: int = 512,
        n_components: int = 10,
    ) -> ShapeModel:
        """Build a shape model for one bone type from landmark data.

        Args:
            bone_type: Type of bone.
            specimens_landmarks: List of per-specimen landmark lists.
            image_size: Image coordinate space.
            n_components: Number of PCA components.
        """
        vectors: list[np.ndarray] = []
        for landmarks in specimens_landmarks:
            coords = normalize_landmarks(landmarks, image_size)
            aligned = align_landmarks(coords)
            vectors.append(flatten_landmarks(aligned))

        model = ShapeModel(bone_type, n_components)
        model.fit(vectors)
        self.models[bone_type] = model
        return model

    def analyze(
        self,
        bone_type: str,
        landmarks: list[dict],
        image_size: int = 512,
    ) -> dict:
        """Analyze conformation of a single specimen.

        Returns shape code, Mahalanobis distance, and deviation flags.
        """
        if bone_type not in self.models:
            return {
                "error": f"No shape model for {bone_type}",
                "shape_code": [],
                "mahalanobis_distance": 0.0,
                "flags": ["no_model"],
            }

        model = self.models[bone_type]
        coords = normalize_landmarks(landmarks, image_size)
        aligned = align_landmarks(
            coords,
            reference=unflatten_landmarks(model.mean_shape, model.n_landmarks)
            if model.mean_shape is not None
            else None,
        )
        vector = flatten_landmarks(aligned)

        return model.detect_deviation(vector)

    def get_summary(self, bone_type: str) -> dict:
        """Return summary statistics for a bone type model."""
        if bone_type in self.models:
            return self.models[bone_type].summary()
        return {"error": f"No model for {bone_type}"}

    def save_all(self, models_dir: str) -> None:
        """Save all shape models to the given directory."""
        d = Path(models_dir)
        d.mkdir(parents=True, exist_ok=True)
        for bone, model in self.models.items():
            model.save(str(d / f"shape_model_{bone}.json"))
