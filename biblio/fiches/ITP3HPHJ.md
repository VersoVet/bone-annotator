# Labeling instructions matter in biomedical image analysis

**Auteurs** : Tim Rädsch, Annika Reinke, Vivienn Weru, Minu D. Tizabi, Nicholas Schreck, A. Emre Kavur, Bünyamin Pekdemir, Tobias L. Roß, Annette Kopp‐Schneider, Lena Maier‐Hein
**Année** : 2022
**DOI** : 10.48550/arxiv.2207.09899

## Résumé

Biomedical image analysis algorithm validation depends on high-quality annotation of reference datasets, for which labeling instructions are key. Despite their importance, their optimization remains largely unexplored. Here, we present the first systematic study of labeling instructions and their impact on annotation quality in the field. Through comprehensive examination of professional practice and international competitions registered at the MICCAI Society, we uncovered a discrepancy between annotators' needs for labeling instructions and their current quality and availability. Based on an analysis of 14,040 images annotated by 156 annotators from four professional companies and 708 Amazon Mechanical Turk (MTurk) crowdworkers using instructions with different information density levels, we further found that including exemplary images significantly boosts annotation performance compared to text-only descriptions, while solely extending text descriptions does not. Finally, professional annotators constantly outperform MTurk crowdworkers. Our study raises awareness for the need of quality standards in biomedical image analysis labeling instructions.

## Méthodologie

{'study_design': "Chaque fournisseur d'annotation (5) a annoté les mêmes images successivement avec chaque instruction d'annotation, en utilisant des annotateurs séparés, dans un ordre fixe: instructions textuelles minimales, puis instructions textuelles étendues, puis instructions textuelles étendues avec images", 'intervention': "Instructions d'annotation avec différents niveaux de densité d'information (texte minimal, texte étendu, texte étendu + images)", 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': "Pause minimale de dix jours entre deux instructions d'annotation", 'setting': "Cinq fournisseurs d'annotation professionnels et crowdworkers MTurk"}

## Résultats

{'quantitative': [], 'qualitative_findings': ['Analyse systématique de la perspective et des caractéristiques de travail des annotateurs professionnels', "Analyse des pratiques courantes concernant les instructions d'étiquetage dans les principales compétitions d'imagerie biomédicale", "Investigation de l'impact d'instructions d'étiquetage avec différents niveaux de densité d'information sur la qualité des annotations", "Investigation de l'effet de différents types d'annotateurs sur les données d'imagerie biomédicale"], 'main_findings': ["Il existe un manque de sensibilisation à l'importance des instructions d'étiquetage", "Il existe un manque de recherche quantitative sur la meilleure façon de réaliser l'étiquetage"]}

## Conclusions

Cette étude est la première à examiner quantitativement et de manière critique le rôle des instructions d'annotation dans le travail d'annotation professionnel et externalisé (crowdsourcing). Il existe un écart majeur entre l'importance des instructions d'annotation et leur qualité/disponibilité actuelle. Les descriptions textuelles étendues n'améliorent pas nécessairement la performance d'annotation par rapport aux descriptions textuelles minimales, contrairement aux attentes des annotateurs professionnels. L'ajout d'images entraîne une amélioration nette de la performance chez tous les fournisseurs d'annotation, en particulier sur les images ambiguës présentant des conditions difficiles (mauvaise illumination, objets qui se chevauchent). Les annotateurs issus de sociétés professionnelles fournissent des annotations de qualité nettement supérieure à ceux de MTurk, la plateforme de crowdsourcing la plus populaire en recherche en santé, quel que soit le type d'instructions. 76% des compétitions MICCAI récentes ne rapportent pas leurs instructions d'annotation, ce qui est alarmant et appelle à un changement de paradigme dans la pratique courante. La publication des instructions d'annotation est une condition préalable pour permettre la vérification indépendante et la reproduction des annotations créées, de façon analogue à la publication du code pour les résultats algorithmiques. Les créateurs de jeux de données et organisateurs de compétitions devraient publier leurs instructions d'annotation, et le processus de création devrait être itératif pour bien modéliser la distribution sous-jacente des données. Le crowdsourcing combiné à des stratégies d'annotation assistées par ordinateur peut constituer une approche valide et rentable, la connaissance médicale n'étant souvent nécessaire que pour la création des instructions et non pour l'annotation elle-même. Les résultats, bien que centrés sur l'analyse d'images biomédicales, sont transposables à d'autres domaines de recherche et à l'annotation de données externalisées en général. Il est envisagé que l'établissement et l'adoption généralisée de standards de qualité pour les instructions d'annotation deviennent impératifs à l'avenir, étant donné la complexité et la diversité croissantes des jeux de données.

## Aggregated results of the Medical Image Computing and Computer Assisted Intervention Society (MICCAI) competition analysis. For each competition, the individual competition task submission documents were evaluated.

| Analysis results of MICCAI registered competitions |
| --- | --- | --- |
| Date of evaluation | Nov 10 2021 |  |
| Total number of competi- | 53 |  |
| tions* |  |  |
| Total number of competi- | 96 |  |
| tion tasks |  |  |
| Competition tasks which.. | absolute relative |
| do not need to publish LIs** | 20 | 20.83% |
| or have valid justification |  |  |
| Could/should publish | 76 | 79.17% |
| In scope competition tasks | absolute relative |
| (76) which ... |  |  |
| publish LIs | 18 | 23.68% |
| do not publish / have LIs | 58 | 76.32% |
| Inter-rater agreement: | 90.63% |  |
| ** LI = Labeling Instruction |  |  |
| * All information based on the Challenge design docs, mainly question 23 b/a, of the |
| MICCAI registered competitions (Link | accessed: 2021-11-10) between 2020 and 2021. |

## Overview• Terminology.…………………………………………………... 2 • Goal………………………………………………………………….. 3 • Occlusion………………………………………………………... 4 • Medical instruments………………………………………. 5 • Medical instruments -Holes…………………………. 6 • Medical instruments -Holes exception……….. 7 • Medical instruments -Transparency……………. 8 • Text overlay……………..………………………………………. 9 • Image overlay……………..………………..…………………. 10

| 1 |
| --- |
