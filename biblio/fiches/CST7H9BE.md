# ProtoSAM for automated one shot medical image segmentation using foundational models.

**Auteurs** : Lev Ayzenberg, Raja Giryes, Hayit Greenspan
**Année** : 2025
**DOI** : 10.1038/s41598-025-06643-0

## Résumé

This work presents an advance in one-shot medical image segmentation, where a single image-label sample from a new site is used for finetuning the solution - particularly valuable in scenarios where labeled data is scarce or rapid adaptation to new classes and sites is required. We introduce ProtoSAM, a novel, fully automated framework, for one-shot medical image segmentation that combines Prototypical networks, known for few-shot segmentation, with the Segment Anything Model (SAM), a natural image foundation model for segmentation. The proposed method creates an initial coarse segmentation mask using the ALPnet prototypical network, augmented with a DINOv2 encoder. Following the extraction of an initial mask, prompts are extracted, such as points and bounding boxes, which are then input into SAM. We present extensive validation on multiple datasets including CT, MRI, and endoscopy images, demonstrating state-of-the-art results in many scenarios. Our results show that an untrained Prot

## Méthodologie

{'study_design': "Approche de segmentation 2D coupe par coupe (slice-by-slice), même pour les données volumétriques (CT, IRM), car ProtoSAM s'appuie sur des modèles fondationnels (SAM, DINOv2) conçus pour des images 2D", 'intervention': None, 'control': 'Comparaison avec nnU-Net utilisé dans sa configuration 2D (nnU-Net 2D) pour assurer une base de comparaison équitable', 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Conclusions

ProtoSAM is a novel automatic framework for one-shot image segmentation that achieves competitive performance across various organs and modalities, often surpassing previous SSL pre-trained methods Encoder finetuning further boosts performance, enabling ProtoSAM to outperform all previous one-shot methods ProtoSAM generates segmentation masks using only a single annotated support image, unlike SAM which requires manual prompts for each new image or manual selection among multiple candidate masks ProtoSAM outperforms SAM in specific anatomical regions, particularly on MRI data where SAM shows a notable performance drop, and demonstrates more consistent performance across both CT and MRI modalities EFT-SP (using superpixels) substantially improved results for CT and MRI datasets but provided only minor benefits for polyp segmentation, while EFT-SAM delivered more significant improvements for polyp segmentation with comparable gains on CT and MRI SAM shows potential as a self-supervised learning (SSL) tool, generating high-quality pseudo-labels that can enhance segmentation performance without requiring manual annotations ProtoSAM presents a promising, novel and generalizable approach to one-shot image segmentation in medical imaging, with potential applications where labeled data is scarce or rapid adaptation to new classes is required

## Distribution

| Modality | Label Number of Slices Resolution |
| --- | --- | --- | --- |
|  | Liver | 583 | 256 × 256 |
| MRI | RK LK | 356 373 | 256 × 256 256 × 256 |
|  | Spleen 347 | 256 × 256 |
|  | Spleen 1010 | 512 × 512 |
| CT | RK LK | 1047 1061 | 512 × 512 512 × 512 |
|  | Liver | 1805 | 512 × 512 |
| Endoscopy Polyps 738 | varies |

## MRI

|  |  | LK | RK | Spleen | Liver | Mean |
| --- | --- | --- | --- | --- | --- | --- |
| Method | SSL MRI / CT | MRI / CT | MRI / CT | MRI / CT | MRI / CT |
| Few-Shot |  |  |  |  |  |  |
| SSL-ALPNet 9 | ✓ | 73.63±4.60 / 63.34±9.33 | 78.39±5.51 / 54.82±11.7 | 67.02±7.98 / 60.25±6.67 | 73.05±3.49 / 73.65±3.61 73.02±6.01 / 63.02±7.97 |
| SSL-ALPNet+BP 10 | ✓ | 78.77 / 66.04 | 83.44 / 62.14 | 70.02 / 68.39 | 75.01 / 73.90 | 76.81 / 67.62 |
| CRAP-Net 11 | ✓ | 74.66 / 70.91 | 82.77 / 67.33 | 73.82 / 70.17 | 70.82 / 70.45 | 73.82 / 69.72 |
| CRTPNet 12 | ✓ | 76.74 / 66.37 | 80.15 / 61.05 | 70.07 / 67.92 | 73.36 / 73.88 | 75.08 / 67.31 |
| SSL-DINOv2 13 | ✓ | 75.06±11.61 / 69.96±11.61 80.21±2.14 / 66.40±12.99 71.86±10.30 / 73.00±6.49 73.50±5.95 / 76.40±3.89 75.16±2.14 / 71.44±6.49 |
| SSL-DINOv2+CCA 13 ✓ | 81.43±13.84 / 66.40±13.84 84.40±4.07 / 69.96±13.65 73.30±10.27 / 74.60±6.58 74.20±5.46 / 81.67±4.41 78.43±4.07 / 73.16±6.58 |
| PerSAM 33 | ✗ | 35.72 / 23.89 | 40.27 / 25.85 | 41.53 / 22.31 | 14.96 / 25.98 | 33.12 / 24.51 |
| PerSAM-modified | ✗ | 53.76±7.41 / 45.05±11.48 62.30±6.33/43.29±12.13 | 68.65±10.46 / 57.36±10.27 64.38±10.66 / 80.75±1.56 62.27±6.26 / 56.61±17.27 |
| AutoSAM 17 | ✗ | 61.07 / 43.20 | 64.46 / 38.77 | 69.03 / 54.50 | 68.10 / 70.68 | 65.66 / 51.79 |
| ProtoMedSAM | ✗ | 69.97±4.97 / 66.08±9.45 | 77.16±3.92 / 67.15±6.01 | 69.68±8.38 / 60.53±2.94 | 71.99±6.12 / 78.64±3.03 72.20±4.44 / 68.10±4.44 |
| ProtoSAM-base | ✗ | 70.47±3.93 / 67.54±8.33 | 79.03±3.06 / 64.52±7.85 | 69.56±7.87 / 57.99±3.40 | 69.88±4.89 / 77.56±2.50 72.23±3.93 / 66.90±8.33 |
| ProtoSAM | ✗ | 73.11±3.98 / 70.63±12.04 86.27±3.29 / 71.59±10.27 82.46±6.41 / 68.97±5.20 | 81.36±5.68 / 86.21±6.22 80.80±5.54 / 74.55±7.98 |
| ProtoSAM+EFT-SP | ✓ | 87.16±1.60 / 75.72±16.69 89.23±2.11 / 71.33±15.96 80.28±8.02 / 83.05±3.24 | 79.07±4.35 / 86.33± 4.21 83.94±5.01 / 79.11±6.82 |
| ProtoSAM+EFT-SAM ✓ | 86.15±1.43 / 73.88±24.30 90.02±2.68 / 70.64±15.22 82.76±7.06 / 84.33±4.91 | 77.54±3.77 / 87.63±2.97 84.12±5.29 / 79.12±8.14 |
| Requires User Interaction |  |  |  |  |  |
| SAM (best mask) 4 | ✗ | 77.32±4.54 / 85.21±3.29 | 80.75±3.85 / 85.36±2.63 66.37±4.25 / 76.56±4.44 | 27.61±6.61 / 69.58±1.39 63.01±1.39 / 79.18±3.29 |
| Supervised |  |  |  |  |  |  |
| nnUNET-2D 37 |  | 92.50±0.22 / 83.92±2.54 | 93.15±1.53 / 81.47±8.29 | 86.25±9.30 / 90.65±4.66 | 89.34±10.43 / 93.98±4.00 90.31±7.04 / 87.50±6.94 |
| SWIN UNETR 34 |  | -/ 95.6 | -/ 95.8 | -/ 97.6 | -/ 98.5 | -/ 96.88 |
| MS-Dual-Guided 38 |  | 88.01±6.16/ - | 87.96±6.46 / - | 78.61±18.69 / - | 92.46±2.82 / - | 86.75±5.05 / - |

## Wilcoxon rank test.

|  | Kvasir33 28 | Clinic 29 | Colon 30 | ETIS 31 |  | All |
| --- | --- | --- | --- | --- | --- | --- |
| Method | Dice IoU | Dice IoU | Dice IoU | Dice | IoU | Dice IoU |
| Few-Shot |  |  |  |  |  |  |
| AutoSAM 17 1-shot | 35.64 25.18 20.31 14.12 10.34 6.29 | 13.97 9.00 | 15.57 10.23 |
| AutoSAM 17 5-shot | 59.56 48.14 38.90 29.34 35.60 25.75 26.57 19.53 36.72 33.33 |
| AutoSAM 17 100-shot | 73.44 62.51 62.64 52.26 53.27 43.24 38.52 29.94 52.87 43.08 |
| PerSAM(modified) 33 | 65.58 56.70 53.70 47.42 48.19 42.53 24.79 21.51 44.79 39.28 |
| ProtoMedSAM (1-shot) | 81.11 72.75 66.54 57.31 64.34 55.61 59.899 51.66 65.62 57.02 |
| ProtoSAM-base (1-shot) | 79.98 71.12 65.79 56.12 65.48 57.11 63.07 55.50 66.83 58.50 |
| ProtoSAM (1-shot) | 81.55 73.66 69.01 60.80 67.31 59.60 62.33 55.47 68.06 60.49 |
| ProtoSAM (1-shot) + EFT-SP | 78.21 69.83 73.39 65.66 69.97 61.84 61.54 55.06 69.13 61.44 |
| ProtoSAM (1-shot) + EFT-SAM 81.10 72.48 69.94 62.16 71.57 64.28 65.87 58.85 71.21 63.77 |
| Requires User Interaction |  |  |  |  |  |  |
| SAM (best mask) 4 | 77.91 69.28 57.23 50.66 46.08 39.73 52.32 47.42 59.94 53.98 |
| Supervised |  |  |  |  |  |  |
| AutoSAM 17 | 91.00 87.00 92.80 89.33 83.00 76.70 79.70 74.00 86.25 81.75 |

## Polyp segmentation benchmarks results.

|  | LK | RK | Spleen | Liver | Mean | Polyp |
| --- | --- | --- | --- | --- | --- | --- |
| Method | MRI / CT | MRI / CT | MRI / CT | MRI / CT | MRI / CT | Endoscopy |
| Few-Shot |  |  |  |  |  |  |
| ProtoSAM | 111.38±93.93 / 163.34±76.12 | 50.92±85.57 / 100.96±77.30 38.84±51.44 / 134.23±93.33 | 27.03±38.41 / 21.64±23.40 | 57.04±67.34 / 105.04±67.54 | 92.21 |
| ProtoSAM+EFT-SP | 27.78±31.51 / 43.47±47.09 18.40±30.69 / 38.94±42.45 31.90±36.00 / 45.41±39.27 | 43.21±42.55 / 17.76±14.03 | 30.32±35.18 / 36.39±35.71 | 87.07 |
| ProtoSAM+EFT-SAM | 30.12±41.11 / 61.33±56.45 33.25±68.52 / 66.91±61.46 15.99±18.21 / 66.63±51.74 | 28.86±33.70 / 15.94±14.20 | 27.05±40.91 / 52.70±46.36 | 90.61 |

## .99 ± 11.51 69.31 ± 12.39 64.86 ± 12.11 74.86 ± 6.49 62.26 ± 4.91 51.32 ± 10.12 78.97 ± 3.96 64.27 ± 8.98 67.02 ± 8.12 65.04 .70 61.33 ± 10.01 68.27 ± 12.41 62.27 ± 10.83 73.25 ± 7.35 60.07 ± 6.23 68.03 ± 4.86 82.55 ± 4.14 67.30 ± 7.33 66.56 ± 7.80 66.26 .98 67.25 ± 8.97 86.82 ± 2.75 69.36 ± 8.99 81.63 ± 5.94 66.97 ± 7.31 79.39 ± 5.99 82.32 ± 9.46 80.03 ± 5.16 71.48 ± 8.68 65.50 .40 69.15 ± 12.10 86.19 ± 2.94 69.19 ± 10.15 78.89 ± 7.85 59.38 ± 8.67 81.60 ± 5.34 85.32 ± 6.95 79.52 ± 5.38 70.76 ± 9.47 68.08 .98 70.63 ± 12.05 86.27 ± 3.29 71.59 ± 10.28 82.46 ± 6.41 68.97 ± 5.20 81.36 ± 5.68 86.21 ± 6.22 80.80 ± 4.84 74.35 ± 8.44 67.84 .72 70.44 ± 12.28 86.22 ± 3.16 70.29 ± 10.34 80.48 ± 7.41 65.79 ± 6.00 82.04 ± 4.86 86.32 ± 6.04 80.06 ± 5.04 73.21 ± 8.66 68.57 .42 70.51 ± 12.15 85.75 ± 3.40 70.58 ± 10.60 81.21 ± 7.01 65.27 ± 6.01 81.70 ± 5.01 86.45 ± 5.59 79.99 ± 4.96 73.20 ± 8.59 68.52 73.90 ± 6.77

| 48.93 ± 5.04 51.95 ± 11.12 56.84 ± 6.38 54.09 ± 5.68 62.32 ± 12.00 49.16 ± 9.46 62.59 ± 1.79 78.04 ± 5.92 57.67 ± 6.30 58.31 ± 8.05 58.70 58.23 ± 7.17 | 61.60 ± 6.91 6165.44 ± 8.55 | 59.64 ± 466.71 ± 7.57 | 72.31 ± 572.34 ± 6.92 | 71.40 ± 572.79 ± 7.43 | 73.11 ± 374.33 ± 6.64 | 71.51 ± 473.95 ± 6.85 | 71.29 ± 4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
| ✗ | ✓ | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ |
| ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ |

### Formule


$$P (m, n; c) = 1 LH LW ∑ h ∑ w f θ (x s (c))[h, w](1)$$

### Formule


$$P g (c) = ∑ h,w y s (c)[h, w]f θ (x s (c))[h, w] ∑ h,w y s (c)[h, w](2)$$

### Formule


$$S l (c j )(h, w) = α • P l (c) ⊙ f θ (x q )[h, w](3)$$

### Formule


$$S ′ (c)(h, w) = ∑ l S l (c)[h, w] • softmax l [S l (c)[h, w]](4)$$

### Formule


$$ŷq (h, w) = softmax c [S ′ (c)[h, w]](5)$$

### Formule


$$Confidence = ∑ i pi • ŷi ∑ i ŷi (6$$

### Formule


$$)$$

### Formule


$$L i seg (θ; S, Q) = - 1 HW H ∑ h=1 W ∑ w=1 ∑ c∈{c 0 ,c p } Tg(y r (c))[h, w] log(ŷ r (c)[h, w])(7)$$

### Formule


$$Lreg(θ; S ′ , S) = - 1 HW H ∑ h=1 W ∑ w=1 ∑ c∈{c 0 ,c p } y r (c)[h, w] log(ȳ r (c)[h, w]) (8$$

### Formule


$$)$$

### Formule


$$Dice = 2 • |A ∩ B| |A| + |B| (9)$$

### Formule


$$IoU = |A ∩ B| |A ∪ B| (10)$$

### Formule


$$HD95(X, Y ) = max(h95(X, Y ), h95(Y, X)) (11$$

### Formule


$$)$$

### Formule


$$h95(X, Y ) = P95 x∈X (min y∈Y ∥x -y∥) (12$$

### Formule


$$)$$
