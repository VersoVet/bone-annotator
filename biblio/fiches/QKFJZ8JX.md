# Accelerating Volumetric Medical Image Annotation via Short-Long Memory SAM 2.

**Auteurs** : Chen Y, Yildiz Z, Li Q, Chen Y, Dong H, Gu H, Konz N, Mazurowski MA.
**Année** : 2026
**DOI** : 10.1109/tmi.2025.3627954

## Résumé

Manual annotation of volumetric medical images, such as magnetic resonance imaging (MRI) and computed tomography (CT), is a labor-intensive and time-consuming process. Recent advancements in foundation models for video object segmentation, such as Segment Anything Model 2 (SAM 2), offer a potential opportunity to significantly speed up the annotation process by manually annotating one or a few slices and then propagating target masks across the entire volume. However, the performance of SAM 2 in this context varies. Our experiments show that relying on a single memory bank and attention module is prone to error propagation, particularly at boundary regions where the target is present in the previous slice but absent in the current one. To address this problem, we propose Short-Long Memory SAM 2 (SLM-SAM 2), a novel architecture that integrates distinct short-term and long-term memory banks with separate attention modules to improve segmentation accuracy. We evaluate SLM-SAM 2 on four p

## Méthodologie

{'study_design': 'Comparative experimental evaluation of a novel volumetric medical image segmentation/annotation propagation architecture (SLM-SAM 2) against multiple baseline models on four public datasets', 'intervention': 'Application of SLM-SAM 2, which integrates separate short-term and long-term memory banks with distinct attention modules and a learnable attention fuser, to propagate manually annotated masks from one or a few slices across an entire volumetric image', 'control': 'Default SAM 2 (single memory bank and attention module), Cutie, Cutie+, iSegFormer, nnUNet (basic and exhaustive settings), Medical SAM Adapter (MSA), UNETR, Swin UNETR, LSTM-MM-UNet, BCDUNet, VoxelMorph, Sli2Vol', 'primary_outcomes': ['Dice Similarity Coefficient (DSC)', 'Average Symmetric Surface Distance (ASSD)'], 'secondary_outcomes': ['Manual correction time reduction'], 'statistical_methods': ['Bootstrapping with 1000 resamples for confidence interval estimation'], 'duration': None, 'setting': 'Four public datasets covering organs, bones, muscles and fetal head, using MRI, CT, and ultrasound video/volumetric data; models trained using AdamW optimizer with initial learning rate of 1×10⁻³'}

## Résultats

{'quantitative': [{'outcome': 'Average Dice Similarity Coefficient improvement over default SAM 2 (5 volumes scenario)', 'value': '0.14', 'unit': 'DSC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'achieving an average Dice Similarity Coefficient improvement of 0.14 and 0.10 in the scenarios when 5 volumes and 1 volume are'}, {'outcome': 'Average Dice Similarity Coefficient improvement over default SAM 2 (1 volume scenario)', 'value': '0.10', 'unit': 'DSC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'achieving an average Dice Similarity Coefficient improvement of 0.14 and 0.10 in the scenarios when 5 volumes and 1 volume are'}, {'outcome': 'Reduction in manual correction time', 'value': '60.575', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'we showed that SLM-SAM 2 reduces manual correction time by 60.575%, highlighting its practical value in medical image annotation.'}], 'qualitative_findings': ['SLM-SAM 2 outperforms SAM 2 on most datasets under the 1-Volume setting, excluding CT-Heart, where both methods perform similarly', 'SLM-SAM 2 exhibits greater robustness than SAM 2 in handling over-propagation with gaps and intermittent object reappearances', 'Performance within each method remains comparable under varying initial slice settings'], 'main_findings': ['Relying on a single memory bank and attention module (default SAM 2) is prone to error propagation, particularly at boundary regions where the target is present in the previous slice but absent in the current one', 'SLM-SAM 2 markedly outperforms default SAM 2 across four public datasets covering organs, bones, and muscles in MRI, CT, and ultrasound', 'SLM-SAM 2 demonstrates the best average performance among all baselines in both DSC and ASSD', 'SLM-SAM 2 outperforms all baselines on most datasets by a significant margin']}

## Conclusions

SLM-SAM 2 introduces a dynamic short-long memory module integrating both short-term and long-term memory along with a learnable attention fuser to accelerate volumetric medical image annotation SLM-SAM 2 demonstrates superior performance compared to leading automatic 2D and 3D models, as well as state-of-the-art unsupervised and supervised VOS methods, effectively alleviating over-propagation issues and other common propagation errors SLM-SAM 2 reduces manual correction time by 60.575%, highlighting its practical value in medical image annotation A 3D Slicer extension (SegmentHumanBody) has been developed to enable interactive inference and bidirectional mask propagation using finetuned SLM-SAM 2 checkpoint weights

## UNet 0.4483 18.7278 0.0741 18.4087 0.1178 21.6110 0.3521 14.5100 0.1877 46.1875 0.4406 31.9848 0.1423 54.3272 0.0935 51.4670 0.5311 30.1221

| 0.6991 10.8537 | 0.7817 9.2342 | 0.7356 6.9148 |  | 0.5376 18.6205 | 0.5796 14.2872 |  |  | 0.4005 10.8755 |  | 0.4984 10.8782 | 0.4128 15.3546 |  | 0.5239 51.1868 | 0.8500 3.1714 | 0.8501 3.1133 | 0.8635 2.3445 | 0.8764 2.4207 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.4850 | 1.4003 | 2.4229 |  | 7.7069 | 3.7137 |  |  | 3.3482 |  | 2.8654 | 4.0077 |  | 4.5420 | 1.5448 | 1.5357 | 1.4530 | 0.7524 |  |
| 0.6818 | 0.7562 | 0.5967 |  | 0.3260 | 0.4981 |  |  | 0.2674 |  | 0.5163 | 0.4352 |  | 0.7347 | 0.6813 | 0.6839 | 0.7045 | 0.8118 |  |
| 1.9009 | 1.7841 | 1.6441 |  | 3.8774 | 3.9244 |  |  | 4.4915 |  | 3.0872 | 3.7066 |  | 1.7567 | 2.1894 | 2.1434 | 1.4828 | 0.7276 |  |
| 8917 0.3348 8.1976 0.1445 22.6483 0.2731 10.8427 0.6426 7.5425 0.9013 1.8705 0.7083 | nnUNet (E) † 0.9073 2.8406 0.6234 8.8195 0.4337 23.2610 0.7548 29.3823 0.8013 9.1686 0.9476 1.5655 0.7843 | MSA 0.8366 1.7724 0.5203 4.8257 0.1514 10.6728 0.6367 3.4611 0.7020 5.4726 0.9223 3.3323 0.6345 | II. 3D Models | UNETR 0.4661 22.5008 0.2754 13.3468 0.0320 76.1877 0.1548 51.7418 0.5727 21.5100 0.5524 10.3962 0.4691 | SwinUNETR 0.6508 4.6814 0.3778 8.8737 0.1525 13.4887 0.3182 21.0385 0.5937 17.1132 0.5948 8.6549 0.5324 | III. ConvLSTM/BiConvLSTM-based Models | LSTM-MM- | BCDUNet 0.4253 4.4763 0.0651 21.7007 0.1100 26.6618 0.1191 7.2795 0.4579 25.5236 0.0539 15.8434 0.2282 | IV. Unsupervised VOS Models | VoxelMorph 0.3854 5.8693 0.2501 13.7858 0.4307 15.6178 0.7806 2.6862 0.5211 6.6286 0.3411 8.3026 0.5707 | Sli2Vol 0.8287 1.6272 0.4676 10.9631 0.4636 13.0736 0.7549 5.3969 0.6243 6.3413 0.3042 9.1010 0.5214 | V. Semi-supervised VOS Models | 7.8476 0.6496 13.9058 0.5769 47.0773 0.8156 iSegFormer 0.8067 8.9592 0.4358 17.7530 0.5016 14.4014 0.8605 | 0.5550 0.7855 6.2811 0.6303 16.7382 0.7081 8.3856 0.9629 Cutie 0.8976 1.9001 0.5340 6.6390 0.6806 | 0.5197 0.7031 12.2835 0.6285 17.0783 0.7209 7.7925 0.9574 Cutie+ 0.8997 1.6683 0.5572 6.3690 0.6628 | 0.4508 0.6925 15.6042 0.6267 52.3565 0.7926 9.1385 0.9633 SAM 2 0.8668 5.9103 0.2341 30.4152 0.6381 | 0.9643 0.4298 0.8543 0.4767 0.7655 8.2143 4.0753 0.9607 SLM-SAM 2 0.9368 1.3643 0.6294 8.4185 0.7255 | †: METHOD REQUIRES RETRAINING FOR EACH TEST VOLUME. |

## PERFORMANCE (DSC) OF SAM 2 AND SLM-SAM 2 ACROSS ALL DATASETS UNDER DIFFERENT INITIAL SLICE SELECTION OPTIONS. BEST RESULTS ARE IN BOLD.

| Methods | Q | L | M |
| --- | --- | --- | --- |
| SAM 2 | 0.7261 0.7296 0.7042 |
| SLM-SAM 2 0.8107 0.8231 0.8390 |

### Formule


$$A SAM2 t = A F I t , ℳ(1)$$

### Formule


$$F I t = E I I t (2) ℳ = { F M j | F M j ∈ ℳ} (3$$

### Formule


$$A sℎort t = A sℎort F I t , ℳ sℎort(4)$$

### Formule


$$A long t = A long F I t , ℳ long(5)$$

### Formule


$$ℳ sℎort = F M t -1(6)$$

### Formule


$$ℳ long = F M t -1 , F M t -2 , …, F M t -6 , F M c (7$$

### Formule


$$A SLM -SAM2 t = ℱ A sℎort t , A long t(8)$$

### Formule


$$DSC(A, B) = 2 A ∩ B A + B(9)$$

### Formule


$$ASSD(A, B) = p ∈ S A d p, S B + q ∈ S B d q, S A S A + S B(10)$$

### Formule


$$denoted as ℳ O + ℳ R = 7 .$$

### Formule


$$ℳ O + ℳ R = 1 consistently outperforms ℳ O + ℳ R = 7 ,$$

### Formule


$$SP V saved = SP V SAM2 -SP V SLM -SAM2 SP V SAM2(13)$$

### Formule


$$CSR saved = CSR SAM2 -CSR SLM -SAM2 CSR SAM2(14)$$
