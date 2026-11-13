# Fig. 2. Example of annotation of a surgical wound image with an external fixator on a patient after orthopedic surgery using the CVAT (Computer Vision Annotation Tool) application. It includes areas of the wound itself and surrounding regions important for the study. Zone boundaries are color-coded, and their names are listed on the right.



## Resume


Fig. 2. Example of annotation of a surgical wound image with an external fixator on a patient after orthopedic surgery using the CVAT (Computer Vision Annotation Tool) application. It includes areas of the wound itself and surrounding regions important for the study. Zone boundaries are color-coded, and their names are listed on the right.

IAT - Image Annotation Tool: Manual

The annotation of image and video data of large datasets is a fundamental task in multimedia information retrieval and computer vision applications. In order to support the users during the image and video annotation process, several software tools have been developed to provide them with a graphical environment which helps drawing object contours, handling tracking information and specifying object metadata. Here we introduce a preliminary version of the image annotation tools developed at the Imaging and Vision Laboratory.

A Guide to Annotation of Neurosurgical Intraoperative Video for Machine Learning Analysis and Computer Vision.

Annotating Medical Image Data

Figure 2. CVAT annotation interface

Medical Image Annotation

Data annotation and its evaluation in artificial intelligence-based anatomy recognition for ultrasound-guided regional anesthesia: a clinical perspective.


## Quote


Annotation manuelle via l'outil CVAT (Computer Vision Annotation Tool) : ellipses pour la région du cerveau (incluant le crâne fœtal), rectangles orientés pour le CSP et le LV.

Image annotation and segmentation are core components for computer-aided diagnosis (CAD) and image recognition systems [102]. CAD systems use medical images to identify image features and diagnose lesions [116].

De nombreux outils logiciels gratuits (ImageJ, Fiji, 3D Slicer, ITK-Snap) et outils d'annotation (VGG Image Annotator, MakeSense.AI, CVAT) existent pour faciliter le traitement, la segmentation et l'annotation d'images médicales

The proposed annotation object makes several types of annotation possible, such as freehand sketching and scanned medical documents (Figs. 5 and6).


## Insight


methodology: Le processus d'annotation a combiné des outils standardisés (CVAT) avec des formats géométriques adaptés à chaque structure anatomique : ellipses pour le cerveau et rectangles orientés pour le CSP et les LV.
L'annotation a été réalisée manuellement par un doctorant à l'aide de l'outil CVAT (Computer Vision Annotation Tool), un choix technique qui garantit la reproductibilité et la traçabilité du processus. Le choix de la forme géométrique d'annotation a été adapté à la morphologie de chaque structure : des ellipses ont été utilisées pour délimiter la région cérébrale incluant le crâne fœtal, tandis que des rectangles orientés ont servi à circonscrire le cavum du septum pellucidum et les ventricules latéraux. Ces annotations géométriques primaires ont ensuite été converties en masques par encodage RLE (run length encoding) ainsi qu'en coordonnées de bounding box, permettant une flexibilité d'usage pour différents types de tâches de vision par ordinateur (segmentation, détection). Cette double conversion technique constitue un prérequis essentiel à la diffusion du dataset dans les 11 formats annotés proposés (Cityscapes, YOLO, CVAT, Datumaro, COCO, TFRecord, PASCAL, LabelMe, Segmentation mask, OpenImage, ICDAR).

clinical relevance: L'annotation et la segmentation d'images constituent des composantes essentielles des systèmes de diagnostic assisté par ordinateur (CAD), qui exploitent les images médicales pour identifier des caractéristiques d'image, diagnostiquer des lésions et reconnaître des régions d'intérêt (ROI).

efficacy: Dans les articles d’ophtalmologie recensés, sept logiciels d’annotation distincts étaient utilisés, mais seuls CVAT et ImageJ étaient librement accessibles.

methodology: Les annotations couvrent trois catégories principales sur les radiographies (corps vertébraux L1-L5, disques intervertébraux, matériel chirurgical) et des annotations voxel pour les structures vertébrales sur CT, permettant une évaluation fine des tâches de segmentation.

implications: L'outil d'annotation, adapté aux spécificités des images OCT, prend en charge jusqu'à 20 caractéristiques par coupe et sélectionne automatiquement 3 coupes par volume OCT à annoter, optimisant ainsi le temps expert.
L'outil d'annotation, développé comme un fork du logiciel HUMAN (Hierarchical Universal Modular ANnotator), a été spécifiquement adapté aux particularités des volumes OCT rétiniens, qui se composent de nombreuses coupes successives (B-scans) dont l'annotation exhaustive serait extrêmement chronophage pour les ophtalmologues experts. En prenant en charge jusqu'à 20 caractéristiques anatomiques ou pathologiques différentes par coupe et en sélectionnant automatiquement seulement 3 coupes représentatives par volume OCT pour l'annotation, l'outil réduit considérablement la charge de travail tout en préservant l'information cliniquement pertinente nécessaire à l'entraînement des modèles. Cette approche ciblée s'inscrit directement dans la logique de l'Active Learning, où l'objectif est de maximiser l'information extraite de chaque annotation experte plutôt que de multiplier les annotations exhaustives et redondantes.

interoperability: L'adoption de formats d'annotation d'image standardisés fondés sur l'outil CVAT permet aux laboratoires d'EM d'entraîner des modèles de deep learning sur leurs propres jeux de données annotés, en substituant simplement les données d'entraînement des cas d'usage préexistants.


## Methodologie


L’introduction de l’article « VR-based annotation assistance system for volumetric medical image segmentation » situe le travail dans le domaine de l’imagerie médicale et en présente les enjeux de manière approfondie. Elle examine les principaux formats de fichiers utilisés pour stocker et échanger les images médicales. Elle passe ensuite en revue des exemples de logiciels de réalité virtuelle (VR) dédiés à la visualisation d’images médicales. Enfin, elle décrit les outils couramment proposés dans ces applications, ce qui cadre le besoin d’assistance à l’annotation en environnement VR.

L'essor du deep learning en imagerie médicale a considérablement accru la demande en données annotées de haute qualité, ces annotations (Ground-Truth) étant indispensables à l'entraînement, aux tests et à l'évaluation des modèles de diagnostic assisté par ordinateur (CAD). Les outils d'annotation se répartissent en trois modalités - manuelle, semi-automatique et automatique - et prennent en charge diverses techniques graphiques telles que les polygones, points, lignes, polylignes ou masques dessinés à main levée, appliquées à des tâches allant de la classification d'image à la segmentation au niveau du pixel. Une revue comparative de 13 outils d'annotation d'images médicales, évalués selon sept critères (plateforme, zoom, coût, formats d'entrée/sortie, types d'annotation graphique et méthode d'annotation), montre que malgré leur caractère chronophage et leur coût en ressources humaines expertes, les outils d'annotation manuelle demeurent les plus répandus dans le domaine médical. Les approches semi-automatiques et automatiques, quant à elles, permettraient de réduire le temps et les efforts requis tout en offrant de meilleurs résultats comparativement à l'annotation strictement manuelle.


## Synthese


L’introduction de l’article « VR-based annotation assistance system for volumetric medical image segmentation » situe le travail dans le domaine de l’imagerie médicale et en présente les enjeux de manière approfondie. Elle examine les principaux formats de fichiers utilisés pour stocker et échanger les images médicales. Elle passe ensuite en revue des exemples de logiciels de réalité virtuelle (VR) dédiés à la visualisation d’images médicales. Enfin, elle décrit les outils couramment proposés dans ces applications, ce qui cadre le besoin d’assistance à l’annotation en environnement VR.

L’article présente une version préliminaire d’IAT (Image Annotation Tool), outil d’annotation d’images développé au Imaging and Vision Laboratory. L’objectif principal est d’introduire cette interface et d’en évaluer la qualité d’usage, en vérifiant si le programme répond correctement aux actions et aux besoins des utilisateurs. L’évaluation repose sur une phase de tests d’utilisabilité comprenant des tâches d’annotation de difficulté croissante, suivie d’un questionnaire de 14 énoncés notés sur une échelle de 1 à 5. La population de testeurs inclut des utilisateurs peu ou moyennement expérimentés en informatique ainsi que des utilisateurs experts. Dans l’ensemble, le système s’est révélé intuitif : tous les utilisateurs, sauf un, ont pu atteindre les objectifs proposés, et les fonctionnalités initiales ainsi que l’interface graphique ont été jugées efficaces. Les auteurs présentent IAT comme une première étape vers un outil plus complet, visant notamment l’ajout de fonctionnalités pour simplifier et accélérer le processus d’annotation.

Cette revue systématique évalue les logiciels d’annotation d’images utilisés dans des projets d’intelligence artificielle en ophtalmologie et compare leur praticité pour l’annotation d’images du fond d’œil. Une recherche PubMed réalisée le 8 juillet 2022, complétée par une recherche Google, a permis d’identifier 131 logiciels et plateformes d’annotation. Après application de critères de praticité et évaluation directe des outils (téléchargement ou accès en ligne), dix logiciels ont été retenus. Parmi les logiciels mentionnés dans la littérature ophtalmologique, seuls CVAT et ImageJ étaient librement accessibles. Sur les dix outils inclus, trois étaient exclusivement cloud, cinq étaient des applications de bureau téléchargeables et deux proposaient les deux modalités. Les auteurs présentent ce travail comme la première étude systématisant le recensement, l’évaluation et la comparaison de logiciels d’annotation pour les images de fond d’œil.

L'essor du deep learning en imagerie médicale a considérablement accru la demande en données annotées de haute qualité, ces annotations (Ground-Truth) étant indispensables à l'entraînement, aux tests et à l'évaluation des modèles de diagnostic assisté par ordinateur (CAD). Les outils d'annotation se répartissent en trois modalités - manuelle, semi-automatique et automatique - et prennent en charge diverses techniques graphiques telles que les polygones, points, lignes, polylignes ou masques dessinés à main levée, appliquées à des tâches allant de la classification d'image à la segmentation au niveau du pixel. Une revue comparative de 13 outils d'annotation d'images médicales, évalués selon sept critères (plateforme, zoom, coût, formats d'entrée/sortie, types d'annotation graphique et méthode d'annotation), montre que malgré leur caractère chronophage et leur coût en ressources humaines expertes, les outils d'annotation manuelle demeurent les plus répandus dans le domaine médical. Les approches semi-automatiques et automatiques, quant à elles, permettraient de réduire le temps et les efforts requis tout en offrant de meilleurs résultats comparativement à l'annotation strictement manuelle.


## Raw_Video_Annotation_Tools_Workflows


Computer scientists and engineers design most VATs for computer vision, machine learning, and robotics research and applications [12,35,4,16,7]. However, there are a handful of tools specifically designed for and used by other domains such as film studies [13,44] where VAT allows for character analysis and scene analysis. Journalists use VAT to annotate and synchronize events from multiple sources to present a cohesive story [43]. In sports, teams annotate games and significant events and move to study for their teams [45,46]. While most tools have different focuses, the primary annotation is marking a binary exists or not and a temporal range of events of interest. To this end, events annotation is the foundation that makes further work easier or, in some cases, possible. So it is essential to have accurate annotations. Support for synchronized multi-camera views, micro and macro visualization of events in a timeline, and convenient searching and reviewing video features make FEVA a f

Computer scientists and engineers design most VATs for computer vision, machine learning, and robotics research and applications [12,35,4,16,7]. However, there are a handful of tools specifically designed for and used by other domains such as film studies [13,44] where VAT allows for character analysis and scene analysis. Journalists use VAT to annotate and synchronize events from multiple sources to present a cohesive story [43]. In sports, teams annotate games and significant events and move to study for their teams [45,46]. While most tools have different focuses, the primary annotation is marking a binary exists or not and a temporal range of events of interest. To this end, events annotation is the foundation that makes further work easier or, in some cases, possible. So it is essential to have accurate annotations. Support for synchronized multi-camera views, micro and macro visualization of events in a timeline, and convenient searching and reviewing video features make FEVA a f


## Raw_Full_Text


Chapter 7
Conclusions and Future Research
Directions
Image annotation represents a major economic issue and involves several applications,
including but not limited to: social networks, the Web, medical imaging, biocomput-
ing, remote sensing, news, image and video monitoring and information retrieval.
Recently, many advances have been made to reduce the semantic gap problem, and
to improve automatic image annotation systems. These advances include computer
vision techniques (such as image features, image descriptors, sparse representation,
etc.) and artiﬁcial intelligence (such as machine learning, data clustering, knowledge
engineering, etc.). However, automatic image annotation is still an open issue and
does not seem to be resolved in the next few years. Indeed, current systems for image
annotation face signiﬁcant problems, including the semantic gap, the scalability prob-
lem, the subjectivity of image semantics, the lack of robustness of current computer
vision techniques, and mo

Chapter 7
Conclusions and Future Research
Directions
Image annotation represents a major economic issue and involves several applications,
including but not limited to: social networks, the Web, medical imaging, biocomput-
ing, remote sensing, news, image and video monitoring and information retrieval.
Recently, many advances have been made to reduce the semantic gap problem, and
to improve automatic image annotation systems. These advances include computer
vision techniques (such as image features, image descriptors, sparse representation,
etc.) and artiﬁcial intelligence (such as machine learning, data clustering, knowledge
engineering, etc.). However, automatic image annotation is still an open issue and
does not seem to be resolved in the next few years. Indeed, current systems for image
annotation face signiﬁcant problems, including the semantic gap, the scalability prob-
lem, the subjectivity of image semantics, the lack of robustness of current computer
vision techniques, and mo


## Discussion


Les auteurs concluent avec la présentation d'iVAT, un outil d'annotation vidéo interactif intégrant trois modalités (manuelle, semi-automatique et automatique) reposant sur des algorithmes de vision par ordinateur conçus pour un fonctionnement incrémental. L'évaluation quantitative montre que les modes semi-automatique et automatique réduisent le ratio moyen d'interventions humaines d'au moins un ordre de grandeur par rapport au mode manuel, tandis qu'une comparaison avec l'outil de référence ViPER-GT indique une meilleure utilisabilité et un nombre d'interactions requis plus faible pour iVAT. L'outil, développé en C/C++ avec Qt et OpenCV, est présenté comme modulaire et portable, facilitant l'ajout de nouveaux modules de vision et son déploiement sur plateformes mobiles. Les auteurs annoncent comme perspectives l'extension de l'outil à la détection automatique et semi-automatique d'actions, ainsi que l'évaluation de son efficacité sur d'autres domaines d'application.

Les auteurs situent IAT comme une première étape vers un outil d’annotation d’images plus complet. Ils soulignent l’efficacité des fonctionnalités et de l’interface actuelles, tout en projetant l’ajout de nouvelles capacités pour simplifier et accélérer l’annotation, notamment via des algorithmes de traitement d’image pour une annotation semi-automatique des régions d’intérêt.


## Conclusion


Computer vision is increasingly applied to upper limb orthopaedic imaging, though the field remains in its early stages The 16 included studies demonstrate that automated fracture detection and radiographic measurement are technically achievable, with strong accuracy and reliability Most developed applications lie in wrist fracture detection and postoperative shoulder analysis Widespread clinical implementation is limited by small sample sizes, retrospective design, and lack of prospective testing Future studies must prioritise external validation, transparent reporting, and expansion into MRI- and ultrasound-based soft-tissue and intra-operative applications Real progress will depend on collaboration across clinical, engineering, and regulatory domains