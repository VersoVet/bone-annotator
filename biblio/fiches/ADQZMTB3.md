# Large-scale annotation dataset for fetal head biometry in ultrasound images.

**Auteurs** : Mahmood Alzubaidi, Marco Agus, Michel Makhlouf, Fatima Anver, Khalid Alyafei
**Année** : 2023
**DOI** : 10.1016/j.dib.2023.109708

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## 2023  The Author(s). Published by Elsevier Inc.

|  | This is an open access article under the CC BY license |
| --- | --- |
|  | ( http://creativecommons.org/licenses/by/4.0/ ) |
| Specifications Table |  |
| Subject | Computer Vision and Pattern Recognition. |
| Specific subject area | Ultrasound Fetal head dataset for computer vision tasks in prenatal diagnostics. |
| Data format | Raw, Analyzed |
| Type of data | Table, Image |
| Data collection |  |

## An overview of existing Fetal head ultrasound image datasets including computer vision task, and number of class.

| Dataset ID | Dataset | Computer vision task | Number | Format | Size |
| --- | --- | --- | --- | --- | --- |
|  |  |  | of classes |  |  |
| A | Fetal_Plane_DB | Image Classification | 9 | PNG images with classes | 12400 |
| B | Fetal_head_HC | Image segmentation | 1 | PNG images with | 999 |
|  | 18_Grand |  |  | corresponding masks |  |
| C | Our dataset | Classification, Segmentation, | 3 | PNG images with the | 3832 |
|  |  | and object detection |  | following format: CityScapes, |  |
|  |  |  |  | Datumaro, COCO, CVAT, |  |
|  |  |  |  | ImageNet, LabelMe, |  |
|  |  |  |  | OpenImage, PASCAL, |  |
|  |  |  |  | Segmentation masks, |  |
|  |  |  |  | TFRecord, YOLO |  |

## Intraclass Correlation Coefficient (ICC) and Jaccard similarity (JS) values for inter-rater reliability by fetal plane.

| 1st iteration: Rater Reliability between Student and Physician |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fetal Plane Group | Number of images | Brain ICC | CSP ICC | LV ICC | Brain JS | CSP JS | LV JS |
| Trans-Thalamic | 1565 | 0.940 | 0.939 | 0.662 | 0.999 | 0.929 | 0.603 |
| Trans-Ventricular | 584 | 1.00 | 0.985 | 0.974 | 1.00 | 0.989 | 0.989 |
| Trans-Cerebellum | 684 | 1.00 | 0.792 | 0.218 | 1.00 | 0.818 | 0.125 |
| Diverse head images | 999 | 1.00 | 0.871 | 0.926 | 1.00 | 0.875 | 0.930 |
| 2nd iteration: Rater Reliability between Student and Radiologic Technologist |  |  |  |
| Trans-Thalamic | 301 | 1.00 | 0.853 | 0.80 | 1.00 | 0.760 | 0.67 |
| Trans-Ventricular | 110 | 1.00 | 0.854 | 0.855 | 1.00 | 0.878 | 0.958 |
| Trans-Cerebellum | 150 | 1.00 | 0.865 | 0.662 | 1.00 | 0.833 | 0.50 |
| Diverse head images | 200 | 1.00 | 0.887 | 0.892 | 1.00 | 0.840 | 0.849 |

### Formule


$$IC C ( 2 , 1 ) = M S between -M S within M S between + ( k -1 ) M S within$$

### Formule


$$JS ( A, B ) = | A ∩ B | | AB |(2)$$
