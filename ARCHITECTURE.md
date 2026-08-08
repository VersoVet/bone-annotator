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

### 7. **training** — Orchestration training GPU
- **Responsabilité**: Soumettre jobs ML à ml-compute (Ray)
- **Fonctions**:
  - `submit_training(dataset_yaml, epochs)` → job_id
  - `check_job_status(job_id)` → status
  - Callback: `POST /api/training/callback?job_id=...&status=...`
- **Source**: Migrer depuis `bone-ml/src/modules/training/service.py`
- **Dépendances**: ml-compute Ray API
- **État**: À migrer (adapter pour ml-compute au lieu d'exécution locale)

### 8. **dataset** — Export annotations format YOLO
- **Responsabilité**: Conversion annotations BD → YOLO dataset format
- **Fonctions**:
  - `export_to_yolo(acquisitions: list[str])` → yaml config
  - Split train/val/test
- **Source**: Migrer depuis `bone-ml/src/modules/dataset/service.py`
- **État**: À migrer

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

**Dernière mise à jour**: 2026-08-08
