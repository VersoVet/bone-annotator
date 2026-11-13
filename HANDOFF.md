# Handoff — bone-annotator

- **When**: 2026-11-04 18:49:18 UTC
- **From**: previous
- **To**: claude
- **Reason**: credits epuises / switch manuel dashboard

## Instructions pour le nouvel agent

1. Lis ce fichier en entier (transcript ci-dessous).
2. Lis `TODO.md` et `ARCHITECTURE.md`.
3. Verifie `git status` / diffs recents.
4. Reprends le travail sans recommencer de zero.

## Transcript terminal (agent precedent)

```text
  injoignable (non bloquant).

  À faire côté humain : corriger les zones dans
  CVAT #28 (http://10.0.0.59:8080/tasks/28) →
  Sync → Valider GOLD → quality_tier=gold en PG.


  [Pasted text #1 +34 lines]


  Je vérifie l'état live S0 et je comble ce qui
  manque encore.

  $ curl -s -X POST
    http://10.0.0.59:9468/api/cvat/connect | jq -c
    .
    curl -s
    http://10.0.0.59:9468/api/annotation/task/4 |
    jq
    '.task|{id,status,cvat_task_id,frame_count,ann
    otated_frames,has_pre_annotations,cvat_url}'
    6.8s
    … 11 input + 53 output lines hidden · ctrl+o
    to expand
      "errors": []
    }

  $ # Confirm validate endpoint + gold path still
    wired; do NOT promote Otsu seeds to gold
    curl -s http://10.0.0.59:9468/openapi.json |
    jq '[.paths|to_entries[]|select(.key|test("pre
    -annotate|validate|tasks/failed|sync"))|.key]'
    999ms
    … 6 input + 18 output lines hidden · ctrl+o to
    expand
    2d35011f8147fb9072e6037f8d96d71e  /opt/onyx/s…
    21fe0663f6299b22a3db95b658496eee  /opt/onyx/s…

  S0 est déjà opérationnel (l’état « created / 0
  annotations » est obsolète).

  ┌────────────┬───────────────────────────────┐
  │ Check      │ Live                          │
  ├────────────┼───────────────────────────────┤
  │ Task 4     │ reviewing, CVAT #28, 929      │
  │            │ frames                        │
  ├────────────┼───────────────────────────────┤
  │ Pré-annot  │ 5 masks sur                   │
  │ CPU        │ [0,232,464,696,928]           │
  ├────────────┼───────────────────────────────┤
  │ Sync       │ 5 frames / 5 zones OK         │
  │ CVAT→PG    │                               │
  ├────────────┼───────────────────────────────┤
  │ Dashboard  │ Pré-annoter / Sync / Valider  │
  │            │ GOLD / Nettoyer échecs        │
  ├────────────┼───────────────────────────────┤
  │ DELETE     │ OK (0 failed)                 │
  │ /tasks/fai │                               │
  │ led        │                               │
  ├────────────┼───────────────────────────────┤
  │ Fallback   │ bone-ml down → CPU Otsu ;     │
  │            │ MedSAM2 Cortex OK             │
  └────────────┴───────────────────────────────┘

  Reste humain : corriger dans CVAT #28
  (http://10.0.0.59:8080/tasks/28) → Sync →
  Valider GOLD → quality_tier=gold.


  [Pasted text #1 +34 lines]


  Vérification rapide de l'état live — le S0 est
  déjà en place.

  $ curl -s
    http://10.0.0.59:9468/api/annotation/task/4 |
    jq -c '.task|{id,status,cvat_task_id,annotated
    _frames,frame_count,has_pre_annotations}'
    curl -s -X POST
    http://10.0.0.59:9468/api/annotation/sync/4 |
    jq -c . 14s
    … 4 input + 4 output lines hidden · ctrl+o to
    expand
    2
    2

  S0 opérationnel — rien à corriger côté code.

  • Task 4 : reviewing, CVAT #28, 5 zones
    syncées PG, pré-annot CPU OK
  • Dashboard : Pré-annoter / Sync / Valider
    GOLD / Nettoyer échecs
  • Fallback : CPU Otsu (Synapse sans GPU ;
    bone-ml down)

  Action restante : corriger dans CVAT #28
  (http://10.0.0.59:8080/tasks/28) → Sync →
  Valider GOLD.

  Finished Run Forge validate for bone-annotator

    Globbed  in ...e-onyx-projects-skills-bone-annot
ator/
            "terminals
            *
            .
            t
            x
            t
            "
    Found 21 files

  $ ls -lt /home/onyx/.cursor/projects/home-onyx-p
    rojects-skills-bone-annotator/terminals/
    2>/dev/null | head -20; rg -l
    "validate/bone-annotator|Forge validate"
    /home/onyx/.cursor/projects/home-onyx-projects
    -skills-bone-annotator/terminals/ 2>/dev/null
    | head -5 357ms
    … 23 output lines hidden · ctrl+o to expand
    /home/onyx/.cursor/projects/home-onyx-project…
    /home/onyx/.cursor/projects/home-onyx-project…

    Read …ls-bone-annotator/terminals/701320.txt

  La validation a renvoyé valid: false sans
  détail utile — je récupère le rapport complet.

  $ curl -s -X POST http://10.0.0.13:4080/api/vali
    date/bone-annotator | jq '{valid, summary,
    errors: [.phases[]?|select(.status=="error" or
    .valid==false)|{id,name,status,message:(.mess
    age//.error//.detail),issues:(.issues//.errors
    //.failures)[0:3]}], fail_count:
    ([.phases[]?|select(.status=="error" or
    .valid==false)]|length)}' 2>/dev/null | head
    -120 30s

    Monitored background tasks, 2 complete
    … 3 earlier items hidden
    Waited for shell
    Read ...ects-skills-bone-annotator/terminals/
    701323.txt
    Ran jq 'keys' /tmp/ba_validate.json; jq
    '.summary' /tmp/ba_validate.json; jq
    'paths(scalars) as $p |
    select(($p|tostring)|test("error|fail";"i"))
    | [$p, getpath($p)]' /tmp/ba_validate.json
    2>/dev/null | head -40
    # try common layouts
    jq 'if .phases then (.phases|type) elif
    .results then (.results|type) elif .report
    then (.report|keys) else empty end'
    /tmp/ba_validate.json
    wc -c /tmp/ba_validate.json

  Validate a échoué (3 erreurs). Je corrige
  complexité et couverture pour débloquer.

  $ jq -r '.errors[]' /tmp/ba_validate.json
    jq -r '.errors_detailed[] | "\(.code) \(.phase
    // .name // ""): \(.message //
    .correction.action // .)"'
    /tmp/ba_validate.json 2>/dev/null | head -20
    274ms
    … 1 input + 48 output lines hidden · ctrl+o to
    expand
      }
    ]

    Read 2 files
    Read
    src/modules/annotation/cpu_preannotate.py
    Read ...odules/annotation/tests/test_cpu_prea
    nnotate.py

    Edited cpu_preannotate.py +131 -77

    ▎      first = labels[0]
    ▎      return int(first["id"]),
    ▎  str(first.get("name", "zone"))
    ▎
    ▎+ def resolve_seed_frames(n_frames: int,
    ▎  max_seeds: int) -> list[int]:
    ▎+     """Spread seed indices across a frame
    ▎  series (includes first and last).
    ▎+
    ▎+     Args:
    ▎+         n_frames: Total number of frames.
    ▎+         max_seeds: Maximum seeds to
    ▎  place.
    ▎+
    ▎+     Returns:
    ▎+         Sorted unique frame indices.
    ▎ … truncated (224 more lines) · ctrl+r to
    ▎ review

    Edited test_cpu_preannotate.py +3

    ▎  from PIL import Image
    ▎
    ▎  from
    ▎  src.modules.annotation.cpu_preannotate
    ▎  import (
    ▎+     _strip_shape_ids,
    ▎      binary_mask_to_rle,
    ▎      bone_mask_from_frame,
    ▎+     build_seed_shapes,
    ▎      mask_to_bbox_points,
    ▎      otsu_threshold,
    ▎      pick_seed_label_id,
    ▎+     resolve_seed_frames,
    ▎  )
    ▎ … truncated (2 more lines) · ctrl+r to
    ▎ review

    Edited test_cpu_preannotate.py +33

    ▎      assert _is_success_status("started")
    ▎  is False
    ▎      assert _is_success_status("error:no
    ▎  model") is False
    ▎      assert _is_success_status("deferred:g
    ▎  pu_unavailable") is False
    ▎+
    ▎+
    ▎+ def test_resolve_seed_frames_spreads() ->
    ▎  None:
    ▎+     """Seed indices include endpoints and
    ▎  stay within bounds."""
    ▎+     frames = resolve_seed_frames(929, 5)
    ▎+     assert frames[0] == 0
    ▎+     assert frames[-1] == 928
    ▎+     assert len(frames) == 5
    ▎+     assert resolve_seed_frames(3, 5) ==
    ▎  [0, 1, 2]
    ▎ … truncated (24 more lines) · ctrl+r to
    ▎ review

    Edited cpu_preannotate.py +1 -7

    ▎      if not ok and use_mask:
    ▎          logger.warning("Mask push failed
    ▎  for CVAT #%s — retrying with rectangles",
    ▎  cvat_task_id)
    ▎          shapes =
    ▎  rectangles_from_masks(frame_files,
    ▎  shapes, label_id)
    ▎-         payload = {
    ▎-             "version": 0,
    ▎-             "shapes": existing_shapes +
    ▎  shapes,
    ▎-             "tracks": [],
    ▎-             "tags": [],
    ▎-         }
    ▎-         ok = await cvat_client.update_ann
    ▎  otations(int(cvat_task_id), payload)
    ▎+         ok, _ = await
    ▎  _merge_push_shapes(cvat_client,
    ▎  int(cvat_task_id), shapes)
    ▎      if not ok:
    ▎ … truncated (2 more lines) · ctrl+r to
    ▎ review

  $ source /opt/onyx/venv/bin/activate
    cd /home/onyx/projects/skills/bone-annotator
    8.7s
    … 12 input + 31 output lines hidden · ctrl+o
    to expand
    42 files skipped due to complete coverage.
    30 passed in 4.46s

  $ source /opt/onyx/venv/bin/activate
    cd /home/onyx/projects/skills/bone-annotator
    18s
    … 4 input + 17 output lines hidden · ctrl+o to
    expand
    For more information, try '--help'.
    1

  $ source /opt/onyx/venv/bin/activate
    cd /home/onyx/projects/skills/bone-annotator
    1.3s
    … 25 input + 35 output lines hidden · ctrl+o
    to expand
    src/modules/annotation/workflow_routes.py:39:…
    src/modules/annotation/workflow_routes.py:65:…

  $ scp -q /home/onyx/projects/skills/bone-annotat
    or/src/modules/annotation/cpu_preannotate.py \
      /home/onyx/projects/skills/bone-annotator/sr
    c/modules/annotation/tests/test_cpu_preannotat
    e.py \ 2.0s
    … 2 input lines hidden · ctrl+o to expand

  Forge validate : valid: false — 3 erreurs, 24
  warnings.

  ┌─────┬──────────────────────────────────────┐
  │ Cod │ Problème                             │
  │ e   │                                      │
  ├─────┼──────────────────────────────────────┤
  │ E99 │ push_cpu_seeds trop complexe →       │
  │ 9   │ corrigé (cc 26→10)                   │
  ├─────┼──────────────────────────────────────┤
  │ E00 │ Couverture 49% → corrigé (~50% +     │
  │ 9   │ tests CPU)                           │
  ├─────┼──────────────────────────────────────┤
  │ E00 │ 95 docstrings Args/Raises désalignés │
  │ 8   │ → encore bloquant                    │
  └─────┴──────────────────────────────────────┘

  S0 live reste OK ; le deploy Forge formel
  attend le fix docstrings.




  → Add a follow-up


  Auto · 31.5% · 24 files edited    Run Everything
  ~/projects/skills/bone-annotator · dev
```
