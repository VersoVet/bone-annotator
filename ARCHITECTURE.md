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

### 1. **annotation** — Orchestration annotation ✅
- **Responsabilité**: Interface principale pour l'annotation (CVAT + BoneSeg/YOLO)
- **Modules**:
  - `service.py` — Orchestration workflow (create/sync/validate)
  - `background.py` — Préparation dataset + upload CVAT async (`asyncio.create_task`)
  - `cvat_sync.py` — Sync annotations CVAT → PostgreSQL
  - `ml_bridge.py` — Pré-annotation : BoneSeg → multitask → YOLO (avec check GPU)
  - `sam_proxy.py` — Proxy SAM embeddings pour interactor CVAT
  - `medsam2_bridge.py` — Propagation temporelle MedSAM2
- **Routes**: 
  - `POST /api/annotation/task` — Créer tâche (retour immédiat, status=`preparing`)
  - `GET /api/annotation/tasks/{task_id}` — Polling statut + `progress`
  - `POST /api/annotation/sync/{task_id}` — Sync CVAT → PostgreSQL
  - `POST /api/annotation/validate/{task_id}` — Validation tâche
- **Flux async**: `preparing` → `uploading` → `created` (notes/progress via PostgreSQL)
- **Dépendances**: cvat, preparation, sources, labels, storage, boneseg

### 1b. **boneseg** — Orchestration BoneSeg ✅
- **Responsabilité**: Active learning, test set gelé, coordination GPU
- **Modules**:
  - `gpu.py` — Vérification GPU (boneseg train + ml-compute jobs)
  - `service.py` — Cycle AL : catalog/sync → suggest → create tasks
  - `routes.py` — Endpoints `/api/boneseg/*`
- **Routes**:
  - `GET /api/boneseg/gpu-status` — Disponibilité GPU
  - `POST /api/boneseg/active-learning/run` — Cycle active learning
  - `POST /api/boneseg/test-set` — Ajouter au test set gelé
  - `GET /api/boneseg/test-set` — Lister test set
  - `GET /api/boneseg/catalog/stats` — Stats catalogue (proxy bone-ml)
- **Cron**: `daily-active-learning` (6h)
- **Dépendances**: annotation, storage, bone-ml

### 2. **bonestore** — Accès NFS acquisitions
- **Responsabilité**: Traversée BoneStore, listing, chargement métadonnées
- **Fonctions**:
  - Énumération acquisitions par type os
  - Extraction path .b2nd pour chaque acquisition
  - Cache métadonnées (nombre frames, résolution)
- **Source**: Migrer depuis `bone-recognition/src/annotation/bonestore.py`
- **État**: À migrer

### 3. **imaging** — Pipeline chargement frames ✅
- **Responsabilité**: Décodage .b2nd, cache LRU CPU, PNG conversion, catalogue anatomique
- **Statut**: COMPLÉTÉ (v0.1.20)
- **Implémentation**:
  - `imaging.py` — Blosc2 frame loading, uint16→PNG normalization (148 LOC)
  - `frame_cache.py` — Thread-safe LRU OrderedDict cache (59 LOC)
  - `catalog.py` — Bone taxonomy parser (70 LOC)
  - `service.py` — Async service wrapper (106 LOC)
  - `routes.py` — 7 FastAPI endpoints (150 LOC)
- **Routes**:
  - `GET /api/imaging/status` → service status + cache stats
  - `GET /api/imaging/cache/stats` → cache sizes
  - `POST /api/imaging/cache/clear` → clear caches
  - `POST /api/imaging/frame/png` → load frame → PNG response
  - `GET /api/imaging/frame/info` → frame metadata
  - `GET /api/imaging/catalog` → imaging filters
  - `POST /api/imaging/parse-category` → parse BoneStore dirname
- **Tests**: 21 tests (LRU cache, catalog parsing, PNG conversion, frame index extraction)
- **Dépendances**: blosc2, Pillow, imaging-sdk (optional)

### 4. **storage** — Persistance annotations
- **Responsabilité**: PostgreSQL + Qdrant pour annotations
- **Modules**:
  - `pg_db.py` — Client PostgreSQL (acquisitions, frame_annotations, quality_tier)
  - `task_db.py` — Tâches annotation, migrations (test_sets, bonestore_catalog, boneseg_training_runs)
  - `pg_utils.py` — Helpers (`compute_quality_tier`)
  - `qdrant_store.py` — Stockage embeddings bone_atlas + bone_annotations
- **Fonctions**:
  - CRUD annotations (zones, landmarks, measurements) avec tiers gold/silver/pseudo
  - Test set gelé par acquisition
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
- **Statut**: COMPLÉTÉ (v0.1.20 — export réel implémenté)
- **Implémentation**:
  - `export_to_yolo(acquisitions, train_ratio=0.7)` → fetch annotations PostgreSQL, convert zones → YOLO .txt, copy images
  - `_zone_to_yolo_line()` — zone bbox → normalized YOLO format (class_id x_center y_center w h)
  - `_find_frame_image()` — locate frame in BoneStore
  - `_get_frame_dimensions()` — read .b2nd or standard image dimensions
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

## Preprocessing distribué (OnyxGlia)

Le preprocessing des acquisitions (DICOM .b2nd → PNG 16-bit) est délégué à une
machine dédiée au calcul : **OnyxGlia** (10.0.0.8).

```
bone-annotator (Synapse :9468)
    │
    │  POST /api/preprocess (httpx async)
    ▼
bone-preprocessor (Glia :9480)            ← service dédié
    │
    ├─ imaging-sdk (AutoAdjustOptimizer)  ← paramètres W/L auto par frame
    ├─ ThreadPoolExecutor (12 workers)    ← parallélisme CPU 24 cores
    ├─ NFS read  /mnt/bonestore           ← acquisitions .b2nd (read-only)
    ├─ NFS read  /opt/onyx/imaging-sdk/pipelines  ← pipelines (NFS depuis Synapse)
    └─ NFS write /mnt/cortex-bone-share   ← output PNG (partagé Synapse+Glia)
```

| Machine | Rôle | Specs |
|---------|------|-------|
| **OnyxGlia** (10.0.0.8) | Preprocessing batch | 2× Xeon E5-2630, 24 cores, 62 Go RAM |
| **OnyxSynapse** (10.0.0.59) | API + CVAT + stockage | Service bone-annotator |

**Fallback** : si Glia est injoignable, le preprocessing retombe en mode local
(single-thread sur Synapse). Configurable dans `config/bone-annotator.yaml` section `preprocessing:`.

**Performance** : 929 frames en ~66s (Glia, 12 workers) vs ~8 min (Synapse, single-thread) = **7× plus rapide**.

---

## Segmentation et propagation

Le serveur SAM legacy sur OnyxCortex `:9470` fournit les embeddings `/api/embed`
utilisés par les fonctions Nuclio interactor CVAT, y compris MedSAM ViT-B.
MedSAM2 sur `:9473` expose un contrat différent (`/segment`, `/propagate`) et
est appelé exclusivement par le module `annotation.medsam2_bridge`. Le bridge
reconstruit les masques CVAT en pleine image et propage toutes les frames par
lots chevauchants, sans rééchantillonnage ni perte d'indices.

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

## Résumé Implémentation (v0.1.19 - Complete API with Labels Management)

| Module | Statut | Routes | Endpoints | Complexity |
|--------|--------|--------|-----------|------------|
| labels | ✅ | labels/routes.py | GET/GET/GET/GET/GET/POST/POST/POST | basic |
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
| imaging | ✅ | imaging/routes.py | GET/GET/POST/POST/GET/GET/POST | medium |
| imaging.service | ✅ | - | - | medium |
| annotation.service | ⚠️ | - | - | complex |

### API Endpoints Implemented: 75+
- Health/Status: 4 endpoints
- Ingestion: 4 endpoints
- BoneStore: 3 endpoints
- Annotation: 15 endpoints (CRUD + profiles + batch + MedSAM2 + CVAT sync)
- Prediction: 3 endpoints
- Dataset/Training: 7 endpoints
- Embeddings: 4 endpoints
- Dashboard/Monitoring: 7 endpoints
- Labels/Anatomy: 10 endpoints
- Analysis/Post-Processing: 5 endpoints
- CVAT/Workflow: 8 endpoints
- Imaging: 7 endpoints
- Admin: 5 endpoints (reset, tracking, cancel, retry, settings)

Tests: 85 passing (unit + module)
Validation Forge: VALID (0E/4W)

---

**Dernière mise à jour**: 2026-09-01
**Phase**: Multi-objective annotation pipeline (profiles, Glia preprocessing, MedSAM2)
**Version**: v0.1.83
**Status**: Batch profile creation, dashboard enrichi, auto_bone_mask, preprocessing distribué (Glia)
**Coverage**: All modules have REST API routes (75+ endpoints)
**Test Coverage**: 22+ annotation, 6 preparation, 8 integration
 
