# CervSpineNet: a hybrid deep learning-based approach for the segmentation of cervical spinous processes.

**Auteurs** : Sawant JS, Moukheiber L, Nair A, Mahajan A, Byun J, Pichaimani I, Yoon ST, Martin CT, Mitchell CS.
**Année** : 2025
**DOI** : 10.3389/fbioe.2025.1733689

## Résumé

<h4>Introduction</h4>Accurate segmentation of cervical spinous processes on lateral X-rays is essential for reliable anatomical landmarking, surgical planning, and longitudinal assessment of spinal deformity. However, no publicly available dataset provides pixel-level annotations of these structures, and manual delineation remains time-consuming and operator dependent. To address this gap, we curated an expert-labeled dataset of 500 cervical spine radiographs and developed CervSpineNet, a hybrid deep learning framework for automated spinous process segmentation.<h4>Methods</h4>CervSpineNet integrates a transformer-based encoder to capture global anatomical context with a lightweight convolutional decoder to refine local boundaries. Training used a compound loss function that combines Dice, Focal Tversky, Hausdorff distance transform, and Structural Similarity (SSIM) terms to jointly optimize region overlap, class balance, structural fidelity, and boundary accuracy. The model was traine

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Quantitative evaluation of segmentation models on the original dataset.

| Models | Dice | IoU | SSIM | HD95 | VS |
| --- | --- | --- | --- | --- | --- |
| SAM | 0.8553 | 0.7532 | 0.9752 | 25.744 | 0.9132 |
| U-net | 0.9013 | 0.8226 | 0.969 | 3.1296 | 0.9726 |
| Text-guided SegFormer | 0.9266 | 0.8641 | 0.9778 | 4.2251 | 0.9819 |
| DeepLabV3+ | 0.9287 | 0.8676 | 0.9781 | 4.0418 | 0.9831 |
| CervSpineNet | 0.9315 | 0.8726 | 0.9831 | 3.3549 | 0.9818 |
| Mean Dice, IoU, SSIM, HD95, and Volumetric Similarity (VS) scores are reported on the held-out test set (n = 100). CervSpineNet achieved the highest Dice and SSIM, indicating strong overlap |
| and structural fidelity, while maintaining the lowest HD95 (better boundary accuracy). |  |  |  |
| Across all tables, numeric values in bold font indicate the best mean score yielded |  |  |  |  |
| TABLE 2 Quantitative evaluation on the CLAHE-enhanced dataset. |  |  |  |  |
| Models | Dice | IoU | SSIM | HD95 | VS |
| SAM | 0.8246 | 0.7103 | 0.9733 | 27.555 | 0.8929 |
| U-net | 0.9033 | 0.8268 | 0.9707 | 3.4191 | 0.9598 |
| Text-guided SegFormer | 0.9250 | 0.8614 | 0.9776 | 4.2898 | 0.9778 |
| DeepLabV3+ | 0.9260 | 0.8631 | 0.9778 | 4.7765 | 0.9806 |
| CervSpineNet | 0.9313 | 0.8722 | 0.9829 | 2.6561 | 0.9777 |

## Quantitative evaluation on the augmented dataset.Results of all segmentation models after data augmentation with rotations and translations. CervSpineNet again produced the best or near-best mean scores across all metrics, confirming generalization under data diversity. Across all tables, numeric values in bold font indicate the best mean score yielded

| Models | Dice | IoU | SSIM | HD95 | VS |
| --- | --- | --- | --- | --- | --- |
| SAM | 0.7955 | 0.6698 | 0.9722 | 28.8584 | 0.8435 |
| U-net | 0.9099 | 0.8367 | 0.9712 | 3.0973 | 0.9721 |
| Text-guided SegFormer | 0.9289 | 0.8679 | 0.9781 | 4.0540 | 0.9820 |
| DeepLabV3+ | 0.9303 | 0.8704 | 0.9784 | 3.7779 | 0.9838 |
| CervSpineNet | 0.9326 | 0.8744 | 0.9832 | 2.3806 | 0.9833 |

## Architectural Ablation Experiments and the metrics yielded: This table follows a similar structure as Tables 1-3 and demonstrates a comparison between different ablation experiments done with the hybrid model architecture utilizing the same metrics as used previously. Across all tables, numeric values in bold font indicate the best mean score yielded TABLE 5 Loss Ablation Experiments and the metrics yielded: different combinations of loss functions and their results. FT indicates Focal Tversky Loss; SSIM is Structural Similarity Index Loss; HD95 represents 95th percentile of Hausdorff Distance Loss. Across all tables, numeric values in bold font indicate the best mean score yielded

| Experiment | Dice | IoU | SSIM | HD95 | VS |
| --- | --- | --- | --- | --- | --- |
| Pure CNN + basic decoder | 0.8516 | 0.7616 | 0.9828 | 33.9749 | 0.9222 |
| Pure CNN + full decoder | 0.8852 | 0.8021 | 0.9849 | 20.175 | 0.9534 |
| ViT-b encoder + basic decoder | 0.9307 | 0.8713 | 0.9886 | 8.8335 | 0.9804 |
| ViT-b encoder + full decoder (CervSpineNet) | 0.9315 | 0.8726 | 0.9831 | 3.3549 | 0.9818 |
| Experiment | Dice | IoU | SSIM | HD95 | VS |
| Dice | 0.9153 | 0.8457 | 0.9815 | 5.8591 | 0.9694 |
| Dice + FT | 0.9288 | 0.868 | 0.9826 | 3.9504 | 0.9743 |
| Dice + SSIM | 0.931 | 0.8719 | 0.9832 | 3.8787 | 0.9812 |
| Dice + FT + SSIM | 0.9286 | 0.868 | 0.9829 | 5.0694 | 0.979 |
| Dice + FT + SSIM + HD95 (CervSpineNet) | 0.9315 | 0.8726 | 0.9831 | 3.3549 | 0.9818 |

### Formule


$$F enc � ViT SAM x ( ) ∈ R 256×64×64 (1)$$

### Formule


$$F O � ϕ K*F + b ( )(2)$$

### Formule


$$F ( ) � F + ϕ K2*ϕ K1*F + b1 ( ) + b2 􏼁(3)$$

### Formule


$$z c � 1 hw 􏽘 i,j F c,i,j(4)$$

### Formule


$$s � σ W2ϕ W1z ( ) 􏼁(5)$$

### Formule


$$SE F ( ) c,i,j � s c × F c,i,j(6)$$

### Formule


$$F ⊖ � Upsample ×2 F ( ) ∈ R C× 2h ( )× 2w ( )(7)$$

### Formule


$$Loss dice ŷ, y 􏼁 � 1 - 2􏽐 i∈Ω ŷi y i + ε 􏽐 i∈Ω ŷi + 􏽐 i∈Ω y i + ε (8)$$

### Formule


$$TP � 􏽘 i∈Ω ŷi y i , FP � 􏽘 i∈Ω ŷi 1 -y i 􏼁, FN � 􏽘 i∈Ω 1 -ŷi 􏼁y i (9)$$

### Formule


$$T ŷ, y 􏼁 � TP + ε TP + αFN + βFP + ε (10)$$

### Formule


$$Loss FocalTversky ŷ, y 􏼁 � 1 -T ŷ, y 􏼁 􏼁 γ (11)$$

### Formule


$$Loss HausdorffDT ŷ, y 􏼁 � 1 N 􏽘 i∈Ω 􏼌 􏼌 􏼌 􏼌 􏼌 D y,i -D y,i 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 (12)$$

### Formule


$$Loss SSIM ŷ, y 􏼁 � 1 -SSIM ŷ, y 􏼁(13)$$

### Formule


$$Loss Total � 0.5 × Loss Dice ŷ, y 􏼁 􏼂 􏼃 + 0.3 × Loss FocalTversky ŷ, y 􏼁 􏽨 􏽩 + 0.1 × Loss HausdorffDT ŷ, y 􏼁 􏽨 􏽩 + 0.1 × Loss SSIM ŷ, y 􏼁 􏼂 􏼃(14)$$

### Formule


$$Dice � 2 • TP 2 • TP + FP + FN (15) IoU � TP TP + FP + FN (16) VS � 1 - TP + FP ( ) -TP + FN ( ) | | TP + FP ( ) + TP + FN ( ) | |(17)$$

### Formule


$$SSIM x, y 􏼁 � 2μ x μ y + C1 􏼐 􏼑 2σ xy + C2 􏼐 􏼑 μ 2 x + μ 2 y + C1 􏼐 􏼑 σ 2 x + σ 2 y + C2 􏼐 􏼑(18)$$

### Formule


$$D A, B ( ) � min b∈B d a, b ( ) 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 a ∈ A 􏼚 􏼛, D B, A ( ) � min a∈A d b, a ( ) 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 b ∈ B 􏼚 􏼛(19)$$

### Formule


$$HD95 A, B ( ) � percentile 95 S ( )(20)$$
