# Enhancing automatic landmark localization in X-ray images using combined segmentation and regression models: application to lower limb alignment assessment.

**Auteurs** : Zarghami A, Amador Sánchez S, Van Overschelde P, Vandemeulebroucke J.
**Année** : 2026
**DOI** : 10.1038/s41598-026-49750-2

## Résumé

Manual landmark detection in lower limb medical imaging is time-consuming and error-prone. Recently, authors have proposed automatic landmark detection methods based on image segmentation, coordinate regression, or a combination of both to aid clinicians. While the latter approach shows promising results, detailed optimization of its design choices, including the integration strategy and hyperparameter tuning, remains unexplored. This study investigates the optimal approach to combining image segmentation and coordinate regression, focusing on selecting suitable network architectures and optimizing their configurations. We contrasted two methods for training the network: end-to-end training and cascading the subnetworks, and assessed the optimal architecture for each strategy. For landmark segmentation, we compared U-Net and Swin-UNETR models, and for coordinate regression, we assessed VGG-16, ResNet-50, and Swin-B. Performance was evaluated in detecting eight landmarks in each leg of

## Méthodologie

{'study_design': "Étude comparative de méthodes de deep learning combinant segmentation d'image et régression de coordonnées pour la détection automatique de repères anatomiques, avec comparaison de deux stratégies d'entraînement (end-to-end vs. cascade) et de plusieurs architectures", 'intervention': 'Modèles de segmentation (U-Net, Swin-UNETR) combinés à des modèles de régression de coordonnées (VGG-16, ResNet-50, Swin-B), entraînés selon deux stratégies : end-to-end et cascade', 'control': None, 'primary_outcomes': ['Erreur de distance euclidienne médiane (mm) entre repères prédits et repères de référence', 'Nombre de faux positifs', 'Success Detection Rate (SDR)'], 'secondary_outcomes': ["Évaluation de l'alignement des membres inférieurs (angle hip-knee-ankle, HKA)", 'MAD, mLDFA, mMPTA'], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'Erreur de distance euclidienne médiane - Swin-UNETR', 'value': '1.74', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': 'IQR = 0.98 mm', 'source_section': 'Results', 'source_quote': 'Swin-UNETR slightly outperformed U-Net, with a lower Euclidean distance error (1.74 mm [0.98 mm] versus 1.75 mm [1.06 mm]) and significantly fewer false positives (160 vs. 502).'}, {'outcome': 'Erreur de distance euclidienne médiane - U-Net', 'value': '1.75', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': 'IQR = 1.06 mm', 'source_section': 'Results', 'source_quote': 'Swin-UNETR slightly outperformed U-Net, with a lower Euclidean distance error (1.74 mm [0.98 mm] versus 1.75 mm [1.06 mm]) and significantly fewer false positives (160 vs. 502).'}, {'outcome': 'Faux positifs - Swin-UNETR vs U-Net', 'value': '160 vs. 502', 'unit': 'count', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'the Swin-UNETR yields significantly fewer false positives (160 vs. 502)'}, {'outcome': 'Erreur de distance euclidienne médiane - VGG-16 end-to-end (meilleure configuration)', 'value': '2.44', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': 'IQR = 2.12 mm', 'source_section': 'Abstract / Conclusion', 'source_quote': 'For coordinate regression, VGG-16 in the endto-end configuration achieved the highest accuracy (2.44 mm [2.12 mm]) and proved optimal for lower limb alignment assessment'}, {'outcome': "Pourcentage d'estimations dans 1.5° de l'angle HKA de référence", 'value': '97.88', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'with 97.88% of estimations falling within 1.5 • of the hip-knee-ankle angle ground truth'}], 'qualitative_findings': ["La difficulté de localisation dépend du repère : les repères de l'interligne du genou (FC et TP) présentent des erreurs moyennes plus élevées et une plus grande variabilité que le repère fémoral (HoF) et les malléoles", "Pour ResNet-50 et Swin-B, un compromis existe selon la stratégie d'entraînement : ResNet-50 surpasse Swin-B en cascade, mais Swin-B surpasse ResNet-50 en end-to-end"], 'main_findings': ["Swin-UNETR surpasse légèrement U-Net en termes d'erreur de distance et présente significativement moins de faux positifs", "VGG-16 est le réseau de régression optimal, quelle que soit la modalité d'entraînement", "L'approche end-to-end surpasse globalement l'approche en cascade", "La combinaison Swin-UNETR + VGG-16 en configuration end-to-end offre la performance la plus précise et robuste pour la détection automatique de repères et l'évaluation de l'alignement des membres inférieurs"]}

## Conclusions

La combinaison d'un modèle Swin-UNETR et d'un réseau VGG-16 selon une optimisation end-to-end permet d'obtenir une détection précise des repères (erreur médiane de 2.44 mm, IQR de 2.12 mm) et une évaluation fiable de l'alignement des membres inférieurs Cette configuration démontre une meilleure performance que son équivalent en cascade, même lorsqu'elle est associée à d'autres modèles dans la phase de régression

## Descriptive

| Variable | Category | Value |
| --- | --- | --- |
|  | Male [%] | 34.06 |
| Gender | Female [%] | 56.47 |
|  | Unknown [%] | 9.47 |
| Age | Years [median (IQR)] | 64 (18) |
|  | Hip (one side) [%] | 10.01 |
|  | Hip (both sides) [%] | 4.13 |
| Presence of external devices | Knee (one side) [%] Knee (both sides) [%] | 35.15 13.93 |
|  | Ankle (one side) [%] | 2.39 |
|  | Ankle (both sides) [%] | 0.11 |
| Presence of "R" marker | Obstructing marker [%] 7.73 |
|  | 0 [%] | 44.29 |
|  | 1 [%] | 33.02 |
| KL grade | 2 [%] | 10.88 |
|  | 3 [%] | 6.80 |
|  | 4 [%] | 5.01 |

## Euclidean distance [mm] Missed detection False positives

| U-Net | 1.75 (1.06) | 4 | 502 |
| --- | --- | --- | --- |
| Swin-UNETR 1.74 (0.98) | 4 | 160 |

## 5 •

| End-to-end |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| VGG-16 | 1.88 ± 1.47 1.91 ± 1.39 | 1.10 ± 1.31 | 0.47 ± 0.37 97.88 |
| ResNet-50 4.11 ± 2.90 | 2.57 ± 1.72 | 1.37 ± 1.35 | 1.1 ± 0.77 | 72.42 |
| Swin-B | 2.74 ± 2.18 | 2.34 ± 1.61 | 1.23 ± 1.33 | 0.71 ± 0.55 | 89.83 |
| Cascade |  |  |  |  |  |
| VGG-16 | 2.21 ± 1.93 | 1.78 ± 1.24 0.94 ± 1.09 0.56 ± 0.48 | 94.49 |
| ResNet-50 6.13 ± 4.75 | 2.32 ± 1.63 | 1.73 ± 1.43 | 1.77 ± 1.28 | 47.03 |
| Swin-B | 7.37 ± 5.33 | 2.68 ± 1.90 | 1.81 ± 1.58 | 2.29 ± 1.53 | 35.16 |

### Formule


$$L total = LSgm + LReg.$$

### Formule


$$LDsc-CE = LDsc + LCE, (2$$

### Formule


$$)$$

### Formule


$$LDsc = 1 - 2T P 2T P + F P + F N , (3$$

### Formule


$$) LCE = -(y log(ŷ) + (1 -y) log(1 -ŷ)) . (4$$

### Formule


$$)$$

### Formule


$$LMSE = 1 n n ∑ i=1 ∥p i -pi ∥ 2 2 (5$$

### Formule


$$)$$

### Formule


$$Distance(p i , pi ) = √ (pi,x -pi,x) 2 + (pi,y -pi,y) 2 . (6$$

### Formule


$$)$$

### Formule


$$SDRz = n d n × 100%(7)$$

### Formule


$$MAE = 1 n n ∑ i=1 | mi -mi| (8$$

### Formule


$$)$$
