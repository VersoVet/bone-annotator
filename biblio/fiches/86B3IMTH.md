# MedLSAM: Localize and segment anything model for 3D CT images.

**Auteurs** : Wenhui Lei, Wei Xu, Kang Li, Xiaofan Zhang, Shaoting Zhang
**Année** : 2025
**DOI** : 10.1016/j.media.2024.103370

## Résumé

Recent advancements in foundation models have shown significant potential in medical image analysis. However, there is still a gap in models specifically designed for medical image localization. To address this, we introduce MedLAM, a 3D medical foundation localization model that accurately identifies any anatomical part within the body using only a few template scans. MedLAM employs two self-supervision tasks: unified anatomical mapping (UAM) and multi-scale similarity (MSS) across a comprehensive dataset of 14,012 CT scans. Furthermore, we developed MedLSAM by integrating MedLAM with the Segment Anything Model (SAM). This innovative framework requires extreme point annotations across three directions on several templates to enable MedLAM to locate the target anatomical structure in the image, with SAM performing the segmentation. It significantly reduces the amount of manual annotation required by SAM in 3D medical imaging scenarios. We conducted extensive experiments on two 3D datas

## Méthodologie

{'study_design': "Approche en deux étapes : (1) MedLAM localise automatiquement les structures anatomiques cibles dans des images médicales volumétriques via deux tâches d'auto-supervision (unified anatomical mapping - UAM et multi-scale similarity - MSS) et un réseau de projection prédisant les décalages physiques 3D entre patches ; (2) SAM ou MedSAM utilise les bounding boxes issues de MedLAM pour effectuer la segmentation.", 'intervention': 'MedLSAM (MedLAM + SAM/MedSAM) utilisant des annotations par points extrêmes sur quelques templates pour générer automatiquement des prompts (bboxes) de segmentation', 'control': "Comparaisons avec UniverSeg (Butoi et al., 2023), prompts issus de nnDetection, prompts manuels (borne supérieure de performance pour SAM/MedSAM), et nnU-Net (Isensee et al., 2021) entraîné soit sur le même petit ensemble de support (borne inférieure) soit sur l'ensemble complet des données via validation croisée à 5 plis (borne supérieure)", 'primary_outcomes': ['Précision de localisation anatomique de MedLAM', 'Score DSC (Dice Similarity Coefficient) de segmentation de MedLSAM comparé aux méthodes de référence'], 'secondary_outcomes': ["Réduction du volume d'annotations manuelles nécessaires"], 'statistical_methods': ['Validation croisée à cinq plis (nnU-Net, nnDetection)', 'Comparaison de scores DSC entre méthodes'], 'duration': None, 'setting': "Étude computationnelle sur données d'imagerie médicale (CT scans), non clinique"}

## Résultats

{'quantitative': [{'outcome': 'DSC score - œil gauche (MedLSAM vs prompt manuel)', 'value': '69.3% (MedLSAM) vs 70.0% (manuel)', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'in the case of the left and right eye, MedLSAM attains a DSC score of 69.3% and 69.4%, while the manual prompt reaches 70.0% and 69.1%'}, {'outcome': 'DSC score - œil droit (MedLSAM vs prompt manuel)', 'value': '69.4% (MedLSAM) vs 69.1% (manuel)', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'in the case of the left and right eye, MedLSAM attains a DSC score of 69.3% and 69.4%, while the manual prompt reaches 70.0% and 69.1%'}, {'outcome': 'Écart de DSC MedLSAM vs prompt manuel pour le pancréas', 'value': "jusqu'à 35% d'écart", 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'for certain abdominal organs with substantial shape variability, such as the pancreas, the performance gap between MedLSAM and manual prompts is more significant, with a DSC score difference reaching up to 35%'}], 'qualitative_findings': ['MedLSAM performe de manière comparable aux prompts manuels sur certains organes de la tête et du cou', 'MedLSAM reste en retrait pour les organes abdominaux volumineux ou morphologiquement complexes'], 'main_findings': ['MedLAM peut localiser directement des structures anatomiques à partir de seulement quelques scans de référence, avec des performances comparables aux modèles entièrement supervisés', "MedLSAM se rapproche des performances de SAM et de ses adaptations médicales avec prompts manuels, tout en minimisant le besoin d'annotations par points sur l'ensemble du jeu de données", 'nnU-Net, même entraîné avec seulement cinq paires image-label de support, peut surpasser les résultats de segmentation par prompts manuels pour la plupart des organes abdominaux', 'Les méthodes de segmentation basées sur des prompts automatiques restent en deçà des méthodes entièrement supervisées']}

## Conclusions

MedLAM, en utilisant seulement quelques échantillons de support, peut atteindre des performances comparables ou supérieures aux modèles entièrement supervisés existants pour la localisation anatomique MedLSAM constitue une avancée pionnière vers l'automatisation complète de l'utilisation de SAM en imagerie médicale, réduisant considérablement la charge d'annotation MedLSAM ne parvient pas encore à égaler les modèles entièrement supervisés comme nnU-Net, en particulier pour les organes présentant des anomalies anatomiques significatives Des travaux futurs devraient viser à améliorer la polyvalence de MedLAM et son intégration avec les applications émergentes d'IA médicale généraliste (GMAI)

## Multi Scale Similarity Feature Decoder Feature Decoder 𝒄 𝒋 𝒙 Feature Encoder Feature Encoder 𝒙 ′ 𝒄′ 𝒋 𝒄 𝒋 Extract feature Conv. Extract the target point Feature map & Normalize

| 𝒄′ 𝒋 | 2x ↓ | 4x ↓ |
| --- | --- | --- |
|  | CE Loss |
| 𝑺 𝒄 𝒋 𝟎 | 𝑺 𝒄 𝒋 𝟏 | 𝑺 𝒄 𝒋 𝟐 |
| 𝒔 | 𝒔 | 𝒔 |

## Detailed information of the 16 CT datasets for MedLAM training.

| Dataset | Number | Anatomical Region |
| --- | --- | --- |
| GLIA Bo et al. (2021) | 1338 | HaN |
| ACRIN 6685Lowe et al. (2019) | 260 | HaN |
| OPC-RadiomicsKwan et al. (2018) | 606 | HaN |
| Head-Neck-PET-CTVallieres et al. (2017) | 298 | HaN |
| HNSCC Grossberg et al. (2018) | 591 | HaN/Thorax/Abdomen |
| autoPET Gatidis et al. (2022) | 1014 | Whole |
| MELA Chen (2022) | 770 | Thorax |
| LIDC-IDRIArmato III et al. (2011) | 1308 | Thorax |
| STOIC2021Revel et al. (2021) | 2000 | Thorax |
| MSD-LungAntonelli et al. (2022) | 95 | Thorax |
| CBIS-DDSMLee et al. (2017) | 2620 | Thorax |
| AMOS 2022Ji et al. (2022) | 500 | Thorax/Abdomen |
| Kits19Heller et al. (2020) | 141 | Abdomen |
| MSD-ColonAntonelli et al. (2022) | 190 | Abdomen |
| MSD-PancreasAntonelli et al. (2022) | 281 | Abdomen |
| FLARE2022Ma et al. (2022) | 2000 | Abdomen |
| Total | 14,012 | Whole |

## Comparison of MedLAM with few-shot and fully supervised (FS) localization models on the landmark localization task using the StructSeg Headand-Neck and WORD datasets. Results are reported in Average Localization Error (ALE, mean±std mm). " †" indicates that the differences between Med-LAM and all baseline methods are statistically significant at p < 0.05.

|  | (a) StructSeg Head-and-Neck |  |
| --- | --- | --- | --- | --- |
| Organs | MedLAM (5-shot) | DetCo (5-shot) | Mask R-CNN nnDetection (FS) (FS) |
| Brain Stem | 3.5 ± 2.3 † | 54.1±55.8 | 5.2±0.4 | 15.5±19.1 |
| Eye L | 3.4 ± 1.5 | 56.4±44.1 | 3.5±0.6 | 11.5±18.7 |
| Eye R | 3.0 ± 1.3 † | 68.6±48.6 | 3.9±0.5 | 13.3±13.9 |
| Lens L | 3.7 ± 1.4 † | 97.9±50.9 | 16.6±0.7 | 20.5±34.2 |
| Lens R | 3.1 ± 1.7 † | 80.8±62.8 | 15.4±0.6 | 25.8±28.2 |
| Opt Nerve L | 3.6 ± 2.3 † | 75.8±41.6 | 18.3±38.2 | 18.5±21.0 |
| Opt Nerve R | 3.8 ± 2.1 † | 70.3±52.1 | 25.1±57.0 | 31.4±23.9 |
| Opt Chiasma | 4.1 ± 2.0 † | 68.1±52.6 | 26.3±34.4 | 14.8±18.3 |
| Temporal Lobes L 5.7 ± 2.5 | 93.6±51.2 | 5.7±5.3 | 31.6±34.0 |
| Temporal Lobes R 4.6 ± 3.2 | 64.5±52.7 | 5.2±2.2 | 17.9±22.7 |
| Pituitary | 4.5 ± 2.3 † | 89.5±38.3 | 67.8±57.3 | 34.7±27.1 |
| Parotid Gland L | 6.6±2.4 | 64.8±41.3 | 6.6 ± 1.7 | 17.9±22.7 |
| Parotid Gland R | 6.4 ± 3.4 † | 80.3±52.2 | 32.0±127.2 | 23.1±32.3 |
| Inner Ear L | 4.1 ± 1.3 † | 57.1±38.0 | 64.0±0.0 | 17.4±21.0 |
| Inner Ear R | 4.7 ± 1.4 † | 73.1±44.4 | 38.8±0.0 | 29.8±25.1 |
| Mid Ear L | 5.7 ± 3.6 † | 75.0±55.4 | 22.6±1.1 | 28.0±27.2 |
| Mid Ear R | 5.4 ± 2.9 † | 74.0±63.5 | 43.2±23.2 | 28.3±26.0 |
| TM Joint L | 4.5 ± 1.8 † | 52.7±46.5 | 47.9±33.9 | 18.7±19.5 |
| TM Joint R | 3.9 ± 1.5 † | 83.9±54.3 | 49.3±33.8 | 33.5±36.0 |
| Spinal Cord | 4.4 ± 3.1 † | 97.6±40.2 | 27.4±41.7 | 17.1±26.3 |
| Mandible L | 3.6 ± 2.2 † | 72.1±46.9 | 7.0±19.9 | 26.3±21.5 |
| Mandible R | 3.8 ± 2.6 † 129.2±45.9 | 5.5±1.6 | 34.5±32.3 |
| Average | 4.3 ± 1.2 † | 75.2±32.7 | 24.4±14.5 | 23.3±12.9 |
|  |  | (b) WORD |  |  |
| Organs | MedLAM (5-shot) | DetCo (5-shot) | Mask R-CNN nnDetection (FS) (FS) |
| Liver | 20.4±14.4 144.3±61.5 | 11.5 ± 5.8 † | 38.0±51.1 |
| Spleen | 9.5 ± 7.3 | 65.6±68.8 | 11.9±3.3 | 22.7±30.0 |
| Kidney L | 8.8 ± 14.3 61.6±42.8 | 11.2±14.5 | 20.4±36.9 |
| Kidney R | 5.9 ± 5.8 103.9±50.1 | 7.9±5.2 | 40.1±41.4 |
| Stomach | 29.3±20.2 71.8±54.4 | 14.2 ± 4.4 † | 32.7±36.1 |
| Gallbladder | 33.8±15.6 137.0±75.7 | 8.8 ± 7.1 † | 38.1±43.2 |
| Esophagus | 12.2±9.2 | 85.8±44.2 | 6.2 ± 2.8 † | 27.4±32.1 |
| Pancreas | 23.3±13.5 64.0±58.2 | 13.5 ± 3.5 † | 37.7±47.1 |
| Duodenum | 19.6±15.6 81.7±58.4 | 13.5 ± 5.5 † | 39.5±42.6 |
| Colon | 28.7±20.1 75.1±77.8 | 21.5 ± 11.3 † | 43.9±47.0 |
| Intestine | 28.9±13.2 97.1±65.4 | 18.9 ± 7.9 † | 39.2±44.9 |
| Adrenal | 12.6±9.5 | 82.5±51.5 | 10.8 ± 7.7 † | 24.1±46.6 |
| Rectum | 13.2±8.1 104.6±53.4 | 9.5 ± 16.5 † | 33.4±31.2 |
| Bladder | 14.2±9.5 109.1±82.0 | 6.9 ± 3.0 † | 34.3±41.8 |
| Head of Femur L 10.6±27.3 97.5±48.8 | 5.3 ± 2.8 † | 20.8±38.6 |
| Head of Femur R 9.7±11.7 | 88.8±72.7 | 6.2 ± 6.1 † | 46.7±68.3 |
| Average | 17.5±10.8 92.2±45.4 | 11.1 ± 4.2 † | 33.6±30.2 |
| 4.4. Evaluation of MedLAM |  |  |
| 4.4.1. Comparison with Other Methods |  |

## Comparison of MedLAM with few-shot, fully supervised (FS), and zero-shot localization models on the organ detection task using the StructSeg Headand-Neck and WORD datasets. Results are reported in IoU and Wall Distance (WD). " †" indicates that the differences between MedLAM and all baseline methods are statistically significant at p < 0.05.

| (a) StructSeg Head-and-Neck |
| --- |

## Impact of the support volume size k of MedLAM on organ detection: IoU score ↑ (mean ± std %) on the WORD dataset. ± 12.4 46.9 ± 15.6 55.4 ± 16.9 53.1 ± 17.3 Head of Femur L 57.4 ± 12.7 72.6 ± 13.9 76.7 ± 16.7 76.3 ± 14.7 Head of Femur R 50.2 ± 10.3 71.9 ± 14.6 69.4 ± 14.4 70.4 ± 14.3 Average 36.8 ± 13.9 49.3 ± 14.7 56.6 ± 14.8 58.1 ± 14.7

| Organs |  | k |  |
| --- | --- | --- | --- | --- |
|  | 1 | 3 | 5 | 7 |
| Liver | 57.9 ± 12.7 69.0 ± 11.4 73.0 ± 11.6 76.1 ± 10.7 |
| Spleen | 53.7 ± 14.3 50.9 ± 19.9 70.9 ± 13.3 72.2 ± 12.6 |
| Kidney L | 51.0 ± 25.1 67.6 ± 16.8 71.0 ± 15.9 71.0 ± 15.7 |
| Kidney R | 43.1 ± 21.0 66.9 ± 14.4 76.0 ± 13.8 76.1 ± 11.5 |
| Stomach | 37.9 ± 15.4 43.6 ± 13.1 49.1 ± 14.3 52.9 ± 14.6 |
| Gallbladder | 06.0 ± 7.4 12.3 ± 11.9 12.0 ± 11.0 13.8 ± 17.1 |
| Esophagus | 35.2 ± 19.3 32.9 ± 15.1 44.2 ± 17.9 45.8 ± 17.2 |
| Pancreas | 20.5 ± 10.5 29.4 ± 14.7 44.1 ± 17.3 52.8 ± 17.3 |
| Duodenum | 23.7 ± 14.7 31.5 ± 16.1 44.5 ± 17.5 45.4 ± 16.7 |
| Colon | 47.3 ± 10.1 60.4 ± 12.1 67.0 ± 13.0 68.2 ± 12.0 |
| Intestine | 47.7 ± 13.1 56.1 ± 11.6 62.6 ± 11.0 64.0 ± 12.2 |
| Adrenal | 23.3 ± 13.8 30.7 ± 18.4 40.4 ± 17.7 41.1 ± 17.4 |
| Rectum | 18.6 ± 9.6 46.8 ± 15.0 49.3 ± 15.3 50.3 ± 14.5 |
| Bladder | 16.0 |  |  |

## Ablation study of Unified Anatomical Mapping (UAM) and Multi Scale Similarity (MSS) in MedLAM for organ detection: IoU score ↑ (mean ± std %) on the WORD dataset. " †" means the differences between UAM+MSS and using UAM or MSS alone are significant at p < 0.05.

|  | UAM |  | UAM | UAM | UAM | UAM | UAM | UAM | UAM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Organs | + | + | + | + |  |  |  |

## 57.1 ± 10.5 39.7 ± 27.4 76.0 ± 8.3 76.7 ± 7.9 71.5 ± 10.1 75.0 ± 09.1 78.5 ± 7.7 76.6 ± 7.7 73.0 ± 11.6 † ± 15.7 72.1 ± 16.0 69.1 ± 21.7 74.7 ± 15.2 74.4 ± 14.1 72.6 ± 12.9 70.9 ± 13.3 † ± 11.5 44.0 ± 18.8 34.1 ± 21.6 42.5 ± 17.4 45.0 ± 18.6 42.8 ± 16.2 44.1 ± 17.3 Duodenum 32.2 ± 10.5 31.4 ± 17.8 45.8 ± 16.2 35.8 ± 20.3 31.6 ± 18.2 39.3 ± 17.6 42.8 ± 15.4 51.0 ± 13.4 44.5 ± 17.5 † Colon 60.9 ± 13.4 42.8 ± 25.6 63.7 ± 12.9 65.3 ± 12.1 61.0 ± 11.1 65.2 ± 11.8 64.5 ± 11.7 63.2 ± 12.5 67.0 ± 13.0 † Intestine 58.7 ± 11.6 27.7 ± 21.1 63.1 ± 13.0 61.8 ± 16.8 62.0 ± 17.0 61.9 ± 17.6 65.2 ± 13.1 63.9 ± 14.0 62.6 ± 11.0 Adrenal 29.8 ± 17.0 10.5 ± 15.6 36.8 ± 16.1 30.5 ± 18.8 32.2 ± 19.7 35.0 ± 19.7 38.1 ± 15.7 38.6 ± 13.5 40.4 ± 17.7 † Rectum 34.6 ± 10.5 47.9 ± 18.2 49.1 ± 12.4 47.5 ± 11.6 32.1 ± 19.4 47.9 ± 12.7 51.8 ± 12.7 53.3 ± 13.7 49.3 ± 15.3 † Bladder 33.9 ± 15.2 45.8 ± 23.0 49.5 ± 18.1 55.3 ± 21.1 49.6 ± 20.1 52.3 ± 22.2 50.8 ± 20.4 55.4 ± 16.9 55.4 ± 16.9 † Head of Femur R 36.2 ± 10.9 55.3 ± 29.4 63.8 ± 13.3 70.9 ± 12.5 75.9 ± 13.7 74.0 ± 14.0 70.2 ± 14.2 68.3 ± 13.9 69.4 ± 14.4 † Average 39.2 ± 11.7 34.2 ± 21.9 52.8 ± 13.1 53.6 ± 15.0 50.6 ± 17.4 54.9 ± 15.8 56.5 ± 13.6 55.9 ± 13.2 56.6 ± 14.8 †

| Spleen 63.0 Kidney L 40.1 ± 7.7 49.3 ± 34.2 45.9 ± 11.4 39.9 ± 30.7 60.5 ± 10.4 58.9 ± 19.4 52.1 ± 23.4 54.5 ± 22.9 64.8 ± 16.4 63.7 ± 14.8 | 71.0 ± 15.9 † |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kidney R | 40.4 ± 9.3 | 40.6 ± 34.6 | 62.7 ± 12.1 68.2 ± 14.4 54.4 ± 27.8 73.0 ± 13.1 76.3 ± 8.9 | 70.6 ± 9.4 | 76.0 ± 13.8 † |
| Stomach | 38.7 ± 12.2 | 25.4 ± 21.9 | 47.4 ± 15.7 43.4 ± 15.6 46.4 ± 16.7 47.2 ± 17.6 45.9 ± 12.9 47.3 ± 14.8 | 49.1 ± 14.3 † |
| Gallbladder | 10.2 ± 12.9 | 4.1 ± 9.5 | 10.1 ± 9.5 | 7.4 ± 7.1 | 7.3 ± 8.1 | 9.3 ± 13.1 | 9.2 ± 6.8 | 8.9 ± 7.0 | 12.0 ± 11.0 |
| Esophagus | 22.0 ± 9.2 | 1.5 ± 3.4 | 41.0 ± 15.6 39.5 ± 18.4 46.4 ± 20.4 43.6 ± 19.2 44.2 ± 20.5 41.0 ± 18.5 | 44.2 ± 17.9 † |
| Pancreas 39.8 Head of Femur L 43.7 ± 10.8 42.9 ± 13.5 13.6 ± 15.5 71.9 ± 22.4 71.8 ± 8.5 | 80.2 ± 8.7 | 84.1 ± 8.9 | 83.1 ± 8.9 | 81.6 ± 9.1 | 77.9 ± 8.5 | 76.7 ± 16.7 † |

## Performance of MedLAM in localizing normal and abnormal organs in the FLARE2023 validation dataset. " †" means the differences between normal and abnormal organs are significant at p < 0.05.

| Organs | IoU ↑ (mean ± std %) | WD ↓ (mean ± std mm) |
| --- | --- | --- | --- | --- |
|  | Normal | Abnormal | Normal | Abnormal |
| Liver | 71.2 ± 11.1 | 69.2 ± 9.7 | 12.0 ± 5.8 | 12.0 ± 4.7 |
| Kidney L 68.0 ± 21.4 † | 55.8 ± 24.7 | 7.1 ± 6.6 † 14.9 ± 19.1 |
| Kidney R 74.9 ± 20.0 | 67.7 ± 19.7 | 4.7 ± 6.0 | 6.8 ± 6.1 |
| Pancreas | 35.9 ± 15.0 | 36.8 ± 7.1 | 17.9 ± 7.0 | 14.1 ± 2.9 |
| Stomach | 45.9 ± 15.6 64.5 ± 11.9 † 18.7 ± 7.9 12.3 ± 4.8 † |
| Average | 59.2 ± 16.6 | 58.8 ± 14.6 | 12.1 ± 6.7 | 12.0 ± 7.5 |

## Comparison of DSC scores ↑ (mean ± std%) for MedLSAM using different localization strategies on the StructSeg Head-and-Neck dataset: Whole-Patch Localization (WPL) and Sub-Patch Localization (SPL) with varying slice intervals n. " †" means the differences between SPL and WPL are significant at p < 0.05.

|  |  | SAM |  |  | MedSAM |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Organs |  | SPL |  | WPL |  | SPL |  | WPL |
|  | n = 6 mm | n = 15 mm n = 30 mm |  | n = 6 mm | n = 15 mm n = 30 mm |  |
| Brain Stem | 63.5 ± 6.3 † | 60.1 ± 6.7 | 51.5 ± 6.0 | 50.8 ± 6.2 | 73.3 ± 5.0 † | 71.9 ± 4.8 | 67.4 ± 4.2 | 66.6 ± 4.4 |
| Eye L | 64.5 ± 6.5 † | 61.2 ± 6.7 | 61.2 ± 6.7 | 61.2 ± 6.7 | 69.3 ± 5.9 † | 66.4 ± 5.7 | 66.4 ± 5.7 | 66.4 ± 5.7 |
| Eye R | 67.3 ± 5.8 † | 64.5 ± 6.6 | 64.5 ± 6.6 | 64.5 ± 6.6 | 69.4 ± 5.5 † | 67.8 ± 6.0 | 67.8 ± 6.0 | 67.8 ± 6.0 |
| Lens L | 15.9 ± 7.8 | 15.7 ± 7.7 | 15.7 ± 7.7 | 15.7 ± 7.7 | 16.0 ± 6.7 | 15.8 ± 6.7 | 15.8 ± 6.7 | 15.8 ± 6.7 |
| Lens R | 13.8 ± 8.8 | 14.1 ± 8.6 | 13.5 ± 8.7 | 13.5 ± 8.7 | 14.0 ± 5.5 | 14.0 ± 5.6 | 13.7 ± 5.5 | 13.7 ± 5.5 |
| Opt Nerve L | 23.7 ± 6.1 | 23.9 ± 5.9 | 23.7 ± 6.1 | 23.7 ± 6.1 | 23.5 ± 6.2 | 23.6 ± 6.2 | 23.5 ± 6.2 | 23.5 ± 6.2 |
| Opt Nerve R | 27.8 ± 10.2 27.8 ± 10.2 27.8 ± 10.2 27.8 ± 10.2 | 26.3 ± 6.6 | 26.3 ± 6.6 | 26.3 ± 6.6 | 26.3 ± 6.6 |
| Opt Chiasma | 11.4 ± 10.6 11.4 ± 10.6 11.4 ± 10.6 11.4 ± 10.6 14.4 ± 11.4 14.4 ± 11.4 14.4 ± 11.4 14.4 ± 11.4 |
| Temporal Lobes L 28.2 ± 15.2 21.7 ± 14.8 25.7 ± 13.4 25.7 ± 13.4 78.3 ± 3.5 † | 73.1 ± 3.5 | 71.0 ± 3.6 | 71.0 ± 3.6 |
| Temporal Lobes R 24.1 ± 17.4 † 18.2 ± 17.7 18.5 ± 16.4 18.5 ± 16.4 78.0 ± 4.3 † | 75.9 ± 3.1 | 71.0 ± 3.5 | 71.0 ± 3.5 |
| Pituitary | 12.5 ± 10.7 12.6 ± 10.7 12.6 ± 10.7 12.6 ± 10.7 | 10.2 ± 9.2 | 10.3 ± 9.4 | 10.3 ± 9.4 | 10.3 ± 9.4 |
| Parotid Gland L | 15.5 ± 11.9 † | 10.4 ± 9.6 | 5.5 ± 6.6 | 5.5 ± 6.6 | 59.6 ± 6.5 † | 56.4 ± 6.6 | 48.1 ± 7.3 | 48.1 ± 7.3 |
| Parotid Gland R | 17.2 ± 9.9 † | 13.1 ± 10.5 | 7.7 ± 7.7 | 7.7 ± 7.7 | 57.1 ± 6.8 † | 54.6 ± 6.8 | 45.3 ± 7.8 | 45.3 ± 7.8 |
| Inner Ear L | 40.4 ± 11.8 40.4 ± 11.8 40.4 ± 11.8 40.4 ± 11.8 | 42.3 ± 9.9 | 42.3 ± 9.9 | 42.3 ± 9.9 | 42.3 ± 9.9 |
| Inner Ear R | 48.9 ± 9.5 | 48.9 ± 9.5 | 48.9 ± 9.5 | 48.9 ± 9.5 | 45.9 ± 11.2 45.9 ± 11.2 45.9 ± 11.2 45.9 ± 11.2 |
| Mid Ear L | 64.6 ± 14.3 62.3 ± 14.7 62.3 ± 14.7 62.3 ± 14.7 59.7 ± 9.6 † | 55.8 ± 10.0 55.7 ± 10.0 55.7 ± 10.0 |
| Mid Ear R | 64.7 ± 13.1 62.4 ± 13.1 62.4 ± 13.0 62.4 ± 13.0 59.3 ± 11.2 † 53.6 ± 12.1 53.4 ± 11.9 53.4 ± 11.9 |
| TM Joint L | 38.3 ± 10.1 38.3 ± 10.1 38.3 ± 10.1 38.3 ± 10.1 39.0 ± 10.9 39.0 ± 10.9 39.0 ± 10.9 39.0 ± 10.9 |
| TM Joint R | 41.5 ± 10.0 41.5 ± 10.0 41.5 ± 10.0 41.5 ± 10.0 | 38.3 ± 9.5 | 38.3 ± 9.5 | 38.3 ± 9.5 | 38.3 ± 9.5 |
| Spinal Cord | 27.9 ± 8.3 † | 27.7 ± 8.2 | 27.8 ± 8.3 | 7.8 ± 2.9 | 34.7 ± 6.9 † | 34.7 ± 6.9 | 34.7 ± 6.9 | 11.7 ± 3.9 |
| Mandible L | 78.0 ± 4.9 † | 78.0 ± 5.2 | 68.0 ± 6.2 | 47.0 ± 5.3 | 66.7 ± 6.1 † | 66.7 ± 5.2 | 46.7 ± 5.8 | 22.9 ± 4.1 |
| Mandible R | 71.4 ± 4.0 † | 69.0 ± 4.4 | 58.5 ± 3.9 | 40.2 ± 4.6 | 66.0 ± 4.7 † | 64.7 ± 4.9 | 48.2 ± 5.0 | 25.9 ± 3.2 |
| Average | 39.1 ± 9.7 † | 37.4 ± 9.7 | 35.8 ± 9.2 | 33.1 ± 9.1 | 47.3 ± 7.4 † | 46.0 ± 7.4 | 43.0 ± 7.5 | 39.8 ± 7.2 |
| tion workload in medical image segmentation. |  |  |  |  |  |  |

## Comparison of DSC scores ↑ (mean ± std%) between MedLAM-generated bounding box prompts and manually annotated prompts on the Totalsegmentator dataset.

| Organs | MedLAM Manual Prompt | Organs | MedLAM Manual Prompt |
| --- | --- | --- | --- | --- | --- |
|  |  | SAM |  |  | SAM |
| Spleen | 71.2 ± 15.2 | 83.8 ± 12.3 | Iliac Vena Left | 43.9 ± 11.5 | 68.7 ± 5.0 |
| Kidney Right | 82.5 ± 7.0 | 90.3 ± 2.6 | Iliac Vena Right | 58.7 ± 11.4 | 68.5 ± 4.7 |
| Kidney Left | 80.6 ± 9.1 | 89.4 ± 2.3 | Small Bowel | 38.0 ± 13.9 | 60.2 ± 10.9 |
| Gallbladder | 56.5 ± 24.0 | 74.1 ± 21.2 | Duodenum | 33.4 ± 21.0 | 53.9 ± 11.7 |
| Liver | 70.5 ± 13.5 | 82.4 ± 7.9 | Colon | 17.9 ± 8.4 | 37.1 ± 4.9 |
| Stomach | 59.7 ± 15.3 | 77.6 ± 11.7 | Rib Left 1 | 64.3 ± 12.2 | 75.9 ± 6.4 |
| Aorta | 64.5 ± 17.6 | 75.5 ± 11.2 | Rib Left 2 | 68.6 ± 11.5 | 73.1 ± 9.1 |
| Inferior Vena Cava | 38.1 ± 13.6 | 77.4 ± 7.7 | Rib Left 3 | 57.8 ± 12.8 | 71.9 ± 8.6 |
| Portal Vein and Splenic vein 19.5 ± 17.9 | 32.8 ± 14.4 | Rib Left 4 | 56.1 ± 24.5 | 64.3 ± 18.8 |
| Pancreas | 39.6 ± 18.8 | 60.9 ± 13.5 | Rib Left 5 | 52.0 ± 27.3 | 65.9 ± 20.0 |
| Adrenal Gland Right | 29.8 ± 15.4 | 49.0 ± 11.6 | Rib Left 6 | 57.5 ± 15.6 | 74.6 ± 8.0 |
| Adrenal Gland Left | 46.1 ± 13.1 | 56.0 ± 10.6 | Rib Left 7 | 49.9 ± 21.6 | 73.0 ± 14.1 |
| Lung Upper Lobe Left | 61.2 ± 12.7 | 85.5 ± 10.1 | Rib Left 8 | 59.7 ± 16.8 | 72.5 ± 7.5 |
| Lung Lower Lobe Left | 76.6 ± 19.2 | 85.0 ± 13.1 | Rib Left 9 | 60.3 ± 18.9 | 72.8 ± 12.7 |
| Lung Upper Lobe Right | 64.9 ± 20.8 | 84.3 ± 18.7 | Rib Left 10 | 61.1 ± 13.8 | 73.9 ± 4.7 |
| Lung Middle Lobe Right | 67.8 ± 16.1 | 79.0 ± 12.1 | Rib Left 11 | 54.6 ± 9.9 | 72.4 ± 4.6 |
| Lung Lower Lobe Right | 72.0 ± 27.3 | 81.1 ± 20.2 | Rib Left 12 | 46.5 ± 14.1 | 66.5 ± 6.8 |
| Vertebrae L5 | 72.2 ± 16.2 | 78.1 ± 6.5 | Rib Right 1 | 53.6 ± 16.0 | 75.1 ± 9.1 |
| Vertebrae L4 | 70.6 ± 14.1 | 78.9 ± 7.7 | Rib Right 2 | 65.4 ± 14.3 | 76.1 ± 7.3 |
| Vertebrae L3 | 70.1 ± 8.7 | 81.6 ± 3.8 | Rib Right 3 | 48.2 ± 26.1 | 66.4 ± 17.1 |
| Vertebrae L2 | 68.1 ± 9.8 | 80.0 ± 5.8 | Rib Right 4 | 53.5 ± 19.8 | 68.2 ± 17.0 |
| Vertebrae L1 | 71.2 ± 12.2 | 82.5 ± 3.7 | Rib Right 5 | 51.3 ± 25.0 | 67.6 ± 20.8 |
| Vertebrae T12 | 59.8 ± 16.2 | 78.2 ± 13.2 | Rib Right 6 | 54.2 ± 16.3 | 76.7 ± 7.1 |
| Vertebrae T11 | 68.1 ± 17.5 | 76.0 ± 9.9 | Rib Right 7 | 57.2 ± 9.6 | 76.8 ± 5.5 |
| Vertebrae T10 | 64.9 ± 7.4 | 77.2 ± 4.8 | Rib Right 8 | 60.2 ± 22.4 | 72.5 ± 12.9 |
| Vertebrae T9 | 69.2 ± 12.8 | 75.8 ± 6.6 | Rib Right 9 | 51.5 ± 13.0 | 73.8 ± 6.3 |
| Vertebrae T8 | 56.5 ± 19.0 | 67.9 ± 16.8 | Rib Right 10 | 55.5 ± 8.9 | 74.7 ± 4.6 |
| Vertebrae T7 | 57.3 ± 10.2 | 71.7 ± 5.9 | Rib Right 11 | 50.7 ± 7.8 | 73.5 ± 4.8 |
| Vertebrae T6 | 51.6 ± 20.3 | 61.9 ± 16.1 | Rib Right 12 | 51.4 ± 14.4 | 66.6 ± 6.8 |
| Vertebrae T5 | 48.2 ± 13.0 | 63.5 ± 8.4 | Humerus Left | 70.4 ± 30.0 | 82.3 ± 21.7 |
| Vertebrae T4 | 43.5 ± 24.5 | 56.0 ± 17.3 | Humerus Right | 62.5 ± 34.8 | 75.4 ± 28.3 |
| Vertebrae T3 | 58.7 ± 12.5 | 69.2 ± 4.1 | Scapula Left | 67.7 ± 12.3 | 79.0 ± 8.2 |
| Vertebrae T2 | 62.9 ± 14.7 | 71.2 ± 12.3 | Scapula Right | 69.3 ± 18.0 | 80.4 ± 9.6 |
| Vertebrae T1 | 65.0 ± 8.8 | 78.0 ± 5.5 | Clavicula Left | 78.4 ± 11.2 | 89.1 ± 3.3 |
| Vertebrae C7 | 62.9 ± 16.8 | 73.6 ± 13.2 | Clavicula Right | 77.6 ± 15.3 | 86.5 ± 8.2 |
| Vertebrae C6 | 67.3 ± 15.3 | 73.7 ± 7.4 | Femur Left | 72.2 ± 14.3 | 90.4 ± 4.8 |
| Vertebrae C5 | 62.3 ± 21.5 | 68.3 ± 17.3 | Femur Right | 70.7 ± 19.5 | 87.1 ± 16.1 |
| Vertebrae C4 | 56.4 ± 15.4 | 71.0 ± 10.4 | Hip Left | 77.5 ± 9.9 | 88.9 ± 3.6 |
| Vertebrae C3 | 64.5 ± 9.6 | 74.1 ± 5.3 | Hip Right | 75.7 ± 8.4 | 89.7 ± 3.6 |
| Vertebrae C2 | 68.6 ± 10.4 | 80.6 ± 4.9 | Sacrum | 65.1 ± 12.9 | 82.8 ± 5.5 |
| Vertebrae C1 | 58.9 ± 11.3 | 69.7 ± 6.8 | Face | 52.9 ± 13.2 | 64.0 ± 11.1 |
| Esophagus | 48.5 ± 8.1 | 68.7 ± 5.8 | Gluteus Maximus Left 57.1 ± 15.6 | 70.5 ± 11.4 |
| Trachea | 77.5 ± 6.7 | 89.4 ± 3.9 | Gluteus Maximus Right 50.8 ± 20.7 | 68.8 ± 16.5 |
| Heart Myocardium | 31.0 ± 14.7 | 52.6 ± 10.0 | Gluteus Medius Left | 34.8 ± 18.3 | 51.2 ± 14.7 |
| Heart Atrium Left | 63.6 ± 17.2 | 80.1 ± 7.5 | Gluteus Medius Right | 31.9 ± 20.2 | 53.5 ± 12.0 |
| Heart Ventricle Left | 57.9 ± 15.3 | 68.5 ± 9.7 | Gluteus Minimus Left | 10.7 ± 17.9 | 23.8 ± 9.7 |
| Heart Atrium Right | 58.0 ± 11.8 | 79.5 ± 4.1 | Gluteus Minimus Right 12.7 ± 18.3 | 21.7 ± 12.1 |
| Heart Ventricle Right | 52.4 ± 10.5 | 74.9 ± 4.9 | Autochthon Left | 53.5 ± 9.4 | 78.2 ± 7.1 |
| Pulmonary Artery | 46.0 ± 24.2 | 54.8 ± 17.9 | Autochthon Right | 54.3 ± 11.4 | 77.3 ± 7.2 |
| Brain | 73.5 ± 12.8 | 81.1 ± 8.5 | Iliopsoas Left | 43.0 ± 14.7 | 64.2 ± 11.9 |
| Iliac Artery Left | 47.8 ± 13.1 | 67.4 ± 9.4 | Iliopsoas Right | 58.2 ± 15.2 | 70.7 ± 11.7 |
| Iliac Artery Right | 47.1 ± 13.0 | 66.0 ± 10.8 | Urinary Bladder | 78.5 ± 16.1 | 84.9 ± 8.0 |

### Formule


$$d ′ qs = (c s -c q ) • e.(1)$$

### Formule


$$d qs = r • tanh( p s -p q ).$$

### Formule


$$L MS E = ||d qs -d ′ qs || 2 . (3$$

### Formule


$$)$$

### Formule


$$′ i c ′ j$$

### Formule


$$f i c j = F i (c j ) and f ′ i c ′ j = F ′ i (c ′ j ).$$

### Formule


$$s(a, b) = a • b ||a|| 2 • ||b|| 2 . (4$$

### Formule


$$)$$

### Formule


$$Y i c j (c) =        1, if c = round( c ′ j 2 i ) 0, otherwise(5)$$

### Formule


$$L CE = i -Y i c j • log(S i c j ) -(1 -Y i ) • log(1 -S i c j ). (6)$$

### Formule


$$L S S L = L MS E + L CE .(7)$$

### Formule


$$ALE = 1 6 6 i=1 (x p,i -x gt,i ) 2 + (y p,i -y gt,i ) 2 + (z p,i -z gt,i ) 2$$

### Formule


$$WD = 1 6 |d p,i -d gt,i |,(9)$$

### Formule


$$IoU = V p ∩ V gt V p ∪ V gt ,(10)$$

### Formule


$$DS C( A, B) = 2|A ∩ B| | A| + |B| • 100% (11)$$

### Formule


$$+ + + + + F 2 + F 1 + F 0 F 2 F 1 F 0 F 1 + F 0 F 2 + F 0 F 2 + F 1 F 2 + F 1 + F 0 Liver$$
