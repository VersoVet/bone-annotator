# MA-SAM: Modality-agnostic SAM adaptation for 3D medical image segmentation.

**Auteurs** : Cheng Chen, Juzheng Miao, Dufan Wu, Aoxiao Zhong, Zhiling Yan, Sekeun Kim, Jiang Hu, Zhengliang Liu, Lichao Sun, Xiang Li, Tianming Liu, Pheng-Ann Heng, Quanzheng Li
**Année** : 2024
**DOI** : 10.1016/j.media.2024.103310

## Résumé

The Segment Anything Model (SAM), a foundation model for general image segmentation, has demonstrated impressive zero-shot performance across numerous natural image segmentation tasks. However, SAM's performance significantly declines when applied to medical images, primarily due to the substantial disparity between natural and medical image domains. To effectively adapt SAM to medical images, it is important to incorporate critical third-dimensional information, i.e., volumetric or temporal knowledge, during fine-tuning. Simultaneously, we aim to harness SAM's pre-trained weights within its original 2D backbone to the fullest extent. In this paper, we introduce a modality-agnostic SAM adaptation framework, named as MA-SAM, that is applicable to various volumetric and video medical data. Our method roots in the parameter-efficient fine-tuning strategy to update only a small portion of weight increments while preserving the majority of SAM's pre-trained weights. By injecting a series of

## Méthodologie

{'study_design': "Development and benchmarking of a modality-agnostic, parameter-efficient fine-tuning framework (MA-SAM) for adapting SAM's image encoder (via FacT tensorization-decomposition and injected 3D adapters) and a fully fine-tuned mask decoder with progressive up-sampling, evaluated against SOTA 3D segmentation methods on multiple public datasets.", 'intervention': "Parameter-efficient fine-tuning of SAM's image encoder using FacT plus injected 3D adapters in each transformer block to capture volumetric/temporal information, combined with full fine-tuning of a modified mask decoder with progressive up-sampling; evaluated both without prompts (automatic) and with prompts (e.g., 3D bounding box) for tumor segmentation.", 'control': 'Comparison against SOTA 3D medical image segmentation methods (e.g., nnU-Net, 3D UX-Net, SwinUNETR, nnFormer, 3DSAM-adapter) and a pure 2D SAM fine-tuning baseline (SAMed h).', 'primary_outcomes': ['Dice score', 'Normalized Surface Dice (NSD)'], 'secondary_outcomes': ['Generalization performance compared to domain generalization approaches', 'Effect of prompt quality (tight vs. relaxed bounding boxes) on segmentation performance'], 'statistical_methods': [], 'duration': None, 'setting': 'Benchmark evaluation on 10 public datasets across CT, MRI, and surgical video medical imaging modalities'}

## Résultats

{'quantitative': [{'outcome': 'Dice improvement over nnU-Net across three automatic segmentation tasks', 'value': '0.9%, 2.6%, 9.9%', 'unit': '% Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'surpassing nnU-Net by 0.9%, 2.6%, and 9.9% in Dice for CT multi-organ segmentation, MRI prostate segmentation, and surgical scene segmentation respectively'}, {'outcome': 'Dice improvement over second-best performing approach (automatic segmentation, three tasks)', 'value': '0.9%, 2.6%, 5%', 'unit': '% Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'our method improves the Dice score by 0.9%, 2.6%, 5% compared to the second-best performing approach, respectively'}, {'outcome': 'Best automatic model Dice score for pancreas tumor segmentation', 'value': '41.6', 'unit': '% Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'all automatic segmentation models struggle to correctly delineate pancreas tumor regions, obtaining merely a 41.6% Dice score for the best-performing model'}, {'outcome': 'Dice score with tight 3D bounding box prompt (tumor segmentation)', 'value': '80.35', 'unit': '% Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'By adding prompts in the form of one tight 3D bounding box per volume into the model, our method remarkably boosts the Dice score from 41.6% to 80.35%'}, {'outcome': 'Dice score with 5% relaxed bounding box prompt (tumor segmentation)', 'value': '74.7', 'unit': '% Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'if allowing 5% relaxation on the tightness of provided bounding box, the performance drops to 74.7%'}, {'outcome': 'Dice improvement over 3DSAM-adapter (automatic segmentation, tumor task)', 'value': '10', 'unit': '% Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'Our method also significantly outperforms the recent holistic 3D SAM adaptation method 3DSAM-adapter, with 10% Dice improvement when using automatic segmentation'}, {'outcome': 'Dice improvement over nnU-Net with prompts (tumor segmentation)', 'value': '38.7', 'unit': '% Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Introduction', 'source_quote': 'We show that by further leveraging prompts, our method achieves impressive results in challenging tumor segmentation task, surpassing nnU-Net by 38.7% in Dice score.'}, {'outcome': 'nnU-Net Dice/NSD (tumor segmentation benchmark table)', 'value': '41.6 / 62.5', 'unit': '% Dice / % NSD', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'Dice ↑ NSD ↑ nnU-Net (Isensee et al., 2021) 41.6 62.5'}], 'qualitative_findings': ["SAM's automatic segmentation performance falls slightly behind nnU-Net specifically on tumor segmentation, suggesting reduced effectiveness for objects with ill-defined margins and small sizes, which differ from SAM's natural-image pre-training distribution"], 'main_findings': ['MA-SAM, without any prompts, consistently and significantly outperforms SOTA 3D segmentation approaches across CT multi-organ, MRI prostate, and surgical scene segmentation tasks', 'MA-SAM outperforms the pure 2D SAM fine-tuning method SAMed h, demonstrating the benefit of incorporating volumetric/temporal information', 'MA-SAM demonstrates strong generalization capability, exceeding SOTA domain generalization approaches', 'Using prompts (3D bounding boxes) substantially improves performance on challenging pancreas tumor segmentation, though performance is sensitive to prompt quality/tightness']}

## Conclusions

MA-SAM is a general, modality-agnostic, parameter-efficient SAM adaptation framework applicable to diverse medical image segmentation tasks (CT, MRI, surgical video) Without prompts, MA-SAM's automatic segmentation outperforms various SOTA 3D medical image segmentation methods by a large margin MA-SAM demonstrates outstanding generalization capability, important for deployment across medical datasets Prompt-based segmentation provides substantial advantages for challenging tumor segmentation tasks

## Comparison of abdominal multi-organ segmentation results generated from our MA-SAM method and other state-of-the-art methods on BTCV dataset.

| Methods | Spleen R.Kd L.Kd GB Eso. Liver Stomach Aorta IVC Veins Pancreas AG Average |
| --- | --- | --- | --- | --- | --- |
|  |  | Dice [%] ↑ |  |  |  |
| nnU-Net (Isensee et al., 2021) | 97.0 95.3 | 95.3 63.5 77.5 97.4 | 89.1 | 90.1 88.5 79.0 | 87.1 75.2 86.3 |
| 3D UX-Net (Lee et al., 2023) | 94.6 94.2 | 94.3 59.3 72.2 96.4 | 73.4 | 87.2 84.9 72.2 | 80.9 67.1 81.4 |
| SwinUNETR (Tang et al., 2022b) 95.6 94.2 | 94.3 63.6 75.5 96.6 | 79.2 | 89.9 83.7 75.0 | 82.2 67.3 83.1 |
| nnFormer (Zhou et al., 2023a) | 93.5 94.9 | 95.0 64.1 79.5 96.8 | 90.1 | 89.7 85.9 77.8 | 85.6 73.9 85.6 |
| SAMed h (Zhang and Liu, 2023) 95.3 92.1 | 92.9 62.1 75.3 96.4 | 90.2 | 87.6 79.8 74.2 | 77.9 61.0 82.1 |
| MA-SAM (Ours) | 96.7 95.1 | 95.4 68.2 82.1 96.9 | 92.8 | 91.1 87.5 79.8 | 86.6 73.9 87.2 |
|  |  | HD [%] ↓ |  |  |  |
| nnU-Net (Isensee et al., 2021) | 1.07 1.19 | 1.19 7.49 8.56 1.14 | 4.84 14.11 2.87 5.67 | 2.31 2.23 4.39 |
| 3D UX-Net (Lee et al., 2023) | 3.17 1.59 | 1.26 4.53 13.92 1.75 19.72 12.53 3.47 9.99 | 3.70 4.11 6.68 |
| SwinUNETR (Tang et al., 2022b) 1.21 1.41 | 1.37 2.25 5.82 1.70 13.75 5.92 4.46 7.58 | 3.53 3.40 4.37 |
| nnFormer (Zhou et al., 2023a) | 78.03 1.41 | 1.43 3.00 4.92 1.38 | 4.24 | 7.53 4.02 6.53 | 2.96 2.76 9.95 |
| SAMed h (Zhang and Liu, 2023) 1.37 33.53 1.84 6.27 4.84 1.77 | 7.49 | 4.97 7.28 6.87 10.00 6.49 7.73 |
| MA-SAM (Ours) | 1.00 1.19 | 1.07 1.59 3.77 1.36 | 3.87 | 5.29 3.12 3.25 | 3.93 2.57 2.67 |

## Comparison of prostate segmentation results generated from our MA-SAM method and other state-of-the-art methods on six prostate MRI datasets.

| Spleen | Right kidney | Left kidney | Esophagus | Gallbladder | Liver | Stomach | Aorta | IVC | Veins | Pancreas | Adrenal gland |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CT image | Ground truth | nnU-Net | 3D UX-Net |  | SwinUNETR | nnFormer | SAMed_h | MA-SAM (ours) |

## Comparison of segmentation results from different methods for surgical scene segmentation on Endovis18 dataset.

| Methods | mIoU | Sequence (mIoU) Seq 1 Seq 2 Seq 3 Seq 4 | Dice |
| --- | --- | --- | --- |
| NCT |  |  |  |

## Comparison of generalization performance of nnU-Net and our MA-SAM model with SOTA domain generalization methods on prostate datasets.

| Methods | Site B Site C Site D Site E Site F Average |
| --- | --- | --- |
| nnU-Net (Isensee et al., 2021) 72.0 69.6 84.7 42.5 82.9 | 70.3 |
| TTST* (Karani et al., 2021) | 86.0 74.8 81.0 74.0 80.9 | 79.3 |
| TASD* (Liu et al., 2022) | 87.1 76.4 82.5 76.0 83.2 | 81.1 |
| MA-SAM (Ours) | 86.7 66.6 88.6 79.1 89.5 | 82.1 |

## Comparison of model performance with different mask decoder designs.

| Decoder design | Dice [%] |
| --- | --- |
| SAM mask decoder | 84.4 |
| Progressive up-sampling | 85.1 |
| Multi-scale fusion | 84.5 |

## Comparison of model performance with different network backbones.

| Backbone | Dice [%] |
| --- | --- |
| ViT B | 82.5 |
| ViT L | 84.1 |
| ViT H | 85.1 |

## Comparison of model performance with different position of 3D adapters.

| Position | Dice [%] |
| --- | --- |
| Before MHSA | 86.7 |
| After MHSA | 86.8 |
| Before & after MHSA | 87.2 |

## Ablation on each key component in our method. The markers • and • denote whether a specific component is used or not.

| SAM weights Full FT | FacT 3D Adapters Dice [%] ↑ |
| --- | --- |

### Formule


$$∆W j,k = s • r t 1 =1 r t 2 =1 Σ t 1 ,t 2 U j,t 1 V k,t 2 ,(1)$$

### Formule


$$W q/v = W 0 + s • UΣ q/v V T ,(2)$$

### Formule


$$3DAdapter(M) = M+σ(Conv3D(Norm(M)•W down ))W up , (3)$$

### Formule


$$x = {x i-N-1 2 , ..., x i , ..., x i+ N-1 2 } B i=1 , x ∈ R B×N×H×W .$$

### Formule


$$• • • • 72.2 • • • • 70.4 • • • • 85.3 • • • • 85.1 • • • • 86.4 • • • • 87.2$$
