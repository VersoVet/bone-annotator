# Modeling annotator preference and stochastic annotation error for medical image segmentation

**Auteurs** : Zehui Liao, Shishuai Hu, Yutong Xie, Yong Xia
**Année** : 2024
**DOI** : 10.1016/j.media.2023.103028

## Résumé

Manual annotation of medical images is highly subjective, leading to inevitable and huge annotation biases. Deep learning models may surpass human performance on a variety of tasks, but they may also mimic or amplify these biases. Although we can have multiple annotators and fuse their annotations to reduce stochastic errors, we cannot use this strategy to handle the bias caused by annotators' preferences. In this paper, we highlight the issue of annotator-related biases on medical image segmentation tasks, and propose a Preference-involved Annotation Distribution Learning (PADL) framework to address it from the perspective of disentangling an annotator's preference from stochastic errors using distribution learning so as to produce not only a meta segmentation but also the segmentation possibly made by each annotator. Under this framework, a stochastic error modeling (SEM) module estimates the meta segmentation map and average stochastic error map, and a series of human preference modeling (HPM) modules estimate each annotator's segmentation and the corresponding stochastic error. We evaluated our PADL framework on two medical image benchmarks with different imaging modalities, which have been annotated by multiple medical professionals, and achieved promising performance on all five medical image segmentation tasks.

## Méthodologie

{'study_design': None, 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'Soft Dice of optic disc and optic cup (RIGA dataset) for all compared methods', 'value': 'listed in Table I (not enumerated in text)', 'unit': 'soft Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'The soft Dice of optic disc D s disc and optic cup D s cup obtained by our model and completing methods were listed in Table I.'}, {'outcome': "PADL average D s disc rank among 12 competing methods evaluated against each annotator's delineations", 'value': 'second highest', 'unit': 'rank', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': "the proposed PADL achieves the second highest average D s disc and highest average D s cup when evaluated against each annotator's delineations"}, {'outcome': "PADL average D s cup rank among 12 competing methods evaluated against each annotator's delineations", 'value': 'highest', 'unit': 'rank', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': "the proposed PADL achieves the second highest average D s disc and highest average D s cup when evaluated against each annotator's delineations"}, {'outcome': 'PADL soft Dice on optic disc and optic cup segmentation evaluated against mean voting', 'value': 'highest', 'unit': 'soft Dice rank', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': 'achieves the highest soft Dice on both segmentation tasks when evaluated against the mean voting'}, {'outcome': 'QUBIQ dataset: soft Dice of PADL vs five competing methods evaluated against majority voting, across five CT/MRI segmentation tasks', 'value': 'highest soft Dice on all tasks (values listed in Table II, not enumerated in text)', 'unit': 'soft Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'our PADL achieves the highest soft Dice on all tasks, beating the proxy ground truth strategy, multi-head strategy, and two recent methods'}, {'outcome': "QUBIQ dataset: 'Average' scores comparing CM-Net and PADL for annotator delineation reconstruction across five tasks", 'value': 'PADL performed better than CM-Net on all five tasks (values listed in Table III, not enumerated in text)', 'unit': 'score', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'It can be seen that the PADL model performed better than CM-Net on all five tasks of the QUBIQ dataset'}], 'qualitative_findings': ["The U-Net trained using the annotations from annotator A r always achieves higher performance when evaluated against A r's delineations, except that M1 slightly underperforms M2 in D s cup and M5 slightly underperforms M4 in D s disc.", "The mean voting-based proxy ground truth method MV-UNet outperforms the multi-network (M1∼M6) and multi-head (MH-UNet) methods when evaluated against the mean voting of annotations, but underperforms both when evaluated against each annotator's delineations.", 'A similar conclusion can be drawn for the random annotation-based proxy ground truth method LS-UNet, except for its surprisingly low performance in optic cup segmentation.', 'Both MR-Net and CM-Net perform well no matter being evaluated against the mean voting or each individual annotation, since annotator-related bias is considered.', "MR-Net outperforms CM-Net when evaluated against the mean voting, but is inferior to CM-Net in reconstructing each annotator's delineations, possibly because the annotator decision fusion strategy can hardly preserve each annotator's preference.", "Comparing to CM-Net, PADL reconstructs each annotator's delineations slightly better and performs substantially more accurate meta segmentation approximating the mean voting of annotations.", 'Visualized probabilistic segmentation maps (Figure 4) show PADL produces more accurate probability maps compared to MR-Net, CM-Net, MV-UNet, and MH-UNet, confirming PADL can model consensus among annotators via disentangling stochastic errors from meta segmentation.', 'On QUBIQ, the soft Dice values of three commonly used strategies (MV-UNet, LS-UNet, MH-UNet) are relatively lower than those of others, suggesting both the proxy ground truth strategy and multi-head strategy suffer from limited performance.', "QUBIQ results are consistent with those obtained on RIGA, confirming PADL's superior ability to address stochastic annotation errors and generate meta segmentation.", "CM-Net's backbone was replaced with the one used by other methods for fair comparison, and hyper-parameters were optimized under the same experimental settings."], 'main_findings': ['PADL achieves the highest soft Dice against mean/majority voting on both RIGA (optic disc and cup) and all five QUBIQ tasks, outperforming baseline, multi-head, proxy ground truth, and recent annotator-bias-modeling methods.', "PADL achieves the best or near-best performance in reconstructing individual annotators' delineations on RIGA (second highest D s disc, highest D s cup) and outperforms the strongest competitor CM-Net on all five QUBIQ tasks.", 'Unlike competing methods that trade off between meta segmentation accuracy and annotator-specific delineation reconstruction, PADL improves both simultaneously by disentangling stochastic annotation errors from the meta segmentation.']}

## Conclusions

PADL framework treats annotation bias as a combination of annotator's preference and stochastic errors The SEM module and annotator-specific HPM modules are designed to characterize each annotator's preference while diminishing the impact of stochastic errors This is the first work that simultaneously explicitly models the annotator preference and disentangles the stochastic annotation error by learning the annotation distribution Experimental results on two medical image segmentation benchmarks show that PADL performs well on modeling human preference and disentangling stochastic errors, achieving better performance against other methods for medical image segmentation with biased annotations

## OF OUR PADL FRAMEWORK, 11 COMPETING METHODS, AND TWO VARIANTS OF PADL IN OPTIC DISC AND OPTIC CUP SEGMENTATION ON RIGA. THE SOFT DICE (D s disc (%), D s cup (%)) ARE USED AS THE PERFORMANCE METRIC. THE PREDICTIONS OF EACH MODEL ARE EVALUATED AGAINST EACH ANNOTATOR'S DELINEATIONS AND THE MEAN VOTING ANNOTATION, AND THE AVERAGE PERFORMANCE OVER SIX ANNOTATIONS IS ALSO GIVEN. EXCEPT FOR THE RESULTS OF MULTI-NET (M 1 ∼ M 6 ) AND TWO PADL VARIANTS, TOP THREE RESULTS IN EACH COLUMN ARE HIGHLIGHTED IN RED, BLUE AND GREEN, RESPECTIVELY. IN EACH COLUMN, THE BEST RESULT AMONG M 1 ∼ M 6 IS HIGHLIGHTED WITH UNDERLINE. THE CELLS IN GRAY REPRESENT THE U-NETS TRAINED AND TESTED USING THE ANNOTATIONS FROM THE SAME ANNOTATOR. (96.16, 84.29) (95.08, 80.79) (95.57, 79.82) (96.29, 78.91) (95.91, 80.49) (96.47, 76.57) (95.91, 80.15) (96.27, 80.56) M 2 (95.72, 84.71) (95.50, 84.20) (95.52, 79.87) (96.13, 81.16) (96.13, 80.91) (96.27, 77.93) (95.88, 81.46) (96.30, 82.03) M 3 (95.10, 82.76) (94.50, 79.69) (96.53, 83.10) (96.20, 78.39) (96.28, 81.47) (95.92, 76.73) (95.76, 80.36) (95.89, 80.90) M 4 (95.92, 81.46) (95.30, 82.16) (96.18, 78.53) (96.79, 87.90) (96.84, 74.47) (96.43, 70.57) (96.24, 79.18) (96.44, 78.94) M 5 (95.27, 82.93) (94.83, 79.99) (96.27, 81.62) (96.39, 75.94) (96.69, 83.15) (95.91, 77.64) (95.89, 80.21) (96.08, 81.02) M 6 (95.92, 80.94) (95.31, 78.48) (96.23, 78.14) (96.56, 73.62) (96.45, 81.64) (96.90, 80.45) (96.22, 78.88) (96.55, 80.23) MH-UNet [12] (96.36, 83.49) (95.32, 81.84) (96.75, 77.20) (97.01, 88.21) (97.15, 78.95) (97.22, 75.85) (96.64, 80.92) (97.41, 85.21) MV-UNet [30] (95.12, 76.65) (94.57, 78.12) (95.55, 77.74) (95.79, 76.31) (95.87, 78.67) (95.68, 74.80) (95.43, 77.05) (97.42, 86.11) LS-UNet [18] (95.43, 75.66) (94.82, 74.56) (95.57, 73.52) (95.96, 72.30) (95.90, 75.72) (95.93, 72.85) (95.60, 74.10) (97.58, 82.68) MR-Net [21] (95.35, 81.77) (94.81, 81.18) (95.80, 79.23) (95.96, 84.46) (95.90, 79.04) (95.76, 76.20) (95.60, 80.31) (97.55, 87.20) CM-Net [27] (96.29, 84.59) (95.46, 81.44) (96.60, 81.84) (96.90, 87.52) (96.86, 82.39) (96.93, 78.82) (96.51, 82.77) (96.64, 81.96) Ours w/o SEM (96.49, 84.87) (95.69, 83.13) (96.42, 83.70) (96.93, 88.73) (96.64, 81.99) (96.77, 79.50) (96.49, 83.65) (96.42, 85.37) Ours w/o HPM (95.70, 81.62) (95.17, 79.95) (96.10, 79.38) (96.43, 78.26) (96.37, 80.01) (96.27, 76.21) (96.06, 79.24) (97.71, 87.56)

| Models |  | A 1 |  | A 2 | A 3 | A 4 | A 5 | A 6 | Average | Mean Voting |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M 1 |  |  |  |  |  |  |  |  |
| Image | GT | Ours | MR-Net | CM-Net | MV-UNet | MH-UNet |  |  |

## DICE (%) OF OUR PADL FRAMEWORK AND FIVE COMPETING METHODS OBTAINED ON FIVE SEGMENTATION TASKS USING THE QUBIQ DATASET. THE GROUND TRUTH IS THE MAJORITY VOTING WITH AVERAGE WEIGHT OF ANNOTATIONS FROM MULTIPLE ANNOTATORS, AND THE 'MEAN VOTING' OF EACH TASK IS CALCULATED.

| Methods | D s kidney D s brain D s tumor D s pros1 D s pros2 |
| --- | --- | --- | --- | --- |
| MV-UNet [30] 70.65 | 81.77 | 84.03 | 85.18 68.39 |
| LS-UNet [18] | 72.31 | 82.79 | 85.85 | 86.23 69.05 |
| MH-UNet [12] 73.44 | 83.54 | 86.74 | 87.03 75.61 |
| MR-Net [21] | 74.97 | 84.31 | 88.40 | 87.27 76.01 |
| CM-Net [27] | 76.01 | 84.75 | 87.37 | 88.73 77.39 |
| Ours | 80.34 | 85.86 | 89.25 | 93.30 80.67 |

## DICE (%) OF CM-NET AND OUR PADL ON FIVE TASKS OF THE QUBIQ DATASET. THE PREDICTIONS ARE EVALUATED AGAINST EACH ANNOTATOR'S DELINEATIONS, AND THE AVERAGE SOFT DICE ('AVERAGE') OVER ALL ANNOTATORS IS GIVEN.

| Methods | D s kidney D s brain D s tumor D s pros1 D s pros2 |
| --- | --- | --- | --- | --- |
| CM-Net [27] 80.63 | 83.16 | 87.17 | 87.42 73.45 |
| Ours | 82.26 | 83.19 | 87.58 | 92.26 75.16 |

## DICE (D s avg (%), D s mv (%)) OF PADL AND ITS TWO VARIANTS ON FIVE TASKS OF THE QUBIQ DATASET. THE PREDICTIONS ARE EVALUATED AGAINST EACH ANNOTATOR'S DELINEATIONS (D s avg : AVERAGE SOFT DICE OVER ALL ANNOTATORS) AND MEAN VOTING ANNOTATION (D s mv ). Ours w/o SEM (80.24, 79.84) (80.83, 85.36) (86.34, 87.63) (91.39, 93.13) (74.92, 80.05) Ours w/o HPM (79.36, 80.32) (80.45, 85.73) (86.80, 88.32) (90.45, 93.11) (74.84, 79.53) Ours (82.26, 80.34) (83.19, 85.86) (87.58, 89.25) (92.26, 93.30) (75.16, 80.67)

| Methods | D s kidney | D s brain | D s tumor | D s pros1 | D s pros2 |
| --- | --- | --- | --- | --- | --- |

## DICE (%) OF THE PADL WITH COMPLETE SEM MODULE AND ITS THREE VARIANTS ON THE RIGA DATASET. THE GROUND TRUTH IS THE MEAN VOTING ANNOTATION, AND THE 'MEAN VOTING' OF EACH TASK (OPTIC DISC/CUP SEGMENTATION) IS CALCULATED.

| Baseline √ √ √ √ | σ √ √ √ | SEM module Eµ µ prior √ √ √ | D s disc (%) D s cup (%) 96.42 85.37 97.58 86.93 97.65 87.45 97.65 87.75 |
| --- | --- | --- | --- |

## TABLE VI PERFORMANCE

|  | Models | Average |
| --- | --- | --- |
|  | 1 Layer 1 × 1 Conv | (63.13, 40.30) |
|  | 1 Layer 3 × 3 Conv | (96.55, 83.21) |
| F r µ | 1 Layer 5 × 5 Conv 1 Layer 3 × 3 Conv | (96.66, 82.93) (96.55, 83.21) |
|  | 2 Layers 3 × 3 Conv | (96.52, 84.18) |
|  | 3 Layers 3 × 3 Conv | (96.61, 82.45) |
| HPM w/o f img | (96.40, 83.39) |
| HPM w/o µ | (95.95, 80.22) |
| HPM |  | (96.52, 84.18) |

## PREFERENCE COUNTED ON TRAINING SET (TOP TWO ROWS), TEST SET (MIDDLE TWO ROWS), AND PREDICTED SEGMENTATION MAPS (BOTTOM TWO ROWS) ON THE RIGA DATASET. THE IOU BETWEEN EACH ANNOTATION/SEGMENTATION AND THE UNION OF SIX ANNOTATIONS/SEGMENTATION MAPS IS UTILIZED TO QUANTIFY THE ANNOTATOR'S PREFERENCE. THE NUMBER IN EACH BRACKET IS THE RANK OF IOU FROM HIGHEST TO LOWEST IN EACH ROW. Ar MEANS THE r-TH ANNOTATOR. Average IoU on Training Set Disc 89.46 (5) 88.29 (6) 93.40 (1) 90.63 (4) 92.93 (2) 90.97 (3) Cup 69.09 (3) 71.74 (2) 62.80 (4) 91.68 (1) 56.58 (5) 56.37 (6) Average IoU on Test Set Disc 88.26 (6) 88.50 (5) 94.76 (1) 91.49 (2) 92.77 (3) 89.55 (4) Cup 67.25 (3) 73.56 (2) 65.75 (4) 91.34 (1) 58.22 (5) 54.36 (6) Average IoU on Segmentation Maps Disc 96.14 (5) 95.48 (6) 99.00 (1) 96.48 (4) 98.47 (2) 96.85 (3) Cup 70.15 (3) 75.34 (2) 62.08 (4) 99.35 (1) 56.49 (6) 57.49 (5)

|  | (%) |  |  | A1 |  | A2 | A3 | A4 | A5 |  | A6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Image |  |  |  |  |  |  |  |  |  |  |  |
| MV/MS |  |  |  |  |  |  |  |  |  |  |  |
| 𝐴 1 |  |  |  |  |  |  |  |  |  |  |  |
| 𝐴 2 |  |  |  |  |  |  |  |  |  |  |  |
| 𝐴 3 |  |  |  |  |  |  |  |  |  |  |  |
| 𝐴 4 |  |  |  |  |  |  |  |  |  |  |  |
| 𝐴 5 |  |  |  |  |  |  |  |  |  |  |  |
| 𝐴 6 |  |  |  |  |  |  |  |  |  |  |  |
| GT | 𝜇 𝑟 | GT | 𝜇 𝑟 | GT | 𝜇 𝑟 | GT | 𝜇 𝑟 | GT | 𝜇 𝑟 | GT | 𝜇 𝑟 |

### Formule


$$A 1 A 2 A 3 A 4 A 5 A 6$$

### Formule


$$D = {x i , y i1 , y i2 , • • • , y iR } N i=1$$

### Formule


$$f img = F D (F E (x; θ E ) ; θ D ) ,(1)$$

### Formule


$$µ = F µ (f img ; θ µ ) ,(2)$$

### Formule


$$f σ = F σ (f img ; θ σ ) ,(3)$$

### Formule


$$E µ = -µ × log 2 (µ) -(1 -µ) × log 2 (1 -µ).(4)$$

### Formule


$$f σ = f σ × (1 + E µ ).(5)$$

### Formule


$$σ = F o σ ((µ c f σ ); θ o σ ),(6)$$

### Formule


$$µ r = F r µ ((µ c F r p (f img ; θ r p )); θ r µ ),(7)$$

### Formule


$$L = L meta (y s , ŷs ) + R r=1 L pref (y r , ŷs r ),(8)$$

### Formule


$$L meta (y s , ŷs ) = -y s × log ŷs -(1 -y s ) × log (1 -ŷs ).(9)$$
