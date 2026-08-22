# Feature Aggregation and Refinement Network for 2D Anatomical Landmark Detection

**Auteurs** : Yueyuan Ao, Hong Wu
**Année** : 2022
**DOI** : 10.1007/s10278-022-00718-4

## Résumé

Localization of anatomical landmarks is essential for clinical diagnosis, treatment planning, and research. This paper proposes a novel deep network named feature aggregation and refinement network (FARNet) for automatically detecting anatomical landmarks. FARNet employs an encoder-decoder structure architecture. To alleviate the problem of limited training data in the medical domain, we adopt a backbone network pre-trained on natural images as the encoder. The decoder includes a multi-scale feature aggregation module for multi-scale feature fusion and a feature refinement module for high-resolution heatmap regression. Coarse-to-fine supervisions are applied to the two modules to facilitate end-to-end training. We further propose a novel loss function named Exponential Weighted Center loss for accurate heatmap regression, which focuses on the losses from the pixels near landmarks and suppresses the ones from far away. We evaluate FARNet on three publicly available anatomical landmark detection datasets, including cephalometric, hand, and spine radiographs. Our network achieves state-of-the-art performances on all three datasets. Code is available at https:// github. com/ Juven ileIn Wind/ FARNet.

## Méthodologie

{'study_design': "Développement et évaluation d'un réseau de neurones profond (FARNet) à architecture encodeur-décodeur, comprenant un backbone pré-entraîné sur images naturelles, un module d'agrégation de caractéristiques multi-échelles (MSFA) et un module de raffinement de caractéristiques (FR), avec supervision coarse-to-fine et une nouvelle fonction de perte (Exponential Weighted Center loss)", 'intervention': "Réseau FARNet : encodeur pré-entraîné sur images naturelles (plusieurs backbones comparés, dont DenseNet-121) + décodeur composé du module MSFA (fusion multi-échelle via chemins d'upsampling/downsampling et connexions résiduelles) et du module FR (génération de cartes de caractéristiques à la résolution exacte de l'image d'entrée)", 'control': None, 'primary_outcomes': ['Précision de la détection/localisation des repères anatomiques'], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [], 'qualitative_findings': [], 'main_findings': ["FARNet atteint des performances état de l'art sur les trois jeux de données évalués (céphalométrique, main, colonne vertébrale)", 'Parmi les réseaux pré-entraînés comparés comme encodeur, DenseNet-121 obtient les meilleures performances', 'La nature end-to-end du réseau le rend plus efficace que les approches précédentes basées sur des patches']}

## Conclusions

FARNet, avec son backbone pré-entraîné, son module d'agrégation de caractéristiques multi-échelles et son module de raffinement de caractéristiques, permet une détection efficace et précise de repères anatomiques Les supervisions coarse-to-fine appliquées aux deux modules facilitent l'entraînement end-to-end La nouvelle fonction de perte proposée, en se concentrant sur les erreurs proches des repères et en supprimant celles éloignées, améliore la régression de heatmap Le réseau atteint des performances état de l'art sur trois jeux de données publics, démontrant son efficacité et sa généralité

## Comparison of our FARNet with prior state-of-the-art methods on the cephalometric X-ray dataset with 19 annotated landmarks The bold value in each column represents the best result

|  |  | Test1 data |  |  |  |  | Test2 data |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Methods | Input size | MRE | 2mm | 2.5mm | 3mm | 4mm | MRE | 2mm | 2.5mm | 3mm | 4mm |
| Ibragimov et al. [20] | - | 1.84 | 71.70 | 77.40 | 81.90 | 88.00 | - | 62.74 | 70.47 | 76.53 | 85.11 |
| Lindner et al. [25] | - | 1.67 | 74.95 | 80.28 | 84.56 | 89.68 | 1.92 | 66.11 | 72.00 | 77.63 | 87.42 |
| Arik et al. [31] | 800 × 640 | - | 75.37 | 80.91 | 84.32 | 88.25 | - | 67.68 | 74.16 | 79.11 | 84.63 |
| Qian et al. [44] | - | - | 82.50 | 86.20 | 89.30 | 92.60 | - | 72.40 | 76.15 | 79.65 | 85.90 |
| Oh et al. [43] | 800 × 640 | 1.18 | 86.20 | 91.20 | 94.40 | 97.70 | 1.44 | 75.89 | 83.36 | 89.26 | 95.73 |
| Chen et al. [42] | 800 × 640 | 1.17 | 86.67 | 92.67 | 95.54 | 98.53 | 1.48 | 75.05 | 82.84 | 88.53 | 95.05 |
| Zhong et al. [38] | 968 × 968 | 1.12 | 86.91 | 91.82 | 94.88 | 97.90 | 1.42 | 76.00 | 82.90 | 88.74 | 94.32 |
| FARNet(Our) | 800 × 640 | 1.12 | 88.03 | 92.73 | 95.96 | 98.48 | 1.42 | 77.00 | 84.42 | 89.47 | 95.21 |

## Table 2

| Landmark localization results from a three-fold cross | Methods | Input size | MRE ± Std (mm) | 2mm (%) | 4mm (%) | 10 mm (%) |
| --- | --- | --- | --- | --- | --- | --- |
| validation on the hand X-ray dataset with 37 annotated landmarks and compare with other methods | Urschler et al. [28] Stern et al. [26] Ebner et al. [23] | 1250 × 1250 1250 × 1250 1250 × 1250 | 0.80 ± 0.93 0.80 ± 0.91 0.97 ± 2.45 | 92.19 92.20 91.60 | 98.46 98.45 97.84 | 99.95 99.95 99.31 |
|  | Lindner et al. [24] | 1250 × 1250 | 0.85 ± 1.01 | 93.68 | 98.95 | 99.94 |
|  | Payer et al. [37] | 512 × 512 | 0.66 ± 0.74 | 94.99 | 99.27 | 99.99 |
|  | FARNet(Our) | 512 × 512 | 0.62 ± 0.55 | 97.24 | 99.8 | 100 |
|  | The bold value in each column represents the best result |  |  |  |

## Landmark localization results on the spinal anterior-posterior X-ray dataset with 68 annotated landmarks and compare with other methods. The units of MSE are the fraction of orinal image (0.010 MSE represents average of 10-pixel error in a 100 × 100 image)

| Methods | MSE (fraction of image) |  |
| --- | --- | --- |
| SVR [27] | 0.006 | 0.93 |
| RFR [21] | 0.0052 | 0.94 |
| BoostNet [33] | 0.0046 | 0.94 |
| FARNet(Our) | 0.0017 | 0.98 |
| The bold value in each column represents the best result |  |

## Comparison of different backbone networks on the Test1 data of the cephalometric X-ray datasetThe bold value in each column represents the best result

|  | MRE | 2mm | 2.5mm | 3mm | 4mm |
| --- | --- | --- | --- | --- | --- |
| VGG-16 | 1.44 | 84.03 | 90.70 | 93.81 | 97.29 |
| VGG-19 | 1.37 | 82.31 | 89.08 | 92.98 | 96.87 |
| ResNet-101 | 1.19 | 86.49 | 92.28 | 95.40 | 98.07 |
| ResNet-152 | 1.29 | 86.76 | 92.42 | 95.33 | 98.03 |
| DenseNet-169 | 1.15 | 87.64 | 92.13 | 95.49 | 98.38 |
| DenseNet-121 | 1.12 | 88.03 | 92.73 | 95.96 | 98.48 |

## Ablation study: the MSFA module, naïve FR module, coarse-to-fine supervision, and the proposed Exponential Weighted Center loss function The bold value in each column represents the best result

|  | MRE | 2mm | 2.5mm | 3mm | 4mm |
| --- | --- | --- | --- | --- | --- |
| U-Net | 1.38 | 84.45 | 90.45 | 93.57 | 97.33 |
| FPN | 1.19 | 85.47 | 92.17 | 95.54 | 98.24 |
| MSFA(+) | 1.18 | 85.73 | 92.31 | 95.83 | 98.36 |
| MSFA | 1.17 | 86.17 | 92.42 | 95.64 | 98.38 |
| MSFA+FR* | 1.16 | 86.91 | 92.63 | 95.68 | 98.45 |
| MSFA+FR | 1.15 | 87.43 | 93.01 | 95.85 | 98.45 |
| MSFA+FR+EWC | 1.12 | 88.03 | 92.73 | 95.96 | 98.48 |

## Lose function comparisonThe bold value in each column represents the best result

|  | MRE | 2mm | 2.5mm | 3mm | 4mm |
| --- | --- | --- | --- | --- | --- |
| L1 | 1.16 | 86.93 | 92.31 | 95.85 | 98.45 |
| Smooth L1 | 1.14 | 87.46 | 92.93 | 95.68 | 98.38 |
| AW | 1.15 | 87.08 | 92.31 | 95.64 | 98.38 |
| MSE | 1.15 | 87.43 | 93.01 | 95.85 | 98.45 |
| EWC | 1.12 | 88.03 | 92.73 | 95.96 | 98.48 |

### Formule


$$(1) H k (i, j) = exp - (i -i k ) 2 + (j -j k ) 2 2 2$$

### Formule


$$Loss = 1 KWH K ∑ k=1 W ∑ i=1 H ∑ j=1 L 2 (y i,j,k , ŷi,j,k )$$
