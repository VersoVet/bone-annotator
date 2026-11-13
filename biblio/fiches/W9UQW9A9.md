# MMAN: Multi-Task and Multi-Scale Attention Network for Concurrently Lower Limbs Segmentation and Landmark Detection



## Resume


MMAN: Multi-Task and Multi-Scale Attention Network for Concurrently Lower Limbs Segmentation and Landmark Detection

Multi-Task Learning Network for Landmark Detection in Anatomical Tree Structures

Segmentation-Guided Coordinate Regression for Robust Landmark Detection on X-Rays: Application to Automated Assessment of Lower Limb Alignment

A Multi-Task Deep Neural Network for Segmentation and Landmark Detection in Cardiac Computerized Tomography

Simultaneous Segmentation and Anatomical Landmark Detection on 3D Data using Context-aware Multi-task Learning

Segmentation-guided coordinate regression for robust landmark detection on X-rays: application to automated assessment of lower limb alignment_supp1-3394895.pdf

SLD: Segmentation-Based Landmark Detection for Spinal Ligaments

Optimization and Benchmarking of Image Segmentation for Improved Landmark Detection in Lower Limb X-Rays and Accurate Coronal Plane Alignment of the Knee Classification

Enhancing automatic landmark localization in X-ray images using combined segmentation and regression models: application to lower limb alignment assessment.

Manual landmark detection in lower limb medical imaging is time-consuming and error-prone. Recently, authors have proposed automatic landmark detection methods based on image segmentation, coordinate regression, or a combination of both to aid clinicians. While the latter approach shows promising results, detailed optimization of its design choices, including the integration strategy and hyperparameter tuning, remains unexplored. This study investigates the optimal approach to combining image segmentation and coordinate regression, focusing on selecting suitable network architectures and optimizing their configurations. We contrasted two methods for training the network: end-to-end training and cascading the subnetworks, and assessed the optimal architecture for each strategy. For landmark segmentation, we compared U-Net and Swin-UNETR models, and for coordinate regression, we assessed VGG-16, ResNet-50, and Swin-B. Performance was evaluated in detecting eight landmarks in each leg of

Solutions for Lower Limb Misalignment: A Segmentation-Guided Coordinate Regression Approach for Landmark Detection and Automatic Measurement

Traditionally, surgeons measure lower limb deformities manually by assessing angles between axes drawn on full lower limb X-rays connecting specific landmarks. This process is considered cumbersome and subject to the surgeon's expertise. Our study aims to alleviate the manual detection of landmarks while enhancing the assessment of lower limb malalignment through an innovative approach that combines coordinate regression and landmark segmentation. While various deep learning solutions exist, our method differs by using landmark segmentation to indicate the possible location of the landmarks; this information is combined with the X-rays to estimate the position of the landmarks via coordinate regression. We named this deep learning architecture segmentation-guided regression.To address the performance of our proposed approach, we evaluated the detection errors for eight landmarks and measured five malalignment metrics. We also compare our approach against landmark regression and landmar

Multi-task deep learning for segmentation and landmark detection in obstetric sonography

Feature Aggregation and Refinement Network for 2D Anatomical Landmark Detection

A deep learning-based multi-view approach to automatic 3D landmarking and deformity assessment of lower limb.

Anatomical Landmark detection in CT-Scan images is widely used in the identification of skeletal disorders. However, the traditional process of manually detecting anatomical landmarks, especially in three dimensions, is both time-consuming and prone to human errors. We propose a novel, deep-learning-based approach to automatic detection of 3D landmarks in CT images of the lower limb. We generate multiple view renderings of the scanned limb and then integrate them, using a pyramid-style convolutional neural network, to build a 3D model of the bone and to determine the spatial coordinates of the landmarks. Those landmarks are then used to calculate key anatomical indicators that would enable the reliable diagnosis of skeletal disorders. To evaluate the performance of the proposed approach we compare its predicted landmark coordinates and resulting anatomical indicators (both 2D and 3D) with those determined by human experts. The average coordinate error (difference between automatically

Collaborative regression-based anatomical landmark detection

Task-Adaptive Framework for Joint Medical Image Segmentation and Landmark Detection

A Multi-Task Based Deep Learning Framework With Landmark Detection for MRI Couinaud Segmentation

Optimization and benchmarking of image segmentation for improved landmark detection in lower limb X-rays and accurate coronal plane alignment of the knee classification_supp1-3572342.pdf

Learning-based landmark detection in pelvis x-rays with attention mechanism: data from the osteoarthritis initiative

Abstract
               Patients with developmental dysplasia of the hip can have this problem throughout their lifetime. The problem is difficult to detect by radiologists throughout x-ray because of an abrasion of anatomical structures. Thus, the landmarks should be automatically and precisely located. In this paper, we propose an attention mechanism of combining multi-dimension information on the basis of separating spatial dimension. The proposed attention mechanism decouples spatial dimension and forms width-channel dimension and height-channel dimension by 1D pooling operations in the height and width of spatial dimension. Then non-local means operations are performed to capture the correlation between long-range pixels in width-channel dimension, as well as that in height-channel dimension at different resolutions. The proposed attention mechanism modules are inserted into the skipped connections of U-Net to form a novel landmark detection structure. This landmark detection method was trained and evaluated through five-fold cross-validation on an open-source dataset, including 524 pelvis x-ray, each containing eight landmarks in pelvis, and achieved excellent performance compared to other landmark detection models. The average point-to-point errors of U-Net, HR-Net, CE-Net, and the proposed network were 3.5651 mm, 3.6118 mm, 3.3914 mm and 3.1350 mm, respectively. The results indicate that the proposed method has the highest detection accuracy. Furthermore, an open-source pelvis dataset is annotated and released for open research.

Automatic assessment of lower limb deformities using high-resolution X-ray images.

<h4>Background</h4>Planning an osteotomy or arthroplasty surgery on a lower limb requires prior classification/identification of its deformities. The detection of skeletal landmarks and the calculation of angles required to identify the deformities are traditionally done manually, with measurement accuracy relying considerably on the experience of the individual doing the measurements. We propose a novel, image pyramid-based approach to skeletal landmark detection.<h4>Methods</h4>The proposed approach uses a Convolutional Neural Network (CNN) that receives the raw X-ray image as input and produces the coordinates of the landmarks. The landmark estimations are modified iteratively via the error feedback method to come closer to the target. Our clinically produced full-leg X-Rays dataset is made publically available and used to train and test the network. Angular quantities are calculated based on detected landmarks. Angles are then classified as lower than normal, normal or higher than