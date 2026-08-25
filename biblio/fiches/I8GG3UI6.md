# Efficient Quantization-Aware Training on Segment Anything Model in Medical Images and Its Deployment

**Auteurs** : Haisheng Lu, Yujie Fu, Fan Zhang, Le Zhang
**Année** : 2025
**DOI** : 10.1007/978-3-031-81854-7_9

## Résumé

Medical image segmentation is a critical component of clinical practice, and the state-of-the-art MedSAM model has significantly advanced this field. Nevertheless, critiques highlight that MedSAM demands substantial computational resources during inference. To address this issue, the CVPR 2024 MedSAM on Laptop Challenge was established to find an optimal balance between accuracy and processing speed. In this paper, we introduce a quantization-aware training pipeline designed to efficiently quantize the Segment Anything Model for medical images and deploy it using the OpenVINO inference engine. This pipeline optimizes both training time and disk storage. Our experimental results confirm that this approach considerably enhances processing speed over the baseline, while still achieving an acceptable accuracy level. The training script, inference script, and quantized model are publicly accessible at https://github.com/AVC2-UESTC/QMedSAM.

## Méthodologie

{'study_design': "Pipeline d'entraînement sensible à la quantification (quantization-aware training, QAT) appliqué au modèle LiteMedSAM (backbone ViT-Tiny distillé), utilisant le framework Xilinx Brevitas, avec déploiement sur le moteur d'inférence OpenVINO", 'intervention': "Quantification du modèle LiteMedSAM via QAT (intégration de nœuds de quantification/dé-quantification dans le graphe de calcul pendant l'entraînement), utilisation d'un dataset en ligne optimisé et d'un sous-ensemble réduit du dataset d'entraînement", 'control': 'Modèle baseline LiteMedSAM (non quantifié) fourni par le challenge', 'primary_outcomes': ['Précision de segmentation (accuracy) moyenne et par modalité', "Vitesse/efficacité d'inférence"], 'secondary_outcomes': ["Espace de stockage disque requis pour l'entraînement", "Balance de la performance entre les différentes modalités d'imagerie"], 'statistical_methods': [], 'duration': None, 'setting': 'CVPR 2024 MedSAM on Laptop Challenge'}

## Résultats

{'quantitative': [], 'qualitative_findings': ['Le modèle quantifié proposé montre une diminution marginale de la précision moyenne mais une bien meilleure balance entre les modalités par rapport au baseline', "L'efficacité d'inférence a été significativement optimisée pour un même backbone", "La performance du modèle sur les différentes modalités varie entre l'ensemble de validation et l'ensemble de test, mais la tendance de balance entre modalités reste cohérente"], 'main_findings': ['Le pipeline de quantification proposé accélère considérablement la vitesse de traitement par rapport au baseline tout en conservant un niveau de précision acceptable', 'Le modèle quantifié atténue le déséquilibre de performance entre les différentes modalités présentes dans le dataset MedSAM']}

## Conclusions

Le pipeline proposé permet de quantifier efficacement LiteMedSAM et de le déployer sur OpenVINO La méthode accélère significativement le baseline tout en maintenant un niveau de précision acceptable Les travaux futurs se concentreront sur l'amélioration de la vitesse du backbone en virgule flottante, la réduction supplémentaire du déséquilibre entre modalités, et le déploiement sur des plateformes matérielles personnalisées

## Parameters of different submodules in LiteMedSAM and MedSAM

| Parameters Image Encoder Prompt Encoder Mask Decoder |
| --- | --- | --- | --- |
| LiteMedSAM MedSAM | 5.7M 89.7M | 6.2K | 4.1M |

## Samples of modalities in the training dataset (including the additional datasets released in the post-challenge task). 3D modalities are counted with the number of 2D clips on the z-axis.

| 3D Modalities | CT | MR | PET |  |
| --- | --- | --- | --- | --- |
| Samples | 1218411 | 236804 | 89059 |  |
| 2D Modalities Endoscopy | X-Ray | Dermoscopy | US |
| Samples | 43443 | 34893 | 3694 | 1646 |
| 2D Modalities | OCT | Mammography Fundus Microscopy |
| Samples | 1436 | 1233 | 1057 | 1000 |

## Training protocols. Values separated by vertical bars in the table correspond to stages 1 ∼ 3.

| Pre-trained Model | LiteMedSAM (the baseline) |
| --- | --- |
| Batch size | 2 | 4 | 2 |
| DDP world size | 4 |
| Samples of each modality (Ns) 900 |
| Optimizer | SGD (momentum=0.9) |
| Total epochs | 14 |
| Initial learning rate | 0.01 |
| Warm-up epochs (Nw) | 5 |
| Cosine annealing epochs (Na) 10 |
| Training time | 5 | 2.5 | 1 hours |

## Development environments and requirements.

| System | Ubuntu 20.04.3 LTS |
| --- | --- |
| CPU | Intel(R) Xeon(R) Gold 5218R CPU@2.10GHz |
| RAM | 16×32GB |
| GPU | 4×NVIDIA GeForce RTX 3090 |
| CUDA version | 12.2 |
| Programming language Python 3.11 |
| Deep learning framework PyTorch 2.0.1 |
| Specific dependencies | Brevitas 0.10.3 |
| Code | https://github.com/AVC2-UESTC/QMedSAM |
| 4 Results and discussion |
| 4.1 Inference speeds of different engines |

## Inference speed of different LiteMedSAM variants.

| Method |
| --- |

## Inference speed of different MedSAM variants.

| Method |
| --- |

## Quantitative evaluation results on the validation dataset.

|  | Stage 3 | Stage 2 | Stage 1 | Baseline |
| --- | --- | --- | --- | --- | --- |
|  | DSC | NSD | DSC NSD DSC NSD | DSC | NSD |
| CT | 89.35% 92.84% 89.73% 93.23% 89.86% 93.27% 90.78% 93.08% |
| MR | 82.41% 87.29% 82.73% 87.76% 82.91% 87.87% 86.43% 90.37% |
| PET | 64.80% 56.33% 63.37% 49.52% 63.86% 48.75% 57.64% 43.05% |
| US | 87.87% 92.41% 87.93% 92.50% 87.88% 92.39% 94.54% 96.62% |
| X-Ray | 78.73% 84.19% 78.14% 83.80% 78.62% 84.31% 79.15% 84.46% |
| Dermoscopy 91.71% 93.31% 92.15% 93.75% 92.12% 93.70% 91.59% 93.21% |
| Endoscopy 93.37% 96.61% 93.56% 96.71% 94.08% 97.12% 94.81% 97.70% |
| Fundus | 93.24% 94.66% 93.85% 95.19% 92.97% 94.30% 94.40% 95.77% |
| Microscope 70.11% 77.35% 71.77% 79.21% 72.77% 80.18% 60.54% 65.12% |
| Average | 83.51% 86.11% 83.69% 85.74% 83.90% 85.76% 83.32% 84.38% |

## Quantitative efficiency in terms of inference running time (seconds). MLE stands for Memory Limit Exceeded.

| Case ID | Size | Objects Baseline Proposed |
| --- | --- | --- | --- | --- |
| 3DBox_CT_0566 | (287, 512, 512) | 6 | 591.1 | 142.1 |
| 3DBox_CT_0888 | (237, 512, 512) | 6 | 168.7 | 51.0 |
| 3DBox_CT_0860 | (246, 512, 512) | 1 | 23.4 | 12.4 |
| 3DBox_MR_0621 | (115, 400, 400) | 6 | 245.6 | 51.5 |
| 3DBox_MR_0121 | (64, 290, 320) | 6 | 168.4 | 31.4 |
| 3DBox_MR_0179 | (84, 512, 512) | 1 | 22.5 | 11.9 |
| 3DBox_PET_0001 | (264, 200, 200) | 1 | 15.1 | 7.3 |
| 2DBox_US_0525 | (256, 256, 3) | 1 | 1.6 | 0.7 |
| 2DBox_X-Ray_0053 | (320, 640, 3) | 34 | 9.2 | 1.8 |
| 2DBox_Dermoscopy_0003 (3024, 4032, 3) | 1 | 6.5 | 1.1 |
| 2DBox_Endoscopy_0086 | (480, 560, 3) | 1 | 2.3 | 0.6 |
| 2DBox_Fundus_0003 | (2048, 2048, 3) | 1 | 3.5 | 0.7 |
| 2DBox_Microscope_0008 (1536, 2040, 3) | 19 | 15.6 | 1.6 |
| 2DBox_Microscope_0016 (1920, 2560, 3) 241 | MLE | 14.0 |

## Evaluation results of the ablation study on the validation dataset.

|  | Stage 3 | Stage 2 | Stage 1 |
| --- | --- | --- | --- |
|  | DSC NSD DSC NSD DSC NSD |
| CT | 88.71% 92.37% 87.02% 91.14% 88.81% 92.45% |
| MR | 81.55% 86.48% 80.91% 86.18% 81.61% 86.40% |
| PET | 64.41% 55.09% 64.35% 54.73% 65.21% 52.62% |
| US | 86.93% 91.76% 86.09% 90.87% 87.43% 91.85% |
| X-Ray | 79.07% 84.53% 76.44% 82.13% 76.18% 81.83% |
| Dermoscopy 91.65% 93.24% 92.63% 94.20% 91.75% 93.34% |
| Endoscopy 93.42% 96.65% 93.99% 97.09% 92.65% 95.84% |
| Fundus | 93.18% 94.59% 96.05% 97.20% 92.93% 94.33% |
| Microscope 72.29% 79.64% 71.03% 78.52% 72.94% 80.40% |
| Average | 83.47% 86.04% 83.17% 85.79% 83.28% 85.45% |
| Proposed | 83.51% 86.11% 83.69% 85.74% 83.90% 85.76% |

## Evaluation results on the test dataset.

|  |  | Proposed |  |  | Baseline |
| --- | --- | --- | --- | --- | --- |
|  | DSC | NSD RunTime DSC | NSD RunTime |
| CT | 69.74% 71.91% 11.78s 55.75% 58.48% 38.78s |
| MR | 69.33% 61.77% 6.20s | 64.80% 62.75% 18.57s |
| X-Ray | 80.13% 89.56% | 2.50s 85.51% 94.40% 9.95s |
| Endoscopy 89.81% 93.15% | 2.18s 94.41% 96.95% 7.56s |
| Fundus | 79.05% 81.28% | 2.23s 87.47% 89.58% 8.77s |
| Microscope 79.68% 81.72% | 2.58s 84.36% 86.15% 16.34s |
| OCT | 72.72% 79.50% | 2.24s | 73.31% 80.20% | 8.39s |
| PET | 76.53% 67.52% | 4.87s | 76.94% 66.98% 14.90s |
| US | 87.49% 92.09% 2.75s | 85.24% 89.73% | 8.96s |
| Average | 78.28% 79.83% | 4.15s | 78.64% 80.58% 14.69s |

### Formule


$$N s (m) = min i∈M N m (i).$$

### Formule


$$N s (m) = max N m (m) 10 , min i∈M N m (i) .$$
