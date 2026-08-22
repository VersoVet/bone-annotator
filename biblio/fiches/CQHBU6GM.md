# Poribohon-BD: Bangladeshi local vehicle image dataset with annotation for classification.

**Auteurs** : Shaira Tabassum, Sabbir Ullah, Nakib Hossain Al-Nur, Swakkhar Shatabda
**Année** : 2020
**DOI** : 10.1016/j.dib.2020.106465

## Résumé

Vehicle Classification has become tremendously important due to various applications such as traffic video surveillance, accident avoidance, traffic congestion prevention, bringing intelligent transportation systems. This article presents 'Poribohon-BD' dataset for vehicle classification purposes in Bangladesh. The vehicle images are collected from two sources: i) smartphone camera, ii) social media. The dataset contains 9058 labeled and annotated images of 15 native Bangladeshi vehicles such as bus, motorbike, three-wheeler rickshaw, truck, wheelbarrow. Data augmentation techniques have been applied to keep the number of images comparable to each type of vehicle. For labeling the images, LabelImg tool by Tzuta Lin has been used. Human faces have also been blurred to maintain privacy and confidentiality. The dataset is compatible with various CNN architectures such as YOLO, VGG-16, R-CNN, DPM. It is available for research purposes at https://data.mendeley.com/datasets/pwyyg8zmk5/2.

## Méthodologie

{'study_design': 'Création de dataset en quatre étapes : collecte de données, prétraitement des données, augmentation des données et annotation des données', 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': 'Bangladesh (routes, autoroutes, plages, différentes localisations)'}

## Résultats

{'quantitative': [{'outcome': "Nombre total d'images labellisées et annotées", 'value': '9058', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The dataset contains 9058 labeled and annotated images of 15 native Bangladeshi vehicles such as bus, motorbike, three-wheeler rickshaw, truck, wheelbarrow.'}, {'outcome': "Nombre d'images collectées via les réseaux sociaux", 'value': 'environ 4000', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Experimental Design, Materials and Methods - Data collection', 'source_quote': 'Around 40 0 0 images are collected from social media (facebook).'}, {'outcome': 'Nombre de nouvelles images générées par augmentation de données', 'value': '1791', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Experimental Design, Materials and Methods - Data augmentation', 'source_quote': 'In Poribohon-BD dataset, few data augmentation techniques such as flipping, cropping, color space transformation have been applied to generate 1791 new images.'}, {'outcome': 'Nombre de classes de véhicules', 'value': '15', 'unit': 'types de véhicules', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Data Description', 'source_quote': 'Poribohon-BD is an image dataset of 15 native vehicles of Bangladesh.'}, {'outcome': 'Nombre de dossiers de données', 'value': '16', 'unit': 'dossiers', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Data Description', 'source_quote': 'The data files are divided into 16 folders.'}], 'qualitative_findings': ['Les visages humains ont été flous dans les images pour préserver la confidentialité', 'Différentes vues, arrière-plans, conditions météorologiques et scénarios ont été considérés pour augmenter la variance des données'], 'main_findings': ['Le dataset Poribohon-BD contient 9058 images labellisées et annotées de 15 véhicules natifs du Bangladesh', 'Le dataset est compatible avec diverses architectures CNN telles que YOLO, VGG-16, R-CNN, DPM', 'Le dataset est disponible pour la recherche']}

## Conclusions

Poribohon-BD fournit une ressource pour entraîner des modèles d'apprentissage profond destinés à la détection, classification et segmentation de véhicules spécifiques au contexte bangladais Le dataset peut bénéficier au développement d'applications de gestion du trafic et de systèmes de transport intelligents au Bangladesh Le dataset peut être étendu en augmentant le nombre d'images par classe et en ajoutant d'autres types de véhicules

## comparison among different public vehicle datasets.

| Specifications | KITTY | Waymo | Cityscapes | ApolloScape Poribohon-BD |
| --- | --- | --- | --- | --- | --- |
| Number of | 7481 | Around | 250 0 0 | 701 | 9058 |
| images |  | 12 |  |  |  |
|  |  | million |  |  |  |
| Annotation | 3D | LiDAR | Fine |  | 2D bounding boxes |
|  | bound- | box | annota- | Semantic |  |
|  | ing | annota- | tions, | annota- |  |
|  | boxes | tions, | coarse | tion |  |
|  |  | camera | annota- |  |  |
|  |  | box | tions |  |  |
|  |  | annota- |  |  |  |
|  |  | tions |  |  |  |
| Number of | 8 | 4 | 30 | 32 | 15 |
| classes |  |  |  |  |  |
| Number of | 5 | 2 | 6 | 6 | 15 |
| vehicle classes |  |  |  |  |  |
| Vehicle related | Car, |  | Car, | Car, | Bicycle, boat, bus, car, CNG, |
| classes | van, | Vehicles, | truck, | motor- | easy-bike, horse-cart, launch, |
|  | truck, | cyclist | bus, | cycle, | leguna, motorbike, rickshaw, |
|  | cyclist, |  | motor- | bicycle, | tractor, truck, van, wheelbarrow |
|  | tram |  | cycle, | truck, |  |
|  |  |  | bicycle, | bus, |  |
|  |  |  | caravan | tricycle |  |
| Unique vehicle | Tram | - | Caravan | Tricycle | Boat, CNG, easy-bike, horse-cart, |
| classes |  |  |  |  | launch, leguna, rickshaw, tractor, |
|  |  |  |  |  | wheelbarrow |

## Data description of 'Poribohon-BD' dataset.

| Classes | Smartphone Cameras Internet Data Augmentation # Image Files # Annotation Files Total Appearance |
| --- | --- | --- | --- | --- | --- | --- |
| Bicycle | 247 | 460 | - | 707 | 707 | 1617 |
| Boat | 33 | 580 | - | 613 | 613 | 1974 |
| Bus | 112 | 340 | - | 452 | 452 | 3711 |
| Car | 148 | 560 | - | 708 | 708 | 1698 |
| CNG | 202 | 70 | - | 533 | 533 | 3214 |
| Easy-bike | 240 | 70 | 261 | 616 | 616 | 2062 |
| Horse-cart | 38 | 90 | 306 | 256 | 256 | 1581 |
| Launch | - | 662 | 128 | 662 | 662 | 332 |
| Leguna | 101 | 10 | - | 218 | 218 | 1686 |
| Motorbike | 124 | 740 | 107 | 864 | 864 | 746 |
| Rickshaw | 435 | 60 | - | 495 | 495 | 3386 |
| Tractor | 2 | 215 | 216 | 433 | 433 | 509 |
| Truck | 294 | 80 | 362 | 736 | 736 | 1673 |
| Van | 307 | 10 | 298 | 615 | 615 | 2057 |
| Wheelbarrow 124 | - | 113 | 237 | 237 | 605 |
| Multi Class | 863 | 50 | - | 913 | 913 | - |
| TOTAL: | 3270 | 3997 | 1791 | 9058 | 9058 | 26851 |
