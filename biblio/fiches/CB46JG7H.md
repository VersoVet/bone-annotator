# Pixel-wise Ground Truth Annotation in Videos - An Semi-automatic Approach for Pixel-wise and Semantic Object Annotation



## Resume


Pixel-wise Ground Truth Annotation in Videos - An Semi-automatic Approach for Pixel-wise and Semantic Object Annotation

Semi-automatic ground truth annotation in videos

Semi-automatic video semantic annotation based on active learning

An interactive tool for manual, semi-automatic and automatic video annotation

Automatic Ground Truths: Projected Image Annotations for Omnidirectional Vision

We present a novel data set made up of omnidirectional video of multiple objects whose centroid positions are annotated automatically. Omnidirectional vision is an active field of research focused on the use of spherical imagery in video analysis and scene understanding, involving tasks such as object detection, tracking and recognition. Our goal is to provide a large and consistently annotated video data set that can be used to train and evaluate new algorithms for these tasks. Here we describe the experimental setup and software environment used to capture and map the 3D ground truth positions of multiple objects into the image. Furthermore, we estimate the expected systematic error on the mapped positions. In addition to final data products, we release publicly the software tools and raw data necessary to re-calibrate the camera and/or redo this mapping. The software also provides a simple framework for comparing the results of standard image annotation tools or visual tracking syst

Learning the What and How of Annotation in Video Object Segmentation

Human-machine collaboration on data annotation of images by semi-automatic labeling

Supervised Learning of Semantic Classes for Image Annotation and Retrieval

Toward Interactive Self-Annotation For Video Object Bounding Box: Recurrent Self-Learning And Hierarchical Annotation Based Framework

Semi-Automatic Data Annotation guided by Feature Space Projection

Data annotation using visual inspection (supervision) of each training sample can be laborious. Interactive solutions alleviate this by helping experts propagate labels from a few supervised samples to unlabeled ones based solely on the visual analysis of their feature space projection (with no further sample supervision). We present a semi-automatic data annotation approach based on suitable feature space projection and semi-supervised label estimation. We validate our method on the popular MNIST dataset and on images of human intestinal parasites with and without fecal impurities, a large and diverse dataset that makes classification very hard. We evaluate two approaches for semi-supervised learning from the latent and projection spaces, to choose the one that best reduces user annotation effort and also increases classification accuracy on unseen data. Our results demonstrate the added-value of visual analytics tools that combine complementary abilities of humans and machines for mo

Pseudo Label-based Multi-View Annotation for Semi-Supervised Medical Image Segmentation


## Synthese


L'introduction dresse un panorama des outils d'annotation vidéo récents, dont l'objectif commun est de réduire l'effort humain requis pour produire des vérités terrain à grande échelle tout en améliorant la qualité des annotations, via des méthodes de vision par ordinateur et d'apprentissage automatique ou via des plateformes de crowd-sourcing. Les auteurs identifient les fonctionnalités caractérisant ces outils, telles que la forme des boîtes englobantes, la propagation d'annotations entre images clés par interpolation linéaire ou par suivi (tracking), et la navigation dans les images et les plans vidéo. Ils soulignent que l'objectif ultime de ces outils est de minimiser au maximum la charge d'annotation manuelle, notamment par l'intégration d'algorithmes de détection d'objets supervisée, de mise en correspondance de gabarits (template matching) ou de reconnaissance d'actions, tout en reconnaissant les limites de robustesse et de spécificité de domaine de ces approches. Une comparaison structurée (Tableau 1) des outils existants est proposée selon des critères de conception, d'interaction utilisateur et de fonctionnalités d'annotation de base et avancées. Les données d'évaluation rapportées pour l'outil présenté montrent que les modes semi-automatique et automatique réduisent d'au moins un ordre de grandeur le nombre d'interventions humaines nécessaires par rapport au mode manuel complet, avec des gains additionnels de quelques pourcents selon l'optimisation des paramètres.

Cet article aborde le problème de l'annotation de vérité terrain (ground truth) pour le développement de systèmes de reconnaissance d'images, une tâche qui demeure un obstacle majeur malgré la facilité croissante de collecte de données visuelles. Les auteurs rappellent avoir précédemment proposé une interface utilisateur zoomable pour l'annotation de jeux de données personnalisés, validée sur des données relativement simples comme COIL-100, mais insuffisante pour des images complexes et encombrées telles que celles issues de webcams. Le présent travail étend cet outil afin de simplifier l'annotation de données plus complexes et introduit des concepts avancés de navigation au sein de grands jeux de données. L'accent est mis sur l'utilisabilité instantanée de l'outil, c'est-à-dire l'élimination du besoin de formation ou de tutoriel préalable, afin de lever les réticences initiales à son adoption.

Cet article aborde le problème de l'annotation de vérité terrain (ground truth) pour le développement de systèmes de reconnaissance d'images, une tâche qui demeure un obstacle majeur malgré la facilité croissante de collecte de données visuelles. Les auteurs rappellent avoir précédemment proposé une interface utilisateur zoomable pour l'annotation de jeux de données personnalisés, validée sur des données relativement simples comme COIL-100, mais insuffisante pour des images complexes et encombrées telles que celles issues de webcams. Le présent travail étend cet outil afin de simplifier l'annotation de données plus complexes et introduit des concepts avancés de navigation au sein de grands jeux de données. L'accent est mis sur l'utilisabilité instantanée de l'outil, c'est-à-dire l'élimination du besoin de formation ou de tutoriel préalable, afin de lever les réticences initiales à son adoption. Les auteurs concluent leur présentation d'un outil d'annotation d'images fondé sur l'organisation par similarité via une carte auto-organisatrice (SOM), qui permet à l'utilisateur de sélectionner et d'annoter simultanément de grands ensembles d'images grâce à une interface de navigation précise adaptée à des jeux de données de plusieurs milliers d'images. Conçu pour des utilisateurs non experts, l'outil signale les nœuds regroupant un grand nombre d'images afin d'orienter l'attention vers les sources probables d'erreurs de clustering, tout en restant utilisable par des experts capables d'y intégrer tout type de caractéristique visuelle usuelle sans modification du système. Les auteurs soulignent que l'outil réduit considérablement le temps et l'effort d'annotation, en particulier pour des données peu variables comme les flux de webcams, mais aussi pour des jeux de données hétérogènes. Ils identifient toutefois deux limites actuelles ouvrant sur des travaux futurs : l'absence de recalcul du clustering en cours d'annotation, écartée pour ne pas désorienter l'utilisateur, et l'extension de l'approche à l'annotation d'événements dynamiques, qui nécessitera de nouveaux concepts de visualisation au-delà du principe de regroupement par similarité déjà établi.

L'introduction dresse un panorama des outils d'annotation vidéo récents, dont l'objectif commun est de réduire l'effort humain requis pour produire des vérités terrain à grande échelle tout en améliorant la qualité des annotations, via des méthodes de vision par ordinateur et d'apprentissage automatique ou via des plateformes de crowd-sourcing. Les auteurs identifient les fonctionnalités caractérisant ces outils, telles que la forme des boîtes englobantes, la propagation d'annotations entre images clés par interpolation linéaire ou par suivi (tracking), et la navigation dans les images et les plans vidéo. Ils soulignent que l'objectif ultime de ces outils est de minimiser au maximum la charge d'annotation manuelle, notamment par l'intégration d'algorithmes de détection d'objets supervisée, de mise en correspondance de gabarits (template matching) ou de reconnaissance d'actions, tout en reconnaissant les limites de robustesse et de spécificité de domaine de ces approches. Une comparaison structurée (Tableau 1) des outils existants est proposée selon des critères de conception, d'interaction utilisateur et de fonctionnalités d'annotation de base et avancées. Les données d'évaluation rapportées pour l'outil présenté montrent que les modes semi-automatique et automatique réduisent d'au moins un ordre de grandeur le nombre d'interventions humaines nécessaires par rapport au mode manuel complet, avec des gains additionnels de quelques pourcents selon l'optimisation des paramètres. Les auteurs concluent avec la présentation d'iVAT, un outil d'annotation vidéo interactif intégrant trois modalités (manuelle, semi-automatique et automatique) reposant sur des algorithmes de vision par ordinateur conçus pour un fonctionnement incrémental. L'évaluation quantitative montre que les modes semi-automatique et automatique réduisent le ratio moyen d'interventions humaines d'au moins un ordre de grandeur par rapport au mode manuel, tandis qu'une comparaison avec l'outil de référence ViPER-GT indique une meilleure utilisabilité et un nombre d'interactions requis plus faible pour iVAT. L'outil, développé en C/C++ avec Qt et OpenCV, est présenté comme modulaire et portable, facilitant l'ajout de nouveaux modules de vision et son déploiement sur plateformes mobiles. Les auteurs annoncent comme perspectives l'extension de l'outil à la détection automatique et semi-automatique d'actions, ainsi que l'évaluation de son efficacité sur d'autres domaines d'application.


## Methodologie


L'introduction dresse un panorama des outils d'annotation vidéo récents, dont l'objectif commun est de réduire l'effort humain requis pour produire des vérités terrain à grande échelle tout en améliorant la qualité des annotations, via des méthodes de vision par ordinateur et d'apprentissage automatique ou via des plateformes de crowd-sourcing. Les auteurs identifient les fonctionnalités caractérisant ces outils, telles que la forme des boîtes englobantes, la propagation d'annotations entre images clés par interpolation linéaire ou par suivi (tracking), et la navigation dans les images et les plans vidéo. Ils soulignent que l'objectif ultime de ces outils est de minimiser au maximum la charge d'annotation manuelle, notamment par l'intégration d'algorithmes de détection d'objets supervisée, de mise en correspondance de gabarits (template matching) ou de reconnaissance d'actions, tout en reconnaissant les limites de robustesse et de spécificité de domaine de ces approches. Une comparaison structurée (Tableau 1) des outils existants est proposée selon des critères de conception, d'interaction utilisateur et de fonctionnalités d'annotation de base et avancées. Les données d'évaluation rapportées pour l'outil présenté montrent que les modes semi-automatique et automatique réduisent d'au moins un ordre de grandeur le nombre d'interventions humaines nécessaires par rapport au mode manuel complet, avec des gains additionnels de quelques pourcents selon l'optimisation des paramètres.

Cet article aborde le problème de l'annotation de vérité terrain (ground truth) pour le développement de systèmes de reconnaissance d'images, une tâche qui demeure un obstacle majeur malgré la facilité croissante de collecte de données visuelles. Les auteurs rappellent avoir précédemment proposé une interface utilisateur zoomable pour l'annotation de jeux de données personnalisés, validée sur des données relativement simples comme COIL-100, mais insuffisante pour des images complexes et encombrées telles que celles issues de webcams. Le présent travail étend cet outil afin de simplifier l'annotation de données plus complexes et introduit des concepts avancés de navigation au sein de grands jeux de données. L'accent est mis sur l'utilisabilité instantanée de l'outil, c'est-à-dire l'élimination du besoin de formation ou de tutoriel préalable, afin de lever les réticences initiales à son adoption.


## Raw_Full_Text


Chapter 2. State of the Art on Image Annotation
Approaches
Pros
Cons
Text-Based Approaches for Image Annotation
Text-Based Ap-
proaches
✓May describe the visual content of
images, and also subjective, spatial,
temporal and social dimensions.
✓Description closer to the human
one.
✗Can only process images with sur-
rounding context,
✗Sensitive to the surrounding con-
text,
✗Sensitive to the subjectivity of hu-
man perception,
✗Do not take into account image
content (may be incoherent w.r.t im-
age content).
Content-Based Approaches for Image Annotation
Automatic
Im-
age
Annotation
Approaches
✓Allow processing raw images with-
out any surrounding information.
✓Retrieval is achieved using seman-
tic concepts.
✓These concepts are extracted au-
tomatically from low-level features.
✓Sometimes description is less sub-
jective than textual approaches.
✓Allow to narrow the semantic gap.
✗Sometimes sensitive to image seg-
mentation.
✗Suﬀer from the scalability prob-
lem.
✗Do not allow semantic in

Chapter 2. State of the Art on Image Annotation
Approaches
Pros
Cons
Text-Based Approaches for Image Annotation
Text-Based Ap-
proaches
✓May describe the visual content of
images, and also subjective, spatial,
temporal and social dimensions.
✓Description closer to the human
one.
✗Can only process images with sur-
rounding context,
✗Sensitive to the surrounding con-
text,
✗Sensitive to the subjectivity of hu-
man perception,
✗Do not take into account image
content (may be incoherent w.r.t im-
age content).
Content-Based Approaches for Image Annotation
Automatic
Im-
age
Annotation
Approaches
✓Allow processing raw images with-
out any surrounding information.
✓Retrieval is achieved using seman-
tic concepts.
✓These concepts are extracted au-
tomatically from low-level features.
✓Sometimes description is less sub-
jective than textual approaches.
✓Allow to narrow the semantic gap.
✗Sometimes sensitive to image seg-
mentation.
✗Suﬀer from the scalability prob-
lem.
✗Do not allow semantic in

Chapter 2. State of the Art on Image Annotation
Content-Based approaches 
Image Indexing and Retrieval 
Text-Based approaches 
Content-Based Visual 
information Retrieval 
Content-Based Image 
Annotation 
Traditional Text Based 
Approaches 
Semantic Based 
Approaches 
Knowledge 
Based 
NLP 
Supervised 
Learning 
Unsupervised 
Learning 
Web 
Based 
Relevance 
Feedback 
Iconography 
Semantic Image Annotation 
Automatic Image 
Annotation 
Ontology 
driven 
approaches 
Information 
fusion 
Semi-
Supervised 
Learning 
Figure 2.1: Proposed taxonomy of image indexing and retrieval approaches. The
scope of our work is in blue boxes.
2.2
The Image Annotation Problem
Automatic image annotation can be deﬁned as the process of automatically assigning
a text description (often reduced to a set of semantic keywords) to a digital image
through a computational model (or a computer system). Automatic image annota-
tion is usually used in image retrieval systems in order to index and retrieve images
of

Chapter 2. State of the Art on Image Annotation
Content-Based approaches 
Image Indexing and Retrieval 
Text-Based approaches 
Content-Based Visual 
information Retrieval 
Content-Based Image 
Annotation 
Traditional Text Based 
Approaches 
Semantic Based 
Approaches 
Knowledge 
Based 
NLP 
Supervised 
Learning 
Unsupervised 
Learning 
Web 
Based 
Relevance 
Feedback 
Iconography 
Semantic Image Annotation 
Automatic Image 
Annotation 
Ontology 
driven 
approaches 
Information 
fusion 
Semi-
Supervised 
Learning 
Figure 2.1: Proposed taxonomy of image indexing and retrieval approaches. The
scope of our work is in blue boxes.
2.2
The Image Annotation Problem
Automatic image annotation can be deﬁned as the process of automatically assigning
a text description (often reduced to a set of semantic keywords) to a digital image
through a computational model (or a computer system). Automatic image annota-
tion is usually used in image retrieval systems in order to index and retrieve images
of

terpreta-
tion of images.
✗Do not adapt to the user back-
ground.
Semantic Image
Annotation Ap-
proaches
✓May describe the visual content of
images, and also subjective, spatial,
temporal and social dimensions.
✓Allow processing raw images with-
out any surrounding information.
✓Retrieval is achieved using ab-
stract and semantic concepts.
✓Description less subjective to hu-
man perception.
✓Allow reasoning on image annota-
tion and interpretation.
✓Allow to narrow the semantic gap.
✓Scale well with large databases.
✗Diﬃcult to implement.
✗Not well explored.
✗The reasoning power has not yet
showed its eﬃciency.
✗Ontological reasoning may be sub-
ject to the scalability problem.
Table 2.2: Comparison of the diﬀerent families of approaches for image annotation.
49


## Quote


the segment-based methods generally produces similar results as the video-based methods with less annotated data, meaning that partially annotating videos seems to be a valid strategy

We presented an alternative and efficient way to annotate objects in videos with segmentation masks.

Recordings from each step are automatically processed by exploiting spatial shifts in the depth data to generate the ground truth annotation. The methods requires no object models, only a single depth sensor, to reduce human time for labeling to simple recording and qualitative inspection.

our data set provides ground truth image annotations that have been automatically mapped from 3D object positions measured by a VICON motion capture system... This approach avoids ad hoc error prone human annotation and allows the systematic error on the ground truth image annotations to be estimated.

Semantic Annotation of Image Resources in Digital Humanities

For example we plan to add advanced image processing algorithms to help the user to semi-automatically annotate regions of interest.


## Insight


methodology: Les auteurs proposent une méthode d'annotation de vérité terrain entièrement automatisée, fondée sur la projection de positions 3D mesurées par un système VICON vers des coordonnées image 2D, évitant ainsi le recours à des annotateurs humains sujets à des biais d'évaluation.

efficacy: SAMannot produit des annotations de segmentation d'instances vidéo de haute qualité, comparables à la vérité terrain, sur les benchmarks publics DAVIS et LVOS.