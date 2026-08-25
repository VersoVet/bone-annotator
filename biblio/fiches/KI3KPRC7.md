# Transductive Kernel Map Learning and Its Application Image Annotation

**Auteurs** : Phong Vo, Hichem Sahbi
**Année** : 2012
**DOI** : 10.5244/c.26.68

## Résumé

Introduction: Liver cancer is among the leading causes of cancer-related deaths worldwide. Accurate delineation of hepatic tumors is crucial for diagnosis, prognosis, and treatment planning, yet manual annotation is labor-intensive and subject to variability. Deep neural networks (DNNs) have shown promise in automating segmentation but require large amounts of high-quality labeled data, which is difficult to obtain. Incorporating noisy labels without proper handling can corrupt training and degrade performance. Methods: We introduce MPVT+, a noise-robust training framework that integrates a pixel-wise noise-adaptation module with a multi-stage perturbation and variable-teacher (MPVT) consistency strategy. The noise adaptor infers corruption probabilities and re-weights unreliable supervision, while MPVT assembles an ensemble of stochastic teacher models that apply progressively stringent perturbations. This combination enables the network to exploit both clean and noisy labels without overfitting. Results: Experiments conducted on 739 retrospectively collected liver-tumor CT datasets demonstrated that MPVT+ significantly outperformed baseline and traditional noise-handling approaches. Compared to a noise-free U-Net baseline (Dice Similarity Coefficient [DSC] 75.1%), MPVT+ improved segmentation accuracy to 80.3%. The framework consistently achieved superior results across multiple evaluation metrics, including DSC, JSC, SVD, and VOE. Discussion: The MPVT+ framework demonstrates that principled noise modeling, coupled with consistency training, effectively unlocks the potential of imperfect medical datasets. This strategy reduces the dependency on perfectly labeled datasets and moves fully automated liver tumor delineation closer to clinical applicability.

## Méthodologie

{'study_design': "Cadre d'entraînement d'apprentissage profond intégrant un module d'adaptation au bruit pixel par pixel avec une stratégie de cohérence multi-étapes de perturbation et de teacher variable (MPVT), comparé à une architecture U-Net de référence sans bruit et à des méthodes traditionnelles de gestion du bruit", 'intervention': 'Framework MPVT+ combinant noise adaptor (couches entièrement connectées et softmax prédisant des variables latentes simulant la génération de bruit dans les labels) et stratégie semi-supervisée MPVT (mean teachers à mise à jour de paramètres variable inspirée du dropout, générant des pseudo-labels robustes avec perturbations progressives)', 'control': 'U-Net de référence entraîné sans gestion du bruit (noise-free baseline)', 'primary_outcomes': ['Dice Similarity Coefficient (DSC) de segmentation des tumeurs hépatiques'], 'secondary_outcomes': ['JSC (Jaccard Similarity Coefficient)', 'SVD', 'VOE (Volumetric Overlap Error)'], 'statistical_methods': [], 'duration': None, 'setting': "Segmentation d'images CT hépatiques (contexte de recherche en imagerie médicale)"}

## Résultats

{'quantitative': [{'outcome': 'Dice Similarity Coefficient (DSC) - U-Net de référence sans bruit', 'value': '75.1', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Discussion', 'source_quote': 'Compared to a noise-free U-Net baseline (Dice Similarity Coefficient [DSC] 75.1%), MPVT+ improved segmentation accuracy to 80.3%.'}, {'outcome': 'Dice Similarity Coefficient (DSC) - MPVT+', 'value': '80.3', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Discussion', 'source_quote': 'MPVT+ achieved the Dice similarity coefficient (DSC) from 75.1 % for a noise-free U-Net baseline to 80.3 %.'}], 'qualitative_findings': [], 'main_findings': ['MPVT+ a significativement surpassé les approches de référence et les méthodes traditionnelles de gestion du bruit', "Le framework a constamment obtenu des résultats supérieurs sur plusieurs métriques d'évaluation (DSC, JSC, SVD, VOE)"]}

## Conclusions

Le cadre MPVT+ démontre qu'une modélisation principielle du bruit, couplée à un entraînement par cohérence, permet d'exploiter efficacement le potentiel de jeux de données médicales imparfaits Cette stratégie réduit la dépendance à des jeux de données parfaitement annotés et rapproche la délinéation entièrement automatisée des tumeurs hépatiques de l'applicabilité clinique L'approche améliore la robustesse au bruit et la capacité de généralisation du modèle en incorporant à la fois des données étiquetées propres et bruitées, surpassant les méthodes traditionnelles

## TABLE 3 Results of ablation analysis.

| Method | DSC | JSC | SVD | VOE |
| --- | --- | --- | --- | --- |
|  | (95% CI) | (95% CI) | (95% CI) | (95% CI) |
| ResNet34 | 75.09 | 63.18 | 24.91 | 36.82 |
|  | (72.30, | (60.07, | (22.12, | (33.72, |
|  | 77.88) | 66.28) | 27.70) | 39.93) |
| Noise Adaptor | 78.08 | 66.08 | 21.92 | 33.92 |
|  | (75.92, | (63.48, | (19.76, | (31.32, |
|  | 80.24) | 68.68) | 24.08) | 36.52) |
| MPVT | 79.27 | 67.25 | 20.73 | 32.75 |
|  | (77.41, | (64.92, | (18.87, | (30.43, |
|  | 81.13) | 69.57) | 22.59) | 35.08) |
| w/o Input | 78.55 | 66.85 | 21.45 | 33.15 |
| Perturbations | (76.28, | (64.22, | (19.17, | (30.51, |
|  | 80.83) | 69.49) | 23.72) | 35.78) |
| w/o Feature | 78.42 | 66.44 | 21.58 | 33.56 |
| Perturbations | (76.30, | (63.92, | (19.46, | (31.03, |
|  | 80.54) | 68.97) | 23.70) | 36.08) |
| w/ One | 77.92 | 65.74 | 22.08 | 34.26 |
| Teacher | (75.84, | (63.20, | (20.00, | (31.72, |
| Model | 80.00) | 68.28) | 24.16) | 36.80) |
| Proposed | 80.29 | 68.68 | 19.71 | 31.32 |
| Method | (78.42, | (66.35, | (17.83, | (29.00, |
|  | 82.16) | 71.00) | 21.58) | 33.65) |
| The best results are bolded. |  |  |  |

### Formule


$$L =L sup (D c ) + β ada L ada (D n ) + β reg σ + β semi (L semi (D c ) + L semi (D n )) ,(1)$$

### Formule


$$(∃ρ ∈ [0, 1]) ∧ ∀ i=j p ij = 1 -ρ ∧ ∀ i =j p ij = ρ 1 -c , (2$$

### Formule


$$)$$

### Formule


$$(∃ρ ∈ [0, 1]) ∧ ∀ i=j p ij = 1 -ρ ∧ ⎛ ⎝ ∀ i =j c j=0 p ij = ρ ⎞ ⎠ , (3$$

### Formule


$$)$$

### Formule


$$p ij (x) = p ỹ = j|y = i, x ,(4)$$

### Formule


$$p ij (ω) = p ỹ = j|y = i, ω ,(5)$$

### Formule


$$ŷada = ŷ • p ada j = 1|i = 1 + 1 -ŷ • p ada j = 1|i = 0 ,$$

### Formule


$$L = L sup + β ada L ada + β reg σ . (7$$

### Formule


$$)$$

### Formule


$$L sup = 1 |D n || | (x,y)∈Dn ω∈ l f θ (T weak (x)) , T weak y , (8$$

### Formule


$$)$$

### Formule


$$L ada = 1 |D n || | x,y ∈D n ω∈ l g f θ T weak x , f θ ada T weak x , T weak y ,(9)$$

### Formule


$$g ŷ, p ada = ŷada =ŷ • p ada j = 1|i = 1 + 1 -ŷ • p ada j = 1|i = 0 . (10$$

### Formule


$$)$$

### Formule


$$σ = 1 |D n || | (x,y)∈Dn ω∈ f θ (T weak (x)) -g f θ (T weak (x)) 2 2 .$$

### Formule


$$L = L sup + β semi L semi , (12$$

### Formule


$$)$$

### Formule


$$L semi = 1 |D n || | x,y ∈D n ω∈ l f θ s T strong T weak x , ρ τ 1 ,τ 2 F θ t T strong T weak x , y ,(13)$$

### Formule


$$y pseudo (c) = ŷ (c) ≥ τ 1 ∨ ŷ (c) ≥ τ 2 ∧ y (c) = 1 .(14)$$
