# Evaluating Iterative Deep Learning as a Labeling-Efficient Strategy for Tubular Segmentation in Digital Nephropathology



## Resume


Evaluating Iterative Deep Learning as a Labeling-Efficient Strategy for Tubular Segmentation in Digital Nephropathology

Deep learning medical image segmentation

Deep learning and its application to medical image segmentation

Reliable Label-Efficient Learning for Biomedical Image Recognition.

The use of deep neural networks for biomedical image analysis requires a sufficient number of labeled datasets. To acquire accurate labels as the gold standard, multiple observers with specific expertise are required for both annotation and proofreading. This process can be time-consuming and labor-intensive, making high-quality, and large-annotated biomedical datasets difficult. To address this problem, we propose a deep active learning framework that enables the active selection of both informative queries and reliable experts. To measure the uncertainty of the unlabeled data, a dropout-based strategy is integrated with a similarity criterion for both data selection and random error elimination. To select the reliable labelers, we adopt an expertise estimator to learn the expertise levels of labelers via offline-testing and online consistency evaluation. The proposed method is applied to classification tasks on two types of medical images including confocal endomicroscopy images and

Deep Neural Architectures for Medical Image Semantic Segmentation: Review

Deep Learning and Data Labeling for Medical Applications

A Localisation-Segmentation Approach for Multi-label Annotation of Lumbar Vertebrae using Deep Nets

Multi-class segmentation of vertebrae is a non-trivial task mainly due to the high correlation in the appearance of adjacent vertebrae. Hence, such a task calls for the consideration of both global and local context. Based on this motivation, we propose a two-staged approach that, given a computed tomography dataset of the spine, segments the five lumbar vertebrae and simultaneously labels them. The first stage employs a multi-layered perceptron performing non-linear regression for locating the lumbar region using the global context. The second stage, comprised of a fully-convolutional deep network, exploits the local context in the localised lumbar region to segment and label the lumbar vertebrae in one go. Aided with practical data augmentation for training, our approach is highly generalisable, capable of successfully segmenting both healthy and abnormal vertebrae (fractured and scoliotic spines). We consistently achieve an average Dice coefficient of over 90 percent on a publicly a

A Deep Learning-Based Fully Automated Vertebra Segmentation and Labeling Workflow.

Aims/Background Spinal disorders, such as herniated discs and scoliosis, are highly prevalent conditions with rising incidence in the aging global population. Accurate analysis of spinal anatomical structures is a critical prerequisite for achieving high-precision positioning with surgical navigation robots. However, traditional manual segmentation methods are limited by issues such as low efficiency and poor consistency. This work aims to develop a fully automated deep learning-based vertebral segmentation and labeling workflow to provide efficient and accurate preoperative analysis support for spine surgery navigation robots.
                  Methods In the localization stage, the You Only Look Once version 7 (YOLOv7) network was utilized to predict the bounding boxes of individual vertebrae on computed tomography (CT) sagittal slices, transforming the 3D localization problem into a 2D one. Subsequently, the Density-Based Spatial Clustering of Applications with Noise (DBSCAN) clustering algorithm was employed to aggregate the 2D detection results into 3D vertebral centers. This approach significantly reduces inference time and enhances localization accuracy. In the segmentation stage, a 3D U-Net model integrated with an attention mechanism was trained using the region of interest (ROI) based on the vertebral center as input, effectively extracting the 3D structural features of vertebrae to achieve precise segmentation. In the labeling stage, a vertebra labeling network was trained by combining deep learning architectures—ResNet and Transformer, which are capable of extracting rich intervertebral features, to obtain the final labeling results through post-processing based on positional logic analysis. To verify the effectiveness of this workflow, experiments were conducted on a dataset comprising 106 spinal CT datasets sourced from various devices, covering a wide range of clinical scenarios.
                  Results The results demonstrate that the method performed excellently in the three key tasks of localization, segmentation, and labeling, with a Mean Localization Error (MLE) of 1.42 mm. The segmentation accuracy metrics included a Dice Similarity Coefficient (DSC) of 0.968 ± 0.014, Intersection over Union (IoU) of 0.879 ± 0.018, Pixel Accuracy (PA) of 0.988 ± 0.005, mean symmetric distance (MSD) of 1.09 ± 0.19 mm, and Hausdorff Distance (HD) of 5.42 ± 2.05 mm. The degree of classification accuracy reached up to 94.36%.
                  Conclusion These quantitative assessments and visualizations confirm the effectiveness of our method (vertebra localization, vertebra segmentation and vertebra labeling), indicating its potential for deployment in spinal surgery navigation robots to provide accurate and efficient preoperative analysis and navigation support for spinal surgeries.

Understanding the Tricks of Deep Learning in Medical Image Segmentation: Challenges and Future Directions

Medical image segmentation using deep learning: A survey

Abstract
                  Deep learning has been widely used for medical image segmentation and a large number of papers has been presented recording the success of deep learning in the field. A comprehensive thematic survey on medical image segmentation using deep learning techniques is presented. This paper makes two original contributions. Firstly, compared to traditional surveys that directly divide literatures of deep learning on medical image segmentation into many groups and introduce literatures in detail for each group, we classify currently popular literatures according to a multi‐level structure from coarse to fine. Secondly, this paper focuses on supervised and weakly supervised learning approaches, without including unsupervised approaches since they have been introduced in many old surveys and they are not popular currently. For supervised learning approaches, we analyse literatures in three aspects: the selection of backbone networks, the design of network blocks, and the improvement of loss functions. For weakly supervised learning approaches, we investigate literature according to data augmentation, transfer learning, and interactive segmentation, separately. Compared to existing surveys, this survey classifies the literatures very differently from before and is more convenient for readers to understand the relevant rationale and will guide them to think of appropriate improvements in medical image segmentation based on deep learning approaches.

Label-Efficient Breast Cancer Histopathological Image Classification.

The automatic classification of breast cancer histopathological images has great significance in computer-aided diagnosis. Recently, deep learning via neural networks has enabled pattern detection and prediction using large, labeled datasets; whereas, collecting and annotating sufficient histological data using professional pathologists is time consuming, tedious, and extremely expensive. In the proposed paper, a deep active learning framework is designed and implemented for classification of breast cancer histopathological images, with the goal of maximizing the learning accuracy from very limited labeling. This method involves manual annotation of the most valuable unlabeled samples, which are then integrated into the training set. The model is then iteratively updated with an increasing training set. Here, two selection strategies are discussed for the proposed deep active learning framework: An entropy-based strategy and a confidence-boosting strategy. The proposed method has been

A Self-Configuring Deep Learning Network for Segmentation of Temporal Bone Anatomy in Cone-Beam CT Imaging.

Preoperative planning for otologic or neurotologic procedures often requires manual segmentation of relevant structures, which can be tedious and time-consuming. Automated methods for segmenting multiple geometrically complex structures can not only streamline preoperative planning but also augment minimally invasive and/or robot-assisted procedures in this space. This study evaluates a state-of-the-art deep learning pipeline for semantic segmentation of temporal bone anatomy.

An Efficient Deep Learning Approach for Brain Tumor Segmentation using 3D Convolutional Neural Network

Efficient labeling of retinal fundus photographs using deep active learning.

To compare the performance of four deep active learning (DAL) approaches to optimize label efficiency for training diabetic retinopathy (DR) classification deep learning models.

Automated Segmentation of Vertebrae on Lateral Chest Radiography Using Deep Learning

The purpose of this study is to develop an automated algorithm for thoracic vertebral segmentation on chest radiography using deep learning. 124 de-identified lateral chest radiographs on unique patients were obtained. Segmentations of visible vertebrae were manually performed by a medical student and verified by a board-certified radiologist. 74 images were used for training, 10 for validation, and 40 were held out for testing. A U-Net deep convolutional neural network was employed for segmentation, using the sum of dice coefficient and binary cross-entropy as the loss function. On the test set, the algorithm demonstrated an average dice coefficient value of 90.5 and an average intersection-over-union (IoU) of 81.75. Deep learning demonstrates promise in the segmentation of vertebrae on lateral chest radiography.

Getting Started with Deep Learning in Medical Imaging

Current and Emerging Trends in Medical Image Segmentation With Deep Learning

Classification Performance of Deep Learning Models for the Assessment of Vertical Dimension on Lateral Cephalometric Radiographs.

<b>Background/Objectives</b>: Vertical growth pattern significantly influences facial aesthetics and treatment choices. Lateral cephalograms are routinely used for the evaluation of vertical jaw relationships in orthodontic diagnosis. The aim of this study was to evaluate the performance of deep learning algorithms in classifying cephalometric radiographs according to vertical skeletal growth patterns without the need for anatomical landmark identification. <b>Methods</b>: This study was carried out on lateral cephalometric radiographs of 1050 patients. Cephalometric radiographs were divided into 3 subgroups based on FMA, SN-GoGn, and Cant of Occlusal Plane angles. Six deep learning models (ResNet101, DenseNet 201, EfficientNet B0, EfficientNet V2 B0, ConvNetBase, and a hybrid model) were employed for the classification of the dataset. The performances of the well-known deep learning models and the hybrid model were compared for accuracy, precision, F1-Score, mean absolute error, Cohen

Multi-label concept detection in imaging entities of biomedical literature leveraging deep learning-based classification and object detection

Panoptic Segmentation and Labelling of Lumbar Spine Vertebrae using Modified Attention Unet

Segmentation and labeling of vertebrae in MRI images of the spine are critical for the diagnosis of illnesses and abnormalities. These steps are indispensable as MRI technology provides detailed information about the tissue structure of the spine. Both supervised and unsupervised segmentation methods exist, yet acquiring sufficient data remains challenging for achieving high accuracy. In this study, we propose an enhancing approach based on modified attention U-Net architecture for panoptic segmentation of 3D sliced MRI data of the lumbar spine. Our method achieves an impressive accuracy of 99.5\% by incorporating novel masking logic, thus significantly advancing the state-of-the-art in vertebral segmentation and labeling. This contributes to more precise and reliable diagnosis and treatment planning.

Active learning using adaptable task-based prioritisation.

Supervised machine learning-based medical image computing applications necessitate expert label curation, while unlabelled image data might be relatively abundant. Active learning methods aim to prioritise a subset of available image data for expert annotation, for label-efficient model training. We develop a controller neural network that measures priority of images in a sequence of batches, as in batch-mode active learning, for multi-class segmentation tasks. The controller is optimised by rewarding positive task-specific performance gain, within a Markov decision process (MDP) environment that also optimises the task predictor. In this work, the task predictor is a segmentation network. A meta-reinforcement learning algorithm is proposed with multiple MDPs, such that the pre-trained controller can be adapted to a new MDP that contains data from different institutes and/or requires segmentation of different organs or structures within the abdomen. We present experimental results usin

Model-data-driven adversarial active learning for brain tumor segmentation.

Active learning (AL) attempts to select informative samples in a dataset to minimize the number of required labels while maximizing the performance of the model. Current AL in segmentation tasks is limited to the expansion of popular classification-based methods including entropy, MC-dropout, etc. Meanwhile, most applications in the medical field are simply migrations that fail to consider the nature of medical images, such as high class imbalance, high domain difference, and data scarcity. In this study, we address these challenges and propose a novel AL framework for medical image segmentation task. Our approach introduces a pseudo-label-based filter addressing excessive blank patches in medical abnormalities segmentation tasks, e.g., lesions, and tumors, used before the AL selection. This filter helps reduce resource usage and allows the model to focus on selecting more informative samples. For the sample selection, we propose a novel query strategy that combines both model impact a

Automatic multi-label temporal bone computed tomography segmentation with deep learning.

Manually segmenting temporal bone computed tomography (CT) images is difficult. Despite accurate automatic segmentation in previous studies using deep learning, they did not consider clinical differences, such as variations in CT scanners. Such differences can significantly affect the accuracy of segmentation.

Pioneering Precision in Lumbar Spine MRI Segmentation with Advanced Deep Learning and Data Enhancement

This study presents an advanced approach to lumbar spine segmentation using deep learning techniques, focusing on addressing key challenges such as class imbalance and data preprocessing. Magnetic resonance imaging (MRI) scans of patients with low back pain are meticulously preprocessed to accurately represent three critical classes: vertebrae, spinal canal, and intervertebral discs (IVDs). By rectifying class inconsistencies in the data preprocessing stage, the fidelity of the training data is ensured. The modified U-Net model incorporates innovative architectural enhancements, including an upsample block with leaky Rectified Linear Units (ReLU) and Glorot uniform initializer, to mitigate common issues such as the dying ReLU problem and improve stability during training. Introducing a custom combined loss function effectively tackles class imbalance, significantly improving segmentation accuracy. Evaluation using a comprehensive suite of metrics showcases the superior performance of t


## Raw_Introduction


Digital pathology has transformed the field of histopathological analysis by employing advanced computational methods to enhance the diagnosis and prognosis of diseases [1], [2]. Semantic segmentation is a pivotal technique in digital pathology, which involves segmenting images into distinct regions that represent various tissue structures, cell types, or subcellular elements [3]- [5]. The precision and efficiency of semantic segmentation are crucial for a wide range of applications, including the detection, grading, and prediction of outcomes for tumors, as well as for the examination of tissue morphology and cell interactions. Consequently, the development and refinement of robust segmentation algorithms are of paramount importance for the continued progress in the field of digital pathology [6]- [8].

Digital pathology has transformed the field of histopathological analysis by employing advanced computational methods to enhance the diagnosis and prognosis of diseases [1], [2]. Semantic segmentation is a pivotal technique in digital pathology, which involves segmenting images into distinct regions that represent various tissue structures, cell types, or subcellular elements [3]- [5]. The precision and efficiency of semantic segmentation are crucial for a wide range of applications, including the detection, grading, and prediction of outcomes for tumors, as well as for the examination of tissue morphology and cell interactions. Consequently, the development and refinement of robust segmentation algorithms are of paramount importance for the continued progress in the field of digital pathology [6]- [8].


## Synthese


L'étude vise à développer un algorithme de deep learning end-to-end permettant la détection et la segmentation de cellules individuelles en pathologie numérique à partir de point labels uniquement, sans nécessiter d'annotations pixel par pixel coûteuses.


## Quote


DeepEdit, a method that enables an uncertaintydriven active learning workflow for labelling medical images using a framework that combines deep learning-based automatic segmentation and interactive edits. Compared to previous interactive approaches, DeepEdit can be easily integrated into any 3D medical segmentation pipeline that includes active learning strategies.


## Raw_Full_Text


.1148/radiol.2021204021 
51. Guinebert S, Petit E, Bousson V, Bodard S, Amoretti N, Kastler B. Automatic semantic 
segmentation and detection of vertebras and intervertebral discs by neural networks. 
Comput Methods Programs Biomed Update [Internet]. 1 janv 2022 [cité 1 juill 
2024];2:100055. 
Disponible 
sur: 
https://www.sciencedirect.com/science/article/pii/S2666990022000076 
52. Liu F, Zhou Z, Jang H, Samsonov A, Zhao G, Kijowski R. Deep convolutional neural network 
and 3D deformable approach for tissue segmentation in musculoskeletal magnetic 
resonance imaging. Magn Reson Med [Internet]. 2018 [cité 1 juill 2024];79(4):2379‑91. 
Disponible 
sur: 
https://onlinelibrary-wiley-com.ezproxy.u-
paris.fr/doi/abs/10.1002/mrm.26841 
53. Zhou Z, Zhao G, Kijowski R, Liu F. Deep convolutional neural network for segmentation of 
knee joint anatomy. Magn Reson Med [Internet]. 2018 [cité 1 juill 2024];80(6):2759‑70. 
Disponible 
sur: 
https://onlinelibrary-wiley-com.ezproxy.u-
paris.fr/doi/abs/

.1148/radiol.2021204021 
51. Guinebert S, Petit E, Bousson V, Bodard S, Amoretti N, Kastler B. Automatic semantic 
segmentation and detection of vertebras and intervertebral discs by neural networks. 
Comput Methods Programs Biomed Update [Internet]. 1 janv 2022 [cité 1 juill 
2024];2:100055. 
Disponible 
sur: 
https://www.sciencedirect.com/science/article/pii/S2666990022000076 
52. Liu F, Zhou Z, Jang H, Samsonov A, Zhao G, Kijowski R. Deep convolutional neural network 
and 3D deformable approach for tissue segmentation in musculoskeletal magnetic 
resonance imaging. Magn Reson Med [Internet]. 2018 [cité 1 juill 2024];79(4):2379‑91. 
Disponible 
sur: 
https://onlinelibrary-wiley-com.ezproxy.u-
paris.fr/doi/abs/10.1002/mrm.26841 
53. Zhou Z, Zhao G, Kijowski R, Liu F. Deep convolutional neural network for segmentation of 
knee joint anatomy. Magn Reson Med [Internet]. 2018 [cité 1 juill 2024];80(6):2759‑70. 
Disponible 
sur: 
https://onlinelibrary-wiley-com.ezproxy.u-
paris.fr/doi/abs/