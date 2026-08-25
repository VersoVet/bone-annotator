# ChEX: Interactive Localization and Region Description in Chest X-rays

**Auteurs** : Philip C. Müller, Georgios Kaissis, Daniel Rueckert
**Année** : 2024
**DOI** : 10.48550/arxiv.2404.15770

## Résumé

Report generation models offer fine-grained textual interpretations of medical images like chest X-rays, yet they often lack interactivity (i.e. the ability to steer the generation process through user queries) and localized interpretability (i.e. visually grounding their predictions), which we deem essential for future adoption in clinical practice. While there have been efforts to tackle these issues, they are either limited in their interactivity by not supporting textual queries or fail to also offer localized interpretability. Therefore, we propose a novel multitask architecture and training paradigm integrating textual prompts and bounding boxes for diverse aspects like anatomical regions and pathologies. We call this approach the Chest X-Ray Explainer (ChEX). Evaluations across a heterogeneous set of 9 chest X-ray tasks, including localized image interpretation and report generation, showcase its competitiveness with SOTA models while additional analysis demonstrates ChEX's interactive capabilities.

## Méthodologie

{'study_design': "Proposition d'une architecture multitâche novatrice intégrant des prompts textuels et des boîtes englobantes pour divers aspects (régions anatomiques, pathologies, phrases de rapport). Étant donné une radiographie thoracique et une requête utilisateur (prompt textuel, ex. nom de pathologie ou région anatomique, ou boîte englobante), le modèle prédit une description textuelle de la région ou de l'aspect interrogé, avec prédiction de boîtes englobantes pertinentes pour les prompts textuels", 'intervention': 'Modèle ChEX (Chest X-Ray Explainer) supportant à la fois requêtes textuelles et boîtes englobantes en entrée, prédisant des descriptions textuelles localisées', 'control': None, 'primary_outcomes': ['Performance sur 9 tâches de radiographie thoracique, incluant génération de rapports (RG), détection de pathologies/objets (OD), ancrage de phrases (SG), classification de régions (RC), et explication de régions (RE)'], 'secondary_outcomes': ['Capacités interactives de ChEX en réponse à des prompts utilisateur spécifiques'], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'Performance ChEX vs TransVG (SupVG, avec backbone CheXzero) sur Sentence Grounding', 'value': 'similaire, avec avantage de TransVG sur mIoU', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, C.1 Sentence Grounding (SG) Task', 'source_quote': 'ChEX demonstrates similar performance to the only generative model OmniFM-DR [83] and the best SupVG model TransVG [9] (with CheXzero [71] backbone), where TransVG shows an advantage on the mIoU metric.'}, {'outcome': 'ChEX vs TransVG sans backbone CheXzero sur mAP', 'value': '18', 'unit': '% mAP (amélioration)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, C.1 Sentence Grounding (SG) Task', 'source_quote': 'ChEX outperforms TransVG without the CheXzero backbone by 18% mAP and is within 1-std on mIoU.'}, {'outcome': 'ChEX vs TransVG sans backbone CheXzero sur mIoU', 'value': 'dans 1 écart-type', 'unit': 'std', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, C.1 Sentence Grounding (SG) Task', 'source_quote': 'ChEX outperforms TransVG without the CheXzero backbone by 18% mAP and is within 1-std on mIoU.'}, {'outcome': 'ChEX vs meilleur baseline (Faster R-CNN + BioVIL, entraîné sur VinDr-CXR) sur Region Classification (RC), dataset MS-CXR', 'value': '8', 'unit': '% (amélioration)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, région classification (RC) (Tab. 9)', 'source_quote': 'The best baseline on MS-CXR is the Faster R-CNN with BioVIL backbone, trained on VinDr-CXR, and is outperformed by 8%'}, {'outcome': 'ChEX vs meilleur baseline (BioVIL, modèle contrastif) sur Region Classification (RC), dataset CIG', 'value': '5', 'unit': '% (amélioration)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, région classification (RC) (Tab. 9)', 'source_quote': 'on CIG the best baseline is the contrastive model BioVIL, which is outperformed by 5%'}], 'qualitative_findings': ['TransVG a été entraîné explicitement sur la tâche de Sentence Grounding, contrairement à ChEX.', "La supériorité de ChEX sur les modèles contrastifs souligne l'importance de la supervision par bounding box pour une localisation précise."], 'main_findings': ['Sur la tâche de Sentence Grounding (SG), ChEX obtient des performances similaires au meilleur modèle génératif (OmniFM-DR) et au meilleur modèle SupVG (TransVG avec backbone CheXzero), avec un avantage de TransVG sur mIoU.', 'ChEX surpasse TransVG (sans backbone CheXzero) de 18% sur mAP et reste dans 1 écart-type sur mIoU.', 'Sur la tâche de Region Classification (RC), ChEX surpasse clairement tous les baselines, avec +8% sur MS-CXR (vs Faster R-CNN+BioVIL) et +5% sur CIG (vs BioVIL contrastif).']}

## Conclusions

Les auteurs proposent ChEX, un modèle pour prédire des descriptions textuelles visuellement ancrées de radiographies thoraciques basées sur des requêtes utilisateur ChEX démontre une performance compétitive par rapport aux modèles SOTA sur 9 tâches ChEX est réactif aux invites utilisateur (prompts), posant ainsi les bases pour de futures avancées dans les modèles de génération de texte interactifs et localisés Même des modèles de langage plus petits peuvent atteindre une performance compétitive lorsque les améliorations priorisent la compréhension d'image Une combinaison synergique d'un encodage d'image optimal avec un focus régional, associée aux capacités déductives et aux connaissances des LLMs, représente une voie prometteuse pour améliorer la génération de rapports Un haut degré d'interprétabilité et l'intégration d'experts médicaux dans le processus de génération (interactivité) offrent une voie plus prometteuse vers l'application clinique que la seule amélioration de la qualité des prédictions

## Benchmark tasks with their datasets and evaluation metrics

| Task Dataset | #Samples #Classes Evaluation Metrics |
| --- | --- | --- | --- |
| Sentence Grounding (SG): Predicting bounding boxes for given sentences |
| MS-CXR [4] | 169 | none mIoU, mAP |
| Pathology Detection (OD): Object detection of pathologies |
| VinDrCXR [54] | 1,500 | top 15 mAP |
| NIH ChestXray (NIH8) [76] | 448 | 8 mAP |
| MS-CXR [4] | 169 | 8 mAP |
| Region Classification (RC): Classifying regions defined by given bounding boxes |
| MS-CXR [4] | 169 | 8 AUROC |
| Chest ImaGenome (CIG) [79] | 3,402 | 53 weighted AUROC (wAUROC) |
| Region Explanation (RE): Predicting descriptions for regions defined by bounding boxes |
| MS-CXR [4] | 169 | none | METEOR [1] Mic-F1-14 † , Mac-F1-14 † |
| Chest ImaGenome (CIG) [79] | 3,402 | none | METEOR [1] Mic-F1-14 † , Mac-F1-14 † |
| Full Report Generation (RG): Predicting full reports from chest X-rays |
|  |  |  | METEOR [1] |
| MIMIC-CXR [30] | 3,082 | none |  |

## In: CVPR. pp. 16772-16782 (2022). https://doi.org/10.1109/CVPR52688.2022.

| 01629 |
| --- |
| 93. Zhou, X., Girdhar, R., Joulin, A., Krähenbühl, P., Misra, I.: Detecting twenty- |
| thousand classes using image-level supervision. In: Avidan, S., Brostow, G., Cissé, |
| M., Farinella, G.M., Hassner, T. (eds.) Computer Vision -ECCV 2022. pp. 350- |
| 368. Springer Nature Switzerland, Cham (2022). https://doi.org/10.1007/978- |
| 3-031-20077-9_21 |
| 94. Zhu, X., Su, W., Lu, L., Li, B., Wang, X., Dai, J.: Deformable DETR: de- |
| formable transformers for end-to-end object detection. In: ICLR (2021), https: |
| //openreview.net/forum?id=gZ9hCDWe6ke |
| 95. Zong, Z., Song, G., Liu, Y.: Detrs with collaborative hybrid assignments training. |
| In: ICCV. pp. 6725-6735 (2023). https://doi.org/10.1109/ICCV51070.2023. |

## Ablation study on the forms of supervision (i.e. token and target types) used for multitask training. We study using only pathology tokens (P-only), only anatomy tokens (A-only), and only sentence tokens (S-only). Additionally, we study the exclusion of specific tokens types (No-P, No-A, No-S). We also study the exclusion of specific target types like bounding box targets (no box), pathology class targets (No cls), and sentence targets (No sent). Best results and those within one std are marked in bold. The symbols M , V , and N indicate that images from MIMIC-CXR, VinDr-CXR, and NIH8 are used for training, respectively.

| ChEX | Token Types | Target Types |
| --- | --- | --- |

## Effect of different prompt sets (anatomy or pathology prompts or both) and filtering (using only regions with positive pathologies) for full report generation. The default setting used by ChEX is highlighted in grey, best results are marked in bold.

|  | Prompt sets |  |  | MIMIC-CXR |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Anatomy Pathology [Mic-F1-14] [Mac-F1-14] [Ex-F1-14] [Mic-P-14] [Mic-R-14] [METEOR] |
| yes | yes | 51.04 | 30.61 | 57.05 | 42.99 | 62.80 | 13.90 |
| yes | positive | 50.13 | 30.67 | 56.91 | 42.46 | 61.22 | 13.60 |
| yes | no | 50.08 | 30.07 | 56.97 | 42.66 | 60.64 | 12.67 |
| positive yes | 52.37 | 32.69 | 58.78 | 45.09 | 62.44 | 13.28 |
| positive positive | 52.02 | 32.88 | 58.36 | 44.64 | 62.33 | 12.24 |
| positive no | 51.27 | 32.18 | 58.82 | 45.16 | 59.31 | 10.77 |
| no | yes | 50.35 | 25.82 | 59.35 | 47.88 | 53.10 | 9.82 |
| no | positive | 50.39 | 26.69 | 60.14 | 49.38 | 51.44 | 8.26 |

## Sentence grounding (SG) results on the MS-CXR dataset. We indicate the use of training or evaluation images from VinDr-CXR by V , from MIMIC-CXR byM , and from other sources by O . All results are based on our own experiments, except OmniFM-DR for which we show the results reported by the original paper. We provide the std based on bootstrapping with N = 250. Best results and those within 1-std are marked in bold.

|  | Sentence Grounding (SG) |
| --- | --- | --- |
|  | MS-CXR M |
|  | [mIoU] | [mAP] |
| ChEX V M | 47.52±1.45 44.47±2.21 |
| Zeroshot Contrastive Models |  |
| BioVIL [4] (masks) M | 22.75±1.26 | - |
| BioVIL [4] (boxes) M | 28.57±1.31 18.62±1.37 |
| CheXzero [71] (masks) M | 11.94±0.59 | - |
| CheXzero [71] (boxes) M | 15.45±0.67 | 5.94±0.64 |
| Multitask Generative Models |  |
| OmniFM-DR [83] V M O | 46.2 | - |
| Supervised Visual Grounding |  |
| TransVG [9] M | 48.81±1.45 37.65±2.61 |
| TransVG [9] (BioVIL [4]) M | 52.13±1.73 41.24±2.73 |
| TransVG [9] (CheXzero [71]) M 53.51±1.53 44.05±2.63 |

## Region explanation (RE) results on the MS-CXR dataset. We indicate the use of training or evaluation images from VinDr-CXR by V and from MIMIC-CXR byM . All results are based on our own experiments and we provide the std based on bootstrapping with N = 10. Best results and those within 1-std are marked in bold.

|  |  | Region Explanation (RE) |  |
| --- | --- | --- | --- | --- |
|  |  | MS-CXR M |  |  |
|  | [Mic-F1-14] [Mac-F1-14] [Mic-F1-5+] [Mac-F1-5+] [METEOR] |
| ChEX V M | 49.97±2.24 20.50±1.54 62.54±1.50 44.95±2.23 8.79±0.54 |
| Generative Models |  |  |  |
| RGRG [70] M | 48.97±2.50 16.37±2.00 60.39±2.21 | 38.34±2.23 | 8.15±0.78 |
| Zeroshot Contrastive Models (Nearest Neighbor, ROI pooled) |  |
| BioVIL [4] M | 5.86±1.41 | 3.69±0.67 12.79±2.25 | 10.95±1.93 | 3.82±0.03 |
| CheXzero [71] M | 5.41±1.30 | 3.40±0.78 11.00±2.25 | 9.02±1.83 | 3.47±0.45 |

## 53.34±0.43 29.13±0.35 44.53±0.40 39.19±0.37 10.18±0.13

| Generative Models |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| RGRG [70] M | 45.26±0.44 20.88±0.19 31.93±0.31 | 27.86±0.32 7.88±0.10 † |
| Zeroshot Contrastive Models (Nearest Neighbor, ROI pooled) |  |
| BioVIL [4] M | 24.40±0.38 | 7.15±0.10 | 9.42±0.22 | 7.45±0.16 | 3.82±0.03 |
| CheXzero [71] M 21.86±0.35 | 8.93±0.15 | 7.78±0.21 | 6.99±0.17 | 3.68±0.04 |
|  |  |  |  |  |  |

## CE results (F1) per pathology/finding for ChEX, RGRG, and MAIRA-1 on the full report full report generation (RG) task on MIMIC-CXR. Except for ChEX, results are taken from the original papers. Our method ChEX performs best on 5 of the 14 classes, even outperforming the much larger MAIRA-1. On 9 of the 14 classes, it outperforms RGRG, where it is able to describe findings and pathologies like lung lesions or enlarged cardiomediastinum, which RGRG is unable to detect at all.

|  | 29.58±0.24 6.52±0.11 13.26±0.10 19.49±0.10 18.49±0.79 |
| --- | --- | --- | --- | --- | --- | --- |
| RGRG [70] M | 37.3 | 12.6 | 16.8 | 26.4 | 49.5 |
| CvT-212DistilGPT2 [55] M | 39.2 | 12.4 | 15.3 | 28.5 | 36.1 |
| M2 Trans w/ NLL+BS+fCEN [49] M | - |  | 11.4 | - | - | 50.9 |
| METransformer [77] M | 38.6 | 12.4 | 15.2 | 29.1 | 36.2 |
| Med-PaLM M (12B) [72] M O | 30.90 | 10.43 | - | 26.16 | 23.43 |
| Med-PaLM M (84B) [72] M O | 32.31 | 11.31 | - | 27.29 | 26.17 |
| Med-PaLM M (562B) [72] M O | 31.73 | 11.50 | - | 27.49 | 25.27 |
| MAIRA-1 [26] M | 39.2 | 14.2 | 33.3 | 28.9 | - |
| Prompt-MRG [29] M | 39.8 | 11.2 | 15.7 | 26.8 | - |
| OmniFM-DR [83] M O | - |  | 11.0 | 14.0 | 26.5 | - |
| RaDialog-INS [57] M O | 34.0 | 9.7 | 13.6 | 27.0 | - |
| RaDialog-RG [57] M O | 34.6 | 9.5 | 14.0 | 27.1 | - |
| ITA [74] M | 39.5 | 12.1 | 14.7 | 28.4 | - |
| COOMG [15] M | 34.6 | 10.4 | 13.7 | 27.9 | - |
| COOMG-RL [15] M | 36.3 | 12.4 | 12.8 | 29.0 | - |
| ORGAN [21] | 40.7 | 12.3 | 16.2 | 29.3 | - |
| BioViL-T [2] M | - |  | 9.2 | - | 29.6 | - |
|  |  |  |  | F1 |  |
| Pathology/Finding |  |  | ChEX RGRG [70] MAIRA-1 [26] |
| Cardiomegaly | 66.62±1.08 | 62.4 | 64.0 |
| Edema | 54.81±1.48 | 51.4 | 44.0 |
| Consolidation |  | 15.27±2.10 | 7.8 | 20.0 |
| Atelectasis |  | 45.99±1.43 | 54.6 | 41.3 |
| Pleural Effusion | 69.11±1.04 | 56.0 | 68.9 |
| Enlarged Cardiomediastinum | 6.81±1.74 | 0.3 | 11.9 |
| Fracture |  | 0.00±0.00 | 0.0 | 24.9 |
| Lung Lesion |  | 14.24±3.05 | 0.7 | 18.8 |
| Lung Opacity | 52.32±1.06 | 26.8 | 49.8 |
| Pleural Other |  | 0.00±0.00 | 0.2 | 14.7 |
| Pneumonia | 19.30±1.55 | 16.2 | 18.3 |
| Pneumothorax |  | 17.59±3.21 | 15.9 | 40.8 |
| Support Devices |  | 69.40±0.92 | 70.9 | 84.5 |
| No Finding |  | 24.36±2.97 | 63.2 | 38.6 |

## We use the MIMIC Chest X-ray (MIMIC-CXR) Database v2.0.0

| E.1 Benchmark Datasets |
| --- |
| MIMIC-CXR |

### Formule


$$V ✓ ✓ ✓ ✓ ✓ ✓ Pathology classes V ✓ ✓ ✓ ✓ ✓ ✓ Anat. boxes M ✓ ✓ ✓ ✓ ✓ ✓ Anat. patho classes M ✓ ✓ ✓ ✓ ✓ ✓ Anat. sentences M ✓ ✓ ✓ ✓ ✓ ✓ Sentences M ✓ ✓ ✓ ✓ ✓ ✓ Sentence Grounding (SG) MS-CXR M [$$

### Formule


$$Chest ImaGenome M [Mic-F1-14] [Mac-F1-14] [Mic-F1-5+] [Mac-F1-5+] [METEOR] ChEX V M$$

### Formule


$$Full Report Generation (RG) MIMIC-CXR M [BLEU-1] [BLEU-4] [METEOR] [ROUGE-L] [CIDEr] ChEX V M$$

### Formule


$$t ′ k,m = q k + t m .(1)$$

### Formule


$$r k = m s k,m • r k,m m s k,m .(2)$$

### Formule


$$p c,m = exp (r c,m • q + c ) exp r c,m • q + c + exp r c,m • q - c ,(3)$$

### Formule


$$L box b, b = 5 • L 1 b, b + 2 • gIoU b, b ,(4)$$

### Formule


$$L match (c, m, m ′ ) = L box bc,m , b c,m ′ + p c,m + 3 • s c,m .(5)$$

### Formule


$$L patho-detect = L box + 3 • L focal .$$

### Formule


$$L patho-cls = - 1 |C| c log y c • exp(cos(r c , q + c )/τ ) + (1 -y c ) • exp(cos(r c , q - c )/τ ) c ′ exp(cos(r c , q + c ′ )/τ ) + exp(cos(r c , q - c ′ )/τ ) ,(6)$$

### Formule


$$L anat-cls = - 1 |A| a log exp 1 |C| c y a,c • cos(r a , q + c )/τ ) + (1 -y a,c ) • cos(r a , q - c )/τ ) c ′ exp(cos(r a , q + c ′ )/τ ) + exp(cos(r a , q - c ′ )/τ )(7)$$

### Formule


$$L sent-contr = - 1 N i 1 |S (i) | s∈S (i) log exp cos r (i) s , q (i) s /τ j,s ′ exp cos r (i) s , q (j) s ′ /τ , (8$$

### Formule


$$)$$

### Formule


$$L stage1 =10 • L patho-detect + 1 • L patho-cls + 0.1 • L anat-detect + 0.005 • L anat-cls + 0.005 • L sent-contr + 1 • L global-contr(9)$$

### Formule


$$L stage2 =0.01 • L anat-cls + 0.04 • L anat-mse + 0.005 • L sent-contr + 0.02 • L sent-mse(10)$$

### Formule


$$L stage3 =1 • L anat-gen + 0.04 • L anat-mse + 0.5 • L sent-gen + 0.02 • L sent-mse(11)$$
