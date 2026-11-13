# Automatic adult age estimation using bone mineral density of proximal femur via deep learning.



## Resume


Automatic adult age estimation using bone mineral density of proximal femur via deep learning.

Accurate adult age estimation (AAE) is critical for forensic and anthropological applications, yet traditional methods relying on bone mineral density (BMD) face significant challenges due to biological variability and methodological limitations. This study aims to develop an end-to-end Deep Learning (DL) based pipeline for automated AAE using BMD from proximal femoral CT scans. The main objectives are to construct a large-scale dataset of 5151 CT scans from real-world clinical and cadaver cohorts, fine-tune the Segment Anything Model (SAM) for accurate femoral bone segmentation, and evaluate multiple convolutional neural networks (CNNs) for precise age estimation based on segmented BMD data. Model performance was assessed through cross-validation, internal clinical testing, and external post-mortem validation. SAM achieved excellent segmentation performance with a Dice coefficient of 0.928 and an average intersection over union (mIoU) of 0.869. The CNN models achieved an average mean

Age estimation based on 3D post-mortem computed tomography images of mandible and femur using convolutional neural networks

Age assessment has attracted increasing attention in the field of forensics. However, most existing works are laborious and requires domain-specific knowledge. Modern computing power makes it is possible to leverage massive amounts of data to produce more reliable results. Therefore, it is logical to use automated age estimation approaches to handle large datasets. In this study, a fully automated age prediction approach was proposed by assessing 3D mandible and femur scans using deep learning. A total of 814 post-mortem computed tomography scans from 619 men and 195 women, within the age range of 20–70, were collected from the National Forensic Service in South Korea. Multiple preprocessing steps were applied for each scan to normalize the image and perform intensity correction to create 3D voxels that represent these parts accurately. The accuracy of the proposed method was evaluated by 10-fold cross-validation. The initial cross-validation results illustrated the potential of the proposed method as it achieved a mean absolute error of 5.15 years with a concordance correlation coefficient of 0.80. The proposed approach is likely to be faster and potentially more reliable, which could be used for age assessment in the future.

Fully Automated Deep Learning System for Bone Age Assessment

Automated age estimation of young individuals based on 3D knee MRI using deep learning

AbstractAge estimation is a crucial element of forensic medicine to assess the chronological age of living individuals without or lacking valid legal documentation. Methods used in practice are labor-intensive, subjective, and frequently comprise radiation exposure. Recently, also non-invasive methods using magnetic resonance imaging (MRI) have evaluated and confirmed a correlation between growth plate ossification in long bones and the chronological age of young subjects. However, automated and user-independent approaches are required to perform reliable assessments on large datasets. The aim of this study was to develop a fully automated and computer-based method for age estimation based on 3D knee MRIs using machine learning. The proposed solution is based on three parts: image-preprocessing, bone segmentation, and age estimation. A total of 185 coronal and 404 sagittal MR volumes from Caucasian male subjects in the age range of 13 and 21 years were available. The best result of the fivefold cross-validation was a mean absolute error of 0.67 ± 0.49 years in age regression and an accuracy of 90.9%, a sensitivity of 88.6%, and a specificity of 94.2% in classification (18-year age limit) using a combination of convolutional neural networks and tree-based machine learning algorithms. The potential of deep learning for age estimation is reflected in the results and can be further improved if it is trained on even larger and more diverse datasets.

Age-related hypermineralization in the female proximal human femur

Automated detection and classification of the proximal humerus fracture by using deep learning algorithm

Hierarchical fracture classification of proximal femur X-Ray images using a multistage Deep Learning approach

Biologically informed dual deep learning for skeletal maturity prediction in pediatrics.

<h4>Background and objective</h4>Accurate bone age estimation is critical for clinical diagnostics, forensic assessments, and growth research. Traditional methods rely on manual interpretation of radiographs, which is subjective and time-consuming. This Perspective introduces a biologically informed dual deep learning framework that leverages published physiological data to conceptually support bone age prediction.<h4>Methods</h4>The framework integrates anatomical and developmental knowledge with a dual neural network architecture. One network extracts morphological features from publicly available datasets, while the second captures age-related growth patterns via supervised learning. No new human or animal data were collected. Illustrative simulations and conceptual analyses explore expected model behavior.<h4>Results</h4>Simulations indicate that incorporating biologically informed priors can improve bone age estimation. Embedding physiological knowledge promotes more stable traini

A deep learning-based approach to automatic proximal femur segmentation in quantitative CT images.

Automatic CT segmentation of proximal femur has a great potential for use in orthopedic diseases, especially in the imaging-based assessments of hip fracture risk. In this study, we proposed an approach based on deep learning for the fast and automatic extraction of the periosteal and endosteal contours of proximal femur in order to differentiate cortical and trabecular bone compartments. A three-dimensional (3D) end-to-end fully convolutional neural network (CNN), which can better combine the information among neighbor slices and get more accurate segmentation results by 3D CNN, was developed for our segmentation task. The separation of cortical and trabecular bones derived from the QCT software MIAF-Femur was used as the segmentation reference. Two models with the same network structures were trained, and they achieved a dice similarity coefficient (DSC) of 97.82% and 96.53% for the periosteal and endosteal contours, respectively. Compared with MIAF-Femur, it takes half an hour to se

Artificial Intelligence (AI)-Based Systems for Automatic Skeletal Maturity Assessment through Bone and Teeth Analysis: A Revolution in the Radiological Workflow?

Bone age is an indicator of bone maturity and is useful for the treatment of different pediatric conditions as well as for legal issues. Bone age can be assessed by the analysis of different skeletal segments and teeth and through several methods; however, traditional bone age assessment is a complicated and time-consuming process, prone to inter- and intra-observer variability. There is a high demand for fully automated systems, but creating an accurate and reliable solution has proven difficult. Deep learning technology, machine learning, and Convolutional Neural Networks-based systems, which are rapidly evolving, have shown promising results in automated bone age assessment. We provide the background of bone age estimation, its usefulness and traditional methods of assessment, and review the currently artificial-intelligence-based solutions for bone age assessment and the future perspectives of these applications.

An Automated Metaheuristic Tunicate Swarm Algorithm Based Deep Convolutional Neural Network for Bone Age Assessment Model

Automatic hip fracture detection using deep learning

TW3-Based Fully Automated Bone Age Assessment System Using Deep Neural Networks

A Deep Learning-Based Method for Automatic Segmentation of Proximal Femur from Quantitative Computed Tomography Images

Purpose: Proximal femur image analyses based on quantitative computed tomography (QCT) provide a method to quantify the bone density and evaluate osteoporosis and risk of fracture. We aim to develop a deep-learning-based method for automatic proximal femur segmentation. Methods and Materials: We developed a 3D image segmentation method based on V-Net, an end-to-end fully convolutional neural network (CNN), to extract the proximal femur QCT images automatically. The proposed V-net methodology adopts a compound loss function, which includes a Dice loss and a L2 regularizer. We performed experiments to evaluate the effectiveness of the proposed segmentation method. In the experiments, a QCT dataset which included 397 QCT subjects was used. For the QCT image of each subject, the ground truth for the proximal femur was delineated by a well-trained scientist. During the experiments for the entire cohort then for male and female subjects separately, 90% of the subjects were used in 10-fold cr

Bone Fracture Detection Based on Deep Learning Techniques

Lower Leg Bone Fracture Detection Using Deep Learning

Deep Learning-based Automated Opportunistic Osteoporosis Screening Using Chest LDCT and Lumbar CT: A Multicenter Cohort Study.

To propose a deep learning (DL) method for automatically measuring bone mineral density (BMD) and validating its diagnostic performance for opportunistic osteoporosis screening using low-dose chest computed tomography (LDCT) and lumbar CT scans across CT scanners from different manufacturers and hospitals.

Bone Age Assessment Empowered with Deep Learning: A Survey, Open Research Challenges and Future Directions

Deep learning is a quite useful and proliferating technique of machine learning. Various applications, such as medical images analysis, medical images processing, text understanding, and speech recognition, have been using deep learning, and it has been providing rather promising results. Both supervised and unsupervised approaches are being used to extract and learn features as well as for the multi-level representation of pattern recognition and classification. Hence, the way of prediction, recognition, and diagnosis in various domains of healthcare including the abdomen, lung cancer, brain tumor, skeletal bone age assessment, and so on, have been transformed and improved significantly by deep learning. By considering a wide range of deep-learning applications, the main aim of this paper is to present a detailed survey on emerging research of deep-learning models for bone age assessment (e.g., segmentation, prediction, and classification). An enormous number of scientific research publications related to bone age assessment using deep learning are explored, studied, and presented in this survey. Furthermore, the emerging trends of this research domain have been analyzed and discussed. Finally, a critical discussion section on the limitations of deep-learning models has been presented. Open research challenges and future directions in this promising area have been included as well.

Convolutional Neural Network Model based Deep Learning Approach for Osteoporosis Fracture Detection

Deep Learning-Assisted Automated Diagnosis of Osteoporosis Based on Computed Tomography Scans: Systematic Review and Meta-Analysis.

Osteoporosis is a prevalent skeletal disorder characterized by decreased bone mass and increased fracture risk; however, it frequently remains underdiagnosed due to limited health care resources and its asymptomatic progression. Deep learning (DL) provides a promising solution for automated screening using computed tomography (CT) scans, enabling earlier detection and improved management.

Diagnosis of Bone Fracture Based on Deep Learning Networks

The Role of Artificial Intelligence in Orthodontics for Determining Skeletal Age Based on Cervical Vertebra Maturation Degree: A Comprehensive Review.

<h4>Background and aims</h4>Dentofacial orthopedic treatment planning highly depends on the estimation of skeletal growth peak. In most cases, chronological age and biological age differ, some techniques estimate skeletal age by analyzing cervical vertebrae maturation (CVM) staging on lateral cephalograms. In this study, we aimed to review the different applications of AI in orthodontics and specifically discussed the different designs of AI models used for CVM estimation.<h4>Methods</h4>Comprehensive searches was conducted across databases including PubMed, Web of Science, Google scholar, Embase, and Scopus using keywords such as orthodontics, cervical vertebra maturation, skeletal age and artificial intelligence.<h4>Results</h4>Utilizing AI algorithms in assessing CVM-based skeletal age enhanced the accuracy of diagnosis, reduced analysis time and minimized observer variability. Deep learning techniques, especially convolutional neural networks (CNNs), have demonstrated promising res

Advanced Bone Fracture Detection Using Hybrid Deep Learning Algorithms and Machine Learning Models for Enhanced Medical Imaging Diagnosis

Deep Learning-Based Automated Bone Fracture Detection and Severity Quantification in X-Ray Imaging Using YOLOv8


## Conclusion


In this study, we developed a deep learning-based multioutput model for automatic bone age prediction and gender classification. Our model successfully predicts bone age with a MSE of approximately 25 and a MAE of 3.1. Additionally, it achieves high classification performance for gender, with an accuracy of 95% and an AUC of 97%. These results demonstrate that despite the challenges posed by radiograph quality, our approach achieves robust performance, surpassing existing automated models. As shown in Fig. 7, the model's performance on real X-ray radiology data further validates its effectiveness in practical scenarios.

A deep learning algorithm capable of detecting patients with osteopenia/osteoporosis (T-score < -1.0) in the femur or lumbar spine using cervical radiography was developed The diagnostic yield of the algorithm was higher than that of experienced spine surgeons After additional validation, the algorithm might serve as a low-cost screening tool for early detection and timely treatment of osteoporosis in older adult patients with cervical diseases such as DCM


## Insight


efficacy: Les algorithmes de deep learning appliqués aux radiographies ont atteint un niveau de maturité suffisant pour obtenir une approbation de la FDA, notamment pour l'estimation de l'âge osseux pédiatrique, la détection de fractures et l'évaluation de la sévérité de l'arthrose du genou et de la hanche.