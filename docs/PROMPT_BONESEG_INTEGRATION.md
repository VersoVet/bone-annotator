# Prompt : Intégration BoneSeg dans bone-annotator

## Contexte

bone-ml a maintenant un module `boneseg` complet pour la segmentation osseuse avec :
- Modèle BoneSegNet (smp U-Net + MC-Dropout) 
- Estimation d'incertitude pour active learning
- Catalogue BoneStore (suivi des 300k acquisitions)
- Training pipeline tier-aware (GOLD/SILVER/PSEUDO)
- Auto-annotation CVAT

bone-annotator doit s'adapter pour utiliser ces nouvelles capacités.

## Modifications nécessaires

### 1. Schema PostgreSQL — Migration

Exécuter ces migrations sur `bone_recognition` (schema `bone_annotations`) :

```sql
-- Colonne quality_tier sur frame_annotations
ALTER TABLE bone_annotations.frame_annotations
  ADD COLUMN IF NOT EXISTS quality_tier VARCHAR(10) DEFAULT 'silver';

-- Peuplement initial basé sur source + validation
UPDATE bone_annotations.frame_annotations
  SET quality_tier = 'gold'
  WHERE source = 'manual' AND validated_by IS NOT NULL;

UPDATE bone_annotations.frame_annotations
  SET quality_tier = 'silver'  
  WHERE source = 'corrected_ml' AND validated_by IS NOT NULL;

UPDATE bone_annotations.frame_annotations
  SET quality_tier = 'pseudo'
  WHERE source = 'ml' AND validated_by IS NULL;

-- Table test set gelé
CREATE TABLE IF NOT EXISTS bone_annotations.test_sets (
  id SERIAL PRIMARY KEY,
  bone_type VARCHAR(50) NOT NULL,
  acquisition_id VARCHAR(100) NOT NULL,
  added_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(bone_type, acquisition_id)
);

-- Catalogue BoneStore pour suivi ML
CREATE TABLE IF NOT EXISTS bone_annotations.bonestore_catalog (
  id SERIAL PRIMARY KEY,
  acquisition_id VARCHAR(100) NOT NULL UNIQUE,
  bone_type VARCHAR(50),
  category VARCHAR(100),
  frame_count INT DEFAULT 0,
  source_path VARCHAR(500),
  first_seen TIMESTAMP DEFAULT NOW(),
  ml_status VARCHAR(20) DEFAULT 'new',
  uncertainty_score FLOAT,
  uncertainty_model VARCHAR(200),
  scored_at TIMESTAMP,
  annotation_tier VARCHAR(10),
  in_test_set BOOLEAN DEFAULT FALSE,
  last_trained_gen INT,
  notes VARCHAR(500)
);
CREATE INDEX IF NOT EXISTS idx_catalog_status ON bone_annotations.bonestore_catalog(ml_status);
CREATE INDEX IF NOT EXISTS idx_catalog_bone ON bone_annotations.bonestore_catalog(bone_type);
CREATE INDEX IF NOT EXISTS idx_catalog_score ON bone_annotations.bonestore_catalog(uncertainty_score DESC);

-- Table training runs boneseg
CREATE TABLE IF NOT EXISTS bone_annotations.boneseg_training_runs (
  id SERIAL PRIMARY KEY,
  run_name VARCHAR(200) NOT NULL,
  bone_type VARCHAR(50) NOT NULL,
  generation INT DEFAULT 1,
  parent_run_id INT REFERENCES boneseg_training_runs(id),
  model_backend VARCHAR(50) DEFAULT 'smp_unet',
  bone_classes JSONB NOT NULL,
  tiers_used JSONB NOT NULL,
  train_count INT, val_count INT, test_count INT,
  epochs INT, best_dice FLOAT,
  per_class_dice JSONB,
  test_dice FLOAT,
  model_output_path VARCHAR(500),
  status VARCHAR(20) DEFAULT 'running',
  started_at TIMESTAMP DEFAULT NOW(),
  completed_at TIMESTAMP
);
```

### 2. Peuplement quality_tier à la sauvegarde

Dans `src/modules/annotation/cvat_sync.py` ou `src/modules/storage/pg_db.py`, quand des annotations sont insérées :

```python
# Règle de peuplement du tier :
if source == "manual" and validated_by is not None:
    quality_tier = "gold"
elif source in ("corrected_ml", "import") and validated_by is not None:
    quality_tier = "silver"
elif source == "ml":
    quality_tier = "pseudo"
else:
    quality_tier = "silver"  # défaut
```

### 3. Appeler BoneSeg pour pré-annotation

Dans `src/modules/annotation/ml_bridge.py`, modifier `call_bone_ml_annotate()` :

```python
# Avant d'appeler /api/cvat/annotate (YOLO), vérifier si un modèle boneseg existe
async def call_bone_ml_annotate(cvat_task_id, bone_type=None):
    # 1. Essayer boneseg d'abord
    try:
        resp = await client.post(
            f"http://{BONE_ML_HOST}:{BONE_ML_PORT}/api/boneseg/annotate",
            json={"cvat_task_id": cvat_task_id, "bone_type": bone_type}
        )
        if resp.status_code == 200 and "error" not in resp.json():
            return "ok_boneseg"
    except Exception:
        pass
    
    # 2. Fallback YOLO
    # ... code existant ...
```

### 4. Active Learning — Orchestration

Ajouter un endpoint ou un cron dans bone-annotator qui :
1. Appelle `POST bone-ml:9463/api/boneseg/catalog/sync` pour détecter les nouvelles acquisitions
2. Appelle `POST bone-ml:9463/api/boneseg/active-learning/suggest` pour obtenir les plus informatives
3. Crée automatiquement des tâches CVAT pour les acquisitions suggérées
4. Appelle `POST bone-ml:9463/api/boneseg/catalog/mark_status` avec status='annotating'

### 5. Gestion du test set gelé

Ajouter un endpoint pour sélectionner les acquisitions du test set :
- Séparation par **acquisition** (pas par frame) pour éviter les fuites
- Idéalement diversifié : différents animaux, races, projections
- Une fois ajouté au test set, jamais utilisé pour training

### 6. Contrainte GPU unique

Avec une seule RTX 4070S sur OnyxCortex :
- Vérifier `GET bone-ml:9463/api/boneseg/train/history` avant de lancer un training
- Si un job est en cours (status='running'), ne pas en lancer un nouveau
- Le scoring d'incertitude et le training ne peuvent pas tourner simultanément
- Utiliser `GET ml-compute:9469/api/jobs?status=running` pour vérifier

## Endpoints bone-ml à appeler

| Endpoint | Méthode | Usage |
|----------|---------|-------|
| `/api/boneseg/predict` | POST | Prédiction sur une image |
| `/api/boneseg/uncertainty` | POST | Scoring incertitude batch |
| `/api/boneseg/models` | GET | Liste des modèles disponibles |
| `/api/boneseg/train` | POST | Lancer un training |
| `/api/boneseg/train/history` | GET | Historique des runs |
| `/api/boneseg/annotate` | POST | Auto-annoter une tâche CVAT |
| `/api/boneseg/catalog/sync` | POST | Scanner BoneStore |
| `/api/boneseg/catalog/stats` | GET | Stats du catalogue |
| `/api/boneseg/catalog/new` | GET | Nouvelles acquisitions |
| `/api/boneseg/active-learning/suggest` | POST | Suggestions AL |
| `/api/boneseg/active-learning/score-pool` | POST | Scorer le pool |
