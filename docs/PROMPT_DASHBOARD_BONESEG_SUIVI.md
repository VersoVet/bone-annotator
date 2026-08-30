# Prompt : Dashboard de suivi de l'apprentissage osseux dans bone-annotator

## Contexte

bone-ml expose maintenant un module `boneseg` complet. bone-annotator doit offrir un tableau de bord synthétique permettant de suivre l'avancée de l'apprentissage en temps réel — progression des annotations, qualité du modèle, activité de l'active learning, et état de la flotte GPU.

## Vue d'ensemble du dashboard

Le dashboard doit répondre en un coup d'oeil aux questions :
1. **Où en est-on ?** — Combien d'annotations GOLD, progression vers le prochain jalon
2. **Le modèle progresse-t-il ?** — Courbe Dice par génération
3. **Que faire ensuite ?** — Suggestions active learning prêtes
4. **La machine tourne-t-elle ?** — GPU occupé, job en cours

## Sections proposées

### 1. Barre de progression par type d'os

Pour chaque bone_type actif, afficher une barre de progression :

```
Humerus  ████████░░░░░░░░  487 / 2000 GOLD   (24%)
         Jalon: Premier modèle exploitable à 500
         Dernière annotation: il y a 3h
```

Jalons (depuis PROMPT_MAJ.txt) :
- 500 : Calibration des règles
- 2000 : Premier modèle (nnU-Net v0)
- 5000 : Modèle exploitable
- 10000 : Très bon segmentateur

**Source** : `GET bone-ml:9463/api/boneseg/catalog/stats?bone_type=humerus`

### 2. Répartition des tiers

Camembert ou barres empilées :

```
GOLD    ███████  487 (validé humain)
SILVER  ████     312 (ML + correction)
PSEUDO  █        89  (ML non vérifié)
---
Total annotés: 888 / 300 000 acquisitions
```

**Source** : `GET bone-ml:9463/api/boneseg/catalog/stats`

### 3. Courbe de progression du modèle

Graphique linéaire : Dice moyen par génération

```
Gen 1  ▪ 0.42  (487 images, smp_unet)
Gen 2  ▪ 0.58  (1200 images)
Gen 3  ▪ 0.71  (2500 images)  ← actuel
```

Avec par-class breakdown au survol.

**Source** : `GET bone-ml:9463/api/boneseg/train/history?bone_type=humerus`

### 4. Active Learning — Prochaines actions

```
📋 50 acquisitions suggérées pour annotation
   Stratégie: hybrid (entropy + diversité)
   Score moyen: 0.84
   [Créer les tâches CVAT] ← bouton

🆕 1 247 nouvelles acquisitions détectées sur BoneStore
   Dernière synchro: il y a 2h
   [Scanner maintenant]
```

**Source** :
- `POST bone-ml:9463/api/boneseg/active-learning/suggest`
- `GET bone-ml:9463/api/boneseg/catalog/new`

### 5. État GPU et jobs

```
🖥️ OnyxCortex (RTX 4070S 12GB)
   Job en cours: humerus_boneseg_gen3 (époque 47/100, 3h12m)
   VRAM: 11.2 / 12 GB

📊 File d'attente: 0 jobs en attente
```

**Source** :
- `GET ml-compute:9469/api/nodes/summary`
- `GET ml-compute:9469/api/jobs?status=running`

### 6. Test set gelé

```
Test set humerus: 150 acquisitions (gelé depuis 2026-08-15)
Test set femur: 0 (⚠️ non défini)

Dernier test Dice: 0.68 (gen 3)
```

**Source** : Requête PG directe `SELECT COUNT(*) FROM test_sets WHERE bone_type = $1`

### 7. Vélocité d'annotation

```
Cette semaine:  42 frames validées (↑ 15% vs semaine dernière)
Ce mois:       187 frames validées
Rythme actuel: ~6 frames/jour
Temps estimé pour 2000 GOLD: ~252 jours au rythme actuel
```

**Source** : Requête PG sur `frame_annotations` avec `validated_at` groupé par semaine

## Suggestions complémentaires pour un bon suivi

### 8. Alertes et notifications

- **Nouveau modèle prêt** : Notification quand un training termine (gen N+1 disponible)
- **Seuil d'annotation atteint** : Notification quand le GOLD atteint un jalon (500, 2000, 5000)
- **Régression modèle** : Alerte si test_dice diminue entre deux générations
- **BoneStore : nouvelles acquisitions** : Notification périodique quand > 100 nouvelles

Implémentation : via Redis pub/sub (canal `onyx:skill:status`) ou endpoint SSE existant (`/api/dashboard/events`).

### 9. Qualité des annotations — Métriques

- **Inter-annotator agreement** : Si plusieurs annotateurs, mesurer le Dice entre leurs annotations sur les mêmes images
- **Temps moyen par frame** : Calculé depuis les timestamps CVAT (created_at → validated_at)
- **Taux de correction ML** : % d'annotations ML qui ont été modifiées lors de la validation
- **Distribution par projection** : Face vs profil vs oblique (depuis les métadonnées BoneStore)

### 10. Historique des décisions

Conserver un log structuré des décisions d'apprentissage :
```json
{
  "date": "2026-08-30",
  "action": "training_started",
  "bone_type": "humerus", 
  "generation": 3,
  "gold_count": 487,
  "silver_count": 312,
  "trigger": "manual",
  "notes": "Premier entraînement après ajout des projections latérales"
}
```

Table PG `learning_decisions` ou simple fichier JSON append-only.

### 11. Comparaison modèle vs humain

Dashboard pour comparer les prédictions du modèle avec les annotations humaines :
- Grille d'images : prédiction modèle | annotation humaine | différence
- Tri par : incertitude décroissante (les cas les plus difficiles en premier)
- Permet à l'annotateur de comprendre où le modèle échoue

Endpoint : `POST bone-ml:9463/api/boneseg/predict` avec `return_uncertainty: true`

### 12. Export rapport hebdomadaire

Générer un résumé hebdomadaire automatique :
- Nombre d'annotations ajoutées
- Nouveau modèle entraîné ? Performances ?
- Acquisitions les plus incertaines restantes
- Recommandation : quel type d'os prioriser

Format : Markdown → envoyable par email via `email-notification` skill.

## Implémentation recommandée

1. **Page dédiée** : `/learning` dans bone-annotator (ou section du dashboard existant)
2. **Auto-refresh** : SSE ou polling 30s sur l'endpoint stats
3. **Responsive** : Doit fonctionner sur l'écran de la station d'annotation
4. **Pas de dépendance directe** : Tout passe par les APIs bone-ml et ml-compute (pas d'import croisé)

## Endpoints bone-ml à consommer

| Endpoint | Fréquence de polling | Données |
|----------|---------------------|---------|
| `GET /api/boneseg/catalog/stats` | 30s | Compteurs par statut et tier |
| `GET /api/boneseg/train/history` | 60s | Historique training + Dice |
| `GET /api/boneseg/models` | 60s | Modèles disponibles |
| `POST /api/boneseg/active-learning/suggest` | À la demande | Suggestions (bouton) |
| `POST /api/boneseg/catalog/sync` | À la demande | Scan BoneStore (bouton) |
| `GET /api/dashboard/stats` (bone-ml) | 30s | GPU fleet, system stats |
