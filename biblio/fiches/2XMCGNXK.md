# SLAM – A thin-client for interoperable annotation and biomedical signal handling



## Resume


SLAM – A thin-client for interoperable annotation and biomedical signal handling

Designing artificial intelligence tools dedicated to biosignal data (e.g. electroencephalography, EEG) analysis is an increasingly considered topic, motivated by clinical needs. In this context, data annotation is a crucial task, as a prerequisite to supervised machine learning / deep learning approaches. However, annotation is a tedious, time consuming and error-prone task, that has generally to be carried out in a limited time by clinicians. Based on these considerations, we propose a software tool dedicated to a clinical use, that aims to tackle the main difficulties encountered by clinicians. It is designed as a thin-client, that can be run on a web interface without requiring complex technical dependencies. It allows user-friendly, interactive visualization and annotation, while minimizing the manual interactions. It relies on an extensible data exchange format specifically tailored for storing biosignal data, associated metadata and annotations. A semantic web paradigm is conside

PyMIC: A deep learning toolkit for annotation-efficient medical image segmentation

SLIP: Segmentation with Low-latency Interactive Prompting for 3D Medical Images

Slim: interoperable slide microscopy viewer and annotation tool for imaging data science and computational pathology

The exchange of large and complex slide microscopy imaging data in biomedical research and pathology practice is impeded by a lack of data standardization and interoperability, which is detrimental to the reproducibility of scientific findings and clinical integration of technological innovations. Slim is an open-source, web-based slide microscopy viewer that implements the internationally accepted Digital Imaging and Communications in Medicine (DICOM) standard to achieve interoperability with a multitude of existing medical imaging systems. We showcase the capabilities of Slim as the slide microscopy viewer of the NCI Imaging Data Commons and demonstrate how the viewer enables interactive visualization of traditional brightfield microscopy and highly-multiplexed immunofluorescence microscopy images from The Cancer Genome Atlas and Human Tissue Atlas Network, respectively, using standard DICOMweb services. We further show how Slim enables the collection of standardized image annotation

HAL-IA: A Hybrid Active Learning framework using Interactive Annotation for medical image segmentation

Active learning with applications in biomedical document annotation

Annotating Medical Image Data

An annotation tool for dermoscopic image segmentation

Towards a better understanding of annotation tools for medical imaging: a survey

Active learning with noise modeling for medical image annotation

Learning with Limited Annotations: A Survey on Deep Semi-Supervised Learning for Medical Image Segmentation

LR-COBRAS: A logic reasoning-driven interactive medical image data annotation algorithm

SAM & SAM 2 in 3D Slicer: SegmentWithSAM Extension for Annotating Medical Images

Accelerating Volumetric Medical Image Annotation via Short-Long Memory SAM 2.

Manual annotation of volumetric medical images, such as magnetic resonance imaging (MRI) and computed tomography (CT), is a labor-intensive and time-consuming process. Recent advancements in foundation models for video object segmentation, such as Segment Anything Model 2 (SAM 2), offer a potential opportunity to significantly speed up the annotation process by manually annotating one or a few slices and then propagating target masks across the entire volume. However, the performance of SAM 2 in this context varies. Our experiments show that relying on a single memory bank and attention module is prone to error propagation, particularly at boundary regions where the target is present in the previous slice but absent in the current one. To address this problem, we propose Short-Long Memory SAM 2 (SLM-SAM 2), a novel architecture that integrates distinct short-term and long-term memory banks with separate attention modules to improve segmentation accuracy. We evaluate SLM-SAM 2 on four p

Deep Learning and Data Labeling for Medical Applications


## Conclusion


SLIP is an end-to-end framework for interactive 3D medical image segmentation that decouples image encoding from prompt-guided refinement through a lightweight patch memory bank, substantially reducing interaction latency while supporting reversible prompting. An extensive simulated evaluation across 13 public datasets spanning diverse anatomical structures and imaging modalities demonstrated the robustness and generalizability of the proposed framework. SLIP achieved state-of-the-art interactive segmentation performance while substantially reducing interaction latency compared with existing methods. Although nnInteractive achieved stronger performance during the earliest refinement stages and on the MRI Uterus task, SLIP maintained responsiveness over prolonged interaction sequences and achieved higher final segmentation accuracy on the majority of the evaluated datasets. The prospective user study showed that although nnInteractive achieved superior performance for the MRI Uterus task, participants consistently preferred low-latency interaction, iterative refinement, and reversible prompting, and SLIP achieved higher overall user preference. Practical annotation efficiency depends not only on segmentation accuracy, but also on the quality of the interaction workflow; low-latency interaction and reversible prompting enabled users to efficiently recover from intermediate interaction errors while preserving annotation progress during challenging cases. The decoupled architecture provides a practical pathway for exploiting future advances in medical vision foundation models by retraining or fine-tuning only the lightweight prompt-guided refinement module rather than the entire framework. Interactive segmentation systems should be evaluated not only by segmentation accuracy, but also by how effectively they support efficient and flexible human interaction through complementary large-scale simulated benchmarks and prospective user studies.


## Discussion


La conclusion de l'article présente SLIP, un cadre d'apprentissage de bout en bout pour la segmentation interactive d'images médicales 3D, qui découple l'encodage de l'image du raffinement guidé par prompts grâce à une banque de mémoire de patchs légère, réduisant ainsi substantiellement la latence d'interaction tout en supportant un prompting réversible. Une évaluation simulée à grande échelle sur 13 jeux de données publics couvrant diverses structures anatomiques et modalités d'imagerie a démontré des performances de segmentation interactive de pointe, SLIP surpassant nnInteractive sur la majorité des jeux de données évalués malgré une performance initiale plus faible et des résultats inférieurs sur la tâche IRM Utérus. Une étude prospective utilisateur (N=6) complémentaire a montré que SLIP et nnInteractive réduisent tous deux significativement le temps d'annotation par rapport à la segmentation manuelle, avec des réductions comparables pour les tâches de lésion hépatique en échographie et en tomodensitométrie, tandis que nnInteractive conserve un avantage net sur la tâche IRM Utérus en raison d'un besoin accru de corrections utilisateur pour SLIP. Les auteurs soulignent néanmoins que les participants ont globalement préféré l'interaction à faible latence, le raffinement itératif et le prompting réversible offerts par SLIP, suggérant que l'efficacité pratique de l'annotation dépend autant de la qualité du flux d'interaction que de la précision de segmentation. Plusieurs limites méthodologiques sont reconnues, notamment l'ambiguïté inhérente au prompting ponctuel en début d'interaction, les contraintes mémoire liées au stockage des embeddings de patchs pour les très grands volumes, et la difficulté de comparaison architecturale directe avec des méthodes comme nnInteractive dont le pipeline d'entraînement n'est pas public.


## Insight


deployment: Pour surmonter les limites de l'interface officielle de SAM2, qui ne prend en charge que des formats de données restreints, les auteurs ont développé un plugin pour 3D Slicer permettant l'annotation de données médicales 3D (CT, IRM, TEP) ainsi qu'une interface Gradio dédiée à la segmentation vidéo médicale.

efficacy / annotation workflow: Des études utilisateurs employant un pipeline itératif human-in-the-loop pour l'annotation de lésions CT, de lésions hépatiques en IRM et de frames vidéo d'échocardiographie montrent que MedSAM2 réduit progressivement le temps d'annotation à chaque cycle de fine-tuning, facilitant ainsi la création de jeux de données médicaux à grande échelle.


## Raw_Introduction


Recent literature has suggested that SAM holds a lot of promise for annotating medical imaging datasets using sparse annotations [2,5,6,[15][16][17]. However, current approaches are limited to the evaluation of SAM in simulated settings as opposed to a realistic crowd-sourced setting and have yet to evaluate the effectiveness of SAMgenerated annotations for training DL segmentation models. The purpose of this study is to 1) evaluate SAM for crowd-sourcing annotations for medical imaging datasets from non-expert annotators, and 2) investigate the feasibility of using SAM-generated annotations for training 3D DL segmentation models.

Recent literature has suggested that SAM holds a lot of promise for annotating medical imaging datasets using sparse annotations [2,5,6,[15][16][17]. However, current approaches are limited to the evaluation of SAM in simulated settings as opposed to a realistic crowd-sourced setting and have yet to evaluate the effectiveness of SAMgenerated annotations for training DL segmentation models. The purpose of this study is to 1) evaluate SAM for crowd-sourcing annotations for medical imaging datasets from non-expert annotators, and 2) investigate the feasibility of using SAM-generated annotations for training 3D DL segmentation models.


## Quote


this paper proposes ILM-ASSL for domain-adaptive semantic segmentation. It learns massive unlabeled data semi-supervised to improve the accuracy in the target domain and provides an accurate selection model for active learning. Then, combined with the predictive uncertainty sample selection strategy of active learning, manual intervention is used to correct the pseudo-labels.

Annotation-Efficient Deep Learning for Medical Imaging

Annotation-Efficient Deep Learning for Medical Imaging

we present several user cases of PyMIC for 2D and 3D medical image segmentation with full annotations, partial annotations, weak annotations and noisy annotations, respectively

The purpose of this study is to 1) evaluate SAM for crowd-sourcing annotations for medical imaging datasets from non-expert annotators, and 2) investigate the feasibility of using SAM-generated annotations for training 3D DL segmentation models.


## Raw_Crowd-Sourcing_Sparse_Annotations


We implemented a pipeline for crowd-sourcing annotations with SAM for the purpose of training 3D DL segmentation models (Figure 2). Since the volumes are provided in the NIfTI format, we used med2image (version 2.6.6) to convert a NIfTI volume into PNG images for each slice. The PNG format was chosen as it is a lossless standard format for image analysis in computer vision. We used the Open-Labeling tool (version 1.3) to annotate the organs of interest for each slice within a volume [4]. Bounding boxes were Figure 2. Pipeline for crowd-sourcing sparse annotations from non-expert annotators for the purpose of training 3D DL segmentation models using SAM-generated annotations. Suppose there is an unannotated medical imaging dataset. Sparse annotations for objects of interest (e.g., organs, tumors, etc.) can be crowd-sourced from non-expert annotators. Then, segmentation masks for the objects of interest can be generated using SAM. Finally, the SAM-generated annotations can be used to tra

We implemented a pipeline for crowd-sourcing annotations with SAM for the purpose of training 3D DL segmentation models (Figure 2). Since the volumes are provided in the NIfTI format, we used med2image (version 2.6.6) to convert a NIfTI volume into PNG images for each slice. The PNG format was chosen as it is a lossless standard format for image analysis in computer vision. We used the Open-Labeling tool (version 1.3) to annotate the organs of interest for each slice within a volume [4]. Bounding boxes were Figure 2. Pipeline for crowd-sourcing sparse annotations from non-expert annotators for the purpose of training 3D DL segmentation models using SAM-generated annotations. Suppose there is an unannotated medical imaging dataset. Sparse annotations for objects of interest (e.g., organs, tumors, etc.) can be crowd-sourced from non-expert annotators. Then, segmentation masks for the objects of interest can be generated using SAM. Finally, the SAM-generated annotations can be used to tra


## Methodologie


Cette étude porte sur la segmentation sémantique interactive appliquée à l'IRM cérébrale de patients atteints de glioblastome, un contexte où les méthodes d'apprentissage automatique supervisé, bien que performantes, sont limitées par la rareté des corpus annotés en imagerie médicale. Les auteurs proposent un cadre itératif dans lequel un classifieur est entraîné à partir d'un faible nombre de pixels annotés par un utilisateur expert, les prédictions intermédiaires étant présentées à ce dernier afin qu'il affine la segmentation par des annotations supplémentaires jusqu'à satisfaction. Ce travail se positionne par rapport à des approches antérieures fondées sur les contours actifs (Top et al.) ou sur les superpixels couplés à une mesure d'incertitude géométrique en plan oblique (Konyushkova et al.), ces derniers ayant également travaillé sur des données IRM de glioblastome mais dans un cadre d'annotation binaire, contrairement à l'approche multiclasse développée ici. Sur le plan méthodologique, cinq modes d'interaction combinant incertitude du classifieur et connaissance experte de la segmentation correcte sont comparés dans cette tâche de segmentation multi-tissus. La méthode MISCLASS-B se révèle globalement la plus performante, avec des différences statistiquement significatives (p < 0,001) entre certaines paires de méthodes après 20 cycles d'interaction.


## Synthese


Cette étude porte sur la segmentation sémantique interactive appliquée à l'IRM cérébrale de patients atteints de glioblastome, un contexte où les méthodes d'apprentissage automatique supervisé, bien que performantes, sont limitées par la rareté des corpus annotés en imagerie médicale. Les auteurs proposent un cadre itératif dans lequel un classifieur est entraîné à partir d'un faible nombre de pixels annotés par un utilisateur expert, les prédictions intermédiaires étant présentées à ce dernier afin qu'il affine la segmentation par des annotations supplémentaires jusqu'à satisfaction. Ce travail se positionne par rapport à des approches antérieures fondées sur les contours actifs (Top et al.) ou sur les superpixels couplés à une mesure d'incertitude géométrique en plan oblique (Konyushkova et al.), ces derniers ayant également travaillé sur des données IRM de glioblastome mais dans un cadre d'annotation binaire, contrairement à l'approche multiclasse développée ici. Sur le plan méthodologique, cinq modes d'interaction combinant incertitude du classifieur et connaissance experte de la segmentation correcte sont comparés dans cette tâche de segmentation multi-tissus. La méthode MISCLASS-B se révèle globalement la plus performante, avec des différences statistiquement significatives (p < 0,001) entre certaines paires de méthodes après 20 cycles d'interaction.