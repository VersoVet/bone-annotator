# SAMJ: fast image annotation on ImageJ/Fiji via segment anything model.

**Auteurs** : Carlos García-López-de-Haro, Caterina Fuster-Barceló, Curtis T Rueden, Jónathan Heras, Vladimír Ulman, Daniel Franco-Barranco, Adrián Inés, Kevin W Eliceiri, Jean-Christophe Olivo-Marin, Jean-Yves Tinevez, Daniel Sage, Arrate Muñoz-Barrutia
**Année** : 2026
**DOI** : 10.1038/s41467-026-71752-x

## Résumé

Accurate image annotation is essential for training artificial intelligence (AI) systems in biomedical image analysis, enabling tasks such as cell detection, tissue quantification, and disease characterization. However, creating pixel-level annotations is a time-consuming and labor-intensive process that requires expert input, limiting the development and adoption of AI methods. Recent advances in foundation models, such as the Segment Anything Model (SAM), enable interactive object segmentation from simple user prompts, but their integration into widely used bioimage analysis platforms remains limited and often requires technical expertise. Here we show that SAMJ, a user-friendly plugin for ImageJ/Fiji, enables fast, interactive, and accurate image annotation on standard computers without requiring programming skills or specialized hardware. SAMJ integrates efficient SAM variants into a familiar graphical interface, allowing users to delineate objects in large scientific images in rea

## Méthodologie

{'study_design': "Présentation d'un outil logiciel (plugin ImageJ/Fiji) accompagnée d'une évaluation comparative de performance d'annotation (benchmarking) entre SAMJ et deux autres outils basés sur SAM (Micro-SAM et l'extension SAM de QuPath), sur plusieurs jeux de données publics d'images biomédicales.", 'intervention': 'Utilisation du plugin SAMJ pour générer des annotations (masques) à partir de prompts (points ou bounding boxes) dérivés automatiquement des annotations de référence (ground truth)', 'control': "Comparaison avec Micro-SAM et l'extension SAM de QuPath, restreinte aux variantes fine-tuned de SAM (et SAM Huge pour les deux autres outils)", 'primary_outcomes': ['Intersection-over-Union (IoU) entre les masques générés et les annotations de référence (ground truth)'], 'secondary_outcomes': ["Facilité d'utilisation (modèles disponibles, compatibilité CPU-only, accélération GPU optionnelle)", 'Temps de chargement du modèle', 'Vitesse de réponse aux prompts', 'Installation en un clic'], 'statistical_methods': [], 'duration': None, 'setting': "Benchmarking réalisé sur des jeux de données publics d'imagerie biomédicale (microscopie optique et électronique)"}

## Résultats

{'quantitative': [], 'qualitative_findings': ['SAMJ permet de délinéer des objets dans de grandes images scientifiques en temps réel via des clics simples ou des bounding boxes', "Dans le cas d'usage de la motilité bactérienne, les annotations de SAMJ sont hautement cohérentes avec les labels de référence générés manuellement", "Le prompting compositionnel multi-étapes (segmentation de sous-structures individuelles fusionnées) donne des annotations significativement plus précises pour les structures allongées ou ramifiées qu'une inférence à prompt unique"], 'main_findings': ['SAMJ intègre SAM dans Fiji via une installation en un clic, sans nécessiter de compétences en programmation ni de matériel spécialisé', 'SAMJ propose cinq variantes de SAM (SAM-2 Tiny, Small, Large, EfficientSAM, EfficientViTSAM-L2) offrant un compromis entre performance et ressources de calcul', "SAMJ s'intègre à Labkit et BigDataViewer, et propose une API Java documentée", "Le pont Java-Python via Appose (avec gestion automatique de l'environnement Python par Micromamba) élimine la configuration manuelle", "SAMJ offre deux modes d'annotation : Live (interactif, un objet à la fois) et Batch (BatchSAMize, segmentation de plusieurs objets à partir de seeds)", 'SAMJ permet une annotation efficace de volumes 3D de microscopie électronique via son intégration à Labkit']}

## Conclusions

SAMJ fournit un moyen convivial et accessible pour les biologistes et les analystes en bioimagerie d'adopter des méthodes d'IA de pointe, facilitant une annotation d'images plus rapide et plus précise SAMJ contribue à la création de jeux de données annotés de haute qualité, favorisant le développement de modèles plus précis et robustes L'intégration de SAM dans Fiji via SAMJ comble une lacune, les plugins Fiji existants comme AnnotatorJ ne disposant pas d'un support direct de SAM contrairement à QuPath et Napari

## Summary of tools integrating annotation capabilities in bioimage analysis platforms

| Tool/Plugin | Platform | Release | Last Update | AI assistance | Annotation | Programming language |
| --- | --- | --- | --- | --- | --- | --- |
| MicroSAM | Napari | 2023 | 03/2025 | Yes (SAM fine-tune) | Polygons BBox Points | Python |
| QuPath Ext. SAM | QuPath | 2023 | 09/2024 | Yes (SAM2) | AutoMask BBox Poitns | Python |
| Napari Plugin of SAM | Napari | 2023 | 04/2023 | Yes (SAM1) | BBox Points | Python |
| Napari Plugin of SAM2 | Napari | 2024 | 09/2024 | Yes (SAM2) | BBox Points | Python |
| AnnotatorJ | Fiji | 2020 | 10/2020 | Yes (CNN) | Instance Semantic BBox | Java |
| Labkit | Fiji | 2022 | 10/2024 | Yes (Random For- | Pixel Classification | Java |
|  |  |  |  | est SAM1,2) |  |  |
| Qualitative Annotations | Fiji | 2020 | 04/2021 | Yes (CNN) | One or Multiple ROI | Python |
| SAMJ | Fiji | 2025 | 04/2025 | Yes (SAM1,2) | BBox Points | Java |

## Comparison of features across SAM-based annotation tools

| Software | One-Click | CPU | GPU | Models |
| --- | --- | --- | --- | --- |
|  | Installation Support | Support Available |
| SAMJ | YES | YES | NO | SAM2 Tiny |
|  | YES | YES | NO | SAM2 Small |
|  | YES | YES | NO | SAM2 Large |
|  | YES | YES | NO | EfficientSAM |
|  | YES | YES | NO | EfficientViTSAM-L2 |
| Micro-SAM | NO | Slow | YES | SAM Base |
|  | NO | Slow | YES | SAM Base Light |
|  | NO | Slow | YES | SAM Base LM fine-tuned |
|  | NO | Slow | YES | SAM Large LM |
|  |  |  |  | fine-tuned |
|  | NO | Slow | YES | SAM Large EM |
|  |  |  |  | fine-tuned |
|  | NO | YES | YES | MobileSAM |
|  | NO | YES | YES | MobileSAM LM |
|  |  |  |  | fine-tuned |
|  | NO | YES | YES | MobileSAM EM |
|  |  |  |  | fine-tuned |
| QuPath-SAM | NO | NO | YES | SAM Huge LM |
|  |  |  |  | fine-tuned |
|  | NO | NO | YES | SAM Huge EM |
|  |  |  |  | fine-tuned |
|  | NO | Slow | YES | SAM Huge |
|  | NO | Slow | YES | SAM Large |
|  | NO | Slow | YES | SAM Base |
|  | NO | YES | YES | MobileSAM |
|  | NO | YES | YES | SAM2 Tiny |
|  | NO | YES | YES | SAM2 Small |
|  | NO | YES | YES | SAM2 Base Plus |
|  | NO | YES | YES | SAM2 Large |
| LM Light Microscopy, EM Electron Microscopy. |  |  |

## time denotes the time required to load a model and encode the image on the CPU before annotation begins. For QuPathSAM, this metric is not applicable because the software does not pre-encode the image; instead, it encodes only the region around the user-provided prompt. If subsequent prompts fall within an already encoded region, no additional computation is required; otherwise, QuPathSAM performs a new local encoding step.

| | CPU-only model loading and annotation times |
| --- | --- | --- | --- |
| across software tools |  |  |
| Software | Model | Load | Annotation |
|  |  | time (s) | time (s) |
| SAMJ | SAM2 Tiny | 1.91 | 0.06 |
|  | SAM2 Small | 2.00 | 0.07 |
|  | SAM2 Large | 3.56 | 0.07 |
|  | EfficientSAM | 2.69 | 0.08 |
|  | EfficientViTSAM-L2 | 1.37 | 0.08 |
| Micro-SAM | MobileSAM LM | 2.27 | 0.04 |
|  | MobileSAM EM | 1.98 | 0.03 |
|  | SAM Base LM | 8.65 | 0.05 |
|  | SAM Base EM | 8.38 | 0.07 |
|  | SAM Large LM | 26.03 | 0.06 |
|  | SAM Large EM | 25.03 | 0.05 |
|  | SAM Huge | 39.39 | 0.04 |
| QuPathSAM | SAM2 Tiny | NA | 0.31 |
|  | SAM2 Small LM | NA | 0.32 |
|  | SAM2 Base Plus EM | NA | 0.58 |
|  | MobileSAM LM | NA | 0.25 |
|  | SAM Huge EM | NA | Only GPU |
|  | SAM Huge LM | NA | Only GPU |

## IoU of annotations produced by each model across datasets

| Software | Model | 21 | 22 | 23 | 24 | 25 | 25 | 26 | 27 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | C | C | B | C | N | C | M | M |
| SAMJ | SAM2 Tiny* | 0.64 | 0.35 | 0.36 | 0.57 | 0.66 | 0.45 | 0.79 | 0.69 |
|  | SAM2 Tiny † | 0.77 | 0.74 | 0.74 | 0.84 | 0.81 | 0.72 | 0.88 | 0.82 |
|  | SAM2 Small* | 0.63 | 0.35 | 0.36 | 0.57 | 0.67 | 0.42 | 0.82 | 0.71 |
|  | SAM2 Small † | 0.77 | 0.73 | 0.74 | 0.84 | 0.82 | 0.73 | 0.88 | 0.82 |
|  | SAM2 Large* | 0.66 | 0.37 | 0.42 | 0.60 | 0.70 | 0.43 | 0.82 | 0.73 |
|  | SAM2 Large † | 0.78 | 0.74 | 0.73 | 0.84 | 0.81 | 0.72 | 0.88 | 0.82 |
|  | EfficientSAM* | 0.63 | 0.40 | 0.39 | 0.55 | 0.68 | 0.42 | 0.69 | 0.70 |
|  | EfficientSAM † | 0.74 | 0.69 | 0.68 | 0.81 | 0.77 | 0.62 | 0.87 | 0.79 |
|  | EfficientViTSAM-L2* | 0.69 | 0.50 | 0.41 | 0.61 | 0.71 | 0.47 | 0.82 | 0.73 |
|  | EfficientViTSAM-L2 † | 0.80 | 0.77 | 0.76 | 0.86 | 0.85 | 0.76 | 0.90 | 0.86 |
| Micro-SAM | MobileSAM LM* | 0.69 | 0.60 | 0.60 | 0.77 | 0.75 | 0.66 | 0.33 | 0.65 |
|  | MobileSAM LM † | 0.82 | 0.80 | 0.76 | 0.85 | 0.84 | 0.80 | 0.77 | 0.84 |
|  | MobileSAM EM* | 0.48 | 0.47 | 0.40 | 0.60 | 0.67 | 0.56 | 0.39 | 0.76 |
|  | MobileSAM EM † | 0.62 | 0.71 | 0.62 | 0.78 | 0.87 | 0.77 | 0.79 | 0.87 |
|  | SAM Base LM* | 0.74 | 0.69 | 0.70 | 0.82 | 0.74 | 0.70 | 0.46 | 0.69 |
|  | SAM Base LM † | 0.85 | 0.83 | 0.82 | 0.89 | 0.84 | 0.82 | 0.79 | 0.84 |
|  | SAM Base EM* | 0.58 | 0.49 | 0.38 | 0.58 | 0.64 | 0.53 | 0.53 | 0.81 |
|  | SAM Base EM † | 0.77 | 0.71 | 0.65 | 0.76 | 0.84 | 0.78 | 0.80 | 0.88 |
|  | SAM Large LM* | 0.77 | 0.71 | 0.74 | 0.83 | 0.75 | 0.71 | 0.49 | 0.69 |
|  | SAM Large LM † | 0.86 | 0.83 | 0.83 | 0.89 | 0.84 | 0.83 | 0.78 | 0.84 |
|  | SAM Large EM* | 0.57 | 0.50 | 0.41 | 0.57 | 0.62 | 0.53 | 0.59 | 0.82 |
|  | SAM Large EM † | 0.76 | 0.69 | 0.63 | 0.75 | 0.84 | 0.78 | 0.78 | 0.89 |
|  | SAM Huge* | 0.64 | 0.28 | 0.30 | 0.55 | 0.64 | 0.35 | 0.44 | 0.70 |
|  | SAM Huge † | 0.76 | 0.69 | 0.62 | 0.75 | 0.79 | 0.59 | 0.71 | 0.82 |
| QuPath-SAM | SAM2 Tiny* | 0.57 | 0.29 | 0.32 | 0.57 | 0.28 | 0.36 | 0.41 | 0.75 |
|  | SAM2 Tiny † | 0.74 | 0.71 | 0.65 | 0.78 | 0.72 | 0.62 | 0.65 | 0.84 |
|  | SAM2 Small* | 0.56 | 0.32 | 0.32 | 0.55 | 0.25 | 0.34 | 0.42 | 0.70 |
|  | SAM2 Small † | 0.76 | 0.68 | 0.64 | 0.77 | 0.75 | 0.65 | 0.65 | 0.84 |
|  | SAM2 Base+* | 0.59 | 0.40 | 0.31 | 0.55 | 0.25 | 0.38 | 0.42 | 0.59 |
|  | SAM2 Base+ † | 0.75 | 0.70 | 0.63 | 0.76 | 0.71 | 0.64 | 0.65 | 0.84 |
|  | MobileSAM* | 0.47 | 0.25 | 0.31 | 0.54 | 0.20 | 0.27 | 0.25 | 0.51 |
|  | MobileSAM † | 0.71 | 0.62 | 0.61 | 0.73 | 0.68 | 0.57 | 0.64 | 0.77 |
|  | SAM Huge LM* | 0.66 | 0.69 | 0.70 | 0.77 | 0.45 | 0.53 | 0.29 | 0.67 |
|  | SAM Huge LM † | 0.75 | 0.80 | 0.81 | 0.87 | 0.68 | 0.64 | 0.69 | 0.73 |
|  | SAM Huge EM* | 0.59 | 0.45 | 0.46 | 0.56 | 0.48 | 0.51 | 0.46 | 0.81 |
|  | SAM Huge EM † | 0.74 | 0.65 | 0.70 | 0.72 | 0.63 | 0.68 | 0.71 | 0.80 |
