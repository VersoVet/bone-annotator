# Reducing annotation effort in muscle MRI segmentation through cross-anatomy learning



## Resume


Reducing annotation effort in muscle MRI segmentation through cross-anatomy learning

Iterative annotation to ease neural network training: Specialized machine learning in medical image analysis

Assisted annotation in Deep LOGISMOS: Simultaneous multi-compartment 3D MRI segmentation of calf muscles.

<h4>Background</h4>Automated segmentation of individual calf muscle compartments in 3D MR images is gaining importance in diagnosing muscle disease, monitoring its progression, and prediction of the disease course. Although deep convolutional neural networks have ushered in a revolution in medical image segmentation, achieving clinically acceptable results is a challenging task and the availability of sufficiently large annotated datasets still limits their applicability.<h4>Purpose</h4>In this paper, we present a novel approach combing deep learning and graph optimization in the paradigm of assisted annotation for solving general segmentation problems in 3D, 4D, and generally n-D with limited annotation cost.<h4>Methods</h4>Deep LOGISMOS combines deep-learning-based pre-segmentation of objects of interest provided by our convolutional neural network, FilterNet+, and our 3D multi-objects LOGISMOS framework (layered optimal graph image segmentation of multiple objects and surfaces) that

Active learning with noise modeling for medical image annotation

An Annotation Sparsification Strategy for 3D Medical Image Segmentation via Representative Selection and Self-Training

Image segmentation is critical to lots of medical applications. While deep learning (DL) methods continue to improve performance for many medical image segmentation tasks, data annotation is a big bottleneck to DL-based segmentation because (1) DL models tend to need a large amount of labeled data to train, and (2) it is highly time-consuming and label-intensive to voxel-wise label 3D medical images. Significantly reducing annotation effort while attaining good performance of DL segmentation models remains a major challenge. In our preliminary experiments, we observe that, using partially labeled datasets, there is indeed a large performance gap with respect to using fully annotated training datasets. In this paper, we propose a new DL framework for reducing annotation effort and bridging the gap between full annotation and sparse annotation in 3D medical image segmentation. We achieve this by (i) selecting representative slices in 3D images that minimize data redundancy and save annotation effort, and (ii) self-training with pseudo-labels automatically generated from the base-models trained using the selected annotated slices. Extensive experiments using two public datasets (the HVSMR 2016 Challenge dataset and mouse piriform cortex dataset) show that our framework yields competitive segmentation results comparing with state-of-the-art DL methods using less than ∼20% of annotated data.

Region-based Active Learning for Reducing Annotation Effort of ECG Waveform Segmentation

Semantic segmentation with less annotation efforts

Annotating Medical Image Data

An integrated iterative annotation technique for easing neural network training in medical image analysis.

Neural networks promise to bring robust, quantitative analysis to medical fields. However, their adoption is limited by the technicalities of training these networks and the required volume and quality of human-generated annotations. To address this gap in the field of pathology, we have created an intuitive interface for data annotation and the display of neural network predictions within a commonly used digital pathology whole-slide viewer. This strategy used a 'human-in-the-loop' to reduce the annotation burden. We demonstrate that segmentation of human and mouse renal micro compartments is repeatedly improved when humans interact with automatically generated annotations throughout the training process. Finally, to show the adaptability of this technique to other medical imaging fields, we demonstrate its ability to iteratively segment human prostate glands from radiology imaging data.

How to select slices for annotation to train best-performing deep learning segmentation models for cross-sectional medical images?

Automated segmentation of medical images heavily relies on the availability of precise manual annotations. However, generating these annotations is often time-consuming, expensive, and sometimes requires specialized expertise (especially for cross-sectional medical images). Therefore, it is essential to optimize the use of annotation resources to ensure efficiency and effectiveness. In this paper, we systematically address the question: "in a non-interactive annotation pipeline, how should slices from cross-sectional medical images be selected for annotation to maximize the performance of the resulting deep learning segmentation models?" We conducted experiments on 4 medical imaging segmentation tasks with varying annotation budgets, numbers of annotated cases, numbers of annotated slices per volume, slice selection techniques, and mask interpolations. We found that:   1) It is almost always preferable to annotate fewer slices per volume and more volumes given an annotation budget. 2)

A Semi-Automatic Magnetic Resonance Imaging Annotation Algorithm Based on Semi-Weakly Supervised Learning.

The annotation of magnetic resonance imaging (MRI) images plays an important role in deep learning-based MRI segmentation tasks. Semi-automatic annotation algorithms are helpful for improving the efficiency and reducing the difficulty of MRI image annotation. However, the existing semi-automatic annotation algorithms based on deep learning have poor pre-annotation performance in the case of insufficient segmentation labels. In this paper, we propose a semi-automatic MRI annotation algorithm based on semi-weakly supervised learning. In order to achieve a better pre-annotation performance in the case of insufficient segmentation labels, semi-supervised and weakly supervised learning were introduced, and a semi-weakly supervised learning segmentation algorithm based on sparse labels was proposed. In addition, in order to improve the contribution rate of a single segmentation label to the performance of the pre-annotation model, an iterative annotation strategy based on active learning was

An annotation tool for dermoscopic image segmentation

Few Slices Suffice: Multi-faceted Consistency Learning with Active Cross-Annotation for Barely-Supervised 3D Medical Image Segmentation

Light mixed‐supervised segmentation for 3D medical image data

Abstract
                  
                    Background
                    Accurate 3D semantic segmentation models are essential for many clinical applications. To train a model for 3D segmentation, voxel‐level annotation is necessary, which is expensive to obtain due to laborious work and privacy protection. To accurately annotate 3D medical data, such as MRI, a common practice is to annotate the volumetric data in a slice‐by‐slice contouring way along principal axes.
                  
                  
                    Purpose
                    In order to reduce the annotation effort in slices, weakly supervised learning with a bounding box (Bbox) was proposed to leverage the discriminating information via a tightness prior assumption. Nevertheless, this method requests accurate and tight Bboxes, which will significantly drop the performance when tightness is not held, that is when a relaxed Bbox is applied. Therefore, there is a need to train a stable model based on relaxed Bbox annotation.
                  
                  
                    Methods
                    This paper presents a mixed‐supervised training strategy to reduce the annotation effort for 3D segmentation tasks. In the proposed approach, a fully annotated contour is only required for a single slice of the volume. In contrast, the rest of the slices with targets are annotated with relaxed Bboxes. This mixed‐supervised method adopts fully supervised learning, relaxed Bbox prior, and contrastive learning during the training, which ensures the network exploits the discriminative information of the training volumes properly. The proposed method was evaluated on two public 3D medical imaging datasets (MRI prostate dataset and Vestibular Schwannoma [VS] dataset).
                  
                  
                    Results
                    The proposed method obtained a high segmentation Dice score of 85.3% on an MRI prostate dataset and 83.3% on a VS dataset with relaxed Bbox annotation, which are close to a fully supervised model. Moreover, with the same relaxed Bbox annotations, the proposed method outperforms the state‐of‐the‐art methods. More importantly, the model performance is stable when the accuracy of Bbox annotation varies.
                  
                  
                    Conclusions
                    The presented study proposes a method based on a mixed‐supervised learning method in 3D medical imaging. The benefit will be stable segmentation of the target in 3D images with low accurate annotation requirement, which leads to easier model training on large‐scale datasets.

Efficient musculoskeletal annotation using free-form deformation.

Traditionally, constructing training datasets for automatic muscle segmentation from medical images involved skilled operators, leading to high labor costs and limited scalability. To address this issue, we developed a tool that enables efficient annotation by non-experts and assessed its effectiveness for training an automatic segmentation network. Our system allows users to deform a template three-dimensional (3D) anatomical model to fit a target magnetic-resonance image using free-form deformation with independent control points for axial, sagittal, and coronal directions. This method simplifies the annotation process by allowing non-experts to intuitively adjust the model, enabling simultaneous annotation of all muscles in the template. We evaluated the quality of the tool-assisted segmentation performed by non-experts, which achieved a Dice coefficient greater than 0.75 compared to expert segmentation, without significant errors such as mislabeling adjacent muscles or omitting mus

Learning with Limited Annotations: A Survey on Deep Semi-Supervised Learning for Medical Image Segmentation

Weakly Supervised Cell Segmentation by Point Annotation.

We propose weakly supervised training schemes to train end-to-end cell segmentation networks that only require a single point annotation per cell as the training label and generate a high-quality segmentation mask close to those fully supervised methods using mask annotation on cells. Three training schemes are investigated to train cell segmentation networks, using the point annotation. First, self-training is performed to learn additional information near the annotated points. Next, co-training is applied to learn more cell regions using multiple networks that supervise each other. Finally, a hybrid-training scheme is proposed to leverage the advantages of both self-training and co-training. During the training process, we propose a divergence loss to avoid the overfitting and a consistency loss to enforce the consensus among multiple co-trained networks. Furthermore, we propose weakly supervised learning with human in the loop, aiming at achieving high segmentation accuracy and anno

HAL-IA: A Hybrid Active Learning framework using Interactive Annotation for medical image segmentation

Impact on Cost and Expert Time of Data-Efficient Deep Learning for Medical Image Segmentation.

A deep learning–based expert-guided annotation loop reduced annotation time and estimated cost while generating high-quality reference standard CT and MRI segmentations and was feasible to implement in a clinical environment without coding.

Active Learning in Brain Tumor Segmentation with Uncertainty Sampling and Annotation Redundancy Restriction.

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


## Quote


Les expériences démontrent que l'Active Learning peut significativement réduire l'effort d'annotation dans le cas d'usage d'imagerie cutanée

Annotation-Efficient Deep Learning for Medical Imaging

Annotation-Efficient Deep Learning for Medical Imaging


## Conclusion


AL can be successfully applied onto medical imaging to reduce the annotation burden through our experiments on brain tumor segmentation an AL framework using Bayesian approximation with dropout at training and testing only needs approximately 30% of the data that a random query strategy would need to achieve full data performance dropout is generalizable to AL in 3D segmentation tasks and in fact superior to bootstrapping a dropout uncertainty estimation framework is optimal the contributions of our study are quantifying the efficacy of multiple AL techniques and showing the impact of combining various uncertainty estimation and annotation redundancy restriction methods


## Discussion


Cette étude propose trois approches de segmentation cellulaire faiblement supervisée reposant uniquement sur des annotations par point : l'auto-apprentissage (self-training), le co-apprentissage (co-training) et une approche hybride combinant les deux. Une perte de divergence et une perte de cohérence sont introduites afin de prévenir le surapprentissage, de stabiliser le processus d'entraînement et de maintenir le consensus entre plusieurs réseaux co-entraînés. Les auteurs intègrent également une supervision faible avec intervention humaine dans la boucle (human-in-the-loop), visant un apprentissage profond efficace en termes d'annotation pour une segmentation cellulaire précise. La validation sur deux jeux de données de référence publics montre que cette approche atteint des performances de segmentation proches de celles des méthodes entièrement supervisées, tout en réduisant considérablement l'effort d'annotation humaine requis.


## Synthese


Cet article présente ADA-SAM, un modèle de segmentation d'images médicales conçu pour réduire la dépendance aux grands ensembles de données annotées manuellement. La méthode repose sur un cadre d'apprentissage multitâche semi-supervisé combinant une branche de segmentation basée sur Segment Anything Model (SAM), guidée par des cartes d'activation de classe issues d'un classificateur auxiliaire, avec un mécanisme de rétroaction par gradient et une adaptation par LoRA, permettant un auto-prompting et une auto-correction sans intervention manuelle. Le modèle a été évalué sur un jeu de données de 21 séquences IRM Turbo Spin Echo des muscles vastus lateralis et vastus medialis, avec une évaluation qualitative innovante impliquant experts et modèles de langage. En configuration semi-supervisée, ADA-SAM surpasse les modèles de référence à tous les niveaux d'annotation testés, atteignant un DSC de 0,91 avec seulement 5 coupes labellisées, tout en offrant une inférence plus rapide et un nombre de paramètres réduit par rapport à SAM-Mix. Les auteurs concluent qu'ADA-SAM constitue une approche efficiente en annotations pour la segmentation musculaire à partir d'IRM, avec un potentiel d'adoption clinique, et prévoient d'étendre sa validation à des données multimodales.

Cette présentation invitée propose un aperçu des approches d’apprentissage profond efficient en annotations pour la segmentation d’images médicales. L’objectif est de présenter des méthodes permettant de réduire le besoin d’annotations manuelles coûteuses, notamment via l’exploitation d’images médicales synthétiques. Trois travaux récents sont exposés : un apprentissage faiblement supervisé s’appuyant sur des informations extraites de comptes rendus radiologiques, un entraînement au moment du test de type synthetic-to-real pour l’adaptation de domaine non supervisée sans accès aux données sources, et une synthèse d’images guidée par pseudo-étiquettes pour l’apprentissage semi-supervisé. La présentation s’inscrit dans une perspective plus large visant à progresser vers une segmentation d’images médicales sans annotations. Il s’agit d’une contribution de synthèse et de cadrage plutôt que d’une étude expérimentale unique.

Cette revue examine les solutions d’apprentissage profond conçues pour atténuer deux limitations majeures des jeux de données de segmentation d’images médicales : la rareté des annotations et leur faible qualité ou granularité. Malgré les progrès des architectures de segmentation, notamment dans les connexions résiduelles, les mécanismes d’attention et les modules hybrides, leurs performances demeurent fortement dépendantes de jeux de données annotés volumineux et fiables. Les approches recensées contre la rareté des annotations comprennent des méthodes semi-automatisées, telles que l’apprentissage actif et la segmentation interactive, ainsi que des méthodes automatisées exploitant des données non annotées, synthétiques ou issues de domaines similaires. La revue couvre également les stratégies adaptées aux annotations clairsemées, bruitées ou limitées au niveau de l’image, tout en soulignant que ces imperfections peuvent compromettre la généralisation en contexte clinique réel [Unknown](zotero://select/library/items/ZRSWCZE4).