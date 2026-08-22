# A novel approach for automatic annotation of human actions in 3D point clouds for flexible collaborative tasks with industrial robots

**Auteurs** : Sebastian Krusche, Ibrahim Al Naser, Mohamad Bdiwi, Steffen Ihlenfeldt
**Année** : 2023
**DOI** : 10.3389/frobt.2023.1028329

## Résumé

Manual annotation for human action recognition with content semantics using 3D Point Cloud (3D-PC) in industrial environments consumes a lot of time and resources. This work aims to recognize, analyze, and model human actions to develop a framework for automatically extracting content semantics. Main Contributions of this work: 1. design a multi-layer structure of various DNN classifiers to detect and extract humans and dynamic objects using 3D-PC preciously, 2. empirical experiments with over 10 subjects for collecting datasets of human actions and activities in one industrial setting, 3. development of an intuitive GUI to verify human actions and its interaction activities with the environment, 4. design and implement a methodology for automatic sequence matching of human actions in 3D-PC. All these procedures are merged in the proposed framework and evaluated in one industrial Use-Case with flexible patch sizes. Comparing the new approach with standard methods has shown that the ann

## Méthodologie

{'study_design': "Développement d'un framework d'annotation automatique (structure multi-couches de classificateurs DNN, GUI, méthodologie de mise en correspondance de séquences) évalué expérimentalement via une étude statistique comparative (système automatique vs système de référence multi-capteurs) et une évaluation qualitative, ainsi qu'une comparaison de temps d'annotation manuelle vs automatique sur 6 scénarios de test", 'intervention': "Framework d'annotation automatique combinant segmentation d'arrière-plan 3D, segmentation/suivi d'objets dynamiques par filtres de Kalman, projection 3D-2D, classification par des classificateurs IA (OpenPose, AlphaPose, DarkNet) et estimation de pose humaine", 'control': "Comparaison avec un système de référence multi-capteurs (Multi-Sensor Reference System) limité à la détection de personnes en 3D, et comparaison avec des méthodes standards d'annotation manuelle (approche en deux étapes avec bounding boxes, et approche par interaction vocale/souris)", 'primary_outcomes': ['Précision de détection/classification personne vs non-personne comparée au système de référence', "Temps d'annotation (accélération du processus par rapport à l'annotation manuelle)"], 'secondary_outcomes': ["Qualité du suivi (tracking) des objets/personnes sur l'ensemble de la séquence", 'Temps de traitement par étape (estimation de pose 2D, mise en correspondance 2D, projection 3D, suivi 3D)'], 'statistical_methods': ["Étude statistique comparative (moyennes et médianes du nombre d'objets détectés par étape de traitement)", 'Comparaison qualitative des taux de classification correcte'], 'duration': None, 'setting': 'Cellule de collaboration homme-robot (HRC) du Fraunhofer IWU, reproduisant une cellule robotique sans clôture de protection dans un environnement de production industrielle automobile, avec 4 capteurs 3D installés'}

## Résultats

{'quantitative': [{'outcome': "Accélération du processus d'annotation grâce à l'automatisation", 'value': '5.2', 'unit': 'facteur multiplicatif', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Conclusion', 'source_quote': 'the annotation process can be accelerated by 5.2 times through automation'}, {'outcome': 'Précision de la distinction personne / non-personne', 'value': '90', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Qualitative assessment', 'source_quote': 'it can generally be concluded that the distinction between non-person and person is accurate in 90% of the scenarios'}, {'outcome': 'Temps moyen de traitement écoulé par objet (annotation automatique complète)', 'value': '207', 'unit': 'ms', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Manual annotation vs. automatic annotation', 'source_quote': 'In total, the average elapsed time per object is 207 ms.'}, {'outcome': 'Temps de classification de la pose humaine par image (OpenPose)', 'value': '84', 'unit': 'ms', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Manual annotation vs. automatic annotation', 'source_quote': 'The times per image are about 84 ms for OpenPose and about 94 ms for AlphaPose.'}, {'outcome': 'Temps de classification de la pose humaine par image (AlphaPose)', 'value': '94', 'unit': 'ms', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Manual annotation vs. automatic annotation', 'source_quote': 'The times per image are about 84 ms for OpenPose and about 94 ms for AlphaPose.'}, {'outcome': 'Temps de mise en correspondance des poses 2D par objet', 'value': '2', 'unit': 'ms', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Manual annotation vs. automatic annotation', 'source_quote': 'matching the 2D poses takes only a short time of about 2 ms per object'}, {'outcome': "Temps de projection des résultats 2D vers l'espace 3D", 'value': '17-35', 'unit': 'ms', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Manual annotation vs. automatic annotation', 'source_quote': 'The projection of the 2D results into the 3D space requires an average time of 17-35 ms.'}, {'outcome': 'Temps de suivi (tracking) des objets 3D', 'value': '3', 'unit': 'ms', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Manual annotation vs. automatic annotation', 'source_quote': 'Similar to matching the 2D poses, the 3D object tracking requires a short time of about 3 ms.'}, {'outcome': 'Temps de vérification manuelle (référence issue de la littérature, non mesuré par les auteurs)', 'value': '2.2', 'unit': 's', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Manual annotation vs. automatic annotation', 'source_quote': 'a time of 2.2 s was chosen, which was taken from the publication (Papadopoulos et al., 2016)'}, {'outcome': 'Nombre de jeux de données collectés', 'value': '31 (mono-personne) / 27 (multi-personnes)', 'unit': 'data sets', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Experiments, Experiment setup', 'source_quote': 'The recordings resulted in 31 data sets for single-person and 27 for multi-person scenarios.'}], 'qualitative_findings': ["Les échelles ou objets similaires sont fréquemment mal classés comme des personnes selon leur forme (Figure 10: 'Ladder is recognized as a person if the bounding box includes the person.')", 'Les scénarios plus complexes entraînent des résultats de suivi et de classification moins précis', "Les écarts de nombre de personnes détectées dans les scénarios complexes ne sont pas nécessairement dus à une mauvaise classification, mais plutôt à des erreurs de suivi ou à la présence de personnes non pertinentes en périphérie de la scène (ex. superviseur de l'enregistrement)"], 'main_findings': ["Le framework d'annotation automatique proposé accélère le processus d'annotation d'un facteur 5.2 par rapport aux méthodes standards d'annotation manuelle", 'La distinction personne/non-personne est correcte dans 90% des scénarios testés', 'Les valeurs moyennes obtenues par le système automatique ne montrent pas de différences significatives majeures avec celles du système de référence multi-capteurs', "Le temps de classification de la pose humaine (OpenPose/AlphaPose) constitue l'étape la plus consommatrice de temps du pipeline automatique"]}

## Conclusions

Le framework d'annotation automatique proposé permet de générer efficacement des annotations de haute qualité pour des jeux de données multi-capteurs 3D avec des séquences d'actions complexes La structure multi-couches de classificateurs DNN permet de détecter facilement les humains et objets dynamiques et de classifier/suivre les séquences d'actions sans que l'annotateur ait à annoter manuellement la pose humaine L'interface graphique intuitive permet à l'utilisateur de vérifier et corriger les résultats du processus d'annotation automatisé La méthodologie de mise en correspondance automatique des séquences d'actions permet de corriger automatiquement les erreurs de suivi et de classification issues de la structure multi-couches L'approche proposée peut accélérer le processus d'annotation jusqu'à un facteur 5.2 grâce à l'automatisation

## Test scenarios to investigate the performance of the annotation tool.

| Scenario-Nr.: | Scenario title | Action types | Active subjects |
| --- | --- | --- | --- |
| 1 | Person walks into robot cell | Standing (static), walking | 1 |
| 2 | Person walks with item | Standing (static), walking, setting up ladder | 1 |
| 3 | Person pushes a transport cart | Standing (static), walking, pushing transport cart | 1 |
| 4 | 2 persons walk into robot cell | Standing (static), walking | 2 |
| 5 | 2 persons hand over an item | Standing (static), walking, handing over item | 2 |
| 6 | 2 persons with a transport cart | Standing (static), walking, Pushing transport cart | 2 |

## Final summary of the statistical evaluation.

|  | Dataset |  |  | 3D person tracking |  | Reference |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | information |  |  | (average number of |  | (average number of |
|  |  |  |  |  | processed objects) |  | processed objects) |  |
| Scenario Number | Number of Datasets | Scenario Mode | Number Subjects | Frames | Total | Valid (Person) | Invalid | Raw | Filtered | Person | Non |
|  |  |  |  |  |  |  |  |  |  | Person |
| Scenario 1 | 11 | single | 1 | 167 | 4,0 | 1.5 | 2.5 | 1.5 | 1.1 | 1.1 | 0.0 |
| Scenario 2 | 10 | single | 1 | 182 | 3.9 | 1.4 | 2.5 | 4.8 | 1.8 | 1.4 | 0.4 |
| Scenario 3 | 10 | single | 1 | 236 | 8.4 | 1.9 | 6.5 | 5.3 | 2.0 | 0.7 | 1.3 |
| Scenario 4 | 9 | multi | 2 | 179 | 8.6 | 2.9 | 5.7 | 2.8 | 2.2 | 2.2 | 0.0 |
| Scenario 5 | 8 | multi | 2 | 182 | 10.4 | 3.5 | 6.9 | 4.8 | 2.5 | 2.3 | 0.3 |
| Scenario 6 | 8 | multi | 2 | 259 | 13.8 | 3.8 | 10.0 | 7.9 | 3.3 | 1.8 | 1.6 |

## Summary of the average time measured for each processing step per scenario. Bold values are the average time over all scenarios.

|  | Dataset information |  |  |  |  | Elapsed time in ms |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | 2D pose | 2D person | 3D | 3D object | Total |
|  |  |  |  |  | estimation | matching | projection | fusion and | time |
|  |  |  |  |  |  |  |  |  | tracking |  |
| Scenario | Number | Scenario | Number | Frames Open | Alpha |  |  |  |  |
| number | of | mode | subjects |  | pose | pose |  |  |  |  |
|  | datasets |  |  |  |  |  |  |  |  |  |
| Scenario 1 | 11 | single | 1 | 167 | 84.0 | 92.9 | 0.9 | 25.6 | 2.3 | 205.6 |
| Scenario 2 | 10 | single | 1 | 182 | 83.9 | 92.7 | 1.3 | 37.2 | 3.1 | 218.2 |
| Scenario 3 | 10 | single | 1 | 236 | 84.0 | 93.2 | 1.4 | 30.9 | 3.0 | 212.5 |
| Scenario 4 | 9 | multi | 2 | 179 | 83.7 | 95.4 | 1.4 | 18.7 | 5.4 | 204.7 |
| Scenario 5 | 8 | multi | 2 | 182 | 83.8 | 95.6 | 1.1 | 17.5 | 3.1 | 201.1 |
| Scenario 6 | 8 | multi | 2 | 259 | 83.9 | 95.6 | 1.2 | 19.4 | 3.1 | 203.2 |
|  |  |  |  |  |  |  |  |  | Mean | 207,6 |

## Qualitative comparison of the presented automatic annotation approach with standard methods.

|  | Two-stage approach (Gygli | Box & speak (Gygli and | Ours (DNN classifiers + human verification |
| --- | --- | --- | --- |
|  | and Ferrari, 2020) | Ferrari, 2020) | (Papadopoulos et al., 2016)) |
| Time/box | 12.5 s | 6.5 s | 2.4 s (0.207 s + 2.2 s) |
| Acceleration of our approach | x5,2 | x2,7 | - |
| compared to standard methods |  |  |  |
