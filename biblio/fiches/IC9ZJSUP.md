# A feasibility study of lung tumor segmentation on kilo-voltage radiographic images with transfer learning: Toward tumor motion tracking in radiotherapy



## Resume


A feasibility study of lung tumor segmentation on kilo-voltage radiographic images with transfer learning: Toward tumor motion tracking in radiotherapy

Signal-aware deep learning-based respiratory motion prediction for lung tumor management.

<h4>Introduction</h4>Respiratory motion management in radiotherapy for lung cancer patients remains a significant challenge, as it directly affects accurate tumor targeting. Furthermore, unaccounted tumor motion during treatment planning and delivery can lead to imaging artifacts and biased dose distributions, which compromises the accuracy of image-guided radiotherapy. This issue places clinicians in a dilemma between expanding treatment margins, which increases radiation exposure to healthy tissue or risking reduced targeting precision.<h4>Methods</h4>In this work, a hybrid deep learning model composed of dilated convolutional layers, bidirectional long-short term memory layers, and a generative autoencoder module is proposed to jointly model the spatial and temporal characteristics of respiratory motion, while enabling reconstruction of the physiologically coherent respiratory signals. Each architectural component learns complementary motion-related patterns from respiratory signals

Prediction of the motion of chest internal points using a recurrent neural network trained with real-time recurrent learning for latency compensation in lung cancer radiotherapy

During the radiotherapy treatment of patients with lung cancer, the radiation delivered to healthy tissue around the tumor needs to be minimized, which is difficult because of respiratory motion and the latency of linear accelerator systems. In the proposed study, we first use the Lucas-Kanade pyramidal optical flow algorithm to perform deformable image registration of chest computed tomography scan images of four patients with lung cancer. We then track three internal points close to the lung tumor based on the previously computed deformation field and predict their position with a recurrent neural network (RNN) trained using real-time recurrent learning (RTRL) and gradient clipping. The breathing data is quite regular, sampled at approximately 2.5Hz, and includes artificial drift in the spine direction. The amplitude of the motion of the tracked points ranged from 12.0mm to 22.7mm. Finally, we propose a simple method for recovering and predicting 3D tumor images from the tracked poin

From CNNs to SAM: A Survey of Deep Learning Techniques for Liver Tumor Segmentation in CT Images.

Accurate liver tumor segmentation is a critical component of clinical assessment, forming the basis for treatment planning, therapy response monitoring, prognostic assessment, and the delivery of precision medicine. However, in real-world clinical practice, this task remains particularly challenging. The intrinsic diversity of liver tumors -manifested in variations of shape, texture, size, and location-combined with the similarity of neighboring organs, indistinct tumor boundaries, and inconsistencies in image acquisition conditions, makes accurate liver lesion segmentation particularly difficult. In clinical practice, traditional segmentation methods are often used due to their interpretability and lower computational requirements. These approaches are labor-intensive and time-consuming, especially when dealing with 3D medical images, making them impractical for large-scale or real-time applications. In recent years, deep learning (DL) models have gained considerable attention for aut

Marker-Less Lung Tumor Tracking from Real-Time Color X-Ray Fluoroscopic Images Using Cross-Patient Deep Learning Model.

Fiducial marker implantation for tumor localization in radiotherapy is effective but invasive and carries complication risks. To address this, we propose a marker-less tumor tracking framework to explore the feasibility of a cross-patient deep learning model, aiming to eliminate the need for per-patient retraining. A novel degradation model generates realistic simulated data from digitally reconstructed radiographs (DRRs) to train a Restormer network, which transforms clinical fluoroscopic images into clean, DRR-like images. Subsequently, a DUCK-Net model, trained on DRRs, performs tumor segmentation. We conducted a feasibility study using a clinical dataset from 7 lung cancer patients, comprising 100 distinct treatment fields. The framework achieved an average processing time of 179.8 ms per image and demonstrated high accuracy: the median 3D Euclidean tumor center tracking error was 1.53 mm, with directional errors of 0.98±0.70 mm (LR), 1.09±0.74 mm (SI), and 1.34±0.94 mm (AP). These

Deep learning workflow in radiology: a primer

Abstract
                  Interest for deep learning in radiology has increased tremendously in the past decade due to the high achievable performance for various computer vision tasks such as detection, segmentation, classification, monitoring, and prediction. This article provides step-by-step practical guidance for conducting a project that involves deep learning in radiology, from defining specifications, to deployment and scaling. Specifically, the objectives of this article are to provide an overview of clinical use cases of deep learning, describe the composition of multi-disciplinary team, and summarize current approaches to patient, data, model, and hardware selection. Key ideas will be illustrated by examples from a prototypical project on imaging of colorectal liver metastasis. This article illustrates the workflow for liver lesion detection, segmentation, classification, monitoring, and prediction of tumor recurrence and patient survival. Challenges are discussed, including ethical considerations, cohorting, data collection, anonymization, and availability of expert annotations. The practical guidance may be adapted to any project that requires automated medical image analysis.

Enhanced Pneumonia Detection Through Transfer Learning on Chest Radiograph Images

Healthy versus pathological learning transferability in shoulder muscle MRI segmentation using deep convolutional encoder-decoders

Automatic segmentation of pathological shoulder muscles in patients with musculo-skeletal diseases is a challenging task due to the huge variability in muscle shape, size, location, texture and injury. A reliable fully-automated segmentation method from magnetic resonance images could greatly help clinicians to plan therapeutic interventions and predict interventional outcomes while eliminating time consuming manual segmentation efforts. The purpose of this work is three-fold. First, we investigate the feasibility of pathological shoulder muscle segmentation using deep learning techniques, given a very limited amount of available annotated pediatric data. Second, we address the learning transferability from healthy to pathological data by comparing different learning schemes in terms of model generalizability. Third, extended versions of deep convolutional encoder-decoder architectures using encoders pre-trained on non-medical data are proposed to improve the segmentation accuracy. Met

A transfer learning-driven fine-tuning of YOLOv10 for improved brain tumor detection in MRI images.

Identifying brain tumors accurately through medical imaging is vital in supporting computer-aided diagnostic systems, playing an essential role in early disease identification and effective treatment planning. Manual analysis of medical scans, like MRI scans, often slow and susceptible to human error, emphasizing the growing demand for automated, efficient, and precise detection systems. In the proposed study, we present an enhanced approach to fine-tuning an object detection model for accurately identifying brain tumors, demonstrating the capabilities of deep learning techniques in medical imaging analysis. The proposed method leverages the YOLOv10 architecture, a state-of-the-art model recognized for its high detection speed and precision. Due to the limited availability of extensive labeled medical imaging datasets, a transfer learning approach is adopted by initializing the model with parameters trained on the COCO dataset. These parameters are then fine-tuned using a brain tumor-s

Application of transformer models in medical image segmentation: a narrative review.

<h4>Background and objective</h4>Transformer-based medical image segmentation plays a crucial role in healthcare applications, facilitating precise diagnosis, treatment planning, and disease monitoring. Traditionally, convolutional neural networks (CNNs), which excel at local feature extraction, have dominated this field. However, they have a limited ability to capture the long-range dependencies within images and thus face difficulty in handling the complex, interconnected structures present in medical data. Transformer modeling, as an advanced tool in natural language processing (NLP), has also demonstrated its value in computer vision tasks. With its increasing popularity, research on its application in medical imaging has grown significantly. Nowadays, several models have demonstrated that combining CNNs and transformers can effectively capture both local and global information, thereby enhancing segmentation performance. A review was conducted to characterize the research on trans

Investigate Uncertainty Estimation in Transfer Learning Based Active Learning for Medical Image Segmentation

Understanding the Tricks of Deep Learning in Medical Image Segmentation: Challenges and Future Directions

Multi-Task Deep Learning for Simultaneous Classification and Segmentation of Cancer Pathologies in Diverse Medical Imaging Modalities

Background: Clinical imaging is an important part of health care providing physicians with great assistance in patients treatment. In fact, segmentation and grading of tumors can help doctors assess the severity of the cancer at an early stage and increase the chances of cure. Despite that Deep Learning for cancer diagnosis has achieved clinically acceptable accuracy, there still remains challenging tasks, especially in the context of insufficient labeled data and the subsequent need for expensive computational ressources. Objective: This paper presents a lightweight classification and segmentation deep learning model to assist in the identification of cancerous tumors with high accuracy despite the scarcity of medical data. Methods: We propose a multi-task architecture for classification and segmentation of cancerous tumors in the Brain, Skin, Prostate and lungs. The model is based on the UNet architecture with different pre-trained deep learning models (VGG 16 and MobileNetv2) as a b

Enhancing Bone Fracture Detection in Medical Imaging: Implementing Transfer Learning and Adversarial Training

A Review on Deep Learning Techniques for Detecting Lung Cancer and Lung Image Annotation

Abstract: Deep learning techniques played a major role in medical research along with convolutional neural networks (CNN) to detect various diseases from the scanned images. There are so many deep learning techniques available in the theory which can be more useful for lung cancer detection and annotations. This paper considered a detailed review on different types of deep learning techniques and their applications for medical image analysis to detect lung cancer using the possible best method in an accurate way. A critical review has been carried out throughout the paper to understand the current state-of-the-art for selecting an appropriate direction for future research.

Can Foundation Models Really Segment Tumors? A Benchmarking Odyssey in Lung CT Imaging

Accurate lung tumor segmentation is crucial for improving diagnosis, treatment planning, and patient outcomes in oncology. However, the complexity of tumor morphology, size, and location poses significant challenges for automated segmentation. This study presents a comprehensive benchmarking analysis of deep learning-based segmentation models, comparing traditional architectures such as U-Net and DeepLabV3, self-configuring models like nnUNet, and foundation models like MedSAM, and MedSAM~2. Evaluating performance across two lung tumor segmentation datasets, we assess segmentation accuracy and computational efficiency under various learning paradigms, including few-shot learning and fine-tuning. The results reveal that while traditional models struggle with tumor delineation, foundation models, particularly MedSAM~2, outperform them in both accuracy and computational efficiency. These findings underscore the potential of foundation models for lung tumor segmentation, highlighting their


## Raw_Introduction


Radiotherapy is used in more than 50% of cancer patients, as a primary treatment or within multimodal care [1]. Treatment planning requires delineating the Clinical Target Volume (CTV) and organs at risk (OARs) on CT to deliver ionizing radiation dose to the target while sparing healthy tissues, a process that remains time-consuming and error-prone. Over the last decade, deep learning (DL) has enabled accurate automatic contouring for many common structures [2]- [4]; however, clinical adoption is still limited for complex targets, where reliability and interpretability are as critical as average segmentation accuracy.

Radiotherapy is used in more than 50% of cancer patients, as a primary treatment or within multimodal care [1]. Treatment planning requires delineating the Clinical Target Volume (CTV) and organs at risk (OARs) on CT to deliver ionizing radiation dose to the target while sparing healthy tissues, a process that remains time-consuming and error-prone. Over the last decade, deep learning (DL) has enabled accurate automatic contouring for many common structures [2]- [4]; however, clinical adoption is still limited for complex targets, where reliability and interpretability are as critical as average segmentation accuracy.


## Quote


Deep learning offers the most promising path forward, with numerous architectures proposed for tumor localization in projection images. However, robust clinical translation remains elusive due to concerns about generalizability, adversarial susceptibility, and potential for hallucinated outputs-failure modes unacceptable in radiation therapy.

The ability to segment and track anatomical structures or lesions across temporally dynamic imaging sequences supports adaptive treatment planning, minimizes radiation exposure to surrounding healthy tissue, and ensures consistency across treatment sessions.

medical images can be used to fine-tune CNN models that have already been trained on datasets of natural images. This method, called transfer learning, has been used in a wide range of medical imaging applications with great success.

A transfer learning-based active learning framework can significantly reduce the size of required labeled training data while maintaining high accuracy of the classification of tumors in brain MRI.

Because accurate and reliable segmentation of lung tissue is of particular importance in various clinical applications such as computer-assisted bronchoscopy, quantification of emphysema, and diagnosis of lung cancer.

L'introduction de grands modèles de fondation pour la segmentation du cancer est cruciale pour obtenir des résultats prometteurs en planification de traitement et en pratique clinique, mais de nombreuses pistes restent à explorer, notamment en matière de segmentation 3D, d'apprentissage faiblement supervisé et d'images multimodales.


## Raw_A_Datasets_Details


The lung dataset is focused on the segmentation of lung tumors from computed tomography (CT) scans. This task presents the specific challenge of identifying small cancerous regions within a large imaging volume.

The lung dataset is focused on the segmentation of lung tumors from computed tomography (CT) scans. This task presents the specific challenge of identifying small cancerous regions within a large imaging volume.


## Synthese


L'étude vise à démontrer l'efficacité des techniques de segmentation pulmonaire et d'exclusion des ombres osseuses pour l'analyse de radiographies thoraciques 2D par deep learning, dans le but d'aider les radiologues à identifier les régions suspectes chez les patients atteints de cancer du poumon.


## Insight


efficacy: Un cadre d’apprentissage actif fondé sur le transfer learning peut réduire significativement la taille des données d’entraînement annotées requises tout en maintenant une précision élevée pour la classification des tumeurs cérébrales en IRM.


## Conclusion


An efficient iterative deconvolution algorithm with a novel resolution subsets-based approach operating on patient DICOM images was used for quantitative improvement in MRI clinical imaging The method can be applied to clinical MRI images and will be crucial to facilitate diagnosis of tumor progression at the earliest stages The method can be considered as an extended blind deblurring or Richardson-Lucy-like algorithm with multiple resolution levels


## Raw_Segmentation


uch as tumor burden, surgical margin error, or treatment response consistency must guide model optimization, ensuring that segmentation outputs move beyond pixel overlap toward trustworthy, outcome-aligned clinical decision support [34].