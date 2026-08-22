# Proximal femur fracture detection on plain radiography via feature pyramid networks.

**Auteurs** : İlkay Yıldız Potter, Diana Yeritsyan, Sarah Mahar, Nadim Kheir, Aidin Vaziri, Melissa Putman, Edward K Rodriguez, Jim Wu, Ara Nazarian, Ashkan Vaziri
**Année** : 2024
**DOI** : 10.1038/s41598-024-63001-2

## Résumé

Hip fractures exceed 250,000 cases annually in the United States, with the worldwide incidence projected to increase by 240-310% by 2050. Hip fractures are predominantly diagnosed by radiologist review of radiographs. In this study, we developed a deep learning model by extending the VarifocalNet Feature Pyramid Network (FPN) for detection and localization of proximal femur fractures from plain radiography with clinically relevant metrics. We used a dataset of 823 hip radiographs of 150 subjects with proximal femur fractures and 362 controls to develop and evaluate the deep learning model. Our model attained 0.94 specificity and 0.95 sensitivity in fracture detection over the diverse imaging dataset. We compared the performance of our model against five benchmark FPN models, demonstrating 6-14% sensitivity and 1-9% accuracy improvement. In addition, we demonstrated that our model outperforms a state-of-the-art transformer model based on DINO network by 17% sensitivity and 5% accuracy,

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Subject level demographics distribution. We also included the scan level age, gender proximal femur fracture presence and imaging device distribution in Supplementary Tables S.1 and S.2.

| Fracture (n |
| --- |

## = 150, ages 26-100) Control (n = 355, ages 18-97)

| Gender, n (%) |  |  |
| --- | --- | --- |
| Female | 87 (58%) | 99 (27%) |
| Male | 35 (23%) | 95 (26%) |
| Unknown | 28 (19%) | 161 (47%) |
| BMI, n (%) |  |  |
| Underweight (< 19) | 11 (7%) | 7 (3%) |
| Healthy weight (19-25) | 31 (21%) | 52 (14%) |
| Overweight (25-30) | 14 (9%) | 32 (10%) |
| Obese (> 30) | 11 (7%) | 27 (8%) |
| Unknown | 83 (56%) | 237 (65%) |
| Race, n (%) |  |  |
| White | 109 (73%) | 152 (42%) |
| Black or African American | 10 (7%) | 19 (6%) |
| Asian | 1 (1%) | 1 (1%) |
| Hispanic | 0 | 6 (2%) |
| Unknown | 30 (19%) | 177 (49%) |

## AUC Specificity Sensitivity Accuracy NPV PPV IOU

| VarifocalNet | Metric CI ( ±) | 0.98 0.03 | 0.94 0.06 | 0.95 0.05 | 0.94 0.06 | 0.94 0.06 | 0.95 0.05 | 0.67 0.09 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Metric | 0.91 | 1.0 | 0.78 | 0.89 | 0.81 | 1.0 | 0.71 |
| DINO | CI ( ±) | 0.07 | 10 -3 | 0.1 | 0.07 | 0.09 | 10 -3 | 0.08 |
|  | p-value 10 -19 10 -21 | 10 -25 | 10 -15 | 10 -24 10 -24 10 -6 |
|  | Metric | 0.95 | 0.97 | 0.89 | 0.93 | 0.89 | 0.97 | 0.67 |
| FasterRCNN | CI ( ±) | 0.05 | 0.04 | 0.07 | 0.06 | 0.07 | 0.04 | 0.09 |
|  | p-value 10 -11 10 -14 | 10 -17 | 0.03 | 10 -12 10 -5 | 0.03 |
|  | Metric | 0.96 | 0.97 | 0.86 | 0.92 | 0.87 | 0.97 | 0.71 |
| CascadeRCNN | CI ( ±) | 0.05 | 0.04 | 0.08 | 0.06 | 0.08 | 0.04 | 0.08 |
|  | p-value 10 -6 | 10 -8 | 10 -22 | 10 -9 | 10 -18 10 -5 | 10 -4 |
|  | Metric | 0.96 | 0.91 | 0.89 | 0.9 | 0.89 | 0.92 | 0.69 |
| RetinaNet | CI ( ±) | 0.05 | 0.07 | 0.07 | 0.07 | 0.07 | 0.06 | 0.09 |
|  | p-value 10 -7 | 10 -9 | 10 -17 | 10 -12 | 10 -14 10 -5 | 10 -3 |
|  | Metric | 0.92 | 0.89 | 0.81 | 0.85 | 0.82 | 0.88 | 0.71 |
| FCOS | CI ( ±) | 0.07 | 0.07 | 0.09 | 0.08 | 0.09 | 0.08 | 0.08 |
|  | p-value 10 -22 10 -13 | 10 -25 | 10 -23 | 10 -23 10 -20 10 -8 |
|  | Metric | 0.96 | 0.97 | 0.84 | 0.9 | 0.85 | 0.97 | 0.67 |
| GCNet | CI ( ±) | 0.05 | 0.04 | 0.08 | 0.07 | 0.08 | 0.04 | 0.09 |
|  | p-value 10 -5 | 10 -8 | 10 -24 | 10 -8 | 10 -22 10 -4 | 0.03 |
|  | Metric | 0.97 | 0.97 | 0.95 | 0.96 | 0.94 | 0.97 | N/A |
| DenseNet | CI ( ±) | 0.03 | 0.03 | 0.05 | 0.04 | 0.06 | 0.03 |  |
|  | p-value 10 -6 | 10 -5 | 0.88 | 10 -4 | 0.43 | 10 -6 |  |
|  | Metric | 0.96 | 0.94 | 0.95 | 0.94 | 0.94 | 0.95 | N/A |
| EfficientNet | CI ( ±) | 0.04 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 |  |
|  | p-value 10 -8 | 0.57 | 0.88 | 0.6 | 0.43 | 0.09 |  |

## AUC Specificity Sensitivity Accuracy NPV PPV

| VarifocalNet | Metric CI ( ±) | 0.82 0.08 | 0.74 0.09 | 0.78 0.08 | 0.76 0.08 | 0.77 0.08 | 0.75 0.08 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Metric | 0.88 | 0.92 | 0.46 | 0.69 | 0.63 | 0.85 |
| DINO | CI ( ±) | 0.07 | 0.05 | 0.1 | 0.09 | 0.09 | 0.07 |
|  | p-value 10 -8 | 10 -18 | 10 -18 | 10 -11 | 10 -16 10 -15 |
|  | Metric | 0.83 | 0.86 | 0.68 | 0.77 | 0.73 | 0.83 |
| FasterRCNN | CI ( ±) | 0.08 | 0.07 | 0.09 | 0.08 | 0.09 | 0.07 |
|  | p-value 0.8 | 10 -16 | 10 -14 | 0.15 | 10 -5 | 10 -12 |
|  | Metric | 0.82 | 0.92 | 0.44 | 0.68 | 0.62 | 0.85 |
| CascadeRCNN | CI( ±) | 0.08 | 0.05 | 0.1 | 0.09 | 0.1 | 0.07 |
|  | p-value 0.4 | 10 -18 | 10 -18 | 10 -13 | 10 -16 10 -15 |
|  | Metric | 0.83 | 0.76 | 0.74 | 0.75 | 0.75 | 0.76 |
| RetinaNet | CI ( ±) | 0.08 | 0.08 | 0.09 | 0.08 | 0.08 | 0.08 |
|  | p-value 0.8 | 0.58 | 10 -5 | 0.28 | 0.02 | 0.36 |
|  | Metric | 0.74 | 0.7 | 0.66 | 0.68 | 0.67 | 0.69 |
| FCOS | CI ( ±) | 0.01 | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 |
|  | p-value 10 -12 10 -7 | 10 -16 | 10 -13 | 10 -13 10 -9 |
|  | Metric | 0.79 | 0.9 | 0.44 | 0.67 | 0.62 | 0.81 |
| GCNet | CI ( ±) | 0.09 | 0.06 | 0.01 | 0.09 | 0.1 | 0.08 |
|  | p-value 10 -4 | 10 -18 | 10 -18 | 10 -14 | 10 -16 10 -9 |
|  | Metric | 0.83 | 0.82 | 0.52 | 0.67 | 0.63 | 0.74 |
| DenseNet | CI ( ±) | 0.08 | 0.08 | 0.1 | 0.09 | 0.09 | 0.09 |
|  | p-value 0.8 | 10 -9 | 10 -18 | 10 -14 | 10 -16 0.2 |
|  | Metric | 0.8 | 0.82 | 0.46 | 0.64 | 0.6 | 0.72 |
| EfficientNet | CI ( ±) | 0.09 | 0.08 | 0.1 | 0.09 | 0.1 | 0.09 |
|  | p-value 10 -3 | 10 -9 | 10 -18 | 10 -17 | 10 -17 10 -4 |

### Formule


$$- 1 |F| i∈F q i q i log p i + 1 -q i log 1 -p i - 1 |F| i∈B 0.75p 2 i log 1 -p i ,(2)$$

### Formule


$$i∈F -1.5 |F| q i GIOU [l i , t i , r i , b i ], l i * , t i * , r i * , b i * -2 |F| q i GIOU l ′ i , t ′ i , r ′ i , b ′ i , l i * , t i * , r i * , b i * ,(3)$$
