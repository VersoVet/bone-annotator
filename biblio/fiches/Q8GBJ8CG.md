# Detecting pediatric wrist fractures using deep-learning-based object detection.



## Resume


Detecting pediatric wrist fractures using deep-learning-based object detection.

Missed fractures are the leading cause of diagnostic error in the emergency department, and fractures of pediatric bones, particularly subtle wrist fractures, can be misidentified because of their varying characteristics and responses to injury.

Deep Learning-Based Multi-Class Pediatric Wrist Fracture Subtype Classification: A Pilot Study Comparing Convolutional Neural Network Architectures

Pediatric wrist fractures are among the most prevalent musculoskeletal injuries in children. Fracture subtype, including buckle/torus, greenstick, and Salter–Harris physeal injuries, directly influences management and prognosis. Subspecialty radiographic expertise required for subtype classification is not universally available in emergency or resource-limited settings. Deep learning (DL) offers an automated approach to fracture subtype recognition from plain radiographs. This pilot study evaluated convolutional neural network (CNN)-based five-class pediatric wrist fracture classification using the GRAZPEDWRI-DX dataset.A total of 940 pediatric wrist radiographs from GRAZPEDWRI-DX (figshare ID 14825193) were labeled using Arbeitsgemeinschaft fur Osteosynthesefragen (AO) pediatric codes into five classes: no fracture, buckle/torus, greenstick, Salter–Harris physeal fracture, and other fracture. Contrast-limited adaptive histogram equalization (CLAHE) and letterbox resizing to 224 × 224

Fracture Detection in Wrist X-ray Images Using Deep Learning-Based Object Detection Models

Hospitals, especially their emergency services, receive a high number of wrist fracture cases. For correct diagnosis and proper treatment of these, images obtained from various medical equipment must be viewed by physicians, along with the patient’s medical records and physical examination. The aim of this study is to perform fracture detection by use of deep-learning on wrist X-ray images to support physicians in the diagnosis of these fractures, particularly in the emergency services. Using SABL, RegNet, RetinaNet, PAA, Libra R-CNN, FSAF, Faster R-CNN, Dynamic R-CNN and DCN deep-learning-based object detection models with various backbones, 20 different fracture detection procedures were performed on Gazi University Hospital’s dataset of wrist X-ray images. To further improve these procedures, five different ensemble models were developed and then used to reform an ensemble model to develop a unique detection model, ‘wrist fracture detection-combo (WFD-C)’. From 26 different models for fracture detection, the highest detection result obtained was 0.8639 average precision (AP50) in the WFD-C model. Huawei Turkey R&amp;D Center supports this study within the scope of the ongoing cooperation project coded 071813 between Gazi University, Huawei and Medskor.

Critical evaluation of deep neural networks for wrist fracture detection.

Wrist Fracture is the most common type of fracture with a high incidence rate. Conventional radiography (i.e. X-ray imaging) is used for wrist fracture detection routinely, but occasionally fracture delineation poses issues and an additional confirmation by computed tomography (CT) is needed for diagnosis. Recent advances in the field of Deep Learning (DL), a subfield of Artificial Intelligence (AI), have shown that wrist fracture detection can be automated using Convolutional Neural Networks. However, previous studies did not pay close attention to the difficult cases which can only be confirmed via CT imaging. In this study, we have developed and analyzed a state-of-the-art DL-based pipeline for wrist (distal radius) fracture detection-DeepWrist, and evaluated it against one general population test set, and one challenging test set comprising only cases requiring confirmation by CT. Our results reveal that a typical state-of-the-art approach, such as DeepWrist, while having a near-pe

Artificial intelligence-based method for detecting wrist fractures in children.

Pediatric wrist fractures are common skeletal injuries in clinical practice; however, due to the ongoing development of children's bones, fracture characteristics are complex and often prone to misdiagnosis or missed diagnosis. Moreover, traditional diagnostic methods rely heavily on the physician's experience, which may compromise efficiency and accuracy, especially in environments with limited medical resources. To address this issue, this study proposes an improved deep learning detection method based on YOLO11s, named Kid-YOLO, for the automatic detection of pediatric wrist fractures in X-ray images. By introducing the C3k2-WTConv module and Focaler-MPDIoU loss function, the model was improved in terms of multi-scale feature extraction, target box localization accuracy optimization, and addressing the class imbalance problem. The C3k2-WTConv module, which combines wavelet transform and convolution operations, effectively enhances the model's ability to detect subtle fractures and c

Deep learning performance compared to healthcare experts in detecting wrist fractures from radiographs: A systematic review and meta-analysis.

To perform a systematic review and meta-analysis of the diagnostic accuracy of deep learning (DL) algorithms in the diagnosis of wrist fractures (WF) on plain wrist radiographs, taking healthcare experts consensus as reference standard.

Arm fracture detection in X-rays based on improved deep convolutional neural network

Deep Learning-Assisted Diagnosis of Pediatric Skull Fractures on Plain Radiographs.

To develop and evaluate a deep learning-based artificial intelligence (AI) model for detecting skull fractures on plain radiographs in children.

FracDet-v11: a multi-scale attention and wavelet-enhanced network for real-time pediatric wrist fracture detection.

Pediatric wrist fracture detection is diagnostically challenging due to subtle fracture morphologies and growth plate obscuration. To address this, we propose FracDet-v11, a specialized real-time framework based on YOLOv11s. We introduce a series of architectural enhancements to optimize feature representation and detection robustness: (1) a reconstructed backbone integrating Haar Wavelet Downsampling (HWD) and PKI-CAA to effectively preserve high-frequency details, complemented by a Dual-branch Channel Attention Module (DCAM); (2) a lightweight Slim-Neck for efficient feature fusion; and (3) a detection head incorporating Deformable Convolution v4 (DCNv4) and Focaler-CIoU loss to adapt to geometric deformations and prioritize hard samples. Benchmarking on the GRAZPEDWRI-DX dataset demonstrates that FracDet-v11 achieves a precision of 73.9% and mAP50 of 64.8%, surpassing the baseline by 3.8% and 3.1%, respectively. Furthermore, the model exhibits robust generalization on the external F

Bone Fracture Detection Based on Deep Learning Techniques

Automatic hip fracture detection using deep learning

External validation of a commercially available deep learning algorithm for fracture detection in children

A pediatric wrist trauma X-ray dataset (GRAZPEDWRI-DX) for machine learning

Abstract
                  Digital radiography is widely available and the standard modality in trauma imaging, often enabling to diagnose pediatric wrist fractures. However, image interpretation requires time-consuming specialized training. Due to astonishing progress in computer vision algorithms, automated fracture detection has become a topic of research interest. This paper presents the GRAZPEDWRI-DX dataset containing annotated pediatric trauma wrist radiographs of 6,091 patients, treated at the Department for Pediatric Surgery of the University Hospital Graz between 2008 and 2018. A total number of 10,643 studies (20,327 images) are made available, typically covering posteroanterior and lateral projections. The dataset is annotated with 74,459 image tags and features 67,771 labeled objects. We de-identified all radiographs and converted the DICOM pixel data to 16-Bit grayscale PNG images. The filenames and the accompanying text files provide basic patient information (age, sex). Several pediatric radiologists annotated dataset images by placing lines, bounding boxes, or polygons to mark pathologies like fractures or periosteal reactions. They also tagged general image characteristics. This dataset is publicly available to encourage computer vision research.

Convolutional Neural Network to Classify Infrared Thermal Images of Fractured Wrists in Pediatrics

Convolutional neural network (CNN) models were devised and evaluated to classify infrared thermal (IRT) images of pediatric wrist fractures. The images were recorded from 19 participants with a wrist fracture and 21 without a fracture (sprain). The injury diagnosis was by X-ray radiography. For each participant, 299 IRT images of their wrists were recorded. These generated 11,960 images (40 participants × 299 images). For each image, the wrist region of interest (ROI) was selected and fast Fourier transformed (FFT) to obtain a magnitude frequency spectrum. The spectrum was resized to 100 × 100 pixels from its center as this region represented the main frequency components. Image augmentations of rotation, translation and shearing were applied to the 11,960 magnitude frequency spectra to assist with the CNN generalization during training. The CNN had 34 layers associated with convolution, batch normalization, rectified linear unit, maximum pooling and SoftMax and classification. The ratio of images for the training and test was 70:30, respectively. The effects of augmentation and dropout on CNN performance were explored. Wrist fracture identification sensitivity and accuracy of 88% and 76%, respectively, were achieved. The CNN model was able to identify wrist fractures; however, a larger sample size would improve accuracy.

Convolutional Neural Networks for Automated Fracture Detection and Localization on Wrist Radiographs


## Quote


This study showed that a deep learning model can be trained to detect wrist fractures in radiographs with diagnostic accuracy similar to that of senior subspecialized orthopedic surgeons.

We designed a deep learning model to detect and localize fractures in wrist radiographs and then trained it on a subset of the labeled dataset. We then clinically tested the trained model's performance on two test datasets

OsteoDetect, an AI based on deep learning, has been approved by the U.S. Food and Drug Administration (FDA) in 2018 for the detection and assisted diagnosis of wrist fractures in adults and has achieved good results, it is still deficient in penetration and clinical application.


## Conclusion


A deep learning model can be trained to detect wrist fractures in radiographs with diagnostic accuracy similar to that of senior subspecialized orthopedic surgeons When emergency medicine clinicians are assisted by the trained model, their ability to detect wrist fractures is significantly improved, diminishing diagnostic errors and improving efficiency The misinterpretation rate of practicing emergency medicine clinicians was reduced by approximately one-half through the assistance of the model The increased sensitivity observed did not come at the expense of lower specificity, likely due to the high standalone diagnostic accuracy of the model It is important to train and evaluate deep learning models on datasets with ground truth labels worth emulating, established by senior subspecialized experts rather than less experienced clinicians Deep learning models offer potential for subspecialized clinicians to teach computers to emulate their diagnostic expertise, potentially helping patients on a global scale Making a prediction using the trained model takes less than a second on a modern computer, suggesting future technology could permit any patient's clinician to receive high-quality radiographic interpretations similar to those of senior subspecialized experts