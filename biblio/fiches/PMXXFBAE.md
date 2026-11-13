# Convolutional neural network landmark regression for automated Cobb angle estimation from spinal radiographs



## Resume


Convolutional neural network landmark regression for automated Cobb angle estimation from spinal radiographs

Automatic Cobb Angle Detection using Vertebra Detector and Vertebra Corners Regression

Correct evaluation and treatment of Scoliosis require accurate estimation of spinal curvature. Current gold standard is to manually estimate Cobb Angles in spinal X-ray images which is time consuming and has high inter-rater variability. We propose an automatic method with a novel framework that first detects vertebrae as objects followed by a landmark detector that estimates the 4 landmark corners of each vertebra separately. Cobb Angles are calculated using the slope of each vertebra obtained from the predicted landmarks. For inference on test data, we perform pre and post processings that include cropping, outlier rejection and smoothing of the predicted landmarks. The results were assessed in AASCE MICCAI challenge 2019 which showed a promise with a SMAPE score of 25.69 on the challenge test set.

Automated Cobb Angle Measurement for Adolescent Idiopathic Scoliosis Using Convolutional Neural Network

The Cobb angle measurement of the scoliotic spine is prone to inter- and intra-observer variations in the clinical setting. This paper proposes a deep learning architecture for detecting spine vertebrae from X-ray images to evaluate the Cobb angle automatically. The public AASCE MICCAI 2019 anterior-posterior X-ray image dataset and local images were used to train and test the proposed convolutional neural network architecture. Sixty-eight landmark features of the spine were detected from the input image to obtain seventeen vertebrae on the spine. The vertebrae locations obtained were processed to automatically measure the Cobb angle. The proposed method can measure the Cobb angle with accuracies up to 93.6% and has excellent reliability compared to clinicians’ measurement (intraclass correlation coefficient &gt; 0.95). The proposed deep learning architecture may be used as a tool to augment Cobb angle measurement in X-ray images of patients with adolescent idiopathic scoliosis in a real-world clinical setting.

Automated anatomical landmark detection ondistal femur surface using convolutional neural network

Segmentation-Guided Coordinate Regression for Robust Landmark Detection on X-Rays: Application to Automated Assessment of Lower Limb Alignment

Segmentation-guided coordinate regression for robust landmark detection on X-rays: application to automated assessment of lower limb alignment_supp1-3394895.pdf

Deep learning approach for automatic landmark detection and alignment analysis in whole-spine lateral radiographs

Abstract
                  
                    Human spinal balance assessment relies considerably on sagittal radiographic parameter measurement. Deep learning could be applied for automatic landmark detection and alignment analysis, with mild to moderate standard errors and favourable correlations with manual measurement. In this study, based on 2210 annotated images of various spinal disease aetiologies, we developed deep learning models capable of automatically locating 45 anatomic landmarks and subsequently generating 18 radiographic parameters on a whole-spine lateral radiograph. In the assessment of model performance, the localisation accuracy and learning speed were the highest for landmarks in the cervical area, followed by those in the lumbosacral, thoracic, and femoral areas. All the predicted radiographic parameters were significantly correlated with ground truth values (all
                    p
                     &lt; 0.001). The human and artificial intelligence comparison revealed that the deep learning model was capable of matching the reliability of doctors for 15/18 of the parameters. The proposed automatic alignment analysis system was able to localise spinal anatomic landmarks with high accuracy and to generate various radiographic parameters with favourable correlations with manual measurements.

Development and validation of a keypoint region-based convolutional neural network to automate thoracic Cobb angle measurements using whole-spine standing radiographs.

<h4>Purpose</h4>Adolescent idiopathic scoliosis (AIS) affects a significant portion of the adolescent population, leading to severe spinal deformities if untreated. Diagnosis, surgical planning, and assessment of outcomes are determined primarily by the Cobb angle on anteroposterior spinal radiographs. Screening for scoliosis enables early interventions and improved outcomes. However, screenings are often conducted through school entities where a trained radiologist may not be available to accurately interpret the imaging results.<h4>Methods</h4>In this study, we developed an artificial intelligence tool utilizing a keypoint region-based convolutional neural network (KR-CNN) for automated thoracic Cobb angle (TCA) measurement. The KR-CNN was trained on 609 whole-spine radiographs of AIS patients and validated using our institutional AIS registry, which included 83 patients who underwent posterior spinal fusion with both preoperative and postoperative anteroposterior X-ray images.<h4>Re

Anatomical landmark detection on bi-planar radiographs for predicting spinopelvic parameters.

Accurate landmark detection is essential for precise analysis of anatomical structures, supporting diagnosis, treatment planning, and monitoring in patients with spinal deformities. Conventional methods rely on laborious landmark identification by medical experts, which motivates automation. The proposed deep learning pipeline processes bi-planar radiographs to determine spinopelvic parameters and Cobb angles without manual supervision.

Collaborative regression-based anatomical landmark detection

Cephalometric landmark detection in dental x-ray images using convolutional neural networks

Sagittal Cervical Spine Landmark Point Detection in X-Ray Using Deep Convolutional Neural Networks

A Deep-Learning-Based Lumbosacral Localization and Landmark Detection Network for Automatic Lumbar Stability and Spondylolisthesis Grading Assessment

Landmark Detection in Cardiac MRI by Using a Convolutional Neural                     Network

2-step deep learning model for landmarks localization in spine radiographs

Abstract
                  In this work we propose to use Deep Learning to automatically calculate the coordinates of the vertebral corners in sagittal x-rays images of the thoracolumbar spine and, from those landmarks, to calculate relevant radiological parameters such as L1–L5 and L1–S1 lordosis and sacral slope. For this purpose, we used 10,193 images annotated with the landmarks coordinates as the ground truth. We realized a model that consists of 2 steps. In step 1, we trained 2 Convolutional Neural Networks to identify each vertebra in the image and calculate the landmarks coordinates respectively. In step 2, we refined the localization using cropped images of a single vertebra as input to another convolutional neural network and we used geometrical transformations to map the corners to the original image. For the localization tasks, we used a differentiable spatial to numerical transform (DSNT) as the top layer. We evaluated the model both qualitatively and quantitatively on a set of 195 test images. The median localization errors relative to the vertebrae dimensions were 1.98% and 1.68% for x and y coordinates respectively. All the predicted angles were highly correlated with the ground truth, despite non-negligible absolute median errors of 1.84°, 2.43° and 1.98° for L1–L5, L1–S1 and SS respectively. Our model is able to calculate with good accuracy the coordinates of the vertebral corners and has a large potential for improving the reliability and repeatability of measurements in clinical tasks.

SAG-net: a spinal anatomical guided network for landmark detection and angle measurement in lateral full-spine radiograph


## Insight


implications: Les auteurs suggèrent que l'estimation directe des angles de Cobb à partir des landmarks, plutôt qu'un calcul géométrique classique, pourrait accroître la robustesse au bruit de prédiction.
Actuellement, les angles de Cobb (MT, PT, TL/L) sont calculés à partir des landmarks prédits via un algorithme géométrique déterministe reposant sur la pente de chaque vertèbre, ce qui rend le calcul final directement sensible à toute erreur locale de prédiction des coins vertébraux. Les auteurs proposent, comme piste future, de remplacer cette étape géométrique par un modèle d'apprentissage capable d'estimer directement les angles à partir des landmarks (ou même de bout en bout), ce qui pourrait offrir une robustesse accrue face au bruit inhérent aux prédictions individuelles des landmarks et potentiellement combler l'écart de performance avec le meilleur score du leaderboard (21.71% vs 25.69% obtenu).