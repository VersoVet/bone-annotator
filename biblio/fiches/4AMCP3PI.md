# Automatic Tracking of Hyoid Bone Displacement and Rotation Relative to Cervical Vertebrae in Videofluoroscopic Swallow Studies Using Deep Learning.

**Auteurs** : Li W, Mao S, Mahoney AS, Coyle JL, Sejdić E.
**Année** : 2024
**DOI** : 10.1007/s10278-024-01039-4

## Résumé

The hyoid bone displacement and rotation are critical kinematic events of the swallowing process in the assessment of videofluoroscopic swallow studies (VFSS). However, the quantitative analysis of such events requires frame-by-frame manual annotation, which is labor-intensive and time-consuming. Our work aims to develop a method of automatically tracking hyoid bone displacement and rotation in VFSS. We proposed a full high-resolution network, a deep learning architecture, to detect the anterior and posterior of the hyoid bone to identify its location and rotation. Meanwhile, the anterior-inferior corners of the C2 and C4 vertebrae were detected simultaneously to automatically establish a new coordinate system and eliminate the effect of posture change. The proposed model was developed by 59,468 VFSS frames collected from 1488 swallowing samples, and it achieved an average landmark localization error of 2.38 pixels (around 0.5% of the image with 448 × 448 pixels) and an average angle p

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## The results of paired t-test results for all pairs of errors. The data (p values) were calculated from comparisons of all metrics for all possible model pairs in the two different datasets

|  |  | Patient dataset |  | Healthy participant dataset |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model1 | Model2 | LE | AE | MAE | LE | AE | MAE |
| Full-HRNet | HRNet | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 |
| Full-HRNet | CPN | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.10 |
| Full-HRNet | ResNet | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| HRNet | CPN | 0.00 | 0.00 | 0.12 | 1.00 | 1.00 | 0.91 |
| HRNet | ResNet | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| CPN | ResNet | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

### Formule


$$(1) MSE = 1 D ∑ D i=1 (y � i -y i ) 2$$

### Formule


$$(2) LE = √ (X -X � ) 2 + (Y -Y � ) 2 (3) AE = | | -� | | (4) MAE = ∑ n i=1 �N i -N � i � n$$
