# A Segmentation-Guided Deep Learning Framework for Scapular Landmark Detection



## Resume


A Segmentation-Guided Deep Learning Framework for Scapular Landmark Detection

A Multi-Task Based Deep Learning Framework With Landmark Detection for MRI Couinaud Segmentation

A deep learning pipeline for semantic facade segmentation

A Multi-Task Deep Neural Network for Segmentation and Landmark Detection in Cardiac Computerized Tomography

Anatomical landmark segmentation in uterine cervix images using deep learning

Task-Adaptive Framework for Joint Medical Image Segmentation and Landmark Detection

Suggestive Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

SLD: Segmentation-Based Landmark Detection for Spinal Ligaments

Multi-task deep learning for segmentation and landmark detection in obstetric sonography

Anatomical landmark segmentation in orthopantomogram radiographs using deep learning

Collaborative regression-based anatomical landmark detection

A two-stage regression framework for automated cephalometric landmark detection incorporating semantically fused anatomical features and multi-head refinement loss

A deep learning framework for the localization of landmarks on the lateral semi circular canals.

This paper introduces a Deep Learning (DL) framework to localize landmark coordinates within the semicircular canals in Computed Tomography (CT) scans of the temporal bone. These landmarks can be consistently defined across patients and imaging modalities and as such can serve as a means of forming a common coordinate system. We propose a DL based framework for automating the landmark selection process. We establish the accuracy of the methods using Bone Beam CT scans of the temporal bone of 20 patients and landmarks selected by 3 human experts as the ground truth. We show that the error rates are similar to the levels of variation in landmark selection achieved by human experts. We further validated the method on CT scans from 14 additional patients, demonstrating that the accuracy remains within clinically acceptable parameters.

Attention, Suggestion and Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

A Real-Time Multi-Task Learning Framework for Ear Recognition and Landmark Localization with Integrated Gradient Architecture

Deep Geodesic Learning for Segmentation and Anatomical Landmarking.

In this paper, we propose a novel deep learning framework for anatomy segmentation and automatic landmarking. Specifically, we focus on the challenging problem of mandible segmentation from cone-beam computed tomography (CBCT) scans and identification of 9 anatomical landmarks of the mandible on the geodesic space. The overall approach employs three inter-related steps. In the first step, we propose a deep neural network architecture with carefully designed regularization, and network hyper-parameters to perform image segmentation without the need for data augmentation and complex post-processing refinement. In the second step, we formulate the landmark localization problem directly on the geodesic space for sparsely-spaced anatomical landmarks. In the third step, we utilize a long short-term memory network to identify the closely-spaced landmarks, which is rather difficult to obtain using other standard networks. The proposed fully automated method showed superior efficacy compared to

Segmentation-Guided Coordinate Regression for Robust Landmark Detection on X-Rays: Application to Automated Assessment of Lower Limb Alignment

DenseSeg: Joint Learning for Semantic Segmentation and Landmark Detection Using Dense Image-to-Shape Representation

Purpose: Semantic segmentation and landmark detection are fundamental tasks of medical image processing, facilitating further analysis of anatomical objects. Although deep learning-based pixel-wise classification has set a new-state-of-the-art for segmentation, it falls short in landmark detection, a strength of shape-based approaches. Methods: In this work, we propose a dense image-to-shape representation that enables the joint learning of landmarks and semantic segmentation by employing a fully convolutional architecture. Our method intuitively allows the extraction of arbitrary landmarks due to its representation of anatomical correspondences. We benchmark our method against the state-of-the-art for semantic segmentation (nnUNet), a shape-based approach employing geometric deep learning and a convolutional neural network-based method for landmark detection. Results: We evaluate our method on two medical dataset: one common benchmark featuring the lungs, heart, and clavicle from thor


## Quote


We present a novel multi-task deep learning framework characterized by its simultaneous detection of critical landmarks and segmentation of Couinaud liver sections.


## Methodologie


Le framework combine, au premier étage, une segmentation osseuse globale et une détection de landmarks via un encodeur partagé et des décodeurs indépendants (hard parameter sharing), puis, au second étage, un affinement local de la segmentation de l'acétabulum couplé à une tâche de détection de contours. Cette approche a été comparée à des méthodes de référence de l'état de l'art (FCN, U-Net, nnU-Net) sur un ensemble de 81 images CT évaluées par validation croisée.