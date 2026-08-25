# LDFSAM: Localization Distillation-Enhanced Feature Prompting SAM for Medical Image Segmentation.

**Auteurs** : Zhao X, Wang C, Xu H, Zhou H, Yu Z, Chen T, Wei X, Zhang R.
**Année** : 2026
**DOI** : 10.3390/jimaging12020074

## Résumé

Standard SAM-based approaches in medical imaging typically rely on explicit geometric prompts, such as bounding boxes or points. However, these rigid spatial constraints are often insufficient for capturing the complex, deformable boundaries of medical structures, where localization noise easily propagates into segmentation errors. To overcome this, we propose the Localization Distillation-Enhanced Feature Prompting SAM (LDFSAM), a novel framework that shifts from discrete coordinate inputs to a latent feature prompting paradigm. We employ a lightweight prompt generator, refined via Localization Distillation (LD), to inject multi-scale features into the SAM decoder as complementary Dense Feature Prompts (DFPs) and Sparse Feature Prompts (SFPs). This effectively guides segmentation without explicit box constraints. Extensive experiments on four public benchmarks (3D CBCT Tooth, ISIC 2018, MMOTU, and Kvasir-SEG) demonstrate that LDFSAM outperforms both prior SAM-based baselines and conve

## Méthodologie

{'study_design': 'Development and evaluation of a novel SAM-based segmentation framework (LDFSAM) using a lightweight prompt generator refined via Localization Distillation (LD) to produce Dense Feature Prompts (DFPs) and Sparse Feature Prompts (SFPs) injected into the SAM decoder, compared against SAM, MedSAM, SAMed, SAM-Med2D and conventional networks', 'intervention': 'LDFSAM: latent feature prompting using LD-refined multi-scale features (DFP + SFP) fed into the SAM decoder, replacing explicit bounding box/point prompts; uses a YOLOv8x teacher and YOLOv8n student for localization distillation', 'control': 'Comparison against SAM, MedSAM, SAMed, and SAM-Med2D (SAM-based baselines) and conventional task-specific segmentation networks', 'primary_outcomes': ['Dice score for segmentation accuracy across four datasets under varying annotation budgets (10%, 20%, 50%, 100%)'], 'secondary_outcomes': ['Parameter counts and computational costs (GPU hours, GFLOPs, FPS)', 'Qualitative boundary adherence and suppression of spurious segmentations', 'Cross-dataset generalization on private in-house CBCT cohort'], 'statistical_methods': ['Five independent runs with fixed random seeds ({10, 42, 123, 2025, 3407})', '95% confidence intervals estimated via non-parametric bootstrap resampling (B = 1000)'], 'duration': None, 'setting': 'Not specified (research/laboratory setting; datasets include CBCT, dermoscopy, ultrasound, and colonoscopy imaging)'}

## Résultats

{'quantitative': [{'outcome': 'Dice score across four public benchmarks', 'value': 'exceeding 0.91', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Extensive experiments on four public benchmarks (3D CBCT Tooth, ISIC 2018, MMOTU, and Kvasir-SEG) demonstrate that LDFSAM outperforms both prior SAM-based baselines and conventional networks, achieving Dice scores exceeding 0.91.'}, {'outcome': 'Automatic prompt generation branch parameters', 'value': '3.3', 'unit': 'M parameters', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'The automatic prompt generation branch operates at 640 × 640 resolution and contains approximately 3.3 M parameters with about 9.4 GFLOPs per image, running at ~122 FPS under our profiling setup.'}, {'outcome': 'SAM segmentation network parameters (excluding prompt branch)', 'value': '271.2', 'unit': 'M parameters', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'Excluding this branch, our SAM segmentation network has approximately 271.2 M parameters.'}, {'outcome': 'Additional parameter overhead of prompt branch', 'value': '1.2', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'Therefore, the proposed prompt branch adds only about 1.2% additional parameters relative to the segmentation model, resulting in a modest computational and memory overhead while enabling fully automatic feature-based prompting.'}], 'qualitative_findings': ['LDFSAM yields masks that adhere more closely to fine tooth boundaries in CBCT slices', 'LDFSAM better captures irregular lesion shapes in dermoscopy images', 'LDFSAM suppresses spurious foreground blobs in colonoscopy scenes'], 'main_findings': ['Latent feature-level prompts (DFP and SFPs) substantially outperform geometric box prompts', 'Combining DFPs and SFPs yields consistent gains over using either alone', 'LDFSAM surpasses existing SAM-based baselines across all annotation budgets (10%, 20%, 50%, 100%), with the advantage most pronounced in low-annotation regimes (10-20%)', 'As training data proportion increases, the performance gap to other SAM-based methods narrows but remains consistent, with LDFSAM showing narrower confidence interval shaded areas reflecting superior stability', 'LDFSAM maintains training time cost comparable to SAM-Med2D despite larger parameter count, achieving lower GPU hours than SAM/MedSAM/SAMed across all four datasets', 'The automatic prompt generation branch is lightweight, adding only ~1.2% additional parameters', 'LDFSAM demonstrates robust generalization on a private in-house CBCT cohort']}

## Conclusions

LDFSAM enhances SAM-based medical segmentation by replacing geometric prompts with localization-distilled feature prompts delivered in the latent space A lightweight detector refined through localization distillation (LD) supplies multi-scale features transformed into DFP and SFP, giving the decoder richer spatial and appearance cues than traditional box or point prompts Feature-based latent prompts substantially outperform box prompts, and combining DFP and SFP yields consistent gains over using either alone Refining the prompt generator via localization-aware distillation is crucial for stable and accurate segmentation LDFSAM consistently surpasses existing SAM-based methods under varying annotation budgets, especially in low-label regimes, achieving Dice scores competitive with or superior to strong task-specific segmentation networks The proposed latent feature prompting mechanism maintains good generalization beyond public benchmarks, as shown on a private in-house CBCT dataset Carefully designed feature-level prompts distilled from a localization model can narrow the gap between generic foundation models and specialized medical segmentation architectures while keeping inference lightweight and modular

## Ablation experiments of bounding-box baseline and dense-sparse feature prompts validity with YOLOv8n/x backbones on 3D CBCT Tooth, ISIC 2018, MMOTU, and Kvasir-SEG datasets. ↑ denotes higher is better. Bold values indicate the best results.

|  |  | 3D CBCT Tooth | ISIC 2018 |  | MMOTU |  | Kvasir-SEG |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Backbone | Method | IoU (%) ↑ | Dice (%) ↑ | IoU (%) ↑ | Dice (%) ↑ | IoU (%) ↑ | Dice(%) ↑ | IoU (%) ↑ | Dice (%) ↑ |
|  | Baseline | 78.91 | 87.36 | 83.55 | 90.28 | 79.34 | 87.88 | 81.67 | 89.54 |
|  | Feature-D | 81.05 | 88.92 | 85.66 | 91.83 | 82.29 | 89.72 | 85.01 | 91.06 |
| YOLOv8n | Feature-S | 79.36 | 88.14 | 84.59 | 91.09 | 81.05 | 88.95 | 84.04 | 90.82 |
|  | Feature-S+D | 81.89 | 89.65 | 86.65 | 92.46 | 83.13 | 90.30 | 85.16 | 91.57 |
|  | Baseline | 81.64 | 89.30 | 85.62 | 91.86 | 83.01 | 90.23 | 84.50 | 91.10 |
|  | Feature-D | 84.78 | 91.05 | 87.90 | 93.26 | 86.15 | 92.21 | 87.44 | 92.81 |
| YOLOv8x | Feature-S | 83.56 | 90.17 | 86.76 | 92.62 | 84.72 | 91.39 | 86.28 | 92.33 |
|  | Feature-S+D | 85.98 | 91.93 | 89.05 | 93.95 | 87.11 | 92.76 | 87.62 | 93.12 |

## Ablation experiments of distillation schemes (w/o distillation, KD distillation, LD (Main) distillation, LD (Main+VLR) distillation) validity on 3D CBCT Tooth, ISIC 2018, MMOTU, and Kvasir-SEG datasets. ↑ denotes higher is better. Bold values indicate the best results.

|  | 3D CBCT Tooth | ISIC 2018 |  | MMOTU |  | Kvasir-SEG |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Method | IoU (%) ↑ | Dice (%) ↑ | IoU (%) ↑ | Dice (%) ↑ | IoU (%) ↑ | Dice (%) ↑ | IoU (%) ↑ | Dice (%) ↑ |
| w/o distillation | 82.03 | 89.65 | 86.94 | 92.46 | 83.16 | 90.30 | 85.53 | 91.57 |
| KD distillation | 85.25 | 91.13 | 88.65 | 93.47 | 86.04 | 91.91 | 87.42 | 92.77 |
| LD (Main) distillation | 85.69 | 91.64 | 88.98 | 93.59 | 86.10 | 92.05 | 87.82 | 92.91 |
| LD (Main+VLR) distillation | 85.81 | 91.79 | 89.27 | 93.71 | 86.56 | 92.21 | 88.10 | 93.04 |

## Comparison of model parameters and computational costs on four datasets.

| Method | All | Trainable | GPU-Hours@100% Masks |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Params (M) | Params (M) | CBCT | ISIC2018 | MMOTU | Kvasir-SEG |
| SAM [6] | 93.7 | 4.1 | 421.5 | 38.6 | 22.3 | 19.7 |
| MedSAM [7] | 93.7 | 4.1 | 410.4 | 30.8 | 17.2 | 15.3 |
| SAMed [21] | 93.9 | 4.2 | 216.7 | 11.9 | 6.4 | 6.0 |
| SAMMed2D [8] | 271.2 | 186.8 | 132.0 | 7.9 | 3.8 | 3.0 |
| LDFSAM | 274.5 | 190.1 | 134.1 | 8.1 | 3.9 | 3.2 |

## Comparison of segmentation performance on the 3D CBCT Tooth dataset. Bold values indicate the best results. ↑ denotes higher is better, and ↓ denotes lower is better.

| Method | IoU (%) ↑ | Dice (%) ↑ | HD (mm) ↓ | ASSD (mm) ↓ | SO (%) ↑ |
| --- | --- | --- | --- | --- | --- |
| UNet3D [11] | 68.00 | 79.52 | 113.78 | 25.50 | 67.09 |
| DenseVNet [33] | 84.57 | 91.15 | 8.21 | 1.14 | 94.88 |
| AttentionUNet3D [34] | 52.52 | 64.08 | 147.10 | 61.10 | 42.49 |
| UNETR [35] | 74.30 | 81.84 | 107.89 | 17.95 | 73.14 |
| SwinUNETR [36] | 83.10 | 89.74 | 82.71 | 7.50 | 86.80 |
| nnFormer [37] | 83.54 | 90.66 | 51.28 | 5.08 | 90.89 |
| 3D UX-Net [38] | 75.40 | 84.89 | 108.52 | 19.69 | 73.48 |
| nnU-Net [4] | 85.33 | 91.50 | 7.87 | 0.96 | 95.05 |
| SegFormer [39] | 85.06 | 91.37 | 9.54 | 1.22 | 93.47 |
| TransUNet [16] | 84.65 | 90.69 | 12.30 | 2.65 | 91.26 |
| LDFSAM | 85.81 | 91.79 | 5.05 | 0.63 | 95.82 |

## Comparison of segmentation performance on ISIC 2018 and Kvasir-SEG datasets. ↑ denotes higher is better. Bold values indicate the best results for each metric.

| Method | ISIC 2018 IoU (%) ↑ | Dice (%) ↑ | ACC (%) ↑ | Kvasir-SEG IoU (%) ↑ | Dice (%) ↑ | ACC (%) ↑ |
| --- | --- | --- | --- | --- | --- | --- |
| U-Net [3] | 76.77 | 86.55 | 95.00 | 73.04 | 84.56 | 95.50 |
| AttU-Net [34] | 78.19 | 87.54 | 95.33 | 75.67 | 86.20 | 95.90 |
| CA-Net [40] | 68.82 | 80.96 | 92.96 | 71.48 | 83.29 | 94.98 |
| CE-Net [41] | 78.05 | 87.47 | 95.40 | 71.98 | 83.72 | 94.91 |
| CPF-Net [42] | 78.47 | 87.70 | 95.52 | 71.11 | 83.54 | 94.85 |
| CKDNet [43] | 77.89 | 87.35 | 95.27 | 70.23 | 82.74 | 94.60 |
| nnU-Net [4] | 80.10 | 88.42 | 95.88 | 87.15 | 92.90 | 98.11 |
| SegFormer [39] | 87.33 | 92.60 | 97.51 | 86.87 | 92.11 | 97.07 |
| TransUNet [16] | 82.45 | 89.53 | 96.39 | 77.65 | 86.82 | 96.04 |
| LDFSAM | 88.47 | 93.71 | 97.86 | 87.22 | 93.04 | 98.39 |

## Comparison of segmentation performance on the MMOTU dataset. Bold values indicate the best results. ↑ denotes higher is better, and ↓ denotes lower is better.

| Method | IoU (%) ↑ | Dice (%) ↑ | HD (mm) ↓ | ASSD (mm) ↓ | ACC (%) ↑ |
| --- | --- | --- | --- | --- | --- |
| U-Net [3] | 80.06 | 88.38 | 18.59 | 3.57 | 96.01 |
| nnU-Net [4] | 84.66 | 91.02 | 13.78 | 1.87 | 96.55 |
| SegFormer [39] | 82.52 | 90.14 | 15.11 | 2.42 | 96.30 |
| TransUNet [16] | 81.35 | 89.30 | 15.69 | 2.78 | 96.13 |
| LDFSAM | 86.56 | 92.21 | 12.05 | 1.80 | 97.10 |

## Results on the private CBCT dataset. Performance drops in IoU and Dice when transferring models from the public 3D CBCT Tooth dataset to the private CBCT dataset. ↑ denotes higher is better, and ↓ denotes lower is better. Bold values indicate the best results.

|  | Public Dataset |  | Private Dataset |  |
| --- | --- | --- | --- | --- |
|  | IoU (%) ↑ | Dice (%) ↑ | IoU (%) ↑ | Dice (%) ↑ |
| SAM-Med2D [8] | 82.36 | 90.10 | 79.71 (↓2.65) | 88.24 (↓1.86) |
| nnUNet [4] | 85.28 | 91.45 | 81.87 (↓3.41) | 89.33 (↓2.12) |
| LDFSAM | 85.81 | 91.79 | 84.22 (↓1.59) | 90.87 (↓0.92) |

### Formule


$$F fused = Φ mix (Concat[P 3 , Up(P 4 ), Up(P 5 )])(1)$$

### Formule


$$F fused ∈ R H S × W$$

### Formule


$$Z cond = Z img + α • P dense (2$$

### Formule


$$)$$

### Formule


$$T sparse = MLP(GAP(F fused ))(3)$$

### Formule


$$p i = S(z i , τ) = e z i /τ$$

### Formule


$$L LD (p S , p T ) = ∑ e∈{t,b,l,r} H (p e T , p e S )(5)$$

### Formule


$$Ω vlr = k | γα pos ≤ X k < α pos (6$$

### Formule


$$)$$

### Formule


$$L total = L det + λ main ∑k∈Ωmai n L (k) LD + λ vlr ∑k∈Ωvl r L (k) LD (7$$

### Formule


$$)$$
