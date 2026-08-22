# Table 3: Image annotation process configuration.

**Auteurs** : Shuang Chin, Jian Dong, Khairunnisa Hasikin, Romano Ngui, Khin Lai, Pauline Yeoh, Xiang Wu
**Année** : 2024
**DOI** : 10.7717/peerjcs.2180/table-3

## Résumé

Background. Bacterial image analysis plays a vital role in various fields, providing valuable information and insights for studying bacterial structural biology, diagnosing and treating infectious diseases caused by pathogenic bacteria, discovering and developing drugs that can combat bacterial infections, etc. As a result, it has prompted efforts to automate bacterial image analysis tasks. By automating analysis tasks and leveraging more advanced computational techniques, such as deep learning (DL) algorithms, bacterial image analysis can contribute to rapid, more accurate, efficient, reliable, and standardised analysis, leading to enhanced understanding, diagnosis, and control of bacterial-related phenomena. Methods. Three object detection networks of DL algorithms, namely SSD-MobileNetV2, EfficientDet, and YOLOv4, were developed to automatically detect Escherichia coli (E. coli) bacteria from microscopic images. The multi-task DL framework is developed to classify the bacteria according to their respective growth stages, which include rod-shaped cells, dividing cells, and microcolonies. Data preprocessing steps were carried out before training the object detection models, including image augmentation, image annotation, and data splitting. The performance of the DL techniques is evaluated using the quantitative assessment method based on mean average precision (mAP), precision, recall, and F1-score. The performance metrics of the models were compared and analysed. The best DL model was then selected to perform multi-task object detections in identifying rod-shaped cells, dividing cells, and microcolonies.Results. The output of the test images generated from the three proposed DL models displayed high detection accuracy, with YOLOv4 achieving the highest confidence score range of detection and being able to create different coloured bounding boxes for different growth stages of E. coli bacteria. In terms of statistical analysis, among the three proposed models, YOLOv4 demonstrates superior performance, achieving the highest mAP of 98% with the highest precision, recall, and F1-score of 86%, 97%, and 91%, respectively.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Table 1 List of techniques from reviewed articles used for bacteria detection and classification using ML and DL approaches.

| Method Model | Data | Feature | Type of | Dataset | Performance | Authors |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Preprocessing | selection | bacteria |  | evaluation |  |
| Machine | RF | • Data annotation | Pixel features | M. tuberculosis | 116 ZN-stained | Acc = 67.98% | Ayas & Ekinci |
| learning |  | • Image denoising |  | bacteria | sputum smear | Se = 89.34% | (2014) |
|  |  | • Connected |  |  | light-field | Sp = 62.89% |  |
|  |  | component analysis |  |  | microscopic images |  |  |
|  |  | • Image rotation |  |  | collected from 5 |  |  |
|  |  | • Image resize |  |  | different slides |  |  |
|  |  | • Pixel |  |  | taken from 5 |  |  |
|  |  | segmentation |  |  | patients |  |  |
|  | K-means | • Grayscale | SURF and | Bacteria | 200 bacterial | Acc = 97% | Mohamed & |
|  | clustering | conversion | LoH | species | microscopic images |  | Afify (2018) |
|  | + SVM | • Histogram |  |  | obtained from the |  |  |
|  |  | equalization |  |  | DIBaS dataset |  |  |
|  |  | • Rescaling of |  |  |  |  |  |
|  |  | image |  |  |  |  |  |
|  | SVM | • Image | ZMI and | Pathogenic | 600 optical | Acc = 90.33% | Rahmayuna et |
|  |  | cropping | texture | bacteria | images downloaded | Se = 97.33% | al. (2018) |
|  |  | • CLAHE | features |  | from the Kaggle | Sp = 90.44% |  |
|  |  |  |  |  | website |  |  |
| Deep | CNN-based | • Data | X | M. tuberculosis | Original dataset: | AUC = 99% | López et al. |
| learning |  | augmentation |  | bacteria | 9,770 patches | Acc = 99% | (2017) |
|  |  | • Grayscale |  |  | extracted from 492 |  |  |
|  |  | conversion and |  |  | extended depth-of-field |  |  |
|  |  | R-G conversion |  |  | smear microscopy |  |  |
|  |  | • Data |  |  | images dataset |  |  |
|  |  | annotation |  |  | Augmented dataset: |  |  |
|  |  |  |  |  | 29,310 patches |  |  |
|  | 1D-CNN | • Flat-field | Spatial-spectral | UTI bacteria | 16,642 bacteria | Acc = 99.7% Turra, Arrigoni |
|  |  | correcting | features |  | colonies grown |  | & Signoroni |
|  |  | and smoothing | (intensity images) |  | on the Petri |  | (2017) |
|  |  | • Image |  |  | dishes, from 106 |  |  |
|  |  | denoising |  |  | HSI volumes |  |  |
|  |  | • Threshold-base |  |  |  |  |  |
|  |  | foreground extraction |  |  |  |  |  |
|  |  | and segmentation |  |  |  |  |  |
|  |  | • Cosine distance |  |  |  |  |  |
|  |  | map weighting |  |  |  |  |  |
|  | CNN + SVM X | Texture | Bacteria | 660 microscopic | Acc = 97.24% Zieliński et al. |
|  |  |  | features | colonies | images obtained |  | (2017) |
|  |  |  |  |  | from DIBaS |  |  |
|  |  |  |  |  | dataset |  |  |
|  | CNN-based | • Image | Pixel | M. tuberculosis | 1,800 patches | Se = 97.13% | Panicker et al. |
|  |  | denoising | features | bacteria | extracted from 120 | P = 78.4% | (2018) |
|  |  | • Image |  |  | M. tuberculosis | F = 86.76% |  |
|  |  | binarization |  |  | images with both |  |  |
|  |  | • Morphological |  |  | high-density and |  |  |
|  |  | opening and |  |  | low-density |  |  |
|  |  | closing |  |  | backgrounds |  |  |
|  |  | • Data |  |  |  |  |  |
|  |  | annotation |  |  |  |  |  |

## Table 2 Data distributions of E. coli bacteria for each growth stage in the public dataset. Growth stages of E. coli cells Before data augmentation After data augmentation

| Rod-shaped E. coli cells | 1,079 | 6,474 |
| --- | --- | --- |
| Dividing E. coli cells | 697 | 4,182 |
| Microcolony of E. coli cells | 157 | 942 |
| Total | 1,933 | 11,598 |

## Table 3 Image annotation process configuration. Growth stages of E. coli cells Class Bounding box color

| Rod-shaped E. coli cells | 0 | Green |
| --- | --- | --- |
| Dividing E. coli cells | 1 | Yellow |
| Microcolony of E. coli cells | 2 | Red |

## Table 4 Training and testing datasets before and after data augmentation. Dataset (percentage) Quantity (images) Original After data augmentation

| Training (70%) | 112 | 672 |
| --- | --- | --- |
| Testing (30%) | 48 | 288 |
| Total (100%) | 160 | 960 |

## Table 5 Hyperparameter settings for DL model training in detection and classification of E. coli cells depending on three growth stages (three classes).

| Training hyperparameters | SSD-MobileNetV2 | EfficientDet | YOLOv4 |
| --- | --- | --- | --- |
| Number of class | 3 | 3 | 3 |
| Image size: Height | 320 | 512 | 416 |
| Image size: Width | 320 | 512 | 416 |
| Number of epochs | 200 | 200 | 200 |
| Number of steps | 12,000 | 48,000 | - |
| Number of iterations | - | - | 6,000 |
| Batch size | 16 | 4 | 32 |
| Subdivision | - | - | 16 |
| Filter | - | 64 | 24 |
| Learning rate | 0.08 | 0.08 | 0.001 |

## E. coli bacteria, whereas the proposed SSD-MobileNetV2 and EfficientDet were only able to create the same-coloured bounding boxes, green bounding boxes, for all classifications of the growth stages of the E. coli bacteria. In the YOLOv4 model, the rod-shaped E. coli cell, dividing E. coli cell, and E. coli microcolony were automatically assigned purple, orange and green bounding boxes, respectively. Associating specific colours to each class, each growth stage of E. coli bacteria in this case, provided clear labelling and annotation of the detected E. coli bacteria, helping visually distinguish and differentiate between E. coli bacteria of various growth stages. Therefore, the different coloured bounding boxes created by the YOLOv4 model in the output image for indication of different growth stages of detected E. coli bacteria supported multi-class detection. They allowed enhanced visual interpretation of the detected E. coli bacteria with their growth stages in the output image. Therefore, the user experience was improved as users can quickly identify and focus on specific objects or classes of interest while reviewing or analysing the detection results, resulting in more efficient analysis and decision-making.

| Performance metrics | Proposed object detection model |  |
| --- | --- | --- | --- |
|  | SSD-MobileNetV2 | EfficientDet | YOLOv4 |
| mAP (%) | 96 | 97 | 98 |
| Precision (%) | 71 | 72 | 86 |
| Recall (%) | 78 | 77 | 97 |
| F1-score (%) | 74 | 74 | 91 |
| stages of the |  |  |  |

### Formule


$$Precision = TP TP + FP × 100%(4)$$

### Formule


$$Recall = TP TP + FN × 100%(5)$$

### Formule


$$F 1 -score = 2 • (Precision × Recall) (Precision + Recall) (6)$$
