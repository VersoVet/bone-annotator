# GTCreator: a flexible annotation tool for image-based datasets.

**Auteurs** : Jorge Bernal, Aymeric Histace, Marc Masana, Quentin Angermann, Cristina Sánchez-Montes, Cristina Rodríguez de Miguel, Maroua Hammami, Ana García-Rodríguez, Henry Córdova, Olivier Romain, Gloria Fernández-Esparrach, Xavier Dray, F Javier Sánchez
**Année** : 2019
**DOI** : 10.1007/s11548-018-1864-x

## Résumé

Methodology evaluation for decision support systems for health is a time-consuming task. To assess performance of polyp detection methods in colonoscopy videos, clinicians have to deal with the annotation of thousands of images. Current existing tools could be improved in terms of flexibility and ease of use.

## Méthodologie

{'study_design': "Comparaison qualitative et quantitative de six outils d'annotation d'images (LabelMe, VIA, RatSnake, VIAT, ImageJ et GTCreator) appliqués à l'annotation de séquences vidéo et d'images fixes HD de coloscopie", 'intervention': "Annotation des mêmes sous-ensembles d'images (séquences vidéo et images HD) à l'aide de chacun des six outils d'annotation", 'control': 'Annotation de référence (ground truth) fournie par un expert externe', 'primary_outcomes': ["Temps total d'annotation moyen par outil", "Précision de l'annotation (score DICE et indice de Jaccard) par outil"], 'secondary_outcomes': ["Temps d'interaction moyen par image", "Temps d'annotation moyen par sous-ensemble d'images (séquences vidéo vs images HD)", 'Score DICE moyen par sous-ensemble de séquence vidéo'], 'statistical_methods': ["Calcul de moyennes et écarts-types du temps d'annotation", 'Métrique DICE', 'Indice de Jaccard'], 'duration': None, 'setting': "Contexte de recherche en systèmes d'aide à la décision pour la coloscopie"}

## Résultats

{'quantitative': [], 'qualitative_findings': ["RatSnake permet la création d'une ontologie sémantique pour les annotations", "VIAT fournit directement en sortie des descripteurs MPEG-7 pour l'image cible", 'LabelMe intègre des capacités de segmentation semi-automatique', "ImageJ inclut une suite complète de traitement d'image", "L'utilisation de certaines capacités de traitement d'image de ces outils nécessite une formation utilisateur importante, ce qui peut empêcher les utilisateurs moins expérimentés d'en tirer profit", "GTCreator intègre des capacités basiques de traitement d'image telles que l'ajustement de contours dessinés à main levée aux contours réels de l'image via une segmentation par watershed avec marqueurs", "GTCreator permet également de modifier localement le contraste de l'image"], 'main_findings': ["Certains outils d'annotation offrent des fonctionnalités additionnelles à valeur ajoutée (ontologie sémantique dans RatSnake, descripteurs MPEG-7 dans VIAT)", "Il existe une variabilité importante des capacités de traitement d'image entre les outils (de la segmentation semi-automatique de LabelMe à la suite complète d'ImageJ)", "La complexité de certaines capacités de traitement d'image constitue une barrière pour les utilisateurs moins expérimentés", "GTCreator propose un compromis avec des capacités de traitement d'image basiques (ajustement de contours par watershed avec marqueurs, ajustement local du contraste) sans la complexité des suites complètes"]}

## Conclusions

Un outil d'annotation a été proposé pour faciliter l'annotation par les cliniciens tout en conservant les fonctionnalités d'autres outils existants La flexibilité, la gestion efficace des données et les capacités de navigation permettent à l'outil d'être utilisé lors des principales étapes d'évaluation de méthodes pour tout domaine d'image Une étude comparative a été réalisée et conclut que GTCreator est l'outil offrant le meilleur compromis entre temps d'annotation et précision La navigation facile dans les images et l'inclusion de capacités d'édition d'images jouent un rôle clé dans la génération d'annotations rapides et précises

## Comparison of mean and standard deviation of the annotation precision with respect to the annotation tool.

| Feature | RatSnake | LabelMe | VIA | VIAT | ImageJ | GTCreator |
| --- | --- | --- | --- | --- | --- | --- |
| Annotation types | Image masks | Image masks, semantic labels | Image masks, formatted text | Image masks, unformatted text | Image masks | Image mask, formatted text |
| Mask anno-tation | Polygon | Polygon | Polygon, pre-determined shapes | Polygon, pre-determined shapes, free-hand | Polygon, pre-determined shapes, free-hand | Polygon, pre-determined shapes, free-hand |
| Mask edit-ing | Annotation transfer | None | Annotation transfer | None | Annotation transfer | Annotation transfer, pixel-wise editing |
| Dataset browsing | Single image | Collection | Collection | Single image | Single image | Collection |
| Input | BMP, JPEG, | BMP, JPEG, | BMP, JPEG, | BMP, JPEG, | BMP, JPEG, | BMP, JPEG, |
| format | PNG, TIFF | PNG | PNG, TIFF | PNG | PNG, TIFF | PNG, TIFF |
| Output for-mat | Binary masks | XML file | CSV file | XML file | Text file | Binary masks, CSV file |
|  |  |  |  |  |  | Filtering- |
| Extra fea-tures | Semantic on-tology | Semi-automatic segmentation | None | MPEG-7 descriptors | Image process-ing suite | based brows-ing, annota-tion merging |
|  |  |  |  |  |  | and reviewing |

## Mean and standard deviation of the annotation precision with respect to the annotation tool. VidFr stands for video sequence frames, HDFr for still HD images.

|  | RatSnake | LabelMe | VIA | VIAT | ImageJ | GTCreator |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | DICE score (mean ± standard deviation) |  |  |
| All | 0.886 ± 0.040 | 0.860 ± 0.080 | 0.876 ± 0.059 | 0.848 ± 0.068 | 0.852 ± 0.082 | 0.908±0.032 |
| VidFr | 0.870 ± 0.058 | 0.851 ± 0.103 | 0.862 ± 0.076 | 0.824 ± 0.089 | 0.832 ± 0.099 | 0.899±0.037 |
| HDFr | 0.935 ± 0.026 | 0.917 ± 0.022 | 0.924 ± 0.015 | 0.927 ± 0.038 | 0.920 ± 0.031 | 0.937±0.029 |
|  |  | Jaccard Index (mean ± standard deviation) |  |  |
| All | 0.938 ± 0.025 | 0.925 ± 0.051 | 0.932 ± 0.035 | 0.915 ± 0.042 | 0.917 ± 0.052 | 0.951±0.017 |
| VidFr | 0.929 ± 0.035 | 0.916 ± 0.064 | 0.924 ± 0.046 | 0.901 ± 0.056 | 0.905 ± 0.063 | 0.946±0.002 |
| HDFr | 0.965 ± 0.009 | 0.956 ± 0.013 | 0.960 ± 0.008 | 0.960 ± 0.024 | 0.958 ± 0.017 | 0.967±0.010 |
|  | Set 1 | Set 2 | Set 3 | Set 4 | Set 5 | Set 6 |
|  |  | DICE score (mean ± standard deviation) |  |  |
| All | 0.921 ± 0.011 | 0.928 ± 0.012 | 0.871 ± 0.027 | 0.887 ± 0.026 | 0.869 ± 0.014 | 0.761±0.058 |
| VidFr | 0.915 ± 0.014 | 0.936 ± 0.008 | 0.812 ± 0.032 | 0.869 ± 0.033 | 0.847 ± 0.019 | 0.720±0.071 |
| HDFr | 0.939 ± 0.014 | 0.900 ± 0.023 | 0.937 ± 0.007 | 0.942 ± 0.011 | 0.940 ± 0.007 | 0.907 ± 0.026 |
|  |  | Jaccard Index (mean ± standard deviation) |  |  |
| All | 0.959 ± 0.006 | 0.962 ± 0.007 | 0.934 ± 0.014 | 0.939 ± 0.015 | 0.929 ± 0.008 | 0.861±0.038 |
| VidFr | 0.955 ± 0.007 | 0.967 ± 0.005 | 0.919 ± 0.019 | 0.929 ± 0.018 | 0.917 ± 0.011 | 0.839±0.004 |
| HDFr | 0.969 ± 0.006 | 0.945 ± 0.015 | 0.967 ± 0.004 | 0.970 ± 0.006 | 0.969 ± 0.004 | 0.948 ± 0.013 |
