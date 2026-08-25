# Automatic Lung Segmentation in Chest X-Ray Images Using SAM With Prompts From YOLO

**Auteurs** : Ebrahim Khalili, Blanca Priego, Antonio León‐Jiménez, Daniel Morillo
**Année** : 2024
**DOI** : 10.1109/access.2024.3454188

## Résumé

Despite the impressive performance of current deep learning models in the field of medical imaging, transferring the lung segmentation task in X-ray images to clinical practice is still a pending task. In this study, the performance of a fully automatic framework for lung field segmentation in chest X-ray images was evaluated. The framework is rooted in the combination of the Segment Anything Model (SAM) with prompt capabilities, and the You Only Look Once (YOLO) model to provide effective prompts. Transfer learning, loss functions, and several validation strategies were thoroughly assessed. This provided a complete benchmark that enabled future research studies to fairly compare new segmentation strategies. The results achieved demonstrated significant robustness and generalization capability against the variability in sensors, populations, disease manifestations, device processing, and imaging conditions. The proposed framework was computationally efficient, could address bias in training over multiple datasets, and had the potential to be applied across other domains and modalities.

## Méthodologie

{'study_design': 'Fully automatic framework for lung segmentation in CXR images, combining the Segment Anything Model (SAM) with prompt capabilities and the You Only Look Once (YOLO) model to provide bounding box prompts.', 'intervention': None, 'control': None, 'primary_outcomes': ['Dice score', 'IoU (Intersection over Union)'], 'secondary_outcomes': [], 'statistical_methods': ['5-fold cross-validation', 'hold-out validation (78-22%)', 'cross-dataset validation'], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [], 'qualitative_findings': [], 'main_findings': []}

## Conclusions

Ce travail a introduit un framework de deep learning entièrement automatisé pour améliorer la précision de la segmentation pulmonaire dans les radiographies thoraciques (CXR) Le framework est basé sur le développement d'un modèle automatisé capable de s'entraîner sur de petits jeux de données tout en restant applicable à des jeux de données plus larges et diversifiés L'utilisation d'un modèle fondateur (SAM) pour la segmentation pulmonaire automatique dans les CXR, combinée à des prompts entièrement automatisés issus d'un modèle YOLO, a permis d'atteindre efficacement les objectifs de segmentation pulmonaire Cette approche souligne l'importance de se concentrer sur la région pulmonaire pour atteindre des capacités de généralisation et suggère des applications potentielles dans divers domaines et modalités La performance et la robustesse du framework ont été rigoureusement évaluées à l'aide d'une gamme de jeux de données et de méthodes de validation, établissant un benchmark précieux pour une analyse comparative équitable dans les recherches futures Les résultats soulignent le potentiel de nouvelles approches pour la segmentation pulmonaire, offrant des méthodes robustes et fiables avec une applicabilité clinique

## Table 6

| summarizes the model performance estimated |
| --- |
| using cross-dataset validation. |

### Formule


$$x i tl = min (x | x = 1) , y i tl = min (y | y = 1)(1)$$

### Formule


$$x i br = max (x | x = 1) , y i br = max (y | y = 1)(2)$$

### Formule


$$GIoU = | A ∩ B| | A ∪ B| - | C\(A ∪ B)| | C| (3)$$

### Formule


$$L = L F,γ + L T ,α,β(4)$$

### Formule


$$L F,γ = c SJ 1/γ (5) SJ = 1 - N i=1 p ic g ic + ε N i=1 p ic +g ic -N i=1 p ic g ic + ε (6) L T ,α,β = N i=1 p ic g ic + ε N i=1 p ic g ic + α N i=1 p ic g ic + β N i=1 p ic g ic + ε(7)$$

### Formule


$$Precision = TP TP + FP(8)$$
