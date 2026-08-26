# MedZeroSeg: Zero-shot medical image segmentation via vision foundation models.

**Auteurs** : Ronghui Zhang, Min Huang, Rui Li
**Année** : 2026
**DOI** : 10.1371/journal.pone.0344978

## Résumé

A novel medical image segmentation framework, MedZeroSeg, is proposed to address key challenges in the field. Leveraging vision foundation models such as CLIP (Contrastive Language-Image Pre-training) and SAM (Segment Anything Model), it achieves zero-shot segmentation, accurately delineating previously unseen medical images without requiring additional labeled data. This significantly reduces reliance on large-scale annotated datasets. At its core, MedZeroSeg introduces a Dual-Path Feature Extraction Module that captures both fine anatomical details and global contextual information through the integration of local and global perception mechanisms, enhancing robustness against the complexity and variability inherent in medical imaging.Additionally, a Context-Enhanced Hard-Negative Contrast Loss is introduced to enhance contrastive learning by exploiting contextual cues and refining hard-negative sampling, leading to better representations and higher efficiency. The key innovation of M

## Méthodologie

{'study_design': "Framework de segmentation zero-shot combinant CLIP et SAM, avec un Dual-Path Feature Extraction Module (DPFEM) et une fonction de perte Context-Enhanced Hard-Negative Contrast (CEHNC); évaluation comparative sur trois datasets publics avec inférence 2D slice-wise pour les données 3D (ACDC, Synapse) en raison de la contrainte d'entrée 2D de CLIP et SAM pré-entraînés", 'intervention': 'Application de MedZeroSeg (approche zero-shot et faiblement supervisée basée sur gScoreCAM après traitement par champ aléatoire conditionnel guidé par DPFEM) comparée à des approches de référence (BiomedCLIP, PMC-CLIP, CLIP pré-entraînés) et à différentes fonctions de perte (InfoNCE, DCL, HN-NCE, CEHNC)', 'control': 'Modèles de base pré-entraînés (BiomedCLIP, PMC-CLIP, CLIP) et fonctions de perte alternatives (InfoNCE, DCL, HN-NCE) comme comparateurs', 'primary_outcomes': ['Intersection over Union (IoU)', 'Dice Similarity Coefficient (DSC)', 'Area Under the Curve (AUC) de la courbe ROC'], 'secondary_outcomes': ['Précision de récupération top-1 et top-2 (image-to-text et text-to-image) sur le dataset ROCO pour évaluer le fine-tuning de BiomedCLIP'], 'statistical_methods': ['Test t apparié (paired-samples t-test), seuil de significativité p < 0.05', 'Résultats rapportés en moyenne ± écart-type sur trois runs indépendants avec graines aléatoires différentes'], 'duration': None, 'setting': 'Implémentation en PyTorch, entraînement sur GPU NVIDIA A100'}

## Résultats

{'quantitative': [{'outcome': 'BiomedCLIP fine-tuned with CEHNC loss vs. other loss functions and pre-trained baselines (CLIP, PMC-CLIP, BiomedCLIP) on cross-modal retrieval (text-to-image, image-to-text) on ROCO dataset', 'value': 'Significantly outperforms all compared methods', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'Through a paired McNemar statistical test, we found that the BiomedCLIP model fine-tuned using our CEHNC loss function significantly outperforms the other available loss functions and all pre-trained baseline models.'}, {'outcome': 'Test set sizes used for evaluation', 'value': 'ACDC (n = 200), Synapse (n = 30), Chest X-ray/COVID-QU-Ex (n = 200)', 'unit': 'n samples', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': 'Test set sizes: ACDC (n = 200), Synapse (n = 30), Chest X-ray/COVID-QU-Ex (n = 200).'}, {'outcome': 'Results reporting format across three independent runs', 'value': 'mean ± standard deviation', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': 'Results are reported as mean ± standard deviation over three independent runs.'}, {'outcome': 'gScoreCAM vs Grad-CAM for SAM bounding box cue generation', 'value': 'gScoreCAM significantly better than Grad-CAM', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'The experimental results show that the bounding box cues generated using gScoreCAM are significantly better than those of the Grad-CAM method, suggesting that gScoreCAM is able to improve segmentation accuracy more effectively.'}, {'outcome': "Zero-shot segmentation: 'saliency map + SAM' vs 'saliency map' alone", 'value': 'Significant superiority in all evaluation metrics', 'unit': None, 'confidence_interval': None, 'p_value': 'p < 0.05', 'effect_size': None, 'source_section': 'Results, paragraphe 5', 'source_quote': 'The experimental results show that the method combining BiomedCLIP and SAM exhibits significant superiority in all evaluation metrics, significantly improving segmentation quality (p < 0.05).'}, {'outcome': 'Chest X-ray dataset: weakly supervised ResUNet IoU vs zero-shot method IoU', 'value': '75.95 vs. 48.85', 'unit': 'IoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 6', 'source_quote': 'For the Chest X-ray dataset, the weakly supervised ResUNet substantially outperforms the zero-shot approach across all metrics (IoU: 75.95 vs. 48.85, DSC: 85.92 vs. 64.24).'}, {'outcome': 'Chest X-ray dataset: weakly supervised ResUNet DSC vs zero-shot method DSC', 'value': '85.92 vs. 64.24', 'unit': 'DSC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 6', 'source_quote': 'For the Chest X-ray dataset, the weakly supervised ResUNet substantially outperforms the zero-shot approach across all metrics (IoU: 75.95 vs. 48.85, DSC: 85.92 vs. 64.24).'}, {'outcome': 'ACDC dataset: zero-shot method (Saliency Maps + DPFEM + CRF) IoU vs weakly supervised ResUNet IoU', 'value': '57.52 vs. 40.99', 'unit': 'IoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 6', 'source_quote': 'Specifically, on ACDC, the zero-shot method achieves IoU of 57.52 vs. 40.99 for weakly supervised, and on Synapse, IoU of 49.91 vs. 41.55.'}, {'outcome': 'Synapse dataset: zero-shot method IoU vs weakly supervised ResUNet IoU', 'value': '49.91 vs. 41.55', 'unit': 'IoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 6', 'source_quote': 'Specifically, on ACDC, the zero-shot method achieves IoU of 57.52 vs. 40.99 for weakly supervised, and on Synapse, IoU of 49.91 vs. 41.55.'}, {'outcome': 'MedZeroSeg (zero-shot) vs fully-supervised ResUNet on ACDC and Synapse tasks', 'value': 'MedZeroSeg outperforms fully supervised ResUNet', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 7', 'source_quote': 'Specifically, MedZeroSeg outperforms the ResUNet-based fully supervised method in the ACDC and Synapse segmentation tasks.'}, {'outcome': 'Fully-supervised method vs zero-shot method on lung radiograph (chest X-ray) segmentation', 'value': 'Fully-supervised outperforms zero-shot on IoU, DSC, AUC', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 8', 'source_quote': 'However, the fully-supervised method still performs well in the lung radiograph segmentation task, outperforming the zero-shot method both in terms of evaluation metrics such as IoU, DSC, and AUC.'}, {'outcome': 'MedZeroSeg vs other methods on chest X-ray dataset (Table 2)', 'value': 'Highest IoU, DSC, and AUC among three methods', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 8', 'source_quote': 'These qualitative findings are consistent with the quantitative results in Table 2, where MedZeroSeg achieves the highest IoU, DSC, and AUC among the three methods on the chest X-ray dataset, further demonstrating its advantage in zero-shot chest X-ray segmentation.'}], 'qualitative_findings': ['gScoreCAM provides more focused localization than Grad-CAM because it directly evaluates channel importance based on activation patterns, whereas Grad-CAM relies on gradient backpropagation which can produce noisy saliency maps.', 'Fine-tuning BiomedCLIP with the CEHNC loss function improves overall segmentation quality across multiple task types and image modalities.', 'Combining gScoreCAM saliency maps with SAM-generated pseudo-masks captures critical image regions more efficiently than saliency maps alone.', 'The performance comparison between zero-shot and weakly supervised methods shows dataset- and metric-dependent trends.', 'MedZeroSeg qualitative results show effective highlighting of pathological opacities while suppressing background structures in chest X-ray images.', 'Statistical significance markers in Table 3 indicate comparisons against the fully supervised ResUNet baseline, not against the weakly supervised method.'], 'main_findings': ['BiomedCLIP fine-tuned with the proposed CEHNC loss function significantly outperforms other loss functions and pre-trained baseline models (CLIP, PMC-CLIP, BiomedCLIP) in cross-modal retrieval on ROCO.', 'gScoreCAM generates significantly better SAM bounding box cues than Grad-CAM, improving zero-shot segmentation accuracy.', 'Combining BiomedCLIP-based saliency maps with SAM pseudo-masks significantly improves zero-shot segmentation quality over saliency maps alone (p < 0.05).', "MedZeroSeg's zero-shot segmentation outperforms the fully-supervised ResUNet baseline on ACDC and Synapse tasks, but underperforms it on chest X-ray/lung radiograph segmentation, where sufficient labeled data remains advantageous.", 'Weakly supervised ResUNet substantially outperforms the zero-shot approach on the Chest X-ray dataset, while the zero-shot method is competitive or superior to weakly supervised ResUNet on ACDC and Synapse.']}

## Conclusions

MedZeroSeg est un framework de segmentation d'images médicales zero-shot exploitant les forces complémentaires de CLIP et SAM, sans fine-tuning spécifique au domaine MedZeroSeg atteint une segmentation précise sur plusieurs modalités, réduisant efficacement la dépendance aux jeux de données annotés à grande échelle Le design intègre un DPFEM (dual-path refinement structure) pour capturer les détails anatomiques locaux et le contexte global, ainsi qu'une nouvelle CEHNC Loss pour améliorer l'apprentissage contrastif via une sélection contextuelle de négatifs difficiles Les résultats expérimentaux sur des jeux de données publics diversifiés (ultrasound, MRI, X-ray) démontrent que MedZeroSeg délivre une précision de segmentation compétitive et une forte généralisation cross-domaine MedZeroSeg constitue une solution efficace, extensible et sans annotation pour la segmentation d'images médicales, contribuant à l'adoption plus large des modèles de fondation en analyse d'imagerie clinique

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
