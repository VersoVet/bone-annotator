# MCP-MedSAM: A Powerful Lightweight Medical Segment Anything Model Trained with a Single GPU in Just One Day

**Auteurs** : Donghang Lyu, Ruochen Gao, Marius Staring
**Année** : 2025
**DOI** : 10.59275/j.melba.2025-4849

## Résumé

Medical image segmentation involves partitioning medical images into meaningful regions, with a focus on identifying anatomical structures and lesions. It has broad applications in healthcare, and deep learning methods have enabled significant advancements in automating this process. Recently, the introduction of the Segmentation Anything Model (SAM), the first foundation model for segmentation task, has prompted researchers to adapt it for the medical domain to improve performance across various tasks. However, SAM’s large model size and high GPU requirements hinder its scalability and development in the medical domain. To address these challenges, research has increasingly focused on lightweight adaptations of SAM to reduce its parameter count, enabling training with limited GPU resources while maintaining competitive segmentation performance. In this work, we propose MCP-MedSAM, a powerful and lightweight medical SAM model designed to be trainable on a single A100 GPU with 40GB of m

## Méthodologie

{'study_design': "Développement et évaluation d'un modèle léger de segmentation médicale (MCP-MedSAM) basé sur l'architecture LiteMedSAM, entraîné sur un seul GPU NVIDIA A100 40GB en une journée, avec introduction de deux nouveaux types de prompts (modality prompt et content prompt) et d'une stratégie d'échantillonnage basée sur la modalité", 'intervention': "Ajout du modality prompt et du content prompt (embeddings sparse et dense) à l'encodeur de prompts, intégration de composants pré-entraînés (dont CLIP), et stratégie d'échantillonnage de données basée sur la modalité", 'control': 'Comparaison avec des méthodes de référence (top-ranking methods) du classement du challenge, incluant notamment DAFT et Medficientsam', 'primary_outcomes': ['Performance de segmentation (DSC)'], 'secondary_outcomes': ["Temps d'entraînement", "Temps d'inférence", 'Équilibre de performance entre modalités (écart-type)'], 'statistical_methods': ['Wilcoxon signed-rank test'], 'duration': 'Entraînement sur 25 epochs, converge en une journée sur un seul GPU', 'setting': 'Expériences réalisées avec Python 3.10 et PyTorch 2.0.0 sur un seul GPU NVIDIA A100 de 40GB de mémoire'}

## Résultats

{'quantitative': [{'outcome': 'Dice Similarity Coefficient (DSC) rapporté, comparé à MedSAM', 'value': '0.85 à 0.90', 'unit': 'DSC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'the reported performance metrics, such as DSC (ranging from 0.85 to 0.90), indicate comparable performance levels'}], 'qualitative_findings': ['MCP-MedSAM a obtenu les meilleurs résultats et a montré une différence statistiquement significative par rapport aux autres méthodes en comparaison de précision (Table 1)', "MCP-MedSAM a nécessité le moins de temps d'entraînement parmi les modèles de référence comparés (Table 2)", 'Un sur-segmentation notable est survenue en endoscopie pour de nombreux modèles de référence, probablement due à des caractéristiques de fond ressemblant à celles de la cible', "MCP-MedSAM présente les valeurs d'écart-type les plus basses, soulignant l'efficacité de la stratégie d'échantillonnage basée sur la modalité pour équilibrer la performance entre modalités"], 'main_findings': ["L'utilisation de l'un ou l'autre prompt (modality ou content) améliore la précision globale de segmentation", "L'incorporation de composants pré-entraînés (poids initiaux liés au domaine médical) conduit à des résultats optimaux", "La stratégie d'échantillonnage basée sur la modalité atténue les effets négatifs du déséquilibre des données, améliorant significativement la performance des modalités sous-représentées comme le PET, au prix d'une légère baisse de performance pour les modalités communes comme CT et MRI"]}

## Conclusions

MCP-MedSAM atteint une meilleure performance globale de segmentation par rapport aux méthodes les mieux classées du challenge, démontrant son efficacité et son potentiel L'intégration de composants pré-entraînés accélère le processus d'entraînement et améliore la performance L'introduction des prompts de modalité et de contenu apporte des informations diverses et précieuses, améliorant la conception légère de MedSAM La stratégie d'échantillonnage de données basée sur la modalité assure un entraînement équitable de chaque modalité, conduisant à une performance globale plus équilibrée

## Accuracy comparison with state-of-the-art methods on the challenge leaderboard, with the best result for each metric highlighted in bold. The † after each metric value indicates a significant difference (p < .05) compared to the proposed method.

| Models | DSC (%) | NSD (%) |
| --- | --- | --- |
| Baseline | 83.81 ± 15.31 † 83.26 ± 22.67 † |
| LiteMedSAM-Rep |  |  |

## Efficiency comparison with state-of-the-art methods on the challenge leaderboard, with the best result for each metric highlighted in bold. Notably, LiteMedSAM-Rep is trained on an NVIDIA RTX 4090, Rep-MedSAM on an NVIDIA V100, and the other models on an NVIDIA A100.

|  | 86.78 ± 8.63 † | 88.44 ± 12.79 † |
| --- | --- | --- |
| MedficientSAM (Le et al., 2024) | 86.20 ± 8.00 † | 87.65 ± 11.61 † |
| DAFT (Ke et al., 2024) | 87.18 ± 8.29 † | 88.32 ± 13.41 † |
| MCP-MedSAM (proposed) | 87.50 ± 6.91 89.40 ± 10.37 |
| Models | GPU Training Time (hours) | CPU Inference Time (seconds) |
| Baseline | - | - |
| LiteMedSAM-Rep |  |  |

## Ablation study of the component of each prompt processing network in the prompt encoder part of MCP-MedSAM model. The checkmark means including the component in the model. And the best result for each evaluation metrics is shown in bold. The † after each metric value indicates a significant difference (p < .05) compared to the proposed method.

| Modality Prompt Text CLIP Modality Embedding Image CLIP CNN Encoder Content Prompt | DSC (%) | NSD (%) |
| --- | --- | --- | --- | --- |
|  |  |  |  | 86.36 ± 8.39 † 87.64 ± 13.23 † |
|  | ✓ | ✓ | ✓ | 86.82 ± 7.97 † 88.35 ± 12.72 † |
| ✓ |  | ✓ | ✓ | 86.57 ± 7.21 † 88.39 ± 10.91 † |
| ✓ | ✓ |  |  | 87.07 ± 7.19 † 88.78 ± 11.07 † |
| ✓ | ✓ |  | ✓ | 86.92 ± 7.83 † 88.47 ± 12.31 † |
| ✓ | ✓ | ✓ |  | 86.92 ± 7.59 † 88.55 ± 12.02 † |
|  |  | ✓ | ✓ | 87.13 ± 6.89 † 88.76 ± 11.12 † |
| ✓ | ✓ | ✓ | ✓ | 87.50 ± 6.91 89.40 ± 10.37 |

## Ablation study of pre-trained components with different weights (natural and medical images) on the MCP-MedSAM model, with the best result for each evaluation metrics highlighted in bold. The † after each metric value indicates a significant difference (p < .05) compared to the proposed method.

| Method |
| --- |

## Performance comparison across different data sampling strategies, with the performance of each modality detailed. And the best performance for each modality and overall performance is shown in bold. The † after each metric value indicates a significant difference (p < .05) compared to the modality sampling strategy. Microscopy 76.42 ± 15.67 83.07 ± 12.80 82.53 ± 15.79 88.50 ± 12.74 82.17 ± 15.20 88.17 ± 12.28 Average 85.34 ± 8.83 † 86.71 ± 13.84 † 87.04 ± 7.97 † 88.37 ± 12.87 † 87.50 ± 6.91 89.40 ± 10.37

| Modality | Slice Sampling DSC (%) NSD (%) | Case Sampling DSC (%) NSD (%) | Modality Sampling DSC (%) NSD (%) |
| --- | --- | --- | --- | --- | --- | --- |
| CT | 91.00 ± 9.69 | 93.85 ± 9.70 | 90.31 ± 8.10 | 93.55 ± 8.35 | 90.02 ± 7.98 | 93.43 ± 8.14 |
| MR | 87.69 ± 10.70 91.68 ± 12.41 85.73 ± 11.07 | 89.79 ± 12.06 85.53 ± 11.14 89.81 ± 12.59 |
| PET | 66.21 ± 11.38 | 49.40 ± 30.40 | 68.06 ± 9.36 | 52.05 ± 29.13 73.38 ± 7.04 61.68 ± 25.88 |
| US | 82.50 ± 10.52 | 87.16 ± 7.20 | 83.97 ± 11.63 | 88.71 ± 8.35 | 84.77 ± 9.62 89.61 ± 6.55 |
| X-ray | 83.44 ± 7.19 | 88.24 ± 7.36 | 86.33 ± 5.91 | 91.00 ± 6.36 | 85.83 ± 5.93 | 90.57 ± 6.27 |
| Dermoscopy | 93.08 ± 5.21 | 94.61 ± 4.36 | 94.58 ± 4.22 | 96.07 ± 3.23 | 94.84 ± 4.54 96.32 ± 3.56 |
| Endoscopy | 93.19 ± 5.12 | 96.08 ± 3.70 | 96.25 ± 4.11 | 98.45 ± 2.19 | 95.17 ± 6.67 | 97.66 ± 5.08 |
| Fundus | 94.57 ± 1.70 | 96.27 ± 1.52 | 95.61 ± 1.41 | 97.21 ± 1.18 | 95.77 ± 1.39 97.35 ± 1.21 |

### Formule


$$L = λ 1 L mask + λ 2 L iou + λ 3 L mcls + λ 4 L contrastive . (1)$$

### Formule


$$L BCE = - N i M i log( Mi ) + (1 -M i ) log(1 -Mi ) ,$$

### Formule


$$L Dice = 1 - 2 N i M i Mi N i M 2 i + N i M 2 i , (3$$

### Formule


$$)$$

### Formule


$$L iou = 1 N ′ N ′ i=1 s i iou -ŝi iou 2 , (4$$

### Formule


$$)$$

### Formule


$$L mcls = - C i=1 y i log(ŷ i ),(5)$$

### Formule


$$sim 1 = F dc • F T sc , (6$$

### Formule


$$) sim 2 = F sc • F T dc ,(7)$$

### Formule


$$L contrastive = (L ce (sim 1 , y) + L ce (sim 2 , y)) /2. (8)$$
