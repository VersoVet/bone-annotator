# Bone anatomical landmark localization with cascaded spatial configuration network



## Resume


Bone anatomical landmark localization with cascaded spatial configuration network

<jats:title>Abstract</jats:title>
                  Accurate localization of bone anatomical landmarks in medical images is of great significance for decision-making in surgical plans and orthopedic surgery visual navigation systems development. However, due to the high dimensionality and large size of medical images, current automatic anatomical landmarks detection methods still have issues in terms of accuracy, robustness, and efficiency. To improve the accuracy of bone anatomical landmark detection in medical images, a new network model with a two-step strategy (coarse localizing and fine localizing) was proposed in this study. By combining fully convolutional neural networks and the heatmap regression model, a cascaded spatial configuration network was designed to combine the global and local features of 3D image features and localize anatomical landmarks stepwise. The model was evaluated with a collected knee CT image dataset and a published spine CT image dataset. The results wer

Integrating geometric configuration and appearance information into a unified framework for anatomical landmark localization

Collaborative regression-based anatomical landmark detection

Integrating spatial configuration into heatmap regression based CNNs for landmark localization

Cascaded convolutional networks for automatic cephalometric landmark detection.

Cephalometric analysis is a fundamental examination which is widely used in orthodontic diagnosis and treatment planning. Its key step is to detect the anatomical landmarks in lateral cephalograms, which is time-consuming in traditional manual way. To solve this problem, we propose a novel approach with a cascaded three-stage convolutional neural networks to predict cephalometric landmarks automatically. In the first stage, high-level features of the craniofacial structures are extracted to locate the lateral face area which helps to overcome the appearance variations. Next, we process the aligned face area to estimate the locations of all landmarks simultaneously. At the last stage, each landmark is refined through a dedicated network using high-resolution image data around the initial position to achieve more accurate result. We evaluate the proposed method on several anatomical landmark datasets and the experimental results show that our method achieved competitive performance compa

Automated anatomical landmark detection ondistal femur surface using convolutional neural network

Multistage Probabilistic Approach for the Localization of Cephalometric Landmarks

Automatic cardiac landmark localization by a recurrent neural network

Landmark Localization From Medical Images With Generative Distribution Prior

Cephalometric landmark detection in dental x-ray images using convolutional neural networks

Anatomical Landmark Localization for Knee X-ray Images via Heatmap Regression Refined with Graph Convolutional Network

Segmentation of Bone Structure in X-ray Images using Convolutional Neural Network

A deep learning framework for the localization of landmarks on the lateral semi circular canals.

This paper introduces a Deep Learning (DL) framework to localize landmark coordinates within the semicircular canals in Computed Tomography (CT) scans of the temporal bone. These landmarks can be consistently defined across patients and imaging modalities and as such can serve as a means of forming a common coordinate system. We propose a DL based framework for automating the landmark selection process. We establish the accuracy of the methods using Bone Beam CT scans of the temporal bone of 20 patients and landmarks selected by 3 human experts as the ground truth. We show that the error rates are similar to the levels of variation in landmark selection achieved by human experts. We further validated the method on CT scans from 14 additional patients, demonstrating that the accuracy remains within clinically acceptable parameters.

Multi-Task Learning Network for Landmark Detection in Anatomical Tree Structures


## Quote


A novel cephalometric landmark detection algorithm based on the SpatialConfiguration-Net architecture is described in detail in Section 3.

Formuler le problème de localisation de landmarks directement dans l'espace géodésique pour les landmarks anatomiques espacés (Step 2)


## Conclusion


Incorporating spatial configuration into a CNN-based heatmap regression architecture (SCN) achieves high landmark localization performance even with limited training datasets. The SCN outperforms state-of-the-art approaches across four size-limited 2D and 3D datasets of different anatomical structures (hand MRI, spine CT, skull radiographs, hand radiographs), demonstrating generic applicability. Even with training limited to as few as 10 images (2DHandReduced), the proposed network achieves results comparable to the state-of-the-art evaluated on the full dataset. By simultaneously and end-to-end optimizing local appearance and spatial configuration components, the landmark localization problem is separated into two simpler subproblems that can be learned from small amounts of training data. The local appearance component learns locally accurate candidate predictions while the spatial configuration component focuses on eliminating ambiguities, improving robustness to misidentification without needing local accuracy. The adapted Localization U-Net achieves competitive localization performance but is not state-of-the-art in robustness towards landmark misidentification, since it lacks prior knowledge of spatial configuration constraints among landmarks. On 2DHandFull, 3DHand, 2DSkull and 3DSpine datasets, SCN outperforms previous random forest based methods, CNN-based preliminary results, and other state-of-the-art/challenge-winning and highly tailored methods, without requiring complex or tailored implementations or postprocessing.