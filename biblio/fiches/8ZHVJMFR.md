# MedCLIP-SAMv2: Towards universal text-driven medical image segmentation.

**Auteurs** : Taha Koleilat, Hojat Asgariandehkordi, Hassan Rivaz, Yiming Xiao
**Année** : 2025
**DOI** : 10.1016/j.media.2025.103749

## Résumé

Segmentation of anatomical structures and pathologies in medical images is essential for modern disease diagnosis, clinical research, and treatment planning. While significant advancements have been made in deep learning-based segmentation techniques, many of these methods still suffer from limitations in data efficiency, generalizability, and interactivity. As a result, developing robust segmentation methods that require fewer labeled datasets remains a critical challenge in medical image analysis. Recently, the introduction of foundation models like CLIP and Segment-Anything-Model (SAM), with robust cross-domain representations, has paved the way for interactive and universal image segmentation. However, further exploration of these models for data-efficient segmentation in medical imaging is an active field of research. In this paper, we introduce MedCLIP-SAMv2, a novel framework that integrates the CLIP and SAM models to perform segmentation on clinical scans using text prompts, in

## Méthodologie

{'study_design': "Framework MedCLIP-SAMv2 combinant fine-tuning de BiomedCLIP (avec perte DHN-NCE) et génération de prompts visuels via Multi-modal Information Bottleneck (M2IB) pour produire des masques de segmentation avec SAM, en zero-shot puis en supervision faible (entraînement de nnUNet sur pseudo-labels avec estimation d'incertitude par checkpoint ensembling)", 'intervention': 'Utilisation de prompts textuels avec BiomedCLIP fine-tuné pour générer des cartes de saillance (comparaison M2IB, gScoreCAM, GradCAM) transformées en prompts visuels (bounding box et/ou points) pour SAM, avec comparaison de différents backbones SAM (SAM, MedSAM, SAM-Med2D)', 'control': None, 'primary_outcomes': ['Score Dice (DSC) de segmentation', 'Normalized Surface Distance (NSD)'], 'secondary_outcomes': ["Estimation de l'incertitude via checkpoint ensembling"], 'statistical_methods': ['Comparaison statistique entre techniques de cartes de saillance (p < 0.05)'], 'duration': None, 'setting': "Validation sur quatre tâches/modalités d'imagerie médicale: segmentation de tumeur du sein en échographie, tumeur cérébrale en IRM, poumon en radiographie thoracique et poumon en CT"}

## Résultats

{'quantitative': [], 'qualitative_findings': ['MedCLIP-SAMv2 consistently produced high-quality segmentation masks in weakly supervised settings across all four imaging modalities.', 'For all datasets except Brain MRI, the initial coarse segmentation was suboptimal, but provided a sufficient starting point for the zero-shot approach to refine coarse activation maps.', 'For breast and brain tumors, the zero-shot results were notably better than those for Lung CT and Lung X-ray.', 'In Lung CT, the primary challenge for the algorithm was distinguishing between the two lobes.', 'The post-processed results for Lung CT showed one large, connected contour in the center.', 'Zero-shot refinement slightly separated the two lung lobe regions, though some artifacts persisted.', 'Weakly supervised training effectively corrected false activations in Lung CT, producing a high-quality segmentation map.', 'For Lung X-ray, weakly supervised training improved upon the less precise zero-shot masks, but the improvement was not as substantial as with Lung CT.', 'For Brain MRI, high uncertainty was observed only at the edges of the segmentation, which is typical.', 'For Breast Ultrasound, high uncertainty was observed at the borders of the segmentation, while the surrounding area outside the borders showed low uncertainty.', 'For Lung X-rays, slight uncertainty appeared in the center of the mask, increasing towards the edges.', 'For Lung CT, high uncertainty was observed both at the edges and in the center of the lung lobes, largely due to artifacts present in the zero-shot pseudo-labels.'], 'main_findings': ['MedCLIP-SAMv2 produces high-quality weakly supervised segmentation masks across four imaging modalities (Brain MRI, Breast Ultrasound, Lung CT, Lung X-ray).', 'Zero-shot refinement improves coarse activation maps, with performance varying by modality (better for breast and brain tumors than for Lung CT and Lung X-ray).', 'Weakly supervised training corrects false activations and artifacts remaining after zero-shot refinement, particularly notable in Lung CT.', 'Uncertainty map patterns differ by modality, generally concentrated at segmentation borders except in Lung CT where artifacts cause additional central uncertainty.']}

## Conclusions

MedCLIP-SAMv2 demonstrates superior performance in zero-shot and weakly supervised medical image segmentation compared to SOTA methods and the original MedCLIP-SAM across CT, MRI, Ultrasound, and X-ray modalities The integration of M2IB effectively extracts meaningful information from medical images and texts, enhancing segmentation performance The introduction of the DHN-NCE loss played a crucial role in fine-tuning BiomedCLIP, enabling the model to focus on challenging details while maintaining high performance across all tasks and modalities The combination of M2IB and DHN-NCE allowed the model to generate coarse segmentation masks that are later refined via SAM in a zero-shot setting without the need for ground truth annotations Contextually rich, descriptive prompts yielded better results in complex tasks like tumor segmentation, while more generic prompts sufficed for simpler tasks like lung segmentation BiomedCLIP learns to encode meaningful latent representations of salient regions within medical scans from natural language supervision, outperforming CLIP in highlighting disease-relevant regions Operating in a weakly supervised paradigm using pseudo-labels from zero-shot segmentation to finetune the model produced notable improvements, particularly in lung CT segmentation The integration of uncertainty estimation through nnUNet with checkpoint ensembling provides a robust method for enhancing segmentation quality while offering insights into prediction confidence SAM showed strong performance in zero-shot settings even without medical pre-training, outperforming MedSAM and SAM-Med2D when provided with imperfect visual prompts MedCLIP-SAMv2 outperforms its predecessor through superior generalization and refined segmentation, demonstrating strong potential for clinical use in data-limited environments

## .12 48.62 10.25 47.96 9.14 50.24 9.2663.14 11.34  66.44 11.58  76.32 11.22  78.46 11.35  57.94  10.49 60.94 10.65 SAMAug 56.39 10.85 59.23 10.92 45.71 10.34 48.81 11.29 57.18 12.12 60.08 12.34 44.61 10.42 46.48 10.57 50.97 10.96 53.65 11.30 .87 58.80 8.63 61.77 8.64 86.07 8.61 88.65 8.09 80.12 8.38 83.73 8.29 70.90 7.92 73.77 7.80 Ours 78.87 12.29 84.58 12.19 80.03 9.91 88.25 10.04 80.77 4.44 84.53 4.51 88.78 4.43 91.95 4.06 82.11 8.49 87.33 8.46 .71 53.82 10.17 66.40 9.96 79.25 2.10 84.80 1.70 65.68 12.02 70.56 11.67 61.58 9.02 69.00 8.86 Self-Prompt-SAM 42.04 17.19 44.30 17.64 46.43 15.25 50.29 15.83 67.97 2.89 71.63 2.83 81.50 3.84 83.40 3.77 59.49 11.74 62.41 12.08 .30 62.82 7.97 72.76 7.94 83.44 1.54 87.73 1.24 86.49 2.49 89.96 1.94 74.78 6.03 80.67 5.86 Self-Prompt-SAM 62.36 16.38 66.01 16.92 52.55 15.29 57.07 15.93 82.49 2.50 86.49 2.45 83.66 3.90 85.49 3.84 70.27 11.44 73.77 11.84 Fully Supervised nnUNet 82.47 10.49 88.32 10.77 87.74 6.28 95.10 6.28 98.72 0.65 99.51 0.41 97.10 2.74 99.18 2.13 84.63 6.27 90.42 6.33 nnUNet Ensemble 84.72 10.97 90.85 11.26 88.82 5.93 95.84 5.54 99.14 2.50 99.82 1.93 98.12 4.09 99.65 4.03 85.43 6.68 91.74 6.66 Comparison of DSC and NSD values (%) with different few-shot and zero-shot medical image segmentation methods (mean std )

| Technique | Method | Breast Ultrasound | Brain MRI | Lung X-ray | Lung CT | All |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | DSC ↑ | NSD ↑ | DSC ↑ | NSD ↑ | DSC ↑ | NSD ↑ | DSC ↑ | NSD ↑ | DSC ↑ | NSD ↑ |
| Zero-shot | SaLIP 44.33 10MedCLIP-SAM 67.82 8.26 | 69.12 9.12 66.72 5.27 68.01 6.16 64.49 9.09 65.89 10.44 59.14 9.52 60.47 9.98 64.54 8.20 66.10 9.08 |
|  | Ours | 77.76 9.52 | 81.11 9.89 76.52 7.06 82.23 7.13 | 75.79 3.44 80.88 3.52 80.38 5.81 82.03 5.94 77.61 6.82 81.56 7.00 |
| Weakly Supervised | nnUNet | 73.77 14.48 79.71 14.79 77.16 12.17 85.21 12.60 70.15 6.40 74.10 6.59 82.24 5.12 85.65 4.70 75.83 10.31 81.17 10.52 |
| MedCLIP-SAM 60.94 5One-shot 58.62 5.66 UniverSeg 40.56 5.14 53.25 6.22 23.81 5.45 35.28 6.49 68.15 2.21 80.09 2.16 54.94 8.21 69.62 7.59 46.87 5.67 59.56 5.98 |
|  | ProtoSAM | 48.44 10.93 50.24 10.84 45.68 15.14 51.69 15.65 80.75 1.40 85.11 1.30 84.50 9.94 87.62 9.72 64.84 10.60 68.67 10.71 |
| Few-shot (K = 4) 54.25 8Few-shot (K = 16) UniverSeg 47.56 8.57 UniverSeg 66.36 8.57 72.22 8Model | Version |  | image → text (%) | text → image (%) |
|  |  |  |  |  |  |  | Top-1 |  | Top-2 | Top-1 | Top-2 |
| CLIP (Radford et al., 2021) |  | Pre-trained |  | 26.68 0.30 | 41.80 0.19 | 26.17 0.20 | 41.13 0.20 |
| PMC-CLIP (Lin et al., 2023a) |  | Pre-trained |  | 75.47 0.37 | 87.46 0.11 | 76.78 0.11 | 88.35 0.19 |
|  |  |  | Pre-trained |  | 81.83 0.20 | 92.79 0.13 | 81.36 0.48 | 92.27 0.14 |
|  |  | InfoNCE (Oord et al., 2018) | 84.21 0.35 | 94.47 0.19 | 85.73 0.19 | 94.99 0.16 |
| BiomedCLIP (Zhang et al., 2023) |  | DCL (Yeh et al., 2022) |  | 84.44 0.37 | 94.68 0.19 | 85.89 0.16 | 95.09 0.19 |
|  |  | HN-NCE (Radenovic et al., 2023) | 84.33 0.35 | 94.60 0.19 | 85.80 0.17 | 95.10 0.19 |
|  |  |  | DHN-NCE (ours) |  | 84.70 0.33 | 94.73 0.16 | 85.99 0.19 | 95.17 0.19 |

## Finally, weakly supervised training with

| Prompt | Breast Ultrasound | Brain MRI | Lung X-ray | Lung CT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | DSC ↑ | NSD ↑ | DSC ↑ | NSD ↑ | DSC ↑ | NSD ↑ | DSC ↑ | NSD ↑ |
| P0 | 63.79 15.12 | 67.89 15.08 | 70.98 7.61 | 76.42 7.63 | 75.79 3.44 | 80.88 3.52 | 69.89 5.14 | 71.83 4.98 |
| P1 | 67.66 14.35 | 71.56 14.78 | 37.19 10.98 | 39.77 11.63 | 69.72 4.65 | 73.52 4.83 | - | - |
| P2 | 69.04 12.45 | 73.33 12.97 | 71.18 7.16 | 77.19 7.14 | 63.91 4.73 | 67.63 5.13 | 80.38 5.81 | 82.03 5.94 |
| P3 | 77.76 9.52 | 81.11 9.89 | 76.52 7.06 | 82.23 7.13 | 63.92 4.88 | 67.73 4.96 | - | - |
| P4 | 67.65 16.54 | 71.02 16.89 | 69.23 8.41 | 74.32 8.59 | 68.95 4.91 | 72.31 4.95 | 75.84 4.88 | 77.56 4.97 |
| P5 | 65.18 17.51 | 68.75 17.93 | 69.81 7.86 | 75.01 7.97 | 68.44 4.63 | 72.09 4.81 | - | - |

## Effect of different components (%, mean std )

| Method |  | DSC↑ | NSD↑ |
| --- | --- | --- | --- |
| 1: Saliency Maps |  | 46.23 8.58 | 50.50 8.86 |
| 2: + DHN-NCE Fine-tuning | 49.10 8.46 | 53.54 8.62 |
| 3: + Post-processing | 51.62 7.57 | 55.23 7.47 |
| 4: + Connected Component Analysis | 57.89 7.87 | 61.54 8.02 |
| 5: + SAM |  | 77.61 6.82 | 81.56 7.00 |
| 6: + nnUNet Ensemble | 82.11 8.49 | 87.33 8.46 |
| Model | Technique | All |  |
|  |  | DSC ↑ | NSD ↑ |
| Pre-trained BiomedCLIP | M2IB gScoreCAM GradCAM | 73.69 7.58 58.92 6.67 29.21 8.74 | 77.32 7.43 62.19 6.02 31.36 8.44 |
| Fine-tuned BiomedCLIP | M2IB gScoreCAM GradCAM | 77.61 6.82 60.52 6.41 30.11 8.92 | 81.56 7.00 63.89 6.39 32.61 8.83 |

## Points 65.56 9.89 68.20 9.97 65.54 8.45 70.73 8.32 75.79 3.44 80.88 3.52 61.49 6.25 63.90 6.74 BBoxes 77.76 9.52 81.11 9.89 76.52 7.06 82.23 7.12 70.55 5.38 74.12 5.77 80.38 5.81 82.03 5.94 Points + BBoxes 74.38 10.57 79.60 10.62 75.48 8.66 80.29 8.64 73.30 5.94 79.22 6.12 62.83 6.72 64.57 6.99 SAM-Med2D ViT-B Points 73.12 9.51 75.16 9.13 66.78 9.97 70.12 9.75 60.58 7.43 64.42 7.73 65.94 7.17 68.05 7.99 BBoxes 75.22 10.04 80.03 10.94 55.21 9.85 61.34 9.93 30.18 11.15 36.35 11.23 63.10 8.57 68.59 8.48 Points + BBoxes 74.83 10.78 79.50 10.12 67.85 10.96 72.04 10.45 37.23 8.69 44.90 9.37 71.22 8.09 78.05 8.11 MedSAM ViT-B BBoxes 63.50 11.42 68.11 11.25 67.68 12.75 73.89 12.67 73.03 6.03 76.23 6.02 62.14 7.80 65.00 7.11

| Model | Type | Prompts | Breast Ultrasound | Brain MRI | Lung X-ray | Lung CT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | DSC ↑ | NSD ↑ | DSC ↑ | NSD ↑ | DSC ↑ | NSD ↑ | DSC ↑ | NSD ↑ |
| SAM | ViT-H |  |  |  |  |  |  |

### Formule


$$L InfoNCE = - B i=1 log exp(z ⊤ i z + i /τ) B j=1 exp(z ⊤ i z j /τ)(1)$$

### Formule


$$L v→t = - B i=1 log exp(I ⊤ p,i T p,i /τ) B j=1 exp(I ⊤ p,i T p, j /τ)(2)$$

### Formule


$$L t→v = - B i=1 log exp(T ⊤ p,i I p,i /τ) B j=1 exp(T ⊤ p,i I p, j /τ)(3)$$

### Formule


$$L v→t = - B i=1         I ⊤ p,i T p,i τ -log B j=1 exp(I ⊤ p,i T p, j /τ)         (4) L t→v = - B i=1         T ⊤ p,i I p,i τ -log B j=1 exp(T ⊤ p,i I p, j /τ)        (5)$$

### Formule


$$B j=1 exp(I ⊤ p,i T p, j /τ) = exp(I ⊤ p,i T p,i /τ) + j i exp(I ⊤ p,i T p, j /τ) (6)$$

### Formule


$$L v→t = - B i=1 I ⊤ p,i T p,i τ + B i=1 log         j i e I ⊤ p,i T p, j /τ         (7) L t→v = - B i=1 T ⊤ p,i I p,i τ + B i=1 log         j i e T ⊤ p,i I p, j /τ         (8)$$

### Formule


$$L v→t = - B i=1 I p,i T ⊤ p,i τ + B i=1 log j i e I p,i T ⊤ p, j /τ W v→t I p,i T p, j(9)$$

### Formule


$$L t→v = - B i=1 T p,i I ⊤ p,i τ + B i=1 log j i e T p,i I ⊤ p, j /τ W t→v T p,i I p, j(10)$$

### Formule


$$L DHN-NCE = L v→t + L t→v (11)$$

### Formule


$$W v→t I p,i T p, j = (B -1) × e β 1 I p,i T p, j /τ k i e β 1 I p,i T p,k /τ (12) W t→v T p,i I p, j = (B -1) × e β 2 T p,i I p, j /τ k i e β 2 T p,i I p,k /τ (13)$$

### Formule


$$Z img = Φ img (I; θ img )(14$$

### Formule


$$Z text = Φ text (T; θ text )(15)$$

### Formule


$$λ S = MI(Z img , Z text ; θ) -γ × MI(Z img , I; θ) (16$$

### Formule


$$)$$

### Formule


$$Y otsu =        1, λ S (x, y) ≥ η * 0, λ S (x, y) < η *(17)$$

### Formule


$$Confidence(c) = i∈c p i • ŷi i∈c ŷi ,(18)$$

### Formule


$$Y coarse = {c ∈ C : Confidence(c) > η c },(19)$$

### Formule


$$Y zero-shot = SAM(Y coarse ; V)(20)$$

### Formule


$$p(Y final |X; T ) ≈ 1 G G n=1 p(Y final |X; M n ) (21$$

### Formule


$$)$$

### Formule


$$H(Y final,(i, j) ) = - R r=1 h(r) log h(r)(22)$$
