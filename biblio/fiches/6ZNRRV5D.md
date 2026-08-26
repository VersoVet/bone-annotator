# Skeleton Ground Truth Extraction: Methodology, Annotation Tool and Benchmarks

**Auteurs** : Cong Yang, Bipin Indurkhya, John See, Bo Gao, Yan Ke, Zeyd Boukhers, Zhenyu Yang, Marcin Grzegorzek
**Année** : 2023
**DOI** : 10.1016/j.dib.2026.1126422352-3409/

## Résumé

Skeleton Ground Truth (GT) is critical to the success of supervised skeleton extraction methods, especially with the popularity of deep learning techniques. Furthermore, we see skeleton GTs used not only for training skeleton detectors with Convolutional Neural Networks (CNN) but also for evaluating skeleton-related pruning and matching algorithms. However, most existing shape and image datasets suffer from the lack of skeleton GT and inconsistency of GT standards. As a result, it is difficult to evaluate and reproduce CNN-based skeleton detectors and algorithms on a fair basis. In this paper, we present a heuristic strategy for object skeleton GT extraction in binary shapes and natural images. Our strategy is built on an extended theory of diagnosticity hypothesis, which enables encoding human-in-the-loop GT extraction based on clues from the target's context, simplicity, and completeness. Using this strategy, we developed a tool, SkeView, to generate skeleton GT of 17 existing shape

## Méthodologie

{'study_design': "Création d'un jeu de données descriptif (data descriptor) via acquisition d'images RGB multi-vues (Structure-from-Motion et stéréo multi-vues) sur des plants de tomate en serre, suivie d'annotations sémantiques/instance manuelles, de génération de graphes topologiques et d'extraction de traits phénotypiques", 'intervention': None, 'control': None, 'primary_outcomes': ['Segmentation sémantique et par instance au niveau des organes', 'Représentations graphiques encodant la topologie et la géométrie des plantes', "Extraction de traits phénotypiques (longueur des entre-nœuds, angles d'insertion, angles phyllotactiques)"], 'secondary_outcomes': ['Validation géométrique interne via points de contrôle indépendants (ICP)'], 'statistical_methods': ["Calcul de l'erreur moyenne (biais)", 'Mean Absolute Error (MAE)', 'Root Mean Square Error (RMSE)'], 'duration': 'Acquisitions multiples au cours du développement végétatif précoce à mi-végétatif (42 scans)', 'setting': "Plants de tomate cultivés en serre, imagés dans une boîte lumineuse LED de 47 × 39 × 78, avec système d'acquisition composé d'un appareil photo Sony A6000 monté sur un rig fixe et d'un plateau tournant motorisé à 360°"}

## Résultats

{'quantitative': [{'outcome': 'Root Mean Square Error (RMSE) de la distance entre points de contrôle (paires B-D, B-E, D-E)', 'value': '0.301', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Experimental Design, Materials and Methods', 'source_quote': 'sub-millimeter RMSE and MAE values across all pairs (0.301 mm and 0.151 mm, respectively) indicate highly stable metric scaling and negligible spatial distortion.'}, {'outcome': 'Mean Absolute Error (MAE) de la distance entre points de contrôle (paires B-D, B-E, D-E)', 'value': '0.151', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Experimental Design, Materials and Methods', 'source_quote': 'sub-millimeter RMSE and MAE values across all pairs (0.301 mm and 0.151 mm, respectively) indicate highly stable metric scaling and negligible spatial distortion.'}, {'outcome': 'Nombre de scans dans le dataset', 'value': '42', 'unit': 'scans', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The dataset contains 42 scans from three greenhousegrown tomato plants acquired across early to mid-vegetative development using a rotational multi-view imaging system.'}, {'outcome': "Nombre d'images RGB par scan", 'value': '60-70', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Each scan consists of 60-70 overlapping RGB images captured under uniform illumination and reconstructed into a metrically scaled dense colored point cloud using Structure-from-Motion and multi-view stereo.'}, {'outcome': "Nombre d'images RGB par scan (précisé)", 'value': '67', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Data Description', 'source_quote': 'The RGB_IMAGES folder contains 67 overlapping multiview photos per scan, serving as the raw input for 3D reconstruction.'}, {'outcome': 'Limite de points traitables par Cloud-Graph', 'value': '5', 'unit': 'millions de points', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Limitations', 'source_quote': 'the current implementation of the Cloud-Graph software has been validated on dense point clouds of up to approximately 5 million points using standard workstation hardware.'}], 'qualitative_findings': ["La distribution des erreurs ICP est centrée près de zéro, confirmant que les déviations résiduelles représentent un bruit de reconstruction aléatoire plutôt qu'un biais d'échelle systématique", "L'analyse temporelle des erreurs ICP montre que la précision métrique est restée parfaitement stable dans le temps, sans dégradation malgré la complexité croissante de la canopée"], 'main_findings': ['TomatoPGT fournit un jeu de données 3D intégré combinant images RGB multi-vues, nuages de points colorés denses, annotations sémantiques/instance au niveau des organes, représentations graphiques de la topologie des plantes, et traits phénotypiques tabulés dérivés de manière déterministe des graphes', 'La validation géométrique interne via points de contrôle indépendants (ICP) confirme une stabilité métrique sub-millimétrique à travers tous les scans', "Deux outils logiciels personnalisés (Cloud-Seg pour l'annotation interactive et Cloud-Graph pour la génération algorithmique de graphes) accompagnent le dataset"]}

## Conclusions

TomatoPGT constitue une base de référence rigoureusement validée pour accélérer la recherche agricole computationnelle, soutenant explicitement les avancées en segmentation 3D, phénotypage non destructif automatisé et développement de jumeaux numériques Le dataset est explicitement présenté comme une 'vérité terrain géométrique' de haute fidélité plutôt qu'une 'vérité terrain biologique' absolue, car aucune mesure manuelle destructive n'a été réalisée pour validation croisée

## 2026 The Author(s). Published by Elsevier Inc. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ )

| Specifications Table |  |
| --- | --- |
| Subject | Biology |
| Specific subject area | 3D tomato plant phenotyping using point-cloud segmentation, graph-based structural |
|  | representation, and graph-derived trait extraction. |
| Type of data | -Raw images: JPEG (multi-view)-Dense point clouds: PLY (XYZ, RGB; normals) |
|  | -Annotated point clouds: TXT (XYZ, RGB, class_id, instance_id, annotation RGB) |
|  | -Graph representations: JSON (nodes, edges, geometry, metadata) |
|  | -Phenotypic traits: CSV (graph-derived measurements) |

## • The dataset supports research in semantic segmentation, graph learning, phenotypic trait extraction, and digital plant modelling.

| Dataset | Crop(s) | Annotations (publicly available) | Notes / Reference |
| --- | --- | --- | --- |
| ROSE-X | Rose | Semantic organ labels | X-ray CT + point cloud; |
|  |  |  | organ-level annotations [ 5 ]. |
| Soybean-MVS | Soybean | Semantic | 102 plants across growth |
|  |  |  | stages; MVS reconstruction [ 6 ]. |
| PLANesT-3D | Pepper, Rose, Ribes | Semantic + Instance | 34 real plants; |
|  |  |  | leaf/stem + leaflet instances |
|  |  |  | [ 7 ]. |
| Pheno4D | Maize, Tomato | Semantic + Instance + Time- | Registered temporal point |
|  |  | series | clouds [ 8 ]. |
| LAST-Straw | Strawberry | Semantic + Instance + Time- | 84 scans of 6 plants; rich trait |
|  |  | series + Skeletons | benchmarks [ 9 ]. |
| TomatoWUR | Tomato | Semantic + Instance + Con- | 44 plants; |
|  |  | nected skeletons + Manual | shape-from-silhouette dataset |
|  |  | traits | [ 10 ]. |
| Crops3D | Maize, Cabbage, | Semantic ± Instance | 1230 colored 3D point clouds; |
|  | Potato, Cotton, |  | multi-sensor collection [ 11 ]. |
|  | Rapeseed, Rice, |  |  |
|  | Tomato, Wheat |  |  |
| MaizeField3D | Maize | Semantic + Instance | 520 annotated field-grown |
|  |  |  | plants; TLS and NURBS models |
|  |  |  | [ 12 ]. |
| TomatoPGT | Tomato | Semantic + Instance + Seman- | 42 Scans; Camera rotational |
| (this work) |  | tic Graph representations + | imaging system [ 2 ] |
|  |  | Phenotypic Trait extraction + | ; includes Cloud Graph and |
|  |  | Software tools | Cloud-Seg software[ 3 ]. |

## Simplified annotation schema and ontology for TomatoPGT.

| Semantic Class | Biological Description | Common Annotation Errors |
| --- | --- | --- |
| Root-Node | Origin / basal attachment of the plant | Missing root assignment |
| Junction-Nodes | fork on the main stem | Conflation with stalk attachment |
| mainStem-Seg | Stem segments / internodes | Broken stem chains; duplicate instance IDs |
| Compound Leaf-Node | Aggregated leaflets and rachis | Inconsistent leaflet grouping |
| Stalk-Seg | Petiole (connecting Junction to Leaf) | Overlapping leaf/stem boundaries |
| Sucker-Seg | Sucker / Branch / Lateral vegetative shoots | Misclassification as primary stems |

## Graph table preview.

| plant_id | graph_nodes | graph_edges | #junctions | #compound_leaves /Ct | #suckers |
| --- | --- | --- | --- | --- | --- |
| BBH_05132025 | 6 | 5 | 1 | 2 | 0 |
| BBH_05152025 | 6 | 5 | 1 | 2 | 0 |
| BBH_05202025 | 7 | 6 | 1 | 2 | 0 |
| BBH_05122025 | 7 | 6 | 1 | 2 | 0 |

## Independent geometric validation.

| Validation pair (ICP) | Theory (mm) | Mean error (mm) | RMSE (mm) | MAE (mm) |
| --- | --- | --- | --- | --- |
| B-D (Step Check) | 32 | 0.0437 | 0.2030 | 0.0988 |
| B-E (Diagonal Check) | 45.2548 | -0.0058 | 0.1991 | 0.1262 |
| D-E (Step Check) | 32 | 0.0160 | 0.3009 | 0.1505 |

### Formule


$$∈ i = D e,i -D t$$

### Formule


$$• Mean error • Standard deviation of • Root Mean Square Error (RMSE) RMSE = 1 N N i =1 D e,i -D t 2$$

### Formule


$$L geo = n -1 k =1 C k -C k +1 .$$

### Formule


$$υ stem •υ lea f υ stem υ lea f$$
