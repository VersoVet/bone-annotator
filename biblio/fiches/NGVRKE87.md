# YOLIC Labeling: A Semi-Automated Image Annotation Tool with Segment Anything Model for Cell-wise Labeling



## Resume


YOLIC Labeling: A Semi-Automated Image Annotation Tool with Segment Anything Model for Cell-wise Labeling

We introduce YOLIC Labeling, a tool designed to streamline the creation of high-quality datasets for cell wise object localization and classification. This tool integrates the Segment Anything Model (SAM) with customizable cell configurations (predefined regions of interest within images) to offer efficient and precise annotations. Key features include SAM-assisted labeling, manual polygon-based annotation, and semi-automatic labeling capabilities. By reducing manual labeling effort while maintaining accuracy, the tool supports the development of robust object localization and classification models, particularly those based on the You-Only-Look-at-Interested-Cells (YOLIC) methodology. YOLIC Labeling addresses the growing demand for efficient, versatile image annotation solutions in computer vision, with applications ranging from autonomous driving to smart industrial systems.

ByLabel: A Boundary Based Semi-Automatic Image Annotation Tool

LabelMe: A Database and Web-Based Tool for Image Annotation

PyMIC: A deep learning toolkit for annotation-efficient medical image segmentation

An annotation tool for dermoscopic image segmentation

LabelMe: Online Image Annotation and Applications

HANOLISTIC: A Hierarchical Automatic Image Annotation System Using Holistic Approach

Image Segmentation and Labeling Using Free-Form Semantic Annotation

Pseudo Label-based Multi-View Annotation for Semi-Supervised Medical Image Segmentation

Active Learning Enabled Low-Cost Cell Image Segmentation Using Bounding Box Annotation

Cell image segmentation is usually implemented using fully supervised deep learning methods, which heavily rely on extensive annotated training data. Yet, due to the complexity of cell morphology and the requirement for specialized knowledge, pixel-level annotation of cell images has become a highly labor-intensive task. To address the above problems, we propose an active learning framework for cell segmentation using bounding box annotations, which greatly reduces the data annotation cost of cell segmentation algorithms. First, we generate a box-supervised learning method (denoted as YOLO-SAM) by combining the YOLOv8 detector with the Segment Anything Model (SAM), which effectively reduces the complexity of data annotation. Furthermore, it is integrated into an active learning framework that employs the MC DropBlock method to train the segmentation model with fewer box-annotated samples. Extensive experiments demonstrate that our model saves more than ninety percent of data annotation

Every Annotation Counts: Multi-label Deep Supervision for Medical Image Segmentation

Reducing Reliance on Expensive Annotations in Medical Image Segmentation Via Diffusion Models and Segment Anything Model

Human-machine collaboration on data annotation of images by semi-automatic labeling

VAST (Volume Annotation and Segmentation Tool): Efficient Manual and Semi-Automatic Labeling of Large 3D Image Stacks

An Image Labeling Tool and Agricultural Dataset for Deep Learning

We introduce a labeling tool and dataset aimed to facilitate computer vision research in agriculture. The annotation tool introduces novel methods for labeling with a variety of manual, semi-automatic, and fully-automatic tools. The dataset includes original images collected from commercial greenhouses, images from PlantVillage, and images from Google Images. Images were annotated with segmentations for foreground leaf, fruit, and stem instances, and diseased leaf area. Labels were in an extended COCO format. In total the dataset contained 10k tomatoes, 7k leaves, 2k stems, and 2k diseased leaf annotations.

Semi-Supervised Semantic Annotator (S3A): Toward Efficient Semantic Image Labeling

An interactive tool for semi-automated leaf annotation

Cell-APP: A generalizable method for cell annotation and cell-segmentation model training.

Deep learning-based segmentation models can accelerate the analysis of high-throughput microscopy data by automatically identifying and classifying cells in images. However, the datasets needed to train these models are typically assembled via laborious hand-annotation. This limits their scale and diversity, which in turn limits model performance. We present Cell-APP (Cellular Annotation and Perception Pipeline), a tool that automates the annotation of high-quality training data for transmitted-light (TL) cell segmentation. Cell-APP uses two inputs-paired TL and nuclear fluorescence images-and operates in two main steps. First, it extracts each cell's location from the nuclear fluorescence channel and provides these locations to promptable deep learning models to generate cell masks. Then, it classifies each cell as mitotic or nonmitotic based on nuclear features. Together, these masks and classifications form the basis for cell segmentation training data. By training vision-transforme

SamDSK: Combining Segment Anything Model with Domain-Specific Knowledge for Semi-Supervised Learning in Medical Image Segmentation

The Segment Anything Model (SAM) exhibits a capability to segment a wide array of objects in natural images, serving as a versatile perceptual tool for various downstream image segmentation tasks. In contrast, medical image segmentation tasks often rely on domain-specific knowledge (DSK). In this paper, we propose a novel method that combines the segmentation foundation model (i.e., SAM) with domain-specific knowledge for reliable utilization of unlabeled images in building a medical image segmentation model. Our new method is iterative and consists of two main stages: (1) segmentation model training; (2) expanding the labeled set by using the trained segmentation model, an unlabeled set, SAM, and domain-specific knowledge. These two stages are repeated until no more samples are added to the labeled set. A novel optimal-matching-based method is developed for combining the SAM-generated segmentation proposals and pixel-level and image-level DSK for constructing annotations of unlabeled

An interactive tool for manual, semi-automatic and automatic video annotation


## Quote


the core of the new Segment Anything Model lies in over a billion annotated data obtained with a mix of various data-centric strategies (e.g., assisted manual labels and pseudo labels), which paves a viable path to build new foundation models, e.g., for general microscopy image restoration or universal in silico labeling

In this paper we introduced a labeling tool multiple manual, semi-automatic, and fully automatic annotation techniques

Annotation manuelle des images avec LabelImg (formats PASCAL VOC XML et YOLO TXT), suivie d'un contrôle qualité en trois phases (auto-validation itérative, vérification automatique de cohérence, adjudication finale par un expert)


## Methodologie


Cet article propose une méthode entièrement automatisée d'annotation de noyaux cellulaires en microscopie de fluorescence, destinée à alimenter l'entraînement de réseaux de neurones convolutifs pour la segmentation d'instance. Le pipeline enchaîne un pré-traitement, un seuillage, une segmentation par ligne de partage des eaux (watershed), un filtrage et un post-traitement appliqués directement aux images brutes, produisant automatiquement des paires image-masque annotées. Cette approche vise à contourner le goulot d'étranglement de l'annotation manuelle, qui est chronophage, sujette à des variations inter-observateurs et peu adaptée à la production de jeux de données spécifiques à chaque expérience. La méthode a été évaluée sur un jeu de données de 6409 objets en comparaison avec une annotation manuelle réalisée par un chercheur unique, et testée en combinaison avec un algorithme de suivi cellulaire (tracking).

L’annotation manuelle d’images multi-libellés à grande échelle demeure coûteuse et incomplète, tandis que les annotations crowdsourcées souffrent souvent d’incomplétude et d’erreurs liées à la fiabilité des annotateurs et à la difficulté des tâches. Les auteurs proposent de remplacer l’annotation exhaustive par une annotation partielle centrée sur les libellés saillants, sous budget d’annotation fixe, et introduisent l’algorithme Adaptive Temperature Associated Model (ATAM) pour l’apprentissage à partir de ces annotations. Dans des comparaisons expérimentales face à TresNet-448 et ML-GCN, ATAM entraîné sur des annotations partielles surpasse les modèles entraînés sur des images entièrement annotées à budget égal, notamment parce que l’annotation partielle couvre environ 2,5 fois plus d’images. Une ablation montre en outre qu’avec 40 % d’annotations partielles, la précision ne se dégrade que légèrement par rapport à une annotation complète à 100 %, tout en économisant 60 % du budget ; en revanche, traiter les libellés manquants comme négatifs dégrade fortement les scores F1 et F2 des méthodes de référence en introduisant du bruit.


## Synthese


Cet article propose une méthode entièrement automatisée d'annotation de noyaux cellulaires en microscopie de fluorescence, destinée à alimenter l'entraînement de réseaux de neurones convolutifs pour la segmentation d'instance. Le pipeline enchaîne un pré-traitement, un seuillage, une segmentation par ligne de partage des eaux (watershed), un filtrage et un post-traitement appliqués directement aux images brutes, produisant automatiquement des paires image-masque annotées. Cette approche vise à contourner le goulot d'étranglement de l'annotation manuelle, qui est chronophage, sujette à des variations inter-observateurs et peu adaptée à la production de jeux de données spécifiques à chaque expérience. La méthode a été évaluée sur un jeu de données de 6409 objets en comparaison avec une annotation manuelle réalisée par un chercheur unique, et testée en combinaison avec un algorithme de suivi cellulaire (tracking).

Cet article propose une méthode entièrement automatisée d'annotation de noyaux cellulaires en microscopie de fluorescence, destinée à alimenter l'entraînement de réseaux de neurones convolutifs pour la segmentation d'instance. Le pipeline enchaîne un pré-traitement, un seuillage, une segmentation par ligne de partage des eaux (watershed), un filtrage et un post-traitement appliqués directement aux images brutes, produisant automatiquement des paires image-masque annotées. Cette approche vise à contourner le goulot d'étranglement de l'annotation manuelle, qui est chronophage, sujette à des variations inter-observateurs et peu adaptée à la production de jeux de données spécifiques à chaque expérience. La méthode a été évaluée sur un jeu de données de 6409 objets en comparaison avec une annotation manuelle réalisée par un chercheur unique, et testée en combinaison avec un algorithme de suivi cellulaire (tracking). Cette étude évalue les performances d'un pipeline automatisé d'annotation d'images de microscopie de fluorescence, combinant prétraitement, seuillage, segmentation par ligne de partage des eaux et post-traitement, en comparaison avec une annotation manuelle réalisée par un chercheur unique, sur un jeu de données de N=6409 images. Les jeux de données ainsi générés sont utilisés pour entraîner un réseau de neurones convolutif de segmentation d'instance des noyaux cellulaires. Les résultats montrent que l'annotation automatique réduit le temps d'étiquetage jusqu'à 99.5% par rapport à l'annotation manuelle, tout en produisant des performances de segmentation comparables à celles obtenues avec un jeu de données annoté manuellement. Bien que l'approche automatisée ne détecte qu'environ 68% du nombre total de noyaux identifiés manuellement par image, sa scalabilité permet son application à des jeux de données de bien plus grande taille, augmentant ainsi le nombre total d'objets annotés disponibles pour l'entraînement. Ces résultats sont en outre démontrés sur des applications de suivi de noyaux (tracking) et d'imagerie à grande échelle. L'annotation manuelle d'un jeu de données de référence de 6409 noyaux a révélé les limites intrinsèques de ce processus : biais lié aux décisions subjectives d'un annotateur unique, variabilité statistique en cas d'annotation par plusieurs chercheurs, fatigue visuelle et temps de traitement prohibitif pour de nombreuses applications biomédicales. En comparaison, la méthode d'annotation automatique proposée offre une alternative reproductible et évolutive, bien qu'elle ne détecte qu'une fraction (68%) du nombre total de noyaux identifiés manuellement dans une image donnée ; cette limite est toutefois compensée par la possibilité d'appliquer la méthode à des jeux de données beaucoup plus vastes. La faisabilité de l'approche a été démontrée sur une image de microscopie à grande échelle contenant plus de 60000 noyaux, segmentés par un réseau de neurones puis suivis sur 8 heures et 20 minutes, l'ensemble du processus (annotation et entraînement, sans pré-entraînement du réseau) ayant été réalisé en moins d'une heure. En conclusion, cette méthode automatise l'annotation des noyaux cellulaires en réduisant considérablement le temps et la charge de travail manuels, tout en permettant l'entraînement de réseaux de neurones pour la détection, la segmentation et le suivi des noyaux au sein d'un processus unique, sans dépendance aux modèles pré-entraînés ou aux jeux de données tiers. Le système, limité à l'identification d'une classe d'objets à faible variance de surface mais indépendant de leur morphologie, fonctionne de manière optimale en association avec un réseau de segmentation d'objets étoilés (star-convex) pour améliorer la séparation des noyaux jointifs, et les auteurs envisagent son adaptation à des morphologies plus complexes, à l'imagerie histopathologique ainsi qu'à la segmentation 3D.

L’annotation manuelle d’images multi-libellés à grande échelle demeure coûteuse et incomplète, tandis que les annotations crowdsourcées souffrent souvent d’incomplétude et d’erreurs liées à la fiabilité des annotateurs et à la difficulté des tâches. Les auteurs proposent de remplacer l’annotation exhaustive par une annotation partielle centrée sur les libellés saillants, sous budget d’annotation fixe, et introduisent l’algorithme Adaptive Temperature Associated Model (ATAM) pour l’apprentissage à partir de ces annotations. Dans des comparaisons expérimentales face à TresNet-448 et ML-GCN, ATAM entraîné sur des annotations partielles surpasse les modèles entraînés sur des images entièrement annotées à budget égal, notamment parce que l’annotation partielle couvre environ 2,5 fois plus d’images. Une ablation montre en outre qu’avec 40 % d’annotations partielles, la précision ne se dégrade que légèrement par rapport à une annotation complète à 100 %, tout en économisant 60 % du budget ; en revanche, traiter les libellés manquants comme négatifs dégrade fortement les scores F1 et F2 des méthodes de référence en introduisant du bruit.


## Insight


future directions: Les modèles fondation tels que Segment Anything Model, dont la puissance repose sur plus d'un milliard d'annotations obtenues par des stratégies data-centric hybrides (labels assistés et pseudo-labels), tracent une voie viable pour développer de nouveaux modèles fondation dédiés à la restauration d'images de microscopie ou au marquage in silico universel.


## Discussion


Cette étude introduit ByLabel, un outil semi-automatique d'annotation d'images fondé sur la détection de contours et des algorithmes de segmentation, conçu pour remplacer l'annotation manuelle directe employée par des outils comme LabelMe. Une évaluation utilisateur comparative (N=10), menée sur des images synthétiques et réelles, montre que ByLabel réduit de 73% le nombre de clics nécessaires et de 56% le temps d'annotation par rapport à LabelMe. La précision de l'annotation est également améliorée de 73%, l'erreur moyenne de frontière passant de 1,1 pixel avec LabelMe à 0,3 pixel avec ByLabel. Les auteurs concluent que ByLabel surpasse LabelMe sur les plans du temps, de la précision et de l'expérience utilisateur, et que l'outil peut en outre être appliqué à l'annotation image par image de flux vidéo.