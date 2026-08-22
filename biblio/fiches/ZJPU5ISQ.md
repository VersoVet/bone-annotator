# A localization strategy combined with transfer learning for image annotation

**Auteurs** : Zhiqiang Chen, Leelavathi Rajamanickam, Jianfang Cao, Aidi Zhao, Xiaohui Hu
**Année** : 2021
**DOI** : 10.1371/journal.pone.0260758

## Résumé

This study aims to solve the overfitting problem caused by insufficient labeled images in the automatic image annotation field. We propose a transfer learning model called CNN-2L that incorporates the label localization strategy described in this study. The model consists of an InceptionV3 network pretrained on the ImageNet dataset and a label localization algorithm. First, the pretrained InceptionV3 network extracts features from the target dataset that are used to train a specific classifier and fine-tune the entire network to obtain an optimal model. Then, the obtained model is used to derive the probabilities of the predicted labels. For this purpose, we introduce a squeeze and excitation (SE) module into the network architecture that augments the useful feature information, inhibits useless feature information, and conducts feature reweighting. Next, we perform label localization to obtain the label probabilities and determine the final label set for each image. During this proces

## Méthodologie

{'study_design': 'Modèle de transfer learning (CNN-2L) combinant un réseau InceptionV3 pré-entraîné sur ImageNet, un module squeeze-and-excitation (SE) pour la repondération des caractéristiques, et une stratégie de localisation de labels pour déterminer le nombre optimal de labels prédits (valeur K)', 'intervention': 'Application du modèle CNN-2L : extraction de caractéristiques via InceptionV3 pré-entraîné et fine-tuning sur le jeu de données cible, intégration du module SE pour la repondération des caractéristiques, puis localisation des labels selon la probabilité prédite et la valeur K optimale', 'control': 'Comparaison avec des méthodes traditionnelles (MBRM, JEC, GMM-MB, méthode de fusion multifeature et similarité sémantique) et des méthodes de deep learning récentes (SEM, Weight-KNN, AHL)', 'primary_outcomes': ['Précision (Precision, P)', 'Rappel (Recall, R)', 'Mesure F1 (F1 measure)'], 'secondary_outcomes': [], 'statistical_methods': ['Calcul de précision (P)', 'Calcul de rappel (R)', 'Calcul de la mesure F1', "Expérience d'ablation pour évaluer l'effet du module SE", 'Comparaison expérimentale de différentes valeurs de K'], 'duration': None, 'setting': 'Expériences réalisées sur les jeux de données publics Corel5k (multilabel image dataset) et MIML (miml-image-data)'}

## Résultats

{'quantitative': [{'outcome': 'Amélioration de la précision (Corel5k) vs MBRM et méthode multifeature/similarité sémantique [27]', 'value': '18% et 15%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'the P score of the CNN-2L method proposed in this study is improved by 18% and 15% compared with those of the classical model MBRM [31] and the multifeature fusion and semantic similarity method in [27], respectively'}, {'outcome': 'Amélioration du rappel (Corel5k) vs MBRM et JEC', 'value': '13% et 6%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The R score is improved by 13% and 6% compared with those of the MBRM [31] and JEC [32] models, respectively.'}, {'outcome': 'Amélioration de la précision (Corel5k) vs Weight-KNN et SEM', 'value': '20% et 5%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'Compared with those of the Weight-KNN [33] and SEM [30] models proposed in the past two years, the P score in this study is improved by 20% and 5%, respectively.'}, {'outcome': 'Amélioration de la mesure F1 (Corel5k) vs SEM', 'value': '1%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'the F1 measure of CNN-2L is 1% higher than that of SEM [30]'}, {'outcome': 'Amélioration de la précision (MIML) vs MBRM et Weight-KNN, et F1 vs JEC', 'value': '29%, 16% (précision) ; 24% (F1)', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'the method proposed in this study increases the precision by 29% and 16% compared with the methods used in MBRM [31] and Weight-KNN [33], respectively; it also increases the comprehensive index F1 by 24% compared with JEC [32]'}, {'outcome': 'Amélioration globale précision, rappel et F1 (Corel5k) vs autres méthodes', 'value': '42%, 38%, 44%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'the proposed CNN-2L model substantially improves the precision, recall and F1 measure results-by 42%, 38% and 44% compared with other methods'}, {'outcome': 'Amélioration de la précision (Corel5k) vs SEM', 'value': '5%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'The CNN-2L model also improves the precision by 5% compared with the recently proposed SEM [30].'}, {'outcome': 'Performance sur MIML : précision, rappel, F1', 'value': '82% (précision), 75% (rappel), 78% (F1)', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'On the MIML dataset, the model proposed in this study achieves a precision of 82%, a recall rate of 75% and an F1 value of 78%; compared with AHL [34], it increases the precision by 11%.'}, {'outcome': "Effet du module SE (expérience d'ablation) sur la précision", 'value': 'amélioration moyenne de 1%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'the precision of the model with the SE module improves by an average of 1% compared with the model without the SE module'}, {'outcome': 'Nombre moyen de labels par image', 'value': '3.4 (Corel5k), 1.2 (MIML)', 'unit': 'labels/image', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'the average number of labels in the Corel5k dataset is 3.4, while that in the MIML dataset is 1.2'}], 'qualitative_findings': ["Pour les catégories aux caractéristiques distinctes (tulip, polar, ground), la précision d'annotation de tous les modèles peut atteindre 100%", "Pour des labels comme flight et plane, la précision d'annotation est faible en raison du nombre limité d'images et de la similarité des caractéristiques entre catégories", "Pour certains labels comme branches et windows, l'ajout du module SE n'améliore pas la précision car les images associées ne sont pas parfaitement annotées"], 'main_findings': ['Le modèle CNN-2L proposé améliore significativement la précision, le rappel et la mesure F1 par rapport aux méthodes traditionnelles (MBRM, JEC) et aux méthodes de deep learning récentes (Weight-KNN, AHL) sur le jeu de données Corel5k', "Le module SE améliore en moyenne la précision d'annotation de 1% par label", 'La valeur optimale de K (nombre de labels prédits) est K=3 pour Corel5k et K=1 pour MIML, privilégiant la précision au détriment potentiel du rappel', "CNN-2L n'améliore pas le rappel par rapport au modèle SEM mais améliore la mesure F1 de 1%"]}

## Conclusions

Le modèle de transfer learning basé sur une stratégie de localisation de labels (CNN-2L) est efficace pour l'annotation automatique d'images multilabels L'utilisation d'un modèle CNN pré-entraîné via transfer learning résout le problème d'insuffisance des jeux de données Le module SE, en repondérant les canaux de caractéristiques, inhibe les caractéristiques non pertinentes et renforce les caractéristiques utiles La stratégie de localisation de labels résout le problème des ensembles de labels vides causé par un seuil fixe Le modèle CNN-2L améliore substantiellement la précision, le rappel et la mesure F1 par rapport aux méthodes existantes sur Corel5k, et améliore la précision de 11% par rapport à AHL sur MIML

## Table 1 . Experimental results for different K values.

|  | K | P | R | F1 |
| --- | --- | --- | --- | --- |
| Corel5k | 3 � | 0.42 | 0.38 | 0.40 |
|  | 4 | 0.41 | 0.43 | 0.42 |
|  | 5 | 0.39 | 0.50 | 0.44 |
| MIML | 1 � | 0.826 | 0.759 | 0.791 |
|  | 2 | 0.803 | 0.785 | 0.794 |
|  | 3 | 0.786 | 0.810 | 0.798 |

## Table 2 . Comparison of annotation precision for single category labels using different algorithms.

| Dataset | Frequency | Label category |  |  | Annotation precision |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Literature [27] | GMM-MB [28] | Literature [29] | SEM [30] | CNN-2 L |
| Corel5k | Low-frequency labels | tulip | 0.875 | 0.896 | 0.962 | 0.963 | 1.000 |
|  |  | sun | 0.597 | 0.632 | 0.666 | 0.654 | 0.684 |
|  |  | sea | 0.786 | 0.775 | 0.769 | 0.792 | 0.800 |
|  |  | palm | 0.729 | 0.730 | 0.764 | 0.835 | 1.000 |
|  |  | fence | 0.928 | 0.922 | 0.950 | 0.926 | 1.000 |
|  |  | runway | 0.762 | 0.769 | 0.823 | 0.871 | 1.000 |
|  |  | flight | 0.369 | 0.413 | 0.463 | 0.467 | 0.500 |
|  |  | head | 0.425 | 0.467 | 0.521 | 0.538 | 0.600 |
|  |  | black | 0.551 | 0.568 | 0.600 | 0.619 | 0.625 |
|  |  | ground | 0.913 | 0.909 | 0.948 | 0.949 | 1.000 |
|  |  | coral | 0.612 | 0.626 | 0.641 | 0.653 | 0.650 |
|  |  | ocean | 0.655 | 0.673 | 0.687 | 0.708 | 0.737 |
|  |  | tiger | 0.926 | 0.941 | 0.962 | 0.961 | 0.950 |
|  |  | fox | 0.779 | 0.776 | 0.777 | 0.783 | 0.800 |
|  |  | arctic | 0.906 | 0.914 | 0.925 | 0.990 | 1.000 |
|  |  | arch | 0.527 | 0.538 | 0.562 | 0.605 | 0.667 |
|  |  | pillar | 0.728 | 0.753 | 0.768 | 0.792 | 0.833 |
|  | Medium-frequency labels | mountain | 0.564 | 0.671 | 0.608 | 0.612 | 0.636 |
|  |  | boats | 0.589 | 0.597 | 0.607 | 0.643 | 0.692 |
|  |  | leaf | 0.628 | 0.615 | 0.644 | 0.659 | 0.714 |
|  |  | birds | 0.763 | 0.779 | 0.778 | 0.791 | 0.852 |
|  |  | bridge | 0.772 | 0.792 | 0.808 | 0.828 | 0.875 |
|  |  | plane | 0.695 | 0.716 | 0.740 | 0.754 | 0.789 |
|  |  | bear | 0.624 | 0.710 | 0.685 | 0.667 | 0.719 |
|  |  | polar | 0.891 | 0.926 | 0.923 | 0.904 | 1.000 |
|  |  | flowers | 0.652 | 0.679 | 0.692 | 0.735 | 0.721 |
|  |  | field | 0.593 | 0.605 | 0.654 | 0.637 | 0.680 |
|  |  | plants | 0.561 | 0.629 | 0.641 | 0.668 | 0.643 |
|  |  | pool | 0.735 | 0.731 | 0.769 | 0.729 | 0.786 |
|  |  | cat | 0.816 | 0.847 | 0.866 | 0.887 | 0.900 |
|  |  | ruins | 0.682 | 0.735 | 0.753 | 0.815 | 0.789 |
|  |  | cars | 0.694 | 0.756 | 0.739 | 0.742 | 0.777 |
|  |  | horses | 0.847 | 0.793 | 0.843 | 0.896 | 0.933 |
|  | high-frequency labels | sky | 0.353 | 0.351 | 0.394 | 0.456 | 0.475 |
|  |  | tree | 0.475 | 0.472 | 0.491 | 0.529 | 0.618 |
|  |  | people | 0.389 | 0.468 | 0.524 | 0.537 | 0.550 |
| MIML | all labels | desert | 0.725 | 0.769 | 0.807 | 0.813 | 0.826 |
|  |  | mountains | 0.766 | 0.801 | 0.824 | 0.816 | 0.832 |
|  |  | sea | 0.713 | 0.796 | 0.792 | 0.835 | 0.823 |
|  |  | sunset | 0.812 | 0.835 | 0.843 | 0.856 | 0.852 |
|  |  | trees | 0.801 | 0.823 | 0.822 | 0.815 | 0.819 |
| https://doi.org/10.1371/journal.pone.0260758.t002 |  |  |  |  |  |

## Table 3 . Experimental comparison of various automatic image-labeling methods.

| Method |  | Corel5k |  |  | MIML |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | P | R | F1 | P | R | F1 |
| MBRM [31] | 0.24 | 0.25 | 0.24 | 0.53 | 0.55 | 0.54 |
| JEC [32] | 0.27 | 0.32 | 0.29 | 0.54 | 0.54 | 0.54 |
| Literature [27] | 0.27 | 0.33 | 0.28 | 0.550 | 0.56 | 0.56 |
| Weight-KNN [33] | 0.22 | 0.15 | 0.18 | 0.66 | 0.69 | 0.67 |
| AHL [34] | 0.31 | 0.38 | 0.34 | 0.71 | 0.73 | 0.72 |
| SEM [30] | 0.37 | 0.52 | 0.43 | 0.77 | 0.79 | 0.78 |
| CNN-2L | 0.42 | 0.38 | 0.44 | 0.82 | 0.75 | 0.78 |

## Due to copyright consideration, the images actually analyzed in the experiment are not provided. https://doi.org/10.1371/journal.pone.0260758.t004

| Corel5K | sun water clouds | sun water clouds | sun water birds | sun sky water |
| --- | --- | --- | --- | --- |
|  | birds |  | sunset sea | clouds birds |
|  | Plane jet f-16 | Plane jet f-16 | Plane grass runway f-16 jet | Plane tails jet runway sky |
|  | Sky tree flowers | Sky tree flowers | Sky tree flowers clouds house | Sky tree flowers house clouds |
|  | Tulip |  |  |  |
|  | Bear polar close-up face | Bear polar snow | Bear face black polar snow | Bear face black close-up snow |
| MIML | Sea sunset | Sea sunset | Water sea boat people mountains | Sea water boat sunset mountains |
|  | Desert | Desert | Mountains | mountains |
|  |  |  | Desert sky grass road | desert sky grass road |
| Note: |  |  |  |  |

### Formule


$$Sigmoid ðxÞ ¼ 1 1 þ expðÀ xÞ ;ð1Þ$$

### Formule


$$z c ¼ F sq ðu c Þ ¼ 1 H � W X H i¼1 X W j¼1 u c ði; jÞ:ð2Þ$$

### Formule


$$s ¼ F ex ðz; WÞ ¼ sðgðz; WÞÞ ¼ sðW 2 dðW 1 zÞÞð3Þ$$

### Formule


$$X c ¼ F scale ðu c ; s c Þ ¼ s c � u cð4Þ$$
