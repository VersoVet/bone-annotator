# Automated identification of bones and joints in whole-body CT-scan images of pigs.

**Auteurs** : Øyvind Nordbø, Muhammad Umair Hassan, Lars Erik Gangsei, Eli Grindflek, Kristin Olstad
**Année** : 2026
**DOI** : 10.1093/jas/skaf449

## Résumé

Computed tomography (CT) images provide fast and accurate non-invasive measurements of anatomy, which are crucial in pig breeding. In the commercial breeding program of Topigs Norsvin, the CT-images are mainly used for estimation of carcass value and for scoring the severity of osteochondrosis lesions in joints. This study presents the first major step towards automated detection of osteochondrosis, using CT images. This involves an anatomic segmentation model that can segment 29 classes of different tissues, like individual bones, muscles, and organs. The algorithm then identifies major joints in the fore- and hindlimbs by detecting the center points of the joints, and this method is validated against manually labeled data. Average distance between labeled and predicted center points was 29 mm (SD = 13mm). The next step will utilize these center points to create bounding boxes for local segmentation models to focus on relevant subsets of voxels, enhancing the detection of lesions in j

## Méthodologie

{'study_design': "Analyse rétrospective de données collectées dans le cadre d'un programme d'élevage approuvé ; développement d'un modèle de segmentation anatomique par apprentissage profond segmentant 29 classes de tissus (os individuels, muscles, organes), suivi d'un algorithme identifiant les articulations majeures des membres antérieurs et postérieurs en détectant les points centraux des articulations, validé contre des données annotées manuellement", 'intervention': None, 'control': None, 'primary_outcomes': ['Distance entre les points centraux des articulations prédits et les points de référence (ground truth) annotés manuellement'], 'secondary_outcomes': ["Ratio segmentation/arrière-plan (background) pour les modèles de détection des lésions d'ostéochondrose", "Proportion des lésions d'ostéochondrose couvertes par les bounding boxes proposées"], 'statistical_methods': [], 'duration': None, 'setting': 'Programme de sélection reproductrice de TopigsNorsvin, avec des animaux soumis aux réglementations de bien-être animal en Norvège et au Canada'}

## Résultats

{'quantitative': [{'outcome': 'Distance moyenne entre les points centraux annotés (ground truth) et les points prédits', 'value': '29', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': 'SD = 13 mm', 'source_section': 'Abstract', 'source_quote': 'Average distance between labeled and predicted center points was 29 mm (SD = 13mm).'}, {'outcome': 'Distance moyenne entre les points centraux prédits et les points de référence, validée sur 199 animaux', 'value': '29', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'Leg joint predictions have been validated against manual segmentations of joint lesions in the shoulder, elbows, knees, and ankles of 199 pigs, resulting in average distance of 29 mm between predicted center points and key-point ground truth.'}, {'outcome': "Couverture des lésions d'ostéochondrose par des bounding boxes de 128 pixels", 'value': '99', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'With this approach, we can create bounding boxes with 128 pixels in each direction, covering 99% of osteochondrosis lesions in the validation data, and at the same time improve the segmentation/background ratio 150-fold, compared with using full CT-scan images.'}, {'outcome': 'Amélioration du ratio segmentation/arrière-plan avec les bounding boxes proposées', 'value': '150-fold', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'With this approach, we can create bounding boxes with 128 pixels in each direction, covering 99% of osteochondrosis lesions in the validation data, and at the same time improve the segmentation/background ratio 150-fold, compared with using full CT-scan images.'}, {'outcome': 'Nombre de voxels dans un scan CT corps entier de porc', 'value': '260-327 million', 'unit': 'voxels', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Introduction', 'source_quote': 'A whole-body CT scan of a pig contains 512 × 512 pixels times 1,000-1,250 transverse slices depending on individual pig length, that is, 260-327 million voxels (Aasmundstad et al., 2013).'}, {'outcome': "Volume moyen des lésions d'ostéochondrose", 'value': '26 to 42', 'unit': 'mm3 (≈22-35 voxels)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Introduction', 'source_quote': 'In a recent labeling study (Olstad et al., 2022b), covering different limb joints in pigs, the mean lesion volume ranged from 26 to 42 mm 3 , which corresponds to ∼22-35 voxels.'}], 'qualitative_findings': [], 'main_findings': ['Un modèle de segmentation anatomique capable de segmenter 29 classes de tissus (os individuels, muscles, organes) a été développé', "L'algorithme identifie les articulations majeures des membres antérieurs et postérieurs en détectant leurs points centraux", 'La distance moyenne entre les points prédits et les points annotés manuellement (ground truth) est de 29 mm (SD = 13 mm), validée sur 199 porcs', "Les bounding boxes de 128 pixels par direction couvrent 99% des lésions d'ostéochondrose et améliorent le ratio segmentation/arrière-plan d'un facteur 150 par rapport aux images CT complètes"]}

## Conclusions

Des méthodes automatisées ont été développées pour segmenter 29 classes de tissus et identifier les articulations des membres dans des images CT de porcs La détection des articulations (épaule, coude, genou, cheville) a été validée contre des données annotées manuellement sur 199 animaux, avec une distance moyenne de 29 mm entre prédictions et vérité terrain La méthode présentée sera utilisée pour extraire automatiquement des bounding boxes pertinentes autour des articulations des membres, afin d'améliorer le ratio segmentation/arrière-plan dans les modèles de ML pour la détection des lésions d'ostéochondrose Cette approche pourrait rendre les programmes de sélection porcine plus durables et rentables en aidant les éleveurs à sélectionner des animaux avec une meilleure santé articulaire grâce à une technologie intelligente plutôt qu'à un scoring manuel

## segmentation model Class Body region Side N.A.V. 1 terminology Term used 1 (single bone)

|  | Forelimb | L 2 | Scapula | Scapula |
| --- | --- | --- | --- | --- |
| 2 (single bone) | Forelimb | L | Humerus | Humerus |
| 3 (bone pair) | Forelimb | L | Radius and ulna | Radius |
| 4 (bone group) | Forelimb | L | Carpus, metacarpals and digits | Carpus |
| 5 (bone group) | Hindlimb | L | Pelvis | Pelvis |
| 6 (single bone) | Hindlimb | L | Femur | Femur |
| 7 (bone pair) | Hindlimb | L | Tibia and fibula | Tibia |
| 8 (bone group) | Hindlimb | L | Tarsus, metatarsals and digits | Tarsus |
| 9 (single bone) | Forelimb | R 3 | Scapula | Scapula |
| 10 (single bone) | Forelimb | R | Humerus | Humerus |
| 11 (bone pair) | Forelimb | R | Radius and ulna | Radius |
| 12 (bone group) | Forelimb | R | Carpus, metacarpals and digits | Carpus |
| 13 (bone group) | Hindlimb | R | Pelvis | Pelvis |
| 14 (single bone) | Hindlimb | R | Femur | Femur |
| 15 (bone pair) | Hindlimb | R | Tibia and fibula | Tibia |
| 16 (bone group) | Hindlimb | R | Tarsus, metatarsals and digits | Tarsus |
| 17 (bone group) | Hindlimb | L & R | Patellae | Kneecap |
| 18 (bone group) | Trunk | L | Costae | Ribs |
| 19 (bone group) | Trunk | R | Costae | Ribs |
| 20 (bone group) | Head | N.A 4 | Caput | Head |
| 21 (bone group) | Spine | N.A | Cervical vertebrae | Neck |
| 22 (bone group | Spine | N.A | Thoracic vertebrae | Upper back |
| 23 (bone group) | Spine | N.A | Lumbar vertebrae | Lower back |
| 24 (bone group) | Spine | N.A | Sacral and coccygeal vertebrae | Tail |
| 25 (bone group) | Trunk | N.A | Sternum | Breastbone |
| 26 (muscle) | Spine | L & R | Longissimus dorsi | Longissimus dorsi |
| 27 (internal organ) | Thorax | N.A | Cor | Heart |
| 28 (internal organ) | Thorax | L & R | Pulmones | Lungs |
| 29 (internal organ) | Thorax | L & R | Everything except heart and lungs | Connective tissue |

## Overview of which bone classes, which were used to calculate the joint

| Joint (N.A.V. 1 | Term | Bone 1 | Bone 2 |
| --- | --- | --- | --- |
| terminology) | used here |  |  |
| Shoulder | Shoulder | Scapula | Humerus |
| (scapulo-humeral joint) |  |  |  |
| Elbow (cubital joint) | Elbow | Humerus | Radius |
|  |  |  | (and ulna) |
| Carpus (radio-carpal | Wrist | Radius | Carpus (and |
| articulation) |  | (and ulna) | distal |
|  |  |  | forelimb) |
| Hip (coxo-femoral joint) | Hip | Femur | Pelvis |
| Stifle (femoro-tibial | Knee | Tibia | Femur |
| joint; knee) |  | (and fibula) |  |
| Tarsus (tarso-crural | Ankle | Tibia | Tarsus (and |
| articulation) |  | (and fibula) | distal |
|  |  |  | hindlimb) |

## Averaged statistics on validation against true segmentations on 199 pigs inside_128 is the ratio of labels within a bouding box of 128 pixels in all directions, centered in the predicted joint center point.

| Joint | Absdiff 1 , mm |  | Npoints 2 |  | min_bb 3 , mm |  | inside_64 4 | inside_128 5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| elbow_l | 35 | (15) | 175 | (352) | 19 | (15) | 0.74 | 0.99 |
| elbow_r | 34 | (15) | 192 | (361) | 20 | (15) | 0.77 | 0.99 |
| ankle_l | 36 | (8) | 70 | (91) | 12 | (14) | 0.5 | 1 |
| ankle_r | 39 | (16) | 91 | (152) | 11 | (12) | 0.47 | 0.99 |
| knee_l | 26 | (8) | 863 | (554) | 59 | (13) | 0.79 | 0.99 |
| knee_r | 25 | (13) | 973 | (658) | 59 | (10) | 0.81 | 0.99 |
| shoulder_l | 20 | (15) | 191 | (252) | 35 | (23) | 0.9 | 0.98 |
| shoulder_r | 21 | (12) | 249 | (421) | 37 | (24) | 0.89 | 0.98 |
| Mean | 29 | (13) | 351 | (355) | 32 | (16) | 0.74 | 0.99 |
| Standard deviations are shown in parenthesis. |  |  |  |  |  |  |
| 1 absdiff, the distance between predicted joint center point and mass center point of lesions for that joint. |  |  |
| 2 Npoints, the number labeled voxels for the joint. |  |  |  |  |  |  |
| 3 min_bb, the minimum size of bounding box to capture all labeled voxels. |  |  |  |  |
| 4 inside_64 is the ratio of labels within a bouding box of 64 pixels in all directions, centered in the predicted joint center point. |  |

### Formule


$$= - + + 1 (1) BCE N y p y p i N i i i i = - ( )+ - ( ) - = ∑ 1 1 1 1 log log( )(2)$$

### Formule


$$v 1 of X X c T c ; vX X X X c T c c T c = λ(3)$$

### Formule


$$R v v v =           1 2 3 (4)$$

### Formule


$$If min min then d p q d p q d p q d p q p joi 1 1 1 2 2 1 2 2 , ,, , , , , ( ) ( )$$

### Formule


$$( ) < ( ) ( ) ( ) ( ) n n t joint p p p = = 1 2 else, .(5)$$
