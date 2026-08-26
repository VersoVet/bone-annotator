# Automatic classification of canine thoracic radiographs using deep learning

**Auteurs** : Tommaso Banzato, Marek Wodziński, Silvia Burti, Valentina Longhin Osti, Valentina Rossoni, Manfredo Atzori, Alessandro Zotti
**Année** : 2021
**DOI** : 10.1038/s41598-021-83515-3

## Résumé

AbstractThe interpretation of thoracic radiographs is a challenging and error-prone task for veterinarians. Despite recent advancements in machine learning and computer vision, the development of computer-aided diagnostic systems for radiographs remains a challenging and unsolved problem, particularly in the context of veterinary medicine. In this study, a novel method, based on multi-label deep convolutional neural network (CNN), for the classification of thoracic radiographs in dogs was developed. All the thoracic radiographs of dogs performed between 2010 and 2020 in the institution were retrospectively collected. Radiographs were taken with two different radiograph acquisition systems and were divided into two data sets accordingly. One data set (Data Set 1) was used for training and testing and another data set (Data Set 2) was used to test the generalization ability of the CNNs. Radiographic findings used as non mutually exclusive labels to train the CNNs were: unremarkable, cardiomegaly, alveolar pattern, bronchial pattern, interstitial pattern, mass, pleural effusion, pneumothorax, and megaesophagus. Two different CNNs, based on ResNet-50 and DenseNet-121 architectures respectively, were developed and tested. The CNN based on ResNet-50 had an Area Under the Receive-Operator Curve (AUC) above 0.8 for all the included radiographic findings except for bronchial and interstitial patterns both on Data Set 1 and Data Set 2. The CNN based on DenseNet-121 had a lower overall performance. Statistically significant differences in the generalization ability between the two CNNs were evident, with the CNN based on ResNet-50 showing better performance for alveolar pattern, interstitial pattern, megaesophagus, and pneumothorax.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Number of LL radiographs showing the following included radiographic findings.

| Radiographic |
| --- |

## finding Data Set 1 Data Set 2

| Unremarkable | 1279 | 365 |
| --- | --- | --- |
| Cardiomegaly | 583 | 138 |
| Bronchial pattern | 123 | 33 |
| Mass | 94 | 32 |
| Pleural effusion | 76 | 16 |
| Alveolar pattern | 59 | 41 |
| Pneumothorax | 33 | 12 |
| Megaoesophagus | 33 | 21 |
| Pneumomediastinum | 5 | 3 |
| Tracheal collapse | 10 | 2 |
| Hernia | 5 | 2 |
| Fracture | 5 | 3 |
| Excluded | 632 | 77 |

## Performances of ResNet-50 in Data Set 1 and Data Set 2. Parentheses show 95% CIs. AUC area under the receiver operator curve, PLR positive likelihood ratio, NLR negative likelihood ratio. Most relevant results have been bolded.

| Test set | Radiographic finding AUC | Sensitivity | Specificity | PLR | NLR |
| --- | --- | --- | --- | --- | --- | --- |
| Data Set 1 | Alveolar pattern | 0.87 (0.78-0.97) | 0.95 (0.64-1) | 0.38 (0.31-0.45) | 1.48 (1.2-1.8) 0.2(0.01-1.4) |
| Data Set 2 | Alveolar pattern | 0.89 (0.86-0.92) | 0.95 (0.9-0.98) | 0.52 (0.38-0.72) | 1.99 (1.8-2.2) 0.095 (0.04-0.2) |
| Data Set 1 | Bronchial pattern | 0.78 (0.66-0.9) | 0.95 (0.66-0.99) 0.092 (0.04-0.68) 1.02 (0.9-1.2) 0.78(0.1-0.54) |
| Data Set 2 | Bronchial pattern | 0.69 (0.61-0.76) | 0.96 (0.86-0.99) 0.20 (0.17-0.24) | 1.2 (1.1-1.3) | 0.2 (0.05-0.8) |
| Data Set 1 | Cardiomegaly | 0.92 (0.88-0.97) | 0.95 (0.86-1) | 0.52 (0.43-0.6) | 1.98 (1.7-2.3) 0.08 (0.02-0.3) |
| Data Set 2 | Cardiomegaly | 0.89 (0.86-0.92) | 0.95 (0.91-0.98) 0.59 (0.54-0.63) | 2.31 (2.1-2.6) 0.076 (0.03-0.2) |
| Data Set 1 | Interstitial pattern | 0.92 (0.9-0.98) | 0.95 (0.52-1) | 0.77 (0.71-0.83) | 3.88 (2.8-5.5) 0.14 (0.02-0.9) |
| Data Set 2 | Interstitial pattern | 0.79 (0.73-0.85) | 0.95 (0.87-1) | 0.44 (0.4-0.48) | 1.72 (1.6-1.9) 0.09 (0.02-0.3) |
| Data Set 1 | Mass | 0.77 (0.68-0.875) 0.95 (0.74-1) | 0.42 (0.35-0.5) | 1.64 (1.4-1.9) 0.12 (0.02-0.8) |
| Data Set 2 | Mass | 0.66 (0.55-0.77) | 0.95 ( 0.85-1) | 0.11 (0.09-0.14) | 1.1 (1-1.2) | 0.26 (0.04-1.8) |
| Data Set 1 | Megaesophagus | 0.78 (0.56-1) | 0.95 (0.42-1) | 0.29 (0.17-0.27) | 1.10 (0.8-1.5) 0.65(0.1-4.1) |
| Data Set 2 | Megaesophagus | 0.80 (0.71-0.90) | 0.95 (0.76-1) | 0.31 (0.27-0.34) | 1.37 (1.2-1.5) 0.16 (0.02-1.1) |
| Data Set 1 | Pleural effusion | 0.96 (0.9-1) | 0.95 (0.64-1) | 0.57 (0.49-0.63) | 2.11 (1.7-2.6) 0.14 (0.02-0.9) |
| Data Set 2 | Pleural effusion | 0.96 (0.93-0.98) | 0.95 (0.73-1) | 0.81 (0.77-0.84) | 4.87(4.0-5.9) | 0.07 (0.01-0.5) |
| Data Set 1 | Pneumothorax | 0.88 (0.72-0.96) | 0.95 (0.75-0.98) 0.40 (0.35-0.34) | 1.56 (1.3-1.6) 0.24 (0.07-1.8) |
| Data Set 2 | Pneumothorax | 0.84 (0.72-0.96) | 0.95 (0.64-0.96) 0.30 (0.27-0.34) | 1.35 (1.2-1.5) 0.18 (0.03-1.2) |
| Data Set 1 | Unremarkable | 0.88 (0.83-0.92) | 0.95 (0.89-0.98) 0.63 (0.54-0.73) | 2.62 (2-4.4) | 0.08 (0.04-0.2) |
| Data Set 2 | Unremarkable | 0.83 (0.80-0.86) | 0.95 (0.92-0.97) 0.44 (0.38-0.5) | 1.69 (1.5-1.9) 0.11(0.07-0.2) |

## Performances of DenseNet-121 in Data Set 1 and Data Set 2. Parentheses show 95% CIs. AUC area under the receiver operator curve, PLR positive likelihood ratio, NLR negative likelihood ratio. Most relevant results have been bolded.

| Test Set | Radiographic finding AUC | Sensitivity | Specificity | PLR | NLR |
| --- | --- | --- | --- | --- | --- | --- |
| Data Set 1 | Alveolar pattern | 0.80 (0.66-0.94) | 0.95 (0.64-1) | 0.33 (0.27-0.40) 1.38 (1.1-1.7) 0.23 (0.04-1.5) |
| Data Set 2 | Alveolar pattern | 0.83 (0.8-0.87) | 0.95 (0.9-0.98) | 0.41 (0.37-0.45) 1.61(1.5-1.7) | 0.12(0.06-0.3) |
| Data Set 1 | Bronchial pattern | 0.69 (0.59-0.8) | 0.95 (0.66-1) | 0.44 (0.37-0.52) 1.67 (1.4-2) | 0.16(0.02-1.1) |
| Data Set 2 | Bronchial pattern | 0.70 (0.63-0.77) | 0.95 (0.83-1) | 0.17 (0.14-0.20) 1.13 (1-1.2) | 0.37 (0.1-1.1) |
| Data Set 1 | Cardiomegaly | 0.87 (0.80-0.93) 0.98 (0.89-1) | 0.24 (0.17-0.31) 1.28 (1.2-1.4) 0.09 (0.01-0.6) |
| Data Set 2 | Cardiomegaly | 0.98 (0.85-0.91) 0.95 (0.87-0.96) 0.65 (0.61-0.99) 2.67 (2.4-3) | 0.11(0.06-0.2) |
| Data Set 1 | Interstitial pattern | 0.78 (0.65-0.91) | 0.95 (0.52-1) | 0.55 (0.44-0.58) 1.82 (1.4-2.4) 0.22(0.03-1.4) |
| Data Set 2 | Interstitial pattern | 0.70 (0.64-0.77) | 0.95 (0.84-1) | 0.25 (0.22-0.23) 1.26(1.2-1.4) | 0.23(0.08-0.7) |
| Data Set 1 | Mass | 0.64 (0.5-0.78) | 0.95 (0.74-1) | 0.04 (0.02-0.07) 0.98 (0.9-1.1) 1.44 (0.2-11.1) |
| Data Set 2 | Mass | 0.59 (0.49-0.7) | 0.95 (0.80-1) | 0.05 (0.03-0.07) 0.99(0.9-1.1) | 1.27 (0.3-5.1) |
| Data Set 1 | Megaesophagus | 0.66 (0.42-0.9) | 0.95 (0.36-1) | 0.17 (0.1-0.22) | 1 (0.7-1.4) | 1 (0.2-6.1) |
| Data Set 2 | Megaesophagus | 0.69 (0.58-0.79) | 0.95 (0.76-1) | 0.28 (0.26-0.32) 1.32(1.2-1.5) | 0.17 (0.03-1.2) |
| Data Set 1 | Pleural effusion | 0.97 (0.93-1) | 0.95 (0.64-1) | 0.83 (0.77-0.88) 5.51(3.9-7.8) | 0.09 (0.01-0.6) |
| Data Set 2 | Pleural effusion | 0.95 (0.93-0.98) | 0.95 (0.73-1) | 0.89 (0.82-0.88) 6.27 (5.1-7.8) 0.06 (0.01-0.4) |
| Data Set 1 | Pneumothorax | 0.56 (0.15-0.96) | 0.95 (0.73-1) | 0.17 (0.07-0.63) 0.8 (0.4-1.8) | 1.97 (0.4-10) |
| Data Set 2 | Pneumothorax | 0.71 (0.6-0.82) | 0.95 (0.74-1) | 0.22 (0.19-0.26) 1.22(1.1-1.4) | 0.24 (0.04-1.6) |
| Data Set 1 | Unremarkable | 0.84 (0.79-0.9) | 0.95 (0.90-0.99) 0.56 (0.46-0.66) 2.16(1.7-2.7) | 0.079 (0.03-0.2) |
| Data Set 2 | Unremarkable | 0.84 (0.81-0.87) | 0.95 (0.92-0.97) 0.42 (0.36-0.48) 1.63(1.5-1.8) | 0.12 (0.08-0.2) |
