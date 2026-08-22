# Detecting pediatric appendicular fractures using artificial intelligence.

**Auteurs** : Nezih Kavak, Rasime Pelin Kavak, Bülent Güngörer, Berna Turhan, Sümeyya Duran Kaymak, Evrim Duman, Serdar Çelik
**Année** : 2024
**DOI** : 10.1590/1806-9282.20240523

## Résumé

The primary objective was to assess the diagnostic accuracy of a deep learning-based artificial intelligence model for the detection of acute appendicular fractures in pediatric patients presenting with a recent history of trauma to the emergency department. The secondary goal was to examine the effect of assistive support on the emergency doctor's ability to detect fractures.

## Méthodologie

{'study_design': "Étude rétrospective utilisant un modèle de réseau de neurones convolutif (CNN) YOLOv8 entraîné sur des radiographies annotées par trois radiologistes (16, 10 et 9 ans d'expérience) selon un critère de consensus (intersection over union > 50%). Le modèle a ensuite été testé sur un sous-ensemble de radiographies, et la performance d'un médecin urgentiste a été comparée avec et sans assistance de l'IA.", 'intervention': "Lecture des radiographies assistée par le modèle d'IA YOLOv8", 'control': "Lecture des radiographies sans assistance de l'IA (médecin urgentiste seul)", 'primary_outcomes': ['Précision diagnostique (sensibilité, spécificité, mAP50, F1 score) du modèle YOLOv8 pour la détection de fractures'], 'secondary_outcomes': ["Effet de l'assistance par IA sur la sensibilité et l'exactitude des lectures du médecin urgentiste"], 'statistical_methods': ['Analyse de la matrice de confusion', 'Calcul de sensibilité, spécificité, exactitude, F1 score', 'mAP50 (mean Average Precision)', 'AUC (Area Under the Curve)'], 'duration': 'Collecte des données du 15 janvier 2015 au 30 décembre 2020', 'setting': "Service des urgences de l'hôpital Dışkapı Yıldırım Beyazıt Research and Training Hospital"}

## Résultats

{'quantitative': [{'outcome': 'mAP50 du modèle YOLOv8', 'value': '89', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The design of the YOLOv8 model yielded significant performance metrics, including a mAP50 of 89%, specificity at 92%, sensitivity reaching 90%, and an F1 score of 90%.'}, {'outcome': 'Spécificité du modèle YOLOv8', 'value': '92', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The design of the YOLOv8 model yielded significant performance metrics, including a mAP50 of 89%, specificity at 92%, sensitivity reaching 90%, and an F1 score of 90%.'}, {'outcome': 'Sensibilité du modèle YOLOv8', 'value': '90', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The design of the YOLOv8 model yielded significant performance metrics, including a mAP50 of 89%, specificity at 92%, sensitivity reaching 90%, and an F1 score of 90%.'}, {'outcome': 'F1 score du modèle YOLOv8', 'value': '90', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The design of the YOLOv8 model yielded significant performance metrics, including a mAP50 of 89%, specificity at 92%, sensitivity reaching 90%, and an F1 score of 90%.'}, {'outcome': 'Exactitude (accuracy) du modèle YOLOv8 selon la matrice de confusion', 'value': '93 et 95', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The analysis of the confusion matrix from testing data revealed that the YOLOv8-informed model attained accuracies of 93 and 95% in identifying fractures (Table 1).'}, {'outcome': 'Sensibilité des lectures assistées par IA', 'value': '97.0', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': '+3.3% par rapport aux lectures sans IA', 'source_section': 'Results', 'source_quote': 'the integration of AI with expert evaluation from an emergency doctor enhanced the sensitivity of assisted readings to 97.0%, marking an improvement of 3.3% over the sensitivity of readings without AI assistance, which stood at 93.7%.'}, {'outcome': 'Sensibilité des lectures sans IA', 'value': '93.7', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'the sensitivity of readings without AI assistance, which stood at 93.7%.'}, {'outcome': 'Exactitude des lectures assistées par IA', 'value': '94.9', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': '+6.9% par rapport aux lectures sans IA', 'source_section': 'Results', 'source_quote': 'Similarly, the accuracy of readings with AI support was elevated to 94.9%, surpassing the accuracy of unassisted readings by 6.9%, which was previously 88% (Table 2).'}, {'outcome': 'Exactitude des lectures sans IA', 'value': '88', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'the accuracy of unassisted readings by 6.9%, which was previously 88% (Table 2).'}, {'outcome': "AUC de l'IA utilisée par un médecin urgentiste", 'value': '0.93', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The application of AI resulted in an AUC of 0.93 when used by an emergency doctor.'}, {'outcome': "Taux de faux positifs de l'algorithme IA", 'value': '7.6', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The AI algorithm exhibited a 7.6% rate of FP, whereas the combination of an emergency doctor and AI assistance was associated with a 3% rate of FP.'}, {'outcome': 'Taux de faux positifs médecin urgentiste + IA', 'value': '3', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The AI algorithm exhibited a 7.6% rate of FP, whereas the combination of an emergency doctor and AI assistance was associated with a 3% rate of FP.'}], 'qualitative_findings': [], 'main_findings': ['Le modèle YOLOv8 a démontré de solides capacités diagnostiques pour identifier les fractures appendiculaires chez les patients pédiatriques', "L'efficacité diagnostique des médecins urgentistes est notablement améliorée lorsqu'elle est complétée par un logiciel d'IA, surpassant les performances de l'IA ou des médecins urgentistes seuls"]}

## Conclusions

Le modèle YOLOv8 démontre une efficacité substantielle dans l'identification des fractures chez les patients pédiatriques, en particulier lorsqu'il est utilisé pour augmenter les capacités diagnostiques des médecins urgentistes.

## YOLOv8 model performance comparison based on the training datasets.

| You Only |
| --- |
| Look Once v8 |

## Artificial intelligence Total sets True positive True negative False positive False negative Sensitivity (95%CI)

|  |  |  |  |  |  |  | Specificity | Accuracy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  | (95%CI) | (95%CI) |
| All | 5,150 | 3,712 | 921 | 352 | 163 | 95.8% | 72.3% | 90.0% |
| Fracture | 850 | 506 | 259 | 72 | 13 | 97.5% | 78.2% | 90.0% |
| Not fracture | 4,300 | 3,208 | 662 | 280 | 150 | 95.5% | 70.3% | 90.0% |

## Emergency doctor and YOLOv8 model performance comparison based on the test datasets.

|  |  |  |  | Without artificial intelligence |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Total sets | True positive | True negative | False positive | False negative | Sensitivity (95%CI) | Specificity (95%CI) | Accuracy (95%CI) |
|  | All | 1,000 | 655 | 230 | 71 | 44 | 93.7% | 75.2% | 88.0% |
|  | Fracture | 400 | 225 | 118 | 38 | 19 | 92.2% | 75.6% | 85.8% |
| Emergency | Not fracture | 600 | 430 | 112 | 33 | 25 | 94.5% | 77.2% | 90.3% |
| doctor |  |  |  | With artificial intelligence |  |  |  |
|  |  | Total sets | True positive | True negative | False positive | False negative | Sensitivity (95%CI) | Specificity (95%CI) | Accuracy (95%CI) |
|  | All | 1,000 | 688 | 261 | 30 | 21 | 97.0% | 89.7% | 94.9% |
|  | Fracture | 400 | 239 | 132 | 21 | 8 | 96.8% | 86.3% | 92.8% |
|  | Not fracture | 600 | 449 | 129 | 9 | 13 | 97.2% | 93.5% | 96.3% |
