# Annotation quality vs. quantity for deep-learned medical image segmentation



## Resume


Annotation quality vs. quantity for deep-learned medical image segmentation

Modeling annotator preference and stochastic annotation error for medical image segmentation

How to select slices for annotation to train best-performing deep learning segmentation models for cross-sectional medical images?

Automated segmentation of medical images heavily relies on the availability of precise manual annotations. However, generating these annotations is often time-consuming, expensive, and sometimes requires specialized expertise (especially for cross-sectional medical images). Therefore, it is essential to optimize the use of annotation resources to ensure efficiency and effectiveness. In this paper, we systematically address the question: "in a non-interactive annotation pipeline, how should slices from cross-sectional medical images be selected for annotation to maximize the performance of the resulting deep learning segmentation models?" We conducted experiments on 4 medical imaging segmentation tasks with varying annotation budgets, numbers of annotated cases, numbers of annotated slices per volume, slice selection techniques, and mask interpolations. We found that:   1) It is almost always preferable to annotate fewer slices per volume and more volumes given an annotation budget. 2)

Efficient Deep-Learning-Assisted Annotation for Medical Image Segmentation

Image segmentation is a fundamental problem in medical image analysis.
Deep learning (DL) methods have achieved state-of-the-art (SOTA) results
in various medical image segmentation tasks. This success is largely
attributable to the use of large annotated datasets for training.
However, due to anatomical variations and complexity of medical image
data, annotations of large medical image datasets are not only
labor-intensive and time-consuming but also demand specialty-oriented
skills. In this paper, we report a novel segmentation quality assessment
(SQA) framework that combines active learning and assisted annotation to
dramatically reduce annotation effort both in image selection and
annotation querying from human experts. We propose a two-branch network
that integrates a spatial and channel-wise probability attention module
into the segmentation network to perform segmentation and predict
potential segmentation errors simultaneously. By directly assessing the
segmentation quality of

Medical Image Segmentation with Efficient Use of Annotations and Resources

Annotating Medical Image Data

Semantic segmentation of computed tomography for radiotherapy with deep learning: compensating insufficient annotation quality using contour augmentation

Enhancing Data Quality and Semantic Annotation by Combining Medical Ontology and Machine Learning Techniques

Learning with Limited Annotations: A Survey on Deep Semi-Supervised Learning for Medical Image Segmentation

PyMIC: A deep learning toolkit for annotation-efficient medical image segmentation

Impact on Cost and Expert Time of Data-Efficient Deep Learning for Medical Image Segmentation.

A deep learning–based expert-guided annotation loop reduced annotation time and estimated cost while generating high-quality reference standard CT and MRI segmentations and was feasible to implement in a clinical environment without coding.

Dual Annotation Learning with Selective Uncertainty for Medical Image Segmentation with Noisy Labels

Learning the What and How of Annotation in Video Object Segmentation

An Annotation Sparsification Strategy for 3D Medical Image Segmentation via Representative Selection and Self-Training

Image segmentation is critical to lots of medical applications. While deep learning (DL) methods continue to improve performance for many medical image segmentation tasks, data annotation is a big bottleneck to DL-based segmentation because (1) DL models tend to need a large amount of labeled data to train, and (2) it is highly time-consuming and label-intensive to voxel-wise label 3D medical images. Significantly reducing annotation effort while attaining good performance of DL segmentation models remains a major challenge. In our preliminary experiments, we observe that, using partially labeled datasets, there is indeed a large performance gap with respect to using fully annotated training datasets. In this paper, we propose a new DL framework for reducing annotation effort and bridging the gap between full annotation and sparse annotation in 3D medical image segmentation. We achieve this by (i) selecting representative slices in 3D images that minimize data redundancy and save annotation effort, and (ii) self-training with pseudo-labels automatically generated from the base-models trained using the selected annotated slices. Extensive experiments using two public datasets (the HVSMR 2016 Challenge dataset and mouse piriform cortex dataset) show that our framework yields competitive segmentation results comparing with state-of-the-art DL methods using less than ∼20% of annotated data.

An annotation tool for dermoscopic image segmentation


## Quote


Annotation-Efficient Deep Learning for Medical Imaging

Annotation-Efficient Deep Learning for Medical Imaging

Real-world challenges in airway endoscopy, including blood contamination, motion blur, occlusions, and variable illumination, may lead to inconsistent or noise-like polygon annotations, affecting segmentation stability. [...] Previous studies indicate that, in deep learning-based medical image analysis, annotation quality may influence segmentation performance more strongly than annotation quantity [3].

The common limitations of medical image segmentation datasets include scarce annotations where only limited annotated data is available for training, and weak annotations where the training data has only sparse annotations, noisy annotations, or image-level annotations.


## Raw_Introduction


Segmentation is among the most common medical image analysis tasks and is critical to a wide variety of clinical applications. To date, data-driven deep learning (DL) methods have shown prominent segmentation performance when trained on fully-annotated datasets [8]. However, data annotation is a significant bottleneck for dataset creation. First, annotation process is tedious, laborious and time-consuming, especially for 3D medical images where dense annotation with voxel-level accuracy is required. Second, medical images typically need to be annotated by medical experts whose time is limited and expensive, making the annotations even more difficult and costly to obtain. Active learning (AL) is a promising solution to improve annotation efficiency by iteratively selecting the most important data to annotate with the goal of reducing the total number of annotated samples required. However, most deep AL methods require an initial set of labeled samples to start the active selection. When

Segmentation is among the most common medical image analysis tasks and is critical to a wide variety of clinical applications. To date, data-driven deep learning (DL) methods have shown prominent segmentation performance when trained on fully-annotated datasets [8]. However, data annotation is a significant bottleneck for dataset creation. First, annotation process is tedious, laborious and time-consuming, especially for 3D medical images where dense annotation with voxel-level accuracy is required. Second, medical images typically need to be annotated by medical experts whose time is limited and expensive, making the annotations even more difficult and costly to obtain. Active learning (AL) is a promising solution to improve annotation efficiency by iteratively selecting the most important data to annotate with the goal of reducing the total number of annotated samples required. However, most deep AL methods require an initial set of labeled samples to start the active selection. When


## Synthese


Cette section met en évidence l'asymétrie fondamentale entre l'annotation par classification (au niveau du patch) et l'annotation par segmentation (au niveau du pixel) en imagerie médicale, cette dernière étant considérablement plus coûteuse en temps et sujette à des erreurs d'annotation, notamment en histopathologie. Une analyse empirique menée sur l'annotation de métastases ganglionnaires par un pathologiste expert révèle qu'environ 80% du temps d'examen est consacré au tracé des contours, contre seulement 20% à l'identification du type de cancer dominant, avec des durées de segmentation pixel-level allant de 15 minutes à deux heures selon la taille et la complexité de la région. Une revue de 22 jeux de données publics en pathologie computationnelle confirme cette disparité: les jeux de données de classification contiennent en moyenne 49 000 images contre seulement 358 pour les jeux de données de segmentation. Face à ce constat, les auteurs proposent une architecture de réseau de neurones entraînée conjointement sur une tâche primaire de segmentation (à partir d'un nombre limité de WSI segmentées) et une tâche auxiliaire de classification (à partir de patchs labellisés), les deux tâches partageant un pathway commun encodant une représentation de caractéristiques partagée, afin de tirer parti de la richesse des données de classification, plus abondantes et moins coûteuses à acquérir. Les auteurs évaluent leur architecture entraînée conjointement sur la segmentation et la classification à partir de patchs partageant un même encodeur commun. Les expériences de validation montrent que l'apprentissage joint avec la tâche de segmentation n'améliore pas, et dégrade même, la performance de classification, ce qui conduit les auteurs à conclure que les caractéristiques apprises pour la segmentation ne sont pas transférables à la classification. À l'inverse, l'ajout de patchs de classification bon marché à un faible pourcentage de patchs de segmentation annotés produit un gain substantiel de performance de segmentation (≥15% en score F1) par rapport à un entraînement utilisant uniquement des données de segmentation, cet écart se réduisant à mesure que la proportion de données de segmentation augmente. La méthode combinée réduit également la variance inter-expériences et produit des masques de prédiction plus stables et spatialement cohérents, un effet attribué au rôle régularisateur des données de classification supplémentaires. Enfin, comparée à l'état de l'art sur les jeux de données ICIAR BACH 2018, DigestPath2019 et Gleason2019, la méthode proposée obtient des scores inférieurs, écart que les auteurs attribuent en partie à l'usage de la moitié du jeu d'entraînement et à un sous-échantillonnage important des images plutôt qu'à des architectures fortement spécialisées au domaine. Cette étude propose une méthode d'annotation d'images médicales exploitant conjointement un petit nombre de patchs annotés au niveau de la segmentation et une majorité de patchs plus faciles à étiqueter au niveau de l'image, via une architecture partageant un même pathway de représentation de caractéristiques entre les tâches de segmentation et de classification. Les résultats montrent que cette approche combinée (S+C ou S+C*) surpasse significativement le réglage segmentation seule d'au moins 15% en F1 lorsque les patchs de segmentation disponibles sont limités (≤10%), tout en réduisant la variance et en produisant des prédictions spatialement plus cohérentes grâce à l'effet régularisateur des données de classification. En revanche, l'entraînement conjoint n'apporte pas de bénéfice à la tâche de classification elle-même, les caractéristiques issues de la segmentation ne s'avérant pas utiles pour cette dernière. Les auteurs reconnaissent des limites méthodologiques, notamment une difficulté à séparer les représentations de fond et de premier plan lorsque les régions d'intérêt sont très petites, ainsi qu'une incapacité à traiter de grands patchs (par exemple 512×512 pixels), pourtant critiques en histopathologie mammaire. Cette méthode est présentée comme un outil potentiel pour accélérer l'acquisition de données ou pour valoriser des jeux de données existants ne comportant que des labels au niveau image, tels que le jeu de données de classification du cancer BreakHis.

Cette section met en évidence l'asymétrie fondamentale entre l'annotation par classification (au niveau du patch) et l'annotation par segmentation (au niveau du pixel) en imagerie médicale, cette dernière étant considérablement plus coûteuse en temps et sujette à des erreurs d'annotation, notamment en histopathologie. Une analyse empirique menée sur l'annotation de métastases ganglionnaires par un pathologiste expert révèle qu'environ 80% du temps d'examen est consacré au tracé des contours, contre seulement 20% à l'identification du type de cancer dominant, avec des durées de segmentation pixel-level allant de 15 minutes à deux heures selon la taille et la complexité de la région. Une revue de 22 jeux de données publics en pathologie computationnelle confirme cette disparité: les jeux de données de classification contiennent en moyenne 49 000 images contre seulement 358 pour les jeux de données de segmentation. Face à ce constat, les auteurs proposent une architecture de réseau de neurones entraînée conjointement sur une tâche primaire de segmentation (à partir d'un nombre limité de WSI segmentées) et une tâche auxiliaire de classification (à partir de patchs labellisés), les deux tâches partageant un pathway commun encodant une représentation de caractéristiques partagée, afin de tirer parti de la richesse des données de classification, plus abondantes et moins coûteuses à acquérir.

Cette revue examine les solutions d’apprentissage profond conçues pour atténuer deux limitations majeures des jeux de données de segmentation d’images médicales : la rareté des annotations et leur faible qualité ou granularité. Malgré les progrès des architectures de segmentation, notamment dans les connexions résiduelles, les mécanismes d’attention et les modules hybrides, leurs performances demeurent fortement dépendantes de jeux de données annotés volumineux et fiables. Les approches recensées contre la rareté des annotations comprennent des méthodes semi-automatisées, telles que l’apprentissage actif et la segmentation interactive, ainsi que des méthodes automatisées exploitant des données non annotées, synthétiques ou issues de domaines similaires. La revue couvre également les stratégies adaptées aux annotations clairsemées, bruitées ou limitées au niveau de l’image, tout en soulignant que ces imperfections peuvent compromettre la généralisation en contexte clinique réel [Unknown](zotero://select/library/items/ZRSWCZE4).


## Methodologie


Cette section met en évidence l'asymétrie fondamentale entre l'annotation par classification (au niveau du patch) et l'annotation par segmentation (au niveau du pixel) en imagerie médicale, cette dernière étant considérablement plus coûteuse en temps et sujette à des erreurs d'annotation, notamment en histopathologie. Une analyse empirique menée sur l'annotation de métastases ganglionnaires par un pathologiste expert révèle qu'environ 80% du temps d'examen est consacré au tracé des contours, contre seulement 20% à l'identification du type de cancer dominant, avec des durées de segmentation pixel-level allant de 15 minutes à deux heures selon la taille et la complexité de la région. Une revue de 22 jeux de données publics en pathologie computationnelle confirme cette disparité: les jeux de données de classification contiennent en moyenne 49 000 images contre seulement 358 pour les jeux de données de segmentation. Face à ce constat, les auteurs proposent une architecture de réseau de neurones entraînée conjointement sur une tâche primaire de segmentation (à partir d'un nombre limité de WSI segmentées) et une tâche auxiliaire de classification (à partir de patchs labellisés), les deux tâches partageant un pathway commun encodant une représentation de caractéristiques partagée, afin de tirer parti de la richesse des données de classification, plus abondantes et moins coûteuses à acquérir.

Cette revue examine les solutions d’apprentissage profond conçues pour atténuer deux limitations majeures des jeux de données de segmentation d’images médicales : la rareté des annotations et leur faible qualité ou granularité. Malgré les progrès des architectures de segmentation, notamment dans les connexions résiduelles, les mécanismes d’attention et les modules hybrides, leurs performances demeurent fortement dépendantes de jeux de données annotés volumineux et fiables. Les approches recensées contre la rareté des annotations comprennent des méthodes semi-automatisées, telles que l’apprentissage actif et la segmentation interactive, ainsi que des méthodes automatisées exploitant des données non annotées, synthétiques ou issues de domaines similaires. La revue couvre également les stratégies adaptées aux annotations clairsemées, bruitées ou limitées au niveau de l’image, tout en soulignant que ces imperfections peuvent compromettre la généralisation en contexte clinique réel [Unknown](zotero://select/library/items/ZRSWCZE4).


## Discussion


Cette étude montre que les annotations produites par SAM à partir d’annotations clairsemées présentent des scores Dice moyens par coupe élevés, mais une cohérence tridimensionnelle insuffisante, associée à des scores Dice volumiques significativement inférieurs à ceux des annotations de référence. En conséquence, les modèles 3D SAM-nnU-Net obtiennent des performances significativement inférieures aux modèles GT-nnU-Net dans les cadres simulé et réaliste de crowdsourcing pour la segmentation d’organes abdominaux sur des images de tomodensitométrie (p < 0,001 pour toutes les comparaisons). La fiabilité des contributions non expertes constitue une autre limite majeure : 4 des 15 volumes, soit 27 %, ne comportaient pas d’annotations complètes des cinq organes étudiés, tandis que le filtrage des annotations incomplètes ou non fiables améliorait les performances du modèle. Ces résultats appellent au développement de modèles de fondation spécialisés dans la segmentation 3D et à l’intégration de procédures automatisées d’évaluation de la qualité avant l’utilisation à grande échelle du crowdsourcing en imagerie médicale [Unknown](zotero://select/library/items/EMVSWG59).

Cette étude montre que les annotations produites par SAM à partir d’annotations clairsemées présentent des scores Dice moyens par coupe élevés, mais une cohérence tridimensionnelle insuffisante, associée à des scores Dice volumiques significativement inférieurs à ceux des annotations de référence. En conséquence, les modèles 3D SAM-nnU-Net obtiennent des performances significativement inférieures aux modèles GT-nnU-Net dans les cadres simulé et réaliste de crowdsourcing pour la segmentation d’organes abdominaux sur des images de tomodensitométrie (p < 0,001 pour toutes les comparaisons). La fiabilité des contributions non expertes constitue une autre limite majeure : 4 des 15 volumes, soit 27 %, ne comportaient pas d’annotations complètes des cinq organes étudiés, tandis que le filtrage des annotations incomplètes ou non fiables améliorait les performances du modèle. Ces résultats appellent au développement de modèles de fondation spécialisés dans la segmentation 3D et à l’intégration de procédures automatisées d’évaluation de la qualité avant l’utilisation à grande échelle du crowdsourcing en imagerie médicale [Unknown](zotero://select/library/items/EMVSWG59).

Cette étude propose une méthode d'annotation d'images médicales exploitant conjointement un petit nombre de patchs annotés au niveau de la segmentation et une majorité de patchs plus faciles à étiqueter au niveau de l'image, via une architecture partageant un même pathway de représentation de caractéristiques entre les tâches de segmentation et de classification. Les résultats montrent que cette approche combinée (S+C ou S+C*) surpasse significativement le réglage segmentation seule d'au moins 15% en F1 lorsque les patchs de segmentation disponibles sont limités (≤10%), tout en réduisant la variance et en produisant des prédictions spatialement plus cohérentes grâce à l'effet régularisateur des données de classification. En revanche, l'entraînement conjoint n'apporte pas de bénéfice à la tâche de classification elle-même, les caractéristiques issues de la segmentation ne s'avérant pas utiles pour cette dernière. Les auteurs reconnaissent des limites méthodologiques, notamment une difficulté à séparer les représentations de fond et de premier plan lorsque les régions d'intérêt sont très petites, ainsi qu'une incapacité à traiter de grands patchs (par exemple 512×512 pixels), pourtant critiques en histopathologie mammaire. Cette méthode est présentée comme un outil potentiel pour accélérer l'acquisition de données ou pour valoriser des jeux de données existants ne comportant que des labels au niveau image, tels que le jeu de données de classification du cancer BreakHis.


## Raw_Discussion


In our 2D segmentation experiments, we found it advantageous to distribute the annotation budget across a greater number of volumes with fewer annotated slices per volume. This approach helps mitigate redundancy in adjacent slices, as focusing annotation on fewer volumes results in many highly similar slices. Annotating a broader range of volumes introduces the model to a wider variety of naturally-occurred variations between volumes, which data augmentation may not replicate. In 3D deep learning methods, the principle that "sparser annotations are better" generally holds true as well, despite the exception we noticed on the ATLAS dataset when a very low number of slices per volume is annotated. When annotation density falls below 20%, prioritizing a higher volume count over annotation density does not result in improved model performance. Our preliminary data on the topic points to the likely impact of the network architecture (the generally observed trend appears to be maintained whe