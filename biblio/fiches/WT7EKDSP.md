# Automated identification of bones and joints in whole-body CT-scan images of pigs.

**Auteurs** : Nordbø Ø, Hassan MU, Gangsei LE, Grindflek E, Olstad K.
**Année** : 2026
**DOI** : 10.1093/jas/skaf449

## Résumé

Computed tomography (CT) images provide fast and accurate non-invasive measurements of anatomy, which are crucial in pig breeding. In the commercial breeding program of Topigs Norsvin, the CT-images are mainly used for estimation of carcass value and for scoring the severity of osteochondrosis lesions in joints. This study presents the first major step towards automated detection of osteochondrosis, using CT images. This involves an anatomic segmentation model that can segment 29 classes of different tissues, like individual bones, muscles, and organs. The algorithm then identifies major joints in the fore- and hindlimbs by detecting the center points of the joints, and this method is validated against manually labeled data. Average distance between labeled and predicted center points was 29 mm (SD = 13mm). The next step will utilize these center points to create bounding boxes for local segmentation models to focus on relevant subsets of voxels, enhancing the detection of lesions in j

## Méthodologie

{'study_design': "Analyse rétrospective de données collectées dans le cadre d'un programme de sélection approuvé ; développement d'un modèle de segmentation anatomique (deep learning) segmentant 29 classes de tissus, suivi d'un algorithme de détection des centres des articulations majeures des membres antérieurs et postérieurs, validé contre des données annotées manuellement", 'intervention': None, 'control': None, 'primary_outcomes': ["Distance entre les points centraux des articulations prédits par l'algorithme et les points centraux annotés manuellement (ground truth)"], 'secondary_outcomes': ["Couverture des lésions d'ostéochondrose par les bounding boxes générées", "Amélioration du ratio segmentation/background par rapport à l'utilisation d'images CT complètes"], 'statistical_methods': ['Distance moyenne (average distance)', 'Écart-type (SD)'], 'duration': None, 'setting': 'Programme de sélection commerciale de TopigsNorsvin, animaux élevés en Norvège et au Canada'}

## Résultats

{'quantitative': [{'outcome': 'Distance moyenne entre points centraux annotés et prédits des articulations', 'value': '29', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': 'SD = 13mm', 'source_section': 'Discussion', 'source_quote': 'Leg joint predictions have been validated against manual segmentations of joint lesions in the shoulder, elbows, knees, and ankles of 199 pigs, resulting in average distance of 29 mm between predicted center points and key-point ground truth.'}, {'outcome': "Couverture des lésions d'ostéochondrose par les bounding boxes de 128 pixels", 'value': '99', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'we can create bounding boxes with 128 pixels in each direction, covering 99% of osteochondrosis lesions in the validation data, and at the same time improve the segmentation/background ratio 150-fold, compared with using full CT-scan images.'}], 'qualitative_findings': [], 'main_findings': ["Développement d'un modèle de segmentation anatomique capable de segmenter 29 classes de tissus (os individuels, muscles, organes)", 'Identification automatisée des articulations majeures des membres via détection des points centraux, validée contre des données annotées manuellement', "Les bounding boxes de 128 pixels par direction couvrent 99% des lésions d'ostéochondrose et améliorent le ratio segmentation/background d'un facteur 150 par rapport aux images CT complètes"]}

## Conclusions

Des méthodes automatisées ont été développées pour segmenter 29 classes de tissus et identifier les articulations des membres dans des images CT-scan de porcs La détection de l'épaule, du coude, du genou et de la cheville a été validée contre des données annotées manuellement sur 199 animaux, avec une distance moyenne de 29 mm entre les prédictions et le ground truth La méthode présentée sera utilisée pour extraire automatiquement des bounding boxes pertinentes autour des articulations des membres, afin d'améliorer le ratio segmentation/background dans les modèles de ML pour la détection des lésions d'ostéochondrose

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
