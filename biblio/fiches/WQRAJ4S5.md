# AnNoBrainer, An Automated Annotation of Mouse Brain Images using Deep Learning.

**Auteurs** : Roman Peter, Petr Hrobar, Josef Navratil, Martin Vagenknecht, Jindrich Soukup, Keiko Tsuji, Nestor X Barrezueta, Anna C Stoll, Renee C Gentzel, Jonathan A Sugam, Jacob Marcus, Danny A Bitton
**Année** : 2024
**DOI** : 10.1007/s12021-024-09679-1

## Résumé

Annotation of multiple regions of interest across the whole mouse brain is an indispensable process for quantitative evaluation of a multitude of study endpoints in neuroscience digital pathology. Prior experience and domain expert knowledge are the key aspects for image annotation quality and consistency. At present, image annotation is often achieved manually by certified pathologists or trained technicians, limiting the total throughput of studies performed at neuroscience digital pathology labs. It may also mean that simpler and quicker methods of examining tissue samples are used by non-pathologists, especially in the early stages of research and preclinical studies. To address these limitations and to meet the growing demand for image analysis in a pharmaceutical setting, we developed AnNoBrainer, an open-source software tool that leverages deep learning, image registration, and standard cortical brain templates to automatically annotate individual brain regions on 2D pathology s

## Méthodologie

{'study_design': "Développement et validation d'un pipeline logiciel de deep learning (mask R-CNN pré-entraîné et affiné, recalage d'image, templates corticaux standards) pour l'annotation automatisée d'images de cerveau de souris, comparé à l'annotation manuelle par des pathologistes/scientifiques entraînés", 'intervention': 'Application du pipeline AnNoBrainer (détection des cerveaux et notes manuscrites via mask R-CNN affiné, appariement aux métadonnées via algorithme hongrois, recalage sur templates de couches cérébrales) à des lames de pathologie', 'control': "Annotation manuelle réalisée par des scientifiques/pathologistes entraînés (standard de référence pour l'évaluation histopathologique)", 'primary_outcomes': ["Précision de l'annotation automatisée comparée à l'évaluation histopathologique des experts", "Temps passé sur l'annotation, le contrôle qualité et l'étiquetage du cerveau"], 'secondary_outcomes': ["Reproductibilité de l'annotation", 'Capacité de détection et de segmentation des cerveaux individuels et des notes manuscrites'], 'statistical_methods': ['Distance euclidienne entre points de grille', "Algorithme hongrois (Hungarian algorithm) pour l'appariement brain-métadonnées"], 'duration': None, 'setting': 'Laboratoire de pathologie numérique en neuroscience, contexte pharmaceutique / recherche préclinique'}

## Résultats

{'quantitative': [{'outcome': "Réduction du temps d'annotation cérébrale, contrôle qualité et étiquetage", 'value': '~50%', 'unit': '% de réduction', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Discussion', 'source_quote': 'a significant reduction (~ 50%) in time spent on brain annotation, quality control and labelling compared to trained scientists in pathology'}, {'outcome': "Conformité aux standards d'évaluation histopathologique des experts", 'value': '>85%', 'unit': '% des cas', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': "AnNoBrainer offers a rapid, accurate, and reproducible automated annotation of mouse brain images that largely meets the experts' histopathological assessment standards (> 85% of cases)"}, {'outcome': 'Identification et segmentation des cerveaux et classification des notes manuscrites sur les lames de test', 'value': '100% (toutes les lames)', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Introduction', 'source_quote': 'The fine-tuned mask R-CNN model was then applied to 20 new slides, where it perfectly identified and segmented all individual brains on each of the slides as well as correctly classified all hand-written note objects.'}], 'qualitative_findings': ["AnNoBrainer a été appliqué avec succès dans de multiples études précliniques de neuroscience à haut débit dans l'industrie, avec de bonnes performances sur des lames de qualité variable (cerveaux légèrement déchirés, asymétriques, etc.), différentes colorations (H&E, Nissl, IHC), bruit de fond et divers templates"], 'main_findings': ["AnNoBrainer atteint une précision comparable à l'annotation manuelle experte", "AnNoBrainer augmente la reproductibilité de l'annotation", "AnNoBrainer réduit le temps d'annotation d'environ 50% par rapport aux scientifiques entraînés", 'Le modèle mask R-CNN affiné distingue efficacement les cerveaux des notes manuscrites, même en présence de tissus manquants, tournés ou déchirés']}

## Conclusions

AnNoBrainer est un pipeline modulaire et extensible d'annotation automatisée du cerveau de souris basé sur le deep learning, capable d'identifier et distinguer le cerveau du bruit, de le relier à ses métadonnées expérimentales, et de le recaler avec son template de couche cérébrale correspondant Le pipeline permet le réentraînement des modèles et l'intégration de nouvelles améliorations par la communauté à mesure que davantage de données étiquetées deviennent disponibles ou que d'autres techniques de coloration sont utilisées

## Table 1

| Deep learning models used in this study | Model Type | Function | Input | Output |
| --- | --- | --- | --- | --- |
|  | Mask R-CNN | Detects individual brains and | Digital Slide image | Coordinates of |
|  |  | handwritten notes present |  | individual brains |
|  |  | on the slide |  | present on the slide |
|  | EfficientNet-B0 | Matches brain to the most | Individual brain image | Predicted Z-axis from |
|  |  | similar Allen brain atlas |  | the Allen brain atlas |
|  |  | reference layer |  |  |

## Model performances for brain atlas layers matching

| Method | Exact accuracy ± 1 accuracy ± 2 accuracy |
| --- | --- | --- | --- |
| Random | 7% | 18% | 28% |
| Resnet 34 (default) 40% | 73% | 88% |
| Resnet 34 (tunned) 50% | 80% | 91% |
| EfficientNet-B0 | 59% | 86% | 94% |

### Formule


$$d 2 (p, q) = N ∑ n=1 D ∑ d=1 p n,i -q n,i 2$$
