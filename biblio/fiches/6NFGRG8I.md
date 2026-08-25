# Osteoporosis prediction from hand X-ray images using segmentation-for-classification and self-supervised learning.

**Auteurs** : Hwang U, Lee CH, Yoon K.
**Année** : 2025
**DOI** : 10.1038/s41598-025-16860-2

## Résumé

Osteoporosis is a prevalent metabolic bone disease that frequently remains undiagnosed due to limited access to bone mineral density (BMD) tests, such as Dual-energy X-ray absorptiometry (DXA). To address this issue, recent research explores alternative indicators from peripheral skeletal sites to enable earlier and more accessible screening. In this paper, we propose a method to predict osteoporosis using hand and wrist X-ray images, which are widely available and cost-effective, though their association with DXA-based diagnoses is not yet fully established. Our approach employs an image segmentation model utilizing a mixture of probabilistic U-Net decoders, which captures predictive uncertainty when segmenting the ulna, radius, and metacarpal bones. The segmentation task is formulated as an optimal transport (OT) problem, effectively addressing the variability inherent in medical images. Additionally, we adopt a self-supervised learning (SSL) strategy that pretrains the model on augm

## Méthodologie

{'study_design': "Étude méthodologique/expérimentale proposant un pipeline en trois étapes : (1) segmentation osseuse incertaine via un mélange de décodeurs U-Net probabilistes optimisé par une perte de transport optimal (Wasserstein), (2) pré-entraînement auto-supervisé (contrastif) de l'encodeur sur des segments osseux augmentés (multi-crop personnalisé), (3) fine-tuning supervisé pour la classification ostéoporose/normal, évalué avec split subject-wise 80/10/10 (train/val/test) sur plusieurs seeds.", 'intervention': None, 'control': "Comparaisons avec des approches supervisées classiques issues de la littérature (ex. DeepDXA de Ho et al., VGG16+Transformer de Wang et al.), ainsi qu'avec des variantes ablées du modèle proposé (sans segmentation, avec U-Net à décodeur unique, sans SSL/multi-crop, avec multi-crop conventionnel).", 'primary_outcomes': ['Classification ostéoporose vs normal à partir des segments osseux (précision, rappel, F1, AUC, exactitude)'], 'secondary_outcomes': ['Qualité de la segmentation des os cibles (ulna, radius, métacarpes)', 'Contribution individuelle de chaque os à la prédiction finale'], 'statistical_methods': ['Perte basée sur le transport optimal (distance de Wasserstein / generalized energy distance) pour la segmentation', 'Optimiseur LARC avec scheduler cosine annealing pour le pré-entraînement SSL', 'Sélection du modèle optimal via le score macro-F1 de validation', 'Moyenne des métriques sur trois essais avec seeds aléatoires distincts', 'Agrégation des décisions par segment osseux via la moyenne des probabilités (argmax) pour la décision finale au niveau du sujet'], 'duration': None, 'setting': 'Images radiographiques cliniques de la main et du poignet corrélées à des diagnostics DXA'}

## Résultats

{'quantitative': [{'outcome': 'F1 score - SimCLR', 'value': '0.68', 'unit': None, 'confidence_interval': '± 0.03', 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'SimCLR achieves the highest F1 score of 0.68 ± 0.03 and an AUC of 0.85 ± 0.01, indicating strong predictive performance and consistency in ranking the positive class.'}, {'outcome': 'AUC - SimCLR', 'value': '0.85', 'unit': None, 'confidence_interval': '± 0.01', 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'SimCLR achieves the highest F1 score of 0.68 ± 0.03 and an AUC of 0.85 ± 0.01, indicating strong predictive performance and consistency in ranking the positive class.'}, {'outcome': 'F1 score et AUC - SwAV (performance la plus faible)', 'value': 'F1=0.54, AUC=0.68', 'unit': None, 'confidence_interval': 'F1 ± 0.13, AUC ± 0.04', 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'SwAV appears to struggle relative to the other models, with both its F1 and AUC scores the lowest at 0.54 ± 0.13 and 0.68 ± 0.04 respectively'}, {'outcome': 'Baisse de performance sans segmentation (SimCLR)', 'value': 'F1 -0.12, AUC -0.07, accuracy -0.07', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Ablation studies', 'source_quote': 'SimCLR experienced the largest decrease in F1 score by 0.12, AUC by 0.07, and accuracy by 0.07, followed closely by VICReg'}, {'outcome': 'U-Net à décodeur unique vs multi-décodeurs (SimCLR)', 'value': 'F1: 0.68→0.62, AUC: 0.85→0.80', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Ablation studies', 'source_quote': 'the single-decoder U-Net consistently underperformed relative to our multi-decoder approach, with SimCLR showing the most pronounced differences: F1 score decreased from 0.68 to 0.62, AUC dropped from 0.85 to 0.80, and accuracy'}, {'outcome': 'Sans multi-crop personnalisé ni pré-entraînement SSL (SimCLR)', 'value': 'F1=0.53, AUC=0.67, accuracy=0.72', 'unit': None, 'confidence_interval': 'F1 ± 0.04, AUC ± 0.03, accuracy ± 0.01', 'p_value': None, 'effect_size': None, 'source_section': 'Results, Ablation studies (Table 6)', 'source_quote': 'the F1 score decreases by 0.15 to 0.53 ± 0.04, AUC by 0.18 to 0.67 ± 0.03, and accuracy by 0.09 to 0.72 ± 0.01'}, {'outcome': 'Comparaison avec la meilleure méthode supervisée antérieure (DeepDXA)', 'value': 'F1 +0.17, AUC +0.19, accuracy +0.15', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Comparative analysis with prior supervised approaches', 'source_quote': 'our proposed framework outperforms all baselines by a substantial margin, improving F1 score by 0.17, AUC by 0.19, and accuracy by 0.15 over the best-performing supervised method (DeepDXA)'}], 'qualitative_findings': ["Le 2ème métacarpe, le radius et l'ulna sont, en moyenne, les principaux contributeurs à la détection de l'ostéoporose parmi les sept segments osseux analysés", "Les caractéristiques non pertinentes pour la tâche (tissus mous : muscles, graisse, peau, nerfs) peuvent interférer avec la distinction des cas d'ostéoporose lorsque la segmentation est omise"], 'main_findings': ['SimCLR obtient les meilleures performances parmi les quatre méthodes SSL testées (F1=0.68±0.03, AUC=0.85±0.01), suivi de VICReg, SupCon puis SwAV', "La segmentation osseuse préalable à la classification améliore significativement les performances par rapport à l'utilisation d'images brutes", "L'architecture à mélange de décodeurs sensible à l'incertitude surpasse un U-Net conventionnel à décodeur unique", "Le pré-entraînement auto-supervisé (SSL) est déterminant : son omission fait chuter fortement les performances, rapprochant le modèle d'une prédiction de classe majoritaire", 'La stratégie de multi-crop personnalisée (garantissant au moins 10% de pixels non nuls par crop) surpasse la stratégie de multi-crop conventionnelle', 'Le framework proposé surpasse les approches supervisées existantes (dont DeepDXA) sur toutes les métriques principales']}

## Conclusions

La combinaison d'une segmentation osseuse sensible à l'incertitude et d'un apprentissage de caractéristiques auto-supervisé constitue une stratégie prometteuse basée sur la vision pour la détection précoce de l'ostéoporose à partir d'images radiographiques périphériques de la main Ce système pourrait réduire la charge de travail clinique en identifiant rapidement les cas probablement positifs et améliorer la prise en charge des patients en détectant des cas d'ostéoporose qui pourraient autrement passer inaperçus L'approche pourrait être intégrée aux flux de travail cliniques existants sans changements d'infrastructure majeurs, la rendant adaptable à des environnements de soins variés, y compris à ressources limitées, et adaptée à un dépistage de population à grande échelle

## Table 2

| Age group Normal Osteoporotic Total |
| --- | --- | --- | --- |
| 10-19 | 0 | 2 | 2 |
| 20-29 | 8 | 0 | 8 |
| 30-39 | 9 | 2 | 11 |
| 40-49 | 24 | 4 | 28 |
| 50-59 | 51 | 12 | 63 |
| 60-69 | 23 | 21 | 44 |
| 70-79 | 13 | 13 | 26 |
| 80-89 | 4 | 5 | 9 |
| 90-99 | 1 | 0 | 1 |

## Number of normal and osteoporotic samples categorized by age.

| Gender Normal Osteoporotic Total |
| --- | --- | --- | --- |
| Male | 18 | 5 | 23 |
| Female 115 | 54 | 169 |

## Table 8

| Model | ROI extraction method | Architecture | F1 | AUC | Accuracy |
| --- | --- | --- | --- | --- | --- |
| Jang et al. 9 | Manual cropping | VGG16 | 0.43 ± 0.05 0.63 ± 0.03 0.62 ± 0.04 |
| Hsieh et al. 8 | Landmark-based cropping | VGG16 | 0.48 ± 0.04 0.65 ± 0.04 0.65 ± 0.03 |
| Wang et al. 22 | Landmark-based cropping | VGG16 + Transformer 0.46 ± 0.06 0.64 ± 0.05 0.64 ± 0.03 |
| Ho et al. (DeepDXA) 10 Segmentation-based | ResNet18 | 0.51 ± 0.03 0.66 ± 0.02 0.67 ± 0.02 |
| Ours (full framework) | Segmentation-based + SSL + enhanced aug ResNet50 | 0.68 ± 0.03 0.85 ± 0.01 0.82 ± 0.02 |

## Comparison of our proposed model against existing supervised baselines. All baselines are trained end-to-end without SSL or enhanced augmentation. The first and second highest performance for each metric is highlighted in bold.

|  | F1 | ∆ | AUC | ∆ | Accuracy | ∆ |
| --- | --- | --- | --- | --- | --- | --- |
| SimCLR 0.65 ± 0.03 -0.03 0.82 ± 0.02 -0.03 0.79 ± 0.05 -0.02 |
| SupCon 0.56 ± 0.04 -0.04 0.74 ± 0.04 -0.05 0.72 ± 0.08 -0.03 |
| SwAV | 0.51 ± 0.09 -0.03 0.66 ± 0.05 -0.02 0.70 ± 0.03 -0.02 |
| VICReg 0.59 ± 0.02 -0.05 0.78 ± 0.03 -0.02 0.74 ± 0.05 -0.03 |

## Counter-effect of conventional multi-crop augmentation on osteoporosis screening. The highest performance for each metric is highlighted in bold.

| F1 | ∆ | AUC | ∆ | Accuracy | ∆ |
| --- | --- | --- | --- | --- | --- |
| Supervised 0.53 ± 0.04 -0.15 0.67 ± 0.03 -0.18 0.72 ± 0.01 -0.09 |

### Formule


$$ūk d [:, i, j] = Wsz k ⊙ (u d [:, i, j] + W b z k )$$

### Formule


$$s k = fConv1D ( ūk d ) .$$

### Formule


$$(j) k } S j=1 to generate S segmentation hypotheses {s (j) k } S j=1$$

### Formule


$$q θ (y|x) = K ∑ k=1 π k (x) ( 1 S S ∑ j=1 δ(s (j) k ) ) (1)$$

### Formule


$$q θ (y|x) = N ∑ i=1 α (i) δ(s (i) ) = K ∑ k=1 S ∑ j=1 π k (x) S δ(s (j) k )(2)$$

### Formule


$$p(y|x) = M ∑ j=1 β (j) δ(y (j) )(3)$$

### Formule


$$min θs D ∑ n=1 N ∑ i=1 M ∑ j=1 T * ij C ( s (i) n (xn; θs), y (j) n )(4)$$

### Formule


$$s.t. T * = arg min θπ , T ∈U ∑ i,j TijCij (5$$

### Formule


$$)$$

### Formule


$$U = { T ∈ R N ×M + : T M = α(xn; θπ), T ⊤ N = β } (6$$

### Formule


$$)$$

### Formule


$$min θs,θπ D ∑ n=1 N ∑ i=1 M ∑ j=1 T * ij C ( s (i) n (xn; θs), y (j) n ) + λDKL ( ∑ j T * ij ∥ α(xn; θπ) )(7)$$

### Formule


$$s.t. T * = arg min T ∈U ′ ∑ i,j TijCij (8$$

### Formule


$$)$$

### Formule


$$U ′ = { T ∈ R N ×M + : T M ≤ γ • N , T ⊤ N = β }(9)$$
