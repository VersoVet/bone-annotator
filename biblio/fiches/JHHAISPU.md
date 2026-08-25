# Foundation Models for Biomedical Image Segmentation: A Survey

**Auteurs** : Ho Hin Lee, 裕二 池谷, Theodore Zhao, Yanbo Xu, Jianwei Yang, Naoto Usuyama, Cliff Wong, Wei Mu, Bennett A. Landman, Yuankai Huo
**Année** : 2024
**DOI** : 10.48550/arxiv.2401.07654

## Résumé

Recent advancements in biomedical image analysis have been significantly driven by the Segment Anything Model (SAM). This transformative technology, originally developed for general-purpose computer vision, has found rapid application in medical image processing. Within the last year, marked by over 100 publications, SAM has demonstrated its prowess in zero-shot learning adaptations for medical imaging. The fundamental premise of SAM lies in its capability to segment or identify objects in images without prior knowledge of the object type or imaging modality. This approach aligns well with tasks achievable by the human visual system, though its application in non-biological vision contexts remains more theoretically challenging. A notable feature of SAM is its ability to adjust segmentation according to a specified resolution scale or area of interest, akin to semantic priming. This adaptability has spurred a wave of creativity and innovation in applying SAM to medical imaging. Our review focuses on the period from April 1, 2023, to September 30, 2023, a critical first six months post-initial publication. We examine the adaptations and integrations of SAM necessary to address longstanding clinical challenges, particularly in the context of 33 open datasets covered in our analysis. While SAM approaches or achieves state-of-the-art performance in numerous applications, it falls short in certain areas, such as segmentation of the carotid artery, adrenal glands, optic nerve, and mandible bone. Our survey delves into the innovative techniques where SAM's foundational approach excels and explores the core concepts in translating and applying these models effectively in diverse medical imaging scenarios.

## Méthodologie

{'study_design': 'Revue de la littérature couvrant la période du 1er avril 2023 au 30 septembre 2023, analysant les adaptations de SAM appliquées à 33 jeux de données ouverts en imagerie médicale', 'intervention': None, 'control': None, 'primary_outcomes': ["Performance de segmentation de SAM comparée à l'état de l'art sur diverses tâches d'imagerie médicale"], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': '1er avril 2023 au 30 septembre 2023 (six premiers mois post-publication initiale)', 'setting': "Analyse bibliographique de publications sur l'imagerie biomédicale"}

## Résultats

{'quantitative': [{'outcome': 'Nombre de publications sur SAM en imagerie médicale durant la première année', 'value': 'over 100', 'unit': 'publications', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Within the last year, marked by over 100 publications, SAM has demonstrated its prowess in zero-shot learning adaptations for medical imaging.'}, {'outcome': 'Taille du jeu de données de pré-entraînement SA-1B', 'value': '11M images, 1.1B masks', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Introduction', 'source_quote': 'The entire SAM is trained on the large-scale dataset SA-1B, which consists of 11M high-resolution images with 1.1B high-quality segmentation masks, 400× more masks than any existing segmentation dataset [80].'}], 'qualitative_findings': ["SAM atteint ou approche l'état de l'art dans de nombreuses applications d'imagerie médicale", 'SAM échoue dans certains domaines spécifiques de segmentation'], 'main_findings': ["SAM approche ou atteint la performance de l'état de l'art dans de nombreuses applications d'imagerie médicale", "SAM échoue dans certaines applications, telles que la segmentation de l'artère carotide, des glandes surrénales, du nerf optique et de la mandibule"]}

## Conclusions

SAM démontre un potentiel important pour combler l'écart technique entre les applications générales et les applications spécifiques au domaine médical Des adaptations et intégrations spécifiques de SAM sont nécessaires pour répondre aux exigences particulières de la segmentation d'images médicales Certaines limitations persistantes de SAM nécessitent des approches méthodologiques futures pour être surmontées

## Chronological timeline of medical image segmentation datasets. "Public" includes a link to each dataset (if available) or paper (if not). "Annotations" denotes the number of classes with ground-truth quality labels in each dataset.

| Year | Dataset | Public |  | Details |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Modality | Anatomy | Data Size | Label Quality | # Targets | Seg. Target Type |
|  | JSRT [134] | X-Ray | Chest | 307 | Manual | 2 | Multi-Organ |
|  | VESSEL12 [124] | CT | Lung | 20 | Manual | 1 | Organ Parts |
|  | PROMISE12 [96] | MRI | Prostate | 100 | Manual | 1 | Single Organ |
|  | NCI-ISBI [21] | MRI | Prostate | 80 | Manual | 2 | Organ Parts |
|  | BTCV [82] | CT | Abdomen | 50 | Manual | 13 | Multi-Organ |
|  | CT-Lymph Nodes [34, 119, 122] | CT | Mediastinum | 176 | Manual | 1 | Single Organ |
|  | GlaS [135, 136] | Pathology | Colon | 165 | Manual | 1 | Cells |
|  | Pancreas-CT [34, 120, 121] | CT | Pancreas | 80 | Manual | 1 | Single Organ |
|  | LiTS [18] | CT | Liver | 131 | Manual | 2 | Tumor |
|  | ACDC [17] | MRI | Heart | 150 | Manual | 3 | Organ Parts |
|  | FUMPE [103] | CT | Lung | 35 | Exp.+Mdl. | 1 | Lesion |
|  | MSD [10] | CT, MRI | Multiple | 1411 CT, 1222 MRI | Manual | 18 | Multi-Task |
|  | DRIVE [138] | Fundus | Retina | 40 | Manual | 1 | Organ Parts |
|  | REFUGE [111] | Fundus | Retina | 1200 | Manual | 2 | Organ Parts |
|  | CHAOS [74-76] | CT, MRI | Abdomen | 40 CT, 40 MRI | Manual | 4 | Multi-Organ |
|  | SIIM-ACR Pneumothorax [160] | X-Ray | Chest | 12047 | Manual | 1 | Lesion |
|  | AbdomenUS [146] | Ultrasound | Abdomen | 61 Real, 926 Synth. | Real+Synth. | 8 | Multi-Organ |
|  | Breast Ultrasound Images [4] | Ultrasound | Breast | 780 | Manual | 3 | Tumor |
|  | CAMUS [83] | Ultrasound | Heart | 500 | Manual | 3 | Organ Parts |
|  | M&Ms [24] | MRI | Heart | 375 | Manual | 3 | Organ Parts |
|  | MosMed COVID-19 [109] | CT | Lung | 50 | Manual | 1 | Infection |
|  | COVID-19 Radiography [32, 116] | X-Ray | Chest | 21165 | Manual | 1 | Single Organ |
|  | COVID-QU-Ex [32, 37, 116, 141, 142] | X-Ray | Chest | 33920 | Manual | 2 | Infection |
|  | QaTa-COV19 [38] | X-Ray | Chest | 9258 | Manual | 1 | Infection |
|  | CT2US [137] | Ultrasound | Abdomen | 4586 | Synth. | 1 | Single Organ |
|  | PolypGen [5-7] | Endoscope | Colon | 8037 | Manual | 1 | Polyp |
|  | AbdomenCT-1K [102] | CT | Abdomen | 1112 | Exp.+Mdl. | 4 | Multi-Organ |
|  | AMOS [72] | CT, MRI | Abdomen | 500 CT, 100 MRI | Exp.+Mdl. | 15 | Multi-Organ |
|  | KiTS [57] | CT | Kidney | 599 | Exp.+Mdl. | 3 | Organ, Tumor |
|  | TotalSegmentator [153] | CT | Full Body | 1228 | Manual | 117 | Multi-Organ |
|  | BraTS [2, 13-16, 73, 77, 81, 106, 107] | MRI | Brain | 4500 | Manual | 3 | Tumor |
|  | HaN-Seg [113] | CT, MRI | Head & Neck | 56 CT, 56 MRI | Manual | 30 | Multi-Organ |
|  | FH-PS-AOP [100] | Ultrasound | Transperineal | 6224 | Exp.+Mdl. | 2 | Multi-Organ |

## Overview of various existing works that build upon SAM.

| Year-Month Method | Tasks | 2D | 3D | A.P.P | P.A | E.Frozen | E.Finetune | R.N.M | T.P.H | T.P.E | T.A | Downstream Tasks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2023-April | SAM-Adaptor [28] |  | - | - | - |  | - | - | - | - |  | Polyp |
| 2023-April | SAMAug [166] |  |  | - | - |  |  | - |  | - | - | - | H&E, Polyp |
| 2023-April | MedSAM Adaptor [154] |  |  | - | - | - | - |  | - | - |  | Abd, Opt, B.T, T.N |
| 2023-April | LOSAM [166] |  |  | - | - | - |  | - | - | - |  | - | Vessel & Lesion |
| 2023-April | SAMed [162] |  |  | - | - | - |  | - | - |  |  |  | Abd |
| 2023-April | GazeSAM [148] |  |  | - |  | - |  | - | - | - | - | - | Abd |
| 2023-April | SkinSAM [63] |  |  | - | - |  | - |  | - | - | - | - | S.L |
| 2023-April | PiClick [158] |  |  | - | - | - |  | - | - | - | - | - | Neural Tissue |
| 2023-May | Polyp-SAM [94] |  |  | - | - | - | - |  | - | - |  | - | Polyp |
| 2023-May | SAM-Track [31] |  |  | - | - |  |  | - | - | - | - | - | Brain |
| 2023-May | WS-SAM [54] |  |  | - |  | - |  | - |  | - | - | - | Polyp |
| 2023-May | BreastSAM [62] |  |  | - | - |  |  | - | - | - | - | - | Breast C. |
| 2023-May | LuSAM [69] |  |  | - | - | - |  | - | - | - | - | - | Lung |
| 2023-May | IAMSAM [84] |  |  | - | - | - |  | - | - | - | - | - | H & E |
| 2023-June | DeSAM [46] |  |  | - | - | - |  | - | - | - |  |  | Prostate |
| 2023-June | AutoSAM(1) [128] |  | - | - | - |  | - | - | - |  | - | H & E, Polyp |
| 2023-June | TEPO [129] |  |  | - |  | - |  | - |  | - | - | - | Brain |
| 2023-June | RASAM [163] |  |  | - | - | - |  | - | - | - | - | - | Organ-at-risk |
| 2023-June | 3DSAM-adaptor [48] | - |  | - |  |  | - | - | - |  |  | Parts Tumor |
| 2023-June | AutoSAM(2) [64] |  | - | - | - |  | - | - |  | - | - | Cardiac Structure |
| 2023-June | MedLSAM [89] |  |  | - |  | - |  | - |  | - | - | - | H & N, Abd, Lung |
| 2023-June | CellViT [59] |  |  | - | - | - | - |  | - |  | - | - | H & E |
| 2023-July | SAM-U [39] |  |  | - | - |  |  | - | - | - | - | - | Opt |
| 2023-July | SAM Med [149] |  |  | - |  |  |  | - | - | - | - |  | Abd, Prostate |
| 2023-July | SAMAug [36] |  |  | - | - |  |  | - | - | - | - | - | Polyp, Lung |
| 2023-July | All-in-SAM [35] |  |  | - |  |  |  | - | - |  |  | - | H & E |
| 2023-July | SAM-Path [161] |  |  | - | - |  |  | - | - |  |  | - | H & E |
| 2023-July | CmAA [132] |  |  | - | - | - |  | - | - |  | - | - | Glioma |
| 2023-July | MedSAM [101] |  |  | - | - | - | - | - |  | - | - | - | 15 I.M, >30 C.T |
| 2023-August | SAM-MLC [66] |  |  | - |  | - |  | - |  | - | - | - | Lung |
| 2023-August | AdaptiveSAM [112] |  | - | - |  | - |  | - |  |  | - | S.S |
| 2023-August | Poly-SAM++ [20] |  | - | - |  |  | - | - | - | - | - | Polyp |
| 2023-August | SPSAM [155] |  |  | - |  |  |  | - | - | - |  | - | Polyp, S.L |
| 2023-August | SamDSK [167] |  |  | - | - | - |  | - |  | - | - | - | Polyp, S.L, Breast C. |
| 2023-August | AutoSAM Adaptor [90] | - |  | - |  |  | - | - | - |  |  | Abd |
| 2023-August | SAM-Med2D [30] |  | - | - | - |  | - | - | - |  |  | 9 MICCAI2023 |
| 2023-August | SAMedOCT [43] |  |  | - | - | - |  | - |  | - | - | - | OCT |
| 2023-September | SAM3D [23] |  |  | - | - | - |  | - | - |  | - | - | Brain Lung" Abd |
| 2023-September | SAMUS [95] |  |  | - | - | - |  | - |  | - | - | - | Ultrasound |
| 2023-September | MA-SAM [25] |  | - |  | - | - |  | - | - | - | - |  | Abd, Prostate, S.S |
| 2023-September | MedVISTA-SAM [25] |  |  | - | - |  | - | - | - | - |  | Echocardiography |

## Quantitative Comparisons between the Zero-Shot Performance of SAM and Current State-Of-The-Art (SOTA) Approaches on Different Radiology Datasets. (p.f: foreground point, p.b: background point)

| Dim. Modality | Region | Targets | SOTAs | Performance MedSAM | SAM | Prompt Mode |
| --- | --- | --- | --- | --- | --- | --- |

## Quantitative Comparisons between the Zero-Shot Performance of SAM and Current State-Of-The-Art (SOTA) Approaches on Different Pathology Datasets.

|  |  | , 107] | MRI | Brain | 1.0 isotropic |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | NCI-ISBI [21] | MRI | Prostate | - | 3.0-4.0 |
|  | PROMISE12 [96] | MRI | Prostate | 0.273-0.750, | 2.2-4.0 |
|  | AMOS (MRI) [72] | MRI | Abdomen | - | 0.82-6.0 |
|  | CHAOS (MRI) [74-76] | MRI | Abdomen | 1.36-1.89 | 5.5-9.0 |
|  | HaN-Seg (MRI) [113] | MRI | Head and Neck | 0.47-0.82 | 3.0-5.0 |
|  | MSD (Brain) [10] | MRI | Brain | 1.0 isotropic |
|  | MSD (Hippocampus) [10] | MRI | Brain | 1.0 isotropic |
|  | MSD (Heart) [10] | MRI | Heart | 1.25 | 2.7 |
|  | MSD (Prostate) [10] | MRI | Prostate | 0.6 | 4.0 |
| Modality | Region | Tasks |  | Resolution | Performance SOTAs SAM | Prompt Mode |
|  | Skin | Tumor |  | 0.5 × | 0.720 [40] | 0.750 | 20 points |
|  |  | Glomerular (CAP) Glomerular Tuft (TUFT) | 5 × | 0.965 [40] 0.966 [40] | 0.801 0.799 | 20 points 20 points |
| H & E | Kidney | Distal Tubular (DT) Proximal Tubular (PT) | 10 × | 0.810 [40] 0.898 [40] | 0.604 0.666 | 20 points 20 points |
|  |  | Arteries (VES) |  | 0.851 [40] | 0.685 | 20 points |
|  |  | Peritubular Capillaries (PTC) |  | 0.772 [40] | 0.646 | 20 points |
|  | Different Tumors | Nuclei |  | 40 × | 0.818 [40] | 0.417 | 20 points |
|  | Colon | Adenocarcinoma, Benign Glands | 20 × | 0.797 [151] | 0.525 | classes prompt |
| sub-saharan africa patient population (brats-africa). arXiv |  |  |  |
| preprint arXiv:2305.19369, 2023. 5, 14 |  |  |  |  |
