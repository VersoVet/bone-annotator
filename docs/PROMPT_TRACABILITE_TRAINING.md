# Prompt : Traçabilité complète acquisition → tâche → training

## Contexte

bone-ml a corrigé ses JOINs pour utiliser `task_id` au lieu de `acquisition_id` afin d'éviter les doublons dans les données d'entraînement. bone-annotator doit maintenant garantir l'intégrité côté annotation.

## Problèmes à corriger dans bone-annotator

### 1. Garde d'unicité à la création de tâche

**Fichier** : `src/modules/annotation/service.py` — `create_task()`

Actuellement, rien n'empêche de créer 2 tâches pour la même acquisition+bone_type. Ajouter une vérification :

```python
async def create_task(self, request):
    # AVANT de créer la tâche, vérifier qu'il n'y a pas de tâche active
    existing = await self.task_db.find_active_task(
        request.acquisition_id, request.bone_type
    )
    if existing:
        return {
            "error": "active_task_exists",
            "existing_task_id": existing["id"],
            "status": existing["status"],
            "hint": "Utilisez POST /api/annotation/re-annotate/{task_id} pour re-annoter"
        }
    # ... suite normale ...
```

**Statuts "actifs"** (empêchent la re-création) : `preparing`, `created`, `annotating`, `reviewing`
**Statuts terminaux** (permettent de re-créer) : `validated`, `rejected`, `failed`

**Méthode à ajouter dans task_db.py** :
```python
async def find_active_task(self, acquisition_id: str, bone_type: str) -> dict | None:
    active_statuses = ('preparing', 'created', 'annotating', 'reviewing')
    row = conn.execute(
        """SELECT id, status, cvat_task_id FROM annotation_tasks
           WHERE acquisition_id = %s AND bone_type = %s AND status IN %s
           ORDER BY id DESC LIMIT 1""",
        (acquisition_id, bone_type, active_statuses)
    )
    return dict(row) if row else None
```

### 2. Validation par task_id (pas acquisition_id)

**Fichier** : `src/modules/storage/task_db.py` — méthode de validation

Le UPDATE actuel marque TOUTES les annotations de l'acquisition :
```sql
-- MAUVAIS
UPDATE frame_annotations SET validated_by=$1
WHERE acquisition_id=$2 AND validated_by IS NULL
```

Doit être :
```sql
-- CORRECT
UPDATE frame_annotations SET validated_by=$1, validated_at=NOW(),
    quality_tier = CASE WHEN source = 'manual' THEN 'gold'
                        WHEN source = 'corrected_ml' THEN 'silver'
                        ELSE 'pseudo' END
WHERE acquisition_id=$2 AND task_id=$3 AND validated_by IS NULL
```

### 3. Assurer que task_id est toujours rempli dans frame_annotations

Lors de l'insertion d'annotations (sync CVAT, pre-annotation ML), vérifier que le champ `task_id` est toujours renseigné. S'il est NULL, la traçabilité est rompue.

**Fichier** : `src/modules/annotation/cvat_sync.py` — `sync_from_cvat()`
**Fichier** : `src/modules/storage/pg_db.py` — `save_frame_annotations()`

### 4. Notifier bone-ml du task_id lors du changement de statut

Quand une tâche passe en statut `annotating`, informer bone-ml pour mettre à jour le `current_task_id` dans `bonestore_catalog` :

```python
# Dans annotation/service.py ou background.py, après création réussie :
async def _notify_catalog_status(acquisition_id, task_id, status):
    async with httpx.AsyncClient() as client:
        await client.post(
            f"http://{BONE_ML_HOST}:{BONE_ML_PORT}/api/boneseg/catalog/mark-status",
            json={
                "acquisition_ids": [acquisition_id],
                "status": status,  # 'annotating'
                "task_id": task_id
            }
        )
```

## Chaîne de traçabilité garantie

```
unified_context.json (session_id)
         │
         ▼
bonestore_catalog.session_id (bone-ml)
         │
         ▼
annotation_tasks.id (bone-annotator)
    ├── acquisition_id
    ├── bone_type
    ├── parent_task_id (re-annotation)
    └── status: validated
         │
         ▼
frame_annotations.task_id (bone-annotator)
    ├── quality_tier: gold/silver/pseudo
    └── validated_by, validated_at
         │
         ▼
boneseg_training_runs.task_ids[] (bone-ml)
    ├── generation
    ├── best_dice, per_class_dice
    └── model_output_path
         │
         ▼
modèle .pt (NFS)
```

Pour un modèle donné, on remonte :
`modèle → training_run.task_ids → annotation_tasks → frame_annotations → acquisition → session_id → unified_context.json`

## Tables PG modifiées (déjà migrées)

```sql
-- bonestore_catalog — colonnes ajoutées
session_id VARCHAR(100)       -- CLÉ TRAÇABILITÉ depuis unified_context.json
specimen_id VARCHAR(100)
acquisition_timestamp TIMESTAMP
accession VARCHAR(100)
species VARCHAR(50)
laterality VARCHAR(10)
pixel_spacing FLOAT
current_task_id INTEGER       -- tâche d'annotation en cours

-- boneseg_training_runs — colonne ajoutée
task_ids INTEGER[]            -- IDs des tâches utilisées pour ce training

-- bone-ml JOIN corrigé : fa.task_id = t.id (pas fa.acquisition_id = t.acquisition_id)
-- + DISTINCT ON pour ne garder que la dernière tâche validée par acquisition
```
