# Generalist models in medical image segmentation: A survey and performance comparison with task-specific approaches

**Auteurs** : Andrea Moglia, Matteo Leccardi, Matteo Cavicchioli, Alice Maccarini, Marco Marcon, Luca Mainardi, Pietro Cerveri
**Année** : 2025
**DOI** : 10.1016/j.inffus.2025.103709

## Résumé

Following the successful paradigm shift of large language models, leveraging pre-training on a massive corpus of data and fine-tuning on different downstream tasks, generalist models have made their foray into computer vision. The introduction of Segment Anything Model (SAM) set a milestone on segmentation of natural images, inspiring the design of a multitude of architectures for medical image segmentation. In this survey we offer a comprehensive and in-depth investigation on generalist models for medical image segmentation. We start with an introduction on the fundamentals concepts underpinning their development. Then, we provide a taxonomy on the different declinations of SAM in terms of zero-shot, fewshot, fine-tuning, adapters, on the recent SAM 2, on other innovative models trained on images alone, and others trained on both text and images. We thoroughly analyze their performances at the level of both primary research and best-in-literature, followed by a rigorous comparison with the state-of-the-art task-specific models. We emphasize the need to address challenges in terms of compliance with regulatory frameworks, privacy and security laws, budget, and trustworthy artificial intelligence (AI). Finally, we share our perspective on future directions concerning synthetic data, early fusion, lessons learnt from generalist models in natural language processing, agentic AI and physical AI, and clinical translation.

## Méthodologie

{'study_design': 'Revue de la littérature (survey) avec recherche systématique sur PubMed, Web of Science, Scopus, IEEE Xplore, arXiv et Google Scholar, complétée par une vérification récursive des références des revues précédemment publiées et des publications sur les modèles task-specific.', 'intervention': None, 'control': None, 'primary_outcomes': ['Comparaison des performances (ex. Dice score) entre modèles généralistes et modèles task-specific sur des jeux de données par région anatomique'], 'secondary_outcomes': ['Identification des défis réglementaires, de confidentialité, de sécurité, budgétaires et de confiance (trustworthy AI)', 'Directions futures : données synthétiques, fusion précoce, IA agentique, IA physique, traduction clinique'], 'statistical_methods': ['Agrégation et alignement de métriques quantitatives (ex. Dice score) à travers jeux de données, points temporels et versions de modèles', "Cadre d'évaluation statistique pour quantifier les écarts de généralisation ('generalization gaps') entre domaines anatomiques et modalités"], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'Dice score moyen entre WT, ET, TC (tumeur cérébrale, BraTS)', 'value': '91.83%, 75.98%, 87.05% respectivement', 'unit': 'Dice score (%)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Appendix B - Contribution analysis', 'source_quote': 'Average Dice score between WT, ET, TC (91.83%, 75.98%, 87.05% respectively).'}, {'outcome': 'Dice score moyen CHAOS CT et CHAOS MRI', 'value': '97.24% (CT), 87.99% (MRI)', 'unit': 'Dice score (%)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Appendix B - Contribution analysis', 'source_quote': 'Average Dice score between CHAOS CT (97.24%) and CHAOS MRI (87.99%).'}, {'outcome': 'Dice score moyen AMOS2 CT et AMOS2 MRI', 'value': '79.94% (CT), 75.41% (MRI)', 'unit': 'Dice score (%)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Appendix B - Contribution analysis', 'source_quote': 'Average Dice score between AMOS2 CT (79.94%) and AMOS2 MRI (75.41%).'}, {'outcome': 'Dice score moyen organe et tumeur', 'value': '96.89% (organe), 84.01% (tumeur)', 'unit': 'Dice score (%)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Appendix B - Contribution analysis', 'source_quote': 'Average Dice score between organ (96.89%) and tumor (84.01%).'}, {'outcome': "Jeu de données FLARE - nombre total d'images à travers toutes les itérations", 'value': '16450 images totales, dont 7400 annotées', 'unit': "nombre d'images", 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Appendix - Datasets description', 'source_quote': 'The total number of images across all iterations is 16450 (10000 CT from FLARE 2024 Task 1 + 5200 MRI from Task 3, plus 1250 PET scans from the 2025 integration), while the number of annotated images is 7400 (2300 with abdominal organs partial annotations from Task 3 + 5100 pantumor annotations only from Task 1).'}], 'qualitative_findings': ['Winners: Task-specific (on primary research). Tie on best in literature with generalist models obtaining a higher median Dice score on Head and Neck Dataset, while task-specific on ToothFairy dataset.', 'Winners: Generalist models on both primary research and best in literature.', 'Winners: Generalist models on all datasets with the exception of ACDC, and Left Atrial Segmentation (median DSC on both primary research, and best in literature).', 'Winners: Task-specific on both primary work, and best in literature.', 'Winner: Foundation models on primary work; foundation models on best in literature on all datasets except ATLAS2023.', 'Winners: Tie with foundation models on eight datasets on primary works, while task specific on seven datasets on best in the literature.'], 'main_findings': ["Le dichotomie fondamentale en segmentation d'images médicales contemporaine se situe entre modèles généralistes et modèles task-specific plutôt qu'entre transformers et CNN", "Les modèles généralistes, pré-entraînés sur des millions d'images médicales multi-modales, montrent une adaptabilité remarquable et des performances constantes à travers diverses régions anatomiques", "Les résultats de performance varient selon la région anatomique : les modèles task-specific dominent sur certains jeux de données (ex. ACDC, Left Atrial Segmentation), tandis que les modèles généralistes/foundation dominent sur d'autres", "Aucune revue publiée précédemment n'avait répondu de façon exhaustive aux questions sur les écarts de performance, le meilleur modèle par organe, l'évolution temporelle des performances, les défis et les directions futures"]}

## Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison with Task-Specific Approaches

| Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison |
| --- | --- |
| with Task-Specific Approaches | A Preprint |
| Section 2: |  |
| Context |  |
| and our |  |
| contri- |  |
| butions |  |
| Generalist |  |
| Models for |  |
| Medical Image |  |
| Segmentation |  |

## SAM for medical annotation Other SAM implementations Zero-shot of SAM 2 Fine-tuning of SAM 2 Other applications of SAM 2 Other modes trained only on images Other models trained on both images and text

| Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison |
| --- | --- | --- | --- | --- |
|  |  |  | with Task-Specific Approaches | A Preprint |
|  |  |  |  | Shen |
|  |  |  |  | Yamagishi |
|  |  | Mazurowski Huang | Zero-shot of SAM | Dong Sengupta |
|  | SAM-MPA, Xu | Few-shot of SAM | MedSAM2, Ma |
|  |  |  |  | Biomedical SAM 2, Yan |
| SAM-Med2D, Cheng MedSAM, Ma | Full fine-tuning of SAM |
|  |  |  |  | Ma |
| SAMed, Zhang |  |  | Medical SAM 2, Zhu |
| FLAP-SAM, Asokan | PEFT of SAM |
| Cheap Lunch SAM, Feng |  |  | UniMiSS, Xie |
|  |  |  |  | Med3D, Chen |
| DeSAM, Gao SAM-Med3D, Wang SAM3D, Bui | Modifications to SAM architecture | Taxonomy | MoME, Zhang SMIT, Jiang Hermes, Gao MIS-FM, Wang |
| 3DMedSAM, Lin |  |  |  | IMIS-Net, Cheng |
| Med-SA, Wu |  |  |  | UniverSeg, Butoi |
| MA-SAM, Chen |  |  |  | STU-Net, Huang |
| LeSAM, Gu |  |  |  | MultiTalent, Ulrich |
| 3DSAM-adapter, Gong TP Mamba, Wang | Adapters for SAM |  | UniSeg, Ye UniSeg33A, Liu |
| EMedSAM, Dong |  |  |  | BrainSegFounder, Cox |
| SPA, Hu |  |  |  | One-Prompt, Wu |
| M-SAM, Shi | SAMM, Liu |  | DoDNet, Zhang DeSD, Ye |
| SAMMed, Wang |  | Disruptive Autoencoders, Valanarasu |
|  |  |  |  | BiomedParse, Zhao |
|  | KnowSAM, Huang SFR SAM, Li MedLSAM, Lei |  | CLIP-Driven Universal Model, Liu Merlin, Blankemeier SAT, Zhao SegVol, Du |
|  |  |  |  | PCNet, Chen |

## Reviewed generalist models for 3D medical image segmentation.

| A Preprint |
| --- |

## Table 2, and Table 6 in the appendix).The number of datasets may vary from the primary to the best-in-literature works since some models, e.g., nnU-Net, and SwinUNETR, were re-implemented from different research groups over time.

| Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison |
| --- |
| with Task-Specific Approaches |
| It is worth noting that the best performance was obtained by different strategies, e.g., retraining, |
| different pre-training, or fine-tuning depending on the model as well as by direct re-implementation |
| by part of a different research group. |

## Highest Dice score achieved by generalist models expressed as percentage [%].Table cells with reference represent either a model tested on a dataset, not used in the primary publication, or an improvement over the primary work. Table cells with percentage increment in green refer to the improvement of Dice score w.r.t. to the primary publication. Best result considering models in this table are formatted as first, second-best and third-best. From Table I and II of Shen et al. (2025) using the 5 clicks prompt configuration. c Average Dice score between BraTS WT, ET, TC (91.58%, 74.84%, 86.22%). d Average Dice score between BraTS WT, ET, TC (91.58%, 74.84%, 86.22%).

| Model |  | First Publ. | BTCV | BraTS | KiTS | LiTS / MSD Liver | MSD Pancreas Tumour | MSD Lung Tumors | Synapse | AMOS | ACDC | PROMISE12 | MSD Colon Cancer | FLARE | TotalSegmentator | MSD Spleen | SegTHOR | MSD Hepatic Vessels | MSD Prostate | TotalSegmentator Organs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MedSAM2 |  | 2025-04 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SPA |  | 2025-01 |  |  |  |  |  |  | 92.88 |  |  | 94.29 |  |  |  |  |  |  |  |
| 3DMedSAM 2024-12 88.60 |  |  | 60.45 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| KnowSAM |  | 2024-12 |  |  |  |  |  |  |  |  | 91.13 |  |  |  |  |  |  |  |  |
| IMIS-Net |  | 2024-11 |  |  |  |  |  |  |  |  |  |  |  |  | 79.06 |  | 89.27 |  |  |
| SAM-MPA |  | 2024-10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TP-Mamba 2024-09 84.80 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EMedSAM |  | 2024-08 |  | 89.30 |  |  |  |  |  |  |  |  |  | 0.88 (a) |  |  |  |  |  |
| Biomedical | 2024-08 |  |  |  |  |  |  |  | 74.39 |  |  |  | 76.32 |  |  |  |  |  |
| SAM-2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (BioSAM-2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SAM 2 |  | 2024-08 | 86.00 Zhu et al. (2024) | 75.52 Shen et al. (2025) (b) | 64.60 Zhu et al. (2024) | 81.32 Shen et al. (2025) (b) | 44.73 Shen et al. (2025) (b) | 71.61 Shen et al. (2025) (b) |  | 54.92 Yan et al. (2024a) |  |  |  | 47.44 Yan et al. (2024a) | 77.62 Cheng et al. (2024) | 79.59 Shen et al. (2025) (b) | 85.86 Cheng et al. (2024) |  |  |
|  |  |  |  | 28.91 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Medical SAM 2 (MedSAM- | 2024-08 89.00 | (a) Li et al. (2025) | 78.20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FLAP-SAM 2024-07 |  |  | 60.46 |  |  |  |  |  |  | 88.67 |  |  |  |  |  |  |  |
| LeSAM |  | 2024-06 |  | 84.95 | 91.86 | 70.62 | 79.42 | 79.57 |  |  |  |  | 77.18 |  |  |  |  | 79.59 |  |
| Merlin |  | 2024-06 |  |  |  |  |  |  |  |  |  |  |  |  | 86.00 |  |  |  |  |
| BrainSegFounder 2024-06 |  | 91.15 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| MoME |  | 2024-05 |  | 88.86 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BiomedParse 2024-05 |  | 79.95 | 80.22 | 83.39 | 50.62 | 66.09 |  | 86.33 | 92.26 | 89.97 | 66.51 |  |  | 96.86 |  | 66.03 | 72.85 |
| PCNet |  | 2024-04 83.85 |  | 86.19 | 96.63 | 79.70 |  |  |  |  |  |  | 90.62 | 91.64 | 95.77 | 87.66 |  |  | 91.09 |
| MEA | M- | 2024-03 |  | 92.08 | 93.50 | 89.95 | 80.49 | 81.62 |  |  |  |  |  |  |  |  |  |  |  |
| SAM |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SFR SAM |  | 2024-03 77.07 | 86.09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | continues → |

## Dice score achieved by task-specific models in their first publication expressed as percentage[%]. Best result considering models in this table are formatted as first, second-best and third-best.

| Model | First Publ. | BTCV | BraTS | KiTS | LiTS / MSD Liver | MSD Pancreas Tumour | MSD Lung Tumors | Synapse | AMOS | ACDC | PROMISE12 | MSD Colon Cancer | FLARE | TotalSegmentator | MSD Spleen | SegTHOR | MSD Hepatic Vessels | MSD Prostate | TotalSegmentator Organs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LHU-Net | 2024-04 |  | 86.05 |  |  |  |  | 87.49 |  | 92.66 |  |  |  |  |  |  |  |  |  |
| SCANeXt | 2024-03 |  | 86.60 |  |  |  |  | 89.67 |  | 95.18 |  |  |  |  |  |  |  |  |  |
| SwinUNETR- | 2023-10 |  |  |  |  | 64.03 | 62.03 |  |  |  |  |  | 94.70 |  |  |  |  | 74.05 |  |
| V2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| NexToU | 2023-05 87.84 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| MedNeXt | 2023-03 88.76 | 88.01 | 91.02 |  |  |  |  | 91.77 |  |  |  |  |  |  |  |  |  |  |
| UNETR++ 2022-12 83.28 | 82.75 |  |  |  | 80.68 | 87.22 |  | 92.83 |  |  |  |  |  |  |  |  |  |
| 3D UX-Net 2022-08 |  |  |  |  |  |  |  | 90.00 |  |  |  | 93.40 |  |  |  |  |  |  |
| MedFormer 2022-02 85.00 |  | 85.00 | 69.00 |  | 74.00 |  | 88.00 | 92.50 |  |  |  |  |  |  |  |  |  |
| TransBTSV2 2022-01 |  | 85.04 (a) | 90.53 | 89.85 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SwinUNETR | 2022-01 83.48 | 88.96 |  |  | 55.49 | 56.72 |  |  |  |  |  | 92.90 |  |  |  |  | 73.32 |  |
| (b) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| nnFormer | 2021-09 |  | 86.40 |  |  |  |  | 86.57 |  | 92.06 |  |  |  |  |  |  |  |  |  |
| MISSFormer 2021-09 |  |  |  |  |  |  | 81.96 |  | 91.19 |  |  |  |  |  |  |  |  |  |
| Swin-Unet | 2021-05 |  |  |  |  |  |  | 79.13 |  | 90.00 |  |  |  |  |  |  |  |  |  |
| TransBTS (c) | 2021-03 |  | 83.57 | 89.10 | 88.95 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CoTr | 2021-03 85.00 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| UNETR | 2021-03 | 87.35 (d) | 71.10 |  |  |  |  |  |  |  |  |  |  |  | 96.40 |  |  |  |  |
| TransUNet | 2021-02 |  | 91.74 |  |  |  |  | 88.39 |  |  |  |  |  |  |  |  | 67.67 |  |  |
| SETR (e) | 2020-12 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SegResNet | 2018-10 |  | 82.19 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| nnU-Net | 2018-10 87.62 | 61.00 | 91.63 | 86.50 | 67.50 | 74.00 |  |  | 92.95 | 91.94 | 58.00 |  |  | 97.00 | 93.00 | 69.00 | 83.50 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | continues → |

## Dice score achieved by generalist models in their first publication expressed as percentage [%]. Best result considering models in this table are formatted as first, second-best and third-best.

| Model |  | First Publ. | BTCV | BraTS | KiTS | LiTS / MSD Liver | MSD Pancreas Tumour | MSD Lung Tumors | Synapse | AMOS | ACDC | PROMISE12 | MSD Colon Cancer | FLARE | TotalSegmentator | MSD Spleen | SegTHOR | MSD Hepatic Vessels | MSD Prostate | TotalSegmentator Organs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MedSAM2 (a) | 2025-04 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SPA |  | 2025-01 |  |  |  |  |  |  | 92.88 |  |  | 94.29 |  |  |  |  |  |  |  |
| 3DMedSAM 2024-12 88.60 |  |  | 60.45 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| KnowSAM |  | 2024-12 |  |  |  |  |  |  |  |  | 91.13 |  |  |  |  |  |  |  |  |
| IMIS-Net |  | 2024-11 |  |  |  |  |  |  |  |  |  |  |  |  | 79.06 (b) |  | 89.27 |  |  |
| SAM-MPA (c) | 2024-10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TP-Mamba 2024-09 84.80 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EMedSAM |  | 2024-08 |  | 89.30 |  |  |  |  |  |  |  |  |  | 0.88 |  |  |  |  |  |
| SAM 2 |  | 2024-08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Medical SAM | 2024-08 89.00 |  | 78.20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 (MedSAM- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Biomedical SAM-2 | 2024-08 |  |  |  |  |  |  |  | 74.39 (d) |  |  |  | 76.32 (e) |  |  |  |  |  |
| (BioSAM-2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FLAP-SAM 2024-07 |  |  | 60.46 |  |  |  |  |  |  | 88.67 |  |  |  |  |  |  |  |
| LeSAM |  | 2024-06 |  | 84.95 (f) | 91.86 | 70.62 | 79.42 | 79.57 |  |  |  |  | 77.18 |  |  |  |  | 79.59 |  |
| Merlin |  | 2024-06 |  |  |  |  |  |  |  |  |  |  |  |  | 86.00 |  |  |  |  |
| BrainSegFounder 2024-06 |  | 91.15 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| MoME (g) |  | 2024-05 |  | 88.86 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BiomedParse | 2024-05 |  | 79.95 | 80.22 | 83.39 | 50.62 | 66.09 |  | 86.33 | 92.26 | 89.97 | 66.51 |  |  | 96.86 |  | 66.03 | 72.85 |
| (h) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PCNet (i) |  | 2024-04 83.85 |  | 86.19 | 96.63 | 79.70 |  |  |  |  |  |  | 90.62 | 91.64 | 95.77 | 87.66 |  |  | 91.09 |
| MEA | M- | 2024-03 |  | 92.08 | 93.50 | 89.95 | 80.49 | 81.62 |  |  |  |  |  |  |  |  |  |  |  |
| SAM |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SFR SAM |  | 2024-03 77.07 | 86.09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Med-SA (j) |  | 2023-12 88.30 | 89.10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | continues → |

## Highest Dice score achieved by task-specific models expressed as percentage [%].Table cells with reference represent either a model tested on a dataset, not used in the primary publication, or an improvement over the primary work. Table cells with percentage increment in green refer to the improvement of Dice score w.r.t. to the primary publication. Best result considering models in this table are formatted as first, second-best and third-best. Datasets Table 7 reports information, links and resources about 3D medical image datasets used to benchmark foundation and specialized models.

| Model | First Publ. | BTCV | BraTS | KiTS | LiTS / MSD Liver | MSD Pancreas Tumour | MSD Lung Tumors | Synapse | AMOS | ACDC | PROMISE12 | MSD Colon Cancer | FLARE | TotalSegmentator | MSD Spleen | SegTHOR | MSD Hepatic Vessels | MSD Prostate | TotalSegmentator Organs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Full list of the datasets used in the reviewed studies. -01 database consists of 3D CT scans from 10 female and 10 male patients with a liver tumor incidence rate of 75%. Not all classes are reported in all images or in equal proportion in the dataset, with the majority of classes pesent in just a few images.

| Dataset Full Name (References) | Related Datasets | Modality | Main Anatomical Structure (Region) | N. Objects Objects | N. Images (with labels) | Links |
| --- | --- | --- | --- | --- | --- | --- |
| 3D-IRCADb | - | 3D CT | Liver, Tumors | 35 | 22 | Official Website |
| Liver segmentation |  |  | (Abdomen) | Aorta, Artery, Biliary System, Bladder, Bone, | (22) | Download |
| 3D-IRCADb-01 |  |  |  | Colon, Duodenum, Gallbladder, Heart, |  | Publication |
| (Soler et al., 2010) |  |  |  | Hyperplasie, Inferior Vena Cava, Kidney (Left), |  |  |
|  |  |  |  | Kidney (Right), Kidneys, Liver, Liver Cyst, |  |  |
|  |  |  |  | Liver Tumor, Lung (Left), Lung (Right), Lungs, |  |  |
|  |  |  |  | Lymph Nodes, Metal, Metastasectomy, |  |  |
|  |  |  |  | Pancreas, Portal Vein and Splenic Vein, Skin, |  |  |
|  |  |  |  | Spleen, Stomach, Stones, Surrenal Gland, |  |  |
|  |  |  |  | Surrenal Gland (Left), Surrenal Gland (Left) |  |  |
|  |  |  |  | Tumor, Surrenal Gland (Right) Tumor, Tumor, |  |  |
|  |  |  |  | Venous System |  |  |
| The 3D-ircadb AbdomenAtlas | - | 3D CT / CT (CE) Abdominal Organs, | 25 | 3410 |  |
| AbdomenAtlas |  |  | Bones | Adrenal Gland (Left), Adrenal Gland (Right), |  |  |
| (Li et al., 2024) |  |  | (Abdomen, Pelvis, Thorax) | Aorta, Bladder, Celiac Trunk, Colon, Duodenum, Esophagus, Femur (Left), Femur |  |  |
|  |  |  |  | (Right), Gallbladder, Hepatic Vessels, Inferior |  |  |
|  |  |  |  | Vena Cava, Kidney (Left), Kidney (Right), |  |  |
|  |  |  |  | Liver, Lung (Left), Lung (Right), Pancreas, |  |  |
|  |  |  |  | Portal and Spleenic Veins, Prostate, Rectum, |  |  |
|  |  |  |  | Small Intestine, Spleen, Stomach |  |  |

## provides whole-body PET/CT volumes with manual tumor lesion annotations and comprises FDG-PET/CT images (1,014 cases from 900 patients) collected primarily from the University Hospital Tbingen and LMU in Munich, and PSMA-PET/CT images (597 cases from 378 patients) from the same institutions. The complete dataset (also referred to as AutoPET III) is an extension of the original AutoPET, which was expanded mutiple times from its first release(Autopet I, II and III in 2022, 2023 and 2024  MICCAI challenges respectively)

|  |  |  |  |  |  | A Preprint |
| --- | --- | --- | --- | --- | --- | --- |
| → continued |  |  |  |  |  |  |
| Dataset Full Name (References) | Related Datasets | Modality | Main Anatomical Structure (Region) | N. Objects Objects | N. Images (with labels) | Links |
| AutoPET | AutoPET I, | 3D CT, | Tumors | 1 | 1816 | Official Challenge Website |
| Automated Lesion | AutoPET II, | 3D PET (FDG), | (Whole Body) | Tumor | (1616) | (1) |
| Segmentation in Whole-Body | AutoPET III | 3D PET (PSMA) |  |  |  | Official Challenge Website |
| PET/CT |  |  |  |  |  | (2) |
| (Gatidis et al., 2022) |  |  |  |  |  | Official Challenge Website |
|  |  |  |  |  |  | (3) |
|  |  |  |  |  |  | Publication |
| The AutoPET dataset BraTS | BraTS 2012, BraTS | 3D MRI (T1), | Brain, Tumors | 10 | 7189 | BraTS Datasets |
| Brain Tumor Segmentation | 2013, BraTS 2014, | 3D MRI (T1-CE), | (Head) | Brain Enhancing Tumor, Brain Gross Tumor | (6457) | Comprehensive Review |
| (Menze et al., 2015; Bakas et al., 2024; Bonato et al., 2025) | BraTS 2015, BraTS 2019, BraTS 2020, 2016, BraTS 2017, BraTS 2018, BraTS | 3D MRI (T2), 3D MRI (T2-FLAIR) |  | Volume, Brain Metastasis, Brain Non-enhancing Non-enhancing FLAIR Superintensity, Brain Resection Cavity, Brain Surrounding Tumor Core, Brain Peritumoral Edema, Brain |  | BraTS 2024 Website BraTS 2025 Website |
|  | BraTS 2021, BraTS |  |  | Tumor Cystic Component, Glioma, Meningioma |  |  |
|  | 2022, BraTS 2023, |  |  |  |  |  |
|  | BraTS 2024 |  |  |  |  |  |

## CT segmentation dataset for cervical cancer patients, primarily used for radiation therapy planning. The name BTCV comes from the Workshop "Multi-Atlas Labeling Beyond The Cranial Vault" held at MICCAI 2015, and is also synonim of the BTCV dataset.

| Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | with Task-Specific Approaches |  | A Preprint |
| → continued |  |  |  |  |  |  |
| Dataset Full Name (References) | Related Datasets | Modality | Main Anatomical Structure (Region) | N. Objects Objects | N. Images (with labels) | Links |
| CANDI | - | 3D MRI (T1) | Brain | 39 | 263 | Official Website |
| The Child and Adolescent |  |  | (Head) | Brain 3rd Ventricle, Brain 4th Ventricle, Brain | (263) |  |
| NeuroDevelopment Initiative |  |  |  | 5th Ventricle, Brain CSF, Brain Left Inferior |  |  |
| (Kennedy et al., 2012) |  |  |  | Lateral Ventricle, Brain Left Lateral Ventricle, |  |  |
|  |  |  |  | Brain Left Undetermined, Brain Left Vessel, |  |  |
|  |  |  |  | Brain Right Inferior Lateral Ventricle, Brain |  |  |
|  |  |  |  | Right Lateral Ventricle, Brain Right |  |  |
|  |  |  |  | Undetermined, Brain Right Vessel, Brain Stem, |  |  |
|  |  |  |  | Cerebral Cortex (Left), Cerebral Cortex (Right), |  |  |
|  |  |  |  | Hippocampus (Left), Hippocampus (Right), |  |  |
|  |  |  |  | Left Accumbens Area, Left Amygdala, Left |  |  |
|  |  |  |  | Caudate, Left Cerebellum Cortex, Left |  |  |
|  |  |  |  | Cerebellum White Matter, Left Cerebral White |  |  |
|  |  |  |  | Matter, Left Pallidum, Left Putamen, Left |  |  |
|  |  |  |  | Thalamus Proper, Left Ventral Diencephalon, |  |  |
|  |  |  |  | Optic Chiasm, Right Accumbens Area, Right |  |  |
|  |  |  |  | Amygdala, Right Caudate, Right Cerebellum |  |  |
|  |  |  |  | Cortex, Right Cerebellum White Matter, Right |  |  |
|  |  |  |  | Cerebral White Matter, Right Pallidum, Right |  |  |
|  |  |  |  | Putamen, Right Thalamus Proper, Right |  |  |
|  |  |  |  | Ventral Diencephalon, White Matter |  |  |
|  |  |  |  | Hypointensities |  |  |
|  | - | 3D CT (CE) | Abdominal Organs | 4 | 50 | Official Website |
| -Atlas Labeling Beyond |  |  | (Pelvis) | Bladder, Brain Enhancing Tumor, Small | (30) |  |
| The Cranial Vault -Cervix |  |  |  | Intestine, Uterus |  |  |
| (Landman et al., 2015) |  |  |  |  |  |  |
| The BTCV Cervix dataset is a continues → |

## dataset of multimodal MRI images to automatically segment acute to subacute ischemic stroke lesions, multiple emboli and cortical infarcts, and is associated with the ISLES 2022 MICCAI challenge. The dataset is divided into a training set of 250 cases and a test set of 150 cases which is used solely for model validation and is not disclosed (not image nor segmentation mask). The ISLES challenge has been held since 2015 hosting several editions, and has grown over time both in scale and in the lesion types included (the 2015 challenge only included ischemic stroke lesions). The ATLAS v2.0 dataset is related to the MICCAI ISLES 2022 Challenge Task 2, bus is disjoint from the ISLES dataset. dataset associated with the MICCAI KiPA 2022 challenge aimed at segmenting 3D kidneys, kidney tumors, arteries, and veins. The dataset includes 130 cases of CT scans with complete annotations. The data is officially divided into 70 cases for the training dataset, 30 cases for the open testing dataset (hidden labels), and 30 cases for the closed testing dataset (hidden image and labels). The dataset includes abnormal kidney samples and the annotation of fine renal vascular structures.The KiTS dataset is a collection of CT scans used for challenges in medical image segmentation, specifically focusing on kidneys and their associated pathologies. The first iteration, KiTS19, released for MICCAI 2019, focused solely on segmenting kidneys and tumors, comprising 210 training and 90 test cases. These 90 test cases were later integrated into the training sets of subsequent challenges. KiTS21, presented at MICCAI 2021, expanded upon KiTS19 by adding the segmentation of cysts to the task. It included 300 publicly available training cases, which incorporated all the data from KiTS19, along with 100 new, non-public testing cases. The most recent iteration, KiTS23, featured at MICCAI 2023, continued to build on its predecessors by encompassing 599 cases (489 for training and 110 for testing). The training set includes all previous KiTS data. A key enhancement in KiTS23 is the inclusion of cases from the "nephrogenic contrast phase" in addition to the "late arterial" phase, and its 110 testing cases are entirely new to the challenge. LASC) datasets focus on the segmentation of the left atrium from medical images, essential for guiding atrial fibrillation treatments and cardiac modeling. The LASC 2013 dataset, used at MICCAI 2013 (STACOM 2013), provided 30 MRI and 30 CT scans. For each modality, 10 datasets were for training with expert segmentations, and 20 for evaluation. The task focused on segmenting the LA, including parts of the LA appendage and proximal pulmonary veins. The Left Atrium 2018 dataset, used at MICCAI 2018, also involved the segmentation of the LA cavity from 154 (100 with labels) Gadolinium-Enhanced MRI (GE-MRI), crucial for understanding atrial fibrosis despite low image contrast. Here are reported the condensed startistics of the two dataset iterations, considering reuse of the MRI scans. LASC18 is part of the Cardiac Atlas Project. is a multi-center CT imaging dataset compiled from 7 distinct medical institutions. The dataset features diverse primary and secondary tumors with varied sizes, appearances, and lesion-to-background contrast levels. It was the basis for related competitions held at ISBI 2017, MICCAI 2017, and MICCAI 2018, and is included integrally as the Liver Tumor task in the Medical Segmentation Decathlon (MSD).

| Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | with Task-Specific Approaches |  | A Preprint A Preprint |
| → continued → continued |  |  |  |  |  |  |
| Dataset Full Name (References) Dataset Full Name (References) | Related Datasets Related Datasets | Modality Modality | Main Anatomical Structure (Region) Main Anatomical Structure (Region) | N. Objects Objects N. Objects Objects | N. Images (with labels) N. Images (with labels) | Links Links |
| ISLES LIDC-IDRI | ATLAS v2.0 - | 3D MRI (DWI), 3D CT (LD) | Brain Lung | 1 1 | 250 1308 | Official Website Official Website |
| Ischemic Stroke LEsion The Lung Image Database |  | 3D MRI | (Head) (Thorax) | Brain Ischemic Stroke Lesion Lung Nodule | (250) (1308) | Official Challenge Website Publication |
| Segmentation Consortium and Image |  | (T2-FLAIR) |  |  |  | Publication |
| (Hernandez Petzsche et al., Database Resource Initiative |  |  |  |  |  |  |
| 2022) (Armato III et al., 2011) |  |  |  |  |  |  |
| The LIDC-IDRI dataset comprises clinical thoracic CT scans from 1,010 patients. It contains 7,371 lesions identified as "nodule" by experienced thoracic radiologists. Nodule annotations include segmentation masks and characterization data. LiTS / MSD Liver The Liver Tumor Segmentation MSD Liver 3D CT Liver, Tumors (Abdomen) 2 Liver, Liver Tumor 201 (131) Official Challenge Website MSD Website ISLES is a KiPA Kidney Parsing -3D CT (CE) Kidneys, Tumors Kidney Tumor, Kidneys, Renal Artery, Renal (70) Publication (Bilic et al., 2023) (Abdomen) 4 100 Official Challenge Website Benchmark Publication |
| (He et al., 2021) |  |  |  | Vein |  |  |
| Lung Nodule Analysis 2016 KiPA is the KiTS The LiTS dataset LUNA16 | KiTS19, KiTS21, LIDC-IDRI | 3D CT / CT (CE) Kidneys (Thorax) 3D CT (LD) Lung | 3 Lung Nodule, Lungs 2 | 599 888 | Official Website |
| Kidney Tumor Segmentation (Setio et al., 2017) | KiTS23 |  | (Abdomen) | Kidney Cyst, Kidney Tumor, Kidneys | (489) | KiTS19 Results |
| (Heller et al., 2021) |  |  |  |  |  | Publication |
|  |  |  |  |  |  | KiTS19 Challenge Data |
|  |  |  |  |  |  | Preprint |
|  |  |  |  |  |  | KiTS21 Challenge Data |
|  |  |  |  |  |  | Preprint |
| LASC | LASC13, LASC18 | 3D CT (CE), | Heart | 1 | 184 | LASC13 Kaggle Challenge |
| Left Atrial Segmentation |  | 3D MRI (T1-CE) | (Thorax) | Heart Atrium (Left) | (110) | LASC13 Preprint |
| Challenge |  |  |  |  |  | LASC13 Publication |
| (Tobon-Gomez et al., 2014; |  |  |  |  |  | LASC18 Official Website |
| Xiong et al., 2021) |  |  |  |  |  | LASC18 IEEE Dataport |
|  |  |  |  |  |  | LASC18 Publication |
|  |  |  |  |  |  | The Cardiac Atlas Project |
| The Left Atrial Segmentation Challenge (continues → |

## (part of MICCAI 2020)  dataset is a collection of 375 images from diverse clinical centers across Spain, Germany, and Canada. It encompasses both healthy individuals and patients with various cardiac pathologies, acquired using MRI scanners from Siemens, General Electric, Philips, and Canon. Expert clinicians have meticulously segmented the left ventricle, right ventricle, and left ventricular myocardium in the images following the same standard as in the ACDC dataset. In the original challenge, training images were 175, of which 25 provided without annotations. The remaining 200 images were used for testing. WHS dataset, introduced at MICCAI 2017, is is aimed at entire heart and its key substructures segmentation from various clinical imaging conditions. It comprises a total of 120 cardiac images, evenly split between 60 CT/CTA and 60 MRI scans. The dataset is divided into a training set (20 CT and 20 MRI scans) and a test set (40 CT and 40 MRI scans). The training set includes manual annotations for seven major cardiac substructures: the left and right ventricular cavities, left and right atrial cavities, left ventricular myocardium, ascending aorta, and pulmonary artery. was created byZhang et al. (2021)  for training and pre-training the DoDNet segmentation model. The dataset is an ensemble of seven publicly-available datasets, specifically from the KiTS dataset and the MSD collection of dataset involving only abdominal organs. Some images are specifically identified as test images. Dataset under direct request. MSD Task10) dataset is a sub-task of the Medical Segmentation Decathlon, focusing on colon tumor segmentation from CT images. It comprises venous phase CT scans from 190 patients undergoing surgery for primary colon cancer.

| Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | with Task-Specific Approaches |  | A Preprint |
| → continued |  |  |  |  |  |  |
| Dataset Full Name (References) | Related Datasets | Modality | Main Anatomical Structure (Region) | N. Objects Objects | N. Images (with labels) | Links |
| MOTS | KiTS, LiTS / MSD | 3D CT / CT (CE) Abdominal Organs, | 11 | 1155 | Official Website |
| Multi-Organ and Tumor | Liver, MSD Colon, |  | Tumors | Colon Tumor, Hepatic Vessels, Kidney Cyst, | (920) |  |
| Segmentation | MSD Hepatic |  | (Abdomen) | Kidney Tumor, Kidneys, Liver, Liver Tumor, |  |  |
| (Zhang et al., 2021) | Vessels, MSD Lung, MSD Pancreas, MSD |  |  | Lung Nodule, Pancreas, Pancreas Tumor, Spleen |  |  |
|  | Spleen |  |  |  |  |  |
| The MOTS dataset MSD Cardiac | - | 3D MRI (T1-CE) Heart | 1 | 30 | MSD Website |
| Medical Segmentation |  |  | (Thorax) | Heart Atrium (Left) | (20) | Publication |
| Decathlon -Cardiac |  |  |  |  |  | Preprint |
| (Simpson et al., 2019; Antonelli |  |  |  |  |  |  |
| et al., 2022) |  |  |  |  |  |  |
| The MSD Cardiac (MSD Task02) dataset, also known as MSD Heart, is a sub-task of the Medical Segmentation Decathlon, focusing on left atrium segmentation from single-modality |
| MRI images. |  |  |  |  |  |  |
| MSD Colon Cancer | - | 3D CT | Colon, Tumors | 1 | 190 | MSD Website |
| Medical Segmentation |  |  | (Abdomen) | Colon Tumor | (126) | Publication |
| Decathlon -Colon Cancer |  |  |  |  |  | Preprint |
| (Simpson et al., 2019; Antonelli |  |  |  |  |  |  |
| et al., 2022) |  |  |  |  |  |  |
| The MSD Colon Cancer (MSD Hepatic Vessels | - | 3D CT (CE) | Liver, Tumors | 2 | 443 | MSD Website |
| -Centre, Multi-Vendor & Multi-Disease Cardiac Image Segmentation Challenge et al., 2022) Medical Segmentation (Simpson et al., 2019; Antonelli Decathlon -Hepatic Vessels | - | 3D MRI (T1-CE) Heart (Thorax) (Abdomen) | 3 Heart Ventricle (Left), Heart Ventricle (Right), Myocardium Hepatic Vessels, Liver Tumor | 375 (150) (303) | Publication Official Website Publication Preprint |
| (Campello et al., 2021) |  |  |  |  |  |  |
| The M&Ms Challenge MM-WHS | - | 3D CT / CT | Heart | 7 | 120 | Official Website |
| Multi-Modality Whole Heart |  | (CE), | (Thorax) | Aorta, Heart Atrium (Left), Heart Atrium | (40) |  |
| Segmentation |  | 3D MRI (T1-CE) |  | (Right), Heart Ventricle (Left), Heart Ventricle |  |  |
| - |  |  |  | (Right), Myocardium (Left Ventricle), |  |  |
|  |  |  |  | Pulmonary Artery |  |  |
| The MM-continues → |

## MSD Task04) dataset is a sub-task of the Medical Segmentation Decathlon, focusing on the segmentation of the hippocampal region from single-modality MRI. This dataset contains segmentations of the two distinct anterior and posterior parts of the hippocampus. The dataset officially comprises 394 images, with 263 intended for training and 131 for testing. However, the downloadable training set contains 260 cases, and the test set contains 130 cases. Test results can be submitted to the official MSD website for evaluation. MSD Task06) dataset is a sub-task of the Medical Segmentation Decathlon, focusing on lung tumor segmentation from thin-section CT images. It includes CT scans of 96 patients with non-small cell lung cancer (NSCLC), officially divided into 64 cases for training and 32 for testing. However, 63 cases can be downloaded for the training set. MSD Task07) dataset is a sub-task of the Medical Segmentation Decathlon, focusing on segmenting both the pancreas and its tumors from CT images. It's considered one of the two most challenging tasks in MSD, alongside the Colon Cancer task. The dataset specifically includes three types of pancreatic tumors: intraductal papillary mucinous neoplasms, pancreatic neuroendocrine tumors, and pancreatic ductal adenocarcinomas. MSD Task05) dataset is a sub-task of the Medical Segmentation Decathlon, focusing on segmenting two distinct prostate regions: the central gland and the peripheral zone. This dataset utilizes multi-parametric MR images (T2-weighted and ADC). MICCAI 2008 challenge, is an MRI-based dataset focused on fully automated 3D segmentation of Multiple Sclerosis (MS) lesions. The data was provided by Boston Children's Hospital and the University of North Carolina (UNC) using a Siemens 3T Allegra MRI scanner. Series of Imaging Studies (OASIS) project aims to provide freely available neuroimaging datasets to the scientific community. The series includes four main datasets: OASIS-1 (cross-sectional MRI data for aging and Alzheimer's), OASIS-2 (longitudinal MRI data for aging and Alzheimer's), OASIS-3 (extensive longitudinal multimodal data for aging and Alzheimers Disease), OASIS-3 Tau (OASIS-3 Flortaucipir F18 (AV1451) PET) and OASIS-4 (MR and clinical data for individuals with memory complaints). The OASIS-1 dataset is a cross-sectional collection of MRI scans from 416 subjects aged 18 to 96. Each subject has 3 or 4 individual MRI scans from single sessions. Notably, 100 subjects over 60 years old have been clinically diagnosed with very mild to moderate Alzheimer's disease. A separate reliability dataset includes 20 non-demented subjects rescanned within 90 days. The dataset consists of 35 label classes which are brain portions, sections, and sub-organs. CT dataset comprises 80 images, specifically focusing on manual annotations of the pancreas. Provided by the National Institutes of Health Clinical Center, this dataset explicitly excludes pancreatic tumors, featuring 17 healthy kidney donors and 63 patients without major abdominal diseases or pancreatic cancer. The scans, acquired in the portal venous phase using Philips and Siemens scanners, have undergone meticulous manual segmentation of the pancreas. Originally 82 cases, the latest Version 2 has removed two redundant cases (25 and 70). This dataset is incorporated into larger public datasets like AbdomenCT-1K and AbdomenAtlas. stems from two MICCAI challengges aimed at Intervertebral Disc (IVD) analysis from MRI scans, crucial for understanding low back pain. The MICCAI 2015 challenge (Automatic 3D MRI IVD Localization and Segmentation) used 25 T2-weighted MRI cases. The later MICCAI 2018 (IVDM3Seg) challenge evolved to include 16 multi-modality MR cases (Dixon protocol), aiming for more robust algorithms in varied clinical settings. Each multi-modality MRI patient scans set contains four aligned volumes: in-phase, opposed-phase, fat and water images. In total there are 96 high resolution 3D MRI volume data. One mask volume is present for each patient. Here we report the combined statistics of the two datasets created by the same research group. Overall, SpineWeb was initiative from a canadian medical imaging research group, however the related websites have been shut down, and few indications remain of the original challenge.

| Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | with Task-Specific Approaches with Task-Specific Approaches with Task-Specific Approaches |  | A Preprint A Preprint A Preprint |
| → continued → continued → continued |  |  |  |  |  |  |
| Dataset Full Name (References) Dataset Full Name (References) Dataset Full Name (References) | Related Datasets Related Datasets Related Datasets | Modality Modality Modality | Main Anatomical Structure (Region) Main Anatomical Structure (Region) Main Anatomical Structure (Region) | N. Objects Objects N. Objects Objects N. Objects Objects | N. Images (with labels) N. Images (with labels) N. Images (with labels) | Links Links Links |
| MSD Lung Tumors OASIS-1 SpineWeb | --Automatic 3D MRI | 3D CT 3D MRI (T1 3D MRI (T2 | Lung, Tumors Brain Spine | 1 -13 | 95 416 24 | MSD Website OASIS Project MICCAI 2015 Publication |
| Medical Segmentation OASIS-1: Cross-sectional MRI SpineWeb | IVD Localization and | MP-RAGE) Dixon Protocol), | (Thorax) (Head) (Abdomen, Pelvis) | Lung Nodule [Too Many To List] Intervertebral Disc (L1-L2), Intervertebral Disc | (63) (416) (16) | Publication Official Website CSI 2016 Challenge |
| Decathlon -Lung Tumours (Simpson et al., 2019; Antonelli Data in Young, Middle Aged, Nondemented and Demented (Zheng et al., 2017) | Segmentation, IVDM3Seg | 3D MRI (T2) |  | (L2-L3), Intervertebral Disc (L3-L4), Intervertebral Disc (L4-L5), Intervertebral Disc |  | Preprint Publication Publication CSI 2016 Challenge |
| et al., 2022) Older Adults |  |  |  | (T11-T12), Intervertebral Disc (T12-L1), |  | Website |
| (Marcus et al., 2007) The MSD Lung Tumours (MSD Pancreas Tumour Medical Segmentation Decathlon -Pancreas Tumour (Simpson et al., 2019; Antonelli et al., 2022) Medical Segmentation Decathlon -Colon Cancer (Marcus et al., 2007) The Cranial Vault -Abdomen (Label Subset of Eight) (Landman et al., 2015) The MSD Pancreas Tumour (MSD Prostate --The Open Access OASIS-3 OASIS-3: Longitudinal Multimodal Neuroimaging, Clinical, and Cognitive Dataset Alzheimers Disease Multi-Atlas Labeling Beyond for Normal Aging and -The SpineWeb dataset Synapse - | 3D CT (CE) 3D MRI (T2) 3D PET (T2-FLAIR), 3D MRI (T1 MP-RAGE), 3D MRI (T2), 3D MRI 3D MRI (SWI), 3D CT, 3D fMRI (ASL), 3D fMRI (BOLD), 3D MRI (DTI), 3D CT (CE) | Pancreas (Abdomen) Prostate (Pelvis) (Abdomen) Brain (Head) Abdominal Organs | Vertebra L1 (First Sacral), Vertebra L2 (Second Sacral), Vertebra L3 (Third Sacral), Vertebra 2 Pancreas, Pancreas Tumor 2 Prostate (Peripheral Zone), Prostate (Transition Zone) (Right), Liver, Pancreas, Spleen, Stomach L4 (Fourth Sacral), Vertebra L5 (Fifth Sacral), Vertebra T11 (Eleventh Lumbar), Vertebra T12 (Twelfth Lumbar) Aorta, Gallbladder, Kidney (Left), Kidney -[On Demand from Dataset Curators], Brain, Cerebral Cortex, Cerebral Cortex white Matter, Subcortical Gray Matter 8 | 420 (281) 48 (32) (30) 6922 (-) 50 | SpineWeb 2015 Data MSD Website Publication Preprint Preprint MSD Website Publication MICCAI 2018 IVDM3Seg Official Website OASIS Project Official Website Publication Preprint Official Website |
| (Simpson et al., 2019; Antonelli |  | (Amyloid), |  |  |  |  |
| et al., 2022) |  | 3D PET (FDG), |  |  |  |  |
|  |  | 3D PET (Tau) |  |  |  |  |
| The Open Access Series of Imaging Studies (OASIS) project aims to provide freely available neuroimaging datasets to the scientific community. The series includes four main datasets: OASIS-1 (cross-sectional MRI data for aging and Alzheimer's), OASIS-2 (longitudinal MRI data for aging and Alzheimer's), OASIS-3 (extensive longitudinal multimodal data for aging and Alzheimers Disease), OASIS-3 Tau (OASIS-3 Flortaucipir F18 (AV1451) PET) and OASIS-4 (MR and clinical data for individuals with memory complaints). OASIS-3 is a The MSD Prostate (MSD Spleen Medical Segmentation -3D CT (CE) Spleen (Abdomen) 1 Spleen 61 (41) retrospective, longitudinal compilation of multimodal data collected over 30 years from 1378 participants (755 cognitively normal, 622 with cognitive decline, aged 42-95). It includes MSD Website 2842 MRI sessions with diverse sequences such as T1w, T2w, FLAIR, ASL, SWI, time of flight, resting-state BOLD, and DTI. Many MRI sessions are accompanied by FreeSurfer Publication segmentation masks. The dataset also features over 2157 raw PET imaging scans from PIB, AV45, and FDG tracers, with accompanying post-processed files from the Pet Unified Decathlon -Spleen Preprint Pipeline (PUP). Additionally, 451 Tau PET sessions (AV1451) are available as a sub-project. Also 1472 CT scans are available. Available labels numerosity and description is not very |
| (Simpson et al., 2019; Antonelli clear from website and publications. |  |  |  |  |  |
| et al., 2022) |  |  |  |  |  |  |
| The MSD Spleen (MSD Task09) dataset is a sub-task of the Medical Segmentation Decathlon, focusing on spleen segmentation from CT images. The dataset consists of portal NIH Pancreas-CT (Abdomen) Pancreas (80) venous phase CT scans from patients undergoing chemotherapy for liver metastases. Pancreas-CT -3D CT (CE) Pancreas 1 80 Official Website |
| (Roth et al., 2016) |  |  |  |  |  |  |
| (Simpson et al., 2019; Antonelli et al., 2022) The MSD Hippocampus (continues → -3D MRI (T1 MP-RAGE) Brain (Head) 2 Hippocampus (Anterior), Hippocampus (Posterior) 390 (260) MSD Website Publication Preprint MSSEG Multiple Sclerosis Lesion Segmentation (Styner et al., 2008) -3D MRI (DTI), 3D MRI (T1), 3D MRI (T2), 3D MRI (T2-FLAIR) Brain (Head) 1 Brain Hemorrage 51 (20) Official Website Publication The MSSEG (also MSseg08) dataset, created for a continues → The Pancreas-continues → |

## , introduced as part of a MICCAI 2023 challenge, is designed for voxel-level segmentation of the Inferior Alveolar Nerve (IAN) in Cone Beam Computed Tomography (CBCT) scans. It comprises 443 CBCT images, featuring both sparse annotations (443 cases total, 290 for training) of whihc some have dense annotations (153 cases total, 130 for training). For challenge evaluation, 8 cases are reserved for validation and 15 for testing, with additional undisclosed data provided during the evaluation phase. provides paired Magnetic Resonance Angiography (MRA) and Computed Tomography Angiography (CTA) scans. Initially launched as the TopCoW 2023 challenge, it focused on multi-class CoW vessel segmentation. The TopCoW 2024 edition significantly expands the dataset, increasing training data to 125 CTA/MRA pairs and doubling the online test set to 70 pairs with multi-center data. Labels for some 2023 data were updated for accuracy. The dataset includes 13 distinct vessel components of the CoW for segmentation. Originating from stroke patients at the University Hospital Zurich, scans were acquired using Siemens 1.5T or 3T MRI and various CT scanners.TotalSegmentator is a series of publicly-available, whole-body CT and MRI datasets with comprehensively annotated anatomical structures. The evolution of TotalSegmentator has involved expansions in both modalities and annotation scope. The initial release in July 2022, TotalSegmentator (dubbed TotalSegmentator V1), introduced the largest publicly available CT segmentation dataset at the time. It comprised 1204 CT images, providing annotations for 104 distinct anatomical structures. These images were distributed as 1082 for training, 57 for validation, and 65 for testing. Subsequently, the TotalSegmentator MRI dataset was introduced. This dataset includes 298 MR images, offering segmentation annotations for up to 56 common anatomical structures. Of these, 251 MR images originate from routine clinical practice at the University Hospital Basel, while 47 images from the Imaging Data Commons (IDC) platform were included to enhance diversity. This MRI component accounts for various lesions, scanners, imaging sequences, and data from different medical institutions. An update to the CT dataset was released as TotalSegmentator V2 in September 2023, building upon the first version. This update increased the total number of CT images from 1204 to 1228, with the increment specifically in the test set, expanded from 65 to 89 images. The number of annotated categories also increased from 104 to 117. Here are reported the condensed statistics fro TotalSegmentator V2 and MRI. Cathegories are not reported as they are too many, please refer to the official websites and publications. Models benhmarked on TotalSegmentator usually provide Dice scores for the following categories of grouped classes: All (all labels), Cardiac, Muscles, Organs, Ribs, Vertebrae. is a collection of test images from 8 different hospitals used for testing thoracic, abdominal and pelvic organs segmentation algorithm from CT images. The proposed training set is AbdomenAtlas, while the Touchstone Benchmark is a collection of volume-only test images. The Touchstone Benchmark is composed of two challenges: Touchstone 1.0 including 9 classes, the training set for which is the AbdomenAtlas 1.0 Mini, and the Touchstone 1.1 including all 25 classes, for which AbdomenAtlas 1.1 Mini should be used. The test sets are made of images from the publicly-available TotalSegmentator V2 and from a private dataset. Currently, only Touchstone 1.0 leaderboards are available, for which 9 classes are considered.WORD is a large-scale CT dataset specifically designed for comprehensive abdominal organ segmentation. It features 150 CT scans that span the entire abdominal region, each meticulously annotated for 16 distinct abdominal organs. This dataset is officially split into 100 scans for training, 20 for validation, and 30 for testing, however all labels are provided. What sets WORD apart from other common abdominal organ segmentation datasets is its extensive coverage of intestinal categories, including detailed annotations for the colon, intestine, and rectum. Additionally, it uniquely includes annotations for the left and right femoral heads.

| Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | with Task-Specific Approaches with Task-Specific Approaches |  | A Preprint A Preprint |
| → continued → continued |  |  |  |  |  |  |
| Dataset Full Name (References) Dataset Full Name (References) | Related Datasets Related Datasets | Modality Modality | Main Anatomical Structure (Region) Main Anatomical Structure (Region) | N. Objects Objects N. Objects Objects | N. Images (with labels) N. Images (with labels) | Links Links |
| TopCoW WORD | -- | 3D CT (CE), 3D CT (CE) | Brain Abdominal Organs | 13 16 | 200 150 | Official Challenge Website GitHub |
| TopCoW (Topology-Aware Whole Abdominal Organ |  | 3D MRI | (Head) (Abdomen, Pelvis) | Brain CoW Anterior Cerebral Artery (Left), Adrenal Glands, Bladder, Colon, Duodenum, | (130) (150) | Preprint Publication |
| Anatomical Segmentation of Dataset |  | (TOF-MRA) |  | Brain CoW Anterior Cerebral Artery (Right), Esophagus, Femur Head (Left), Femur Head |  | Publication (2) |
| the Circle of Willis (Liao et al., 2023; Luo et al., |  |  |  | Brain CoW Anterior Communicating Artery, (Right), Gallbladder, Intestine, Kidney (Left), |  |  |
| (Yang et al., 2024) 2022) |  |  |  | Brain CoW Basilar Artery, Brain CoW Internal Kidney (Right), Liver, Pancreas, Rectum, |  |  |
|  |  |  |  | Carotid Artery (Left), Brain CoW Internal Spleen, Stomach |  |  |
|  |  |  |  | Carotid Artery (Right), Brain CoW Middle |  |  |
|  |  |  |  | Cerebral Artery (Left), Brain CoW Middle |  |  |
|  |  |  |  | Cerebral Artery (Right), Brain CoW Posterior |  |  |
|  |  |  |  | Cerebral Artery (Left), Brain CoW Posterior |  |  |
|  |  |  |  | Cerebral Artery (Right), Brain CoW Posterior |  |  |
|  |  |  |  | Communicating Artery (Left), Brain CoW |  |  |
|  |  |  |  | Posterior Communicating Artery (Right), Brain |  |  |
|  |  |  |  | CoW Third A2 Artery |  |  |
| The TopCoW dataset TotalSegmentator | - | 3D CT / CT | Whole Body | - | 1526 | GitHub |
| TotalSegmentator |  | (CE), | (Whole Body) | [Too Many To List] | (1437) | Official Website |
| (Akinci DAntonoli et al., 2025; |  | 3D MRI |  |  |  | TotalSegmentator |
| Wasserthal et al., 2023) |  |  |  |  |  | Publication |
|  |  |  |  |  |  | TotalSegmentator MRI |
|  |  |  |  |  |  | Publication |
| ToothFairy | - | 3D CT (CB) | Mandible | 1 | 443 | Official Challenge Website |
| ToothFairy MICCAI 2023 |  |  | (Head) | Inferior Alveolar Nerve | (420) | Publication |
| Challenge Dataset |  |  |  |  |  |  |
| (Cipriano et al., 2022) |  |  |  |  |  |  |
| Touchstone Touchstone Benchmark (Bassi et al., 2024) The ToothFairy datasetcontinues → AbdomenAtlas, TotalSegmentator 3D CT / CT (CE) Abdominal Organs (Abdomen) 9 Aorta, Gallbladder, Inferior Vena Cava, Kidney (Left), Kidney (Right), Liver, Pancreas, Spleen, Stomach 6933 (0) Official Website Publication The Touchstone Benchmark continues → |

## Table 8 lists online repositories or collections of publicly available datasets for 3D medical image segmentation and analysiss. Collection of public repositories or articles aggregating 3D medical image datasets. This collection can be used to scout for datasets and gathers the efforts of the whole research community in one place.

| Name | Link |
| --- | --- |
| CLIP-Driven Universal Model | GitHub |
| SAT-DS | GitHub |
| TotalSegmentator | GitHub |
| AbdomenAtlas | GitHub |
| IMIS-Benchmark | GitHUb |
| M3D | GitHub |
| BiomedParseData | Hugging Face |
| OpenMEDLab | GitHub |
| (Awesome-Medical-Dataset) |  |
| Human Heart Project | Website |
| SA-Med3D-140K | GitHub |
| MedSAM Dataset List | GitHub |

## Results overview for brain datasets.

|  |  |  | Brain |  |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| ATLAS v2.0 | A 2 H 2 V 0 | 62.03 62.03 - | 66.62 66.62 - | 71.20 71.20 - | 1. H BrainSegFounder (71.20) 2. H MoME (62.03) |
| BraTS | A 24 H 12 V 12 | 55.68 55.68 61.00 | 85.66 85.69 85.54 | 92.08 92.08 91.74 | 1. H MEA M-SAM (92.08) 2. V TransUNet (91.74) 3. H BrainSegFounder (91.15) |
|  |  |  |  |  | 4. H EMedSAM (89.30) |
|  |  |  |  |  | 5. H Med-SA (89.10) |
| DLBS | A 1 H 1 | 96.54 96.54 | 96.54 96.54 | 96.54 96.54 | 1. H HERMES (96.54) |
|  | V 0 | - | - | - |  |
|  |  |  |  |  | continues → |

## Results overview for head and neck datasets.

|  |  | Head and Neck |  |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| HNASC | A 1 H 1 | 82.74 82.74 | 82.74 82.74 | 82.74 82.74 | 1. H MIS-FM (82.74) |
|  | V 0 | - | - | - |  |
| ToothFairy | A 4 H 4 V 0 | 61.40 61.40 - | 76.73 76.73 - | 80.80 80.80 - | 1. H Medical SAM 2 (MedSAM-2) (80.80) 2. H SAT (78.17) |
|  |  |  |  |  | 3. H SAM-Med2D (75.29) |
|  |  |  |  |  | 4. H One-Prompt (61.40) |
| Best-in-literature |  |  |  |  |
| HNASC | A 5 H 1 V 4 | 69.10 82.74 69.10 | 78.66 82.74 74.47 | 82.74 82.74 80.37 | 1. H MIS-FM (82.74) 2. V UNETR++ (80.37) 3. V nnU-Net (78.66) |
|  |  |  |  |  | 4. V nnFormer (70.27) |
|  |  |  |  |  | 5. V TransUNet (69.10) |
|  |  |  |  |  | continues → |

## Results overview for lungs datasets.

|  |  |  | Lungs |  |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| LIDC-IDRI | A 2 H 1 V 1 | 77.05 92.87 77.05 | 84.96 92.87 77.05 | 92.87 92.87 77.05 | 1. H Med3D (92.87) 2. V UNet++ (77.05) |
| LUNA16 | A 1 H 1 | 97.16 97.16 | 97.16 97.16 | 97.16 97.16 | 1. H SAT (97.16) |
|  | V 0 | - | - | - |  |
| MSD Lung Tu-mors | A 14 H 9 V 5 | 56.72 61.28 56.72 | 72.06 71.42 74.00 | 81.62 81.62 80.68 | 1. H MEA M-SAM (81.62) 2. V UNETR++ (80.68) 3. H CLIP-Driven Universal |
|  |  |  |  |  | Model (80.01) |
|  |  |  |  |  | 4. H LeSAM (79.57) |
|  |  |  |  |  | 5. V MedFormer (74.00) |
| Best-in-literature |  |  |  |  |
|  |  |  |  |  | continues → |

## Results overview for heart and thoracic vasculature datasets.

|  |  | Heart and Thoracic Vasculature |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| ACDC | A 13 H 5 V 8 | 70.90 70.90 90.00 | 92.06 90.41 92.58 | 95.18 92.26 95.18 | 1. V SCANeXt (95.18) 2. V nnU-Net (92.95) 3. V UNETR++ (92.83) |
|  |  |  |  |  | 4. V LHU-Net (92.66) |
|  |  |  |  |  | 5. V MedFormer (92.50) |
| LASC | A 2 H 1 V 1 | 91.00 91.00 91.55 | 91.28 91.00 91.55 | 91.55 91.00 91.55 | 1. V LHU-Net (91.55) 2. H SFR SAM (91.00) |
| M&Ms | A 1 H 1 | 87.02 87.02 | 87.02 87.02 | 87.02 87.02 | 1. H HERMES (87.02) |
|  | V 0 | - | - | - |  |
| MM-WHS | A 1 H 1 | 89.44 89.44 | 89.44 89.44 | 89.44 89.44 | 1. H SAT (89.44) |
|  | V 0 | - | - | - |  |
|  |  |  |  |  | continues → |
|  |  |  | 92 |  |  |

## Results overview for thoracic structures (multiorgan) datasets.

|  | Thoracic Structures (multiorgan) |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| SegTHOR | A 7 H 6 V 1 | 81.55 81.55 93.00 | 88.98 88.32 93.00 | 93.00 89.56 93.00 | 1. V nnU-Net (93.00) 2. H MIS-FM (89.56) 3. H IMIS-Net (89.27) |
|  |  |  |  |  | 4. H SAT (88.98) |
|  |  |  |  |  | 5. H PCNet (87.66) |
| Best-in-literature |  |  |  |  |
| SegTHOR | A 16 H 11 V 5 | 74.90 74.90 85.46 | 86.39 85.91 87.33 | 93.00 89.56 93.00 | 1. V nnU-Net (93.00) 2. V SwinUNETR (89.92) 3. H MIS-FM (89.56) |
|  |  |  |  |  | 4. H IMIS-Net (89.27) |
|  |  |  |  |  | 5. H SAT (88.98) |

## Results overview for bones datasets. Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison with Task-Specific Approaches

|  |  |  | Bones |  |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| TotalSegmentator Ribs | A 3 H 3 V 0 | 90.29 90.29 - | 91.53 91.53 - | 91.66 91.66 - | 1. H PCNet (91.66) 2. H SAT (91.53) 3. H STU-Net (90.29) |
| TotalSegmentator Vertebrae | A 4 H 4 V 0 | 86.49 86.49 - | 90.43 90.43 - | 91.69 91.69 - | 1. H PCNet (91.69) 2. H STU-Net (90.43) 3. H SAT (90.42) |
|  |  |  |  |  | 4. H CLIP-Driven Universal |
|  |  |  |  |  | Model (86.49) |
| VerSe | A 4 H 4 V 0 | 66.65 66.65 - | 75.21 75.21 - | 86.10 86.10 - | 1. H UniSeg (86.10) 2. H SAT (81.01) 3. H PCNet (69.40) |
|  |  |  |  |  | 4. H STU-Net (66.65) |
|  |  |  |  |  | continues → |

## Results overview for muscles datasets.

|  |  |  | Muscles |  |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| TotalSegmentator Muscles | A 4 H 4 V 0 | 88.83 88.83 - | 92.73 92.73 - | 94.43 94.43 - | 1. H CLIP-Driven Universal Model (94.43) 2. H SAT (93.33) |
|  |  |  |  |  | 3. H PCNet (92.13) |
|  |  |  |  |  | 4. H STU-Net (88.83) |
| Best-in-literature |  |  |  |  |
|  |  |  |  |  | continues → |

## Results overview for liver datasets.

|  |  |  | Liver |  |  |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| ATLAS 2023 | A 4 H 4 V 0 | 63.80 63.80 - | 71.11 71.11 - | 76.26 76.26 - | 1. H SAT (76.26) 2. H Medical SAM 2 (MedSAM-2) (71.80) |
|  |  |  |  |  | 3. H SAM-Med2D (70.42) |
|  |  |  |  |  | 4. H One-Prompt (63.80) |
| MSD Hepatic Ves-sels | A 9 H 7 V 2 | 63.43 63.43 67.67 | 68.20 68.20 68.34 | 79.59 79.59 69.00 | 1. H LeSAM (79.59) 2. H CLIP-Driven Universal Model (71.51) |
|  |  |  |  |  | 3. H UniSeg (71.20) |
|  |  |  |  |  | 4. V nnU-Net (69.00) |
|  |  |  |  |  | 5. H DeSD (68.20) |
|  |  |  |  |  | continues → |
|  |  |  | 100 |  |  |

## Results overview for pancreas datasets.

|  |  |  |  | Pancreas |  |
| --- | --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| MSD Tumour | Pancreas | A 16 H 13 V 3 | 40.20 40.20 55.49 | 70.75 71.54 64.03 | 80.49 80.49 67.50 | 1. H MEA M-SAM (80.49) 2. H PCNet (79.70) 3. H LeSAM (79.42) |
|  |  |  |  |  |  | 4. H STU-Net (78.95) |
|  |  |  |  |  |  | 5. H CLIP-Driven Universal |
|  |  |  |  |  |  | Model (72.59) |
| Pancreas-CT | A 1 H 0 | 81.96 - | 81.96 - | 81.96 - | 1. V LHU-Net (81.96) |
|  |  | V 1 | 81.96 | 81.96 | 81.96 |  |
| Best-in-literature |  |  |  |  |
|  |  |  |  |  |  | continues → |

## Results overview for colon datasets.

|  |  |  | Colon |  |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| MSD Colon Can-cer | A 10 H 9 V 1 | 38.45 38.45 58.00 | 56.50 55.00 58.00 | 77.18 77.18 58.00 | 1. H LeSAM (77.18) 2. H BiomedParse (66.51) 3. H CLIP-Driven Universal |
|  |  |  |  |  | Model (63.14) |
|  |  |  |  |  | 4. H 3DSAM-adapter (60.93) |
|  |  |  |  |  | 5. V nnU-Net (58.00) |
| Best-in-literature |  |  |  |  |
| MSD Colon Can-cer | A 18 H 13 V 5 | 18.80 38.45 18.80 | 58.73 63.14 39.80 | 77.18 77.18 59.45 | 1. H LeSAM (77.18) 2. H SAM-Med2D (76.45) 3. H Med-SA (75.36) |
|  |  |  |  |  | 4. H MedSAM (72.76) |
|  |  |  |  |  | 5. H BiomedParse (66.51) |

## Results overview for kidney datasets.

|  |  |  | Kidney |  |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| KiPA | A 1 H 1 | 80.19 80.19 | 80.19 80.19 | 80.19 80.19 | 1. H PCNet (80.19) |
|  | V 0 | - | - | - |  |
| KiTS | A 23 H 18 V 5 | 60.46 60.46 85.00 | 85.98 84.72 90.53 | 93.50 93.50 91.63 | 1. H MEA M-SAM (93.50) 2. H LeSAM (91.86) 3. V nnU-Net (91.63) |
|  |  |  |  |  | 4. V MedNeXt (91.02) |
|  |  |  |  |  | 5. V TransBTSV2 (90.53) |
| Best-in-literature |  |  |  |  |
| KiPA | A 4 H 2 V 2 | 30.72 78.44 30.72 | 59.34 79.31 35.48 | 80.19 80.19 40.25 | 1. H PCNet (80.19) 2. H STU-Net (78.44) 3. V SwinUNETR (40.25) |
|  |  |  |  |  | 4. V nnU-Net (30.72) |
|  |  |  |  |  | continues → |

## Results overview for spleen datasets.

|  |  |  | Spleen |  |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| MSD Spleen | A 10 H 8 V 2 | 93.91 93.91 96.40 | 96.20 95.88 96.70 | 97.27 97.27 97.00 | 1. H CLIP-Driven Universal Model (97.27) 2. V nnU-Net (97.00) |
|  |  |  |  |  | 3. H BiomedParse (96.86) |
|  |  |  |  |  | 4. H UniSeg (96.40) |
|  |  |  |  |  | 5. V UNETR (96.40) |
| Best-in-literature |  |  |  |  |
| MSD Spleen | A 17 H 11 V 6 | 79.59 79.59 92.20 | 95.77 95.77 96.05 | 97.27 97.27 97.00 | 1. H CLIP-Driven Universal Model (97.27) 2. V nnU-Net (97.00) |
|  |  |  |  |  | 3. V SwinUNETR (96.99) |
|  |  |  |  |  | 4. H BiomedParse (96.86) |
|  |  |  |  |  | 5. H DoDNet (96.50) |

## Results overview for prostate datasets.

|  |  |  | Prostate |  |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| MSD Prostate | A 6 H 3 V 3 | 72.85 72.85 73.32 | 76.02 77.98 74.05 | 89.70 89.70 83.50 | 1. H UniSeg (89.70) 2. V nnU-Net (83.50) 3. H SAT (77.98) |
|  |  |  |  |  | 4. V SwinUNETR-V2 (74.05) |
|  |  |  |  |  | 5. V SwinUNETR (73.32) |
| PROMISE12 | A 7 H 5 V 2 | 86.90 87.28 86.90 | 89.97 89.97 89.42 | 94.29 94.29 91.94 | 1. H SPA (94.29) 2. H MA-SAM (92.60) 3. V nnU-Net (91.94) |
|  |  |  |  |  | 4. H BiomedParse (89.97) |
|  |  |  |  |  | 5. H FLAP-SAM (88.67) |
| Best-in-literature |  |  |  |  |
|  |  |  |  |  | continues → |

## Results overview for abdominal multi-organ datasets. Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison with Task-Specific Approaches Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison with Task-Specific Approaches Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison with Task-Specific Approaches Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison with Task-Specific Approaches

|  |  | Abdominal Multi-Organ |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| AMOS | A 11 H 8 V 3 | 74.39 74.39 88.00 | 88.00 86.13 90.00 | 91.77 90.49 91.77 | 1. V MedNeXt (91.77) 2. H STU-Net (90.49) 3. V 3D UX-Net (90.00) |
|  |  |  |  |  | 4. H MultiTalent (89.81) |
|  |  |  |  |  | 5. H HERMES (88.59) |
|  |  |  |  |  | continues → |

## Results overview for whole body lesions datasets.

|  |  | Whole Body Lesions |  |
| --- | --- | --- | --- | --- | --- |
| Benchmark | N. | Min. | Median Max. Top 5 overall |
| Primary |  |  |  |  |  |
| AutoPET | A 1 H 1 | 74.04 74.04 | 74.04 74.04 | 74.04 74.04 | 1. H HERMES (74.04) |
|  | V 0 | - | - | - |  |
| ULS | A 1 H 1 | 70.46 70.46 | 70.46 70.46 | 70.46 70.46 | 1. H SegVol (70.46) |
|  | V 0 | - | - | - |  |
| Best-in-literature |  |  |  |  |
|  |  |  |  |  | continues → |

### Formule


$$Biomedical$$

### Formule


$$- 3D CT / CT (CE), 3D MRI (T1), 3D MRI (T2) Abdominal Organs (Abdomen)4 Kidney (Left), Kidney (Right), Liver, Spleen 40 (20)$$
