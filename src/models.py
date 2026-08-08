"""Modèles Pydantic pour bone-annotator.

Définitions de schémas request/response pour l'API.
"""

from typing import Optional

from pydantic import BaseModel, Field


# ============================================================================
# Ingestion Models
# ============================================================================


class IngestionSyncResponse(BaseModel):
    """Réponse synchronisation BoneStore."""

    synced: int = Field(..., description="Acquisitions synchronisées")
    new: int = Field(..., description="Nouvelles acquisitions découvertes")
    pending: int = Field(..., description="Acquisitions en attente traitement")
    timestamp: str = Field(..., description="Timestamp synchronisation")


# ============================================================================
# Annotation Models (CVAT)
# ============================================================================


class AnnotationTaskRequest(BaseModel):
    """Requête création tâche annotation CVAT."""

    acquisition_id: str = Field(..., description="ID acquisition BoneStore")
    bone_type: str = Field(
        ..., description="Type os (humerus, femur, tibia, etc.)"
    )
    frames_sample: Optional[int] = Field(
        None, description="Nombre de frames à sampler (None = toutes)"
    )
    assignee: Optional[str] = Field(None, description="Email assigné (optionnel)")


class AnnotationTaskResponse(BaseModel):
    """Réponse création tâche annotation."""

    task_id: str = Field(..., description="ID CVAT task")
    acquisition_id: str = Field(..., description="ID acquisition liée")
    status: str = Field(..., description="Statut: created, pending, in_progress")
    frame_count: int = Field(..., description="Nombre frames")
    url: str = Field(..., description="URL CVAT task")


class AnnotationTaskStatusResponse(BaseModel):
    """Statut d'une tâche annotation."""

    task_id: str = Field(..., description="ID CVAT task")
    status: str = Field(
        ..., description="Statut: created, in_progress, completed, rejected"
    )
    progress_percent: int = Field(..., description="Progression 0-100")
    annotated_frames: int = Field(..., description="Frames annotés")
    total_frames: int = Field(..., description="Total frames")
    assignee: Optional[str] = Field(None, description="Assigné à")
    created_at: str = Field(..., description="Timestamp création")


class AnnotationExportRequest(BaseModel):
    """Requête export annotations CVAT → YOLO."""

    task_ids: list[str] = Field(..., description="IDs CVAT tasks à exporter")
    format: str = Field(default="yolo", description="Format export (yolo)")


class AnnotationExportResponse(BaseModel):
    """Réponse export annotations."""

    dataset_yaml: str = Field(..., description="Chemin dataset YAML")
    images: int = Field(..., description="Nombre images")
    annotations: int = Field(..., description="Nombre annotations")
    zones_count: int = Field(..., description="Nombre zones")
    landmarks_count: int = Field(..., description="Nombre landmarks")


# ============================================================================
# Prediction Models (YOLO)
# ============================================================================


class PredictRequest(BaseModel):
    """Requête prédiction YOLO."""

    acquisition_id: str = Field(..., description="ID acquisition")
    model_version: Optional[str] = Field(
        None, description="Version modèle (None = dernière)"
    )
    confidence_threshold: float = Field(
        default=0.5, ge=0.0, le=1.0, description="Seuil confiance"
    )


class PredictProgressResponse(BaseModel):
    """Statut progression prédiction."""

    task_id: str = Field(..., description="ID tâche prédiction")
    status: str = Field(..., description="Statut: queued, processing, completed")
    frames_predicted: int = Field(..., description="Frames traités")
    total_frames: int = Field(..., description="Total frames")
    eta_seconds: Optional[int] = Field(None, description="ETA secondes")


class BoundingBox(BaseModel):
    """Bounding box détection."""

    x: float = Field(..., ge=0.0, description="X top-left")
    y: float = Field(..., ge=0.0, description="Y top-left")
    width: float = Field(..., gt=0.0, description="Largeur")
    height: float = Field(..., gt=0.0, description="Hauteur")


class Zone(BaseModel):
    """Zone détectée (anatomique ou pathologique)."""

    class_name: str = Field(..., description="Classe zone (metaphysis, diaphysis)")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confiance")
    bbox: BoundingBox = Field(..., description="Bounding box")


class Landmark(BaseModel):
    """Landmark détecté (point anatomique)."""

    landmark_type: str = Field(
        ..., description="Type (medial_epicondyle, lateral_epicondyle)"
    )
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confiance")
    x: float = Field(..., description="Coordonnée X pixels")
    y: float = Field(..., description="Coordonnée Y pixels")


class FramePrediction(BaseModel):
    """Prédictions pour une frame."""

    frame_idx: int = Field(..., ge=0, description="Index frame")
    zones: list[Zone] = Field(default_factory=list, description="Zones détectées")
    landmarks: list[Landmark] = Field(
        default_factory=list, description="Landmarks détectés"
    )


class PredictResultResponse(BaseModel):
    """Résultats prédiction YOLO."""

    task_id: str = Field(..., description="ID tâche")
    status: str = Field(..., description="Statut: completed, failed")
    predictions: list[FramePrediction] = Field(
        ..., description="Prédictions par frame"
    )
    duration_seconds: float = Field(..., gt=0, description="Durée traitement")


# ============================================================================
# Training Models
# ============================================================================


class TrainingSubmitRequest(BaseModel):
    """Requête soumission training YOLO."""

    dataset_yaml: str = Field(..., description="Chemin dataset YAML")
    epochs: int = Field(default=100, ge=1, description="Nombre epochs")
    batch_size: int = Field(default=32, ge=1, description="Taille batch")
    model: str = Field(default="yolov8m", description="Modèle (yolov8s/m/l/x)")
    learning_rate: float = Field(default=0.001, gt=0, description="Learning rate")


class TrainingSubmitResponse(BaseModel):
    """Réponse soumission training."""

    job_id: str = Field(..., description="ID Ray job")
    status: str = Field(..., description="Statut: submitted")
    submission_time: str = Field(..., description="Timestamp soumission")
    eta_minutes: Optional[int] = Field(None, description="ETA minutes")


class TrainingStatusResponse(BaseModel):
    """Statut d'un job training."""

    job_id: str = Field(..., description="ID Ray job")
    status: str = Field(
        ...,
        description="Statut: submitted, running, success, failed, cancelled",
    )
    epoch: Optional[int] = Field(None, description="Epoch courant (si running)")
    total_epochs: int = Field(..., description="Total epochs")
    loss: Optional[float] = Field(None, description="Loss courant")
    map: Optional[float] = Field(None, description="mAP courant")
    progress_percent: int = Field(default=0, ge=0, le=100, description="Progression")


class TrainingMetrics(BaseModel):
    """Métriques training finales."""

    map: float = Field(..., ge=0.0, le=1.0, description="mAP")
    map50: float = Field(..., ge=0.0, le=1.0, description="mAP@50")
    loss: float = Field(..., ge=0.0, description="Loss final")
    precision: Optional[float] = Field(None, ge=0.0, le=1.0, description="Precision")
    recall: Optional[float] = Field(None, ge=0.0, le=1.0, description="Recall")


class TrainingCallbackRequest(BaseModel):
    """Callback depuis ml-compute (Ray job completion)."""

    job_id: str = Field(..., description="ID Ray job")
    status: str = Field(..., description="Statut: success, failed, cancelled")
    result: Optional[dict] = Field(None, description="Résultats job")
    error: Optional[str] = Field(None, description="Message erreur si failed")


class TrainingCallbackResponse(BaseModel):
    """Réponse callback training."""

    acknowledged: bool = Field(..., description="Callback reçu")
    model_version: Optional[str] = Field(None, description="Version modèle créée")


# ============================================================================
# Dataset Models
# ============================================================================


class DatasetExportRequest(BaseModel):
    """Requête export dataset YOLO."""

    acquisitions: list[str] = Field(..., description="IDs acquisitions à exporter")
    split: dict = Field(
        default={"train": 0.8, "val": 0.2},
        description="Split train/val/test (somme=1.0)",
    )
    augmentation: bool = Field(default=False, description="Augmentation données")


class DatasetExportResponse(BaseModel):
    """Réponse export dataset."""

    dataset_yaml: str = Field(..., description="Chemin dataset YAML")
    images: int = Field(..., description="Nombre images")
    annotations: int = Field(..., description="Nombre annotations")


# ============================================================================
# Status Models
# ============================================================================


class HealthResponse(BaseModel):
    """Réponse health check."""

    status: str = Field(..., description="Status: healthy, degraded")
    version: str = Field(..., description="Version skill")
    dependencies: dict = Field(..., description="État dépendances")


class ReadyResponse(BaseModel):
    """Réponse readiness check."""

    status: str = Field(..., description="Status: ready, not_ready")


class ApiStatusResponse(BaseModel):
    """Réponse statut API."""

    service: str = Field(..., description="Nom service")
    version: str = Field(..., description="Version")
    status: str = Field(..., description="Statut: development, production")
    dependencies: dict = Field(..., description="État dépendances")
