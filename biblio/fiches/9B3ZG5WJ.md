# Anatomical Landmark Localization for Knee X-ray Images via Heatmap Regression Refined with Graph Convolutional Network



## Resume


Anatomical Landmark Localization for Knee X-ray Images via Heatmap Regression Refined with Graph Convolutional Network

Multi-Scale Heatmap Regression with Structural Prior and Graph-Aware Refinement for Robust Cephalometric Landmark Localization

Optimization and Benchmarking of Image Segmentation for Improved Landmark Detection in Lower Limb X-Rays and Accurate Coronal Plane Alignment of the Knee Classification

Subpixel Heatmap Regression for Facial Landmark Localization

Bone anatomical landmark localization with cascaded spatial configuration network

<jats:title>Abstract</jats:title>
                  Accurate localization of bone anatomical landmarks in medical images is of great significance for decision-making in surgical plans and orthopedic surgery visual navigation systems development. However, due to the high dimensionality and large size of medical images, current automatic anatomical landmarks detection methods still have issues in terms of accuracy, robustness, and efficiency. To improve the accuracy of bone anatomical landmark detection in medical images, a new network model with a two-step strategy (coarse localizing and fine localizing) was proposed in this study. By combining fully convolutional neural networks and the heatmap regression model, a cascaded spatial configuration network was designed to combine the global and local features of 3D image features and localize anatomical landmarks stepwise. The model was evaluated with a collected knee CT image dataset and a published spine CT image dataset. The results wer

A Light-Weighted Network for Facial Landmark Detection via Combined Heatmap and Coordinate Regression

Enhanced Cephalometric Landmark Detection Using Multi-scale Feature Learning and Heatmap Regression

Heatmap-Based Active Shape Model for Landmark Detection in Lumbar X-ray Images.

Medical staff inspect lumbar X-ray images to diagnose lumbar spine diseases, and the analysis process is currently automated using deep-learning techniques. The detection of landmarks is necessary in the automatic process of localizing the position and identifying the morphological features of the vertebrae. However, detection errors may occur owing to the noise and ambiguity of images, as well as individual variations in the shape of the lumbar vertebrae. This study proposes a method to improve the robustness of landmark detection results. This method assumes that landmarks are detected by a convolutional neural network-based two-step model consisting of Pose-Net and M-Net. The model generates a heatmap response to indicate the probable landmark positions. The proposed method then corrects the landmark positions using the heatmap response and active shape model, which employs statistical information on the landmark distribution. Experiments were conducted using 3600 lumbar X-ray image

Optimization and benchmarking of image segmentation for improved landmark detection in lower limb X-rays and accurate coronal plane alignment of the knee classification_supp1-3572342.pdf

Integrating spatial configuration into heatmap regression based CNNs for landmark localization

Segmentation-Guided Coordinate Regression for Robust Landmark Detection on X-Rays: Application to Automated Assessment of Lower Limb Alignment

Segmentation-guided coordinate regression for robust landmark detection on X-rays: application to automated assessment of lower limb alignment_supp1-3394895.pdf

Automatic assessment of lower limb deformities using high-resolution X-ray images.

<h4>Background</h4>Planning an osteotomy or arthroplasty surgery on a lower limb requires prior classification/identification of its deformities. The detection of skeletal landmarks and the calculation of angles required to identify the deformities are traditionally done manually, with measurement accuracy relying considerably on the experience of the individual doing the measurements. We propose a novel, image pyramid-based approach to skeletal landmark detection.<h4>Methods</h4>The proposed approach uses a Convolutional Neural Network (CNN) that receives the raw X-ray image as input and produces the coordinates of the landmarks. The landmark estimations are modified iteratively via the error feedback method to come closer to the target. Our clinically produced full-leg X-Rays dataset is made publically available and used to train and test the network. Angular quantities are calculated based on detected landmarks. Angles are then classified as lower than normal, normal or higher than

Vision Multi-Hop Integration Graph Convolutional Network for X-Ray Landmark Detection

Feature Aggregation and Refinement Network for 2D Anatomical Landmark Detection

Segmentation of Bone Structure in X-ray Images using Convolutional Neural Network

Automated anatomical landmark detection ondistal femur surface using convolutional neural network

Landmark Detection in Cardiac MRI by Using a Convolutional Neural                     Network

Think About Boundary: Fusing Multi-level Boundary Information for Landmark Heatmap Regression

Learn Fine-Grained Adaptive Loss for Multiple Anatomical Landmark Detection in Medical Images.

Automatic and accurate detection of anatomical landmarks is an essential operation in medical image analysis with a multitude of applications. Recent deep learning methods have improved results by directly encoding the appearance of the captured anatomy with the likelihood maps (i.e., heatmaps). However, most current solutions overlook another essence of heatmap regression, the objective metric for regressing target heatmaps and rely on hand-crafted heuristics to set the target precision, thus being usually cumbersome and task-specific. In this paper, we propose a novel learning-to-learn framework for landmark detection to optimize the neural network and the target precision simultaneously. The pivot of this work is to leverage the reinforcement learning (RL) framework to search objective metrics for regressing multiple heatmaps dynamically during the training process, thus avoiding setting problem-specific target precision. We also introduce an early-stop strategy for active terminati


## Synthese


Cette étude rétrospective monocentrique vise à développer et évaluer une méthode de localisation de repères anatomiques par réseau de neurones convolutif (CNN), fondée sur des cartes de chaleur (heatmaps), pour quantifier automatiquement l'alignement des membres inférieurs chez l'enfant à partir de l'angle hanche-genou-cheville (HKAA). Ce dernier, défini comme l'angle aigu entre l'axe mécanique fémoral et l'axe mécanique tibial, repose sur la localisation précise de trois centres anatomiques (tête fémorale, épine tibiale, plafond tibial), une tâche manuelle chronophage et sujette à la variabilité inter-observateur que les auteurs proposent d'automatiser. Sur une cohorte de 528 patients avec repères annotés manuellement comme référence, le modèle développé a démontré une faible proportion de valeurs aberrantes (1,1 %) et une erreur absolue moyenne de prédiction de l'HKAA de 0,94° ± 0,84°, avec une corrélation intraclasse de 0,974 par rapport à l'annotation humaine. Le modèle s'est en outre montré robuste face à des radiographies présentant des déformations squelettiques sévères ou du matériel métallique occlusif, deux facteurs confondants pourtant présents dans une part substantielle de la base de données.

Les auteurs situent leur outil landmarker dans le paysage des méthodes de localisation de landmarks anatomiques, qui se répartissent principalement entre régression de coordonnées et régression de heatmap, cette dernière ayant progressivement dominé le champ en raison de performances supérieures. Ils distinguent les approches de heatmap régression directe (statique ou adaptative, avec des paramètres de distribution fixes ou appris) des méthodes récentes fondées sur des réseaux entièrement convolutifs couplés à des opérations de décodage différentiables telles que le soft-argmax, certaines intégrant des fonctions de perte tenant compte de l'incertitude de l'annotation. Dans le domaine médical spécifiquement, les approches en deux étapes (localisation grossière puis raffinement sur un patch haute résolution) ainsi que les méthodes fondées sur la segmentation de structures anatomiques sont couramment employées. Les auteurs soulignent que les outils généralistes existants, tels qu'OpenPose ou MMPose, conçus pour l'estimation de pose humaine, ne couvrent pas l'ensemble des méthodes de génération et de décodage de heatmap, la quantification d'incertitude, ni les prétraitements spécifiques à l'imagerie médicale, ce qui justifie le développement d'un outil dédié, modulaire et évalué quantitativement sur deux benchmarks (2D et 3D) où il surpasse les approches de référence de la littérature.


## Methodologie


Cette étude rétrospective monocentrique vise à développer et évaluer une méthode de localisation de repères anatomiques par réseau de neurones convolutif (CNN), fondée sur des cartes de chaleur (heatmaps), pour quantifier automatiquement l'alignement des membres inférieurs chez l'enfant à partir de l'angle hanche-genou-cheville (HKAA). Ce dernier, défini comme l'angle aigu entre l'axe mécanique fémoral et l'axe mécanique tibial, repose sur la localisation précise de trois centres anatomiques (tête fémorale, épine tibiale, plafond tibial), une tâche manuelle chronophage et sujette à la variabilité inter-observateur que les auteurs proposent d'automatiser. Sur une cohorte de 528 patients avec repères annotés manuellement comme référence, le modèle développé a démontré une faible proportion de valeurs aberrantes (1,1 %) et une erreur absolue moyenne de prédiction de l'HKAA de 0,94° ± 0,84°, avec une corrélation intraclasse de 0,974 par rapport à l'annotation humaine. Le modèle s'est en outre montré robuste face à des radiographies présentant des déformations squelettiques sévères ou du matériel métallique occlusif, deux facteurs confondants pourtant présents dans une part substantielle de la base de données.

Les auteurs situent leur outil landmarker dans le paysage des méthodes de localisation de landmarks anatomiques, qui se répartissent principalement entre régression de coordonnées et régression de heatmap, cette dernière ayant progressivement dominé le champ en raison de performances supérieures. Ils distinguent les approches de heatmap régression directe (statique ou adaptative, avec des paramètres de distribution fixes ou appris) des méthodes récentes fondées sur des réseaux entièrement convolutifs couplés à des opérations de décodage différentiables telles que le soft-argmax, certaines intégrant des fonctions de perte tenant compte de l'incertitude de l'annotation. Dans le domaine médical spécifiquement, les approches en deux étapes (localisation grossière puis raffinement sur un patch haute résolution) ainsi que les méthodes fondées sur la segmentation de structures anatomiques sont couramment employées. Les auteurs soulignent que les outils généralistes existants, tels qu'OpenPose ou MMPose, conçus pour l'estimation de pose humaine, ne couvrent pas l'ensemble des méthodes de génération et de décodage de heatmap, la quantification d'incertitude, ni les prétraitements spécifiques à l'imagerie médicale, ce qui justifie le développement d'un outil dédié, modulaire et évalué quantitativement sur deux benchmarks (2D et 3D) où il surpasse les approches de référence de la littérature.


## Conclusion


Incorporating spatial configuration into a CNN-based heatmap regression architecture (SCN) achieves high landmark localization performance even with limited training datasets. The SCN outperforms state-of-the-art approaches across four size-limited 2D and 3D datasets of different anatomical structures (hand MRI, spine CT, skull radiographs, hand radiographs), demonstrating generic applicability. Even with training limited to as few as 10 images (2DHandReduced), the proposed network achieves results comparable to the state-of-the-art evaluated on the full dataset. By simultaneously and end-to-end optimizing local appearance and spatial configuration components, the landmark localization problem is separated into two simpler subproblems that can be learned from small amounts of training data. The local appearance component learns locally accurate candidate predictions while the spatial configuration component focuses on eliminating ambiguities, improving robustness to misidentification without needing local accuracy. The adapted Localization U-Net achieves competitive localization performance but is not state-of-the-art in robustness towards landmark misidentification, since it lacks prior knowledge of spatial configuration constraints among landmarks. On 2DHandFull, 3DHand, 2DSkull and 3DSpine datasets, SCN outperforms previous random forest based methods, CNN-based preliminary results, and other state-of-the-art/challenge-winning and highly tailored methods, without requiring complex or tailored implementations or postprocessing.