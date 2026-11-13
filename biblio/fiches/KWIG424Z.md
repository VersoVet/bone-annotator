# DL-AAT: An Automatic Annotation Tool for Efficient Data Labeling in Vision-Based Systems



## Resume


DL-AAT: An Automatic Annotation Tool for Efficient Data Labeling in Vision-Based Systems

Efficient annotation of image data sets for computer vision applications

Computer Vision Annotation Tool

Smart Data Annotation: Accelerating Data Labeling Processes through Deep Learning

VAST (Volume Annotation and Segmentation Tool): Efficient Manual and Semi-Automatic Labeling of Large 3D Image Stacks

LabelMe: A Database and Web-Based Tool for Image Annotation

Novel artificial intelligence-driven software significantly shortens the time required for annotation in computer vision projects

Background and study aims The contribution of artificial intelligence (AI) to endoscopy is rapidly expanding. Accurate labelling of source data (video frames) remains the rate-limiting step for such projects and is a painstaking, cost-inefficient, time-consuming process. A novel software platform, Cord Vision (CdV) allows automated annotation based on “embedded intelligence.” The user manually labels a representative proportion of frames in a section of video (typically 5 %), to create ‘micro-modelsʼ which allow accurate propagation of the label throughout the remaining video frames. This could drastically reduce the time required for annotation.  
          Methods We conducted a comparative study with an open-source labelling platform (CVAT) to determine speed and accuracy of labelling. 
          Results Across 5 users, CdV resulted in a significant increase in labelling performance (P < 0.001) compared to CVAT for bounding box placement. 
          Conclusions This advance represen

LabelMe: Online Image Annotation and Applications

PyTAGIT: a scalable and interactive human-in-the-loop tool for fast image annotation

Speeding up scientific imaging workflows: Design of automated image annotation tool

LATTE: Accelerating LiDAR Point Cloud Annotation via Sensor Fusion, One-Click Annotation, and Tracking

LiDAR (Light Detection And Ranging) is an essential and widely adopted sensor for autonomous vehicles, particularly for those vehicles operating at higher levels (L4-L5) of autonomy. Recent work has demonstrated the promise of deep-learning approaches for LiDAR-based detection. However, deep-learning algorithms are extremely data hungry, requiring large amounts of labeled point-cloud data for training and evaluation. Annotating LiDAR point cloud data is challenging due to the following issues: 1) A LiDAR point cloud is usually sparse and has low resolution, making it difficult for human annotators to recognize objects. 2) Compared to annotation on 2D images, the operation of drawing 3D bounding boxes or even point-wise labels on LiDAR point clouds is more complex and time-consuming. 3) LiDAR data are usually collected in sequences, so consecutive frames are highly correlated, leading to repeated annotations. To tackle these challenges, we propose LATTE, an open-sourced annotation tool

Human-machine collaboration on data annotation of images by semi-automatic labeling

3D Image Annotation using Deep Learning and View-based Image Features

An interactive tool for manual, semi-automatic and automatic video annotation

Active learning based image annotation


## Synthese


L’article présente une version préliminaire d’IAT (Image Annotation Tool), outil d’annotation d’images développé au Imaging and Vision Laboratory. L’objectif principal est d’introduire cette interface et d’en évaluer la qualité d’usage, en vérifiant si le programme répond correctement aux actions et aux besoins des utilisateurs. L’évaluation repose sur une phase de tests d’utilisabilité comprenant des tâches d’annotation de difficulté croissante, suivie d’un questionnaire de 14 énoncés notés sur une échelle de 1 à 5. La population de testeurs inclut des utilisateurs peu ou moyennement expérimentés en informatique ainsi que des utilisateurs experts. Dans l’ensemble, le système s’est révélé intuitif : tous les utilisateurs, sauf un, ont pu atteindre les objectifs proposés, et les fonctionnalités initiales ainsi que l’interface graphique ont été jugées efficaces. Les auteurs présentent IAT comme une première étape vers un outil plus complet, visant notamment l’ajout de fonctionnalités pour simplifier et accélérer le processus d’annotation.

L’estimation de pose constitue un problème fondamental en vision par ordinateur, mais l’annotation manuelle des données de pose demeure chronophage et coûteuse, tandis que les systèmes multi-caméras, bien qu’utilisés pour générer automatiquement des labels, requièrent encore une annotation initiale importante. Les auteurs proposent un processus d’annotation fondé sur l’apprentissage actif (Active Learning, AL) afin de concentrer le budget d’annotation sur les échantillons les plus informatifs pour l’estimation de pose 3D du corps et de la main à partir d’images RGB multi-vues. Contrairement aux approches AL mono-vues existantes, deux stratégies exploitant la géométrie multi-vues sont introduites, et un mécanisme d’auto-entraînement (self-training) enrichit les labels humains par des pseudo-labels dérivés des prédictions du modèle. Le système itératif combine ainsi une branche AL de sélection des frames non annotées et une branche de pseudo-labellisation, sans coût annotationnel ni computationnel supplémentaire. Des simulations et expériences sur CMU Panoptic et InterHand2.6M indiquent des gains d’efficacité d’annotation, avec une réduction rapportée jusqu’à 60 % du temps de cycle et 80 % du coût de main-d’œuvre sur CMU Panoptic par rapport aux processus d’annotation existants.

L’estimation de pose constitue un problème fondamental en vision par ordinateur, mais l’annotation manuelle des données de pose demeure chronophage et coûteuse, tandis que les systèmes multi-caméras, bien qu’utilisés pour générer automatiquement des labels, requièrent encore une annotation initiale importante. Les auteurs proposent un processus d’annotation fondé sur l’apprentissage actif (Active Learning, AL) afin de concentrer le budget d’annotation sur les échantillons les plus informatifs pour l’estimation de pose 3D du corps et de la main à partir d’images RGB multi-vues. Contrairement aux approches AL mono-vues existantes, deux stratégies exploitant la géométrie multi-vues sont introduites, et un mécanisme d’auto-entraînement (self-training) enrichit les labels humains par des pseudo-labels dérivés des prédictions du modèle. Le système itératif combine ainsi une branche AL de sélection des frames non annotées et une branche de pseudo-labellisation, sans coût annotationnel ni computationnel supplémentaire. Des simulations et expériences sur CMU Panoptic et InterHand2.6M indiquent des gains d’efficacité d’annotation, avec une réduction rapportée jusqu’à 60 % du temps de cycle et 80 % du coût de main-d’œuvre sur CMU Panoptic par rapport aux processus d’annotation existants.

L'introduction dresse un panorama des outils d'annotation vidéo récents, dont l'objectif commun est de réduire l'effort humain requis pour produire des vérités terrain à grande échelle tout en améliorant la qualité des annotations, via des méthodes de vision par ordinateur et d'apprentissage automatique ou via des plateformes de crowd-sourcing. Les auteurs identifient les fonctionnalités caractérisant ces outils, telles que la forme des boîtes englobantes, la propagation d'annotations entre images clés par interpolation linéaire ou par suivi (tracking), et la navigation dans les images et les plans vidéo. Ils soulignent que l'objectif ultime de ces outils est de minimiser au maximum la charge d'annotation manuelle, notamment par l'intégration d'algorithmes de détection d'objets supervisée, de mise en correspondance de gabarits (template matching) ou de reconnaissance d'actions, tout en reconnaissant les limites de robustesse et de spécificité de domaine de ces approches. Une comparaison structurée (Tableau 1) des outils existants est proposée selon des critères de conception, d'interaction utilisateur et de fonctionnalités d'annotation de base et avancées. Les données d'évaluation rapportées pour l'outil présenté montrent que les modes semi-automatique et automatique réduisent d'au moins un ordre de grandeur le nombre d'interventions humaines nécessaires par rapport au mode manuel complet, avec des gains additionnels de quelques pourcents selon l'optimisation des paramètres. Les auteurs concluent avec la présentation d'iVAT, un outil d'annotation vidéo interactif intégrant trois modalités (manuelle, semi-automatique et automatique) reposant sur des algorithmes de vision par ordinateur conçus pour un fonctionnement incrémental. L'évaluation quantitative montre que les modes semi-automatique et automatique réduisent le ratio moyen d'interventions humaines d'au moins un ordre de grandeur par rapport au mode manuel, tandis qu'une comparaison avec l'outil de référence ViPER-GT indique une meilleure utilisabilité et un nombre d'interactions requis plus faible pour iVAT. L'outil, développé en C/C++ avec Qt et OpenCV, est présenté comme modulaire et portable, facilitant l'ajout de nouveaux modules de vision et son déploiement sur plateformes mobiles. Les auteurs annoncent comme perspectives l'extension de l'outil à la détection automatique et semi-automatique d'actions, ainsi que l'évaluation de son efficacité sur d'autres domaines d'application.


## Raw_B._Case_Study:_Oracle-Assisted_In-Context_Learning_For_Safe_And_Efficient_Uav_Resource_Allocation


2) Detection: Liang etal. [53] are concerned with 3D object detection for AVs. DL-based object detectors require large annotated datasets, which incur high annotation costs. To address this problem, they develop diversity-based AL, which uses the multimodal information of an AV dataset to propose a detection function that enforces spatial and temporal diversity in the selected samples. In this approach, the most informative frames and objects are automatically selected for annotation by humans. Similarly, Ding etal. [35] address vehicle type recognition (VTR) from surveillance data in intelligent transportation. To facilitate manual labeling of large-scale surveillance data, they propose a VTR system based on deep AL. A deep neural network is efficiently trained by actively, incrementally, and automatically selecting unlabeled data points for human labeling. The training procedure is repeated several times so that the neural network is re-trained with the incrementally updated training

2) Detection: Liang etal. [53] are concerned with 3D object detection for AVs. DL-based object detectors require large annotated datasets, which incur high annotation costs. To address this problem, they develop diversity-based AL, which uses the multimodal information of an AV dataset to propose a detection function that enforces spatial and temporal diversity in the selected samples. In this approach, the most informative frames and objects are automatically selected for annotation by humans. Similarly, Ding etal. [35] address vehicle type recognition (VTR) from surveillance data in intelligent transportation. To facilitate manual labeling of large-scale surveillance data, they propose a VTR system based on deep AL. A deep neural network is efficiently trained by actively, incrementally, and automatically selecting unlabeled data points for human labeling. The training procedure is repeated several times so that the neural network is re-trained with the incrementally updated training


## Quote


To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking.

To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking.


## Raw_Related_Work


Annotation tools: Many efforts focus on improving annotation tools to generate more data for deep learning training, but most of the annotation tools are focusing on images. VIA [12] provides a simple yet powerful webpage-based tool for drawing bounding boxes and polygons on images. Later works such as PolygonRNN [13], [14] seek to utilize more advanced algorithms to facilitate and accelerate human annotations. For video annotation, VATIC [15] integrates tracking (mainly linear interpolation) to reduce annotating repeated entities in consecutive frames. For autonomous driving applications, Yu et al. propose Scalabel [16], a package of tools that support annotating bounding boxes and semantic masks on images. Few works have focused on building LiDAR annotation tools. The Apolloscape [6] dataset's annotation pipeline uses sensor fusion and image-based detection to generate labels through images. But their 3D annotations are for static backgrounds instead of moving objects. [17] adopts a

Annotation tools: Many efforts focus on improving annotation tools to generate more data for deep learning training, but most of the annotation tools are focusing on images. VIA [12] provides a simple yet powerful webpage-based tool for drawing bounding boxes and polygons on images. Later works such as PolygonRNN [13], [14] seek to utilize more advanced algorithms to facilitate and accelerate human annotations. For video annotation, VATIC [15] integrates tracking (mainly linear interpolation) to reduce annotating repeated entities in consecutive frames. For autonomous driving applications, Yu et al. propose Scalabel [16], a package of tools that support annotating bounding boxes and semantic masks on images. Few works have focused on building LiDAR annotation tools. The Apolloscape [6] dataset's annotation pipeline uses sensor fusion and image-based detection to generate labels through images. But their 3D annotations are for static backgrounds instead of moving objects. [17] adopts a


## Methodologie


L’estimation de pose constitue un problème fondamental en vision par ordinateur, mais l’annotation manuelle des données de pose demeure chronophage et coûteuse, tandis que les systèmes multi-caméras, bien qu’utilisés pour générer automatiquement des labels, requièrent encore une annotation initiale importante. Les auteurs proposent un processus d’annotation fondé sur l’apprentissage actif (Active Learning, AL) afin de concentrer le budget d’annotation sur les échantillons les plus informatifs pour l’estimation de pose 3D du corps et de la main à partir d’images RGB multi-vues. Contrairement aux approches AL mono-vues existantes, deux stratégies exploitant la géométrie multi-vues sont introduites, et un mécanisme d’auto-entraînement (self-training) enrichit les labels humains par des pseudo-labels dérivés des prédictions du modèle. Le système itératif combine ainsi une branche AL de sélection des frames non annotées et une branche de pseudo-labellisation, sans coût annotationnel ni computationnel supplémentaire. Des simulations et expériences sur CMU Panoptic et InterHand2.6M indiquent des gains d’efficacité d’annotation, avec une réduction rapportée jusqu’à 60 % du temps de cycle et 80 % du coût de main-d’œuvre sur CMU Panoptic par rapport aux processus d’annotation existants.

L’estimation de pose constitue un problème fondamental en vision par ordinateur, mais l’annotation manuelle des données de pose demeure chronophage et coûteuse, tandis que les systèmes multi-caméras, bien qu’utilisés pour générer automatiquement des labels, requièrent encore une annotation initiale importante. Les auteurs proposent un processus d’annotation fondé sur l’apprentissage actif (Active Learning, AL) afin de concentrer le budget d’annotation sur les échantillons les plus informatifs pour l’estimation de pose 3D du corps et de la main à partir d’images RGB multi-vues. Contrairement aux approches AL mono-vues existantes, deux stratégies exploitant la géométrie multi-vues sont introduites, et un mécanisme d’auto-entraînement (self-training) enrichit les labels humains par des pseudo-labels dérivés des prédictions du modèle. Le système itératif combine ainsi une branche AL de sélection des frames non annotées et une branche de pseudo-labellisation, sans coût annotationnel ni computationnel supplémentaire. Des simulations et expériences sur CMU Panoptic et InterHand2.6M indiquent des gains d’efficacité d’annotation, avec une réduction rapportée jusqu’à 60 % du temps de cycle et 80 % du coût de main-d’œuvre sur CMU Panoptic par rapport aux processus d’annotation existants.


## Raw_Conclusion


Efficiently annotating LiDAR point clouds at scale is crucial for the development of LiDAR-based detection and autonomous driving. However, annotating LiDAR point clouds is difficult due to the challenges of low resolution, complex annotating operations, and sequential correlation. To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking. Based on our own experiments we estimate that LATTE achieves a 6.2x speedup compared with baseline annotation tools and delivers better label quality with 23.6% and 2.2% higher instance-level precision and recall, and 2.0% higher bounding box IoU.

Efficiently annotating LiDAR point clouds at scale is crucial for the development of LiDAR-based detection and autonomous driving. However, annotating LiDAR point clouds is difficult due to the challenges of low resolution, complex annotating operations, and sequential correlation. To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking. Based on our own experiments we estimate that LATTE achieves a 6.2x speedup compared with baseline annotation tools and delivers better label quality with 23.6% and 2.2% higher instance-level precision and recall, and 2.0% higher bounding box IoU.


## Raw_Labeling_System


To satisfy these requirements, we design an efficient labeling system that is sufficient for the annotation of a large driving video database. First of all, the system is adaptable so that it would allow the practice of various kinds of annotation work such as bounding box and region annotation. Secondly, the system aims to make the annotation process as seamless and user-friendly as possible. Besides, we choose to implement the annotation system as a web-based tool so that it can be simply accessed through a web browser without installation. Figure 2 (a) shows an overview of our system. In this section, we will describe the details and evaluate the efficiency of our annotation tool. Fig. 2: Back-end and front-end of our labeling system