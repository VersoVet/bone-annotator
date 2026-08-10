# bone-annotator - API Endpoints

Annotation des images osseuses fluoroscopie 360°.

---

## Santé & Statut

### `GET /health`
Vérification de santé du service.

**Response** (200):
```json
{
  "status": "healthy",
  "version": "0.1.0",
  "dependencies": {
    "bonestore": true,
    "postgres": true,
    "qdrant": true,
    "cvat": true,
    "redis": true
  }
}
```

**Response** (503 - service down):
```json
{
  "detail": "dependencies_not_ready"
}
```

---

### `GET /ready`
Readiness check pour orchestration (Kubernetes, systemd).

**Response** (200):
```json
{
  "status": "ready"
}
```

**Response** (503):
```json
{
  "status": "not_ready"
}
```

---

### `GET /api/status`
Statut détaillé du service et modules.

**Response** (200):
```json
{
  "service": "bone-annotator",
  "version": "0.1.0",
  "status": "development",
  "dependencies": {
    "bonestore": "✓",
    "postgres": "✓",
    "qdrant": "✓",
    "cvat": "✓",
    "redis": "✓"
  }
}
```

---

## Ingestion (Sync BoneStore)

### `POST /api/ingestion/sync`
Synchronisation des acquisitions BoneStore → registre ingestion.

**Response** (200):
```json
{
  "synced": 5,
  "new": 2,
  "pending": 12,
  "timestamp": "2026-08-08T10:30:00Z"
}
```

---

## Annotation

### `POST /api/annotation/task`
Créer une tâche CVAT pour une acquisition.

**Request**:
```json
{
  "acquisition_id": "acq_001_humerus",
  "bone_type": "humerus",
  "frames_sample": 10,
  "assignee": "radiologist@hospital.fr"
}
```

**Response** (201):
```json
{
  "task_id": "cvat_task_42",
  "acquisition_id": "acq_001_humerus",
  "status": "created",
  "frame_count": 120,
  "url": "http://cvat.synapse:8080/tasks/42"
}
```

---

### `GET /api/annotation/task/{task_id}`
Récupérer le statut d'une tâche CVAT.

**Response** (200):
```json
{
  "task_id": "cvat_task_42",
  "status": "in_progress",
  "progress_percent": 45,
  "annotated_frames": 54,
  "total_frames": 120,
  "assignee": "radiologist@hospital.fr",
  "created_at": "2026-08-05T14:20:00Z"
}
```

---

### `POST /api/annotation/export`
Exporter annotations depuis CVAT → format YOLO dataset.

**Request**:
```json
{
  "task_ids": ["cvat_task_42", "cvat_task_43"],
  "format": "yolo"
}
```

**Response** (200):
```json
{
  "dataset_yaml": "/opt/onyx/skills/bone-annotator/data/datasets/dataset_20260808.yaml",
  "images": 240,
  "annotations": 240,
  "zones_count": 145,
  "landmarks_count": 890
}
```

---

## Prédiction (YOLO)

### `POST /api/predict`
Prédictions YOLO sur une acquisition (pré-annotation).

**Request**:
```json
{
  "acquisition_id": "acq_001_humerus",
  "model_version": "yolov8_20260801",
  "confidence_threshold": 0.5
}
```

**Response** (200):
```json
{
  "task_id": "pred_12345",
  "status": "processing",
  "frames_predicted": 0,
  "total_frames": 120,
  "eta_seconds": 45
}
```

---

### `GET /api/predict/result/{task_id}`
Récupérer résultats prédiction.

**Response** (200):
```json
{
  "task_id": "pred_12345",
  "status": "completed",
  "predictions": [
    {
      "frame_idx": 0,
      "zones": [
        {"class": "metaphysis", "confidence": 0.94, "bbox": [10, 20, 100, 120]}
      ],
      "landmarks": [
        {"type": "medial_epicondyle", "confidence": 0.87, "x": 55, "y": 80}
      ]
    }
  ],
  "duration_seconds": 45
}
```

---

## Training

### `POST /api/training/submit`
Soumettre un job training YOLO à ml-compute.

**Request**:
```json
{
  "dataset_yaml": "/path/to/dataset.yaml",
  "epochs": 100,
  "batch_size": 32,
  "model": "yolov8m"
}
```

**Response** (201):
```json
{
  "job_id": "ray_job_xyz789",
  "status": "submitted",
  "submission_time": "2026-08-08T10:40:00Z",
  "eta_minutes": 120
}
```

---

### `GET /api/training/status/{job_id}`
Récupérer le statut d'un job training.

**Response** (200):
```json
{
  "job_id": "ray_job_xyz789",
  "status": "running",
  "epoch": 45,
  "total_epochs": 100,
  "loss": 0.12,
  "map": 0.78,
  "progress_percent": 45
}
```

---

### `POST /api/training/callback`
Callback de ml-compute (notification completion).

**Request** (from ml-compute):
```json
{
  "job_id": "ray_job_xyz789",
  "status": "success",
  "result": {
    "model_path": "s3://models/yolov8m_20260808.pt",
    "metrics": {
      "map": 0.82,
      "map50": 0.91,
      "loss": 0.08
    }
  }
}
```

**Response** (200):
```json
{
  "acknowledged": true,
  "model_version": "yolov8m_20260808"
}
```

---

## Dataset

### `GET /api/dataset/list`
Lister les datasets disponibles.

**Response** (200):
```json
{
  "datasets": [
    {
      "yaml": "dataset_20260808.yaml",
      "created": "2026-08-08T10:00:00Z",
      "images": 240,
      "train": 192,
      "val": 48,
      "zones": 145,
      "landmarks": 890
    }
  ]
}
```

---

### `POST /api/dataset/export`
Exporter annotations → YOLO format.

**Request**:
```json
{
  "acquisitions": ["acq_001", "acq_002"],
  "split": {"train": 0.8, "val": 0.2},
  "augmentation": true
}
```

**Response** (200):
```json
{
  "dataset_yaml": "/opt/onyx/skills/bone-annotator/data/datasets/dataset_20260808.yaml",
  "images": 240,
  "annotations": 240
}
```

---

## Dashboard (SSE)

### `GET /api/dashboard/events`
Stream SSE des événements pipeline (WebSocket alternative).

**Headers**:
```
Content-Type: text/event-stream
Cache-Control: no-cache
```

**Events**:
```
event: ingestion_complete
data: {"acquisition_id": "acq_001", "frames": 120}

event: prediction_complete
data: {"task_id": "pred_123", "accuracy": 0.82}

event: training_update
data: {"job_id": "ray_job_xyz", "epoch": 45, "loss": 0.12}
```

---

### `GET /api/dashboard/training-status`
Statut en direct de tous les training jobs.

**Response** (200):
```json
{
  "active_jobs": [
    {
      "job_id": "ray_job_xyz789",
      "status": "running",
      "progress_percent": 45,
      "eta_minutes": 65
    }
  ],
  "recent_completed": [
    {
      "job_id": "ray_job_abc123",
      "status": "success",
      "map": 0.82
    }
  ]
}
```

---

## Administratif

### `GET /`
Racine API — informations générales.

**Response**:
```json
{
  "service": "bone-annotator",
  "version": "0.1.0",
  "description": "Annotation des images d'os nus (fluoroscopie 360°)",
  "docs": "/docs",
  "status": "/api/status"
}
```

---

## ML — Datasets

### `POST /api/ml/dataset/export`
Exporter les annotations au format YOLO pour l'entraînement.

**Request**:
```json
{
  "acquisitions": ["acq_001", "acq_002"],
  "output_dir": "data/datasets/yolo_20260810",
  "train_ratio": 0.7,
  "val_ratio": 0.2,
  "labels_mapping": {
    "proximal_humerus": 0,
    "distal_humerus": 1
  }
}
```

**Response** (200):
```json
{
  "status": "success",
  "dataset_path": "/path/to/dataset",
  "yaml_path": "/path/to/dataset.yaml",
  "split_stats": {
    "train": 14,
    "val": 6,
    "test": 0
  },
  "total_acquisitions": 20
}
```

### `GET /api/ml/dataset/{dataset_id}/stats`
Récupérer les statistiques d'un dataset existant.

**Response** (200):
```json
{
  "dataset_dir": "/data/datasets/yolo_20260810",
  "splits": {
    "train": {"images": 14, "labels": 14},
    "val": {"images": 6, "labels": 6},
    "test": {"images": 0, "labels": 0}
  },
  "total_images": 20,
  "total_labels": 20
}
```

### `DELETE /api/ml/dataset/{dataset_id}`
Supprimer un dataset.

**Response** (200):
```json
{
  "status": "success",
  "message": "Dataset deleted"
}
```

---

## Codes de Réponse

| Code | Description |
|------|-------------|
| **200** | OK — succès |
| **201** | Created — ressource créée |
| **400** | Bad Request — paramètres invalides |
| **401** | Unauthorized — authentification requise |
| **404** | Not Found — ressource inexistante |
| **503** | Service Unavailable — dépendances manquantes |

---

## Configuration Base de Données

### PostgreSQL Connection
```
Host: 10.0.0.59
Port: 5433
Database: bone_annotations
User: bone
```

### Qdrant Connection
```
Host: 10.0.0.59
Port: 6333
Collections: bone_atlas, bone_annotations
```

---

**Dernière mise à jour**: 2026-08-10
**Phase**: 2 (CVAT Enhancement & ml-compute Training)
**Version**: v0.1.14
