# Detection and Localization of Spine Disorders from Plain Radiography.

**Auteurs** : İlkay Yıldız Potter, Diana Yeritsyan, Edward K Rodriguez, Jim S Wu, Ara Nazarian, Ashkan Vaziri
**Année** : 2024
**DOI** : 10.1007/s10278-024-01175-x

## Résumé

Spine disorders can cause severe functional limitations, including back pain, decreased pulmonary function, and increased mortality risk. Plain radiography is the first-line imaging modality to diagnose suspected spine disorders. Nevertheless, radiographical appearance is not always sufficient due to highly variable patient and imaging parameters, which can lead to misdiagnosis or delayed diagnosis. Employing an accurate automated detection model can alleviate the workload of clinical experts, thereby reducing human errors, facilitating earlier detection, and improving diagnostic accuracy. To this end, deep learning-based computer-aided diagnosis (CAD) tools have significantly outperformed the accuracy of traditional CAD software. Motivated by these observations, we proposed a deep learning-based approach for end-to-end detection and localization of spine disorders from plain radiographs. In doing so, we took the first steps in employing state-of-the-art transformer networks to differe

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Table 1

| Distribution of images with respect to age, sex, and |  | Female |  | Male |  | Unknown | Sum |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VCF presence for the VCF dataset. The numbers of the subjects (n) in each group is | Age | VCF (n = 104) | Normal (n = 286) | VCF (n = 33) | Normal (n = 50) | VCF (n = 1) | Normal (n = 1) |  |
| presented below each subgroup | < 18 | 4 | 39 | 1 | 5 | 2 | 0 | 51 |
|  | 18-30 | 0 | 31 | 0 | 4 | 0 | 0 | 35 |
|  | 31-40 | 0 | 63 | 1 | 3 | 0 | 0 | 67 |
|  | 41-50 | 3 | 57 | 2 | 8 | 0 | 0 | 70 |
|  | 51-60 | 15 | 18 | 8 | 3 | 0 | 0 | 44 |
|  | 61-70 | 13 | 5 | 3 | 2 | 0 | 0 | 23 |
|  | 71-80 | 11 | 2 | 2 | 0 | 0 | 0 | 15 |
|  | 81-90 | 31 | 0 | 4 | 0 | 0 | 0 | 35 |
|  | Unknown | 177 | 314 | 60 | 68 | 0 | 2 | 621 |
|  | Sum | 254 | 529 | 81 | 93 | 2 | 2 | 961 |

## Distribution of images with respect to age, sex, and spondylolisthesis presence for the spondylolisthesis dataset. The numbers of the subjects (n) in each group is presented below each subgroup

|  | Female |  | Male |  | Unknown | Sum |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Age | Spondylolisthesis | Normal | Spondylolisthesis | Normal | Spondylolisthesis | Normal |  |
|  | (n = 246) | (n = 324) | (n = 87) | (n = 87) | (n = 3) | (n = 2) |  |
| < 18 | 8 | 49 | 3 | 6 | 1 | 0 | 67 |
| 18-30 | 0 | 58 | 0 | 11 | 0 | 0 | 69 |
| 31-40 | 6 | 74 | 1 | 9 | 0 | 0 | 90 |
| 41-50 | 19 | 61 | 5 | 12 | 0 | 0 | 97 |
| 51-60 | 20 | 34 | 8 | 13 | 0 | 0 | 75 |
| 61-70 | 38 | 16 | 16 | 8 | 0 | 0 | 78 |
| 71-80 | 27 | 11 | 13 | 4 | 0 | 0 | 55 |
| 81-90 | 10 | 1 | 7 | 2 | 0 | 0 | 20 |
| Unknown | 172 | 343 | 57 | 68 | 2 | 2 | 644 |
| Sum | 300 | 647 | 110 | 133 | 3 | 2 | 1195 |

## Comparison of DINO with the highest VCF detection performance to other models on the VCF dataset.

|  | Model |  | AUC NPV Specificity PPV Sensitivity Accuracy IOU |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | DINO | Metric | 0.97 | 0.98 | 0.97 | 0.94 | 0.96 | 0.96 | 0.49 |
| Detection metrics include Area Under the Receiver Operating | Faster R-CNN | CI (+ / -) 0.02 Metric 0.93 | 0.01 0.94 | 0.01 0.95 | 0.02 0.91 | 0.01 0.88 | 0.01 0.93 | 0.08 0.53 |
| Characteristic Curve (AUC), |  | CI (+ / -) 0.03 | 0.02 | 0.02 | 0.02 | 0.03 | 0.02 | 0.08 |
| sensitivity, specificity, accuracy, positive predictive value (PPV), and negative predictive value (NPV). Localization is assessed by Intersection over Union | RetinaNet | p-value Metric CI (+ / -) 0.03 10 -21 10 -29 10 -13 0.9 0.94 0.89 0.02 0.03 p-value 10 -28 10 -27 10 -35 | 10 -15 10 -31 0.82 0.9 0.03 0.02 10 -36 10 -27 | 10 -19 0.89 0.03 10 -32 | 10 -4 0.51 0.08 10 -2 |
| (IOU). The row with the highest value for each metric is written in bold. Below each metric, the 95% confidence interval | Cascade R-CNN | Metric CI (+ / -) 0.03 0.9 p-value 10 -31 10 -33 10 -21 0.92 0.94 0.02 0.02 | 0.89 0.03 10 -23 10 -34 0.86 0.03 | 0.91 0.02 10 -22 | 0.5 0.08 0.2 |
| (CI) is written. For each model except DINO, p-values (for the two-sided Mann-Whitney nonparametric test) comparing the metrics to those of DINO | FCOS RepPoints | Metric CI (+ / -) 0.04 0.83 p-value 10 -36 10 -36 10 -34 0.81 0.88 0.03 0.03 Metric 0.89 0.86 0.93 | 0.74 0.04 10 -36 10 -36 0.62 0.04 0.85 0.72 | 0.79 0.03 10 -36 0.86 | 0.65 0.07 10 -26 0.6 |
| are also written |  | CI (+ / -) 0.03 | 0.03 | 0.02 | 0.03 | 0.04 | 0.03 | 0.08 |
|  |  | p-value | 10 -29 10 -36 10 -23 | 10 -34 10 -36 | 10 -35 | 10 -16 |
|  | AC-Faster R-CNN Metric | 0.91 | 0.92 | 0.9 | 0.83 | 0.86 | 0.89 | 0.48 |
|  |  | CI (+ / -) 0.03 | 0.02 | 0.02 | 0.03 | 0.03 | 0.03 | 0.08 |
|  |  | p-value | 10 -28 10 -34 10 -32 | 10 -35 10 -34 | 10 -33 | 0.09 |
|  | Deformable DETR Metric | 0.96 | 0.98 | 0.94 | 0.9 | 0.96 | 0.95 | 0.41 |
|  |  | CI (+ / -) 0.02 | 0.01 | 0.02 | 0.02 | 0.01 | 0.02 | 0.08 |
|  |  | p-value | 0.06 | 0.70 | 10 -16 | 10 -19 0.3 | 10 -4 | 10 -4 |
|  | Conditional DETR Metric | 0.88 | 0.95 | 0.73 | 0.65 | 0.93 | 0.8 | 0.49 |
|  |  | CI (+ / -) 0.03 | 0.02 | 0.04 | 0.04 | 0.02 | 0.03 | 0.08 |
|  |  | p-value | 10 -33 10 -24 10 -36 | 10 -36 10 -17 | 10 -36 | 0.9 |
|  | DAB DETR | Metric | 0.78 | 0.84 | 0.73 | 0.6 | 0.75 | 0.74 | 0.44 |
|  |  | CI (+ / -) 0.05 | 0.03 | 0.04 | 0.04 | 0.04 | 0.04 | 0.08 |
|  |  | p-value | 10 -36 10 -36 10 -36 | 10 -36 10 -36 | 10 -36 | 0.02 |

## Table 4

| Comparison of Deformable DETR with the highest spondylolisthesis | Model Deformable DETR Metric | AUC NPV Specificity PPV Sensitivity Accuracy IOU 0.95 0.96 0.87 0.81 0.94 0.89 0.44 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| detection performance to other models on the Spondylolisthesis dataset. | Faster R-CNN | CI (+ / -) 0.02 Metric 0.81 | 0.01 0.86 | 0.01 0.79 | 0.02 0.7 | 0.01 0.78 | 0.01 0.79 | 0.08 0.48 |
| Detection metrics include Area |  | CI (+ / -) 0.03 | 0.02 | 0.02 | 0.02 | 0.03 | 0.02 | 0.08 |
| Under the Receiver Operating Characteristic Curve (AUC), sensitivity, specificity, accuracy, positive predictive value (PPV), and negative predictive value | RetinaNet | p-value Metric CI (+ / -) 0.03 10 -20 10 -28 10 -9 0.78 0.83 0.77 0.02 0.03 p-value 10 -29 10 -26 10 -35 | 10 -13 10 -34 0.66 0.74 0.03 0.02 10 -36 10 -29 | 10 -20 0.76 0.03 10 -31 | 10 -3 0.5 0.08 0.5 |
| (NPV). Localization is assessed by Intersection over Union (IOU). The row with the highest value for each metric is written | Cascade R-CNN | Metric CI(+ / -) 0.03 0.75 p-value 10 -31 10 -32 10 -16 0.84 0.68 0.02 0.02 | 0.59 0.03 10 -25 10 -35 0.78 0.03 | 0.72 0.02 10 -27 | 0.49 0.08 0.5 |
| in bold. Below each metric, | FCOS | Metric | 0.78 | 0.84 | 0.69 | 0.6 | 0.78 | 0.72 | 0.47 |
| the 95% confidence interval (CI) is written. For each model except Deformable DETR, p-values (for the two-sided | RepPoints | CI (+ / -) 0.04 p-value 10 -36 10 -36 10 -35 0.03 0.03 Metric 0.79 0.85 0.67 | 0.04 10 -36 10 -36 0.04 0.6 0.81 | 0.03 10 -36 0.72 | 0.07 10 -24 0.47 |
| Mann-Whitney nonparametric |  | CI (+ / -) 0.03 | 0.03 | 0.02 | 0.03 | 0.04 | 0.03 | 0.08 |
| test) comparing the metrics to those of Deformable DETR are also written | AC-Faster R-CNN | p-value Metric CI (+ / -) 0.03 10 -31 10 -36 10 -28 0.81 0.84 0.76 0.02 0.02 | 10 -34 10 -36 0.66 0.76 0.03 0.03 | 10 -35 0.76 0.03 | 10 -12 0.5 0.08 |
|  |  | p-value | 10 -26 10 -32 10 -35 | 10 -35 10 -35 | 10 -33 | 0.02 |
|  | Conditional DETR | Metric | 0.8 | 0.92 | 0.63 | 0.6 | 0.91 | 0.74 | 0.46 |
|  |  | CI (+ / -) 0.02 | 0.01 | 0.02 | 0.02 | 0.01 | 0.02 | 0.08 |
|  |  | p-value | 10 -4 | 0.9 | 10 -19 | 10 -18 0.6 | 10 -6 | 10 -11 |
|  | DAB DETR | Metric | 0.78 | 0.82 | 0.68 | 0.58 | 0.75 | 0.7 | 0.41 |
|  |  | CI (+ / -) 0.03 | 0.02 | 0.04 | 0.04 | 0.02 | 0.03 | 0.08 |
|  |  | p-value | 10 -33 10 -22 10 -36 | 10 -36 10 -15 | 10 -36 | 0.5 |
|  | DINO | Metric | 0.94 | 0.94 | 0.86 | 0.8 | 0.9 | 0.88 | 0.46 |
|  |  | CI (+ / -) 0.05 | 0.03 | 0.04 | 0.04 | 0.04 | 0.04 | 0.08 |
|  |  | p-value | 10 -36 10 -36 10 -36 | 10 -36 10 -36 | 10 -36 | 10 -5 |
