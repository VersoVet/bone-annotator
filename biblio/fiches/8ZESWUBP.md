# TrackMe:A Simple and Effective Multiple Object Tracking Annotation Tool

**Auteurs** : Thinh Phan, Isaac Phillips, Andrew Lockett, Michael T. Kidd, Ngan Le
**Année** : 2024

## Résumé

Object tracking, especially animal tracking, is one of the key topics that attract a lot of attention due to its benefits of animal behavior understanding and monitoring. Recent state-of-the-art tracking methods are founded on deep learning architectures for object detection, appearance feature extraction and track association. Despite the good tracking performance, these methods are trained and evaluated on common objects such as human and cars. To perform on the animal, there is a need to create large datasets of different types in multiple conditions. The dataset construction comprises of data collection and data annotation. In this work, we put more focus on the latter task. Particularly, we renovate the well-known tool, LabelMe, so as to assist common user with or without in-depth knowledge about computer science to annotate the data with less effort. The new tool named as TrackMe inherits the simplicity, high compatibility with varied systems, minimal hardware requirement and con

## Méthodologie

{'study_design': "Article de description d'outil (tool paper) présentant le développement logiciel de TrackMe, une extension de LabelMe intégrant des fonctionnalités de suivi multi-objets", 'intervention': "Ajout des fonctionnalités suivantes à LabelMe : champ ID d'objet, dialogues 'Polygon IDs' et 'Navigation', interpolation de boîtes/ID via Gaussian Process Regression (GPR) avec noyau Rational Quadratic, association d'ID basée sur suivi-par-détection (YOLO-v8 pour la détection, SORT pour l'association), et fonctionnalités de modification de boîtes/ID sur plusieurs frames", 'control': None, 'primary_outcomes': ["Fonctionnalités d'annotation de suivi multi-objets intégrées à l'outil (interpolation, association d'ID, modification)"], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': "Développement logiciel basé sur l'outil open source LabelMe, en Python"}

## Résultats

{'quantitative': [], 'qualitative_findings': ["TrackMe hérite de la simplicité, de la haute compatibilité avec divers systèmes, des exigences matérielles minimales et de l'utilisation pratique des fonctionnalités de LabelMe", "La fonctionnalité 'Box/ID Interpolation' basée sur GPR permet de compléter automatiquement les boîtes manquantes entre des frames annotées, sans nécessiter de GPU", "Deux fonctionnalités d'association d'ID sont proposées : 'Track from Scratch' et 'Track with Current Annotation'", "'Box & ID Modification' permet la suppression de boîtes et l'ajustement de labels/ID sur une série d'images, contrairement à LabelMe limité à la correction d'une seule frame"], 'main_findings': ["TrackMe ajoute un champ ID à LabelMe et adapte l'interface graphique pour l'annotation de suivi d'objets", 'TrackMe intègre des fonctionnalités de génération et de modification de pistes (tracklets) absentes de LabelMe', "L'entraînement et la prédiction du GPR sont rapides et ne nécessitent pas de GPU"]}

## Conclusions

TrackMe est un outil de suivi vidéo complet et facile à utiliser, adapté à tout type de sujet L'outil vise à aider un plus grand nombre de personnes, avec ou sans connaissances en informatique, à installer et utiliser confortablement des fonctionnalités de suivi TrackMe sera mis à jour avec de nouvelles fonctionnalités d'annotation vidéo et le code sera publié pour d'autres développeurs
