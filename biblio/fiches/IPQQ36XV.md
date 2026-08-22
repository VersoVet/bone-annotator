# Detection of ankle fractures using deep learning algorithms.

**Auteurs** : Soheil Ashkani-Esfahani, Reza Mojahed Yazdi, Rohan Bhimani, Gino M Kerkhoffs, Mario Maas, Christopher W DiGiovanni, Bart Lubberts, Daniel Guss
**Année** : 2022
**DOI** : 10.1016/j.fas.2022.05.005

## Résumé

Early and accurate detection of ankle fractures are crucial for optimizing treatment and thus reducing future complications. Radiographs are the most abundant imaging techniques for assessing fractures. Deep learning (DL) methods, through adequately trained deep convolutional neural networks (DCNNs), have been previously shown to faster and accurately analyze radiographic images without human intervention. Herein, we aimed to assess the performance of two different DCNNs in detecting ankle fractures using radiographs compared to the ground truth.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 500

## Baseline characteristics of the patients with ankle fracture diagnosed on radiograph and the age and sex matched controls with healthy ankles. The radiographs of these groups were used to build a database to develop deep learning algorithms for detection of ankle fractures.

| Group | Patient group | Control group | p-value |
| --- | --- | --- | --- |
| Gender | M 61 % (643/1050) M 56 % (592/1050) 0.1 |
|  | F | 39 % (407/1050) F | 44 % (458/1050) |
| Age | 44 ± 17 | 39 ± 20 | 0.3 |
| (mean ± SD) |  |  |  |
| BMI | 32 ± 10 | 28 ± 11 | 0.4 |
| (mean ± SD) |  |  |  |
| Abbreviations: F, female; M, Male; BMI, body mass index; SD, standard deviation. |

## The proportion of ankle fractures based on Danis-Weber classification in a cohort of 1050 patients.

| Groups | No. of | No. tibial | No. talus body |
| --- | --- | --- | --- |
|  | patients (%) | fractures (%) | fractures (%) |
| Weber A | 279/1050 (27 %) | 10/279 (4 %) | 3/279 (1 %) |
| Weber B | 407/1050 (39 %) | 61/407 (15 %) | 3/407 (1 %) |
| Weber C | 200/1050 (19 %) | 22/200 (11 %) | 0/200 (0 %) |
| Others* | 164/1050 (16 %) | 122/164 (74 %) | 42/164 (26 %) |
| Total | 1050/1050 | 215/1050 (20 %) | 48/1050 (5 %) |
|  | (100 %) |  |  |

## Performance of two deep convolutional neural network (DCNN) models in detection of ankle fractures on radiographs. Single-view (anteroposterior) and three-view radiographs were used to assess the accuracy of each DCNN model.

| S. Ashkani-Esfahani, R. Mojahed Yazdi, R. Bhimani et al. |  |  |  |  | Foot and Ankle Surgery 28 (2022) 1259-1265 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | No. of radiographic views | Sensitivity | Specificity | PPV | NPV | Accuracy | F-Score | AUC |
| Inception V3 | Single view | 91 % | 94 % | 94 % | 91 % | 92 % | 92 % | 95 % |
|  | Three views | 99 % | 99 % | 99 % | 99 % | 99 % | 99 % | 99 % |
| Resnet-50 | Single view | 94 % | 89 % | 90 % | 94 % | 92 % | 92 % | 94 % |
|  | Three views | 98 % | 94 % | 95 % | 97 % | 96 % | 96 % | 98 % |

### Formule


$$= × × + score 2 PPV Sensitivity$$
