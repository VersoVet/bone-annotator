# Foundational Segmentation Models and Clinical Data Mining Enable Accurate Computer Vision for Lung Cancer.

**Auteurs** : Nathaniel C Swinburne, Christopher B Jackson, Andrew M Pagano, Joseph N Stember, Javin Schefflein, Brett Marinelli, Prashanth Kumar Panyam, Arthur Autz, Mohapar S Chopra, Andrei I Holodny, Michelle S Ginsberg
**Année** : 2025
**DOI** : 10.1007/s10278-024-01304-6

## Résumé

This study aims to assess the effectiveness of integrating Segment Anything Model (SAM) and its variant MedSAM into the automated mining, object detection, and segmentation (MODS) methodology for developing robust lung cancer detection and segmentation models without post hoc labeling of training images. In a retrospective analysis, 10,000 chest computed tomography scans from patients with lung cancer were mined. Line measurement annotations were converted to bounding boxes, excluding boxes < 1 cm or > 7 cm. The You Only Look Once object detection architecture was used for teacher-student learning to label unannotated lesions on the training images. Subsequently, a final tumor detection model was trained and employed with SAM and MedSAM for tumor segmentation. Model performance was assessed on a manually annotated test dataset, with additional evaluations conducted on an external lung cancer dataset before and after detection model fine-tuning. Bootstrap resampling was used to calculat

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Patient characteristicsUnless otherwise indicated, data are numbers of patients.

|  | Training group | Testing group | Total |
| --- | --- | --- | --- |
| Patient demographics |  |  |  |
| • No. of patients | 4052 | 125 | 4177 |
| • Mean age (y) | 68.6 ± 12.7 | 68.6 ± 13.8 | 68.6 ± 12.8 |
| • Sex | 2233 women, 1819 men | 68 women, 57 men | 2301 |
|  |  |  | women, |
|  |  |  | 1876 men |
| Lung cancer subtype |  |  |  |
| • Adenocarcinoma | 2506 | 70 | 2576 |
| • Squamous cell carcinoma | 454 | 15 | 469 |
| • Neuroendocrine | 148 | 6 | 154 |
| • Small cell carcinoma | 126 | 3 | 129 |
| • Other, multiple, or unavailable | 818 | 31 | 849 |
| No. of unique scans | 4400 | 136 | 4536 |
| Image slice thickness (mm) |  |  |  |
| • 5.0 | 13,378 | 381 | 13,759 |
| • 1.25 | 3640 | 168 | 3808 |
| • Other | 24 | 0 | 24 |
| Mean box length (cm) | 2.08 ± 1.09 | 2.15 ± 1.07 | 2.08 ± 1.09 |

## Results of manual inspection of mined and selflabeled image annotationsResults of manual inspection conducted on randomly selected subsets of both mined and self-labeled image annotations. In the mined image subset, other abnormalities consisted of bullae, esophageal masses, and the tracheal lumen diameter. In the self-labeled subset, other abnormalities consisted of bullae, loculated pleural fluid, apical pleural scarring, and regions of fibrosis. False positives observed in this subset were predominantly vessels imaged in cross-section and respiratory motion artifacts.

| Total boxes | Pulmonary nod- | Pleural masses | Lymph nodes | Other | False posi- |
| --- | --- | --- | --- | --- | --- |
|  | ules/masses |  |  |  | tives/spuri- |
|  |  |  |  |  | ous |
| Mined image subset (500 images) |  |  |  |  |
| 505 | Solid: 283 | 40 | 46 | 6 | 0 |
|  | Sub-solid: 130 |  |  |  |  |
| Self-labeled image subset (500 images) |  |  |  |  |
| 500 | Solid: 253 | 42 | 32 | 14 | 48 |
|  | Sub-solid: 111 |  |  |  |  |

## Tumor detection model performance Detection F1 scores obtained from the teacher and student tumor detection models using both the internal and external test sets. For assessment on the external dataset, the detection models were scored before and after fine-tuning. Values in bold represent the highest performance achieved for each test set.

| Model Internal test set | External LIDC-IDRI test set |
| --- | --- | --- |
| F1 score (95% CI) F1 score before | F1 score after fine- |
|  | fine-tuning (95% | tuning (95% CI) |
|  | CI) |  |
| Teacher 0.847 (0.812- | 0.723 (0.649- | 0.790 (0.723- |
| 0.880) | 0.800) | 0.852) |
| Student 0.860 (0.825-0.893) | 0.765 (0.679-0.841) | 0.832 (0.764-0.895) |
| CI, confidence interval; LIDC-IDRI, Lung Image Database Consor- |
| tium image collection |  |  |

## Integrated tumor detection and segmentation model performance

|  | Internal test set | External LIDC-IDRI test set |
| --- | --- | --- |
|  | DSC (95% CI) | DSC (95% CI) |
| Student detection | 0.842 (0.805-0.873) 0.802 (0.714-0.870) |
| model + SAM |  |
| Student detection | 0.822 (0.785-0.851) 0.804 (0.730-0.858) |
| model + Med- |  |
| SAM |  |
| Segmentation Dice similarity coefficients (DSCs) obtained from the |
| integrated tumor detection and segmentation models using both the |
| internal and external test sets. The top-performing detection mod- |
| els-student model for the internal test set and fine-tuned student |
| model for the external test set-were paired with SAM and Med- |
| SAM for segmentation. Bold values indicate the highest performance |
| for each test set. |  |
| CI, confidence interval; MedSAM, Segment Anything Model for |
| Medical Imaging; SAM, Segment Anything Model; LIDC-IDRI, Lung |
| Image Database Consortium image collection |
