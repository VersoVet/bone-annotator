# Critical evaluation of deep neural networks for wrist fracture detection.

**Auteurs** : Abu Mohammed Raisuddin, Elias Vaattovaara, Mika Nevalainen, Marko Nikki, Elina Järvenpää, Kaisa Makkonen, Pekka Pinola, Tuula Palsio, Arttu Niemensivu, Osmo Tervonen, Aleksei Tiulpin
**Année** : 2021
**DOI** : 10.1038/s41598-021-85570-2

## Résumé

Wrist Fracture is the most common type of fracture with a high incidence rate. Conventional radiography (i.e. X-ray imaging) is used for wrist fracture detection routinely, but occasionally fracture delineation poses issues and an additional confirmation by computed tomography (CT) is needed for diagnosis. Recent advances in the field of Deep Learning (DL), a subfield of Artificial Intelligence (AI), have shown that wrist fracture detection can be automated using Convolutional Neural Networks. However, previous studies did not pay close attention to the difficult cases which can only be confirmed via CT imaging. In this study, we have developed and analyzed a state-of-the-art DL-based pipeline for wrist (distal radius) fracture detection-DeepWrist, and evaluated it against one general population test set, and one challenging test set comprising only cases requiring confirmation by CT. Our results reveal that a typical state-of-the-art approach, such as DeepWrist, while having a near-pe

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## . Our study leveraged three datasets, where one was used for training, and the other two for testing. These datasets consisted of referrals, PA and LAT images, and radiology reports. All the data were extracted from the Oulu University Hospital's (OUH) Picture Archiving and Communication System (PACS) and the Radiology Information System. We used pseudonymization to keep patients' identities protected. The project was approved by the Ethics Committee of Northern Ostrobothnia Hospital District (decision number: 126/2014), and the patients' informed consent requirement was waived due to the retrospective nature of this study. All methods of this research were performed in accordance with the Declaration of Helsinki.

| Training dataset. To create the training set, we biased our data selection keeping the ratio of fractures 50% . |
| --- |
| Initially, our training dataset included 1000 cases with distal radius fractures. Subsequently, images, which had |
| artifacts (reasons-non-diagnostic quality or implants) were removed leaving 953 distal radius fracture cases. |
| In total, 1946 wrist studies (3873 PA and LAT images) were used in our training set. All the cases in this train- |

## Datasets used in this study.

|  |  |  |  |  |  | # Fracture | # Normal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dataset | # Cases # Fracture cases # Normal cases View # Radiographs | radiographs | radiographs |
| Training set | 1946 | 953 | 993 | PA LAT | 1962 1911 | 954 946 | 1008 965 |
| Test set #1 | 207 | 129 | 78 | PA LAT | 207 207 | 129 129 | 78 78 |
| Test set #2 | 105 | 20 | 85 | PA LAT | 105 105 | 20 20 | 85 85 |

## Performance of 5 readers and DeepWrist on trivial cases (test set #1). 95% confidence intervals (CI) are shown in parentheses. BA stands for balanced accuracy.

|  | Radiology |  |  | Primary care | Primary care |
| --- | --- | --- | --- | --- | --- | --- |
|  | resident | Radiologist 1 | Radiologist 2 | Physician 1 | Physician 2 | DeepWrist |
| Sensitivity (95% CI) | 0.98 (0.96-1.00) | 1.00 (1.00-1.00) 0.99 (0.97-1.00) 0.99 (0.97-1.00) | 0.92 (0.87-0.96) | 0.97 (0.94-1.00) |
| Specificity (95% CI) | 0.93 (0.87-0.98) | 0.97 (0.93-1.00) 1.00 (1.00-1.00) 0.73 (0.62-0.82) | 0.97 (0.93-1.00) | 0.87 (0.79-0.93) |
| Precision (95% CI) 0.96 (0.92-0.99) | 0.98 (0.96-1.00) 1.00 (1.00-1.00) 0.85 (0.81-0.90) | 0.98 (0.95-1.00) | 0.92 (0.88-0.96) |
| F 1 score (95% CI) 0.97 (0.95-0.99) | 0.99 (0.98-1.00) 0.99 (0.98-1.00) 0.92 (0.89-0.94) | 0.95 (0.92-0.97) | 0.95 (0.92-0.97) |
| BA (95% CI) | 0.96 (0.92-0.98) | 0.98 (0.96-1.00) 0.99 (0.98-1.00) 0.86 (0.81-0.91) | 0.94 (0.91-0.97) | 0.92 (0.88-0.96) |

## Performance of 4 readers and DeepWrist on hard cases (test set #2). 95% confidence intervals (CI) are shown in parentheses. BA stands for balanced accuracy.

| Radiologist |
| --- |

## 1 Radiologist 2 Primary care Physician 1 Primary care Physician 2 DeepWrist

| Sensitivity (95% CI) | 0.40 (0.20-0.60) 0.40 (0.20-0.60) 0.50 (0.30-0.70) | 0.60 (0.40-0.80) | 0.60 (0.40-0.80) |
| --- | --- | --- | --- |
| Specificity (95% CI) | 0.95 (0.90-0.98) 0.96 (0.91-1.00) 0.80 (0.71-0.88) | 0.64 (0.54-0.74) | 0.92 (0.87-0.97) |
| Precision (95% CI) | 0.66 (0.41-0.91) 0.72 (0.50-1.00) 0.37 (0.23-0.52) | 0.28 (0.19-0.38) | 0.66 (0.48-0.87) |
| F 1 score (95% CI) | 0.50 (0.27-0.70) 0.51 (0.28-0.70) 0.42 (0.25-0.58) | 0.38 (0.25-0.50) | 0.63 (0.44-0.80) |
| BA (95% CI) | 0.67 (0.57-0.78) 0.68 (0.57-0.79) 0.65 (0.53-0.76) | 0.62 (0.50-0.73) | 0.76 (0.65-0.87) |

### Formule


$$x mix = x 1 + (1 -)x 2$$

### Formule


$$y mix = y 1 + (1 -)y 2$$
