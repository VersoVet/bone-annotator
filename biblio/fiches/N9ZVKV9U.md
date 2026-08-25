# MedZeroSeg: Zero-shot medical image segmentation via vision foundation models.

**Auteurs** : Ronghui Zhang, Min Huang, Rui Li
**Année** : 2026
**DOI** : 10.1371/journal.pone.0344978

## Résumé

A novel medical image segmentation framework, MedZeroSeg, is proposed to address key challenges in the field. Leveraging vision foundation models such as CLIP (Contrastive Language-Image Pre-training) and SAM (Segment Anything Model), it achieves zero-shot segmentation, accurately delineating previously unseen medical images without requiring additional labeled data. This significantly reduces reliance on large-scale annotated datasets. At its core, MedZeroSeg introduces a Dual-Path Feature Extraction Module that captures both fine anatomical details and global contextual information through the integration of local and global perception mechanisms, enhancing robustness against the complexity and variability inherent in medical imaging.Additionally, a Context-Enhanced Hard-Negative Contrast Loss is introduced to enhance contrastive learning by exploiting contextual cues and refining hard-negative sampling, leading to better representations and higher efficiency. The key innovation of M

## Méthodologie

{'study_design': "Comparaison expérimentale d'un framework de segmentation zero-shot (MedZeroSeg) intégrant CLIP et SAM, avec un Dual-Path Feature Extraction Module (DPFEM) et une fonction de perte Context-Enhanced Hard-Negative Contrast (CEHNC), évaluée sur trois jeux de données publics en conditions zero-shot et faiblement supervisées, avec études d'ablation", 'intervention': 'Application du framework MedZeroSeg (CLIP + SAM + DPFEM + CEHNC) pour générer des pseudo-masques de segmentation zero-shot via gScoreCAM après traitement par champ aléatoire conditionnel (CRF) guidé par le DPFEM', 'control': 'Modèles de référence pré-entraînés (BiomedCLIP, PMC-CLIP, CLIP) et fonctions de perte alternatives (InfoNCE, DCL, HN-NCE) ; comparaison également avec Grad-CAM comme technique alternative à gScoreCAM', 'primary_outcomes': ['Qualité de segmentation zero-shot et faiblement supervisée (Dice Similarity Coefficient, IoU, AUC)'], 'secondary_outcomes': ["Précision de récupération top-1 et top-2 (image-to-text et text-to-image) pour l'évaluation du fine-tuning de BiomedCLIP sur ROCO"], 'statistical_methods': ['Test t apparié (paired-samples t-test), seuil de significativité p < 0,05', 'Résultats rapportés en moyenne ± écart-type sur trois essais indépendants avec graines aléatoires différentes'], 'duration': None, 'setting': 'Expériences computationnelles menées sur GPU NVIDIA A100, implémentation PyTorch, sur trois jeux de données publics (ACDC, Synapse, COVID-QU-Ex) et le jeu ROCO pour la validation du fine-tuning de CLIP'}

## Résultats

{'quantitative': [{'outcome': 'Chest X-ray segmentation IoU (weakly supervised ResUNet vs. zero-shot)', 'value': '75.95 vs. 48.85', 'unit': 'IoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 7 (weakly supervised setting)', 'source_quote': 'the weakly supervised ResUNet substantially outperforms the zero-shot approach across all metrics (IoU: 75.95 vs. 48.85, DSC: 85.92 vs. 64.24)'}, {'outcome': 'Chest X-ray segmentation DSC (weakly supervised ResUNet vs. zero-shot)', 'value': '85.92 vs. 64.24', 'unit': 'DSC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 7 (weakly supervised setting)', 'source_quote': 'the weakly supervised ResUNet substantially outperforms the zero-shot approach across all metrics (IoU: 75.95 vs. 48.85, DSC: 85.92 vs. 64.24)'}, {'outcome': 'ACDC segmentation IoU (zero-shot Saliency Maps + DPFEM + CRF vs. weakly supervised ResUNet)', 'value': '57.52 vs. 40.99', 'unit': 'IoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 7 (weakly supervised setting)', 'source_quote': 'on ACDC, the zero-shot method achieves IoU of 57.52 vs. 40.99 for weakly supervised'}, {'outcome': 'Synapse segmentation IoU (zero-shot vs. weakly supervised ResUNet)', 'value': '49.91 vs. 41.55', 'unit': 'IoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 7 (weakly supervised setting)', 'source_quote': 'on Synapse, IoU of 49.91 vs. 41.55'}, {'outcome': 'Amélioration de la qualité de segmentation avec la méthode combinant BiomedCLIP et SAM (saliency map + SAM) en zero-shot', 'value': 'significatif', 'unit': 'p-value', 'confidence_interval': None, 'p_value': 'p < 0.05', 'effect_size': None, 'source_section': 'Results, paragraphe 5 (zero-shot segmentation task)', 'source_quote': 'the method combining BiomedCLIP and SAM exhibits significant superiority in all evaluation metrics, significantly improving segmentation quality (p < 0.05)'}, {'outcome': "Taille de l'échantillon de test ACDC", 'value': '200', 'unit': 'n (cas de test)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2 (Table 2)', 'source_quote': 'Test set sizes: ACDC (n = 200), Synapse (n = 30), Chest X-ray/COVID-QU-Ex (n = 200).'}, {'outcome': "Taille de l'échantillon de test Synapse", 'value': '30', 'unit': 'n (cas de test)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2 (Table 2)', 'source_quote': 'Test set sizes: ACDC (n = 200), Synapse (n = 30), Chest X-ray/COVID-QU-Ex (n = 200).'}, {'outcome': "Taille de l'échantillon de test Chest X-ray/COVID-QU-Ex", 'value': '200', 'unit': 'n (cas de test)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2 (Table 2)', 'source_quote': 'Test set sizes: ACDC (n = 200), Synapse (n = 30), Chest X-ray/COVID-QU-Ex (n = 200).'}], 'qualitative_findings': ['Le modèle BiomedCLIP fine-tuné avec la fonction de perte CEHNC surpasse significativement les autres fonctions de perte disponibles ainsi que tous les modèles pré-entraînés de référence (test de McNemar apparié).', "Les indices de bounding box générés à l'aide de gScoreCAM sont significativement meilleurs que ceux de la méthode Grad-CAM, suggérant que gScoreCAM améliore plus efficacement la précision de segmentation.", "L'amélioration substantielle des performances de gScoreCAM par rapport à Grad-CAM s'explique par des mécanismes fondamentalement différents : Grad-CAM repose sur la rétropropagation de gradient pouvant produire des cartes de saillance bruitées, tandis que gScoreCAM évalue directement l'importance des canaux en fonction des motifs d'activation, offrant une localisation plus précise.", 'La méthode proposée avec gScoreCAM surpasse systématiquement les autres approches dans toutes les modalités.', "Le fine-tuning de BiomedCLIP avec la fonction de perte CEHNC proposée confirme sa performance supérieure sur plusieurs types de tâches et modalités d'image différentes, avec une amélioration globale de la qualité de segmentation.", "La méthode combinant BiomedCLIP et SAM (saliency map + SAM) montre une supériorité significative sur toutes les métriques d'évaluation par rapport à la génération d'étiquettes initiales basée uniquement sur la carte de saillance gScoreCAM.", "Pour le jeu de données Chest X-ray, le ResUNet supervisé faiblement surpasse substantiellement l'approche zero-shot sur toutes les métriques.", "Pour ACDC et Synapse, la méthode zero-shot (Saliency Maps + DPFEM + CRF) atteint des performances compétitives voire supérieures à celles du ResUNet supervisé faiblement, en termes d'IoU et de DSC.", 'Les marqueurs de significativité statistique du Tableau 3 indiquent des comparaisons par rapport à la référence ResUNet entièrement supervisée, et non par rapport à la méthode faiblement supervisée.', 'MedZeroSeg surpasse la méthode entièrement supervisée basée sur ResUNet dans les tâches de segmentation ACDC et Synapse.', "La méthode entièrement supervisée reste supérieure à la méthode zero-shot pour la tâche de segmentation des radiographies pulmonaires, en termes d'IoU, de DSC et d'AUC, suggérant qu'une quantité suffisante de données étiquetées reste un facteur clé de précision dans certains scénarios d'application.", "MedZeroSeg atteint les valeurs les plus élevées d'IoU, de DSC et d'AUC parmi les trois méthodes comparées sur le jeu de données de radiographie thoracique, confirmant son avantage en segmentation zero-shot des radiographies pulmonaires.", "L'inclusion de la méthode MIS-Net (référence faiblement supervisée basée sur SAM) dans le Tableau 2 permet de démontrer clairement les améliorations apportées par la méthode proposée."], 'main_findings': ['La fonction de perte CEHNC améliore significativement la précision de récupération cross-modale (text-to-image et image-to-text) de BiomedCLIP par rapport aux autres fonctions de perte et aux modèles pré-entraînés de référence (CLIP, PMC-CLIP, BiomedCLIP original).', 'gScoreCAM génère des indices de bounding box de meilleure qualité que Grad-CAM pour guider SAM, améliorant ainsi la précision de segmentation.', "La combinaison de la carte de saillance gScoreCAM avec des pseudo-masques générés par SAM ('saliency map + SAM') améliore significativement (p < 0.05) la qualité de segmentation zero-shot par rapport à l'utilisation de la carte de saillance seule.", 'Les performances relatives entre méthodes zero-shot et faiblement supervisées dépendent du jeu de données et de la métrique : le ResUNet faiblement supervisé domine nettement sur Chest X-ray, alors que la méthode zero-shot est compétitive voire supérieure sur ACDC et Synapse.', "MedZeroSeg (zero-shot) surpasse même le ResUNet entièrement supervisé sur les tâches ACDC et Synapse, démontrant qu'une segmentation de haute qualité est possible sans données annotées volumineuses dans certains contextes.", "Sur la tâche de segmentation de radiographies pulmonaires, la méthode entièrement supervisée reste supérieure à MedZeroSeg, soulignant l'importance des données étiquetées pour certaines applications."]}

## Conclusions

MedZeroSeg is a zero-shot medical image segmentation framework that leverages the complementary strengths of CLIP and SAM, achieving accurate segmentation across multiple modalities without any domain-specific fine-tuning, effectively reducing reliance on large-scale annotated datasets The DPFEM (dual-path refinement structure) captures both local anatomical details and global contextual information The novel CEHNC Loss enhances contrastive learning through context-aware hard negative selection, enabling more robust and efficient feature alignment between image and text modalities Experimental results on diverse public datasets, including ultrasound, MRI, and X-ray, demonstrate that MedZeroSeg delivers competitive segmentation accuracy and strong cross-domain generalization MedZeroSeg provides an efficient, extensible, and annotation-free solution for medical image segmentation, contributing to the broader adoption of foundation models in clinical imaging analysis

## COVID-QU-Ex dataset. URLs: https://www. kaggle.com/datasets/anasmohammedtahir/ covidqu. This work was partially supported by the Research on Multi-Instrument Automatic Reading Method Based on Character Recognition and Key Point Detection for the Fujian Natural Science Foundation General Project under the Grant No. 2025J011098 (received by MH), the Education and Research Project for Young and Middle-aged Teachers by the Department of Education of Fujian Province under the Grant No. JAT200983 (received by RZ), the Fujian Jiangxia University Research Talent Cultivation Project under the Grant No. JXZ2019012 (received by MH), and the Project of the Fujian Provincial Department of Science and Technology on the Research of Cavity Decay OTDR Distributed Sensing Technology and Current Detection Application under the Grant No. 2021J011224 (received by MH).

| Funding: |
| --- |

## Results are reported as mean ± standard deviation over three independent runs. The proposed CEHNC loss achieves the best performance across all metrics. Evaluation is performed on the ROCO dataset with 1,000 image-text pairs in the test set.

| Model | Version | img → txt (%) |  | txt → img (%) |  |
| --- | --- | --- | --- | --- | --- |
|  |  | top-1 | top-2 | top-1 | top-2 |
| BiomedCLIP | Pre-trained | 81.37 ± 0.22 | 92.22 ± 0.29 | 80.93 ± 0.21 | 91.74 ± 0.25 |
|  | InfoNCE | 83.74 ± 0.28 | 93.90 ± 0.30 | 85.26 ± 0.23 | 94.44 ± 0.27 |
|  | DCL | 84.07 ± 0.20 | 94.11 ± 0.26 | 85.42 ± 0.24 | 94.54 ± 0.22 |
|  | HN-NCE | 83.96 ± 0.27 | 94.03 ± 0.21 | 85.33 ± 0.29 | 94.55 ± 0.28 |
|  | CEHNC (Ours) | 84.66 ± 0.25 | 94.93 ± 0.23 | 86.12 ± 0.26 | 95.29 ± 0.31 |
| CLIP | Pretrained | 26.35 ± 0.20 | 41.37 ± 0.30 | 25.84 ± 0.15 | 40.68 ± 0.22 |
| PMC-CLIP | Pretrained | 75.19 ± 0.35 | 86.91 ± 0.18 | 76.43 ± 0.31 | 87.80 ± 0.24 |
| https://doi.org/10.1371/journal.pone.0344978.t001 |  |  |  |  |

## Table 2 . Comparison of different models and CAM techniques with standard deviation and training time.

| Modality | Model | CAM | IoU (%) | DSC (%) | AUC (%) | Time (min) |
| --- | --- | --- | --- | --- | --- | --- |
| ACDC | BiomedCLIP | gScoreCAM | 55.67 ± 6.23 | 65.38 ± 5.42 | 77.86 ± 5.13 | 18.3 |
|  |  | Grad-CAM | 17.42 ± 7.31 | 23.14 ± 7.65 | 59.54 ± 7.12 | 16.8 |
|  | MIS-Net | gScoreCAM | 56.23 ± 6.01 | 66.12 ± 7.21 | 77.98 ± 6.12 | 19.1 |
|  |  | Grad-CAM | 19.01 ± 8.23 | 23.89 ± 6.78 | 60.54 ± 5.89 | 17.6 |
|  | Ours | gScoreCAM | 57.31 ± 5.87 | 67.07 ± 7.95 | 78.65 ± 6.01 | 18.7 |
|  |  | Grad-CAM | 20.07 ± 8.54 | 24.72 ± 6.38 | 61.87 ± 5.23 | 17.1 |
| Synapse | BiomedCLIP | gScoreCAM | 48.04 ± 8.14 | 64.28 ± 5.64 | 78.64 ± 5.78 | 21.7 |
|  |  | Grad-CAM | 25.44 ± 5.29 | 32.17 ± 6.41 | 75.46 ± 8.34 | 19.5 |
|  | MIS-Net | gScoreCAM | 49.21 ± 5.56 | 65.34 ± 6.54 | 79.87 ± 7.65 | 22.8 |
|  |  | Grad-CAM | 26.14 ± 6.32 | 32.45 ± 6.34 | 76.45 ± 5.21 | 20.1 |
|  | Ours | gScoreCAM | 50.30 ± 5.45 | 65.98 ± 6.72 | 80.55 ± 7.92 | 22.5 |
|  |  | Grad-CAM | 27.05 ± 6.56 | 32.88 ± 6.17 | 77.79 ± 5.01 | 19.9 |
| Chest X-ray | BiomedCLIP | gScoreCAM | 46.51 ± 6.78 | 62.19 ± 7.19 | 76.95 ± 5.34 | 15.2 |
|  |  | Grad-CAM | 21.39 ± 7.83 | 35.26 ± 7.49 | 59.42 ± 6.21 | 14.0 |
|  | MIS-Net | gScoreCAM | 48.21 ± 7.45 | 63.21 ± 5.98 | 76.98 ± 6.75 | 15.8 |
|  |  | Grad-CAM | 25.14 ± 6.12 | 37.76 ± 7.21 | 61.02 ± 5.45 | 15.3 |
|  | Ours | gScoreCAM | 49.14 ± 7.32 | 64.17 ± 5.23 | 77.57 ± 6.89 | 15.6 |
|  |  | Grad-CAM | 26.02 ± 5.45 | 38.89 ± 7.62 | 62.32 ± 5.18 | 15.1 |

## Results are reported as mean ± standard deviation over three independent runs. Statistical significance (two-tailed paired t-test) is assessed against the Full supervision-ResUNet on the same test set. Test set sizes: ACDC (n = 200), Synapse (n = 30), Chest X-ray/COVID-QU-Ex (n = 200). Significance levels: *** p < 0.001, ** p < 0.01, * p < 0.05. Note: The statistical significance markers indicate comparisons against the fully supervised baseline, not against the weakly supervised method.

| Modality | Model | IoU (%) | DSC (%) | AUC (%) |
| --- | --- | --- | --- | --- |
| ACDC | Saliency Maps + CRF | 39.78 ± 6.45 | 51.29 ± 8.13 | 73.28 ± 5.67 |
|  | Saliency Maps + DPFEM + CRF | 57.52 ± | 67.49 ± 5.02 * | 78.99 ± 6.15 * |
|  |  | 7.91 *** |  |  |
|  | Weak supervision-ResUNet | 40.99 ± 6.87 | 58.31 ± 6.71 | 81.07 ± 6.98 |
|  | Full supervision-ResUNet | 52.88 ± 7.39 | 67.06 ± 6.48 | 84.38 ± 7.65 |
| Synapse | Saliency Maps + CRF | 38.71 ± 5.37 | 52.84 ± 5.87 | 75.52 ± 6.39 |
|  | Saliency Maps + DPFEM + CRF | 49.91 ± 6.18 * | 66.48 ± 5.54 * | 81.03 ± 7.16 * |
|  | Weak supervision-ResUNet | 41.55 ± 7.56 | 58.56 ± 6.97 | 78.10 ± 6.54 |
|  | Full supervision-ResUNet | 45.62 ± 6.52 | 62.36 ± 6.81 | 79.61 ± 5.98 |
| Chest X-ray | Saliency Maps + CRF | 34.61 ± 6.98 | 49.21 ± 7.84 | 71.66 ± 6.86 |
|  | Saliency Maps + DPFEM + CRF | 48.85 ± | 64.24 ± | 78.29 ± |
|  |  | 7.82 *** | 7.87 *** | 5.82 *** |
|  | Weak supervision-ResUNet | 75.95 ± 7.43 | 85.92 ± 7.02 | 90.59 ± 5.84 |
|  | Full supervision-ResUNet | 94.89 ± 5.75 | 97.31 ± 5.53 | 98.22 ± 5.27 |

### Formule


$$L CEHNC = L img→txt + L txt→img ,(1)$$

### Formule


$$L img→txt = - 1 M M ∑ n=1 log ( e γ(z ⊤ n sn) e γ(z ⊤ n sn) + ∑ m̸ =n e γ(z ⊤ n sm) • ω 1 (z n , s m ) ) ,(2)$$

### Formule


$$L txt→img = - 1 M M ∑ n=1 log ( e γ(s ⊤ n zn) e γ(s ⊤ n zn) + ∑ m̸ =n e γ(s ⊤ n zm) • ω 2 (s n , z m ) ) . (3$$

### Formule


$$)$$

### Formule


$$ω 1 (z, s) = exp ( -λ 1 • ∥z -s∥ 2 ) ,(4)$$

### Formule


$$ω 2 (s, z) = exp ( -λ 2 • ∥s -z∥ 2 ) . (5$$

### Formule


$$)$$

### Formule


$$F 0 = Conv(I),(6)$$

### Formule


$$F local = SiLU(Pointwise(Depthwise(F 0 )))(7)$$

### Formule


$$F global = SHSA(F 0 ),(8)$$

### Formule


$$F fused = Conv([F local , F global ]),(9)$$

### Formule


$$IoU = TP TP + FP + FN , (10$$

### Formule


$$) DSC = 2 × TP 2 × TP + FP + FN , (11$$

### Formule


$$) AUC = ∫ 1 0 TPR(FPR) d(FPR). (12$$

### Formule


$$)$$
