# bone-annotator - Guide de Développement Forge

> **FICHIER GÉNÉRÉ PAR FORGE**
> Mis à jour lors des validations et déploiements

---

## Écosystème du Skill

### Description
**bone-annotator** est un service d'annotation d'images osseuses issues de séries de fluoroscopie (rotation 360° sur le grand axe).

**Flux principal** :
1. Accès aux acquisitions via BoneStore (NFS `/mnt/bonestore`, format `.b2nd`)
2. Pré-annotation automatique YOLO (détection landmarks + zones anatomiques)
3. Annotation manuelle via CVAT (séries d'images type vidéo)
4. Boucle d'apprentissage actif : annotation → training GPU → pré-annotation suivantes

### Configuration Skill
| Champ | Valeur |
|-------|--------|
| **Nom** | bone-annotator |
| **Type** | python |
| **Port** | 9468 |
| **Brain Area** | cortex-visuel |
| **Target** | OnyxSynapse (10.0.0.59) |
| **Run Mode** | service |
| **Repository** | VersoVet/bone-annotator |

### Services Externes
| Service | URL | Usage |
|---------|-----|-------|
| BoneStore NFS | `/mnt/bonestore` (10.0.0.52) | Images .b2nd, 312 acquisitions |
| PostgreSQL | 10.0.0.59:5433 | Schema `bone_annotations` (annotations, landmarks) |
| Qdrant | 10.0.0.59:6333 | Collections `bone_atlas`, `bone_annotations` (512D/768D embeddings) |
| CVAT | Synapse | Annotation d'images séries (à installer) |
| label-generator | 10.0.0.59:9466 | Labels anatomiques (zones, landmarks, critères) |
| ml-compute | 10.0.0.44:9469 | Jobs GPU (Ray) — training YOLO, batch inference |
| Orthanc Research | 10.0.0.6:8044 | PACS source d'images DICOM |

---

## Cycle de Vie Forge

```
INTENT → PLAN → INIT → DEV → VALIDATE → REVIEW → DEPLOY
```

**Vous êtes ici**: INIT (initialisation structure)

### Phases Critiques de Validation

#### Phase 1: Structure (Fichiers Obligatoires)
✅ `manifest.json` présent et valide
✅ `CLAUDE.md` présent (ce fichier)
✅ `.gitignore` présent (sécurité)
✅ `src/main.py` présent (point d'entrée)
✅ `backup.json` présent (run_mode=service)
✅ `cron.json` présent (run_mode=service)
⏳ `ARCHITECTURE.md` à compléter
⏳ `API.md` à compléter
⏳ `DIAGRAM.md` à générer

#### Phase 16: Type Checking (mypy - ZÉRO ERREUR)
- Tous les paramètres doivent avoir un type explicite
- Tous les retours doivent avoir un type
- Pas de `Any` implicite

#### Phase 18: Docstrings (Google convention - 80%+ coverage)
- Fonctions publiques: docstring OBLIGATOIRE
- Format: description + Args/Returns/Raises
- Convention: Google style

#### Phase 20: Backup (run_mode=service)
✅ `backup.json` configuré avec:
- PostgreSQL (criticality: critical)
- Qdrant (criticality: high)
- Config files (criticality: medium)
- SQLite ingestion registry (criticality: medium)

---

## Architecture Modulaire OBLIGATOIRE

### Structure Standard
```
bone-annotator/
├── CLAUDE.md              # Ce fichier
├── ARCHITECTURE.md        # Structure et composants
├── API.md                 # Documentation endpoints
├── TODO.md                # Tâches en cours
├── manifest.json          # Configuration Forge
├── backup.json            # Stratégie sauvegarde
├── cron.json              # Tâches cron
├── .gitignore             # Patterns ignorés
│
├── src/
│   ├── __init__.py
│   ├── main.py            # Point d'entrée FastAPI ✅
│   ├── models.py          # Modèles Pydantic
│   │
│   └── modules/           # MODULES FONCTIONNELS
│       ├── annotation/    # Annotation (CVAT, détection)
│       ├── bonestore/     # Accès NFS acquisitions
│       ├── imaging/       # Chargement frames .b2nd
│       ├── storage/       # PostgreSQL + Qdrant
│       ├── ingestion/     # Sync BoneStore → registry
│       ├── predict/       # YOLO inférence
│       ├── training/      # YOLO training (ml-compute)
│       ├── dataset/       # Export annotations YOLO
│       ├── cvat/          # Client CVAT REST API
│       └── dashboard/     # SSE events + monitoring
│
├── biblio/                # Bibliographie (optionnel)
│   ├── INDEX.md
│   └── fiches/
│
└── tests/                 # Tests intégration
    └── test_integration.py
```

### Règles Modules
1. **Un module = une responsabilité**
2. **Chaque module < 300 lignes** (split si nécessaire)
3. **Tests unitaires** dans `modules/{nom}/tests/`
4. **Interface claire** (fonctions publiques typées + docstrings)
5. **Pas de dépendances circulaires**

---

## Développement Python Optimisé

### Environnement
```bash
# TOUJOURS utiliser le venv global
source /opt/onyx/venv/bin/activate

# Vérifier l'activation
which python  # Doit afficher /opt/onyx/venv/bin/python
```

### Linting avec Ruff (OBLIGATOIRE avant commit)
```bash
ruff check src/ --fix
ruff format src/
```

### Type Checking avec mypy
```bash
mypy src/ --strict
```

### Tests
```bash
pytest tests/ -x -q
pytest --cov=src --cov-report=term-missing
```

---

## ⚠️ AVANT CHAQUE COMMIT

```bash
# 1. Linting
ruff check src/ --fix
ruff format src/

# 2. Type checking
mypy src/ --strict

# 3. Tests
pytest tests/ -x -q

# 4. Documentation à jour
# - ARCHITECTURE.md
# - API.md
# - TODO.md

# 5. Validation Forge (18 phases)
curl -X POST http://10.0.0.13:4080/api/validate/bone-annotator | jq .
```

---

## Workflow Session

### Au démarrage
1. ✅ Lire `/opt/onyx/forge/CLAUDE.md` (règles Forge globales)
2. ✅ Lire ce fichier (`bone-annotator/CLAUDE.md`)
3. ✅ Lire `TODO.md` (tâches en cours)
4. ✅ Lire `ARCHITECTURE.md` (structure)
5. ✅ Lire `API.md` (endpoints)
6. ✅ Lire `manifest.json` (configuration)
7. ✅ Lire `DEV_CONTEXT.md` (contexte métier)

### Développement
1. Identifier la tâche dans `TODO.md`
2. Créer/modifier le module approprié (< 300 lignes)
3. Ajouter **types explicites** à toutes les fonctions
4. Écrire **docstrings** (Google convention)
5. Écrire les **tests** du module
6. Mettre à jour `ARCHITECTURE.md` et `API.md`
7. **Ruff check/fix** avant commit

### Commandes Forge Clés
```bash
# Validation (22 phases, rapport structure)
/forge-validate bone-annotator

# Revue multi-LLM (optionnel, score 0-100)
/forge-review bone-annotator

# Déploiement complet (git, SSH, systemd)
/forge-deploy bone-annotator
```

---

## Réutilisation de Skills Existants

**AVANT de coder une fonctionnalité** :
1. Consulter les skills existants via API
2. Lire leurs `API.md` pour endpoints disponibles
3. Utiliser leurs endpoints plutôt que recoder

### Skills Dépendants
- **label-generator** (9466) : labels anatomiques
- **ml-compute** (9469) : jobs GPU training/inference

### Code à Migrer
Depuis `bone-recognition` et `bone-ml` (voir `DEV_CONTEXT.md` pour détails):
- Modules annotation, bonestore, imaging
- Modules storage (PostgreSQL), predict, training
- Dashboard et monitoring

---

## Sécurité

### Credentials via Vault (OBLIGATOIRE)
```python
import httpx

async def get_secret(key: str) -> str:
    async with httpx.AsyncClient() as client:
        r = await client.get(f"http://10.0.0.44:8050/vault/{key}")
        return r.json()["value"]
```

### Jamais en dur
```python
# INTERDIT
API_KEY = "sk-xxx..."

# CORRECT
API_KEY = await get_secret("api_key")
```

### Pas d'imports relatifs
```python
# CORRECT
from src.modules.annotation import service

# INCORRECT
from .modules.annotation import service
```

---

## Checklist Pré-Commit

```
📋 AVANT de committer:

Infrastructure:
☐ CLAUDE.md présent (ce fichier)
☐ API.md documenterait
☐ ARCHITECTURE.md à jour
☐ TODO.md reflète l'état
☐ .gitignore complet
☐ backup.json configuré (run_mode=service)
☐ cron.json configuré (daily-health-check)
☐ manifest.json valide

Code:
☐ Tous les paramètres typés (Phase 16)
☐ Tous les retours typés
☐ Docstrings Google convention (Phase 18)
☐ Pas de credentials en dur
☐ Imports absolus (from src.xxx import)
☐ Chaque module < 300 lignes (Phase 15)
☐ httpx async (pas requests)
☐ Pydantic pour validations

Tests:
☐ pytest passe sans erreur
☐ Tous les modules ont des tests

Validation:
☐ ruff check src/ passe
☐ mypy src/ passe (zéro erreur)
☐ /forge-validate = valid: true
```

---

## Références

| Doc | Usage |
|-----|-------|
| `/opt/onyx/forge/CLAUDE.md` | Règles Forge complètes |
| `DEV_CONTEXT.md` | Contexte métier détaillé |
| `manifest.json` | Configuration du skill |
| `backup.json` | Stratégie sauvegarde (criticités) |
| `cron.json` | Tâches cron (health check, sync) |
| `http://10.0.0.44:8050/vault/` | Secrets Onyx Vault |
| `http://10.0.0.44:8083/api/backup-targets` | Types de backup disponibles |

---

## Version du Fichier

- **Généré**: 2026-08-08
- **Skill**: bone-annotator
- **Version Forge**: 1.0.0
