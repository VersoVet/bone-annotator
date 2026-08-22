# Rib fracture detection system based on deep learning.

**Auteurs** : Liding Yao, Xiaojun Guan, Xiaowei Song, Yanbin Tan, Chun Wang, Chaohui Jin, Ming Chen, Huogen Wang, Minming Zhang
**Année** : 2021
**DOI** : 10.1038/s41598-021-03002-7

## Résumé

Rib fracture detection is time-consuming and demanding work for radiologists. This study aimed to introduce a novel rib fracture detection system based on deep learning which can help radiologists to diagnose rib fractures in chest computer tomography (CT) images conveniently and accurately. A total of 1707 patients were included in this study from a single center. We developed a novel rib fracture detection system on chest CT using a three-step algorithm. According to the examination time, 1507, 100 and 100 patients were allocated to the training set, the validation set and the testing set, respectively. Free Response ROC analysis was performed to evaluate the sensitivity and false positivity of the deep learning algorithm. Precision, recall, F1-score, negative predictive value (NPV) and detection and diagnosis were selected as evaluation metrics to compare the diagnostic efficiency of this system with radiologists. The radiologist-only study was used as a benchmark and the radiologis

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## The overview of dataset.

| Cohorts |
| --- |

## No. Patients No. CT slices No. Fractures

| Training | 1507 | 581,701 | 7362 |
| --- | --- | --- | --- |
| Validation | 100 | 36,697 | 473 |
| Testing | 100 | 37,183 | 436 |

## The overview of dataset for the training of U-Net and 3D DenseNet.

|  | U-Net | 3D DenseNet |  |
| --- | --- | --- | --- |
| Cohorts | No. CT images No. Fracture blocks No. Normal blocks |
| Training | 4496 | 91,574 | 50,078,825 |
| Validation | 3145 | 5981 | 3,323,151 |
| Testing | 3568 | 5992 | 3,452,162 |

## The comparison of the performance between our Rib Fracture Detection System with Fast RCNN, Faster RCNN, YOLOv3.

| Group | Model Fast RCNN Faster RCNN YOLOv3 |
| --- | --- | --- | --- | --- |
| F1-score | 0.890 | 0.863 | 0.870 | 0.877 |
| Recall | 0.913 | 0.874 | 0.889 | 0.894 |
| Precision | 0.869 | 0.853 | 0.852 | 0.861 |
| NPV | 0.969 | 0.925 | 0.932 | 0.942 |

### Formule


$$L dice = 1 - 2 N i=1 p i * g i + ǫ N i=1 p i + N i=1 g i + ǫ$$

### Formule


$$IOU = |A ∩ B| |A ∪ B| DSC = 2|A ∩ B| |A| + |B|$$
