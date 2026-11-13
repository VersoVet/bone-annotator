# HAL-IA: A Hybrid Active Learning framework using Interactive Annotation for medical image segmentation



## Resume


HAL-IA: A Hybrid Active Learning framework using Interactive Annotation for medical image segmentation

Suggestive Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

Attention, Suggestion and Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

Progressive medical image annotation with convolutional neural network-based interactive segmentation method

Active learning with noise modeling for medical image annotation

Modular Deep Active Learning Framework for Image Annotation: A Technical Report for the Ophthalmo-AI Project

Image annotation is one of the most essential tasks for guaranteeing proper treatment for patients and tracking progress over the course of therapy in the field of medical imaging and disease diagnosis. However, manually annotating a lot of 2D and 3D imaging data can be extremely tedious. Deep Learning (DL) based segmentation algorithms have completely transformed this process and made it possible to automate image segmentation. By accurately segmenting medical images, these algorithms can greatly minimize the time and effort necessary for manual annotation. Additionally, by incorporating Active Learning (AL) methods, these segmentation algorithms can perform far more effectively with a smaller amount of ground truth data. We introduce MedDeepCyleAL, an end-to-end framework implementing the complete AL cycle. It provides researchers with the flexibility to choose the type of deep learning model they wish to employ and includes an annotation tool that supports the classification and seg

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

Invited 2 - Annotation-Efficient Deep Learning for Medical Image Segmentation

Active learning based image annotation

Medical Image Segmentation with Efficient Use of Annotations and Resources

PyMIC: A deep learning toolkit for annotation-efficient medical image segmentation

Interactive image segmentation

An annotation tool for dermoscopic image segmentation

Effective image annotation via active learning

Annotating Medical Image Data

Learning with Limited Annotations: A Survey on Deep Semi-Supervised Learning for Medical Image Segmentation

Interactive Segmentation and its Use at Scale through Concurrent Annotation and Training

Segmentation interactive et son utilisation à grande échelle par annotation et entraînement simultanés
                L'apprentissage automatique (ML) s'appuie sur des algorithmes statistiques apprenant à partir de données pour prédire ou décider sans instructions explicites. Ces algorithmes se concrétisent dans des modèles reflétant les motifs appris. L'entraînement ajuste leurs paramètres à partir des données d'entrée. Le modèle peut alors s'appliquer à des données inédites. L'annotation fournit des étiquettes vérités terrain guidant l'entraînement. Un modèle de ML est souvent un réseau de neurones artificiels (ANN), composé de couches de neurones artificiels. L'apprentissage profond (DL), sous-ensemble du ML, mobilise des réseaux profonds plus performants, mais exigeant de plus grands ensembles de données.La demande de grands jeux de données annotées est particulièrement forte en imagerie médicale, où l'annotation précise se révèle difficile en raison de la complexité des données, de l'expertise requise et du caractère critique des prédictions. La segmentation, tâche essentielle dans l'interprétation d'images médicales, exige une délinéation au pixel près réalisée par des spécialistes — un processus chronophage et peu extensible. L'annotation en imagerie médicale soulève donc deux défis majeurs : (1) la nécessité de solutions d'annotation adaptées au contexte clinique pour accélérer l'annotation et améliorer les performances, et (2) la nécessité de systèmes dédiés à l'annotation à grande échelle afin de produire les données d'entraînement nécessaires à ces solutions.La segmentation d'images médicales peut être manuelle, automatique ou semi-automatique (interactive). Les segmentations servent souvent au diagnostic ou à des tâches ultérieures, comme la génération de modèles 3D pour la réalité augmentée (RA) chirurgicale dans ce travail. Compte tenu des enjeux élevés, les algorithmes interactifs conviennent au milieu clinique, car l'expert peut rectifier les sorties du modèle. Pour corriger efficacement, le modèle doit interpréter les retours de l'utilisateur et en déduire son intention, souvent négligée par les approches actuelles. Les systèmes d'annotation efficaces s'appuient généralement sur un prédicteur neuronal entraîné à partir de données annotées par des outils classiques, puis figé. Cette méthode est sous-optimale : (1) elle exige un grand volume de données annotées dès le départ, et (2) le prédicteur ne profite pas des annotations nouvelles. Il en résulte une dépendance circulaire, non abordée directement dans la littérature.Dans cette thèse, nous répondons à ces deux défis avec quatre contributions pour la segmentation et l'annotation, réparties en deux approches centrées sur les données et deux sur les applications. Côté données, nous présentons un nouvel ensemble FPMRI (FPMRId) et étudions sa variabilité inter-experts. Côté applications, nous proposons deux solutions clés. D'abord, un cadre général de segmentation interactive qui améliore les performances en tenant compte de la manière habituelle de segmenter. Contrairement aux méthodes existantes qui ignorent la séquence des interactions, nous introduisons une mémoire d'interactions intégrée à l'entraînement, assurant plus de précision avec moins d'interventions. Ensuite, SAIM (Single Active Interactive Model) intègre la sélection de données, l'annotation et l'entraînement au sein d'une architecture unifiée grâce à un modèle partagé. SAIM est une solution « deux-en-un » : le modèle partagé sert à la fois d'outil d'annotation et de prédicteur déployable. Il fonctionne en boucle : le modèle partagé, pré-entraîné sur quelques centaines d'images, est utilisé pour sélectionner les données à annoter, proposer des annotations et, si besoin, les corriger de manière interactive. Cette approche atténue le besoin de vastes ensembles annotés dès le départ, permettant de commencer avec peu de données, tout en améliorant progressivement le modèle et en diminuant la charge d'annotation. Bien que SAIM soit appliqué à la segmentation, il n'est pas limité à une tâche ou un domaine donné.

SliceInsightNet: Advanced Hybrid Image Segmentation for Spine Annotation in MRI

Active learning with applications in biomedical document annotation


## Discussion


Cette conclusion présente un framework d'apprentissage hybride bi-niveau pour la segmentation d'images médicales, conçu pour tirer parti d'un grand nombre d'instances faiblement annotées associées à un nombre restreint d'instances fortement annotées. L'approche repose sur deux composantes complémentaires : l'algorithme d'apprentissage DII, qui ajuste automatiquement le poids attribué à chaque instance faiblement annotée en se guidant sur la direction du gradient issu des rares instances fortement annotées, ce qui permet de compenser l'incohérence entre instances ; et le framework DCR, qui combine un entraînement collaboratif et une régularisation de cohérence pour atténuer la distorsion inhérente aux annotations faibles. Les expériences menées démontrent que cette méthode surpasse nettement les approches état de l'art existantes et se rapproche des performances obtenues en supervision complète. Les auteurs concluent que ce framework constitue une solution prometteuse pour la segmentation d'images médicales dans des contextes où l'annotation exhaustive est coûteuse ou difficile à obtenir.


## Conclusion


Le framework HISE permet d'obtenir à la fois des données annotées et des modèles de segmentation entraînés simultanément, avec un coût d'annotation humaine considérablement réduit La stratégie d'apprentissage actif basée sur la cohérence locale permet d'identifier efficacement les échantillons difficiles nécessitant une intervention humaine L'apprentissage progressif permet d'améliorer incrémentalement le modèle de segmentation au fil des itérations Contrairement à l'annotation humaine classique, HISE peut rapporter la difficulté de segmentation de chaque image, ce qui peut servir de prior pour le développement de modèles de segmentation avancés Les travaux futurs viseront à étendre HISE à des tâches de segmentation plus complexes impliquant de nombreuses classes


## Synthese


Le segmentation d'images médicales constitue une tâche fondamentale pour de nombreuses applications biomédicales, mais les modèles d'apprentissage profond dépendent fortement d'annotations exhaustives de haute qualité, dont la production reste coûteuse en expertise, en temps et en main-d'œuvre. Pour pallier cette limite, les auteurs proposent un framework hybride-supervisé combinant, de façon itérative, un niveau supérieur d'Instance Importance Learning (DII) et un niveau inférieur de Dual Co-Regularization (DCR). Le module DII ajuste automatiquement le poids attribué à chaque instance faiblement annotée en s'appuyant sur la direction du gradient issue des quelques instances fortement annotées, ce qui permet de compenser l'incohérence entre instances faiblement labellisées. Le module DCR repose sur une architecture à double réseau entraînée de manière collaborative, chaque réseau étant supervisé à la fois par son annotation propre et par le masque pseudo-généré par l'autre branche, réduisant ainsi la distorsion inhérente aux labels faibles. Cette approche permet, avec seulement 10% de labels forts, d'atteindre une performance compétitive comparable à un scénario entièrement supervisé. Cette conclusion présente un framework d'apprentissage hybride bi-niveau pour la segmentation d'images médicales, conçu pour tirer parti d'un grand nombre d'instances faiblement annotées associées à un nombre restreint d'instances fortement annotées. L'approche repose sur deux composantes complémentaires : l'algorithme d'apprentissage DII, qui ajuste automatiquement le poids attribué à chaque instance faiblement annotée en se guidant sur la direction du gradient issu des rares instances fortement annotées, ce qui permet de compenser l'incohérence entre instances ; et le framework DCR, qui combine un entraînement collaboratif et une régularisation de cohérence pour atténuer la distorsion inhérente aux annotations faibles. Les expériences menées démontrent que cette méthode surpasse nettement les approches état de l'art existantes et se rapproche des performances obtenues en supervision complète. Les auteurs concluent que ce framework constitue une solution prometteuse pour la segmentation d'images médicales dans des contextes où l'annotation exhaustive est coûteuse ou difficile à obtenir.

Cet article propose un cadre d'apprentissage actif profond, nommé Suggestive Annotation, destiné à réduire l'effort d'annotation manuelle requis pour la segmentation d'images biomédicales. La méthode combine un réseau entièrement convolutif (FCN) avec une stratégie d'apprentissage actif, où l'incertitude et la similarité estimées à partir d'un ensemble de FCN sont utilisées pour sélectionner itérativement les images les plus informatives à annoter, via une formulation généralisée du problème de couverture maximale. Le cadre a été évalué sur deux jeux de données distincts: le 2015 MICCAI Gland Challenge et un jeu de données de segmentation d'images échographiques de ganglions lymphatiques. Les résultats montrent que les suggestions d'annotation fondées conjointement sur l'incertitude et la similarité surpassent à la fois la sélection aléatoire et la sélection basée sur l'incertitude seule. Les auteurs concluent qu'une performance de segmentation à l'état de l'art peut être obtenue avec seulement 50% des données d'entraînement annotées, démontrant ainsi la capacité du framework à orienter efficacement les efforts d'annotation manuelle vers les zones les plus utiles.

Cette revue examine les solutions d’apprentissage profond conçues pour atténuer deux limitations majeures des jeux de données de segmentation d’images médicales : la rareté des annotations et leur faible qualité ou granularité. Malgré les progrès des architectures de segmentation, notamment dans les connexions résiduelles, les mécanismes d’attention et les modules hybrides, leurs performances demeurent fortement dépendantes de jeux de données annotés volumineux et fiables. Les approches recensées contre la rareté des annotations comprennent des méthodes semi-automatisées, telles que l’apprentissage actif et la segmentation interactive, ainsi que des méthodes automatisées exploitant des données non annotées, synthétiques ou issues de domaines similaires. La revue couvre également les stratégies adaptées aux annotations clairsemées, bruitées ou limitées au niveau de l’image, tout en soulignant que ces imperfections peuvent compromettre la généralisation en contexte clinique réel [Unknown](zotero://select/library/items/ZRSWCZE4).


## Quote


Annotation-Efficient Deep Learning for Medical Imaging

Annotation-Efficient Deep Learning for Medical Imaging

Address the challenge of annotation-efficient deep learning for medical imaging with a holistic approach


## Raw_Introduction


Segmentation is among the most common medical image analysis tasks and is critical to a wide variety of clinical applications. To date, data-driven deep learning (DL) methods have shown prominent segmentation performance when trained on fully-annotated datasets [8]. However, data annotation is a significant bottleneck for dataset creation. First, annotation process is tedious, laborious and time-consuming, especially for 3D medical images where dense annotation with voxel-level accuracy is required. Second, medical images typically need to be annotated by medical experts whose time is limited and expensive, making the annotations even more difficult and costly to obtain. Active learning (AL) is a promising solution to improve annotation efficiency by iteratively selecting the most important data to annotate with the goal of reducing the total number of annotated samples required. However, most deep AL methods require an initial set of labeled samples to start the active selection. When

Segmentation is among the most common medical image analysis tasks and is critical to a wide variety of clinical applications. To date, data-driven deep learning (DL) methods have shown prominent segmentation performance when trained on fully-annotated datasets [8]. However, data annotation is a significant bottleneck for dataset creation. First, annotation process is tedious, laborious and time-consuming, especially for 3D medical images where dense annotation with voxel-level accuracy is required. Second, medical images typically need to be annotated by medical experts whose time is limited and expensive, making the annotations even more difficult and costly to obtain. Active learning (AL) is a promising solution to improve annotation efficiency by iteratively selecting the most important data to annotate with the goal of reducing the total number of annotated samples required. However, most deep AL methods require an initial set of labeled samples to start the active selection. When


## Methodologie


Cette revue examine les solutions d’apprentissage profond conçues pour atténuer deux limitations majeures des jeux de données de segmentation d’images médicales : la rareté des annotations et leur faible qualité ou granularité. Malgré les progrès des architectures de segmentation, notamment dans les connexions résiduelles, les mécanismes d’attention et les modules hybrides, leurs performances demeurent fortement dépendantes de jeux de données annotés volumineux et fiables. Les approches recensées contre la rareté des annotations comprennent des méthodes semi-automatisées, telles que l’apprentissage actif et la segmentation interactive, ainsi que des méthodes automatisées exploitant des données non annotées, synthétiques ou issues de domaines similaires. La revue couvre également les stratégies adaptées aux annotations clairsemées, bruitées ou limitées au niveau de l’image, tout en soulignant que ces imperfections peuvent compromettre la généralisation en contexte clinique réel [Unknown](zotero://select/library/items/ZRSWCZE4).