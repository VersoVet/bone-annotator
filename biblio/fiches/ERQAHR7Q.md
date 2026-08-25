# Explainable opportunistic osteoporosis screening from chest X-rays: a retrospective comparison of foundation models

**Auteurs** : Jae-Won Kim, Sangmin Kwak, Hyeokjong Lee, Jooyoung Chang, Sang Min Park
**Année** : 2025
**DOI** : 10.1007/s00198-025-07727-3

## Résumé

We evaluated foundation models for opportunistic osteoporosis screening from chest X-rays using a novel explainability framework. DINOv2 with low-rank adaptation achieved the best performance (AUC 0.93) while demonstrating clear clinical reasoning. Our findings highlight that explainability should be prioritized alongside accuracy in medical AI, enhancing trust in clinical deployment. Purpose Deep learning models show promise for opportunistic osteoporosis screening from chest X-rays but have traditionally relied on convolutional neural networks with limited explainability. This study introduces a quantitative framework for explainability evaluation and systematically compares diverse foundation models to identify an optimal balance between performance and explainability. Methods In this retrospective study, a retrospective dataset comprising 21,031 chest X-rays paired with bone mineral density scores from 14,502 female patients at Seoul National University Hospital was used. Twelve foundation model variantscombinations of natural-and medical-domain models fine-tuned using various strategies-were trained to classify osteoporosis status (normal, osteopenia, or osteoporosis). Foundation models were evaluated based on predictive performance (AUC, accuracy, sensitivity, and specificity) and explainability, assessed through occlusion analysis (AUC change after bone perturbation, bone ) and saliency-map analysis (overlap between bone regions and saliency maps, IoU bone ). Results DINOv2, fine-tuned with low-rank adaptation, achieved the highest predictive performance (AUC of 0.93; 95% CI, 0.92-0.94) and demonstrated robust explainability by focusing on clinically relevant bone structures, such as the spine and ribs. In osteoporosis screening from chest X-rays, statistical analysis showed that medical foundation models did not consistently outperform natural-domain models, and higher performance did not always correlate with better explainability. Conclusion Our findings underscore the necessity of incorporating explainability as a key criterion when selecting deep learning models for opportunistic osteoporosis screening. Furthermore, the proposed framework can be readily extended to other medical tasks, fostering the development of more trustworthy and interpretable AI-assisted screening tools.

## Méthodologie

{'study_design': 'Étude rétrospective monocentrique comparant douze variantes de modèles de fondation (combinaisons de modèles de domaine naturel et médical, fine-tunés selon diverses stratégies) pour classifier le statut ostéoporotique (normal, ostéopénie, ostéoporose) à partir de radiographies thoraciques appariées à des mesures DXA', 'intervention': 'Fine-tuning de modèles de fondation (DINOv2, OpenCLIP, CheXagent, RAD-DINO, etc.) selon trois méthodes: évaluation linéaire (encodeur gelé), fine-tuning partiel (dernier bloc transformer), et adaptation à faible rang (LoRA, rang 8)', 'control': None, 'primary_outcomes': ['AUC', 'Accuracy', 'Sensibilité', 'Spécificité'], 'secondary_outcomes': ["Explicabilité via analyse d'occlusion (changement d'AUC après perturbation osseuse, ∆AUC_bone)", 'Explicabilité via analyse de carte de saillance (chevauchement entre régions osseuses et cartes de saillance, IoU_bone)'], 'statistical_methods': ["Calcul d'intervalles de confiance à 95% pour l'AUC", "Analyse de corrélation entre AUC et métriques d'explicabilité", 'Comparaisons statistiques entre modèles (tests de significativité)'], 'duration': None, 'setting': 'Health Promotion Center, Seoul National University Hospital'}

## Résultats

{'quantitative': [{'outcome': 'AUC de DINOv2 fine-tuné avec LoRA', 'value': '0.93', 'unit': 'AUC', 'confidence_interval': '95% CI, 0.92-0.94', 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'DINOv2, fine-tuned with low-rank adaptation, achieved the highest predictive performance (AUC of 0.93; 95% CI, 0.92-0.94) and demonstrated robust explainability by focusing on clinically relevant bone structures, such as the spine and ribs.'}, {'outcome': 'AUC de CheXagent/partial fine-tuning et RAD-DINO/LoRA', 'value': '0.90', 'unit': 'AUC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'For instance, mid-tier models such as CheXagent/partial fine-tuning and RAD-DINO/LoRA achieved competitive predictive performance (both AUC = 0.90, ranking fifth and sixth, respectively), yet their explainability metrics were weaker'}, {'outcome': 'AUC de DINOv2/linear', 'value': '0.77', 'unit': 'AUC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'DINOv2/linear exhibited the highest IoU All bones score and primarily focused on the spine and ribs, yet its predictive performance was suboptimal (AUC = 0.77).'}], 'qualitative_findings': ['Les modèles de fondation médicaux (ex. CheXagent, RAD-DINO) ne surpassent pas systématiquement les modèles de domaine naturel (ex. DINOv2, OpenCLIP) pour cette tâche', "Les régions osseuses les plus influentes identifiées par l'analyse d'explicabilité sont la colonne vertébrale et les côtes", "Le fine-tuning (LoRA ou partiel) surpasse systématiquement l'évaluation linéaire, quel que soit le modèle de fondation"], 'main_findings': ['DINOv2 fine-tuné avec LoRA obtient la meilleure performance prédictive (AUC=0.93) tout en démontrant un raisonnement clinique clair centré sur les structures osseuses pertinentes', "Une performance élevée ne garantit pas une bonne explicabilité, et inversement : aucune corrélation significative n'a été observée entre l'AUC et l'IoU_All bones", "Les modèles médicaux spécialisés n'apportent pas d'avantage constant par rapport aux modèles de domaine naturel, remettant en question la nécessité de développer des modèles de fondation médicaux spécifiques pour cette tâche"]}

## Conclusions

DINOv2/LoRA est identifié comme le modèle optimal, offrant un équilibre entre forte performance prédictive et explicabilité claire centrée sur les structures osseuses L'explicabilité doit être considérée comme un critère clé, au même titre que la performance, lors de la sélection de modèles de deep learning pour le dépistage opportuniste de l'ostéoporose Le cadre proposé est extensible à d'autres tâches médicales impliquant des structures anatomiques bien définies, favorisant le développement d'outils d'IA plus fiables et interprétables

## Table 1

| Demographic characteristics of the datasets | Training set | Validation set | Test set | Overall |
| --- | --- | --- | --- | --- |
| Participant | 10,152 | 1450 | 2900 | 14,502 |
| Chest radiograph images | 14,824 | 2044 | 4163 | 21,031 |
| Age (years), μ ± σ | 55.97 ± 9.73 | 55.81 ± 9.81 | 56.06 ± 9.51 | 55.97 ± 9.69 |
| BMD (g/cm 2 ), μ ± σ |  |  |  |  |
| L 1 -L 4 | 1.08 ± 0.17 | 1.08 ± 0.17 | 1.08 ± 0.17 | 1.08 ± 0.17 |
| Femur neck | 0.85 ± 0.12 | 0.85 ± 0.13 | 0.85 ± 0.13 | 0.85 ± 0.12 |
| T-score, μ ± σ |  |  |  |  |
| L 1 -L 4 | -0.36 ± 1.35 | -0.33 ± 1.35 | -0.34 ± 1.37 | -0.35 ± 1.36 |
| Femur neck | -0.43 ± 1.03 | -0.45 ± 1.04 | -0.43 ± 1.04 | -0.43 ± 1.03 |
| T-score categories, n (%) |  |  |  |  |
| Normal | 8487 (57.25%) | 1140 (55.77%) | 2411 (57.91%) | 12,038 (57.24%) |
| Osteopenia | 5597 (37.76%) | 798 (39.04%) | 1541 (37.02%) | 7936 (37.73%) |
| Osteoporosis | 740 (4.99%) | 106 (5.19%) | 211 (5.07%) | 1057 (5.03%) |
| B M D, bone mineral density; μ, mean; σ , standard deviation |  |  |
| were observed among the foundation models ( p > 0.05), |  |  |  |
| indicating that their out-of-the-box feature representations |  |  |  |
| for osteoporosis screening are comparable. Detailed results |  |  |  |
| for the normal and osteopenia classes are provided in Sup- |  |  |  |
| plemental Table |  |  |  |  |

## The osteoporosis predictive performance metrics of foundation models

| Model | Method | AUC (95% CI) | Accuracy (%) (95% CI) | Sensitivity (%) (95% CI) | Specificity (%) (95% CI) |
| --- | --- | --- | --- | --- | --- |
| OpenCLIP | Linear | 0.73 (0.72-0.74) | 62.62 (61.15-64.09) | 74.41 (73.08-75.73) | 61.99 (60.52-63.47) |
|  | Partial ft | 0.91 (0.90-0.92) | 82.30 (81.14-83.46) | 83.89 (82.77-85.00) | 82.21 (81.05-83.37) |
|  | LoRA | 0.91 (0.90-0.92) | 79.01 (77.77-80.24) | 88.63 (87.66-89.59) | 78.49 (77.24-79.74) |
| DINOv2 | Linear | 0.77 (0.76-0.79) | 66.66 (65.23-68.09) | 76.78 (75.49-78.06) | 66.12 (64.68-67.56) |
|  | Partial ft | 0.91 (0.90-0.92) | 81.60 (80.42-82.78) | 85.31 (84.23-86.38) | 81.40 (80.22-82.58) |
|  | LoRA | 0.93 (0.92-0.94) | 87.39 (86.38-88.40) | 84.36 (83.26-85.46) | 87.55 (86.55-88.55) |
| CheXagent | Linear | 0.72 (0.71-0.73) | 66.92 (65.49-68.35) | 68.25 (66.83-69.66) | 66.85 (65.42-68.28) |
|  | Partial ft | 0.90 (0.89-0.91) | 82.70 (81.5683.85) | 82.46 (81.31-83.62) | 82.72 (81.57-83.87) |
|  | LoRA | 0.85 (0.84-0.86) | 76.24 (74.95-77.54) | 79.62 (78.40-80.84) | 76.06 (74.77-77.36) |
| RAD-DINO | Linear | 0.72 (0.70-0.73) | 66.99 (65.57-68.42) | 66.82 (65.39-68.25) | 67.00 (65.58-68.43) |
|  | Partial ft | 0.89 (0.88-0.90) | 85.73 (84.67-86.79) | 76.30 (75.01-77.60) | 86.23 (85.19-87.28) |
|  | LoRA | 0.90 (0.89-0.91) | 86.69 (85.66-87.72) | 76.78 (75.49-78.06) | 87.22 (86.21-88.24) |

### Formule


$$bone = AUC bone -max(No-bone AUC, 0.5)(1)$$
