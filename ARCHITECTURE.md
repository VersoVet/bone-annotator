# bone-annotator - Architecture

Annotation des images osseuses fluoroscopie 360° avec pré-annotation YOLO automatique.

---

## Vue Générale

```
┌─────────────────────────────────────────────────────────────┐
│                    bone-annotator (FastAPI)                  │
│                      Port 9468 - Synapse                     │
└─────────────────────────────────────────────────────────────┘
     │
     ├─→ BoneStore (NFS)                    [10.0.0.52:/mnt/bonestore]
     │   └─ 312 acquisitions (.b2nd format)
     │
     ├─→ PostgreSQL                         [10.0.0.59:5433]
     │   └─ Schema: bone_annotations
     │       ├─ acquisitions
     │       ├─ annotations (zones, landmarks)
     │       ├─ measurements (longueurs, angles)
     │       └─ lesions (pathologies détectées)
     │
     ├─→ Qdrant                             [10.0.0.59:6333]
     │   ├─ bone_atlas (512D embeddings)
     │   └─ bone_annotations (768D labels)
     │
     ├─→ CVAT                               [Synapse - à installer]
     │   └─ Annotation collaborative séries images
     │
     ├─→ label-generator                    [10.0.0.59:9466]
     │   └─ Labels anatomiques (zones, landmarks, critères)
     │
     └─→ ml-compute (Ray)                   [10.0.0.44:9469]
         └─ Training YOLO, batch inference GPU
```

---

## Modules Fonctionnels

### 1. **annotation** — Orchestration annotation
- **Responsabilité**: Interface principale pour l'annotation (CVAT + YOLO)
- **Routes**: 
  - `POST /api/annotation/task` — Créer une tâche CVAT
  - `GET /api/annotation/task/{task_id}` — Statut d'une tâche
  - `POST /api/annotation/export` — Exporter annotations YOLO
- **Dépendances**: cvat, bonestore, predict
- **État**: À migrer depuis bone-recognition

### 2. **bonestore** — Accès NFS acquisitions
- **Responsabilité**: Traversée BoneStore, listing, chargement métadonnées
- **Fonctions**:
  - Énumération acquisitions par type os
  - Extraction path .b2nd pour chaque acquisition
  - Cache métadonnées (nombre frames, résolution)
- **Source**: Migrer depuis `bone-recognition/src/annotation/bonestore.py`
- **État**: À migrer

### 3. **imaging** — Pipeline chargement frames
- **Responsabilité**: Décodage .b2nd, cache LRU GPU, pipeline imaging-sdk
- **Fonctions**:
  - `load_frame(acquisition_id, frame_idx)` → numpy array
  - Cache LRU en mémoire GPU (10-20 acquisitions)
  - Normalisation / prétraitement
- **Source**: Migrer depuis `bone-recognition/src/annotation/imaging.py`
- **Dépendances**: imaging-sdk, bonestore
- **État**: À migrer

### 4. **storage** — Persistance annotations
- **Responsabilité**: PostgreSQL + Qdrant pour annotations
- **Modules**:
  - `pg_db.py` — Client PostgreSQL (acquisitions, annotations, measurements, lesions)
  - `qdrant_store.py` — Stockage embeddings bone_atlas + bone_annotations
- **Fonctions**:
  - CRUD annotations (zones, landmarks, measurements)
  - Recherche sémantique Qdrant
- **Source**: Migrer depuis `bone-recognition/src/annotation/pg_db.py`
- **État**: À migrer

### 5. **ingestion** — Sync BoneStore → Registry
- **Responsabilité**: Scan périodique BoneStore, registre ingestion
- **Modules**:
  - `service.py` — Orchestration ingestion
  - `registry.py` — Suivi SQLite acquisitions traitées
- **Fonctions**:
  - `sync_acquisitions()` — Découvrir nouvelles acquisitions
  - `mark_ingested(acquisition_id)` — Marquer comme ingérée
  - `get_pending()` → list[acquisition]
- **Source**: Migrer depuis `bone-recognition/src/data/bonestore_ingest.py`
- **Cron**: `POST /api/ingestion/sync` toutes les heures
- **État**: À migrer

### 6. **predict** — Inférence YOLO
- **Responsabilité**: Pré-annotation automatique landmarks + zones
- **Fonctions**:
  - `predict(frames: list[np.ndarray])` → dict annotations
  - Format sortie compatible CVAT
- **Source**: Migrer depuis `bone-ml/src/modules/predict/service.py`
- **Dépendances**: imaging
- **État**: À migrer

### 7. **training** — Orchestration training GPU ✅
- **Responsabilité**: Soumettre jobs ML à ml-compute (Ray)
- **Statut**: COMPLÉTÉ (v0.1.14)
- **Implémentation**:
  - `start_training(config)` → Ray Jobs submission
  - `get_training_status(job_id)` → query ml-compute
  - `cancel_training(job_id)` → cancel job
  - `poll_job_status()` → wait for completion
- **Dépendances**: ml-compute Ray API (10.0.0.44:9469)
- **Routes**: 
  - `GET /api/ml/training/status` → job status
  - `GET /api/ml/training/jobs` → list active jobs
  - `POST /api/ml/training/{job_id}/cancel` → cancel

### 8. **dataset** — Export annotations format YOLO ✅
- **Responsabilité**: Conversion annotations BD → YOLO dataset format
- **Statut**: COMPLÉTÉ (v0.1.14)
- **Implémentation**:
  - `export_to_yolo(acquisitions, train_ratio=0.7)` → YOLO dataset
  - `get_dataset_stats(dataset_dir)` → split info
  - `delete_dataset(dataset_dir)` → cleanup
- **Routes**:
  - `POST /api/ml/dataset/export` → create dataset
  - `GET /api/ml/dataset/{id}/stats` → get stats
  - `DELETE /api/ml/dataset/{id}` → delete
- **Output**: dataset.yaml + train/val/test/{images,labels}/

### 9. **cvat** — Client CVAT REST API
- **Responsabilité**: Intégration CVAT (nouveau module)
- **Modules**:
  - `client.py` — API REST CVAT (auth, CRUD tasks)
  - `sync.py` — Synchronisation annotations CVAT ↔ PostgreSQL
  - `format.py` — Conversion annotations CVAT → internal format
- **Fonctions**:
  - `create_task(frames, labels, metadata)` → task_id
  - `push_predictions(task_id, predictions)` — Pré-annotation
  - `sync_from_cvat()` — Importer annotations complétées
- **État**: À créer

### 10. **dashboard** — Monitoring pipeline
- **Responsabilité**: SSE events, statut training, logs
- **Routes**:
  - `GET /api/dashboard/events` — SSE stream
  - `GET /api/dashboard/training-status` — Monitoring training
  - `GET /api/dashboard/logs` — Logs récents
- **State**: À créer

### 11. **analysis** (optionnel) — Post-inférence
- **Responsabilité**: Analyse morphométrique (density, contours, conformation)
- **Source**: Migrer depuis `bone-recognition/src/analysis/`
- **État**: À migrer (phase 2)

---

## Flux de Données Principal

### 1. Ingestion
```
BoneStore (NFS)
    ↓ (acquisition discovery)
ingestion:sync()
    ↓
PostgreSQL (acquisitions table)
    ↓
cache: ingestion_registry.db
```

### 2. Pré-annotation
```
PostgreSQL (acquisitions)
    ↓ (pending acquisitions)
imaging:load_frame()
    ↓ (cache LRU GPU)
predict:predict()
    ↓ (YOLO model)
CVAT API (push predictions)
```

### 3. Annotation Manuelle
```
CVAT (annotation collaborative)
    ↓ (user edits)
cvat:sync_from_cvat()
    ↓
PostgreSQL (annotations stored)
    ↓
Qdrant (embeddings vectorized)
```

### 4. Training Actif
```
PostgreSQL (annotations)
    ↓
dataset:export_to_yolo()
    ↓ (YOLO dataset format)
training:submit_training()
    ↓ (Ray Job to ml-compute)
ml-compute:9469 (GPU training)
    ↓ (callback on complete)
training:callback()
    ↓ (store model path)
PostgreSQL (models table)
```

### 5. Itération
```
meilleur_modèle
    ↓
predict:predict() [avec nouveau modèle]
    ↓
CVAT:push_predictions()
    ↓ (boucle d'apprentissage actif)
```

---

## Dépendances Externes

| Dépendance | Type | Usage | Criticité |
|-----------|------|-------|-----------|
| BoneStore NFS | I/O | Images .b2nd | critical |
| PostgreSQL | DB | Annotations métier | critical |
| Qdrant | VectorDB | Embeddings labels | high |
| CVAT | External | Annotation séries | high |
| ml-compute Ray | Compute | Training GPU | high |
| label-generator | API | Labels anatomiques | medium |
| Orthanc PACS | External | Source images DICOM | low |

---

## Données Persistantes

### PostgreSQL (10.0.0.59:5433)
Schema: `bone_annotations`
- **acquisitions** — Métadonnées acquisitions BoneStore
- **annotations** — Zones, landmarks manuels/auto
- **measurements** — Longueurs, angles, ratios
- **lesions** — Pathologies détectées
- **models** — Versions YOLO entraînées
- **training_jobs** — Historique training Ray

### Qdrant (10.0.0.59:6333)
- **bone_atlas** (512D) — Embeddings reference anatomy
- **bone_annotations** (768D) — Embeddings labels et critères

### SQLite Local
- **data/ingestion_registry.db** — Suivi acquisitions ingérées

---

## Configuration Forge

| Champ | Valeur |
|-------|--------|
| **Type** | python |
| **Port** | 9468 |
| **Brain Area** | cortex-visuel |
| **Target** | OnyxSynapse (10.0.0.59) |
| **Run Mode** | service |
| **Memory Limit** | 4GB (GPU workload) |

---

## Prochaines Étapes

1. **Phase 1**: Migrer modules bonestore, imaging, storage
2. **Phase 2**: Migrer modules annotation, predict, dataset
3. **Phase 3**: Créer module CVAT (client, sync, format)
4. **Phase 4**: Adapter training pour ml-compute Ray
5. **Phase 5**: Dashboard monitoring + SSE events
6. **Phase 6**: Tests intégration bout-en-bout
7. **Phase 7**: Validation Forge complète
8. **Phase 8**: Déploiement OnyxSynapse

---

## Résumé Implémentation (v0.1.18 - Complete API Routes with Analysis & CVAT)

| Module | Statut | Routes | Endpoints | Complexity |
|--------|--------|--------|-----------|------------|
| labels | ✅ | - | - | basic |
| cvat.client | ✅ | - | - | basic |
| training | ✅ | ml/routes.py | GET/POST | medium |
| dataset | ✅ | ml/routes.py | POST/GET/DEL | medium |
| storage | ✅ | - | - | medium |
| storage.service | ✅ | - | - | medium |
| annotation.routes | ✅ | annotation/routes.py | POST/GET/POST | medium |
| predict | ✅ | ml/predict/routes.py | GET/POST/POST | medium |
| predict.service | ✅ | - | - | complex |
| ingestion | ✅ | ingestion/routes.py | POST/GET/GET/POST | medium |
| ingestion.service | ✅ | - | - | medium |
| bonestore | ✅ | bonestore/routes.py | GET/GET/GET | basic |
| bonestore.service | ✅ | - | - | basic |
| embeddings | ✅ | embeddings/routes.py | POST/GET/GET/POST | medium |
| embeddings.service | ✅ | - | - | medium |
| dashboard | ✅ | dashboard/routes.py | GET/GET/GET/GET/GET/GET/POST | medium |
| dashboard.service | ✅ | - | - | medium |
| analysis | ✅ | analysis/routes.py | GET/POST/POST/POST/POST | medium |
| analysis.service | ✅ | - | - | medium |
| cvat | ✅ | cvat/routes.py | POST/GET/GET/GET/POST/GET/POST/GET | medium |
| cvat.service | ✅ | - | - | medium |
| imaging.service | ⚠️ | - | - | complex |
| annotation.service | ⚠️ | - | - | complex |

### API Endpoints Implemented: 40+
- Health/Status: 4 endpoints
- Ingestion: 4 endpoints
- BoneStore: 3 endpoints
- Annotation: 5 endpoints
- Prediction: 3 endpoints
- Dataset/Training: 7 endpoints
- Embeddings: 4 endpoints
- Dashboard/Monitoring: 7 endpoints
- Analysis/Post-Processing: 5 endpoints
- CVAT/Workflow: 8 endpoints

Tests: 42/61 passing (69%)
Validation Forge: VALID (0E/3W)
Commits: 6 feature commits

---

**Dernière mise à jour**: 2026-08-10
**Phase**: 2 (CVAT Enhancement & ml-compute Training)
**Version**: v0.1.18
**Status**: All API Routes Complete (40+ endpoints: Dashboard, Analysis, CVAT integrated)
**Coverage**: All core modules + dashboard + analysis + CVAT have REST API routes
**Test Coverage**: 42/61 passing (69%)
