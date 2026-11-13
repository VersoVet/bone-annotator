# Generation of fluoroscopy-alike radiographs as alternative datasets for deep learning in interventional radiology



## Resume


Generation of fluoroscopy-alike radiographs as alternative datasets for deep learning in interventional radiology

DeepDRR -- A Catalyst for Machine Learning in Fluoroscopy-guided Procedures

Machine learning-based approaches outperform competing methods in most disciplines relevant to diagnostic radiology. Interventional radiology, however, has not yet benefited substantially from the advent of deep learning, in particular because of two reasons: 1) Most images acquired during the procedure are never archived and are thus not available for learning, and 2) even if they were available, annotations would be a severe challenge due to the vast amounts of data. When considering fluoroscopy-guided procedures, an interesting alternative to true interventional fluoroscopy is in silico simulation of the procedure from 3D diagnostic CT. In this case, labeling is comparably easy and potentially readily available, yet, the appropriateness of resulting synthetic data is dependent on the forward model. In this work, we propose DeepDRR, a framework for fast and realistic simulation of fluoroscopy and digital radiography from CT scans, tightly integrated with the software platforms native

Generation of training dataset for deep-learning noise reduction

Deep learning approach for the prediction of diseases in medical images

Deep Learning Model for Real-Time Catheter Tracking from Fluoroscopy

Automatic localization of anatomical landmarks in head cine fluoroscopy images via deep learning.

Fluoroscopy guided interventions (FGIs) pose a risk of prolonged radiation exposure; personalized patient dosimetry is necessary to improve patient safety during these procedures. However, current FGIs systems do not capture the precise exposure regions of the patient, making it challenging to perform patient-procedure-specific dosimetry. Thus, there is a pressing need to develop approaches to extract and use this information to enable personalized radiation dosimetry for interventional procedures.

A Standardised Approach for Preparing Imaging Data for Machine Learning Tasks in Radiology

Enhancing medical image super-resolution through generative adversarial networks and transformer-based joint feature learning

Deep Learning for the Radiographic Detection of Periodontal Bone Loss

Anatomical landmark segmentation in orthopantomogram radiographs using deep learning

Development of an artificial intelligence system using deep learning to indicate anatomical landmarks during laparoscopic cholecystectomy

Fluoroscopic Image Denoising with Feature Preserving Residual Noise Learning

Breast cancer detection in pathological imaging using deep learning methods

Use of deep learning approaches for the prediction of diseases from medical images

Deep learning‐based reconstruction of interventional tools and devices from four X‐ray projections for tomographic interventional guidance

AbstractPurposeImage guidance for minimally invasive interventions is usually performed by acquiring fluoroscopic images using a monoplanar or a biplanar C‐arm system. However, the projective data provide only limited information about the spatial structure and position of interventional tools and devices such as stents, guide wires, or coils. In this work, we propose a deep learning‐based pipeline for real‐time tomographic (four‐dimensional [4D]) interventional guidance at conventional dose levels.MethodsOur pipeline is comprised of two steps. In the first one, interventional tools are extracted from four cone‐beam CT projections using a deep convolutional neural network. These projections are then Feldkamp reconstructed and fed into a second network, which is trained to segment the interventional tools and devices in this highly undersampled reconstruction. Both networks are trained using simulated CT data and evaluated on both simulated data and C‐arm cone‐beam CT measurements of stents, coils, and guide wires.ResultsThe pipeline is capable of reconstructing interventional tools from only four X‐ray projections without the need for a patient prior. At an isotropic voxel size of 100 , our methods achieve a precision/recall within a 100  environment of the ground truth of 93%/98%, 90%/71%, and 93%/76% for guide wires, stents, and coils, respectively.ConclusionsA deep learning‐based approach for 4D interventional guidance is able to overcome the drawbacks of today's interventional guidance by providing full spatiotemporal (4D) information about the interventional tools at dose levels comparable to conventional fluoroscopy.


## Raw_Discussion


We proposed DeepDRR, a framework for fast and realistic generation of synthetic X-ray images from diagnostic 3D CT, in an effort to ease the establishment of machine learning-based approaches in fluoroscopy-guided procedures.


## Quote


We proposed DeepDRR, a framework for fast and realistic generation of synthetic X-ray images from diagnostic 3D CT, in an effort to ease the establishment of machine learning-based approaches in fluoroscopy-guided procedures.

We propose an alternative image reconstruction strategy based on a learning-based algorithm, called convolutional neural networks (CNNs).

Le dataset, validé par des experts médicaux (radiologues et orthopédiste) et testé techniquement avec des modèles de deep learning (YOLOv8s/YOLOv8s-seg), constitue une ressource précieuse pour le développement et l'évaluation d'algorithmes d'apprentissage automatique pour le diagnostic des fractures osseuses


## Conclusion


The proposed deep learning-based framework shows promising capability for denoising interventional X-ray fluoroscopy images. The results from the catheter detection show that the network does not affect the results of such an algorithm when used as a pre-processing step. The extensive qualitative and quantitative evaluations suggest that the network may be of benefit to reduce radiation dose when applied in real time in the catheter laboratory.

DeepDRR permet, selon les auteurs, une génération rapide et réaliste de radiographies synthétiques à partir de CT diagnostiques 3D. L'association d'une décomposition des matériaux et d'une estimation de la diffusion fondées sur l'apprentissage avec une projection analytique et une injection réaliste du bruit produit des données adaptées à l'entraînement de modèles. Sur la tâche de substitution étudiée, les modèles entraînés sur DeepDRRs se généralisent aux données cliniques sans réentraînement ni adaptation de domaine, contrairement au même modèle entraîné sur des DRRs conventionnels. Les auteurs considèrent la simulation réaliste in silico des radiographies comme un catalyseur potentiel du développement de l'apprentissage automatique pour les procédures guidées par fluoroscopie. La force de la conclusion sur la détection des repères est limitée dans le texte fourni par l'absence de métriques quantitatives de précision, d'intervalles de confiance, de valeurs p et de tailles d'effet.


## Raw_Unnamed


d as inputs for tomographic reconstruction.


## Insight


implications: FracAtlas constitue une ressource benchmark standardisée destinée à stimuler le développement et l'évaluation comparative d'algorithmes d'apprentissage automatique pour le diagnostic assisté par ordinateur des fractures osseuses.
En rendant public un dataset de radiographies triplement annoté (classification, localisation, segmentation) et validé par des experts cliniques, les auteurs offrent à la communauté de recherche en imagerie médicale une ressource de référence standardisée permettant des comparaisons rigoureuses entre différentes architectures de deep learning. Cette disponibilité publique répond directement à un besoin identifié dans la littérature, où le manque de datasets ouverts de qualité suffisante freinait le développement reproductible d'algorithmes de détection automatique de fractures. La validation technique préliminaire via YOLOv8s (mAP de 56,2%) établit une performance de référence (baseline) que les futurs travaux pourront chercher à améliorer, notamment sur la dimension du rappel qui reste le point faible identifié. À plus long terme, l'existence d'un tel dataset pourrait faciliter le développement d'outils d'aide au diagnostic radiologique déployables dans des contextes cliniques à ressources limitées, où l'accès à une expertise radiologique spécialisée peut être restreint, bien que cela nécessiterait des étapes de validation clinique supplémentaires au-delà de la seule performance technique rapportée dans cette étude de description de dataset.