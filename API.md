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
  "status": "success",
  "synced": 5,
  "new": 2,
  "pending": 12,
  "timestamp": "2026-08-10T10:30:00Z"
}
```

### `GET /api/ingestion/pending`
Récupérer les acquisitions en attente d'annotation.

**Response** (200):
```json
{
  "acquisitions": [
    {"id": "acq_001", "bone_type": "humerus", "frame_count": 120}
  ],
  "total": 45,
  "limit": 100,
  "offset": 0
}
```

### `GET /api/ingestion/status`
Statut global de l'ingestion.

**Response** (200):
```json
{
  "status": "ready",
  "total_acquisitions": 312,
  "pending": 45,
  "last_sync": "2026-08-10T00:00:00Z"
}
```

---

## BoneStore

### `GET /api/bonestore/acquisitions`
Lister les acquisitions disponibles.

**Query params**: `bone_type`, `side`, `limit`

**Response** (200):
```json
{
  "acquisitions": [
    {
      "id": "acq_001",
      "bone_type": "humerus",
      "side": "left",
      "region": "proximal",
      "frame_count": 120,
      "has_timecodes": true,
      "path": "/mnt/bonestore/humerus_left_proximal/acq_001"
    }
  ],
  "total": 312,
  "filtered": 45,
  "limit": 100
}
```

### `GET /api/bonestore/acquisitions/{acquisition_id}`
Détails d'une acquisition avec liste de frames.

**Response** (200):
```json
{
  "acquisition_id": "acq_001",
  "path": "/mnt/bonestore/...",
  "frame_count": 120,
  "frames": [
    {"index": 0, "filename": "frame_0000.b2nd", "angle_deg": 0.0, "position": 0}
  ],
  "timecodes_available": true
}
```

### `GET /api/bonestore/stats`
Statistiques globales du BoneStore.

**Response** (200):
```json
{
  "total_acquisitions": 312,
  "total_frames": 42560,
  "acquisitions_by_bone_type": {"humerus": 80, "radius": 75, "ulna": 62},
  "acquisitions_with_timecodes": 310,
  "acquisitions_without_timecodes": 2
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

### `GET /api/predict/model-info`
Informations sur le modèle YOLO chargé.

**Response** (200):
```json
{
  "model_version": "/opt/onyx/skills/bone-ml/models/yolov8_20260808.pt",
  "model_loaded": true,
  "model_type": "yolov8"
}
```

### `POST /api/predict/task`
Prédictions YOLO sur une tâche simple.

**Request**:
```json
{
  "id": "task_001",
  "data": {
    "image": "/mnt/bonestore/humerus_left_proximal/acq_001/raw/frame_0000.b2nd"
  }
}
```

**Response** (200):
```json
{
  "result": [
    {
      "type": "rectanglelabels",
      "value": {
        "x": 20.5,
        "y": 15.3,
        "width": 60.2,
        "height": 70.1,
        "rectanglelabels": ["metaphysis"]
      },
      "score": 0.94,
      "from_name": "label",
      "to_name": "image"
    }
  ],
  "score": 0.91
}
```

### `POST /api/predict/batch`
Prédictions batch sur plusieurs tâches.

**Request**:
```json
{
  "tasks": [
    {"id": "task_001", "data": {"image": "..."}},
    {"id": "task_002", "data": {"image": "..."}}
  ],
  "model_version": null
}
```

**Response** (200):
```json
{
  "status": "completed",
  "total_tasks": 2,
  "predictions": {
    "task_001": {"result": [...], "score": 0.91},
    "task_002": {"result": [...], "score": 0.88}
  }
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

## Dashboard (Monitoring & SSE)

### `GET /api/dashboard/events`
Real-time SSE stream for pipeline events.

**Headers**:
```
Content-Type: text/event-stream
Cache-Control: no-cache
Connection: keep-alive
```

**Event Types**:
```
event: ingestion_started
data: {"stage": "ingestion", "message": "Started BoneStore sync"}

event: ingestion_complete
data: {"stage": "ingestion", "acquisitions": 45, "frames": 5400}

event: prediction_progress
data: {"stage": "prediction", "step": 10, "total": 45}

event: training_update
data: {"job_id": "ray_job_xyz", "epoch": 25, "loss": 0.23}

event: stage_completed
data: {"stage": "prediction", "status": "completed", "metrics": {...}}
```

### `GET /api/dashboard/state`
Current pipeline state snapshot.

**Response** (200):
```json
{
  "status": "success",
  "timestamp": "2026-08-10T12:30:00Z",
  "pipeline_state": {
    "ingestion": {"status": "idle", "pending": 12},
    "prediction": {"status": "running", "progress": 45},
    "annotation": {"status": "waiting", "tasks": 8},
    "training": {"status": "idle", "active_jobs": 0}
  }
}
```

### `GET /api/dashboard/history`
Recent event history (up to 1000 events).

**Query params**: `limit` (default 200, max 1000)

**Response** (200):
```json
{
  "status": "success",
  "total": 150,
  "limit": 200,
  "events": [
    {
      "type": "ingestion_started",
      "timestamp": "2026-08-10T12:25:00Z",
      "data": {...}
    }
  ]
}
```

### `GET /api/dashboard/metrics`
Performance metrics for pipeline stages.

**Query params**: `stage` (optional, e.g., "prediction", "training", or omit for all)

**Response** (200):
```json
{
  "status": "success",
  "stage": "prediction",
  "metrics": {
    "total_time": 245.5,
    "throughput": 12.3,
    "avg_confidence": 0.87,
    "errors": 0
  }
}
```

### `GET /api/dashboard/status`
Dashboard service health and statistics.

**Response** (200):
```json
{
  "status": "ready",
  "service": "dashboard",
  "components": {
    "status": "ready",
    "pipeline_state": {"ingestion": {...}},
    "subscribers": 3,
    "history_size": 245
  }
}
```

### `GET /api/dashboard/logs`
Recent application logs (alias for history with limit=100).

**Query params**: `limit` (default 100, max 500)

**Response** (200):
```json
{
  "status": "success",
  "total": 87,
  "logs": [...]
}
```

### `POST /api/dashboard/event`
Publish a custom event (for testing/monitoring).

**Request**:
```json
{
  "event_type": "custom_test",
  "data": {"message": "Manual test event"}
}
```

**Response** (200):
```json
{
  "status": "published",
  "event_type": "custom_test",
  "data": {...}
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

## Embeddings & Semantic Search

### `POST /api/embeddings/search/bone-atlas`
Search bone atlas with semantic embedding vector.

**Request**:
```json
{
  "embedding": [0.5, -0.2, 0.1, ...],  // 512D vector
  "limit": 10,
  "min_confidence": 0.3
}
```

**Response** (200):
```json
{
  "status": "success",
  "query_vector_size": 512,
  "results": [
    {
      "id": "bone_001",
      "distance": 0.15,
      "bone_type": "humerus",
      "side": "left",
      "region": "proximal"
    }
  ],
  "total": 3
}
```

### `GET /api/embeddings/similar/{bone_id}`
Find bones similar to a reference bone.

**Response** (200):
```json
{
  "status": "success",
  "reference_bone_id": "bone_001",
  "similar_bones": [
    {"id": "bone_042", "distance": 0.12},
    {"id": "bone_089", "distance": 0.18}
  ],
  "total": 2
}
```

### `GET /api/embeddings/stats`
Get vector collection statistics.

**Response** (200):
```json
{
  "status": "ready",
  "collections": {
    "bone_atlas": {
      "vector_size": 512,
      "distance_metric": "cosine",
      "description": "Reference bone anatomy embeddings"
    },
    "bone_annotations": {
      "vector_size": 768,
      "distance_metric": "cosine",
      "description": "Annotation labels embeddings"
    }
  }
}
```

---

## Labels (Anatomical Reference)

### `GET /api/labels/status`
Get label service status and available bone types.

**Response** (200):
```json
{
  "status": "ready",
  "service": "labels",
  "components": {
    "service": "labels",
    "cache_loaded": true,
    "bone_types_available": ["humerus", "radius", "ulna", "femur"],
    "total_zones": 24,
    "total_landmarks": 18
  }
}
```

### `GET /api/labels/anatomy`
Get all anatomical labels for all bone types.

**Response** (200):
```json
{
  "status": "success",
  "bone_types": ["humerus", "radius", "ulna"],
  "labels": {
    "humerus": {
      "zones": [...],
      "landmarks": [...],
      "lesion_criteria": {...}
    }
  }
}
```

### `GET /api/labels/bones/{bone_type}`
Get complete label hierarchy for a specific bone type.

**Response** (200):
```json
{
  "status": "success",
  "bone_type": "humerus",
  "labels": {
    "bone_type": "humerus",
    "zones": [
      {"id": "proximal_humerus", "name": "Proximal Humerus", "region": "proximal"}
    ],
    "landmarks": [
      {"id": "greater_tubercle", "name": "Greater Tubercle"}
    ],
    "lesion_criteria": {...},
    "regions": ["proximal", "distal", "entire"]
  }
}
```

### `GET /api/labels/bones/{bone_type}/zones`
Get anatomical zones for a bone type with optional region filtering.

**Query params**: `region` (proximal, distal, entire)

**Response** (200):
```json
{
  "status": "success",
  "bone_type": "humerus",
  "region": "proximal",
  "zones": [
    {"id": "proximal_humerus", "name": "Proximal Humerus"},
    {"id": "metaphysis", "name": "Metaphysis"}
  ],
  "count": 2
}
```

### `GET /api/labels/bones/{bone_type}/landmarks`
Get anatomical landmarks for a bone type.

**Response** (200):
```json
{
  "status": "success",
  "bone_type": "humerus",
  "landmarks": [
    {"id": "greater_tubercle", "name": "Greater Tubercle", "region": "proximal"},
    {"id": "medial_epicondyle", "name": "Medial Epicondyle", "region": "distal"}
  ],
  "count": 2
}
```

### `GET /api/labels/bones/{bone_type}/lesion-criteria`
Get lesion criteria and pathology classification for a bone type.

**Response** (200):
```json
{
  "status": "success",
  "bone_type": "humerus",
  "criteria": {
    "fracture": {"severity": "high", "types": ["proximal", "diaphyseal", "distal"]},
    "osteoporosis": {"severity": "medium", "indicators": ["density_loss", "trabecular_thinning"]}
  }
}
```

### `POST /api/labels/validate/zone`
Validate that a zone annotation is applicable for a bone type and region.

**Query params**: `bone_type`, `zone_id`, `region` (optional)

**Response** (200):
```json
{
  "status": "success",
  "valid": true,
  "bone_type": "humerus",
  "zone_id": "proximal_humerus",
  "region": "any"
}
```

### `POST /api/labels/validate/landmark`
Validate that a landmark annotation is applicable for a bone type.

**Query params**: `bone_type`, `landmark_id`

**Response** (200):
```json
{
  "status": "success",
  "valid": true,
  "bone_type": "humerus",
  "landmark_id": "greater_tubercle"
}
```

### `POST /api/labels/sync`
Synchronize labels from label-generator service.

**Response** (200):
```json
{
  "status": "synced",
  "bone_types_updated": 4
}
```

---

## Analysis (Post-Annotation)

### `GET /api/analysis/status`
Get analysis service status and available models.

**Response** (200):
```json
{
  "status": "ready",
  "service": "analysis",
  "components": {
    "status": "ready",
    "conformation_models": ["humerus", "radius", "ulna"]
  }
}
```

### `POST /api/analysis/density`
Analyze bone density from segmentation mask.

**Request**:
```json
{
  "density_mask": [[0, 1, 1], [1, 2, 1]],
  "image_data": [[0.5, 0.6], [0.7, 0.8]]
}
```

**Response** (200):
```json
{
  "status": "success",
  "analysis": {
    "mean_density": 0.65,
    "std_density": 0.12,
    "cortical_thickness": 2.3
  }
}
```

### `POST /api/analysis/conformation`
Analyze bone conformation from landmarks.

**Request**:
```json
{
  "bone_type": "humerus",
  "landmarks": [
    {"id": "proximal", "x": 50, "y": 100},
    {"id": "distal", "x": 200, "y": 400}
  ],
  "image_size": 512
}
```

**Response** (200):
```json
{
  "status": "success",
  "bone_type": "humerus",
  "analysis": {
    "morphology_score": 0.87,
    "alignment": "normal"
  }
}
```

### `POST /api/analysis/anomalies`
Detect density anomalies.

**Request**:
```json
{
  "density_stats": {
    "mean": 0.65,
    "std": 0.12,
    "min": 0.2,
    "max": 0.95
  },
  "reference_stats": null
}
```

**Response** (200):
```json
{
  "status": "success",
  "anomalies": [
    {"type": "low_density", "severity": "medium", "region": "distal"}
  ],
  "count": 1
}
```

### `POST /api/analysis/axis`
Compute principal bone axis from landmarks.

**Request**:
```json
{
  "landmarks": [
    {"id": "proximal", "x": 50, "y": 100},
    {"id": "midpoint", "x": 125, "y": 250},
    {"id": "distal", "x": 200, "y": 400}
  ],
  "bone_type": "humerus"
}
```

**Response** (200):
```json
{
  "status": "success",
  "bone_type": "humerus",
  "axis": {
    "angle_deg": 12.5,
    "direction": [0.21, 0.98],
    "length": 424.3
  }
}
```

---

## CVAT (Annotation Workflow)

### `POST /api/cvat/connect`
Connect and authenticate with CVAT server.

**Response** (200):
```json
{
  "status": "connected",
  "authenticated": true
}
```

### `GET /api/cvat/tasks`
List all CVAT tasks.

**Query params**: `limit` (default 100, max 500)

**Response** (200):
```json
{
  "status": "success",
  "total": 45,
  "limit": 100,
  "tasks": [
    {
      "id": 42,
      "name": "bone_annotation_batch_1",
      "status": "in_progress",
      "frames": 120
    }
  ]
}
```

### `GET /api/cvat/tasks/{task_id}`
Get details of a specific CVAT task.

**Response** (200):
```json
{
  "status": "success",
  "task": {
    "id": 42,
    "name": "bone_annotation_batch_1",
    "status": "in_progress",
    "frames": 120,
    "assignee": "radiologist@hospital.fr"
  }
}
```

### `POST /api/cvat/tasks`
Create a new CVAT task.

**Request**:
```json
{
  "name": "bone_annotation_humerus",
  "project_id": null
}
```

**Response** (201):
```json
{
  "status": "created",
  "task": {
    "id": 43,
    "name": "bone_annotation_humerus"
  }
}
```

### `GET /api/cvat/tasks/{task_id}/annotations`
Pull annotations from a CVAT task.

**Response** (200):
```json
{
  "status": "success",
  "task_id": 42,
  "annotations": {
    "zones": [
      {"id": "zone_1", "type": "metaphysis", "bbox": [20, 50, 200, 300]}
    ],
    "landmarks": [...]
  }
}
```

### `POST /api/cvat/tasks/{task_id}/annotations`
Push annotations to a CVAT task.

**Request**:
```json
{
  "task_id": 42,
  "annotations": {
    "zones": [...],
    "landmarks": [...]
  }
}
```

**Response** (200):
```json
{
  "status": "pushed",
  "task_id": 42
}
```

### `POST /api/cvat/tasks/{task_id}/sync`
Synchronize annotations bidirectionally.

**Request**:
```json
{
  "task_id": 42,
  "local_annotations": {...},
  "strategy": "local_wins"
}
```

**Response** (200):
```json
{
  "status": "synced",
  "task_id": 42,
  "strategy": "local_wins",
  "annotations": {...}
}
```

### `GET /api/cvat/status`
Get CVAT service status.

**Response** (200):
```json
{
  "status": "ready",
  "service": "cvat",
  "components": {
    "status": "connected",
    "authenticated": true
  }
}
```

---

## Imaging (Frame Loading & Cache)

### `GET /api/imaging/status`
Get imaging service status with cache statistics.

**Response** (200):
```json
{
  "status": "ready",
  "service": "imaging",
  "cache_stats": {
    "raw_cache_size": 12,
    "processed_cache_size": 5
  }
}
```

### `GET /api/imaging/cache/stats`
Get frame cache statistics.

**Response** (200):
```json
{
  "status": "ok",
  "cache": {
    "raw_cache_size": 12,
    "processed_cache_size": 5
  }
}
```

### `POST /api/imaging/cache/clear`
Clear all frame caches (raw + processed).

**Response** (200):
```json
{
  "status": "ok",
  "message": "Caches cleared"
}
```

### `POST /api/imaging/frame/png`
Load a .b2nd frame and return as PNG image.

**Request**:
```json
{
  "path": "/mnt/bonestore/humerus_left/acq_001/raw/frame_0042.b2nd",
  "size": 768
}
```

**Response** (200): PNG image bytes (`Content-Type: image/png`)

### `GET /api/imaging/frame/info`
Get frame metadata (shape, dtype, size) without full loading.

**Query params**: `path` (required)

**Response** (200):
```json
{
  "status": "ok",
  "path": "/mnt/bonestore/.../frame_0042.b2nd",
  "shape": [1380, 1380],
  "dtype": "uint16",
  "size_bytes": 3808800
}
```

### `GET /api/imaging/catalog`
Get available imaging filters catalog.

**Response** (200):
```json
{
  "status": "ok",
  "filters": {
    "clahe": {
      "category": "enhancement",
      "description": "Contrast Limited Adaptive Histogram Equalization",
      "gpu": true,
      "params": [...]
    }
  },
  "count": 12
}
```

### `POST /api/imaging/parse-category`
Parse bone category from BoneStore directory name.

**Request**:
```json
{
  "dirname": "001^humerus_left_proximal"
}
```

**Response** (200):
```json
{
  "status": "ok",
  "bone_type": "humerus",
  "side": "left",
  "region": "proximal"
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

**Dernière mise à jour**: 2026-08-16
**Phase**: 2 (Priority 1 modules implementation)
**Version**: v0.1.20
**Endpoints**: 57+ (Health/Status 4, Ingestion 4, BoneStore 3, Annotation 5, Prediction 3, Dataset/Training 7, Embeddings 4, Dashboard 7, Labels 10, Analysis 5, CVAT 8, Imaging 7)
