# LabEquipVis: An annotated image dataset of computer laboratory equipment for object detection and smart lab automation.

**Auteurs** : Alam BMS, Mia MP, Kibria G, Mahi JA, Noor MT, Momo IJ, Niloy NT.
**Année** : 2025
**DOI** : 10.1016/j.dib.2025.112206

## Résumé

This article introduces LabEquipVis, a comprehensive dataset of high-resolution, annotated images of general-purpose laboratory equipment designed to facilitate machine learning and computer vision research in laboratory automation. The dataset comprises RGB images of ten common laboratory items, including AC units, chairs, CPUs, digital boards, fire extinguishers, keyboards, lights, monitors, mice, and projectors. Images were captured from multiple laboratory facilities at East West University, Dhaka, Bangladesh, using an Oppo Reno8 Pro camera. To ensure diversity and robustness, footage was recorded from four distinct angles: front, top-down, 45-degree, and side views, under consistent lighting conditions. Additionally, the dataset includes augmented versions of the images employing transformations such as rotation, brightness adjustment, and cropping, which enhance model generalization for real-world scenarios. All images were standardized to a resolution of 640 × 640 pixels in JPEG

## Méthodologie

{'study_design': "Constitution d'un jeu de données d'images annotées pour la détection d'objets ; images capturées sous quatre angles distincts (frontal, plongée, 45 degrés, latéral) sous des conditions d'éclairage constantes, avec versions augmentées (rotation, ajustement de luminosité, recadrage)", 'intervention': None, 'control': None, 'primary_outcomes': ['Précision de détection/classification des équipements de laboratoire par un modèle entraîné sur le dataset (YOLOv11)'], 'secondary_outcomes': [], 'statistical_methods': ['Matrice de confusion'], 'duration': None, 'setting': "Six laboratoires informatiques de l'East West University, Dhaka, Bangladesh"}

## Résultats

{'quantitative': [{'outcome': 'Précision du modèle YOLOv11 entraîné sur le dataset LabEquipVis', 'value': '84.94', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Validating the credibility of the dataset', 'source_quote': "However, the model's accuracy with this dataset is 84.94 % with only slight modification."}], 'qualitative_findings': [], 'main_findings': ["Le dataset LabEquipVis contient 2584 images RGB brutes couvrant dix catégories d'équipements de laboratoire informatique", 'Les images ont été annotées manuellement via Roboflow avec des boîtes englobantes', 'Le dataset inclut des versions originales et augmentées organisées en sous-dossiers Test, Train et Validation', "L'entraînement du modèle YOLOv11 sur ce dataset a atteint une précision de 84.94%, validant la fiabilité du dataset"]}

## Conclusions

Le dataset LabEquipVis constitue une ressource nouvelle et utile pour faire progresser la recherche en détection d'objets, robotique et systèmes de laboratoire intelligents Le dataset comble une lacune critique laissée par les jeux de données existants centrés sur les instruments de laboratoires de chimie plutôt que sur les laboratoires informatiques Le dataset supporte l'intégration avec des frameworks de détection d'objets tels que YOLOv4, YOLOv5, YOLOv8, YOLOv9, YOLOv11 et EfficientDet

## Distribution of annotated object instances across 10 classes in the dataset.

| CLASS NAME |
| --- |

## Specifications of the smartphone camera.

| Camera Feature |
| --- |

## Model summary.

| Class | Images | Instances | Box (P | R | mAP50 | mAP50-95) |
| --- | --- | --- | --- | --- | --- | --- |
| all | 516 | 9317 | 0.888 | 0.829 | 0.882 | 0.699 |
| Ac | 29 | 48 | 0.952 | 0.938 | 0.936 | 0.857 |
| Chair | 387 | 1889 | 0.825 | 0.805 | 0.848 | 0.649 |
| CPU | 295 | 786 | 0.757 | 0.687 | 0.756 | 0.539 |
| Digital board | 67 | 68 | 0.835 | 0.853 | 0.879 | 0.737 |
| Fire Extinguisher | 78 | 145 | 0.917 | 0.762 | 0.869 | 0.609 |
| Keyboard | 261 | 729 | 0.834 | 0.861 | 0.889 | 0.76 |
| Light | 87 | 248 | 0.923 | 0.839 | 0.916 | 0.684 |
| Monitor | 432 | 3749 | 0.945 | 0.947 | 0.963 | 0.799 |
| Mouse | 358 | 1600 | 0.93 | 0.636 | 0.786 | 0.592 |
| Projector | 55 | 55 | 0.964 | 0.968 | 0.982 | 0.765 |
