# TODO - bone-annotator

## Phase 1: Migration du Code (PRIORITÉ HAUTE)

- [ ] Migrer modules bonestore, imaging, storage depuis bone-recognition
  - [ ] `src/modules/bonestore/service.py` — Traversée NFS BoneStore (172 lignes)
  - [ ] `src/modules/imaging/service.py` — Chargement frames .b2nd, cache LRU (205 lignes)
  - [ ] `src/modules/imaging/catalog.py` — Taxonomie anatomique (60 lignes)
  - [ ] `src/modules/storage/pg_db.py` — Client PostgreSQL (418 lignes)

- [ ] Migrer modules annotation, predict, dataset depuis bone-ml
  - [ ] `src/modules/annotation/service.py` — Service annotation principal (434 lignes)
  - [ ] `src/modules/annotation/routes.py` — Routes FastAPI (167 lignes)
  - [ ] `src/modules/predict/service.py` — Inférence YOLO (249 lignes)
  - [ ] `src/modules/dataset/service.py` — Export YOLO format (218 lignes)

- [ ] Migrer modules ingestion, analysis depuis bone-recognition
  - [ ] `src/modules/ingestion/service.py` — Ingestion BoneStore (439 lignes)
  - [ ] `src/modules/ingestion/registry.py` — Registre SQLite (385 lignes)
  - [ ] `src/modules/analysis/` — Post-inférence (~890 lignes)

## Phase 2: Création Modules CVAT (PRIORITÉ HAUTE)

- [ ] Créer module CVAT
  - [ ] `src/modules/cvat/client.py` — Client REST CVAT API
  - [ ] `src/modules/cvat/sync.py` — Synchronisation annotations CVAT ↔ PostgreSQL
  - [ ] `src/modules/cvat/format.py` — Conversion format CVAT → internal
  - [ ] Tests unitaires

- [ ] Adapter module training pour ml-compute
  - [ ] Migrer depuis bone-ml
  - [ ] Adapter pour Ray Jobs API (ml-compute:9469) au lieu d'exécution locale
  - [ ] Callback handler pour résultats training

## Phase 3: Adaptation Dependencies Externes ✓ COMPLÈTE

- [x] Créer `src/config.py` avec configuration centralisée
  - [x] Check BoneStore NFS
  - [x] Connexion PostgreSQL (bone_annotations)
  - [x] Connexion Qdrant (collections)
  - [x] Check CVAT API
  - [x] Check ml-compute Ray
  - [x] Check Redis

- [x] Implémenter lifespan avec checks réels
  - [x] wait_for_dependency avec backoff exponentiel
  - [x] Intégration OnyxClient (déjà fait)
  - [x] Événements startup/shutdown

- [x] Ajouter endpoints de monitoring
  - [x] `/api/config` — Configuration des dépendances
  - [x] `/api/dependencies` — État détaillé des dépendances

- [x] Intégration label-generator
  - [x] Module `src/modules/labels/service.py`
  - [x] Cache local labels + critères
  - [x] Sync depuis label-generator
  - [x] Validation annotations

## Phase 4: Dashboard & Monitoring ✓ COMPLÈTE

- [x] Service dashboard (Phase 2 - déjà migré)
  - [x] Events service avec EventBus
  - [x] Monitoring service avec métriques
  - [x] Pipeline status tracking

- [x] Pages HTML dashboard
  - [x] `static/index.html` — Dashboard principal (422 lignes)
  - [x] `static/training.html` — Monitoring training (335 lignes)
  - [x] `static/annotations.html` — Historique annotations (415 lignes)

- [x] Endpoints de monitoring
  - [x] `/annotate/` — Page HTML dashboard
  - [x] `/api/training/status` — État des jobs training
  - [x] `/api/annotations` — Liste annotations
  - [x] `/api/events` — Stream SSE des événements

## Phase 5: Tests & Validation

- [ ] Tests unitaires chaque module
  - [ ] `src/modules/*/tests/test_*.py`
  - [ ] Couverture minimum 80%

- [ ] Tests intégration
  - [ ] `tests/test_integration.py`
  - [ ] Flux complet: BoneStore → CVAT → training

- [ ] Validation Forge (22 phases)
  - [ ] `/forge-validate bone-annotator`
  - [ ] Corriger erreurs structure/type/docstrings

- [ ] Revue multi-LLM
  - [ ] `/forge-review bone-annotator`
  - [ ] Score ≥ 70/100

## Phase 6: Déploiement

- [ ] `/forge-deploy bone-annotator`
  - [ ] Git push branch dev → main
  - [ ] SSH sync OnyxSynapse
  - [ ] systemd restart bone-annotator
  - [ ] Health check

- [ ] Post-deploy audit
  - [ ] Vérifier connexions PostgreSQL, Qdrant
  - [ ] Ingestion sync première exécution
  - [ ] Monitoring logs

---

## Documentation

- [x] CLAUDE.md créé
- [x] ARCHITECTURE.md créé
- [x] API.md créé
- [ ] DIAGRAM.md (diagramme Mermaid architecture)
- [x] manifest.json valide
- [x] backup.json créé
- [x] cron.json créé
- [x] .gitignore créé

---

## Dépendances Internes

```
predict → imaging → bonestore
       ↓
    storage (PostgreSQL)
       ↓
     cvat → annotation
             ↓
          training → ml-compute
             ↓
          dataset
             ↓
        dashboard
```

---

## Données Critiques

- PostgreSQL schema `bone_annotations` — **CRITICAL** (irremplaçable)
- Qdrant collections — **HIGH** (vectorisation)
- SQLite ingestion registry — **MEDIUM** (reconstructible)

---

## Références

- DEV_CONTEXT.md — Contexte métier détaillé
- bone-recognition/ — Source modules annotation
- bone-ml/ — Source modules training/predict
- `/opt/onyx/forge/CLAUDE.md` — Règles Forge complètes

---

**Dernière mise à jour**: 2026-08-08
**État**: Initialisation terminée, migration en cours
