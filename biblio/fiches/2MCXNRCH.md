# CATS: Cloud-native time-series data annotation tool for intensive care



## Resume


CATS: Cloud-native time-series data annotation tool for intensive care

Intensive care units are complex, data-rich healthcare environments which provide substantial opportunities for applications in machine learning. While certain solutions can be derived directly from data, complex problems require additional human input provided in the form of data annotations. Due to the large size and complexities associated with healthcare data, the existing software packages for time-series data annotation are infeasible for effective use in the clinical setting and frequently require significant time commitments and technical expertise.Our software provides a comprehensive, end-to-end solution to the time-series data annotation and proposes a novel approach for a semi-automated annotation in the cloud. It allows for conducting large-scale, asynchronous data annotation activities across multiple, geographically distributed users. The adoption of our software could benefit the wider research community by enhancing existing datasets, creating novel avenues for researc

Capturing Requirements for a Data Annotation Tool for Intensive Care: Experimental User-Centered Design Study

Intensive care units (ICUs) are complex and data-rich environments. Data routinely collected in the ICUs provides tremendous opportunities for machine learning, but their use comes with significant challenges. Complex problems may require additional input from humans which can be provided through a process of data annotation. Annotation is a complex, time-consuming process that requires domain expertise and technical proficiency. Existing data annotation tools fail to provide an effective solution to this problem. In this study, we investigated clinicians' approach to the annotation task. We focused on establishing the characteristics of the annotation process in the context of clinical data and identifying differences in the annotation workflow between different staff roles. The overall goal was to elicit requirements for a software tool that could facilitate an effective and time-efficient data annotation. We conducted an experiment involving clinicians from the ICUs annotating print

Annotating Medical Image Data

Speeding up scientific imaging workflows: Design of automated image annotation tool

An interactive tool for manual, semi-automatic and automatic video annotation

Computer Vision Annotation Tool

SLAM – A thin-client for interoperable annotation and biomedical signal handling

Designing artificial intelligence tools dedicated to biosignal data (e.g. electroencephalography, EEG) analysis is an increasingly considered topic, motivated by clinical needs. In this context, data annotation is a crucial task, as a prerequisite to supervised machine learning / deep learning approaches. However, annotation is a tedious, time consuming and error-prone task, that has generally to be carried out in a limited time by clinicians. Based on these considerations, we propose a software tool dedicated to a clinical use, that aims to tackle the main difficulties encountered by clinicians. It is designed as a thin-client, that can be run on a web interface without requiring complex technical dependencies. It allows user-friendly, interactive visualization and annotation, while minimizing the manual interactions. It relies on an extensible data exchange format specifically tailored for storing biosignal data, associated metadata and annotations. A semantic web paradigm is conside

DL-AAT: An Automatic Annotation Tool for Efficient Data Labeling in Vision-Based Systems

Efficient annotation of image data sets for computer vision applications

AI-Enhanced Annotation Tool for Aneurysm Medical Image Labeling

An annotation tool for dermoscopic image segmentation

Use of deep learning to automate the annotation of USG lung image data

PyTAGIT: a scalable and interactive human-in-the-loop tool for fast image annotation


## Synthese


L’annotation de données de haute qualité constitue un facteur déterminant pour les applications d’apprentissage supervisé en médecine, alors que le temps des experts cliniques demeure fortement contraint. Pour répondre à cette tension, les auteurs proposent un cadre en deux étapes, confiant à un expert l’annotation ciblée de quelques images puis à un non-expert le complément des frames adjacentes avec assistance par intelligence artificielle. Ce processus est opérationnalisé dans le logiciel open source Fast Colonoscopy Annotation Tool (FastCat), conçu pour l’annotation de vidéos endoscopiques et extensible à d’autres domaines médicaux. Sur le plan méthodologique, les scènes pertinentes sont sélectionnées par extraction d’images, les annotations expertes initialisent un modèle d’IA qui propose des détections sur les frames voisines, et le non-expert corrige ces suggestions avant export pour l’entraînement. Selon les données associées, cette combinaison accélère sensiblement l’annotation tout en maintenant une précision comparable, les gains liés à l’IA saturant autour d’un F1-score d’environ 0,8.

L’annotation de données de haute qualité constitue un facteur déterminant pour les applications d’apprentissage supervisé en médecine, alors que le temps des experts cliniques demeure fortement contraint. Pour répondre à cette tension, les auteurs proposent un cadre en deux étapes, confiant à un expert l’annotation ciblée de quelques images puis à un non-expert le complément des frames adjacentes avec assistance par intelligence artificielle. Ce processus est opérationnalisé dans le logiciel open source Fast Colonoscopy Annotation Tool (FastCat), conçu pour l’annotation de vidéos endoscopiques et extensible à d’autres domaines médicaux. Sur le plan méthodologique, les scènes pertinentes sont sélectionnées par extraction d’images, les annotations expertes initialisent un modèle d’IA qui propose des détections sur les frames voisines, et le non-expert corrige ces suggestions avant export pour l’entraînement. Selon les données associées, cette combinaison accélère sensiblement l’annotation tout en maintenant une précision comparable, les gains liés à l’IA saturant autour d’un F1-score d’environ 0,8. Les résultats indiquent que la combinaison d’un algorithme de détection de freeze-frames, d’annotations expertes ciblées et de suggestions de boîtes englobantes par IA augmente significativement la vitesse d’annotation tout en maintenant, voire en améliorant, la précision (Tables 2 et 3). Cet avantage ne s’explique pas par une différence d’expérience entre outils, les annotateurs les ayant utilisés en alternance sur des vidéos ordonnées aléatoirement, avec des courbes d’apprentissage similaires mais décalées vers des temps plus courts pour l’outil proposé (Figure 1). La vitesse d’annotation s’améliore avec la performance de l’IA jusqu’à un F1-score d’environ 0,8, au-delà duquel les gains saturent, ce qui suggère qu’une IA suffisamment performante suffit. Enfin, l’expérience médicale n’apparaît pas associée à la vitesse ni à la performance d’annotation (Table 3), et l’outil plus que double la vitesse d’annotation tout en préservant une précision comparable aux outils état de l’art et un coût d’annotation experte limité. Les auteurs présentent un outil d’annotation semi-automatisée pour la gastro-entérologie, fondé sur un flux de travail combinant étapes algorithmiques et manuelles, conçu pour réduire significativement la charge des annotateurs experts et accélérer le processus par rapport aux outils existants. Le cadre proposé répartit l’annotation entre un expert, qui valide quelques images clés, et un non-expert assisté par l’IA pour annoter les trames adjacentes, ce qui permet de diminuer d’un facteur 20 le volume de travail expert sur leurs données tout en préservant une qualité d’annotation très élevée. Les auteurs rapportent une vitesse d’annotation plus que doublée, une précision comparable aux outils de l’état de l’art, et une saturation des gains liés à l’IA autour d’un F1-score d’environ 0,8. Ils publient en outre un logiciel open source comprenant deux interfaces (expert et non-expert) et indiquent que ces résultats soutiennent une amélioration marquée de l’annotation d’images et de vidéos endoscopiques, tout en soulignant les limites de l’étude et des pistes d’extension.

L’intelligence artificielle, et en particulier l’apprentissage automatique, repose fortement sur la quantité et la qualité des données pour produire des modèles efficaces, ce qui en fait un levier d’innovation croissant en santé. Les unités de soins intensifs (USI), environnements complexes et riches en données issues de dispositifs médicaux et de systèmes d’information clinique, offrent un terrain favorable au déploiement de modèles d’apprentissage automatique. Toutefois, certaines tâches complexes nécessitent des annotations humaines pour fournir un contexte clinique que les données brutes seules ne permettent pas d’inférer, alors même que le volume et la complexité des données d’USI rendent cette annotation particulièrement laborieuse. Des biais liés aux annotateurs, à la temporalité ou à la sélection des données peuvent en outre compromettre la qualité des labels. Pour capturer les exigences d’un outil d’annotation adapté, une étude expérimentale a été menée auprès de personnels cliniques d’USI, consistant à annoter manuellement des extraits de séries temporelles imprimés sur papier, les observations servant de base à l’analyse des besoins logiciels. Cette étude expérimentale a exploré les pratiques d’annotation de données par des professionnels de soins intensifs afin d’établir les exigences d’un outil numérique destiné à l’annotation de grands jeux de données en réanimation. Les membres du personnel clinique de l’USI ont annoté manuellement des extraits de séries temporelles imprimés sur papier ; les observations réalisées pendant la tâche ont servi de base à l’analyse et à la dérivation des exigences logicielles. Les résultats indiquent que le processus d’annotation des séries temporelles suit une boucle cyclique annotation–évaluation comprenant l’investigation des données, la création de labels, la réévaluation des données une fois les labels appliqués, puis le raffinement de ces labels. À partir de cette analyse, onze exigences clés ont été formulées : cinq relatives à l’annotation des admissions individuelles de patients, trois adaptées à une fonctionnalité d’annotation semi-automatisée, deux exigences opérationnelles centrées sur l’efficacité du flux de travail, et une exigence portant sur l’usage futur des labels dans un contexte d’apprentissage automatique. Cette étude expérimentale centrée sur l’utilisateur a examiné la manière dont le personnel clinique des unités de soins intensifs (USI) aborde l’annotation manuelle d’extraits de séries temporelles imprimés sur papier, les observations recueillies servant de base à l’analyse et à la formulation d’exigences logicielles. Les auteurs concluent que l’annotation des données constitue un processus cyclique exigeant flexibilité dans l’exploration et le marquage, continuité du flux de travail entre admissions, ainsi qu’une transition fluide entre analyse, annotation et raffinement des labels. Au total, onze exigences clés ont été établies pour un outil d’annotation numérique déployable en milieu de soins, dont cinq relatives à l’annotation d’admissions individuelles, trois à l’annotation semi-automatisée, deux à l’efficacité opérationnelle du workflow et une à l’usage futur des labels en apprentissage automatique. Les auteurs soulignent que les adaptations semi-automatisées doivent offrir une interface réactive, adaptée au volume de données et permettant une analyse à l’échelle individuelle comme à celle de l’ensemble du jeu de données, afin de mieux valoriser les données massives des USI et l’essor des méthodes computationnelles en santé.


## Methodologie


L’annotation de données de haute qualité constitue un facteur déterminant pour les applications d’apprentissage supervisé en médecine, alors que le temps des experts cliniques demeure fortement contraint. Pour répondre à cette tension, les auteurs proposent un cadre en deux étapes, confiant à un expert l’annotation ciblée de quelques images puis à un non-expert le complément des frames adjacentes avec assistance par intelligence artificielle. Ce processus est opérationnalisé dans le logiciel open source Fast Colonoscopy Annotation Tool (FastCat), conçu pour l’annotation de vidéos endoscopiques et extensible à d’autres domaines médicaux. Sur le plan méthodologique, les scènes pertinentes sont sélectionnées par extraction d’images, les annotations expertes initialisent un modèle d’IA qui propose des détections sur les frames voisines, et le non-expert corrige ces suggestions avant export pour l’entraînement. Selon les données associées, cette combinaison accélère sensiblement l’annotation tout en maintenant une précision comparable, les gains liés à l’IA saturant autour d’un F1-score d’environ 0,8.


## Resultats


Cette étude expérimentale a exploré les pratiques d’annotation de données par des professionnels de soins intensifs afin d’établir les exigences d’un outil numérique destiné à l’annotation de grands jeux de données en réanimation. Les membres du personnel clinique de l’USI ont annoté manuellement des extraits de séries temporelles imprimés sur papier ; les observations réalisées pendant la tâche ont servi de base à l’analyse et à la dérivation des exigences logicielles. Les résultats indiquent que le processus d’annotation des séries temporelles suit une boucle cyclique annotation–évaluation comprenant l’investigation des données, la création de labels, la réévaluation des données une fois les labels appliqués, puis le raffinement de ces labels. À partir de cette analyse, onze exigences clés ont été formulées : cinq relatives à l’annotation des admissions individuelles de patients, trois adaptées à une fonctionnalité d’annotation semi-automatisée, deux exigences opérationnelles centrées sur l’efficacité du flux de travail, et une exigence portant sur l’usage futur des labels dans un contexte d’apprentissage automatique.


## Discussion


Cette étude expérimentale centrée sur l’utilisateur a examiné la manière dont le personnel clinique des unités de soins intensifs (USI) aborde l’annotation manuelle d’extraits de séries temporelles imprimés sur papier, les observations recueillies servant de base à l’analyse et à la formulation d’exigences logicielles. Les auteurs concluent que l’annotation des données constitue un processus cyclique exigeant flexibilité dans l’exploration et le marquage, continuité du flux de travail entre admissions, ainsi qu’une transition fluide entre analyse, annotation et raffinement des labels. Au total, onze exigences clés ont été établies pour un outil d’annotation numérique déployable en milieu de soins, dont cinq relatives à l’annotation d’admissions individuelles, trois à l’annotation semi-automatisée, deux à l’efficacité opérationnelle du workflow et une à l’usage futur des labels en apprentissage automatique. Les auteurs soulignent que les adaptations semi-automatisées doivent offrir une interface réactive, adaptée au volume de données et permettant une analyse à l’échelle individuelle comme à celle de l’ensemble du jeu de données, afin de mieux valoriser les données massives des USI et l’essor des méthodes computationnelles en santé.


## Conclusion


In this study, we investigated how clinical staff from ICUs approach the task of data annotation and established 11 key requirements for a digital data annotation tool that could be deployed within the health care setting. Our findings revealed that data annotation is a cyclic process that demands flexibility in how annotators investigate and annotate the data. Preservation of the workflow continuity across different admissions and fluid transition between analysis, annotation, and refinement of the label are essential to facilitating effective data annotation in the clinical domain. Adaptations for the semiautomated annotation need to consider these factors by providing a responsive interface that dynamically adapts to the volume of data and allows for analysis on both an individual and a dataset-wide basis. The significance of these findings is evident in their potential to guide the development of a data annotation tool that capitalizes on the considerable data generated in the ICUs and the expanding use of computational methods in health care.


## Quote


In this study, we investigated how clinical staff from ICUs approach the task of data annotation and established 11 key requirements for a digital data annotation tool that could be deployed within the health care setting.

To understand how clinicians approach and reason about the data annotation process, we conducted an experimental study that involved members of the clinical staff from the ICU manually annotating excerpts of time-series data printed on paper. Observations taken during task completion served as a basis for analysis and were used to derive the requirements for the data annotation software.

The software includes annotation tools developed in Qt C++ and a cloud-based data management framework developed in python using Flask.

To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking.

To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking.


## Insight


methodology: Pour dériver les exigences d’un outil d’annotation de données en soins intensifs, une étude expérimentale a été menée auprès de personnels cliniques d’USI, qui annotaient manuellement des extraits de séries temporelles imprimés sur papier ; les observations recueillies pendant la tâche ont servi de base à l’analyse.


## Raw_Conclusion


Efficiently annotating LiDAR point clouds at scale is crucial for the development of LiDAR-based detection and autonomous driving. However, annotating LiDAR point clouds is difficult due to the challenges of low resolution, complex annotating operations, and sequential correlation. To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking. Based on our own experiments we estimate that LATTE achieves a 6.2x speedup compared with baseline annotation tools and delivers better label quality with 23.6% and 2.2% higher instance-level precision and recall, and 2.0% higher bounding box IoU.

Efficiently annotating LiDAR point clouds at scale is crucial for the development of LiDAR-based detection and autonomous driving. However, annotating LiDAR point clouds is difficult due to the challenges of low resolution, complex annotating operations, and sequential correlation. To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking. Based on our own experiments we estimate that LATTE achieves a 6.2x speedup compared with baseline annotation tools and delivers better label quality with 23.6% and 2.2% higher instance-level precision and recall, and 2.0% higher bounding box IoU.


## Raw_Procedure


FEVA: Fast Event Video Annotation Tool

FEVA: Fast Event Video Annotation Tool