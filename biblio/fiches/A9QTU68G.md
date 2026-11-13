# Assisted annotation in Deep LOGISMOS: Simultaneous multi-compartment 3D MRI segmentation of calf muscles.



## Resume


Assisted annotation in Deep LOGISMOS: Simultaneous multi-compartment 3D MRI segmentation of calf muscles.

<h4>Background</h4>Automated segmentation of individual calf muscle compartments in 3D MR images is gaining importance in diagnosing muscle disease, monitoring its progression, and prediction of the disease course. Although deep convolutional neural networks have ushered in a revolution in medical image segmentation, achieving clinically acceptable results is a challenging task and the availability of sufficiently large annotated datasets still limits their applicability.<h4>Purpose</h4>In this paper, we present a novel approach combing deep learning and graph optimization in the paradigm of assisted annotation for solving general segmentation problems in 3D, 4D, and generally n-D with limited annotation cost.<h4>Methods</h4>Deep LOGISMOS combines deep-learning-based pre-segmentation of objects of interest provided by our convolutional neural network, FilterNet+, and our 3D multi-objects LOGISMOS framework (layered optimal graph image segmentation of multiple objects and surfaces) that

Suggestive Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

MRSegmentator: Multi-Modality Segmentation of 40 Classes in MRI and CT

Purpose: To develop and evaluate a deep learning model for multi-organ segmentation of MRI scans.   Materials and Methods: The model was trained on 1,200 manually annotated 3D axial MRI scans from the UK Biobank, 221 in-house MRI scans, and 1228 CT scans from the TotalSegmentator dataset. A human-in-the-loop annotation workflow was employed, leveraging cross-modality transfer learning from an existing CT segmentation model to segment 40 anatomical structures. The annotation process began with a model based on transfer learning between CT and MR, which was iteratively refined based on manual corrections to predicted segmentations. The model's performance was evaluated on MRI examinations obtained from the German National Cohort (NAKO) study (n=900) from the AMOS22 dataset (n=60) and from the TotalSegmentator-MRI test data (n=29). The Dice Similarity Coefficient (DSC) and Hausdorff Distance (HD) were used to assess segmentation quality, stratified by organ and scan type. The model and it

SliceInsightNet: Advanced Hybrid Image Segmentation for Spine Annotation in MRI

Invited 2 - Annotation-Efficient Deep Learning for Medical Image Segmentation

Learning with Limited Annotations: A Survey on Deep Semi-Supervised Learning for Medical Image Segmentation

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

SAM & SAM 2 in 3D Slicer: SegmentWithSAM Extension for Annotating Medical Images

Attention, Suggestion and Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

AUTOMATIC MULTI-CLASS SEGMENTATION OF HIP JOINT SPACE USING 3D DEEP LEARNING ALGORITHMS

<jats:sec id="sec69_1" sec-type="intro"><jats:title>Introduction</jats:title>Three-dimensional (3D) morphological understanding of the hip joint, specifically the joint space and surrounding anatomy, including the proximal femur and the pelvis bone, is crucial for a range of orthopedic diagnoses and surgical planning. While deep learning algorithms can provide higher accuracy for segmenting bony structures, delineating hip joint space formed by cartilage layers is often left for subjective manual evaluation. This study compared the performance of two state-of-the-art 3D deep learning architectures (3D UNET and 3D UNETR) for automated segmentation of proximal femur bone, pelvis bone, and hip joint space with single and multi-class label segmentation strategies.</jats:sec><jats:sec id="sec69_2" sec-type="methods"><jats:title>Method</jats:title>A dataset of 56 3D CT images covering the hip joint was used for the study. Two bones and hip joint space were manually segmented for training and

Self-Supervised Learning for Annotation-Efficient Endoscopic Instrument Segmentation

A Localisation-Segmentation Approach for Multi-label Annotation of Lumbar Vertebrae using Deep Nets

Multi-class segmentation of vertebrae is a non-trivial task mainly due to the high correlation in the appearance of adjacent vertebrae. Hence, such a task calls for the consideration of both global and local context. Based on this motivation, we propose a two-staged approach that, given a computed tomography dataset of the spine, segments the five lumbar vertebrae and simultaneously labels them. The first stage employs a multi-layered perceptron performing non-linear regression for locating the lumbar region using the global context. The second stage, comprised of a fully-convolutional deep network, exploits the local context in the localised lumbar region to segment and label the lumbar vertebrae in one go. Aided with practical data augmentation for training, our approach is highly generalisable, capable of successfully segmenting both healthy and abnormal vertebrae (fractured and scoliotic spines). We consistently achieve an average Dice coefficient of over 90 percent on a publicly a

Deep Learning Method for Rapid Simultaneous Multistructure Temporal Bone Segmentation.

To develop and validate a deep learning algorithm for the automated segmentation of key temporal bone structures from clinical computed tomography (CT) data sets.

Automatic Segmentation of Early Triassic Vertebrate Fossil CT Scans: Reducing Human Annotation Time through Deep Learning

<title>Abstract</title>
        <p>Recent developments in Deep Learning have opened the possibility for automated segmentation of large and highly detailed CT scan datasets of fossil material. However, previous methodologies have required large amounts of training data to reliably extract complex skeletal structures. Here we present a method for automated Deep Learning segmentation to obtain high-fidelity 3D models of fossils digitally extracted from the surrounding rock, training the model with less than 1%-2% of the total CT dataset. This workflow has the capacity to revolutionise the use of Deep Learning to significantly reduce the processing time of such data and boost the availability of segmented CT-scanned fossil material for future research outputs. Our final Unet segmentation model achieved a validation Dice similarity of 0.96.</p>

Automated radiographic assessment of lower limb alignment using deep learning in a data-constrained clinical setting.

BACKGROUND: A model using stacked hourglass neural network modules was developed for automated lower limb alignment measurements in full-leg frontal radiographs. The goal was to assess whether high accuracy could be achieved with training on relatively small datasets, a common constraint in clinical research. METHODS: The model first identifies joints regions of interest (ROIs), then detects anatomical landmarks for alignment measurement within each ROI. 112 bilateral radiographs (216 annotated single-leg images) were used for training and validation, 99 (186 legs) as internal test set, and 25 (49) as external test set. Performance metrics included intraclass correlation coefficient (ICCs) and mean absolute error (MAE). RESULTS: The model achieved excellent agreement (ICCs > 0.9) with manual annotations for all alignment parameters, except for the joint line convergence angle (ICC < 0.5), which also showed poor agreement between human readers (0.73). CONCLUSION: The proposed approach d

Use of deep learning to automate the annotation of USG lung image data

PyMIC: A deep learning toolkit for annotation-efficient medical image segmentation

Automatic Segmentation, Localization, and Identification of Vertebrae in 3D CT Images Using Cascaded Convolutional Neural Networks

This paper presents a method for automatic segmentation, localization, and identification of vertebrae in arbitrary 3D CT images. Many previous works do not perform the three tasks simultaneously even though requiring a priori knowledge of which part of the anatomy is visible in the 3D CT images. Our method tackles all these tasks in a single multi-stage framework without any assumptions. In the first stage, we train a 3D Fully Convolutional Networks to find the bounding boxes of the cervical, thoracic, and lumbar vertebrae. In the second stage, we train an iterative 3D Fully Convolutional Networks to segment individual vertebrae in the bounding box. The input to the second networks have an auxiliary channel in addition to the 3D CT images. Given the segmented vertebra regions in the auxiliary channel, the networks output the next vertebra. The proposed method is evaluated in terms of segmentation, localization, and identification accuracy with two public datasets of 15 3D CT images fr

Deep learning for detection and 3D segmentation of maxillofacial bone lesions in cone beam CT.

To develop an automated deep-learning algorithm for detection and 3D segmentation of incidental bone lesions in maxillofacial CBCT scans.

DeepEdit: Deep Editable Learning for Interactive Segmentation of 3D Medical Images

Automatic segmentation of medical images is a key step for diagnostic and interventional tasks. However, achieving this requires large amounts of annotated volumes, which can be tedious and time-consuming task for expert annotators. In this paper, we introduce DeepEdit, a deep learning-based method for volumetric medical image annotation, that allows automatic and semi-automatic segmentation, and click-based refinement. DeepEdit combines the power of two methods: a non-interactive (i.e. automatic segmentation using nnU-Net, UNET or UNETR) and an interactive segmentation method (i.e. DeepGrow), into a single deep learning model. It allows easy integration of uncertainty-based ranking strategies (i.e. aleatoric and epistemic uncertainty computation) and active learning. We propose and implement a method for training DeepEdit by using standard training combined with user interaction simulation. Once trained, DeepEdit allows clinicians to quickly segment their datasets by using the algorit

Deep Learning-Based Annotation Transfer between Molecular Imaging Modalities: An Automated Workflow for Multimodal Data Integration

A Calibrated Deep Learning Framework Integrating Spatial Annotations and Clinical Metadata for Safe Three-Class Bone Lesion Classification on Radiographs

An annotation tool for dermoscopic image segmentation

Three-Dimensional Magnetic Resonance Imaging Bone Models of the Hip Joint Using Deep Learning: Dynamic Simulation of Hip Impingement for Diagnosis of Intra- and Extra-articular Hip Impingement.

<h4>Background</h4>Dynamic 3-dimensional (3D) simulation of hip impingement enables better understanding of complex hip deformities in young adult patients with femoroacetabular impingement (FAI). Deep learning algorithms may improve magnetic resonance imaging (MRI) segmentation.<h4>Purpose</h4>(1) To evaluate the accuracy of 3D models created using convolutional neural networks (CNNs) for fully automatic MRI bone segmentation of the hip joint, (2) to correlate hip range of motion (ROM) between manual and automatic segmentation, and (3) to compare location of hip impingement in 3D models created using automatic bone segmentation in patients with FAI.<h4>Study design</h4>Cohort study (diagnosis); Level of evidence, 3.<h4>Methods</h4>The authors retrospectively reviewed 31 hip MRI scans from 26 symptomatic patients (mean age, 27 years) with hip pain due to FAI. All patients had matched computed tomography (CT) and MRI scans of the pelvis and the knee. CT- and MRI-based osseous 3D models


## Raw_Introduction


Several automated algorithms for knee segmentation have been proposed in the literature such as approximate binary k-NN classifiers [4], deformable active shape models [6], local image patch optimization using Markov random fields [10], hierarchical two stage cartilage classifiers optimized by graph cuts [15], and multi-atlas labeling with locally weighted voting [9]. Many of these methods make use of locally (not globally) optimal techniques to solve the segmentation problem. For example, Wang et al. [15] used multi-label graph cuts to optimize the background combining bone regions with true background and the cartilage classifier outputs. LOGISMOS algorithm [16] can simultaneously segment multiple surfaces in different objects taking contextual information between them to make the segmentation robust with guaranteed global optimality.

Segmentation is among the most common medical image analysis tasks and is critical to a wide variety of clinical applications. To date, data-driven deep learning (DL) methods have shown prominent segmentation performance when trained on fully-annotated datasets [8]. However, data annotation is a significant bottleneck for dataset creation. First, annotation process is tedious, laborious and time-consuming, especially for 3D medical images where dense annotation with voxel-level accuracy is required. Second, medical images typically need to be annotated by medical experts whose time is limited and expensive, making the annotations even more difficult and costly to obtain. Active learning (AL) is a promising solution to improve annotation efficiency by iteratively selecting the most important data to annotate with the goal of reducing the total number of annotated samples required. However, most deep AL methods require an initial set of labeled samples to start the active selection. When

Segmentation is among the most common medical image analysis tasks and is critical to a wide variety of clinical applications. To date, data-driven deep learning (DL) methods have shown prominent segmentation performance when trained on fully-annotated datasets [8]. However, data annotation is a significant bottleneck for dataset creation. First, annotation process is tedious, laborious and time-consuming, especially for 3D medical images where dense annotation with voxel-level accuracy is required. Second, medical images typically need to be annotated by medical experts whose time is limited and expensive, making the annotations even more difficult and costly to obtain. Active learning (AL) is a promising solution to improve annotation efficiency by iteratively selecting the most important data to annotate with the goal of reducing the total number of annotated samples required. However, most deep AL methods require an initial set of labeled samples to start the active selection. When


## Conclusion


L'annotation assistée par SAM 2 peut réduire substantiellement la charge de travail manuelle associée à l'annotation de grands ensembles de données d'imagerie 3D pour l'entraînement de modèles de segmentation en aval, tout en maintenant la performance de ces modèles L'intégration de SAM 2 dans les outils d'annotation existants (par ex. via le plug-in disponible pour 3D Slicer) présente un potentiel prometteur pour réduire la charge de travail manuelle dans les workflows de segmentation humaine, réduisant les coûts et favorisant la recherche et le développement de dispositifs médicaux


## Discussion


Cette étude présente DeepEdit, une méthode de deep learning permettant un flux de travail d'apprentissage actif guidé par l'incertitude pour l'annotation d'images médicales, en combinant au sein d'un même modèle la segmentation automatique et l'édition interactive. Contrairement aux approches interactives antérieures, DeepEdit s'intègre facilement dans tout pipeline de segmentation médicale 3D incluant des stratégies d'apprentissage actif. L'outil offre aux cliniciens et biologistes deux modalités d'usage complémentaires : l'obtention d'une segmentation automatique modifiable ultérieurement via des clics dans une interface utilisateur (par exemple 3D Slicer ou OHIF), ou la génération directe d'une segmentation semi-automatique à partir de clics fournis par l'utilisateur. Les auteurs concluent que cette approche pourrait réduire significativement le temps consacré par les cliniciens et biologistes à l'annotation de nouveaux jeux de données, diminuant ainsi le coût et l'effort associés à ce processus.