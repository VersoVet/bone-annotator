# OHIF-SAM2: Accelerating Radiology Workflows with Segment Anything Model 2

**Auteurs** : Jaeyoung Cho, Aditya Rastogi, Jingyu Liu, Philipp Vollmuth, Kai Schlamp, Philipp Vollmuth
**Année** : 2024
**DOI** : 10.36227/techrxiv.173387978.85520380/v1

## Résumé

The release of Segment Anything Models (SAM1 and SAM2) by Meta has significantly influenced various domains, including medical imaging. However, existing implementations of SAM primarily focus on standalone tools that require local installation and configuration, limiting accessibility and ease of use. In this work, we present the web-based extension of SAM2 integrated into the Open Health Imaging Foundation (OHIF) viewer. Our solution supports all SAM2 prompt types, including points and bounding boxes, and enables multi-label predictions. This web-based integration eliminates installation requirements, offering a more user-friendly interface. The implementation is open-source and available at https://github.com/CCI-Bonn/OHIF-SAM2.

## Méthodologie

{'study_design': 'Étude expérimentale comparative : fine-tuning de plusieurs CNN pré-entraînés (VGG19, ResNet152v2, MobileNetv2, NASNetMobile, NASNetLarge, Inception-ResNet) sur un dataset combiné de fruits/légumes, conversion en TensorFlow Lite, puis déploiement et profilage sur deux appareils mobiles réels comparés à un nouveau modèle proposé, FruitVegCNN (10 couches : 6 convolutionnelles + 4 fully connected)', 'intervention': "Entraînement et déploiement du modèle proposé FruitVegCNN sur les appareils mobiles, avec augmentation de données (rotation, décalage largeur/hauteur, zoom, flip horizontal, salt & pepper, coarse dropout) et couches de dropout (p=0.3 et p=0.5) pour réduire l'overfitting", 'control': 'Modèles CNN pré-entraînés state-of-the-art existants : VGG19, ResNet152v2, MobileNetv2, NASNetMobile, NASNetLarge, Inception-ResNet', 'primary_outcomes': ['Précision de validation (validation accuracy)', 'Précision de test (testing accuracy)', "Consommation d'énergie (Power, mW)", 'Consommation mémoire RAM (GB)', 'Temps de chargement du modèle (Ld. time, sec)'], 'secondary_outcomes': ['Charge CPU (%)', 'Charge GPU (%)', 'Température de la batterie (°C)'], 'statistical_methods': [], 'duration': "Profilage effectué pendant 60 secondes d'exécution de l'application Flutter sur chaque appareil", 'setting': 'Entraînement sur ordinateur avec 4 CPU Intel Xeon Gold 6134 et GPU Nvidia Tesla P100 (12GB) sous TensorFlow ; évaluation sur appareils mobiles réels Huawei P20 Lite (Kirin 659 MPSoC, Android 8.0.0.168 Oreo) et Samsung Galaxy Note 9 (Exynos 9810 MPSoC, Android 9 Pie)'}

## Résultats

{'quantitative': [{'outcome': 'Nombre de paramètres de FruitVegCNN', 'value': '53391', 'unit': 'paramètres', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results (V.B Reducing overfitting)', 'source_quote': 'Our neural network architecture has 53,391 parameters and it makes it insufficient to learn so many parameters without overfitting.'}, {'outcome': 'Performance FruitVegCNN sur Huawei P20 Lite (Ld. time, RAM, CPU%, GPU%, Power, Bat. Temp.)', 'value': '9 sec / 0.34 GB / 58% / 14% / 1560 mW / 33°C', 'unit': 'mixte', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The Ld. time (sec), RAM (GB), CPU%, GPU%, Power (mW) & Bat. Temp. (°C) for FruitVegCNN in Huawei P20 Lite are 9, 0.34, 58, 14, 1560 and 33 respectively.'}, {'outcome': 'Performance FruitVegCNN sur Samsung Galaxy Note 9 (Ld. time, RAM, CPU%, GPU%, Power, Bat. Temp.)', 'value': '1 sec / 0.5 GB / 45% / 0% / 3092 mW / 32°C', 'unit': 'mixte', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'In Samsung Galaxy Note 9, the Ld. time (sec), RAM (GB), CPU%, GPU%, Power (mW) & Bat. Temp. (°C) for FruitVegCNN are 1, 0.5, 45, 0, 3092 and 32 respectively.'}, {'outcome': "Réduction de consommation d'énergie de FruitVegCNN vs VGG sur Huawei P20 Lite", 'value': '54.88', 'unit': '% de réduction', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results / Conclusion', 'source_quote': 'Compared to VGG, FruitVegCNN consumes 54.88% less power, 56.41% less RAM memory and loads 47.06% faster in Huawei P20 Lite.'}, {'outcome': 'Réduction de RAM de FruitVegCNN vs VGG sur Huawei P20 Lite', 'value': '56.41', 'unit': '% de réduction', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results / Conclusion', 'source_quote': 'Compared to VGG, FruitVegCNN consumes 54.88% less power, 56.41% less RAM memory and loads 47.06% faster in Huawei P20 Lite.'}, {'outcome': 'Amélioration du temps de chargement de FruitVegCNN vs VGG sur Huawei P20 Lite', 'value': '47.06', 'unit': '% plus rapide', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results / Conclusion', 'source_quote': 'Compared to VGG, FruitVegCNN consumes 54.88% less power, 56.41% less RAM memory and loads 47.06% faster in Huawei P20 Lite.'}, {'outcome': "Réduction de consommation d'énergie de FruitVegCNN vs VGG sur Samsung Galaxy Note 9", 'value': '61.12', 'unit': '% de réduction', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results / Conclusion', 'source_quote': 'Whereas, in Samsung Galaxy Note 9, compared to VGG, FruitVegCNN consumes 61.12% less power, 44.44% less RAM memory and loads 66.67% faster.'}, {'outcome': 'Réduction de RAM de FruitVegCNN vs VGG sur Samsung Galaxy Note 9', 'value': '44.44', 'unit': '% de réduction', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results / Conclusion', 'source_quote': 'Whereas, in Samsung Galaxy Note 9, compared to VGG, FruitVegCNN consumes 61.12% less power, 44.44% less RAM memory and loads 66.67% faster.'}, {'outcome': 'Amélioration du temps de chargement de FruitVegCNN vs VGG sur Samsung Galaxy Note 9', 'value': '66.67', 'unit': '% plus rapide', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results / Conclusion', 'source_quote': 'Whereas, in Samsung Galaxy Note 9, compared to VGG, FruitVegCNN consumes 61.12% less power, 44.44% less RAM memory and loads 66.67% faster.'}, {'outcome': "Nombre total d'images du dataset combiné", 'value': '90483', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods (IV.A Dataset)', 'source_quote': 'The dataset consists of a total of 90483 images (67692 images for training and 22688 images for validation) for 131 different types (class labels) of fruits and vegetables.'}, {'outcome': "Nombre d'images de test", 'value': '660', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods (IV.A Dataset)', 'source_quote': 'Therefore, the total number of testing images were 660.'}], 'qualitative_findings': ['VGG19 a obtenu la meilleure précision de validation pour la classification des fruits et légumes', 'Les deux architectures NASNet (NASNetMobile et NASNetLarge) ont obtenu les moins bonnes performances de validation', 'FruitVegCNN a performé de manière très proche des autres CNN populaires en termes de précision de test tout en consommant beaucoup moins de ressources'], 'main_findings': ['FruitVegCNN est le modèle le plus efficace en énergie tout en consommant le moins de mémoire (disque et RAM) parmi les CNN comparés', "FruitVegCNN atteint une précision de test comparable aux modèles CNN état de l'art, avec beaucoup moins de paramètres entraînables (53 391)", 'FruitVegCNN offre le meilleur compromis performance/efficacité énergétique/mémoire pour un déploiement sur MPSoC mobile']}

## Conclusions

FruitVegCNN permet une classification des fruits et légumes performante et efficace en énergie sur des appareils mobiles réels (Huawei P20 Lite et Samsung Galaxy Note 9) Comparé à VGG, FruitVegCNN consomme 54.88% moins d'énergie, 56.41% moins de RAM et se charge 47.06% plus vite sur Huawei P20 Lite Comparé à VGG, FruitVegCNN consomme 61.12% moins d'énergie, 44.44% moins de RAM et se charge 66.67% plus vite sur Samsung Galaxy Note 9 Il s'agit, selon les auteurs, du premier travail de conception et d'implémentation d'un modèle CNN pour la classification de fruits et légumes sur une plateforme mobile

## Comparison between CNN models based on disk size and parameters

| CNN Model | Size | Parameters |
| --- | --- | --- |
| ResNet152v2 | 232 MB | 60,380,648 |
| NASNetMobile | 23 MB | 5,326,716 |
| NASNetLarge | 343 MB | 88,949,818 |
| VGG19 | 549 MB | 143,667,240 |
| MobileNetv2 | 14 MB | 3,538,984 |
| Inception-ResNet | 215 MB | 55,873,736 |

## Comparison between trained CNN models on validation accuracy (%)

| CNN Model | Validation Accuracy (%) |
| --- | --- |
| ResNet152v2 | 95.027 |
| NASNetMobile | 10.108 |
| NASNetLarge | 10.054 |
| VGG19 | 98.918 |
| MobileNetv2 | 97.892 |
| Inception-ResNet | 98.432 |

## Comparison between trained CNN models in Tensorflow Lite format based on disk size

| CNN Model | Size |
| --- | --- |
| ResNet152v2 | 335.5 MB |
| NASNetMobile | 20.9 MB |
| NASNetLarge | 352.5 MB |
| VGG19 | 182.9 MB |
| MobileNetv2 | 23.3 MB |
| Inception-ResNet | 340.8 MB |
| (NASNetMobile and NASNetLarge) and Inception-ResNet |
| models got reduced. Table III shows the reduced disk size |
| of the trained CNNs in Tensorflow Lite format for mobile |
| implementation. |  |

## Comparison between trained CNN models in Tensorflow Lite format based on Ld. time, RAM, CPU%, GPU%, Power and Bat. Temp. in Huawei P20 Lite

| CNN Model | Ld. time (sec) | RAM (GB) | CPU% | GPU% | Power (mW) | Bat. Temp. (°C) |
| --- | --- | --- | --- | --- | --- | --- |
| ResNet152v2 | 16 | 0.65 | 64 | 21 | 2150 | 37 |
| NASNetMobile | 13 | 0.53 | 61 | 15 | 3302 | 37 |
| NASNetLarge | 14 | 0.69 | 68 | 11 | 3475 | 33 |
| VGG19 | 17 | 0.78 | 72 | 22 | 3458 | 30 |
| MobileNetv2 | 11 | 0.54 | 59 | 13 | 2746 | 36 |
| Inception-ResNet | 12 | 0.62 | 59 | 22 | 2880 | 38 |

## Comparison between trained CNN models in Tensorflow Lite format based on Ld. time, RAM, CPU%, GPU%, Power and Bat. Temp. in Samsung Galaxy Note 9

| CNN Model | Ld. time (sec) | RAM (GB) | CPU% | GPU% | Power (mW) | Bat. Temp. (°C) |
| --- | --- | --- | --- | --- | --- | --- |
| ResNet152v2 | 4 | 0.72 | 56 | 1 | 4052 | 35 |
| NASNetMobile | 6 | 0.83 | 56 | 0 | 3953 | 34 |
| NASNetLarge | 19 | 1.39 | 54 | 1 | 4026 | 36 |
| VGG19 | 3 | 0.9 | 62 | 1 | 7952 | 35 |
| MobileNetv2 | 2 | 0.73 | 53 | 0 | 4019 | 35 |
| Inception-ResNet | 5 | 0.74 | 55 | 1 | 4042 | 35 |

## Comparison between trained CNN models on testing accuracy (%)

| CNN Model | Testing Accuracy (%) |
| --- | --- |
| ResNet152v2 | 68.18 |
| NASNetMobile | 2.5 |
| NASNetLarge | 1.515 |
| VGG19 | 72.72 |
| MobileNetv2 | 70 |
| Inception-ResNet | 70.45 |
| FruitVegCNN | 71.36 |
