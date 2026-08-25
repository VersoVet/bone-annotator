# Labels4Rails: A Railway Image Annotation Tool and Associated Reference Dataset

**Auteurs** : Tina Hiebert, Florian Hofstetter, Carsten Thomas, Savera Mushtaq, Eero Kaan, Biranavan Parameswaran
**Année** : 2025
**DOI** : 10.3390/data10120210

## Résumé

The development of autonomous train systems relies heavily on machine learning (ML) models, which in turn depend on large, high-quality annotated datasets for training and evaluation. The railway domain lacks adequate public datasets and efficient annotation tools. To address this gap, we present Labels4Rails, a tool designed specifically for the annotation of railway scenes. It captures track topology, switch states including switch directions, and informational tags regarding the images’ content and leverages consistent camera perspectives and the fixed track geometries inherent to railways for annotation efficiency. We used Labels4Rails to create the L4R_NLB reference dataset from Norwegian railway footage. The dataset contains 10,253 annotated images across four seasons, including 1415 switch annotations. Both the tool and dataset are publicly available.

## Méthodologie

{'study_design': "Développement d'un outil d'annotation (Labels4Rails) suivi d'une étude de cas d'application pour créer un dataset (L4R_NLB), avec une expérience comparative mesurant le temps d'annotation", 'intervention': "Annotation d'images ferroviaires avec l'outil Labels4Rails (topologie des voies, états des aiguillages, tags informationnels)", 'control': 'Annotation des mêmes images avec un outil générique, CVAT', 'primary_outcomes': ['Temps requis pour annoter les images (voies, aiguillages, tags)'], 'secondary_outcomes': ["Facilité d'utilisation de l'outil", "Utilisabilité des fonctionnalités d'annotation automatisée basées sur l'IA"], 'statistical_methods': [], 'duration': None, 'setting': "Annotation réalisée avec la participation d'un grand nombre d'étudiants, y compris certains sans formation technique"}

## Résultats

{'quantitative': [{'outcome': "Nombre d'images annotées dans le dataset L4R_NLB", 'value': '10253', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The dataset contains 10,253 annotated images across four seasons, including 1415 switch annotations.'}, {'outcome': "Nombre d'annotations d'aiguillages", 'value': '1415', 'unit': 'annotations', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The dataset contains 10,253 annotated images across four seasons, including 1415 switch annotations.'}], 'qualitative_findings': ['Le tableau (Figure 2, Tables 2 et 3) mentionne des observations comparatives entre Labels4Rails et CVAT, mais les valeurs numériques détaillées ne sont pas fournies dans le texte fourni'], 'main_findings': ["Labels4Rails s'est avéré facile à utiliser, y compris par des étudiants sans formation technique", "L'outil réduit considérablement l'effort requis pour annoter des données d'images", "Le dataset L4R_NLB constitue une contribution importante aux jeux de données d'entraînement ML disponibles publiquement pour la conduite automatisée ferroviaire"]}

## Conclusions

Labels4Rails représente une avancée significative pour une solution d'annotation d'images efficace, adaptée à la conduite automatisée ferroviaire L'outil réduit considérablement l'effort requis pour annoter des données d'images et permet la création de jeux de données d'entraînement ML pertinents avec un effort acceptable Le dataset L4R_NLB peut être utilisé efficacement pour de nombreuses tâches d'entraînement dans le contexte des systèmes de perception ML pour trains autonomes, mais doit parfois être combiné avec d'autres datasets pour obtenir la variété nécessaire de scènes et de types d'objets

## Time required for annotation (maximum, minimum and weighted average), comparing CVAT and Labels4Rails (manual annotation).

|  | CVAT |  |  | Labels4Rails (Manual) |  |
| --- | --- | --- | --- | --- | --- | --- |
| max | min | avg | max | min | avg | gain |

## Intervals of the Time of Day tag for each season. The numbers denote the indices of the images.

|  | Twilight | Day | Twilight | Night |
| --- | --- | --- | --- | --- |
| Spring | - | 0-7154 | - | - |
| Summer | - | 0-7154 | - | - |
| Autumn | 0-469 | 470-7154 | - | - |
| Winter | 0-819 | 820-6084 | 6085-6936 | 6937-7154 |

## Tag statistics of the L4R_NLB dataset.

| Track Layout | Light | Weather |  |
| --- | --- | --- | --- |
| straight | 2991 natural | 9947 sunny | 2522 |
| curve | 7734 artificial | 217 rainy | 1249 |
| straight and curve | 735 dark | 1155 cloudy | 7252 |
| parallel structures | 281 bright | 929 snow | 3273 |
| orthogonal structures | 556 hard shadows | 1165 foggy | 21 |
| unknown | 257 uniform | 8355 unknown | 421 |
|  | unknown | 57 |  |
| Environment | Time of Day | Additional |  |
| rural | 9453 twilight | 958 obstruction | 547 |
| urban | 940 day | 8781 |  |
| station | 629 night | 172 |  |
| underground | 547 unknown | 342 |  |
| unknown | 0 |  |  |

## Switch and track statistics of the L4R_NLB dataset.

| Switch Type (Merge) | Switch Type (Fork) |  |
| --- | --- | --- |
| Left | 185 Left | 150 |
| Right | 214 Right | 162 |
| Unknown | 430 Unknown | 274 |
| Total | 829 Total | 586 |
| Images with Merges | 666 Images with Forks | 446 |
| Images with Switches |  | 960 |
| Images with Multiple Tracks |  | 1793 |
| Images with Tracks and Switches |  | 937 |
