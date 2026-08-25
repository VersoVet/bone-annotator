# A Systematic Literature Review of You Only Look Once Architectures (v1-v12) in Healthcare Systems.

**Auteurs** : Sahingoz OK, Karatas Baydogmus G, Kugu E.
**Année** : 2026
**DOI** : 10.3390/diagnostics16060935

## Résumé

<b>Background/Objectives</b>: The integration of deep learning and computer vision into healthcare has improved medical diagnosis and image analysis. Among object detection algorithms, the YOLO family has attracted substantial attention due to its ability to analyze images in real time with reported improvements in detection performance across multiple studies. This systematic review examines the evolution of YOLO algorithms for diagnostic applications in healthcare from YOLOv1 to YOLOv12. <b>Methods</b>: Peer-reviewed scientific articles published up to 1 January 2026 were retrieved from major scientific databases in accordance with PRISMA 2020 guidelines. The included studies applied YOLO models to medical imaging tasks, including disease and lesion detection and support for clinical procedures. Performance was synthesized using reported metrics such as average precision, accuracy, inference time, and computational efficiency. <b>Results</b>: The reviewed literature suggests progress

## Méthodologie

{'study_design': 'Systematic literature review conducted in accordance with PRISMA 2020 guidelines, involving a defined research question, inclusion/exclusion criteria, a search strategy across major scientific databases, and synthesis of retrieved studies', 'intervention': None, 'control': None, 'primary_outcomes': ['Reported detection/diagnostic performance of YOLO models (average precision, accuracy)', 'Inference time and computational efficiency of YOLO models'], 'secondary_outcomes': ['Frequency of use of different YOLO versions across studies', 'Application domains (radiological, pathological, ophthalmological, endoscopic)', 'Technical challenges and limitations reported in the literature'], 'statistical_methods': ['Narrative/qualitative synthesis of reported performance metrics', 'Frequency analysis of model usage and challenge categories'], 'duration': 'Studies published up to 1 January 2026', 'setting': 'Peer-reviewed scientific literature retrieved from major scientific databases'}

## Résultats

{'quantitative': [{'outcome': 'Proportion of studies using YOLOv5 and YOLOv8', 'value': 'close to 90%', 'unit': '% of studies reviewed', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'The frequency of model usage analysis clearly shows that YOLOv5 and YOLOv8 are the most widely used models, comprising close to 90% of the studies reviewed, indicating a clear preference for models that provide a good trade-off between detection accuracy and computational complexity.'}, {'outcome': 'Studies reporting limitations of computational efficiency', 'value': '36.6', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'The most common problems are the limitations of computational efficiency (36.6%), the difficulty of fine-grained lesion localization (35.5%), the limitations of the dataset (32.3%), and multimodal complexity (29.0%).'}, {'outcome': 'Studies reporting difficulty of fine-grained lesion localization', 'value': '35.5', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'The most common problems are the limitations of computational efficiency (36.6%), the difficulty of fine-grained lesion localization (35.5%), the limitations of the dataset (32.3%), and multimodal complexity (29.0%).'}, {'outcome': 'Studies reporting dataset limitations', 'value': '32.3', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'The most common problems are the limitations of computational efficiency (36.6%), the difficulty of fine-grained lesion localization (35.5%), the limitations of the dataset (32.3%), and multimodal complexity (29.0%).'}, {'outcome': 'Studies reporting multimodal complexity', 'value': '29.0', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'The most common problems are the limitations of computational efficiency (36.6%), the difficulty of fine-grained lesion localization (35.5%), the limitations of the dataset (32.3%), and multimodal complexity (29.0%).'}], 'qualitative_findings': ['YOLO-based models are most frequently employed in cancer detection, lesion localization, fracture identification, and pulmonary disease analysis', 'Cancer-related studies form one of the largest thematic clusters', 'The trend towards YOLOv9-YOLOv12 models indicates a shift towards better feature aggregation, attention, and efficiency, although clinical usage remains relatively low', 'Recent research increasingly uses transfer learning, multi-scale feature fusion, hybrid CNN-Transformer models, and lightweight models to address identified challenges'], 'main_findings': ['YOLO architectures have evolved into a popular detection solution in healthcare, especially in radiological and optical imaging', 'YOLOv5 and YOLOv8 are the most widely used architectures, reflecting a favorable trade-off between accuracy and computational complexity', 'YOLO-based methods demonstrate strong performance across radiological, pathological, ophthalmological, and endoscopic applications', 'High accuracy and fast inference alone are insufficient for real-world diagnostic adoption; interpretability, clinical validation, and system integration remain critical challenges']}

## Conclusions

YOLO models have matured into robust and optimized solutions for medical image analysis Challenges remain in interpretability, cross-institution generalization, and deployment on edge devices YOLO architectures have established themselves as foundational components of real-time computer vision for medical diagnostics, offering an effective balance between speed and detection accuracy Future research should focus on explainable YOLO-based diagnostic models, standardized benchmarking across heterogeneous medical datasets, multi-center clinical evaluations, and algorithmic designs aligned with clinical reasoning, regulatory requirements, and patient safety standards

## Inclusion and exclusion criteria.

| Inclusion Criteria | Exclusion Criteria |
| --- | --- | --- | --- |
|  |  | • | Studies not applying YOLO- |
| • • • • • | Peer-reviewed journal articles; Studies explicitly using YOLO or its variants (e.g., YOLOv3, YOLOv5, YOLOv11); Applications within healthcare contexts (e.g., medical imaging, patient monitoring, disease detection); Publications in English; Articles published between 2018 and 1 January 2026. | • • • • • • | based architectures; Papers outside the healthcare domain (e.g., agriculture, industrial or general surveillance); Review papers, editorials, white papers, or non-peer-reviewed sources; Articles without accessible full-text; Publications in language other than English; Publication before 2018; Studies focused on dentistry |
|  |  |  | (excluded to maintain a |
|  |  |  | focused scope). |

## Study quality assessment framework across five domains.

| Domain | Key Evaluation Criteria | Reporting Level (Scoring) | Interpretation |
| --- | --- | --- | --- |
| Dataset Transparency | Dataset source clearly stated; sample size reported; class distribution described | 2 = Fully reported 1 = Partially reported 0 = Not reported | Evaluates reproducibility and adequacy of data representation |
| Validation Strategy | Clear train/validation/test split; use of cross-validation; external validation (if applicable) | 2 = Robust validation inadequate validation (Cross Validation and/or external validation) 1 = Basic split only 0 = Unclear or | Assesses methodological rigor and reliability of performance claims |
|  | Standard metrics (mAP, | 2 = Comprehensive |  |
|  | sensitivity, specificity, | metrics | Measures transparency |
| Performance | precision, recall); | 1 = Standard metrics | and statistical |
| Reporting | multiple complementary | only | robustness of reported |
|  | metrics; confidence | 0 = Limited or unclear | results |
|  | intervals reported | metrics |  |
| Overfitting Assessment | Absence of data leakage; justified augmentation strategy; external/generalization testing | 2 = Explicit overfitting provided mitigation and generalization analysis 1 = Partial discussion 0 = No evidence | Evaluates model generalizability and robustness |
| Clinical Relevance | Addresses real diagnostic need; clinical interpretation of outputs; deployment considerations integration) (workflow, edge devices, | 2 = Strong clinical study integration 1 = Partial clinical discussion 0 = Purely technical | Assesses practical applicability in healthcare environments |

## Ref, Year Keywords Used YOLO Models Review Type Focus Area Year Span Used Databases/Datasets

| [17], | YOLO, single stage detection, YOLOv10, YOLOv11, performance evaluation; deep neural network; real-time object detection | YOLOv1 to YOLOv11 | Systematic | Evolution and benchmarks in healthcare, autonomous systems, and agriculture. | 2015-2023 | IEEEXplore, SpringerLink, CVPR, ICCV, ECCV |
| --- | --- | --- | --- | --- | --- | --- |
| [18], | Autonomous driving, object detection, YOLO algorithm, applications | YOLOv1 to YOLOv12 | Non-systematic | Autonomous driving scenarios (vehicles, pedestrians, signs, lights, lane lines). | 2017-2024 | Science Direct, Web of Science , IEEEXplore |
| [19], | Lightweight YOLO, Resource-constrained, SLR | YOLOv1 to YOLOv11 | Systematic | Optimization for edge devices (pruning, quantization, KD). | 2016-2024 | MDPI, Springer, IEEE, Elsevier, Frontiers, Tech Science, SAGE, IET |
|  | YOLO variants; real-time defect |  |  |  |  |  |
| [20], | detection; fabric detection; deep learning in textiles; convolutional neural networks; textile industry; | YOLO-v1 to YOLO-v11 | Systematic | Automated quality control in textiles (tears, stains, holes). | N/A | N/A |
|  | quality control |  |  |  |  |  |
| [21], | YOLO, healthcare applications, artificial intelligence, medical object systematic review detection, medical imaging, | YOLOv1 to YOLOv8 | Systematic | Medical diagnostics (oncology, surgical tools). pathology, radiology, | 2018-2023 PubMed |
| [22], | YOLO, UAV, object detection, interdisciplinary, application | YOLOv1 to YOLOv7 | Non-systematic | Aerial monitoring in engineering, agriculture, and rescue. | 2017-2022 | Web of Science, KCI, MEDLINE®, SciELO, CNKI |
| [23], | industrial defect detection; object detection; smart manufacturing; quality inspection | YOLOv1 to YOLOv8 | In-depth Review | Industrial surface defect detection. | 2015-2022 N/A |
|  | Deep learning, Images, Fruit |  |  |  |  |  |
| [24], | detection, Computer vision, Transfer learning, Automation, | YOLOv1 to YOLO-NAS | Systematic | Agricultural object recognition (crops, pests, diseases, animals). | 2015-2024 Scopus |
|  | Digital tools |  |  |  |  |  |

## Frequency of reported technical challenges and corresponding mitigation strategies in YOLO-based healthcare studies.

| Challenges | Possible Solutions |
| --- | --- |

## Keyword occurrences and total link strength.

| ID | Keyword | Occurrences | Total Link Strength |
| --- | --- | --- | --- |
| 1 | deep learning | 186 | 366 |
| 2 | object detection | 81 | 170 |
| 3 | YOLO | 79 | 210 |
| 4 | artificial intelligence | 47 | 89 |
| 5 | computer vision | 33 | 74 |
| 6 | YOLOv8 | 33 | 78 |
| 7 | machine learning | 24 | 48 |
| 8 | YOLOv5 | 23 | 46 |
| 9 | attention mechanism | 18 | 38 |
| 10 | convolutional neural network | 18 | 33 |
| 11 | feature extraction | 16 | 80 |

## Comparative analysis of YOLO models across healthcare systems.

| Healthcare |  |  |
| --- | --- | --- |
| Domain-Specific | YOLO Models and Enhancements | Performance Metrics and Comparison |
| Application |  |  |
|  | CE-YOLO: Incorporates Partial Channel Cross-Stage |  |
| Gastroenterology-Colorectal Polyp | Connections (PCST) and Dynamic Cross-Branch Fusion (DCBM) for highly efficient, lightweight processing |  |
| Detection |  |  |

### Formule


$$Accuracy = TP + TN TP + TN + FP + FN(1)$$

### Formule


$$IoU = Areao f Overlap Areao f Union(2)$$

### Formule


$$mAP = 1 N N ∑ i=1 AP i(3)$$

### Formule


$$Precision = TP TP + FP(4)$$

### Formule


$$Recall = TP TP + FN(5)$$

### Formule


$$F1-Score = 2 × Precision × Recall Precision + Recall(6)$$
