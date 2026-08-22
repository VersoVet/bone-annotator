# PFUS1: Premier pelvic floor ultrasound segmentation dataset. A resource for advancing research.

**Auteurs** : Solís-Martín D, Sainz JA, Galán-Páez J, Borrego-Díaz J, García-Mejido JA.
**Année** : 2026
**DOI** : 10.1016/j.dib.2025.112346

## Résumé

This article presents a curated dataset of transperineal pelvic floor ultrasound videos collected from 111 patients in a clinical setting using a Canon i700 Aplio® ultrasound system with a PVT-675 MV 3D probe. Each video captures the midsagittal view of pelvic floor organs at rest and during the Valsalva maneuver. Eight anatomical structures were manually annotated by an expert sonographer using the CVAT platform, resulting in pixel-level segmentation masks. The dataset is intended to support research in automated pelvic floor assessment, medical image segmentation, and dynamic organ tracking. To facilitate reuse, a public source code repository is provided with scripts for data loading, mask generation, and training of baseline deep learning models, including Feature Pyramid Networks (FPNs). This dataset represents the first annotated ultrasound video resources focused on pelvic floor anatomy and is designed to enable benchmarking, reproducibility, and methodological innovation in com

## Méthodologie

{'study_design': "Étude descriptive de création et curation d'un jeu de données (dataset paper) comprenant collecte de données, annotation manuelle, préparation des données, conception et exécution d'expérimentations de validation, et analyse des résultats.", 'intervention': "Manœuvre de Valsalva réalisée par les patientes pendant l'échographie transpérinéale, en complément d'une acquisition au repos", 'control': "Comparaison intra-patiente entre l'état de repos et la manœuvre de Valsalva (pas de groupe contrôle séparé)", 'primary_outcomes': ["Production de masques de segmentation pixel par pixel pour huit structures anatomiques (pubis, urètre, vessie, vagin, utérus, anus, rectum, muscle releveur de l'anus)"], 'secondary_outcomes': ["Validation du jeu de données via l'entraînement d'un modèle de deep learning de référence (FPN)"], 'statistical_methods': ["Score de Dice pour l'évaluation du modèle de segmentation", 'Interpolation linéaire entre images annotées pour générer les labels des images non annotées'], 'duration': 'Recrutement des patientes entre le 1er avril et le 31 juillet 2023', 'setting': "Consultations de gynécologie générale, hôpital unique en Andalousie, Espagne (étude approuvée par le Andalucia's Board of Biomedicine Ethics Committee, code 0625-N-23)"}

## Résultats

{'quantitative': [{'outcome': 'Score de Dice du modèle de segmentation entraîné sur le jeu de données', 'value': '0.79', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Experimental Design, Materials and Methods', 'source_quote': 'The validity of the dataset has been demonstrated by training different deep learning models, achieving a model with a Dice score of 0.79 [ 1 ].'}], 'qualitative_findings': [], 'main_findings': ["Création d'un jeu de données de vidéos échographiques transpérinéales du plancher pelvien avec annotations manuelles de huit structures anatomiques via la plateforme CVAT", "Le jeu de données couvre à la fois l'état de repos et la manœuvre de Valsalva, permettant une analyse dynamique", 'Un pipeline de prétraitement (binarisation, érosion, dilatation, extraction de contours) isole le cône échographique', "Un dépôt de code source public est fourni pour le chargement des données, la génération des masques et l'entraînement d'un réseau FPN", "Ce jeu de données constitue la première ressource vidéo échographique annotée dédiée à l'anatomie du plancher pelvien"]}

## Conclusions

Ce jeu de données représente la première ressource de vidéos échographiques annotées centrée sur l'anatomie du plancher pelvien Il est conçu pour permettre le benchmarking, la reproductibilité et l'innovation méthodologique en diagnostic assisté par ordinateur et analyse d'images médicales

## Table

| }, |
| --- |
| … |
| … |
| … |
| ] |

## Dataset summary.

| Characteristic | Value |
| --- | --- |
| Number of patients | 101 |
| Total video sequences | 101 |
| Video types | Valsalva maneuver |
| Annotated organs | 8 (bladder, urethra, vagina, rectum, anal canal, levator ani, pubic bone, rectal ampulla) |
| Total frames | 45-245 |
| Labeled frames | 12-51 |
| Frame resolution | 70 0 ×50 0 |
| File format -Videos | List of PNG files (one per frame) |
| File format -Annotations | JSON |
| Total dataset size | 5,4 GB |
| Imaging modality | Transperineal ultrasound |
| Plane of acquisition | Midsagittal |
