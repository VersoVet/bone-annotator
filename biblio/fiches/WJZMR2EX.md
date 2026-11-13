# Evaluation of a convolutional neural network to identify scaphoid fractures on radiographs.



## Resume


Evaluation of a convolutional neural network to identify scaphoid fractures on radiographs.

This study aimed to develop and evaluate a convolutional neural network for identifying scaphoid fractures on radiographs. A dataset of 1918 wrist radiographs (600 patients) was taken from an orthopaedic referral centre between 2010 to 2020. A YOLOv3 and a MobileNetV3 convolutional neural network were trained for scaphoid detection and fracture classification, respectively. The diagnostic performance of the convolutional neural network was compared with the majority decision of four hand surgeons. The convolutional neural network achieved a sensitivity of 82% and specificity of 94%, with an area under the receiver operating characteristic of 92%, whereas the surgeons achieved a sensitivity of 76% and specificity of 96%. The comparison indicated that the convolutional neural network's performance was similar to the majority vote of surgeons. It further revealed that convolutional neural network could be used in identifying scaphoid fractures on radiographs reliably, and has potential to

Development and Validation of a Deep Learning Model Using Convolutional Neural Networks to Identify Scaphoid Fractures in Radiographs

The Detection and Classification of Scaphoid Fracture in Radiograph by Using the Convolutional Neural Network

Objective:
Scaphoid fractures, particularly occult and non-displaced fractures, are difficult to detect using traditional X-ray methods due to their subtle appearance and variability in bone density.
The study proposes a two-stage CNN approach to detect and classify scaphoid fractures using anterior-posterior (AP) and lateral (LA) X-ray views for more accurate diagnosis.
Methods:
The study emphasizes the use of multi-view X-ray images (AP and LA views) to improve fracture detection and classification. The multi-view fusion module helps integrate information from both views to enhance detection accuracy, particularly for occult fractures that may not be visible in a single view. The proposed method includes two stages that are stage 1: Detect the scaphoid bone using Faster R-CNN and Feature Pyramid Network (FPN) for region proposal and small object detection. The detection accuracy for scaphoid localization is 100% with Intersection over Union (IoU) scores of 0.8662 for AP views and 0.8

Bone Fracture Detection from X-ray Images using a Convolutional Neural Network (CNN)

Bone fractures are common injuries that require quick and accurate diagnosis to provide the right medical care. The “convolutional neural network” technique relies mostly on manual inspection, by radiologists and can be laborious and prone to error. The objective of this work was to increase the efficiency and accuracy of fracture identification by automating the examination of X-ray images using convolutional neural networks. A “convolutional neural network” model created to detect bone fractures in X-ray images was used in the present study. The model was trained and validated using an extensive dataset of X-ray images, which included both fractured and nonfractured bones. Multiple convolutional layers were used in the “convolutional neural network” architecture for feature extraction, and pooling and fully connected layers were added for classification. The main measures used to assess the model&amp;#039;s performance were sensitivity, specificity, and accuracy. In regard to identif

Effects of Image Degradation on Deep Neural Network Classification of Scaphoid Fracture Radiographs: Comparison Study of Different Noise Types.

<h4>Background</h4>Deep learning models have shown strong potential for automated fracture detection in medical images. However, their robustness under varying image quality remains uncertain, particularly for small and subtle fractures, such as scaphoid fractures. Understanding how different types of image perturbations affect model performance is crucial for ensuring reliable deployment in clinical practice.<h4>Objective</h4>This study aimed to evaluate the robustness of a deep learning model trained to detect scaphoid fractures in radiographs when exposed to various image perturbations. We sought to identify which perturbations most strongly impact performance and to explore strategies to mitigate performance degradation.<h4>Methods</h4>Radiographic datasets were systematically modified by applying Gaussian noise, blurring, JPEG compression, contrast-limited adaptive histogram equalization, resizing, and geometric offsets. Model accuracy was evaluated across different perturbation t

Bone Fracture Detection using Region-Based Convolutional Neural Network

A Comparative Study of Certain Convolutional Neural Network Architectures for X-ray Image Analysis in Bone Fracture Detection and Identification

Evaluation of deep learning and convolutional neural network algorithms for mandibular fracture detection using radiographic images: A systematic review and meta-analysis

Computed Tomography Cervical Spine Fracture Detection Using a Convolutional Neural Network

Deep Learning in Scaphoid Fracture Detection and Healing Prediction: A Systematic Review of Artificial Intelligence Applications in Hand Surgery.

Scaphoid fractures are the most common carpal bone injuries and continue to pose diagnostic and therapeutic challenges due to their tendency for delayed union or non-union. Interpretation variability and delayed detection remain key contributors to missed injuries and adverse outcomes. Deep learning (DL) models, particularly convolutional neural networks (CNNs), have shown strong performance in musculoskeletal imaging and offer potential to improve diagnostic accuracy and prognostication in hand surgery. A systematic review of PubMed, Embase, and PMC was conducted covering January 2015 to March 2025, following Preferred Reporting Items for Systematic Review and Meta-Analysis (PRISMA) 2020 guidelines. Studies were eligible if they applied DL algorithms to detect or classify scaphoid fractures or to predict union and non-union, and reported at least one diagnostic metric (accuracy, area under the curve (AUC), sensitivity, or specificity). Traditional machine-learning approaches, cadaveri

Convolutional Neural Networks for Automated Fracture Detection and Localization on Wrist Radiographs

Convolutional Neural Network Model based Deep Learning Approach for Osteoporosis Fracture Detection

Is Convolutional Neural Network Accurate for Automatic Detection of Zygomatic Fractures on Computed Tomography?

Zygomatic fractures involve complex anatomical structures of the mid-face and the diagnosis can be challenging and labor-consuming. This research aimed to evaluate the performance of an automatic algorithm for the detection of zygomatic fractures based on convolutional neural network (CNN) on spiral computed tomography (CT).

Bone Fracture Classification Using Skeletal Radiographs and Deep Learning

Bone Fracture Detection in X-ray Images using Convolutional Neural Network

It is critical to design a fracture detection system to offer quick results and reduce diagnosing errors. Using X-ray images in growing artificial intelligence methodologies, especially the deep learning method, has become a practical choice for detecting bone fractures. This research paper suggests a deep learning method using X-ray images for early diagnosis of bone disorders and also detection of different bone fractures. The effectiveness of the convolutional neural network model for classifying bone fractures from normal bones is used. Several significant factors such as no. of epochs, batch size, type of optimizers and learning rate are considered to find the best-suited model. Hence, it is found that the convolutional neural network model has good performance using the specificity of 89.865%, accuracy of 90% approximately, and area under ROC curve of 0.8088.

Development of a manufacturer-independent convolutional neural network for the automated identification of vertebral compression fractures in vertebral fracture assessment images using active learning.

Convolutional neural networks (CNNs) can identify vertebral compression fractures in GE vertebral fracture assessment (VFA) images with high balanced accuracy, but performance against Hologic VFAs is unknown. To obtain good classification performance, supervised machine learning requires balanced and labeled training data. Active learning is an iterative data annotation process with the ability to reduce the cost of labeling medical image data and reduce class imbalance.

Bone Fracture Detection Using Residual Neural Network

Artificial intelligence fracture recognition on computed tomography: review of literature and recommendations

Abstract
                Purpose
                The use of computed tomography (CT) in fractures is time consuming, challenging and suffers from poor inter-surgeon reliability. Convolutional neural networks (CNNs), a subset of artificial intelligence (AI), may overcome shortcomings and reduce clinical burdens to detect and classify fractures. The aim of this review was to summarize literature on CNNs for the detection and classification of fractures on CT scans, focusing on its accuracy and to evaluate the beneficial role in daily practice.
              
                Methods
                Literature search was performed according to the PRISMA statement, and Embase, Medline ALL, Web of Science Core Collection, Cochrane Central Register of Controlled Trials and Google Scholar databases were searched. Studies were eligible when the use of AI for the detection of fractures on CT scans was described. Quality assessment was done with a modified version of the methodologic index for nonrandomized studies (MINORS), with a seven-item checklist. Performance of AI was defined as accuracy, F1-score and area under the curve (AUC).
              
                Results
                Of the 1140 identified studies, 17 were included. Accuracy ranged from 69 to 99%, the F1-score ranged from 0.35 to 0.94 and the AUC, ranging from 0.77 to 0.95. Based on ten studies, CNN showed a similar or improved diagnostic accuracy in addition to clinical evaluation only.
              
                Conclusions
                CNNs are applicable for the detection and classification fractures on CT scans. This can improve automated and clinician-aided diagnostics. Further research should focus on the additional value of CNN used for CT scans in daily clinics.

Artificial intelligence detection of distal radius fractures: a comparison between the convolutional neural network and professional assessments


## Insight


efficacy: Le deep learning, en particulier les réseaux de neurones convolutifs (CNN), démontre un potentiel important et parfois une performance supérieure à celle des praticiens humains pour la détection et la classification de fractures osseuses à partir d'images radiographiques.

efficacy: Les algorithmes basés sur des réseaux de neurones convolutifs (CNN) améliorent la précision diagnostique des fractures de côtes tout en réduisant le temps d'interprétation des radiologues.


## Discussion


Cette revue synthétise les approches de deep learning appliquées à la détection et à la classification des fractures osseuses à partir d'images radiologiques, en concluant que les modèles fondés sur les réseaux de neurones convolutifs (CNN), en particulier InceptionNet et XceptionNet, obtiennent des performances élevées dans cette tâche. Les auteurs soulignent que le diagnostic radiographique manuel effectué par les radiologues experts demeure un processus chronophage et exigeant en ressources humaines, que les techniques de détection automatisée pourraient utilement soutenir. La rareté des données d'entraînement annotées est identifiée, par consensus dans la littérature examinée, comme le principal obstacle au développement d'algorithmes de classification hautement performants, et aucun modèle standardisé consensuel n'a pu être dégagé compte tenu des données actuellement disponibles. Les auteurs positionnent explicitement le deep learning comme un outil d'assistance au radiologue plutôt que comme un substitut à son expertise, répondant ainsi aux inquiétudes professionnelles relatives à un remplacement du jugement clinique humain.


## Quote


Within orthopedic trauma surgery, early investigations have shown that deep neural networks can detect fractures on radiographs with accuracy approaching that of expert clinicians [4,5].


## Synthese


L'objectif de cette étude est de concevoir et d'évaluer de manière exhaustive un modèle de deep learning basé sur des réseaux de neurones convolutifs (CNN) pour la détection précoce et le diagnostic de fractures osseuses à partir d'images radiographiques (X-ray), dans un contexte où les erreurs de diagnostic humain et les délais de traitement clinique demeurent des enjeux importants. Cette démarche est motivée par le constat, formulé en Discussion, que la plupart des techniques antérieures avaient été évaluées sur un nombre minimal de données, sans étude comparative systématique des architectures et hyperparamètres. Les auteurs cherchent spécifiquement à étudier l'impact de plusieurs hyperparamètres (taux d'apprentissage, nombre d'epochs, optimiseur, taille de batch) sur la performance de classification, et à identifier, parmi six modèles CNN testés, celui offrant la meilleure efficacité pour distinguer les images osseuses fracturées des images non fracturées.