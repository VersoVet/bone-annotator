# Iterative Loop Method Combining Active and Semi-Supervised Learning for Domain Adaptive Semantic Segmentation

**Auteurs** : Licong Guan, Yuan Xue
**Année** : 2023
**DOI** : 10.48550/arxiv.2301.13361

## Méthodologie

{'study_design': "Proposition d'une méthode (ILM-ASSL) en trois étapes itératives : (1) apprentissage semi-supervisé (modèle enseignant-étudiant) sur données étiquetées et non étiquetées, (2) apprentissage actif basé sur une stratégie de sélection par incertitude prédictive pour identifier les images cibles les plus utiles à annoter, (3) annotation/correction manuelle des labels par des experts, suivie d'un nouvel entraînement semi-supervisé (boucle répétée).", 'intervention': "Sélection active d'images non étiquetées selon un score d'incertitude (entropie moyenne des prédictions du modèle enseignant), correction manuelle des pseudo-labels pour ces images, puis réintégration dans l'entraînement semi-supervisé.", 'control': 'Modèles de référence sans la composante proposée : UDA (ProDA, DAP+ProDA), apprentissage actif seul (AADA, MADA, LabOR, RIPU), et une baseline utilisant 5% de données cibles sélectionnées aléatoirement entraînées sur DeepLab-v3+.', 'primary_outcomes': ["mean Intersection-over-Union (mIoU) sur l'ensemble de validation Cityscapes"], 'secondary_outcomes': ["Performance par classe, en particulier sur les classes rares ('tail categories') de Cityscapes (traffic light, traffic sign, rider, bus, train, motorcycle, bicycle)", 'Qualité visuelle des cartes de segmentation prédites', 'Visualisation t-SNE des représentations de caractéristiques apprises'], 'statistical_methods': ['Cross-entropy loss (supervisée et non supervisée)', 'Contrastive learning loss', 'Entropy-based pseudo-label thresholding (percentile)', 'Exponential moving average (EMA) pour la mise à jour du modèle enseignant', 'SGD optimizer'], 'duration': "Environ 100K itérations d'entraînement par expérience", 'setting': 'Expériences réalisées sur GPU NVIDIA A100 avec PyTorch, architectures DeepLabv2 et DeepLab-v3+ avec backbone ResNet-101 pré-entraîné sur ImageNet.'}

## Résultats

{'quantitative': [{'outcome': 'Amélioration mIoU sur GTAV → Cityscapes par rapport à la meilleure méthode précédente', 'value': '4.9%', 'unit': 'mIoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Results', 'source_quote': 'improving by 4.9% mIoU and 5.2% mIoU, compared to the previous best method, respectively'}, {'outcome': 'Amélioration mIoU sur SYNTHIA → Cityscapes par rapport à la meilleure méthode précédente', 'value': '5.2%', 'unit': 'mIoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Results', 'source_quote': 'improving by 4.9% mIoU and 5.2% mIoU, compared to the previous best method, respectively'}, {'outcome': "Amélioration mIoU sur GTAV → Cityscapes vs RIPU avec budget d'annotation identique (5%)", 'value': '4.9%', 'unit': 'mIoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Comparisons With the State-of-the-arts', 'source_quote': 'using the same annotation budget (5%), our method achieves 4.9% mIoU improvement over RIPU [41]'}, {'outcome': "Amélioration mIoU sur SYNTHIA → Cityscapes vs RIPU avec budget d'annotation identique (5%)", 'value': '5.2%', 'unit': 'mIoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Comparisons With the State-of-the-arts', 'source_quote': 'our method achieves 5.2% mIoU improvement over RIPU [41] if the same annotation budget (5%) is used'}, {'outcome': 'Gain de performance apporté par L_u (perte non supervisée) par rapport à la baseline', 'value': '10.38%', 'unit': 'points de performance', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Ablation Study', 'source_quote': 'Compared to the baseline, L u can leverage the unlabeled data of the target domain to improve performance by 10.38%.'}, {'outcome': 'Gain de performance additionnel après ajout de L_c (perte contrastive)', 'value': '0.9%', 'unit': 'points de performance', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Ablation Study', 'source_quote': 'The performance is further improved by 0.9% after adding L c in semi-supervised learning.'}, {'outcome': 'Performance finale (mIoU) après ajout de la sélection par apprentissage actif', 'value': '76.11', 'unit': '% mIoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Ablation Study', 'source_quote': 'our performance reaches 76.11%, proving the effectiveness of the sample selection strategy based on prediction uncertainty'}, {'outcome': "mIoU avec budget d'annotation de 2.2% (DeepLab-v3+)", 'value': '75.0', 'unit': '% mIoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Qualitative Results / Table', 'source_quote': 'Ours (2.2%) V3+ 75.0 80.9'}, {'outcome': "mIoU avec budget d'annotation de 5.0% (DeepLab-v3+)", 'value': '76.1', 'unit': '% mIoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Qualitative Results / Table', 'source_quote': 'Ours (5.0%) 76.1 82.1'}], 'qualitative_findings': ["ILM-ASSL produit des prédictions plus lisses pour les catégories de tête (ex: 'pole') et améliore nettement les catégories rares de Cityscapes ('bus', 'rider', 'traffic sign') par rapport à RIPU (GTAV → Cityscapes)", "Sur SYNTHIA → Cityscapes, ILM-ASSL prédit correctement la classe manquante 'truck' avec seulement une petite quantité de données cibles, et offre un contour plus détaillé pour la classe 'person'", "La visualisation t-SNE montre qu'ILM-ASSL sépare mieux les caractéristiques entre catégories, avec une frontière de décision plus nette que les méthodes concurrentes (RIPU)"], 'main_findings': ["ILM-ASSL établit l'état de l'art sur GTAV → Cityscapes et SYNTHIA → Cityscapes, dépassant les méthodes d'adaptation de domaine non supervisée (ProDA, DAP+ProDA) et d'apprentissage actif (LabOR, RIPU)", 'Avec seulement 1% des données cibles, ILM-ASSL dépasse déjà les meilleures méthodes non supervisées antérieures', "La méthode améliore particulièrement les performances sur les classes rares ('tail categories') de Cityscapes, atténuant le problème de distribution à longue traîne", 'Chaque composant (perte non supervisée L_u, perte contrastive L_c, sélection active) contribue de manière cumulative et significative à la performance finale']}

## Conclusions

ILM-ASSL atteint les meilleures performances en segmentation sémantique adaptative au domaine avec un coût d'étiquetage minimal en combinant apprentissage semi-supervisé et apprentissage actif L'apprentissage semi-supervisé améliore la précision du modèle sur le domaine cible en exploitant des données massives non étiquetées, tandis que l'intervention humaine limitée corrige le bruit des pseudo-labels La stratégie de sélection basée sur l'incertitude de prédiction, avec une image entière comme unité minimale de sélection (compatible avec Labelme), réduit davantage le coût d'annotation dans une perspective d'application pratique L'efficacité de la méthode est validée par des expériences extensives et des études d'ablation, avec des résultats état de l'art

## COMPARISON WITH PREVIOUS RESULTS ON TASK GTAV → CITYSCAPES. WE REPORT THE MIOU AND THE BEST RESULTS ARE SHOWN IN BOLD.Methods with V2 are based on DeepLab-v2

| Method | Net. | r o a d | s id e . | b u il . | w a ll | f e n c e | p o le | li g h t | s ig n | v e g . | te r r. | s k y | p e r s . | r id e r | c a r | tr u c k | b u s | tr a in | m o to r | b ik e | mIoU |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Source Only |  | 75.8 16.8 77.2 12.5 | 21.0 25.5 30.1 20.1 81.3 24.6 70.3 53.8 26.4 49.9 17.2 25.9 | 6.5 | 25.3 36.0 | 36.6 |
| CBST [20] |  | 91.8 53.5 | 80.5 32.7 21.0 34.0 28.9 20.4 83.9 34.2 80.9 53.1 24.0 82.7 30.3 35.9 16.0 25.9 | 42.8 | 45.9 |
| MRKLD [21] |  | 91.0 | 55.4 80.0 33.7 21.4 37.3 32.9 24.5 85.0 34.1 80.8 57.7 24.6 84.1 27.8 30.1 26.9 26.0 | 42.3 | 47.1 |
| ASS [26] | V2 | 90.6 44.7 | 84.8 34.3 28.7 31.6 35.0 37.6 84.7 43.3 85.3 57.0 31.5 83.8 42.6 48.5 | 1.9 | 30.4 | 39.0 | 49.2 |
| SAC [35] |  | 90.4 53.9 | 86.6 42.4 27.3 45.1 48.5 42.7 87.4 40.1 86.1 67.5 29.7 88.5 49.1 54.6 | 9.8 | 26.6 | 45.3 | 53.8 |
| ProDA [14] |  | 87.8 | 56.0 79.7 46.3 44.8 45.6 53.5 53.5 88.6 45.2 82.1 70.7 39.2 88.8 45.5 59.4 | 1.0 | 48.9 | 56.4 | 57.5 |
| DAP+ProDA [10] |  | 94.5 | 63.1 89.1 29.8 47.5 50.4 56.7 58.7 89.5 50.2 87.0 73.6 38.6 91.3 50.2 52.9 | 0.0 | 50.2 | 63.5 | 59.8 |
| LabOR (2.2%) [15] |  | 96.6 77.0 | 89.6 47.8 50.7 | 48.0 56.6 63.5 89.5 | 57.8 | 91.6 72.0 47.3 91.7 62.1 61.9 48.9 47.9 65.3 | 66.6 |
| RIPU (2.2%) [41] | V2 | 96.5 74.1 89.7 53.1 | 51.0 43.8 53.4 62.2 90.0 57.6 92.6 73.0 53.0 92.8 73.8 78.5 62.0 55.6 70.0 | 69.6 |
| Ours (2.2%) |  | 96.4 74.6 | 91.1 45.9 | 52.4 59.4 67.9 68.3 91.4 | 50.0 | 92.8 76.2 57.2 93.6 78.2 81.3 69.5 58.4 72.1 | 72.5 |
| AADA (5%) [16] |  | 92.2 59.9 87.3 36.4 45.7 46.1 50.6 59.5 88.3 44.0 90.2 69.7 38.2 90.0 55.3 45.1 32.0 32.6 62.9 | 59.3 |
| MADA (5%) [40] |  | 95.1 69.8 | 88.5 43.3 48.7 45.7 53.3 59.2 89.1 46.7 91.5 73.9 50.1 91.2 60.6 56.9 48.4 51.6 | 68.7 | 64.9 |
| RIPU (5%) [41] Ours (1%) | V3+ | 97.0 77.3 95.2 67.0 90.9 47.4 49.6 60.9 68.2 67.5 90.9 44.6 91.5 81.3 60.5 93.9 67.2 76.6 47.9 54.7 74.8 90.4 54.6 53.2 47.7 55.9 64.1 90.2 59.2 93.2 75.0 54.8 92.7 73.0 79.7 68.9 55.5 70.3 | 71.2 70.0 |
| Ours (2.2%) |  | 96.5 | 75.6 91.2 46.7 53.6 62.1 70.3 76.0 91.4 52.1 94.1 82.0 60.8 94.4 | 83.1 | 86.4 71.9 61.2 75.8 | 75.0 |
| Ours (5%) |  | 96.9 77.8 91.6 46.7 | 56.0 63.2 70.8 77.4 91.9 | 54.9 94.5 82.3 61.2 94.9 | 79.3 | 88.1 75.3 65.8 77.6 | 76.1 |

## WITH PREVIOUS RESULTS ON TASK SYNTHIA → CITYSCAPES. WE REPORT THE MIOUS IN TERMS OF 13 CLASSES (EXCLUDING THE "WALL", "FENCE", AND "POLE") AND 16 CLASSES. THE BEST RESULTS ARE SHOWN IN BOLD.

| Method | Net. | r o a d | s id e . | b u il . | w a ll * | f e n c e * | p o le * | li g h t | s ig n | v e g . | s k y | p e r s . | r id e r | c a r | b u s | m o to r | b ik e | mIoU mIoU* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Source Only |  | 55.6 23.8 74.6 | 9.2 | 0.2 | 24.4 | 6.1 | 12.1 74.8 79.0 55.3 19.1 39.6 23.3 13.7 25.0 | 33.5 | 38.6 |
| CBST [20] |  | 68.0 29.9 76.3 10.8 | 1.4 | 33.9 | 22.8 29.5 77.6 78.3 60.6 28.3 81.6 23.5 18.8 39.8 | 42.6 | 48.9 |
| MRKLD [21] |  | 67.7 32.2 73.9 10.7 | 1.6 | 37.4 | 22.2 31.2 80.8 80.5 60.8 29.1 82.8 25.0 19.4 45.3 | 43.8 | 50.1 |
| ASS [26] | V2 | 83.0 44.0 80.3 | - | - | - | 17.1 15.8 80.5 81.8 59.9 33.1 70.2 37.3 28.5 45.8 | - | 52.1 |
| SAC [35] |  | 89.3 47.2 85.5 26.5 | 1.3 | 43.0 | 45.5 32.0 87.1 89.3 63.6 25.4 86.9 35.6 30.4 53.0 | 52.6 | 59.3 |
| ProDA [14] |  | 87.8 45.7 84.6 37.1 | 0.6 | 44.0 | 54.6 37.0 88.1 84.4 74.2 24.3 88.2 51.1 40.5 45.6 | 55.5 | 62.0 |
| DAP+ProDA [10] |  | 84.2 46.5 82.5 35.1 | 0.2 | 46.7 | 53.6 45.7 89.3 87.5 75.7 34.6 91.7 73.5 49.4 60.5 | 59.8 | 64.3 |
| RIPU (2.2%) [41] Ours (2.2%) | V2 | 96.8 96.8 | 76.6 89.6 45.0 76.1 89.7 47.3 | 47.7 52.8 | 45.0 56.3 | 53.0 62.5 90.6 92.7 73.0 52.9 93.1 62.9 70.1 91.1 93.2 78.4 59.7 93.5 | 80.5 78.2 | 52.4 70.1 58.2 74.2 | 70.1 73.7 | 75.7 78.6 |
| AADA (5%) [16] |  | 91.3 57.6 86.9 37.6 | 48.3 | 45.0 | 50.4 58.5 88.2 90.3 69.4 37.9 89.9 44.5 32.8 62.5 | 61.9 | 66.2 |
| MADA (5%) [40] |  | 96.5 74.6 88.8 45.9 | 43.8 | 46.7 | 52.4 60.5 89.7 92.2 74.1 51.2 90.9 60.3 52.4 69.4 | 68.1 | 73.3 |
| RIPU (5%) [41] Ours (1%) | V3+ | 97.0 78.9 89.9 47.2 96.8 74.8 90.0 34.0 | 50.7 46.3 | 48.5 60.9 | 55.2 63.9 91.1 93.0 74.4 54.1 92.9 79.9 55.3 71.0 68.0 74.8 90.2 92.5 81.1 58.2 93.0 72.3 63.4 75.6 | 71.4 73.2 | 76.7 79.3 |
| Ours (2.2%) |  | 96.8 76.3 90.9 48.1 | 54.2 | 62.4 | 69.0 77.3 91.0 93.7 82.2 | 60.3 | 94.2 80.0 63.8 76.0 | 76.0 | 80.9 |
| Ours (5%) |  | 97.4 80.1 91.8 38.6 | 55.2 | 64.1 | 70.9 78.7 91.6 94.5 82.7 60.1 | 94.4 81.7 66.8 77.2 | 76.6 | 82.1 |

## STUDY ON THE EFFECTIVENESS OF VARIOUS COMPONENTS.

| Semi-Supervised Learning | Active Learning | GT→Ci |
| --- | --- | --- | --- |
| L u | L c | Prediction uncertainty | mIoU |
|  |  |  | 59.33 |
|  |  |  | 69.71 |
|  |  |  | 70.61 |
|  |  |  | 76.11 |

## RIPU Ours Ground Truth and Image

| road | side. | buil. | wall |
| --- | --- | --- | --- |
| fence | pole | light | sign |
| veg. | terr. | sky | person |
| rider | car | truck | bus |
| train | motor | bike | ignored |

## WITH OPEN SET DOMAIN ADAPTATION.

| Method | Net. | terrain | truck | train mIoU |
| --- | --- | --- | --- | --- | --- |
| Ours (1%) Ours (2.2%) | V3+ | 41.5 53.5 | 51.6 74.7 | 48.6 59.9 | 69.1 73.9 |

## WITH THE SSDA AND SSL METHODS ON TASK GTAV → CITYSCAPES, SYNTHIA → CITYSCAPES.

| Type | Method | Net. | GT→Ci SY→Ci mIoU mIoU* |
| --- | --- | --- | --- | --- |
|  | MME (3.4%) [29] |  | 52.6 | 59.6 |
| SSDA | ASS (3.4%) [26] | V2 | 54.2 | 62.1 |
|  | DLDM (3.4%) [30] |  | 61.2 | 68.4 |
|  | Ours (2.2%) | V2 | 72.5 | 78.6 |
|  | GCT (3.1%) [52] |  | 63.2 | - |
|  | MT (3.1%) |  |  |  |
| SSL |  | V3+ |  |  |

## ON SOURCE-FREE DOMAIN ADAPTATION SCENARIO.

| Method | Net. Budget | GT→Ci mIoU | SY→Ci mIoU mIoU* |
| --- | --- | --- | --- | --- | --- |
| URMA [54] |  | - | 45.1 | 39.6 | 45.0 |
| LD [55] SFDA [56] | V2 | -- | 45.5 53.4 | 42.6 52.0 | 50.1 60.1 |
| RIPU [41] |  | 2.2% | 67.1 | 68.7 | 74.1 |
| Ours | V2 | 2.2% | 70.4 | 72.0 | 78.1 |

## RESULTS FOR MODEL UPPER LIMITS. .0 72.9 81.3 92.9 66.6 94.9 84.6 67.0 95.7 86.8 92.6 85.6 71.7 79.4 81.1

| Task | Net. | Budget | r o a d | s id e . | b u il . | w a ll | f e n c e | p o le | li g h t | s ig n | v e g . | te r r. | s k y | p e r s . | r id e r | c a r | tr u c k | b u s | tr a in | m o to r | b ik e | mIoU |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GTAV→Cityscapes SYNTHIA→Cityscapes | V3+ | 100% 100% | 98.0 97.9 | 84.6 84.2 | 93.0 93.1 | 58.7 63.0 | 62.9 67.3 73.4 80.0 92.8 63.8 95.1 84.2 66.1 95.6 86.6 91.4 82.9 70.0 79.3 61.8 68 | 80.3 |

### Formule


$$L = L s + λ u L u + λ c L c ,(1)$$

### Formule


$$L s = 1 N l N l i=1 1 W H W H j=1 ce (f • h(x l i,j ; θ), y l i,j ) ,(2)$$

### Formule


$$L u = 1 N u Nu i=1 1 W H W H j=1 ce (f • h(x u i,j ; θ), ŷu i,j ) ,(3)$$

### Formule


$$L c = - 1 C × M C-1 c=0 M i=1 log   e aci,a + ci /ω e aci,a + ci /ω + N j=1 e aci,a - cij /ω   .(4)$$

### Formule


$$H(p ij ) = - C-1 c=0 p ij (c) log p ij (c),(5)$$

### Formule


$$ŷu ij = argmax c p ij (c), if H(p ij ) < γ t ,(6)$$

### Formule


$$γ t =np.percentile(H.flatten(),100 * (1-α t )),$$

### Formule


$$α t = α 0 • 1 - t total epoch ,(7)$$

### Formule


$$S = - 1 W H W H j=1 C-1 c=0 p ij (c) log p ij (c),(8)$$
