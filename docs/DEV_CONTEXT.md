# Contexte de développement — bone-annotator

## Objectif

Annotation des images d'os nus issus de séries de fluoroscopie (rotation 360° sur le grand axe). Ce skill gère :
1. L'accès aux images via BoneStore (NFS `/mnt/bonestore`, format `.b2nd`)
2. L'annotation manuelle via CVAT (séries d'images type vidéo)
3. La pré-annotation automatique via YOLO (détection landmarks + zones)
4. La boucle d'apprentissage actif : annotation → training → meilleur modèle → pré-annotation

## Dépendances inter-skills

- **label-generator** (port 9466, Synapse) : fournit les labels de référence (zones, landmarks, critères) via `GET /labels/api/export/cvat?bone_type=humerus`
- **ml-compute** (port 9469, Soma) : exécute les jobs GPU (training YOLO, batch inference) via Ray Jobs API

## Code à migrer

### Depuis bone-recognition (`/home/onyx/projects/skills/bone-recognition/`)

| Source | Destination | Description |
|--------|-------------|-------------|
| `src/annotation/service.py` | `src/modules/annotation/service.py` | Service d'annotation principal (434 lignes) |
| `src/annotation/bonestore.py` | `src/modules/bonestore/service.py` | Traversée NFS BoneStore, listing acquisitions (172 lignes) |
| `src/annotation/imaging.py` | `src/modules/imaging/service.py` | Chargement frames .b2nd, cache LRU GPU, pipeline imaging-sdk (205 lignes) |
| `src/annotation/catalog.py` | `src/modules/imaging/catalog.py` | Taxonomie anatomique, parsing catégories (60 lignes) |
| `src/annotation/annotations.py` | `src/modules/annotation/storage.py` | Sérialisation JSON annotations (88 lignes) |
| `src/annotation/pg_db.py` | `src/modules/storage/pg_db.py` | Client PostgreSQL annotations (418 lignes) |
| `src/annotation/routes.py` | `src/modules/annotation/routes.py` | Routes FastAPI annotateur (167 lignes) |
| `src/data/bonestore_ingest.py` | `src/modules/ingestion/service.py` | Ingestion streaming depuis BoneStore (439 lignes) |
| `src/data/ingestion_registry.py` | `src/modules/ingestion/registry.py` | Suivi d'ingestion SQLite (385 lignes) |
| `src/analysis/*` | `src/modules/analysis/` | Analyse post-inférence (density, landmarks, conformation) (~890 lignes) |
| `src/data/orthanc_client.py` | `src/modules/data/orthanc_client.py` | Client REST Orthanc PACS (293 lignes) |
| `src/data/pseudo_labels.py` | `src/modules/pseudo_labels/service.py` | Génération labels automatiques (479 lignes) |
| `src/embeddings/qdrant_store.py` | `src/modules/embeddings/service.py` | Stockage embeddings bone_atlas Qdrant (100 lignes) |
| `src/dashboard/` | `src/modules/dashboard/` | SSE events + pipeline monitoring (~200 lignes) |

### Depuis bone-ml (`/home/onyx/projects/skills/bone-ml/`)

| Source | Destination | Description |
|--------|-------------|-------------|
| `src/modules/predict/service.py` | `src/modules/predict/service.py` | Inférence YOLO, ML backend Label Studio (249 lignes) |
| `src/modules/predict/routes.py` | `src/modules/predict/routes.py` | Routes predict (70 lignes) |
| `src/modules/training/service.py` | `src/modules/training/service.py` | Orchestration training YOLOv8 (118 lignes) |
| `src/modules/training/routes.py` | `src/modules/training/routes.py` | Routes training (57 lignes) |
| `src/modules/dataset/service.py` | `src/modules/dataset/service.py` | Export annotations → YOLO format (218 lignes) |
| `src/modules/dataset/routes.py` | `src/modules/dataset/routes.py` | Routes dataset (48 lignes) |
| `src/modules/evaluation/service.py` | `src/modules/evaluation/service.py` | Métriques mAP, comparaison modèles (72 lignes) |
| `src/modules/evaluation/routes.py` | `src/modules/evaluation/routes.py` | Routes evaluation (39 lignes) |

## Stratégie CVAT

- **Pourquoi CVAT** : les acquisitions sont des séries d'images (rotation 360°) — CVAT gère les séquences comme des vidéos, parfait pour YOLO frame-by-frame
- **1 task CVAT = 1 acquisition** (toutes les frames en une séquence)
- **Pré-annotation** : YOLO détecte landmarks + zones → push dans CVAT via API REST
- **Boucle d'apprentissage** : annotation manuelle → export YOLO → training via ml-compute → meilleur modèle → pré-annotation des séries suivantes
- **Migration** : garder temporairement l'intégration Label Studio (deprecated) pendant la mise en place de CVAT
- Nouveau module `src/modules/cvat/` (client.py, sync.py, format.py)

## Services externes

| Service | URL | Usage |
|---------|-----|-------|
| BoneStore NFS | `/mnt/bonestore` (10.0.0.52) | Images .b2nd, 312 acquisitions |
| PostgreSQL | 10.0.0.59:5433 | Schema `bone_annotations`, user `bone` |
| Qdrant | 10.0.0.59:6333 | Collection `bone_atlas` (512D embeddings) |
| CVAT | à installer sur Synapse | Annotation d'images séries |
| label-generator | 10.0.0.59:9466 | Labels anatomiques |
| ml-compute | 10.0.0.44:9469 | Jobs GPU (Ray) |
| Orthanc Research | 10.0.0.6:8044 | PACS source d'images DICOM |

## Soumission de jobs ML

Le training et l'inférence GPU se font via ml-compute (Ray) :
```python
import httpx

async def submit_training_job(dataset_yaml: str, epochs: int = 100) -> str:
    async with httpx.AsyncClient() as client:
        resp = await client.post("http://10.0.0.44:9469/api/jobs", json={
            "entrypoint": f"python train_yolo.py --dataset {dataset_yaml} --epochs {epochs}",
            "runtime_env": {"working_dir": "/opt/onyx/ml-jobs/bone-annotator/"},
            "metadata": {
                "skill": "bone-annotator",
                "callback": "http://10.0.0.59:9468/api/training/callback"
            }
        })
        return resp.json()["job_id"]
```

## Données existantes

- 312 acquisitions dans BoneStore (os nus, fluoroscopie 360°)
- 397 articles scientifiques (via label-generator)
- 259 zones accepted, 118 landmarks accepted (via label-generator)
- PostgreSQL: tables acquisitions, annotations (zones, landmarks, measurements, lesions)
- Qdrant: collection bone_atlas (512D), collection bone_annotations (768D, via label-generator)

## Ordre de développement suggéré

1. Copier le code depuis bone-recognition et bone-ml
2. Adapter les imports (`from src.modules.xxx`)
3. Créer `src/main.py` avec lifespan (BoneStore, PostgreSQL, CVAT)
4. Adapter le module training pour soumettre via ml-compute au lieu d'exécuter localement
5. Créer le module CVAT (client.py, sync.py)
6. Adapter le module predict pour CVAT (en plus du format LS existant)
7. Dashboard pipeline avec soumission via ml-compute
