# Affinity-Graph-Guided Contractive Learning for Pretext-Free Medical Image Segmentation with Minimal Annotation

**Auteurs** : Zehua Cheng, Di Yuan, Thomas Lukasiewicz
**Année** : 2024
**DOI** : 10.1109/bibm62325.2024.10822604

## Résumé

The combination of semi-supervised learning (SemiSL) and contrastive learning (CL) has been successful in medical image segmentation with limited annotations. However, these works often rely on pretext tasks that lack the specificity required for pixel-level segmentation, and still face overfitting issues due to insufficient supervision signals resulting from too few annotations. Therefore, this paper proposes an affinitygraph-guided semi-supervised contrastive learning framework (Semi-AGCL) by establishing additional affinity-graph-based supervision signals between the student and teacher network, to achieve medical image segmentation with minimal annotations without pretext. The framework first designs an average-patchentropy-driven inter-patch sampling method, which can provide a robust initial feature space without relying on pretext tasks. Furthermore, the framework designs an affinity-graph-guided loss function, which can improve the quality of the learned representation and the model's generalization ability by exploiting the inherent structure of the data, thus mitigating overfitting. Our experiments indicate that with merely 10% of the complete annotation set, our model approaches the accuracy of the fully annotated baseline, manifesting a marginal deviation of only 2.52%. Under the stringent conditions where only 5% of the annotations are employed, our model exhibits a significant enhancement in performance-surpassing the second-best baseline by 23.09% on the dice metric and achieving an improvement of 26.57% on the notably arduous CRAG and ACDC datasets.

## Méthodologie

{'study_design': "Cadre d'apprentissage contrastif par patchs (patch-wise contrastive learning) avec un modèle enseignant-étudiant (teacher-student), combinant apprentissage semi-supervisé (SemiSL) et apprentissage contrastif (CL), sans tâche prétexte explicite.", 'intervention': "Application du framework Semi-AGCL comprenant : (1) une méthode d'échantillonnage inter-patchs guidée par l'entropie moyenne des patchs (average-patch-entropy-driven inter-patch sampling) pour sélectionner les patchs positifs et négatifs et fournir un espace de caractéristiques initial robuste ; (2) une supervision par graphe d'affinité comme contrainte externe entre les pseudo-labels des réseaux étudiant et enseignant (perte L_PL_AGG) ; (3) une méthode d'échantillonnage de négatifs difficiles (hard negative sampling) rendant les échantillons négatifs similaires aux positifs mais avec des étiquettes différentes, associée à une fonction de perte basée sur le graphe d'affinité entre échantillons positifs et négatifs (perte L_RW_AGG) ; pour les données non labellisées, l'image est découpée en patchs avec augmentation forte (SA) et faible (WA).", 'control': "Pour les données labellisées, une perte supervisée standard L_sup est utilisée directement pour mettre à jour le réseau étudiant ; les baselines de comparaison incluent des méthodes existantes comme UA-MT, Double-UA, SASSNet, DTC, URPC, MC-Net, SS-Net, ainsi qu'un modèle entièrement supervisé (baseline avec annotation complète) mentionné dans l'abstract.", 'primary_outcomes': ["Précision de la segmentation d'images médicales (mesurée notamment par le coefficient Dice) avec un pourcentage minimal d'annotations (5% et 10%)"], 'secondary_outcomes': ['Généralisabilité et robustesse du modèle à travers plusieurs domaines/jeux de données'], 'statistical_methods': [], 'duration': None, 'setting': "Segmentation d'images médicales sur plusieurs jeux de données de domaines diversifiés (ex. CRAG et ACDC mentionnés dans l'abstract)"}

## Résultats

{'quantitative': [{'outcome': 'Amélioration Dice (LA dataset, 5% labeled ratio) vs second meilleur', 'value': '3.11', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe LA dataset', 'source_quote': 'we achieve significant improvements over Dice, Jaccard, HD95, and ASD (i.e., 3.11%, 2.90%, 2.19, and 0.20 over the second one, respectively)'}, {'outcome': 'Amélioration Jaccard (LA dataset, 5% labeled ratio) vs second meilleur', 'value': '2.90', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe LA dataset', 'source_quote': 'we achieve significant improvements over Dice, Jaccard, HD95, and ASD (i.e., 3.11%, 2.90%, 2.19, and 0.20 over the second one, respectively)'}, {'outcome': 'Amélioration HD95 (LA dataset, 5% labeled ratio) vs second meilleur', 'value': '2.19', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe LA dataset', 'source_quote': 'we achieve significant improvements over Dice, Jaccard, HD95, and ASD (i.e., 3.11%, 2.90%, 2.19, and 0.20 over the second one, respectively)'}, {'outcome': 'Amélioration ASD (LA dataset, 5% labeled ratio) vs second meilleur', 'value': '0.20', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe LA dataset', 'source_quote': 'we achieve significant improvements over Dice, Jaccard, HD95, and ASD (i.e., 3.11%, 2.90%, 2.19, and 0.20 over the second one, respectively)'}, {'outcome': 'Amélioration DSC (ACDC dataset, 5% labeled ratio)', 'value': '23.09', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe ACDC dataset', 'source_quote': 'we obtain a huge performance improvement of up to 23.09% in DSC'}, {'outcome': "Taille du patch d'entrée (ACDC)", 'value': '256 × 256', 'unit': 'pixels', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe ACDC dataset', 'source_quote': 'set the input patch size as 256 × 256 and the size of the zero-value region of mask M as 170 × 170'}, {'outcome': 'Taille de la région à zéro du masque M (ACDC)', 'value': '170 × 170', 'unit': 'pixels', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe ACDC dataset', 'source_quote': 'set the input patch size as 256 × 256 and the size of the zero-value region of mask M as 170 × 170'}, {'outcome': 'Batch size (ACDC)', 'value': '24', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe ACDC dataset', 'source_quote': 'The batch size, pre-training iterations, and the self-training training iterations are set as 24, 10k and 30k, respectively.'}, {'outcome': 'Itérations de pré-entraînement (ACDC)', 'value': '10k', 'unit': 'iterations', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe ACDC dataset', 'source_quote': 'The batch size, pre-training iterations, and the self-training training iterations are set as 24, 10k and 30k, respectively.'}, {'outcome': "Itérations d'auto-entraînement (self-training) (ACDC)", 'value': '30k', 'unit': 'iterations', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe ACDC dataset', 'source_quote': 'The batch size, pre-training iterations, and the self-training training iterations are set as 24, 10k and 30k, respectively.'}, {'outcome': 'Ratio de séparation des données (CARG dataset) train/test/validation', 'value': '80-10-10', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe CARG dataset', 'source_quote': 'We follow [42] to split the data into 80 -10 -10 training, test, and validation ratios.'}, {'outcome': 'Temps de calcul avec échantillonnage class confidence (cls conf) - Semi-AGCL', 'value': '1.8', 'unit': 'minutes', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe Computational Efficiency', 'source_quote': 'Semi-AGCL with class confidence (cls conf) sampling is only 1.8 minutes.'}], 'qualitative_findings': ["Le framework proposé obtient les meilleures performances sur les quatre métriques d'évaluation sur le dataset LA, surpassant significativement les autres méthodes concurrentes", "L'amélioration provient de la fonction de perte basée sur le graphe d'affinité, qui exploite la structure inhérente des données et encapsule les relations géométriques et topologiques entre les données, renforçant la compacité intra-classe et la séparabilité inter-classe", 'Sur ACDC, la méthode est clairement optimale sur tous les ratios de labellisation testés (5% et 10%)', "HD95 et ASD à 10% de ratio labellisé ont diminué par rapport à 5%, possiblement parce que la fonction de perte basée sur le graphe d'affinité nécessite une augmentation appropriée des itérations d'entraînement pour les détails complexes des contours", "Sur CARG, la méthode surpasse même U-Net entraîné avec 100% de données labellisées, alors qu'elle n'utilise que 10% de labels", "L'amélioration plus marquée à 5% qu'à 10% de labels (sur CARG et ACDC) s'explique par le fait que les tranches 2D génèrent plus de combinaisons que les données 3D, permettant un meilleur transfert de connaissances des données labellisées vers les non labellisées", "Le dataset CARG contient des images histopathologiques WS (whole slide) avec des caractéristiques de texture supplémentaires enrichissant les informations de contour pour le graphe d'affinité, expliquant une amélioration plus marquée sur ce dataset", 'La méthode proposée segmente avec précision tous les objets, avec des détails de segmentation plus proches de la vérité terrain que les autres approches de référence (visible dans les zones encadrées en rouge de la Figure 2)', "Semi-AGCL a obtenu le deuxième meilleur temps d'entraînement parmi toutes les méthodes d'apprentissage semi-supervisé existantes sur le dataset LA", 'Les performances de Semi-AGCL sont bien meilleures que DTC sur le dataset LA', 'Bien que la méthode implique une manipulation matricielle intensive, elle est hautement parallélisable, offrant un avantage en temps de calcul', "La méthode d'échantillonnage patch-wise class-centric ne nécessite pas de réglage de paramètres et n'augmente pas substantiellement le temps de calcul malgré sa complexité"], 'main_findings': ["Le framework proposé (Semi-AGCL) surpasse les méthodes état de l'art basées sur CL et SemiSL (UA-MT, Double-UA, SASSNet, DTC, URPC, MC-Net, SS-Net) ainsi que les méthodes de distillation semi-supervisées (ACTION, ARCO) sur les datasets LA, ACDC et CARG", 'Sur le dataset LA à 5% de labels, amélioration de 3.11% (Dice), 2.90% (Jaccard), 2.19 (HD95) et 0.20 (ASD) par rapport à la deuxième meilleure méthode', "Sur le dataset ACDC à 5% de labels, amélioration allant jusqu'à 23.09% en DSC", 'Sur le dataset CARG, la méthode atteint une performance supérieure à celle de U-Net entraîné avec 100% de labels, même avec seulement 10% de labels', "Le framework est efficace en termes de calcul, obtenant le deuxième meilleur temps d'entraînement parmi les méthodes comparées tout en étant nettement plus performant que DTC"]}

## Conclusions

Propose un framework de contrastive learning semi-supervisé guidé par graphe d'affinité (Semi-AGCL) pour la segmentation d'images médicales sans tâche prétexte et avec très peu d'annotations Semi-AGCL conçoit une méthode d'échantillonnage inter-patchs guidée par l'entropie moyenne des patchs, fournissant un espace de caractéristiques initial puissant sans tâche prétexte Semi-AGCL conçoit une nouvelle fonction de perte basée sur un graphe d'affinité entre les réseaux étudiant et enseignant pour améliorer la capacité de généralisation du modèle Évalué sur trois jeux de données de segmentation médicale couvrant plusieurs domaines, le framework surpasse les méthodes SOTA avec des annotations minimales, confirmant son efficacité et sa généralisabilité

## Comparisons with state-of-the-art semi-supervised learning on LA dataset.

| Method | Scans used Labeled Unlabeled DSC↑ | Metrics Jaccard↑ HD95↓ | ASD↓ |
| --- | --- | --- | --- | --- | --- | --- |
|  | 5% | 0 | 52.55 | 39.60 | 47.05 | 9.87 |
| V-Net | 10% | 0 | 82.74 | 71.70 | 13.33 | 3.26 |
|  | 100% | 0 | 91.44 | 84.55 | 5.48 | 1.53 |
| UA-MT |  |  | 82.26 | 70.98 | 13.71 | 3.82 |
| Double-UA |  |  | 82.73 | 71.73 | 12.53 | 3.80 |
| SASSNet |  |  | 81.60 | 69.63 | 16.16 | 3.58 |
| DTC URPC | 5% | 95% | 81.25 82.48 | 69.33 71.35 | 14.90 14.65 | 3.99 3.65 |
| MC-Net |  |  | 83.59 | 72.36 | 14.07 | 2.70 |
| SS-Net |  |  | 86.33 | 76.15 | 9.97 | 2.31 |
| ACTION |  |  | 86.60 | 76.20 | 9.70 | 2.24 |
| ARCO |  |  | 86.90 | 76.10 | 9.88 | 2.73 |
| Semi-AGCL |  |  | 90.44 | 79.05 | 7.78 | 2.11 |
| UA-MT |  |  | 87.79 | 78.39 | 8.68 | 2.12 |
| Double-UA |  |  | 88.53 | 78.83 | 8.42 | 2.10 |
| SASSNet |  |  | 87.54 | 78.05 | 9.84 | 2.59 |
| DTC URPC | 10% | 90% | 87.51 86.92 | 78.17 77.03 | 8.23 11.13 | 2.36 2.28 |
| MC-Net |  |  | 87.66 | 78.25 | 10.03 | 1.82 |
| SS-Net |  |  | 88.55 | 79.62 | 7.49 | 1.90 |
| ACTION |  |  | 88.7 | 78.92 | 8.11 | 2.10 |
| ARCO |  |  | 89.1 | 80.71 | 7.78 | 2.30 |
| Semi-AGCL |  |  | 90.33 | 82.53 | 6.68 | 1.78 |

## Comparisons with state-of-the-art semi-supervised learning on the ACDC dataset.

| Method | Scans used Labeled Unlabeled DSC↑ | Metrics Jaccard↑ HD95↓ | ASD↓ |
| --- | --- | --- | --- | --- | --- | --- |
|  | 5% | 0 | 47.82 | 37.01 | 31.16 | 12.66 |
| U-Net | 10% | 0 | 78.22 | 68.05 | 9.33 | 2.70 |
|  | 100% | 0 | 91.44 | 84.55 | 4.30 | 1.00 |
| UA-MT |  |  | 46.04 | 35.97 | 20.08 | 7.75 |
| Double-UA |  |  | 56.88 | 45.53 | 22.70 | 6.26 |
| SASSNet |  |  | 57.77 | 46.14 | 20.05 | 6.06 |
| DTC URPC | 5% | 95% | 56.90 55.58 | 45.66 43.66 | 23.33 13.66 | 7.38 3.78 |
| MC-Net |  |  | 62.85 | 52.29 | 7.62 | 2.33 |
| SS-Net |  |  | 65.83 | 55.38 | 6.67 | 2.28 |
| ACTION |  |  | 87.23 | 75.34 | 2.23 | 1.47 |
| ARCO |  |  | 88.51 | 76.54 | 2.20 | 1.40 |
| Semi-AGCL |  |  | 88.92 | 78.84 | 1.90 | 0.66 |
| UA-MT |  |  | 81.66 | 70.56 | 6.88 | 2.00 |
| Double-UA |  |  | 84.48 | 73.97 | 5.52 | 1.90 |
| SASSNet |  |  | 84.50 | 74.34 | 5.42 | 1.88 |
| DTC URPC | 10% | 90% | 84.29 83.11 | 73.72 72.41 | 12.81 4.84 | 4.00 1.55 |
| MC-Net |  |  | 86.47 | 77.13 | 5.50 | 1.83 |
| SS-Net |  |  | 86.78 | 77.44 | 6.00 | 1.40 |
| ACTION |  |  | 89.70 | 78.86 | 4.36 | 2.33 |
| ARCO |  |  | 92.20 | 81.96 | 3.44 | 2.53 |
| Semi-AGCL |  |  | 91.98 | 82.96 | 3.36 | 1.16 |

## Comparisons with state-of-the-art semi-supervised learning on the CARG dataset.

| Method | Scans used Labeled Unlabeled DSC↑ Jaccard↑ Metrics HD95↓ ASD↓ |
| --- | --- | --- | --- | --- | --- | --- |
|  | 5% | 0 | 40.77 | 33.57 | 30.11 | 11.66 |
| U-Net | 10% | 0 | 75.42 | 70.05 | 8.22 | 2.82 |
|  | 100% | 0 | 91.10 | 83.28 | 1.19 | 1.98 |
| UA-MT |  |  | 47.75 | 38.81 | 18.44 | 6.36 |
| Double-UA |  |  | 50.42 | 44.45 | 15.87 | 7.05 |
| SASSNet |  |  | 48.87 | 40.63 | 18.87 | 6.77 |
| DTC URPC | 5% | 95% | 50.50 58.85 | 45.60 48.89 | 15.92 13.99 | 6.51 5.95 |
| MC-Net |  |  | 58.88 | 50.50 | 9.50 | 5.25 |
| SS-Net |  |  | 58.95 | 48.88 | 10.75 | 4.95 |
| ACTION |  |  | 66.43 | 60.13 | 7.40 | 4.10 |
| ARCO |  |  | 70.63 | 63.33 | 5.20 | 3.33 |
| Semi-AGCL |  |  | 84.42 | 70.49 | 1.48 | 2.88 |
| UA-MT |  |  | 81.46 | 71.42 | 1.48 | 2.23 |
| Double-UA |  |  | 87.01 | 77.58 | 1.50 | 2.63 |
| SASSNet |  |  | 86.43 | 76.98 | 1.67 | 2.66 |
| DTC URPC | 10% | 90% | 84.13 83.36 | 75.24 71.79 | 1.83 1.61 | 2.73 2.33 |
| MC-Net |  |  | 83.30 | 72.11 | 1.61 | 2.13 |
| SS-Net |  |  | 83.40 | 70.25 | 1.88 | 2.58 |
| ACTION |  |  | 85.56 | 77.33 | 1.55 | 2.05 |
| ARCO |  |  | 88.81 | 80.90 | 1.33 | 1.88 |
| Semi-AGCL |  |  | 91.93 | 83.37 | 1.08 | 1.76 |

## Comparisons with different setting of affinity graph loss on the ACDC dataset. GK+L* =

| Equ. 3. |  |  |  |  |  |  |  |  |  |  |  | N i=1 | exp -L * 2σ 2 | in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | L P L AGG |  |  | L RW AGG |  |  | Label=5% |  |  | Label=10% |  |
| GK+L2 GK+L1 | λ||A|| * | A ii | 1:1 random | DSC↑ Jacard↑ HD95↓ ASD↓ | DSC↑ Jacard↑ | HD95↓ ASD↓ |
| - | - | - | - | - | - | 68.82 | 68.77 | 8.67 | 2.40 | 86.78 | 77.63 | 6.68 | 2.00 |
|  |  |  |  |  |  | 66.43 | 68.78 | 8.58 | 2.23 | 87.13 | 77.53 | 6.21 | 1.90 |
|  |  | ✓ | ✓ | ✓ |  | 88.92 86.06 | 78.84 75.83 | 1.90 7.88 | 0.66 1.93 | 89.98 87.93 | 80.96 78.83 | 3.66 8.44 | 1.16 2.00 |
| ✓ |  |  |  |  | ✓ | 85.56 67.78 | 73.26 68.88 | 8.53 8.54 | 2.33 2.89 | 88.10 87.78 | 79.82 77.56 | 7.78 6.70 | 1.83 2.10 |
|  |  |  | ✓ |  |  | 71.71 | 72.53 | 7.74 | 2.11 | 87.78 | 77.58 | 6.71 | 2.15 |
|  |  |  |  | ✓ |  | 70.71 | 71.33 | 8.21 | 2.10 | 87.72 | 77.50 | 5.93 | 1.98 |
|  |  |  |  |  | ✓ | 69.83 | 70.88 | 8.11 | 2.00 | 87.78 | 77.47 | 6.32 | 1.98 |
|  |  |  |  |  |  | 66.52 | 69.00 | 7.93 | 2.07 | 85.55 | 74.32 | 7.01 | 2.11 |
|  |  | ✓ | ✓ | ✓ |  | 87.93 87.78 | 78.63 75.53 | 2.33 3.53 | 1.39 1.66 | 90.12 86.59 | 80.96 74.44 | 3.68 7.43 | 1.19 2.31 |
|  | ✓ |  |  |  | ✓ | 79.35 66.52 | 71.33 69.10 | 7.01 7.53 | 1.99 2.01 | 85.58 85.75 | 75.00 74.42 | 6.66 6.83 | 2.13 1.89 |
|  |  |  | ✓ |  |  | 83.10 | 73.11 | 5.56 | 1.66 | 85.72 | 74.58 | 5.38 | 1.66 |
|  |  |  |  | ✓ |  | 82.33 | 70.31 | 6.87 | 1.77 | 85.22 | 74.46 | 6.82 | 1.89 |
|  |  |  |  |  | ✓ | 82.33 | 70.52 | 7.05 | 1.86 | 85.40 | 74.23 | 6.50 | 1.84 |

## Evaluation of diverse similarity metrics in patch sampling on the ACDC dataset.

| Similarity | Label = 5% DSC↑ Jacard↑ HD95↓ | Label = 10% ASD↓ DSC↑ Jacard↑ HD95↓ ASD↓ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cosine | 74.32 | 66.13 | 10.86 | 3.87 | 81.07 | 70.35 | 9.23 | 6.77 |
| Class Confidence | 78.85 | 69.20 | 10.02 | 3.04 | 85.51 | 74.74 | 5.09 | 3.11 |
| Entropy (Ours) | 88.92 | 78.84 | 1.90 | 0.66 | 89.98 | 80.96 | 3.66 | 0.86 |

## Quantitative comparison of computational time between our methods and other semi-supervised learning methods on Left Atrium MRI dataset. We also present the Semi-AGCL without patch-wise class centric sampling (see Semi-AGCL w/cls conf). The Params is refer to the number of trainable parameters using the same backbone.

| Method | Scaned Used Labeled Unlabeled Params (M) Training time (mins) Computational Cost |
| --- | --- | --- | --- | --- |
| VNet | 5% 100% | 0 0 | 9.44 9.44 | 36.5 37.8 |
| UA-MT |  |  | 9.44 | 67.5 |
| SASSNet |  |  | 20.46 | 73.6 |
| DTC MC-Net | 5% | 95% | 9.44 15.25 | 47.1 88.9 |
| SS-Net |  |  | 9.44 | 70.8 |
| ACTION |  |  | 10.14 | 471.9 |
| ARCO |  |  | 10.14 | 421.1 |
| Semi-AGCL(Ours) |  |  | 9.44 | 48.6 |
| Semi-AGCL w/cls conf |  |  | 9.44 | 46.8 |

### Formule


$$Let X i ∈ R M denote the i th image in a mini-batch, containing M pixels. The value of the m th pixel in image X i is denoted by X i (m).$$

### Formule


$$Ent k i,j = - 1 |P k i,j | m∈P k i,j X ′k i (m) log(X ′k i (m)) + (1 -X ′k i (m)) log(1 -X ′k i (m)),(1)$$

### Formule


$$A ij = exp - |ŷ i t -ŷj s | 2 2 2σ 2 ,(2)$$

### Formule


$$L P L AGG = N i=1 exp - |ŷ i t -ŷi s | 2 2 2σ 2 + γ||A|| * ,(3)$$

### Formule


$$K = K + ∪ K -, K + consisting of positive keys k + i with$$

### Formule


$$L q,k + ,Q = -log exp( q T •k + τ ) exp( q T •k + τ ) + n∈Q exp( q T •n τ ) , (4$$

### Formule


$$)$$

### Formule


$$∂L q,k + ,Q ∂q = - 1 τ ((1 -p k ) • k + - n∈Q p n • n),(5)$$

### Formule


$$h k = A ii n i + (1 -A ii )n j ||A ii n i + (1 -A ii )n j || 2 ,(6)$$

### Formule


$$L RW AGG = -log exp( q T •k + τ ) exp( q T •k + τ ) + h k ∈H exp( q T •h k τ ) .(7)$$

### Formule


$$L all = L sup + L reg + L P L AGG + L RW AGG ,(8)$$
