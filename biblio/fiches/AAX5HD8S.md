# An annotated image dataset for small apple fruitlet detection in complex orchard environments.

**Auteurs** : Wang D, Wang B.
**Année** : 2025
**DOI** : 10.3389/fpls.2025.1664972

## Résumé

This study introduces a small apple pre-thinning dataset designed to support the development of intelligent thinning systems by providing reliable data for small apple detection. The dataset comprises 2,517 RGB images (original size 3024×3024 pixels, uniformly resized to 500×500 pixels for standardization) systematically captured under real-world orchard conditions. The dataset encompasses natural variations in weather conditions (sunny/cloudy), lighting scenarios (direct sunlight/backlight), and fruit sizes (3-25mm diameter range) to ensure broad applicability. Each image was meticulously annotated using LabelImg software, with all small apple targets precisely labeled using both PASCAL VOC (XML) and YOLO (TXT) format bounding boxes, facilitating compatibility with various detection frameworks. Validation experiments conducted across multiple detection architectures (including Faster R-CNN, Cascade R-CNN, YOLO series, RT-DETR, DEIMv2, etc.) demonstrate the dataset's effectiveness. Thi

## Méthodologie

{'study_design': "Construction et validation d'un jeu de données annoté (dataset paper), comprenant trois étapes: collecte de données, annotation de données, et validation du jeu de données via des expériences de benchmarking", 'intervention': "Annotation manuelle des images avec LabelImg (formats PASCAL VOC XML et YOLO TXT), suivie d'un contrôle qualité en trois phases (auto-validation itérative, vérification automatique de cohérence, adjudication finale par un expert)", 'control': None, 'primary_outcomes': ['Performance de détection des petites pommes (Average Precision, Average Recall) selon les métriques COCO'], 'secondary_outcomes': ["Précision par échelle d'objet (AP_S, AP_M, AP_L)", "Taux de correction d'erreurs lors du contrôle qualité"], 'statistical_methods': ['Métriques standard COCO: Average Precision (AP), AP@0.5, Average Recall (AR)', "Analyse statistique descriptive de la composition du dataset (distribution environnementale, temporelle, d'échelle des objets)"], 'duration': "Collecte d'images sur trois sessions en mai 2018 (1, 2 et 4 mai)", 'setting': 'Verger expérimental du College of Horticulture, Northwest A&F University, Yangling, Shaanxi, Chine'}

## Résultats

{'quantitative': [{'outcome': "Nombre total d'images du dataset", 'value': '2517', 'unit': 'images RGB', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The dataset comprises a total of 2,517 RGB images.'}, {'outcome': 'Nombre total de fruitlets annotés', 'value': '22415', 'unit': 'petites pommes annotées', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'A cumulative of 22,415 small apple fruitlets with different conditions were meticulously annotated.'}, {'outcome': 'Proportion de boîtes englobantes de petite taille (petits objets selon critère COCO)', 'value': '>60%', 'unit': 'pourcentage des bounding boxes', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'Notably, over 60% of the bounding boxes have an area smaller than 32 2 pixels, formally categorizing them as small objects according to the COCO benchmark criteria.'}, {'outcome': 'Performance globale de détection (AP) - RT-DETR-L', 'value': '0.669', 'unit': 'Average Precision', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The Transformer-based RT-DETR-L model leads in overall accuracy (AP = 0.669), demonstrating the most robust overall detection capabilities.'}, {'outcome': 'Rappel (Average Recall) - DEIMv2-N', 'value': '0.706', 'unit': 'Average Recall', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'DEIMv2-N excels in recall (AR = 0.706) and loose-threshold precision (AP@0.5 = 0.921)'}, {'outcome': 'Précision à seuil large (AP@0.5) - DEIMv2-N', 'value': '0.921', 'unit': 'AP@0.5', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'DEIMv2-N excels in recall (AR = 0.706) and loose-threshold precision (AP@0.5 = 0.921), offering particular value for applications like fruit thinning where a high recall rate is critical.'}, {'outcome': "Taux de correction d'erreurs lors de l'adjudication finale par expert", 'value': '<2%', 'unit': 'pourcentage', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'The error correction rate during this phase was found to be below 2%, indicating the high initial quality achieved by the previous phases.'}, {'outcome': 'Répartition train/validation/test', 'value': '2013/253/251', 'unit': 'images (ratio 8:1:1)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'The dataset was randomly partitioned into training (2,013 images), validation (253 images), and test (251 images) sets at an 8:1:1 ratio for model training.'}], 'qualitative_findings': ["L'écart de précision entre les petites cibles (AP_S) et les cibles moyennes/grandes est substantiel pour tous les modèles testés, confirmant la difficulté intrinsèque de détection des petites pommes", 'Les modèles modernes de la série YOLO (v8, v11, v12) offrent une alternative équilibrée et performante'], 'main_findings': ['Un jeu de données de 2517 images annotées avec 22415 fruitlets a été construit et validé', 'RT-DETR-L obtient la meilleure précision globale (AP = 0.669) parmi les dix architectures testées', "DEIMv2-N offre le meilleur rappel et la meilleure précision à seuil large, pertinent pour les applications d'éclaircissage nécessitant un haut rappel", 'La détection des petites cibles reste nettement plus difficile que celle des cibles moyennes/grandes, validant la pertinence du dataset pour ce défi']}

## Conclusions

Le dataset introduit comble une lacune de données pour la détection de petites pommes avant éclaircissage, un domaine jusqu'ici peu exploré Les évaluations menées sur dix architectures de détection d'objets valident l'efficacité et l'utilité du dataset proposé Le dataset constitue une ressource précieuse pour le développement de systèmes d'éclaircissage intelligents, avec des applications potentielles pour l'automatisation de l'industrie pomicole, l'amélioration de l'efficacité de l'éclaircissage et de la qualité des fruits

## Comparison of key characteristics between mature fruit detection and pre-thinning small apple detection.

| Characteristic | Mature fruit detection | Pre-thinning small apple detection |
| --- | --- | --- |
| Primary application | Automated harvesting/Yield estimation | Automated thinning |
| Target size | Large (Relative to image) | Small (Area often < 32 2 pixels) |
| Color contrast | High (Red to Green) | Low (Green-on-Green) |
| Representative datasets | MinneApple (Häni et al., 2020) Deep Fruits dataset (Bargoti and Underwood, 2017) | Small apple dataset (This work) |

## Description of camera device.

| Manufacture |
| --- |

## Description of data collection.

| Fruit |
| --- |

## Statistical characterization of the dataset.

| Conditions | Sub-category Number of images | Percentage | Number of targets | Percentage |
| --- | --- | --- | --- | --- | --- |
|  | Sunny | 1,670 | 66.3% | 13,089 | 58.4% |
| Weather |  |  |  |  |  |
|  | Cloudy | 847 | 33.7% | 9,326 | 41.6% |
|  | Direct sunlight | 1,181 | 46.9% | 10,656 | 47.5% |
| Lighting |  |  |  |  |  |
|  | Backlight | 1,336 | 53.1% | 11,759 | 52.5% |
|  | 09:00-11:30 | 996 | 39.6% | 9,983 | 44.5% |
| Acquisition time |  |  |  |  |  |
|  | 14:30-18:30 | 1,521 | 60.4% | 12,432 | 55.5% |
|  | Area < 32² pixels | 2,108 | 83.8% | 14,080 | 62.8% |
| Target size distribution (Area of annotated bounding box) | 32² pixels ≤ Area < 96² pixels | 2,069 | 82.2% | 8,230 | 36.7% |
|  | Area ≥ 96² pixels | 68 | 0.3% | 105 | 0.5% |

### Formule


$$FIGURE 2$$
