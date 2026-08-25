# LVM-Med: Learning Large-Scale Self-Supervised Vision Models for Medical Imaging via Second-order Graph Matching

**Auteurs** : Duy M. H. Nguyen, Hoang Nguyen, Nghiem T. Diep, Tan N. Pham, Tri Cao, Binh T. Nguyen, Paul Swoboda, Nhat Ho, Shadi Albarqouni, Pengtao Xie
**Année** : 2023
**DOI** : 10.48550/arxiv.2306.11925

## Résumé

Obtaining large pre-trained models that can be fine-tuned to new tasks with limited annotated samples has remained an open challenge for medical imaging data. While pre-trained deep networks on ImageNet and vision-language foundation models trained on web-scale data are prevailing approaches, their effectiveness on medical tasks is limited due to the significant domain shift between natural and medical images. To bridge this gap, we introduce LVM-Med, the first family of deep networks trained on large-scale medical datasets. We have collected approximately 1.3 million in medical images from 55 publicly available datasets, covering a large number of organs and modalities such as CT, MRI, X-ray, and Ultrasound. We benchmark several state-of-the-art self-supervised algorithms on this dataset and propose a novel self-supervised contrastive learning algorithm using a graph matching formulation. The proposed approach makes three contributions: (i) it integrates prior pair-wise image similarity metrics based on local and global information; (ii) it captures the structural constraints of feature embeddings through a loss function constructed via a combinatorial graph-matching objective; and (iii) it can be trained efficiently end-to-end using modern gradient-estimation techniques for black-box solvers. We thoroughly evaluate the proposed LVM-Med on 15 downstream medical tasks ranging from segmentation and classification to object detection, and both for the in and out-of-distribution settings. LVM-Med empirically outperforms a number of state-of-the-art supervised, self-supervised, and foundation models. For challenging tasks such as Brain Tumor Classification or Diabetic Retinopathy Grading, LVM-Med improves previous vision-language models trained on 1 billion masks by 6-7% while using only a ResNet-50. We release pre-trained models at this link https://github.com/duyhominhnguyen/LVM-Med.

## Méthodologie

{'study_design': "LVM-Med incorpore une formulation de graph-matching de second ordre qui englobe et étend une large classe de méthodes SSL contrastives. Pour un batch d'images, deux transformations aléatoires sont appliquées à chaque image, puis les images transformées sont passées dans un encodeur d'images. Les vecteurs d'embedding obtenus sont utilisés pour construire deux graphes où les sommets représentent des paires d'images transformées issues de la même image originale ; la résolution d'un problème de graph-matching permet d'apprendre une représentation des caractéristiques servant de prior adapté à une solution globale de l'objectif de graph-matching.", 'intervention': "L'approche proposée (LVM-Med) intègre des métriques de similarité par paires d'images (locales et globales) dans les affinités des sommets, capture les contraintes structurelles des embeddings via une fonction de perte construite à partir d'un objectif combinatoire de graph-matching, et permet un entraînement end-to-end efficace grâce à des techniques modernes d'estimation de gradient (implicit maximum likelihood estimation) pour des solveurs black-box", 'control': "Comparaison avec plusieurs méthodes de l'état de l'art : méthodes SSL supervisées, auto-supervisées (clustering, contrastive, instance-based) et modèles fondation vision-langage (dont SAM, entraîné sur plus d'un milliard de masques annotés)", 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [], 'qualitative_findings': ["L'original SAM (sans fine-tuning) génère souvent des prédictions inutiles ou peu précises", 'SAM avec fine-tuning (encodeurs et réseaux de prompt gelés, seul le décodeur entraîné) et LVM-Med produisent des résultats plus précis que SAM sans fine-tuning', 'SAM (fine-tuning) a tendance à sur-segmenter ou à manquer de structures sur les bords des objets dans plusieurs cas', 'LVM-Med (encodeur avec architecture ViT de SAM) est plus stable que SAM dans les situations de sur-segmentation ou de manque de structures aux bords des objets'], 'main_findings': ['Le fine-tuning est important pour obtenir des résultats adéquats en segmentation basée sur des prompts, comme le confirment les résultats plus précis de SAM (fine-tuning) et LVM-Med par rapport à SAM standard', 'LVM-Med produit des segmentations plus stables et précises que SAM (fine-tuning), notamment au niveau des contours des objets']}

## Conclusions

Une technique d'apprentissage auto-supervisé basée sur le graph matching de second ordre, entraînée sur un grand ensemble de données d'imagerie médicale, améliore significativement les performances sur diverses tâches d'imagerie médicale en aval comparée à d'autres méthodes d'apprentissage supervisé et à des modèles de fondation entraînés sur des centaines de millions d'instances image-texte Les bénéfices de cette approche sont démontrés sur deux architectures différentes, ResNet-50 et ViT, utilisables pour la segmentation end-to-end ou par prompt

## Summary of datasets and downstream tasks

|  |  |  |  |  | AFN-Net | JCS | CoLL | DRG-Net |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Evaluation | Downstream Task Data | Modality | Nums | Task | LVM-Med (DRG-Net) |
| Fine-Tuning | BraTS2018 [64] | 3D MRI | 285 | Tumor Segmentation | 90 |  |
| Fine-Tuning | MMWHS-CT [65] | 3D CT | 20 Heart Structures Segmentation |  |  |
| Fine-Tuning | MMWHS-MRI [65] | 3D MRI | 30 Heart Structures Segmentation |  |  |
| Fine-Tuning | ISIC-2018 [66] | 2D Dermoscopy 2596 Skin Leision Segmentation |  |  |
| Fine-Tuning | JSRT [67] | 2D X-ray | 247 Multi-Organ Segmentation |  |  |
| Fine-Tuning | KvaSir [68] | 2D Endoscope 1000 | Detection Polyp Segmentation & | 85 |  |
| Fine-Tuning | Drive [69] | Fundus | 40 | Vessel Segmentation |  |  |
| Fine-Tuning | BUID [70] | 2D Ultrasound 647 Breast Cancer Segmentation |  |  |
| Linear Evaluation & Fine-Tuning | FGADR [71] | Fundus | 1841 | DR Grading | 80 |  |
| Linear Evaluation & Fine-Tuning | Brain Tumor Classification | 2D MRI | 3264 Brain Tumor Classification |  |  |
| Fine-Tuning | Multi-site Prostate MRI Segmentation [72] | 3D MRI | 116 | Prostate Segmentation |  | Accuracy | Kappa |
| Fine-Tuning | VinDr [73] | 2D X-ray | 18000 Lung Diseases Detection |  |  |

## Performance comparison on five 2D segmentation tasks with fully fine-tuning. Results are reported with an average 2D Dice score on three trial times. The best results in each group are in bold, the overall best value, excluding prompt-based segmentation, is underlined.

|  | Method | ISIC-2018 (Skin Lesion) JSRT (Lung X-ray) KvaSir (Polyp) Drive (Vessel) BUID (Breast Cancer) |
| --- | --- | --- | --- | --- | --- | --- |
|  | Randomly (R50) | 86.16 ± 0.14 | 93.10 ± 0.12 | 62.85 ± 1.32 | 59.82 ± 2.00 | 65.54 ± 0.21 |
|  | Pre-trained ImageNet [60] | 86.87 ± 0.47 | 94.52 ± 2.66 | 83.85 ± 1.32 | 65.12 ± 1.55 | 72.64 ± 1.14 |
| 2D Supervised Method | Attention-Unet [77] | 86.81 ± 0.51 | 94.47 ± 2.71 | 82.23 ± 1.41 | 65.02 ± 1.44 | 72.19 ± 1.16 |
|  | U-Net ++ [78] | 86.71 ± 0.49 | 94.32 ± 2.81 | 82.23 ± 1.41 | 65.38 ± 0.78 | 73.76 ± 2.83 |
|  | Trans U-Net [76] | 86.60 ± 0.82 | 89.80 ± 0.35 | 67.11 ± 0.24 | 62.63 ± 0.24 | 67.90 ± 0.40 |
|  | Twin-Barlon [13] | 86.01 ± 0.07 | 94.56 ± 3.09 | 83.00 ± 0.23 | 65.73 ± 1.46 | 74.46 ± 1.19 |
|  | Dino [79] | 86.79 ± 0.09 | 94.84 ± 2.79 | 79.84 ± 1.62 | 65.39 ± 0.81 | 76.21 ± 0.57 |
|  | SimCLR [15] | 87.28 ± 0.21 | 94.79 ± 2.93 | 82.20 ± 0.51 | 65.22 ± 2.18 | 76.52 ± 0.22 |
| 2D-SSL on medical | Moco-v2 [17] | 87.24 ± 0.14 | 94.05 ± 3.52 | 78.24 ± 1.35 | 64.92 ± 2.21 | 75.93 ± 1.96 |
|  | Deepcluster-v2 [20] | 86.73 ± 0.42 | 94.79 ± 2.89 | 82.69 ± 0.75 | 64.14 ± 0.92 | 76.33 ± 0.99 |
|  | VicRegl [14] | 86.27 ± 0.33 | 94.39 ± 3.25 | 81.93 ± 0.48 | 66.17 ± 0.27 | 75.29 ± 0.64 |
|  | LVM-Med (R50) | 87.76 ± 0.30 | 95.13 ± 2.64 | 86.76 ± 0.94 | 66.97 ± 0.27 | 78.65 ± 0.72 |
|  | Clip [3] | 85.98 ± 0.19 | 89.00 ± 1.08 | 72.63 ± 0.37 | 63.01 ± 0.36 | 70.43 ± 0.24 |
| Foundation Model | Flava [5] SAM [6] | 86.42 ± 0.10 88.17 ± 0.30 | 90.08 ± 0.20 90.68 ± 0.40 | 69.47 ± 0.05 70.75 ± 0.60 | 61.09 ± 0.45 64.04 ± 0.41 | 67.54 ± 1.17 73.07 ± 0.66 |
|  | LVM-Med (SAM's ViT) | 88.41 ± 0.28 | 90.74 ± 0.47 | 73.10 ± 0.08 | 65.49 ± 0.12 | 77.20 ± 0.42 |
|  | SAM (fixed encoder) [9] | 92.42 ± 0.12 | 92.89 ± 5.24 | 89.37 ± 0.57 | 59.74 ± 0.63 | 87.63 ± 0.67 |
| Prompt-based Seg. | SAM with Prompt (no-train) [6] | 55.78 ± 0.66 | 61.97 ± 4.48 | 80.77 ± 0.19 | 15.12 ± 0.24 | 78.44 ± 1.01 |
|  | LVM-Med (SAM's ViT) | 92.48 ± 0.07 | 93.74 ± 4.06 | 90.09 ± 0.14 | 63.01 ± 0.02 | 89.69 ± 0.61 |

## Table 3

| : 3D segmentation task performance |
| --- | --- | --- | --- |
| with fine-tuning on three datasets. Results |
| are reported with an average 3D IoU on five |
| trial times. The best results in each group |
| and overall are in bold and underlined. |
| Method | BraTS | MMWHS-CT MMWHS-MRI |
| 3D-Transformer [80] | 66.54 ± 0.40 | 67.30 ± 2.29 | 67.64 ± 2.21 |
| I3D [81] | 67.83 ± 0.75 | 76.63 ± 2.32 | 66.71 ± 1.27 |
| NiftyNet [82] | 60.78 ± 1.60 | 74.91 ± 2.78 | 64.60 ± 1.96 |
| Med3D [83] | 66.09 ± 1.35 | 75.01 ± 0.74 | 63.43 ± 0.61 |
| Model Genesis [32] | 67.96 ± 1.29 | 76.48 ± 2.89 | 74.53 ± 1.69 |
| Universal Model [84] | 72.10 ± 0.67 | 78.14 ± 0.77 | 77.52 ± 0.50 |
| TransVW [33] | 68.82 ± 0.38 | 79.74 ± 2.78 | 75.08 ± 2.04 |
| SwinViT3D [85] | 70.58 ± 1.27 | 70.19 ± 1.23 | 78.25 ± 1.66 |
| Joint-2D-3D (Deepc) [86] 72.81 ± 0.15 | 83.58 ± 1.54 | 78.14 ± 1.32 |
| Twin-Barlon [13] | 73.30 ± 0.18 | 84.74 ± 1.01 | 76.39 ± 2.23 |
| Dino [79] | 71.72 ± 0.55 | 81.08 ± 1.62 | 70.42 ± 78.74 |
| SimCLR [15] | 73.15 ± 0.27 | 84.60 ± 1.11 | 76.54 ± 2.22 |
| Moco-v2 [17] | 71.97 ± 0.63 | 75.82 ± 4.20 | 68.29 ± 0.15 |
| Deepcluster [20] | 72.96 ± 0.51 | 84.03 ± 0.50 | 79.05 ± 1.63 |
| VicRegl [14] | 73.23 ± 0.33 | 84.72 ± 0.86 | 76.32 ± 0.78 |
| LVM-Med (R50) | 73.58 ± 0.14 | 84.91 ± 0.77 | 78.59 ± 0.84 |
| Clip [3] | 70.24 ± 1.23 | 78.5 ± 2.70 | 65.9 ± 3.98 |
| Flava [5] | 71.19 ± 0.48 | 78.91 ± 2.24 | 67.14 ± 1.20 |
| SAM (Encoder) [6] | 70.11 ± 1.45 | 77.8 ± 1.60 | 68.09 ± 5.49 |
| LVM-Med (SAM's ViT) 71.42 ± 0.70 | 80.78 ± 1.77 | 69.36 ± 0.18 |

## In-out-distribution evaluation for the segmentation task on the Prostate dataset. Results are reported with an average 2D Dice score on three training times.

| Method |  | Multi-site Prostate Segmentation |  |
| --- | --- | --- | --- | --- | --- |
|  | BMC (Based) | RUNMC | BIDMC | HK | Average |
| 2D Supervised |  |  |  |  |  |
| Random | 65.04 ± 2.07 | 51.44 ± 4.13 | 9.95 ± 13.56 | 12.38 ± 7.68 | 34.7 |
| Pretrained ImageNet [60] | 76.47 ± 1.26 | 62.11 ± 0.85 | 43.74 ± 4.38 | 53.90 ± 2.01 | 59.1 |
| 2D SSL on medical data |  |  |  |  |  |
| Twin-Barlon [13] | 76.28 ± 1.76 | 60.09 ± 1.98 32.63 ± 12.32 34.82 ± 15.09 | 51.0 |
| Dino [79] | 77.90 ± 1.15 | 56.90 ± 1.97 | 21.53 ± 5.54 | 30.92 ± 5.41 | 46.8 |
| SimCLR [15] | 76.51 ± 2.07 | 64.10 ± 4.53 | 32.88 ± 5.43 | 42.29 ± 5.98 | 53.9 |
| Moco-v2 [17] | 74.40 ± 0.89 | 55.49 ± 5.45 27.53 ± 10.18 13.65 ± 14.33 | 42.8 |
| Deepcluster [20] | 77.45 ± 0.35 | 64.35 ± 3.15 | 37.73 ± 8.08 | 44.95 ± 8.57 | 56.1 |
| Swav [21] | 77.59 ± 0.61 | 57.61 ± 2.16 38.43 ± 12.55 44.90 ± 4.78 | 54.6 |
| VicRegl [14] | 74.85 ± 1.13 | 54.09 ± 4.35 | 25.56 ± 5.44 35.45 ± 13.03 | 47.5 |
| LVM-Med (R50) | 80.17 ± 0.55 | 62.48 ± 2.03 | 56.76 ± 6.50 | 52.78 ± 3.04 | 63.0 |
| Prompt-based Seg. |  |  |  |  |  |
| SAM (Fixed encoder) [9] | 95.50 ± 0.29 | 90.39 ± 0.39 | 91.41 ± 0.14 | 91.82 ± 0.26 | 92.28 |
| SAM with Prompt (no-train) [6] | 59.11 ± 1.55 | 66.95 ± 2.49 | 59.68 ± 0.49 | 57.41 ± 2.83 | 60.79 |
| LVM-Med (SAM's ViT) | 95.75 +-0.06 90.40 +-0.36 92.03 +-0.20 | 92.75 +-0.48 | 92.73 |

## Performance comparison on linear evaluation and fine-tuning classification. The results are reported with average Accuracy on three training times.

| Method | Linear Evaluation (Frozen) | Fine-tuning |
| --- | --- | --- | --- | --- |
|  | FGADR | Brain Tumor Cls. | FGADR | Brain Tumor Cls. |
| Twin-Barlon [13] | 66.86 ± 0.41 | 63.03 ± 0.32 | 66.37 ± 0.77 | 74.20 ± 1.38 |
| Dino [79] | 65.98 ± 1.91 | 62.27 ± 0.32 | 67.35 ± 1.36 | 71.91 ± 1.55 |
| SimCLR [15] | 65.30 ± 1.70 | 62.52 ± 1.67 | 67.55 ± 0.28 | 73.52 ± 3.56 |
| Moco-v2 [17] | 65.98 ± 1.04 | 62.35 ± 1.92 | 67.55 ± 1.79 | 74.53 ± 0.43 |
| Deepcluster [20] | 65.34 ± 1.93 | 64.47 ± 0.55 | 67.94 ± 1.78 | 73.10 ± 0.55 |
| VicRegl [14] | 64.71 ± 0.60 | 59.64 ± 1.36 | 65.69 ± 1.46 | 73.18 ± 2.03 |
| LVM-Med (R50) | 68.33 ± 0.48 | 66.33 ± 0.31 | 68.32 ± 0.48 | 76.82 ± 2.23 |
| Clip [3] | 57.87 ± 0.50 | 57.87 ± 0.71 | 57.48 ± 0.86 | 34.86 ± 2.27 |
| Flava [5] | 31.87 ± 0.69 | 35.19 ± 0.43 | 57.18 ± 0.96 | 34.01 ± 5.97 |
| Algin [4] | 36.95 ± 1.04 | 30.71 ± 2.35 | 57.28 ± 0.97 | 63.96 ± 0.04 |
| SAM [6] | 55.13 ± 0.41 | 31.81 ± 4.26 | 58.75 ± 1.32 | 60.66 ± 1.36 |
| LVM-Med (SAM's ViT) 62.46 ± 0.86 | 59.31 ± 0.48 | 63.44 ± 0.73 | 67.34 ± 2.08 |

## LVM-Med ablation study.

| Results are reported on an average |
| --- | --- | --- |
| of five 2D segmentation and two lin- |
| ear classification tasks. The two most |
| important factors are highlighted. |
| Method | Cls.(Acc) Seg. (Dice) |
| LVM-Med (Full) | 67.47 | 83.05 |
| LVM-Med w/o second-order | 62.17 | 80.21 |
| LVM-Med w/o message passing | 65.08 | 81.19 |
| LVM-Med w/o Gumbel noise | 64.32 | 81.37 |
| LVM-Med w/o local similarity | 65.67 | 81.54 |

## Configurations for 3D-based-segmentation tasks 15 × 10 -4 , epochs 20 lr = 10 -3 , epochs 20 lr = 15 × 10 -4 , epochs 30 lr = 10 -3 , epochs 30

| hamming loss |
| --- |

## LVM-Med ablation studies trained with full data, small-scale, and different hyper-parameter α fusing global-and local-based similarities. Results are reported on an average of five 2D segmentation, two linear classifications, and two object detection tasks. The most impacted factors are highlighted.We present a parameter comparison of LVM-Med with other foundation models in Table10. Our LVM-Med model, based on ResNet-50, has significantly fewer parameters, approximately 3-4 times smaller than models such as Flava or SAM, while still maintaining competitive performance. When utilizing the ViT encoder pre-trained by the SAM method, LVM-Med's parameters are comparable to the Flava model and slightly higher than Clip and Align by 1.03 and 1.43 times, respectively. However, it is important to note that both LVM-Med and SAM outperform these models by a significant margin in various settings.

| Method | Cls.(Acc) Seg. (Dice) Detect. (mAP50) |
| --- | --- | --- | --- |
| LVM-Med (full, α = 0.8) | 67.47 | 83.05 | 57.1 |
| LVM-Med (small-scale, α = 0.8) | 63.83 | 81.97 | 56.03 |
| LVM-Med (full, α = 0.7) | 65.89 | 82.20 | 56.49 |
| LVM-Med (full, α = 0.9) | 65.03 | 81.09 | 57.14 |
| C.4 Computational complexity |  |  |  |

## Computational complexity of our approaches and other foundation models.

| Method LVM-Med (R50) LVM-Med (ViT) Clip [3] Flava [5] Align [4] SAM (Encoder) [6] |
| --- | --- | --- | --- | --- |
| #Param | 25.55 M | 88.88 M | 85.80 M 86.39 M 62.14 M | 88.88 M |

## Comparing SSL approaches and Foundation models on classification tasks with two evaluation protocols, Linear evaluation and full Fine-tuning. Settings used with several fully connected layers are in cyan. The best results in 2D-SSL and foundation models (two fully connected layers) are in bold; the best results overall are in bold and underlined.

|  | Method | Linear Evaluation (Frozen) | Fine-tuning |  |
| --- | --- | --- | --- | --- | --- |
|  |  | FGADR (DR Grading) Brain Tumor Class. FGADR (DR Grading) Brain Tumor Class. |
|  | Twin-Barlon [13] | 66.86 ± 0.41 | 63.03 ± 0.32 | 66.37 ± 0.77 | 74.20 ± 1.38 |
|  | Dino [79] | 65.98 ± 1.91 | 62.27 ± 0.32 | 67.35 ± 1.36 | 71.91 ± 1.55 |
|  | SimCLR [15] | 65.30 ± 1.70 | 62.52 ± 1.67 | 67.55 ± 0.28 | 73.52 ± 3.56 |
| 2D-SSL on medical | Moco-v2 [17] Deepcluster [20] | 65.98 ± 1.04 65.34 ± 1.93 | 62.35 ± 1.92 64.47 ± 0.55 | 67.55 ± 1.79 67.94 ± 1.78 | 74.53 ± 0.43 73.10 ± 0.55 |
|  | VicRegl [14] | 64.71 ± 0.60 | 59.64 ± 1.36 | 65.69 ± 1.46 | 73.18 ± 2.03 |
|  | LVM-Med (R50) | 68.33 ± 0.48 66.67 ± 0.84 | 66.33 ± 0.31 74.70 ± 0.84 | 68.32 ± 0.48 70.58 ± 0.36 | 76.82 ± 2.23 78.77 ± 0.78 |
|  | Clip [3] | 57.87 ± 0.50 62.66 ± 0.36 | 57.87 ± 0.71 67.85 ± 0.23 | 57.48 ± 0.86 56.21 ± 1.86 | 34.86 ± 2.27 21.74 ± 1.14 |
|  | Flava [5] | 31.87 ± 0.69 32.84 ± 0.12 | 35.19 ± 0.43 24.45 ± 4.30 | 57.18 ± 0.96 56.01 ± 0.86 | 34.01 ± 5.97 33.67 ± 8.11 |
| Foundation Model | Algin [4] | 36.95 ± 1.04 38.12 ± 1.45 | 30.71 ± 2.35 30.34 ± 1.35 | 57.28 ± 0.97 57.87 ± 0.90 | 63.96 ± 0.04 61.42 ± 0.25 |
|  | SAM [6] | 55.13 ± 0.41 57.48 ± 0.24 | 31.81 ± 4.26 36.89 ± 1.61 | 58.75 ± 1.32 58.75 ± 0.99 | 60.66 ± 1.36 60.07 ± 0.31 |
|  | LVM-Med (SAM's ViT) | 62.46 ± 0.86 63.83 ± 1.36 | 59.31 ± 0.48 64.13 ± 1.14 | 63.44 ± 0.73 59.04 ± 0.14 | 67.34 ± 2.08 64.97 ± 2.71 |
| D.1 Promt-based Segmentation on 3D datasets |  |  |  |

## Prompt-based segmentation on 3D datasets.

|  | Method | BraTS | MMWHS-MRI MMWHS-CT |
| --- | --- | --- | --- | --- |
|  | SAM (fixed encoder) [9] | 85.37 ± 0.07 | 77.64 ± 1.14 | 76.61 ± 1.91 |
| Prompt-based Seg. | SAM with Prompt (no-train) [6] 38.97 ± 0.21 | 59.74 ± 0.76 | 50.25 ± 0.33 |
|  | LVM-Med (SAM's ViT) | 85.76 ±0.07 | 78.91 ± 0.80 | 78.03 ± 0.93 |

### Formule


$$H ℓ l = σ D-1 2 (A ℓ + I N ) D-1 2 H ℓ l-1 g l-1 ,(1)$$

### Formule


$$x s i ∈ G s , x t a ∈ G t , we design a vertex affinity matrix c v ∈ R |V s ||V t | where c v$$

### Formule


$$c lo ia (x s i , x t a ) = E p∈P cos(q s p , q t m(p) ) + E p∈P cos(q s p , q t m ′ (p) )(2)$$

### Formule


$$P = {(r, s)| (r, s) ∈ [1, ..., R] × [1, .., S]$$

### Formule


$$c v ia (x s i , x t a ) = α c glo ia (x s i , x t a ) + (1 -α) c lo ia (x s i , x t a ) + c lo ia (x t a , x s i )(3)$$

### Formule


$$GM(c v , c e ) = arg min v∈U (1,1) -i,a c v ia v ia -i,j,a,b c e ia,jb v ia v jb where U (1, 1) = {v ∈ {0, 1} N ×N |v1 N = 1, v T 1 N = 1}(4)$$

### Formule


$$L(v, v * ) = v.(1 -v * ) + v * .(1 -v).(5)$$

### Formule


$$∇ θ E v∼ρ(v;θ) [L(v, v * )].$$

### Formule


$$∇ θ E v∼ρ(v;θ) [L(v, v * )] ≈ ∇ θ E ϵ∼ρ(ϵ) [L(GM(θ + ϵ), v * )].$$

### Formule


$$∇ θ E v∼p(v;θ) [L(v, v * )] ≈ E ϵ∼ρ(ϵ) 1 λ ṽ -GM (θ + ϵ -λ∇ ṽ L(ṽ, v * )) ,(6)$$

### Formule


$$(c v λ , c e λ ) = (c v + ϵ, c e + ϵ ′ ) -λ∇ ṽ L(ṽ, v * ) // Single sample gradient estimate ∂L ∂c v , ∂L ∂c e = ṽ -GM (c v λ , c e λ ) return 1 λ ∂L ∂c v , ∂L ∂c e$$

### Formule


$$X s , Pos s = s(X) # X k = [x k 1 , x k 2 , ..., x k N ], Pos k = [pos k 1 , pos k 2 , ..., pos k N ] , k ∈ {s, t} X t , Pos t = t(X) # compute feature representations Y s = f θ (X s ); Y t = f θ (X t ) # feature dimensions:NxDxRxS # applying projection Z s = h ϕ (Avg(Y s )); Z t = h ϕ (Avg(Y t )) # dimensions:NxF # build graph structures and message passing G s = k-nearest-neighbor(Z s , k_connects) G t = k-nearest-neighbor(Z t ,k_connects) Ẑs = g ϵ (G s , Z s ); Ẑt = g ϵ (G t , Z t ) # compute$$

### Formule


$$c v = {c v ij } ∈ R N×N ; c e = {c e ia,jb } ∈ R |E s ||E t | # E k be a set of edges in G k , k ∈ {s, t} # perturbed costs with Gumbel noise ϵ, ϵ ′ ∼ Gumbel(0, 1) c v = c v + ϵ; c e = c e + ϵ ′$$

### Formule


$$v = GM(c v , c e ) L(v, v * ) = v.(1 -v * ) + v * .(1 -v) # compute$$
