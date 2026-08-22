# A Comprehensive Systematic Review of YOLO for Medical Object Detection (2018 to 2023)

**Auteurs** : Mohammed Gamal Ragab, Said Jadid Abdulkadir, Amgad Muneer, Alawi Alqushaibi, Ebrahim Hamid Sumiea, Rizwan Qureshi, Safwan Mahmood Al-Selwi, Hitham Alhussian
**Année** : 2024
**DOI** : 10.1109/access.2024.3386826

## Résumé

YOLO (You Only Look Once) is an extensively utilized object detection algorithm that has found applications in various medical object detection tasks. This has been accompanied by the emergence of numerous novel variants in recent years, such as YOLOv7 and YOLOv8. This study encompasses a systematic exploration of the PubMed database to identify peer-reviewed articles published between 2018 and 2023. The search procedure found 124 relevant studies that employed YOLO for diverse tasks including lesion detection, skin lesion classification, retinal abnormality identification, cardiac abnormality detection, brain tumor segmentation, and personal protective equipment detection. The findings demonstrated the effectiveness of YOLO in outperforming alternative existing methods for these tasks. However, the review also unveiled certain limitations, such as well-balanced and annotated datasets, and the high computational demands. To conclude, the review highlights the identified research gaps and proposes future directions for leveraging the potential of YOLO for medical object detection.

## Méthodologie

{'study_design': 'Systematic literature review (SLR) conducted using the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) statement.', 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': 'Studies published between 2018 and 2023', 'setting': 'PubMed database'}

## Résultats

{'quantitative': [], 'qualitative_findings': ['The findings demonstrated the effectiveness of YOLO in outperforming alternative existing methods for tasks such as lesion detection, skin lesion classification, retinal abnormality identification, cardiac abnormality detection, brain tumor segmentation, and personal protective equipment detection.', 'The review unveiled certain limitations, such as well-balanced and annotated datasets, and the high computational demands.'], 'main_findings': ['The findings reveal the pivotal role YOLO plays in enhancing the efficiency and accuracy of medical diagnoses and procedures.', 'By rapidly identifying and localizing ailments ranging from tumors to various cancers, YOLO has significantly improved patient outcomes while reducing diagnosis and treatment times.']}

## Conclusions

This SLR offers a comprehensive analysis of the utilization of YOLO in various medical applications, encompassing tumor detection, blood transfusion medicine, COVID-19, colorectal cancer, radiology, laryngeal cancer, parathyroid surgery, and dorsal hand veins recognition, among others. The integration of YOLO into healthcare applications represents a significant stride towards a future where AI not only enhances the accuracy and speed of medical processes but also democratizes access to quality healthcare. Continued research and development are essential for further improvements and for the optimal integration of YOLO into healthcare settings.

## The architecture of YOLO consists of a backbone, neck, and head. Backbone, neck, and head varies in different versions of YOLO. For backbone, normally Darknet, VGG16, or Resnet are used; for neck feature pyramid network (FPN)

| Backbone | Neck | Head |
| --- | --- | --- |
| Features Extractions | Features Aggregation | Final Predictions |
| FIGURE 2: |  |  |

## Table 1

| summarizes the key features of each |
| --- |
| version of YOLO. |

## This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3386826

| iv | VOLUME 11, 2023 |
| --- | --- |

## Key features of each version of YOLO

|  | Version | Date Anchor | Framework | Backbone | AP (%) |
| --- | --- | --- | --- | --- | --- | --- |
|  | YOLO | 2015 | × | Darknet | Darknet24 | 63.4 |
|  | YOLOv2 | 2016 | ✓ | Darknet | Darknet24 | 63.4 |
|  | YOLOv3 | 2018 | ✓ | Darknet | Darknet53 | 36.2 |
|  | YOLOv4 | 2020 | ✓ | Darknet | CSPDarknet53 | 43.5 |
|  | YOLOv5 | 2020 | ✓ | Pytorch | Modified CSP v7 | 55.8 |
|  | PP-YOLO | 2020 | ✓ | PaddlePaddle | ResNet50-vd | 45.9 |
|  | Scaled-YOLOv4 2021 | ✓ | Pytorch | CSPDarknet | 56.0 |
|  | PP-YOLOv2 | 2021 | ✓ | PaddlePaddle | ResNet101-vd | 50.3 |
|  | YOLOR | 2021 | ✓ | Pytorch | CSPDarknet | 55.4 |
|  | YOLOX | 2021 | × | Pytorch | Modified CSP v5 | 51.2 |
|  | PP-YOLOE | 2022 | × | PaddlePaddle | CSPRepResNet | 54.7 |
|  | YOLOv6 | 2022 | × | Pytorch | EfficientRep | 52.5 |
|  | YOLOv7 | 2022 | × | Pytorch | RepConvN | 56.8 |
|  | DAMO-YOLO | 2022 | × | Pytorch | MAE-NAS | 50.0 |
|  | YOLOv8 | 2023 | × | Pytorch | YOLOv8 | 53.9 |
|  | YOLO-NAS | 2023 | × | Pytorch | YOLO-NAS | 52.2 |
| denoted as B gt , while the predicted box is represented as B. | recognition, and image segmentation [72]. By annotating |
| The probability (p) signifies whether the object exists within | images, human annotators or data scientists manually outline |
| the detected bounding box. The Intersection over Union (IoU) | or mark the objects of interest within the image, often by |
| metric, defined by Equation 2, calculates the intersection area | drawing bounding boxes, polygons, or semantic segmenta- |
| between the ground truth and predicted bounding boxes. It | tions around those objects. Accurate annotations are crucial |
| determines an acceptable area for each detected object in the | for training models to accurately detect, recognize, and seg- |
| input image and makes decisions based on it. To obtain the | ment objects. They provide ground truth data, enable object |
| most suitable bounding box, the confidence value is applied | localization, ensure model accuracy and performance, and |
| after the estimation. The process of computation of the IoU | facilitate diverse and domain-specific datasets. Annotations |
| can be illustrated as shown in Figure 4. |  |  | also aid in model evaluation and serve as a valuable resource |
|  |  |  |  | for transfer learning. In summary, image annotation is a fun- |
|  |  |  |  | damental step that underpins the development of reliable and |
|  |  |  | Poor | effective computer vision systems in various industries and |
|  |  |  |  | applications |
|  |  |  | (a) |  |  |
| 𝐼𝑜𝑈 = | 𝐴𝑟𝑒𝑎 𝑜𝑓 𝑈𝑛𝑖𝑜𝑛 𝐴𝑟𝑒𝑎 𝑂𝑣𝑒𝑟𝑙𝑎𝑝 |  | Good |  |  |
|  |  |  | (b) |  |  |
|  |  |  | Excellent |  |  |
|  |  |  | (c) |  |  |
| FIGURE 4: Computing the Intersection over Union: (a) poor detection performance, (b) good detection performance, |  |  |
| (c) excellent detection performance |  |  |  |  |
| D. IMAGE ANNOTATION |  |  |  |  |
| Image annotation [70] is a vital process in computer vision |  |  |
| and machine learning. It is the process of labeling or marking |  |  |
| specific objects or regions of interest within an image [71]. It |  |  |
| involves adding metadata or annotations to images to provide |  |  |
| additional information about the objects or features present |  |  |
| in the image. The purpose of image annotation is to create |  |  |
| a labeled dataset that serves as training data for learning |  |  |
| algorithms, particularly for tasks like object detection, object |  |  |

## YOLO included studies categorized in the Oncology domain

| Ref. | Application | YOLO v. | Dataset Metrics |
| --- | --- | --- | --- | --- |
| Cheng et al. 2021, [94] | Bone metastasis detection | YOLOv4 | D32 | Sensitivity 0.72 ± 0.04 |
|  |  |  |  | Precision 0.90 ± 0.04 |
| Li et al. 2021, [95] | Cell viability assay | YOLOv3 | D31 | Accuracy 0.94 |
|  |  |  |  | Sensitivity 0.936 |
|  |  |  |  | Specificity 0.944 |
| Ku et al. 2022, [93] | Gastroscopy | YOLOv5 | D24 | Precision 0.98 |
|  |  |  |  | Recall 0.89 |
|  |  |  |  | mAP 0.902 |

## YOLO included studies categorized in the Pathology domain

| Ref. | Application | YOLO v. | Dataset Metrics |
| --- | --- | --- | --- | --- |
| Larpant et al. 2022, [96] | Hematology (Blood transfusion) | YOLOv4-tiny D1 | Accuracy 0.966 |
|  |  |  |  | Sensitivity 0.919 |
|  |  |  |  | Specificity 0.9894 |
|  |  |  |  | AUC 0.99 |
| Han et al. 2023, [97] | Hematology (White blood cell | MID-YOLO | D3 | mAP@.5: 99.11% |
|  | detection) |  |  | mAP@.75: 96.54 |
|  |  |  |  | mAP@.5:.95: 81.13 |
|  |  |  |  | Precision: 1.81% higher than original |
| Rong et al. 2023, [31] | Histology-based Nucleus | YOLOv5 | D16 | Accuracy 0.7110 |
|  | Segmentation and Detection |  |  | Precision 0.8308 |
|  |  |  |  | Recall 0.6743 |
|  |  |  |  | F1-score 0.7409 |
|  |  |  |  | mIoU 0.8423 |
| Quan et al. 2023, [98] | Human epidermal growth factor | YOLOv5 | D12 | Precision 0.81 |
|  | receptor 2 (HER2) |  |  |  |
| Zhu et al. 2023, [99] | Sperm detection | YOLOv5s | D36 | Sensitivity 0.9362 |
|  |  |  |  | Precision 0.6435 |
|  |  |  |  | F1-score 0.7363 |
| Sun et al. 2021, [100] | Neuroscience | YOLOv1 | D41 | Accuracy 0.75 |
|  |  |  |  | AUC 0.743 |
|  |  |  |  | Sensitivity 0.80 |
|  |  |  |  | Specificity 0.72 |
| Afshari et al. 2018, [81] | Tumor localization | YOLOv3 | D17 | Precision 0.75 to 0.98 |
|  |  |  |  | Recall 0.94 to 0.1 |
|  |  |  |  | IoU 0.72 |
| Guo et al. 2022, [80] | Vitiligo Lesions | YOLOv3 | D28 | Sensitivity 0.962 |
|  |  |  |  | CPM value of 0.905 |
| Huang et al. 2023, [101] | Yeast cell detection | YOLOv5 | D43 | Accuracy 0.942 |
| system performs preprocessing on DICOM-format mammo- | B. SURGICAL PROCEDURES |
| grams to convert them into images while preserving all the data. It is capable of detecting masses in full-field digital mammograms and can differentiate between malignant and benign lesions automatically, without requiring any human | YOLO could also be applied in surgical procedures. It offers great potential for surgical procedures, particularly in the con-text of computer-assisted and robotic surgery. The algorithm's |
| intervention, significantly reducing the potential for human |  |  |  |
| error and streamlining the entire process. |  |  |  |

## YOLO included studies categorized in the Radiology domain

| Ref. | Application | YOLO v. | Dataset Metrics |
| --- | --- | --- | --- | --- |
| Safdar et al. 2020, [32] | Brain tumor detection | YOLOv3 | D27 | Accuracy 0.60 to 0.96 |
| Al-Antari et al. 2020, [17] Breast cancer detection | YOLOv3 | D10 | Accuracy 0.991 and 0.972 |
|  |  |  |  | F1-scores 0.992 and 0.980 |
| Aly et al. 2021, [90] | Breast cancer detection | YOLOv3 | D11 | Accuracy 0.98 |
|  |  |  |  | Precision 0.95 |
|  |  |  |  | Recall 0.90 |
|  |  |  |  | F1-score 0.925 |
| Fu et al. 2022, [92] | Breast cancer detection | YOLOv3 | D15 | Accuracy 0.9067 |
|  |  |  |  | Precision 0.9281 |
| Baccouche et al. 2022, [19] Breast cancer diagnosis | YOLOv1 | D13 | Accuracy 0.92 |
| Al-Antari et al. 2020, [79] Breast lesions diagnosis | YOLOv3 | D22 | Accuracy 0.9727 |
|  |  |  |  | F1-score 0.9802 |
| Su et al. 2022, [91] | Breast mass detection and | YOLOv5 | D14 | Accuracy 0.957 |
|  | segmentation |  |  | Precision 0.650 |
|  |  |  |  | F1-score 0.745 |
|  |  |  |  | IoU 0.640 |
| Zhuang et al. 2020, [38] | Cardiovascular disease | YOLOv3 | D8 | Accuracy 0.952 |
|  |  |  |  | Precision 0.964 |
|  |  |  |  | Recall 0.940 |
|  |  |  |  | F1-score 0.952 |
| Chen et al. 2023, [102] | Cardiovascular disease | YOLOv3 | D39 | Accuracy 0.9481 |
| Al-Masni et al. 2020, [103] Cerebral microbleeds detection | YOLOv2 | D20 | Sensitivity 0.93.62 |
|  |  |  |  | FP avg 52.18 and 155.50 |
| Nambu et al. 2022, [104] Cervical cytology of squamous cell | YOLOv4 | D30 | Accuracy 0.905 |
|  | atypia |  |  | F-measure 0.705 |
| Boonrod et al. 2022, [105] Cervical spine injury detection | YOLOv4 | D21 | Accuracy 0.75 |
|  |  |  |  | Sensitivity 0.80 |
|  |  |  |  | Specificity 0.72 |
| Tang et al. 2022, [106] | Colon polyps detection | YOLOv4 | D34 | Accuracy 0.8428, 0.7517 and 0.8643 |
|  |  |  |  | mAP 86.8422 , 72.1863 and 77.6162 |
| Pacal et al. 2022, [40] | Colorectal cancer (CRC) | YOLOv4 | D4 | Precision 82.33 to 88.62 |
|  |  |  |  | Recall 71.01 to 77.55 |
|  |  |  |  | F1-score 76.25 to 82.16 |
|  |  |  |  | mAP 74.52 to 96.22 |
| Matsui et al. 2021, [107] | Colorectal cancer (CRC) | YOLOv3 | D33 | IoU 0.9374 and 0.9077 |
| Tang et al. 2023, [108] | Colorectal cancer (CRC) | YOLOv3 | D35 | AP 0.5460 and 0.7541 |
|  |  |  |  | mAP 0.7007 |
|  |  |  |  | IoU 0.5724 |
| Ozturk et al. 2020, [109] | COVID-19 detections | YOLOv3 | D2 | Accuracy 0.9808 |
|  |  |  |  | Sensitivity 0.8535 |
|  |  |  |  | Specificity 0.9218 |
|  |  |  |  | F1-score 0.8737 |
| Kong et al. 2023, [110] | Dentistry | YOLOv4 | D42 | Accuracy 0.762 |
|  |  |  |  | FPS 39.4 |

## YOLO included studies categorized in the Radiology domain

| Ref. | Application | YOLO v. | Dataset Metrics |
| --- | --- | --- | --- | --- |
| Panyarak et al. 2023, [111] Dental caries in bitewing | YOLOv7 | D45 | Precision (0.557 vs. 0.268) |
|  | radiographs | vs |  | F1-score (0.555 vs. 0.375) |
|  |  | YOLOv3 |  | mAP (0.562 vs. 0.458) |
| Tian et al. 2022, [112] | Dorsal hand veins detection | YOLO Nano- | D9 | AP 0.9323 |
|  |  | Vein |  |  |
| Pang et al. 2019, [113] | Gallstone detection | YOLOv3 | D5 | Accuracy 0.927 |
|  |  |  |  | mAP 0.943 |
| Azam et al. 2022, [114] | Laryngeal cancer detection | YOLOv5s | D6 | Precision 0.92 |
|  |  |  |  | Recall 0.90 |
|  |  |  |  | F1-score 0.91 |
| Tsai et al. 2021, [115] | Lumbar disc herniation detection YOLOv3 | D38 | Accuracy 0.736 |
|  |  |  |  | mAP 0.769 |
| Huang et al. 2022, [88] | Lung nodule detection | YOLOv3 | D47 | Sensitivity 0.962 |
|  |  |  |  | FPR 8 |
|  |  |  |  | CPM 0.905 |
| Zhang et al. 2023, [116] | Microaneurysm detection | YOLOv8 | D44 | Recall 0.8823 |
|  |  |  |  | Precision 0.9798 |
|  |  |  |  | F1-score 0.9285 |
|  |  |  |  | AP 0.9462 |
| Rouzrokh et al. 2021, | Orthopedics | YOLOv3 | D37 | Accuracy 0.495 |
| [117] |  |  |  | Sensitivity 0.890 |
|  |  |  |  | Specificity 0.488 |
| Ma et al. 2021, [118] | Pulmonary hypertension | YOLOv3 | D26 | mAP 0.8225 |
|  |  |  |  | Recall 0.9412 |
|  |  |  |  | Precision 0.9661 |
| Ahmadyar et al. 2023, [87] Pulmonary nodule detection | YOLOv5s | D46 | Accuracy 0.984 |
|  |  |  |  | AUC 0.989 |
| Lee et al. 2023, [119] | Rotator cuff tear screening | YOLOv8 | D48 | Accuracy 0.96 |
|  |  |  |  | Sensitivity 0.98 |
|  |  |  |  | Precision 0.98 |
|  |  |  |  | Specificity 0.91 |
|  |  |  |  | F1-score 0.97 |
|  |  |  |  | AUC 0.94 |
| Fu et al. 2022, [120] | Spinal cerebrospinal fluid | YOLOv3 | D29 | Specificity 0.917 |
|  | segmentation |  |  | AUC 0.810 |
| Lv et al. 2022, [121] | Traditional Chinese medicine | YOLOv5 | D25 | Accuracy 0.9433 |
|  | recognition |  |  | FPS 75 |
| Till et al. 2023, [122] | Wrist fractures in children | YOLOv7 | D40 | mAP@0.5 +25.51% |
|  |  |  |  | mAP@[0.5:0.95] +39.78% |

## YOLO included studies categorized in the Surgical Procedures domain

| Ref. | Application | YOLO v. | Dataset Metrics |
| --- | --- | --- | --- | --- |
| Wang et al. 2022, [83] | Parathyroid surgery | YOLOv3, | D7 | Precision 0.887 |
|  |  | Faster R-CNN, |  | Recall 0.923 |
|  |  | and Cascade |  | F1-score 0.905 |
|  |  | algorithms |  |  |
| Amiri Tehrani Zade et al. | Ultrasound Interventions (needle | YOLOv3 | D23 | Accuracy 0.98 |
| 2023, [84] | placement) |  |  |  |

## YOLO included studies categorized in the Personal Protective Equipment Detection domain

| Ref. | Application | YOLO v. | Dataset Metrics |
| --- | --- | --- | --- | --- |
| Han et al. 2022, [21] | Face mask detection | YOLOv4-tiny D18 | mAP 0.6701% |
|  |  |  |  | Speed 92.81 FPS |
| Loey et al. 2021, [125] | Face mask detection | YOLOv2 | D19 | mAP 0.81 |

## ). Not open access. D10 [17] Breast cancer The DDSM dataset with over 26,000 mammograms and the INbreast dataset with 410 mammograms. Breast cancer Pre-operative breast ultrasound videos and clinical parameters from 807 breast cancer patients who visited the Shanghai Cancer Center at Fudan University between February 2019 and July 2020. Ultrasound Interventions Obtained from an injection needle inserted into two ultrasound phantoms: the Ultrasound Compatible Lumbar Epidural Simulator and the Femoral Vascular Access Ezono phantom, consisting of 14 ultrasound sequences, each with 100 frames. Vitiligo lesions The research utilized data from two sources: a dataset of vitiligo lesions from Chinese patients with Fitzpatrick skin types III or IV, and a test set of 145 images of vitiligo lesions from patients with Fitzpatrick skin types I, II, or V. MRM image slices, acquired from various scanners and protocols, these images varied in quality but consistently depicted spinal CSF. Expert manual labeling identified the spinal CSF in each slice. The HT29 Cell Dataset features images of various sizes and resolutions, showcasing diverse light scattering patterns from live, dead, and dying cells. It includes images of 575 live HT29 cells and 575 dead HT29 cells. Chest bone scintigraphy images from 205 prostate cancer patients and 371 breast cancer patients, acquired using a SPECT scanner. Radiologists labeled the images to indicate the presence or absence of bone metastasis.

| D23 [84] Not open access. |
| --- | --- | --- |
| D24 [93] Gastroscopy | Microsoft COCO: 31,117 images from 3,747 patients, all digitized using the same endoscope and annotated with lesion type | COCO |
|  | and location. |  |
| D25 [121] Traditional Chinese | TCM: manually collected dataset of 100 common TCM images from pharmacies, all digitized using the same camera and | Not open access. |
| Medicine | annotated with the location and type of TCM. |  |
| D26 [118] Pulmonary hypertension | The dataset contains MRI images of PH patients, digitized with the same scanner and annotated for the right ventricle | Not open access. |
|  | location. All images are in DICOM format. |  |
| D27 [32] Brain tumor detection | 1,961 MRI brain scan images of low-grade glioma patients, all digitized with the same scanner and annotated with tumor | TCIA |
|  | locations and obtained from TCIA |  |
| D28 [80] Not open access. |
| D29 [120] Spontaneous intracranial | 25,603 Not open access. |
| hypotension |  | DDSM, INbreast |
| D11 [90] Breast mass detection D30 [104] Cervical cytology | INbreast: 410 mammograms from 115 cases: 360 from 90 bilateral breast cases (4 per case) and 50 from 25 mastectomy cases (2 per case), including normal, benign, and malignant cases. Pap smears. Two expert cytopathologists annotated the images. Images were obtained through liquid-based cytology (LBC), a less invasive cervical cell collection method than traditional | INbreast Not open access. |
| assay) D12 [98] Not open access. D31 [95] Oncology (Cell viability Not open access. |
| D13 [19] Breast cancer detection) D32 [94] Oncology (Bone metastasis | A private digital mammographic database. It includes 413 cases, consisting of four categories: Mass, Calcification, Architec-tural Distortions, and Normal. | Not open access. Not open access. |
| D14 [91] Breast cancer D33 [107] Colorectal cancer | I) INbreast: 410 mammograms from 115 cases. II) CBIS-DDSM: 10,240 mammograms which is a subset of the DDSM data selected and curated by a trained mammographer. colorectal lesions. Radiologists identified and labeled these lesions. Extracted from video records from 20 colonoscopy procedures, with images extracted at five-second intervals focusing on | DDSM INbreast, CBIS-Not open access. |
| D15 [92] Breast cancer detection | I) Breast Ultrasound Image (BUSI): 1,577 ultrasound images of breast lesions. II) DDSM database contains 2,620 breast | BUSI, DDSM |
|  | cases across 43 volumes, with four mammograms per case. |  |
| D16 [31] Pathology | Different datasets for lung, liver, and breast cancer tissue (National Lung Screening Trial data set, NuCLS, and Cancer | Link |
|  | Genome Atlas) |  |
| D17 [81] Tumor Localization | PET scans of 156 patients from The Tumor Cancer Imaging Archive (TCIA) which contains PET scans of the whole body. | TCIA |
| D18 [21] Face mask detection | I) MAFA: 30,811 Internet images and 35,806 annotated masked faces. II) WIDER FACE Mask: 30,000 images of people | MAFA, WIDER |
|  | wearing face masks in a variety of settings, and collected from public places. | FACE |
| D19 [125] Face mask detection | A combined dataset from MMD (682 images) and FMD (853 images) for different people wearing face masks. | MMD, FMD |
| D20 [103] Cerebral microbleeds | The study used two MR image datasets from Gachon University Gil Medical Center: a high-resolution set with 72 subjects | Link. |
| detection | (188 CMBs) and a low-resolution set with 107 subjects (572 CMBs), both annotated with CMB locations. |  |
| D21 [105] Cervical spine injury | Lateral neck or cervical spine X-rays from 625 patients with CT scans, annotated for cervical spine injuries based on CT | Not open access. |
| detection | reports. |  |
| D22 [79] Breast lesions | The INbreast database has 410 mammograms from 115 cases: 360 from 90 bilateral breast cases (4 per case) and 50 from 25 | INbreast |
|  | mastectomy cases (2 per case), including normal, benign, and malignant cases. |  |

### Formule


$$IoU = B ∩ B gt B ∪ B gt (2)$$

### Formule


$$      c i x y w h c i x y w h • • • • • • • • • • • • • • • c i x y w h c i x y w h      $$

### Formule


$$b x = σ (t x ) + c x b y = σ (t y ) + c y b w = (p w ) * e tw b h = P h * e th$$
