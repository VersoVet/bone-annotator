# A wild fish image dataset for individual re-identification and phenotyping.

**Auteurs** : Sørdalen TK, Malde K, Sauvaitre C, Skiftesvik AB, Beyan C, Larsen T, Halvorsen KT.
**Année** : 2026
**DOI** : 10.1038/s41597-026-07045-1

## Résumé

Computer vision can transform wildlife monitoring by automating phenotyping and individual identification. Achieving this, however, depends on access to large, well-curated image datasets that capture natural variation across individuals and years. Here, we present Melops, a longitudinal dataset comprising 24 578 images of 9 861 individual corkwing wrasse, Symphodus melops, collected over seven years through a capture-mark-recapture survey. Each fish was PIT-tagged for re-identification and photographed from both sides against a standardized white background with a colour reference. Alongside the images, we provide metadata including body length, sex, and reproductive state. To support deep learning applications, the dataset includes both the original photographs and automatically cropped images focusing on the whole fish or specific body regions. Together, these resources provide a foundation for developing computer vision methods for individual re-identification, colour pattern analy

## Méthodologie

{'study_design': "Étude de capture-marquage-recapture (CMR) longitudinale sur sept ans, avec photographie standardisée bilatérale de chaque individu marqué par PIT-tag ; constitution d'un dataset d'images accompagné de métadonnées et d'annotations pour l'entraînement de modèles de vision par ordinateur.", 'intervention': None, 'control': None, 'primary_outcomes': ['Ré-identification individuelle par vision par ordinateur (re-ID)', 'Classification du sexe / des morphes mâles', 'Analyse des motifs de couleur'], 'secondary_outcomes': ["Détection automatique des régions d'intérêt (corps, tête) et des points anatomiques (keypoints)", 'Évaluation de la performance humaine de ré-identification (benchmark FishFaces)', "Cohérence de l'échelle des images dans le temps"], 'statistical_methods': ['Apprentissage métrique contrastif (triplet loss, hard triplet mining) avec réseau Inception v3 tronqué', "Classification par plus proche voisin (nearest-neighbour) dans l'espace d'embedding", "Détection d'objets YOLOv5 / YOLOv8", 'Formule CIEDE2000 pour le Mean Colour Error (MCE)'], 'duration': 'Sept ans (collecte principale), avec données opportunistes complémentaires entre 2019 et 2023', 'setting': "Ouest de la Norvège, plusieurs sites d'échantillonnage, principalement en août/septembre (après la saison de croissance maximale)"}

## Résultats

{'quantitative': [{'outcome': 'Identification rank-1 (one-shot) par le modèle de ré-identification', 'value': '35%', 'unit': '% accuracy', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Background & Summary', 'source_quote': 'The system achieved 35% oneshot (rank-1 accuracy) identification on a held-out test set, which increased to 53% when combining predictions from the left and right sides of the fish as an ensemble classifier.'}, {'outcome': 'Identification rank-1 avec ensemble gauche/droite', 'value': '53%', 'unit': '% accuracy', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Background & Summary', 'source_quote': 'which increased to 53% when combining predictions from the left and right sides of the fish as an ensemble classifier'}, {'outcome': "Nombre total d'images du dataset Melops", 'value': '24578', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Overview of data', 'source_quote': 'The Melops dataset includes 24 578 images of 9 861 individual corkwing wrasse, of which 1 882 individuals were resighted at least once (2 916 resightings, 8 524 images; Figure 4).'}, {'outcome': 'Individus resightés au moins une fois', 'value': '1882', 'unit': 'individus', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Overview of data', 'source_quote': 'of which 1 882 individuals were resighted at least once (2 916 resightings, 8 524 images; Figure 4)'}, {'outcome': 'Images annotées manuellement (CVAT)', 'value': '907', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Image processing and cropping of regions of interest', 'source_quote': 'To enable automated cropping and extraction of relevant body regions, 907 images were manually annotated using the Computer Vision Annotation Tool 24 .'}, {'outcome': 'Images annotées avec keypoints anatomiques', 'value': '505', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Image processing and cropping of regions of interest', 'source_quote': 'A subset of 505 S. melops images was further annotated with 11 anatomical keypoints and 4 keypoints marking the corners of the white balance reference card visible in most photographs.'}, {'outcome': "Images d'entraînement/validation YOLOv8", 'value': '757 / 150', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Automated detection of regions of interest and keypoints', 'source_quote': 'The dataset was randomly split into 757 training and 150 validation images.'}, {'outcome': 'Triplets créés pour le benchmark humain FishFaces', 'value': '135', 'unit': 'triplets', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Design and sampling of triplets', 'source_quote': 'A total of 135 triplets were made for the benchmark test, though the sampling code can easily be modified for a different sample size.'}, {'outcome': 'Images floues à exclure', 'value': '59', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Usage Notes', 'source_quote': 'We recommend excluding images that are flagged as "blurry" (59 images).'}, {'outcome': 'Images collectées de manière opportuniste', 'value': '7.2', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Dataset', 'source_quote': 'An additional 7.2 % of the images were collected opportunistically during related field experiments and surveys between 2019 and 2023, using fyke nets, baited traps, or hand nets.'}], 'qualitative_findings': ['Chaque labre mélops possède un motif facial complexe et contrasté ("empreinte faciale") qui semble temporellement stable et permet l\'identification visuelle.', 'Les crops centrés sur la tête donnent une meilleure précision de ré-identification que les images du corps entier.', "La performance du modèle décline avec l'augmentation de l'intervalle temporel entre les captures, probablement en raison du biais des données vers des intervalles de recapture plus courts."], 'main_findings': ['Melops est un dataset longitudinal de 24 578 images de 9 861 labres mélops individuels, collecté sur sept ans via capture-marquage-recapture.', 'Le dataset fournit des images originales et des crops automatisés (corps entier, tête, corps sans tête) ainsi que des métadonnées (longueur, sexe, état reproducteur).', 'Une étude préliminaire de ré-identification par apprentissage métrique contrastif a atteint 35% de précision rank-1 (53% avec ensemble gauche/droite).', 'Un modèle YOLOv8 a été entraîné pour détecter automatiquement le corps et la tête des poissons afin de générer les crops.', 'Un benchmark humain de ré-identification (FishFaces, 135 triplets) a été constitué et distribué à huit participants experts.']}

## Conclusions

Le dataset Melops comble une lacune critique de données pour la ré-identification des poissons en fournissant un large ensemble d'images individuelles longitudinales ouvertement disponible. Ce dataset devrait catalyser le développement de modèles de ré-identification plus précis et temporellement robustes pour les poissons. Le dataset soutient également des recherches écologiques et évolutives plus larges (dimorphisme sexuel, tactiques reproductives alternatives, développement individuel, vieillissement, variation de couleur). Le cadre méthodologique est transférable à d'autres espèces du genre Symphodus et pourrait servir de modèle pour des datasets similaires chez d'autres taxons.

## Summary of columns in the Melops metadata file. The table lists key variable names, descriptions, and data types associated with each image and individual. A complete column description, including all complementary metadata fields, is provided in the dataset's readme file.

| Column name | Description |
| --- | --- |
| filename_year | Unique image identifier (combines file name and year). |
| date | Capture date in "dd.mm.yyyy" format. |
| year | Capture year. |
| dayseq | Day sequence (running day number from 11.05.2018 = 1 to 30.08.2024 = 2305). |
| ID | Unique individual ID: PIT tag number (5-6 digits) or untagged followed by a number |
|  | (1-15) for untagged fish. |
| tagged | Indicator if the fish is PIT-tagged (0/1) |
| suspected_tagloss | Indicator if the fish shows evidence of PIT-tag loss (0/1) |
| length | Total length in millimetres. |

## Number of individuals, sightings and images for individuals in the dataset, separated on whether sex has been independently validated by stroking or is unvalidated individuals with female phenotypes. Females and sneaker males cannot be visually distinguished outside the spawning season.

| S |
| --- |
| E S |
| P R |
| I N |
| L E |
| T I C |
| R |
| A |

### Formule


$$A R T I C L E I N P R E S$$

### Formule


$$~7$$

### Formule


$$A R T I C L E I N P R E S S ARTICLE IN PRESS$$
