# MONAI Label: A framework for AI-assisted Interactive Labeling of 3D Medical Images

**Auteurs** : Andres Diaz‐Pinto, Sachidanand Alle, Vishwesh Nath, Yucheng Tang, Alvin Ihsani, Muhammad Asad, Fernando Pérez‐García, Pritesh Mehta, Wenqi Li, Mona G. Flores
**Année** : 2022
**DOI** : 10.48550/arxiv.2203.12362

## Résumé

The lack of annotated datasets is a major bottleneck for training new task-specific supervised machine learning models, considering that manual annotation is extremely expensive and time-consuming. To address this problem, we present MONAI Label, a free and open-source framework that facilitates the development of applications based on artificial intelligence (AI) models that aim at reducing the time required to annotate radiology datasets. Through MONAI Label, researchers can develop AI annotation applications focusing on their domain of expertise. It allows researchers to readily deploy their apps as services, which can be made available to clinicians via their preferred user interface. Currently, MONAI Label readily supports locally installed (3D Slicer) and web-based (OHIF) frontends and offers two active learning strategies to facilitate and speed up the training of segmentation algorithms. MONAI Label allows researchers to make incremental improvements to their AI-based annotation application by making them available to other researchers and clinicians alike. Additionally, MONAI Label provides sample AI-based interactive and non-interactive labeling applications, that can be used directly off the shelf, as plug-and-play to any given dataset. Significant reduced annotation times using the interactive model can be observed on two public datasets.

## Méthodologie

{'study_design': "Présentation d'un framework logiciel (MONAI Label) et évaluation expérimentale de ses approches d'annotation (DeepGrow, DeepEdit, scribbles-based) sur deux jeux de données publics, comparées à des techniques d'annotation traditionnelles (paintbrush, contour)", 'intervention': "Utilisation des modèles d'annotation interactive DeepGrow et DeepEdit, et de la méthode basée sur les scribbles avec optimisation par énergie, au sein du framework MONAI Label", 'control': "Techniques d'annotation manuelle traditionnelles (paintbrush et contourage avancé) et outils basiques de 3D Slicer (Grow from Seeds, Brush)", 'primary_outcomes': ['Temps nécessaire pour annoter un volume 3D', "Nombre d'interactions utilisateur requises"], 'secondary_outcomes': ["Réduction du temps d'annotation grâce à l'apprentissage actif", 'Performance du modèle en fonction du nombre de volumes annotés par étape'], 'statistical_methods': [], 'duration': None, 'setting': 'Expériences réalisées sur deux jeux de données publics : le jeu de données de segmentation de la rate du Medical Segmentation Decathlon (MSD) et le jeu de données cardiaque (CMR) du MSD'}

## Résultats

{'quantitative': [{'outcome': "Temps d'annotation d'un volume 3D avec le pipeline combiné DeepGrow 2D & 3D au stade 4", 'value': '1-2.5', 'unit': 'minutes', 'confidence_interval': None, 'p_value': None, 'effect_size': '10x plus rapide que la technique traditionnelle avancée de contourage', 'source_section': 'Results', 'source_quote': 'At 4 th stage it can be observed that by utilizing the combined pipeline of Deepgrow 2D & 3D the user can annotate 3D volumes in approximately 1 -2.5 minutes which is 10x faster even compared to the advanced traditional technique of contouring manually annotate the 3D volume'}, {'outcome': "Temps moyen d'annotation avec la méthode scribbles-based", 'value': '2', 'unit': 'minutes', 'confidence_interval': None, 'p_value': None, 'effect_size': '12.5x plus rapide que le paintbrush, 6.25x plus rapide que le contourage', 'source_section': 'Results', 'source_quote': 'on average 2 minutes were required to annotate a sample using the scribbles-based method which is 12.5× and 6.25× faster than using the paintbrush and contour-based method, respectively'}, {'outcome': "Temps d'annotation manuelle de l'oreillette gauche (CMR) avec les outils de base de 3D Slicer", 'value': '10', 'unit': 'minutes', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'we measured the time an expert annotator took to manually annotate the left atrium (10 minutes) using the manual/basic available tools in 3D Slicer'}, {'outcome': "Réduction du temps d'annotation des cerveaux malades pour la planification chirurgicale (Neurosurgical Atlas)", 'value': '50-80', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Neurosurgical Atlas', 'source_quote': 'Using the active learning strategies and the noninteractive model available in MONAI Label, neurosurgeons could reduce the time from 50% to 80% annotating diseased brains for surgical planning purposes.'}, {'outcome': 'Nombre de lésions cérébrales segmentées dans le projet Neurosurgical Atlas', 'value': '220', 'unit': 'lésions', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Neurosurgical Atlas', 'source_quote': 'A total of 220 lesions were segmented, and divided into meningiomas, lowgrade gliomas, high-grade gliomas, and brain metastases'}, {'outcome': 'Nombre de volumes CT dans le jeu de données de segmentation de la rate (MSD)', 'value': '41', 'unit': 'volumes 3D CT', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Experiments and Results - DeepGrow Performance', 'source_quote': 'The dataset consists of a total of 41 3D CT volumes.'}, {'outcome': "Nombre d'images CMR dans le jeu de données cardiaque du MSD", 'value': '20', 'unit': 'images CMR', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Experiments and Results', 'source_quote': 'This dataset is composed of 20 CMR images.'}], 'qualitative_findings': ["Le modèle entraîné sur une ou deux images peut ne pas bien performer au début, mais il aide le clinicien à créer rapidement une étiquette qu'il peut modifier via la partie interactive de DeepEdit, réduisant significativement le temps passé sur les autres images", "L'annotation par scribbles offre une interaction naturelle déjà familière à la plupart des annotateurs et introduit de la flexibilité dans la charge de travail"], 'main_findings': ["Le temps nécessaire pour annoter un volume 3D diminue à mesure que davantage de données d'entraînement sont ajoutées à chaque étape", "L'approche interactive combinée DeepGrow 2D & 3D permet une annotation jusqu'à 10x plus rapide que le contourage manuel avancé", "La méthode scribbles-based réduit significativement le temps d'annotation par rapport aux techniques traditionnelles de paintbrush et de contourage", "L'utilisation de DeepEdit avec l'apprentissage actif permet de commencer l'entraînement du modèle après seulement une ou deux images annotées, réduisant le temps total nécessaire avant de disposer d'un modèle utile", "MONAI Label a été utilisé avec succès dans un cas d'usage réel (Neurosurgical Atlas) pour réduire de 50 à 80% le temps d'annotation des cerveaux malades"]}

## Conclusions

MONAI Label est un framework gratuit et open-source qui permet aux utilisateurs de créer des jeux de données annotés et de construire des modèles d'annotation basés sur l'IA pour évaluation clinique MONAI Label réduit le temps et l'effort d'annotation de nouveaux jeux de données et permet l'adaptation continue de l'IA à la tâche via l'apprentissage à partir des interactions utilisateur, via deux interfaces (3D Slicer et OHIF) MONAI Label propose deux approches d'annotation : une approche interactive (DeepGrow, DeepEdit, Scribbles-based) et une approche non-interactive Le framework a été étendu avec une interface de gestion de données XNAT et une application de pathologie (Pathology App) pour la segmentation d'images de pathologie (WSI) MONAI Label offre un planificateur heuristique qui prend en compte le GPU disponible ainsi que les informations d'intensité et spatiales du jeu d'entraînement pour définir les transformations de données et les hyperparamètres

## Modules Overview: MONAI Label provides interfaces that can be implemented by the label app developer for custom functionality as well as utilities that are readily usable in the labeling app. Time spent on annotating the Spleen MSD dataset: This table presents the times spent on each stage annotating volumes from the Spleen dataset using several manual tools (paintbrush, contor-based and scribbles-based methods) and the interactive DeepGrow model available on MONAI Label.

|  |  |  |  |  | MONAI Label Interfaces |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | Tasks |
|  | MONAILabelApp | InferTask | BatchInferTask | TrainTask | Strategy | Scoring Method |
|  |  | InferDeepGrow2D | InferDeepGrow3D | BasicTrain Task | TTA | TTAScoring |
|  |  |  |  |  | MONAI Label Utilities |
| MyApp |  |  |  |  |
| - | infers: | MyInfer | InferDeepGrow2D |  |
| -train: | TrainDeepGrow |  |  |
| - | strategy: | TTA | MyStrategy |  |
| - | scoring_method: | TTAScoring | MyScoringMethod |
| Figure 6: Annotated |  | Paint Brush | Contour-Based | Scribbles-Based | DeepGrow |
|  | Volumes |  | Method | Method | Method | Method |
| Stage 1 |  | 11 |  |  | 275 mins | 137.5 mins | 22 mins | 25 mins |
| Stage 2 | 11 + (5) = 16 |  | 400 mins | 200 mins | 32 mins | 6 -7.5 mins |
| Stage 3 | 11 + 5 + (10) = 26 |  | 650 mins | 325 mins | 52 mins | 3.5 -5 mins |
| Stage 4 11 + 5 + 10 + (10) = 36 | 900 mins | 450 mins | 72 mins | 1 -2.5 mins |

## Obtained results from the interactive DeepGrow model: Total annotation time per stage, training time on each stage, and the validation Dice Scores on the Spleen MSD dataset. The validation set is composed of nine 3D volumes (20%) that were randomly selected from the Spleen MSD dataset.

|  | Total Annotation Time | Training Time | Validation Dice | Validation Dice |
| --- | --- | --- | --- | --- |
|  | Using DeepGrow | DeepGrow 2D & 3D | DeepGrow 2D | DeepGrow 3D |
| Stage 1 | 275 mins | 90 mins | 0.891 | 0.730 |
| Stage 2 | 30 mins | 135 mins | 0.924 | 0.873 |
| Stage 3 | 45 mins | 250 mins | 0.948 | 0.945 |
| Stage 4 | 15 mins | 360 mins | 0.967 | 0.959 |
| 5.2. DeepEdit Performance |  |  |  |
