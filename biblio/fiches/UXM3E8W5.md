# Smart Osteology: An AI-Powered Two-Stage System for Multi-Species Long Bone Detection and Classification Using YOLOv5 and CNN Architectures for Veterinary Anatomy Education and Forensic Applications.

**Auteurs** : Orhan İ.
**Année** : 2025
**DOI** : 10.3390/vetsci12080765

## Résumé

In this study, bone detection was performed using the YOLO algorithm on a dataset comprising photographs of the scapula, humerus, and femur from cattle, horses, and dogs. Subsequently, convolutional neural networks (CNNs) were employed to classify both the bone type and the species. Trained on a total of 26,148 images, the model achieved an accuracy rate of up to 97.6%. The system was designed to operate not only on mobile devices but also in an offline, "closed model" version, thereby enhancing its applicability in forensic medicine settings where data security is critical. Additionally, the application was structured as a virtual assistant capable of responding to users in both written and spoken formats and of generating output in PDF format. In this regard, this study presents a significant example of digital transformation in fields such as veterinary anatomy education, forensic medicine, archaeology, and crime scene investigation, providing a solid foundation for future applicati

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Dataset collected for YOLO training.

| Animal | Bone | Number of Photos | Right | Left |
| --- | --- | --- | --- | --- |
|  | Scapula | 50 | 32 | 18 |
| Horse | Humerus | 246 | 128 | 118 |
|  | Femur | 282 | 92 | 190 |
|  | Scapula | 230 | 122 | 108 |
| Cow | Humerus | 104 | 40 | 64 |
|  | Femur | 172 | 90 | 82 |
|  | Scapula | 120 | 68 | 52 |
| Dog | Humerus | 178 | 90 | 88 |
|  | Femur | 172 | 90 | 82 |
| TOTAL |  | 1554 | 752 | 802 |

## Dataset distribution and number of photos.

| Animal Species | Number of Bones | Bone Type | Number of Images | Training | Testing | Validation |
| --- | --- | --- | --- | --- | --- | --- |
| Cattle | 62 | Scapula | 2744 | 2332 | 274 | 137 |
| Cattle | 58 | Humerus | 2744 | 2332 | 274 | 137 |
| Cattle | 60 | Femur | 2744 | 2332 | 274 | 137 |
| Horse | 52 | Scapula | 2744 | 2332 | 274 | 137 |
| Horse | 56 | Humerus | 2744 | 2332 | 274 | 137 |
| Horse | 52 | Femur | 2744 | 2332 | 274 | 137 |
| Dog | 42 | Scapula | 2744 | 2332 | 274 | 137 |
| Dog | 38 | Humerus | 2744 | 2332 | 274 | 137 |
| Dog | 40 | Femur | 2744 | 2332 | 274 | 137 |
| TOTAL | 460 | 9 Classes | 24,696 | 20,988 | 2466 | 1233 |

## Configuration and hyperparameters of YOLO.

| YOLO Hyperparameters | Value | Description |
| --- | --- | --- |
| Learning Rate (lr0) | 0.01 | Initial learning rate |
| Final LR Factor (lrf) | 0.1 | Final learning rate multiplier |
| Momentum | 0.937 | SGD momentum |
| Weight Decay | 0.0005 | L2 regularization |
| Warmup Epochs | 3.0 | Number of warmup epochs |
| Box Loss Weight | 0.05 | Bounding box loss weight |
| Class Loss Weight | 0.3 | Classification loss weight |
| Object Loss Weight | 0.7 | Objectless loss weight |
| IoU Threshold | 0.2 | IoU threshold value |
| Mosaic Augmentation | 1.0 | Mosaic augmentation ratio |
| Mix-up | 0.15 | Mix-up augmentation ratio |
| Horizontal Flip | 0.5 | Horizontal flip probability |
| HSV-H | 0.015 | Hue variation |
| HSV-S | 0.7 | Saturation variation |
| HSV-V | 0.4 | Value/brightness variation |

## Training configuration and hyperparameters.

| Parameter | ResNet34 | SmallCNN | AlexNet | Rationale |
| --- | --- | --- | --- | --- |
| Learning Rate | 0.001 | 0.001 | 0.001 | Optimal convergence rate |
| Batch Size | 32 | 32 | 32 | Memory efficiency balance |
| Epochs | 100 | 100 | 100 | Sufficient convergence time |
| Optimizer | Adam | Adam | Adam | Adaptive learning rates |
| β 1 ADAM | 0.9 | 0.9 | 0.9 | Adaptive learning rates |
| β 2 ADAM Weight Decay | 0.999 1 × 10 -4 | 0.999 1 × 10 -4 | 0.999 1 × 10 -4 | Standard RMSprop term L2 regularization |
| Loss Function | CrossEntropy | CrossEntropy | CrossEntropy | Multi-class classification |
| LR Scheduler | StepLR | StepLR | StepLR | Learning rate decay |
| Step Size | 30 | 30 | 30 | Scheduler step interval |
| Gamma | 0.1 | 0.1 | 0.1 | Learning rate decay factor |
| Early Stopping | Yes (patience15) | Yes (patience15) | Yes (patience15) | Overfitting prevention |
| Class Weight | Balanced | Balanced | Balanced | Class imbalance handling |

## Performance evaluation of the YOLOv5s model for bone detection across different datasets.

| Dataset | Images | Precision (%) | Recall (%) | mAP@0.5 (%) | F1-Score (%) |
| --- | --- | --- | --- | --- | --- |
| Training | 1321 | 99.9 | 97.2 | 97.1 | 98.5 |
| Testing | 155 | 99.8 | 96.9 | 96.6 | 98.3 |
| Validation | 78 | 99.7 | 96.5 | 96.4 | 98.1 |

## Comparative performance metrics of the models used.

| Model | Accuracy (%) | F1-Score (%) | Precision (%) | Recall (%) |
| --- | --- | --- | --- | --- |
| ResNet34 | 97.6 | 97.2 | 96.8 | 97.4 |
| SmallCNN | 95.0 | 94.6 | 94.3 | 94.8 |
| AlexNet | 91.3 | 90.2 | 89.9 | 90.4 |

## Satisfaction scores by year of students (Q: question) (p > 0.05).

| Year of Student | n | Q1 | Q2 | Q3 | Q4 | Q5 | Mean |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1st Year | 45 | 4.87 ± 0.43 | 4.78 ± 0.59 | 4.91 ± 0.37 | 4.73 ± 0.58 | 4.93 ± 0.35 | 4.84 ± 0.35 |
| 2nd Year | 30 | 4.83 ± 0.48 | 4.77 ± 0.57 | 4.90 ± 0.40 | 4.67 ± 0.61 | 4.90 ± 0.40 | 4.81 ± 0.38 |
| 3rd Year | 25 | 4.76 ± 0.60 | 4.72 ± 0.68 | 4.88 ± 0.44 | 4.60 ± 0.71 | 4.88 ± 0.44 | 4.77 ± 0.44 |
| 4th Year | 25 | 4.72 ± 0.61 | 4.64 ± 0.76 | 4.80 ± 0.50 | 4.52 ± 0.77 | 4.84 ± 0.47 | 4.70 ± 0.48 |
| 5th Year | 25 | 4.80 ± 0.50 | 4.68 ± 0.69 | 4.84 ± 0.47 | 4.56 ± 0.71 | 4.88 ± 0.44 | 4.75 ± 0.42 |

## Detailed results of the student satisfaction survey (n = 150) (p > 0.05).

| Survey Question (n = 150) | Mean ± SS | 1 (%) | 2 (%) | 3 (%) | 4 (%) | 5 (%) | Positive Response (4 + 5) (%) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Q1. The application was easy to use | 4.81 ± 0.52 | 0.7 | 0.0 | 1.3 | 14.0 | 84.0 | 98.0 |
| Q2. Voice and text-based queries functioned accurately enough | 4.73 ± 0.63 | 1.3 | 0.7 | 4.0 | 18.0 | 76.0 | 94.0 |
| Q3. The application's anatomical information was satisfactory | 4.87 ± 0.43 | 0.0 | 0.7 | 2.0 | 8.0 | 89.3 | 97.3 |
| Q4. The PDF export feature was useful | 4.64 ± 0.67 | 1.3 | 2.0 | 6.0 | 20.7 | 70.0 | 90.7 |
| Q5. I was satisfied with the overall performance of the application | 4.87 ± 0.41 | 0.0 | 0.7 | 2.0 | 8.0 | 89.3 | 97.3 |
