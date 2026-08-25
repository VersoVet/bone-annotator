# AGSAM: Agent-Guided Segment Anything Model for Automatic Segmentation in Few-Shot Scenarios

**Auteurs** : Hao Zhou, Yao He, Xiaoxiao Cui, Zhi Xie
**Année** : 2024
**DOI** : 10.3390/bioengineering11050447

## Résumé

Precise medical image segmentation of regions of interest (ROIs) is crucial for accurate disease diagnosis and progression assessment. However, acquiring high-quality annotated data at the pixel level poses a significant challenge due to the resource-intensive nature of this process. This scarcity of high-quality annotated data results in few-shot scenarios, which are highly prevalent in clinical applications. To address this obstacle, this paper introduces Agent-Guided SAM (AGSAM), an innovative approach that transforms the Segment Anything Model (SAM) into a fully automated segmentation method by automating prompt generation. Capitalizing on the pre-trained feature extraction and decoding capabilities of SAM-Med2D, AGSAM circumvents the need for manual prompt engineering, ensuring adaptability across diverse segmentation methods. Furthermore, the proposed feature augmentation convolution module (FACM) enhances model accuracy by promoting stable feature representations. Experimental evaluations demonstrate AGSAM’s consistent superiority over other methods across various metrics. These findings highlight AGSAM’s efficacy in tackling the challenges associated with limited annotated data while achieving high-quality medical image segmentation.

## Méthodologie

{'study_design': "Étude expérimentale comparative avec étude d'ablation, comparant AGSAM à d'autres méthodes de segmentation en reproduisant leurs fonctionnalités principales via code open-source", 'intervention': "Application du framework AGSAM (Agent-Guided SAM), combinant un modèle agent léger générant des prompts automatiques et les modules d'encodage/décodage pré-entraînés de SAM-Med2D, avec le module FACM (feature augmentation convolution module)", 'control': 'Méthodes comparatives (dont AutoSAM et nnSAM mentionnés en introduction) testées et entraînées/affinées de manière uniforme sur le même jeu de données de recherche', 'primary_outcomes': ['Précision de segmentation (métriques diverses non détaillées dans le texte fourni)'], 'secondary_outcomes': [], 'statistical_methods': ['Test t bilatéral (two-sided t-test) avec seuil de significativité p < 0.05'], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [], 'qualitative_findings': [], 'main_findings': ['AGSAM surpasse de manière constante les méthodes comparatives selon diverses métriques', 'Le module FACM améliore la précision du modèle en favorisant des représentations de caractéristiques plus stables']}

## Conclusions

AGSAM est un framework qui exploite SAM pour une segmentation automatique avec un nombre limité d'échantillons d'entraînement Le modèle agent-guidé extrait et fusionne l'encodage de caractéristiques de SAM pour générer des embeddings de prompts pour le décodeur de masques de SAM, éliminant le besoin d'entrées manuelles Les modules d'encodage et de fusion de caractéristiques d'image renforcent l'encodage de SAM en intégrant les capacités du modèle guide, héritant de la représentation de caractéristiques universelle de SAM Le module de génération de prompts guide automatiquement les prédictions de décodage de masques, générant des prompts allant de épars à denses pour contraindre de manière exhaustive et éviter la redondance Une stratégie d'entraînement en ligne d'amélioration des caractéristiques a été explorée, supprimant les réponses de caractéristiques du modèle précédent pendant l'entraînement pour forcer de meilleures réponses aux caractéristiques efficaces lors de l'itération suivante AGSAM a un potentiel en tant que nouveau benchmark few-shot exploitant le pré-entraînement de type SAM

## Comparison results of different methods with different sizes of training sample with DICE and HD in CAMUS. * p < 0.05; ** p < 0.01; *** p < 0.001; ns, not significant (p > 0.05).

|  |  |  |  |  |  |  |  |  | Metrics |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | DICE |  |  |  |  |  |  | HD |  |  |  |  |
| Method |  |  |  |  |  |  |  | Training Sample Size (n) |  |  |  |  |  |  |
|  | 1 | 2 | 4 | 6 | 8 | 12 | 16 | 20 | 1 | 2 | 4 | 6 | 8 | 12 | 16 | 20 |
| FCN | 0.4819 *** | 0.6044 *** | 0.5962 *** | 0.7507 * | 0.7607 *** | 0.7954 ** | 0.8058 ns | 0.8036 ns | 30.7356 *** | 307356 *** | 25.0324 *** | 12.4143 ns | 10.7692 *** | 8.7511 * | 7.9985 ** | 8.1526 ns |
| DeepLabV3 | 0.5157 *** | 0.6312 *** | 0.6382 * | 0.7417 *** | 0.7512 *** | 0.7983 ns | 0.8029 * | 0.8118 ns | 26.2979 *** | 24.4466 *** | 20.1742 *** | 12.1354 ns | 11.6624 *** | 8.3925 *** | 8.5411 *** | 7.3718 ns |
| PSPNet | 0.5308 *** | 0.6198 *** | 0.6059 *** | 0.7002 *** | 0.7206 *** | 0.7400 *** | 0.7592 *** | 0.7681 *** | 23.5507 *** | 17.9434 *** | 18.7494 *** | 12.3391 *** | 11.1914 *** | 11.0718 *** | 9.4149 *** | 9.7201 *** |
| Fast-SCNN | 0.2311 *** | 0.3133 *** | 0.4271 *** | 0.5263 *** | 0.5418 *** | 0.6374 *** | 0.6328 *** | 0.6501 *** | 55.0956 *** | 36.9229 *** | 36.3592 *** | 24.4900 *** | 23.6173 *** | 16.7035 *** | 17.6839 *** | 17.6589 *** |
| TGANet | 0.3387 *** | 0.3503 *** | 0.3886 *** | 0.6406 *** | 0.6435 *** | 0.7145 *** | 0.7216 *** | 0.7069 *** | 57.5892 *** | 56.7400 *** | 44.2247 *** | 19.1582 *** | 19.0647 *** | 14.6703 *** | 14.8420 *** | 15.9357 *** |
| SegFormer | 0.2637 *** | 0.4378 *** | 0.2495 *** | 0.6084 *** | 0.4136 *** | 0.6591 *** | 0.4737 *** | 0.6593 *** | 65.4658 *** | 50.6095 *** | 67.2951 *** | 30.3880 *** | 47.6450 *** | 18.7880 *** | 42.6189 *** | 19.2131 *** |
| Unet++ | 0.2486 *** | 0.2915 *** | 0.3562 *** | 0.6098 *** | 0.6779 *** | 0.7119 *** | 0.7063 *** | 0.7405 *** | 66.9296 *** | 67.5001 *** | 68.7728 *** | 29.8018 *** | 22.7979 *** | 19.4106 *** | 19.3498 *** | 16.7502 *** |
| autoSAM | 0.4482 *** | 0.4911 *** | 0.4465 *** | 0.5844 *** | 0.5807 *** | 0.6671 *** | 0.6642 *** | 0.6682 *** | 61.9208 *** | 51.3325 *** | 47.9954 *** | 20.5984 *** | 20.8936 *** | 17.8528 *** | 17.9705 *** | 18.9544 *** |
| Mamba-Unet | 0.5040 *** | 0.5982 *** | 0.6089 *** | 0.6290 *** | 0.6534 *** | 0.6528 *** | 0.6674 *** | 0.7067 *** | 23.3985 *** | 18.8779 *** | 19.3776 *** | 18.5073 *** | 16.8112 *** | 16.9241 *** | 15.9930 *** | 14.8776 *** |
| nnSAM | 0.5087 | 0.5906 | 0.5882 | 0.7564 | 0.7786 | 0.8021 | 0.8069 | 0.8010 | 32.6712 | 31.6343 | 23.6663 | 11.1222 | 9.2595 | 8.1799 | 7.3214 | 8.2214 |
| (FCN) | *** | *** | *** | ns | ns | ns | *** | ns | *** | *** | *** | * | ns | ns | *** | ns |
| Proposed (FCN) | 0.5419 *** | 0.6164 *** | 0.6103 *** | 0.7570 ns | 0.7818 | 0.8060 | 0.8091 | 0.8052 | 25.5238 *** | 23.3281 *** | 19.4167 *** | 10.5465 | 8.7999 | 7.9875 | 7.1839 | 7.8991 |
| nnSAM | 0.5323 | 0.6417 | 0.6435 | 0.7530 | 0.7588 | 0.7915 | 0.8031 | 0.8058 | 24.2617 | 19.6827 | 17.5183 | 12.6661 | 10.7260 | 9.3173 | 8.4043 | 8.0490 |
| (deep) | *** | *** | ns | ns | *** | *** | ns | ns | *** | *** | ns | ns | *** | *** | ** | ns |
| Proposed (deep) | 0.5758 | 0.6584 | 0.6519 | 0.7599 | 0.7672 ** | 0.7973 * | 0.8091 ns | 0.8104 ns | 20.7766 | 17.5505 | 16.7683 | 11.8957 *** | 10.3071 *** | 8.7514 * | 7.8906 * | 7.6765 ns |

## Comparison results of different methods with different size of training sample with DICE and HD in REFUGE. * p < 0.05; ** p < 0.01; *** p < 0.001; ns, not significant (p > 0.05).

|  |  |  |  |  |  |  |  |  | Metrics |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | DICE |  |  |  |  |  |  | HD |  |  |  |  |
| Method |  |  |  |  |  |  |  | Training Sample Size (n) |  |  |  |  |  |  |
|  | 1 | 2 | 4 | 6 | 8 | 12 | 16 | 20 | 1 | 2 | 4 | 6 | 8 | 12 | 16 | 20 |
| FCN | 0.4790 *** | 0.6759 *** | 0.7762 *** | 0.8210 *** | 0.8130 *** | 0.8726 ns | 0.8718 ns | 0.8751 ns | 20.0650 *** | 10.7355 *** | 5.3205 *** | 3.0799 ** | 3.3850 *** | 1.7938 ns | 1.9800 ns | 1.6347 ns |
| DeepLabV3 | 0.5657 *** | 0.7034 *** | 0.8229 *** | 0.8145 *** | 0.8350 ns | 0.8736 ns | 0.8754 ns | 0.8763 ns | 19.1857 *** | 8.0980 *** | 3.3823 *** | 4.2733 *** | 2.8859 * | 1.7468 ns | 1.7494 ns | 1.4995 ns |
| PSPNet | 0.2952 *** | 0.5397 *** | 0.6876 *** | 0.7643 *** | 0.7935 *** | 0.8342 *** | 0.8432 *** | 0.8349 *** | 36.6751 *** | 8.7706 *** | 6.3812 *** | 8.7565 *** | 7.6729 *** | 5.8643 *** | 3.9266 *** | 3.8622 *** |
| Fast-SCNN | 0.3473 *** | 0.5133 *** | 0.6423 *** | 0.6507 *** | 0.6662 *** | 0.7837 *** | 0.7746 *** | 0.7987 *** | 45.4614 *** | 31.5551 *** | 15.1610 *** | 15.2604 *** | 15.1658 *** | 6.2228 *** | 6.7428 *** | 6.1936 *** |
| TGANet | 0.5750 *** | 0.6537 *** | 0.6491 *** | 0.6970 *** | 0.7471 *** | 0.8157 *** | 0.8091 *** | 0.7976 *** | 26.2602 *** | 26.0183 *** | 31.2509 *** | 26.2529 *** | 15.8280 *** | 8.5710 *** | 9.9134 *** | 10.0348 *** |
| SegFormer | 0.6014 *** | 0.6518 *** | 0.7065 *** | 0.7574 *** | 0.7638 *** | 0.7764 *** | 0.7559 *** | 0.7578 *** | 30.1322 *** | 16.0105 *** | 14.2888 *** | 7.9404 *** | 8.1005 *** | 9.7448 *** | 9.4702 *** | 9.1201 *** |
| Unet++ | 0.5241 *** | 0.4020 *** | 0.7922 *** | 0.8215 *** | 0.7961 *** | 0.8426 *** | 0.8463 *** | 0.8563 *** | 41.3638 *** | 82.2642 *** | 9.9493 *** | 8.1613 *** | 10.7172 *** | 10.3751 *** | 9.2046 *** | 7.2565 *** |
| autoSAM | 0.4723 *** | 0.4456 *** | 0.7208 *** | 0.7627 *** | 0.7789 *** | 0.8042 *** | 0.7972 *** | 0.8076 *** | 22.5677 *** | 35.1402 *** | 12.9685 *** | 8.2359 *** | 8.5600 *** | 6.2316 *** | 5.2601 *** | 5.3802 *** |
| Mamba-Unet | 0.2567 *** | 0.3326 *** | 0.3225 *** | 0.6176 *** | 0.6935 *** | 0.7320 *** | 0.6709 *** | 0.7605 *** | 41.4738 *** | 33.2122 *** | 15.8653 *** | 13.8365 *** | 10.6301 *** | 13.8848 *** | 16.3959 *** | 8.5436 *** |
| nnSAM | 0.6049 | 0.7886 | 0.7994 | 0.8172 | 0.8412 | 0.8737 | 0.8668 | 0.8720 | 13.0598 | 3.8768 | 4.5948 | 3.3072 | 2.6651 | 1.7309 | 1.9841 | 2.0956 |
| (FCN) | *** | ns | *** | *** | *** | ns | *** | ** | *** | ns | *** | *** | *** | ns | ns | * |
| Proposed (FCN) | 0.7141 | 0.7898 | 0.8427 | 0.8449 | 0.8432 | 0.8743 | 0.8773 | 0.8800 | 7.5007 | 4.6304 | 2.3837 | 2.3026 | 2.3543 | 1.7615 | 1.8195 | 1.5801 |
| nnSAM | 0.6347 | 0.7007 | 0.8028 | 0.8176 | 0.8395 | 0.8721 | 0.8681 | 0.8748 | 10.5907 | 9.2379 | 3.9076 | 3.6697 | 2.8225 | 2.0105 | 1.9409 | 1.7629 |
| (deep) | *** | *** | *** | *** | ns | ns | ** | ns | *** | *** | *** | *** | ns | ns | ns | ns |
| Proposed | 0.6725 | 0.7282 | 0.8075 | 0.8229 | 0.8329 | 0.8674 | 0.8741 | 0.8784 | 11.8223 | 7.5185 | 4.2160 | 3.3738 | 2.6646 | 2.1048 | 2.2357 | 1.5954 |
| (deep) | *** | *** | *** | *** | * | * | ns | ns | *** | *** | *** | *** | ns | ns | ns | ns |

## Results of different AGSAM-based models with different module combinations in ablation analysis.

|  |  | Modules |  | Metrics |  |
| --- | --- | --- | --- | --- | --- |
|  | FE | MD | FACM | DICE | HD |
| Ablation study (FCN) n = 1 | × √ √ | × × √ | × × × | 0.4819 0.5087 0.5324 | 33.53 32.67 25.57 |
|  | √ | √ | √ | 0.5419 | 25.52 |
|  |  | Modules |  | Metrics |  |
|  | FE | MD | FACM | DICE | HD |
| Ablation study (DeeplabV3) n = 1 | × √ √ | × × √ | × × × | 0.5157 0.5323 0.5689 | 26.30 24.26 20.67 |
|  | √ | √ | √ | 0.5758 | 20.78 |
|  |  | Modules |  | Metrics |  |
|  | FE | MD | FACM | DICE | HD |
| Ablation study (Unet++) n = 1 | × √ √ | × × √ | × × × | 0.2486 0.2430 0.2592 | 66.93 68.49 66.88 |
|  | √ | √ | √ | 0.2615 | 66.46 |

## Results of AGSAM with different fusion weight ratio of agent and SAM.

| Fusion Weight of Agent and SAM |  | Training Sample Size (n) |  |
| --- | --- | --- | --- | --- | --- | --- |
| Agent | SAM | Metrics | 1 | 4 | 8 | 16 |
| 0.1 | 0.9 | DICE | 0.5758 | 0.6428 | 0.7683 | 0.7986 |
| 0.25 | 0.75 | DICE | 0.5683 | 0.6427 | 0.7672 | 0.8091 |
| 0.5 | 0.5 | DICE | 0.5581 | 0.6385 | 0.7618 | 0.8063 |
| 0.75 | 0.25 | DICE | 0.5536 | 0.6357 | 0.7591 | 0.8023 |
| 0.9 | 0.1 | DICE | 0.5518 | 0.6345 | 0.7580 | 0.8005 |
| 0.1 | 0.9 | HD | 20.7766 | 18.2607 | 10.1163 | 8.0842 |
| 0.25 | 0.75 | HD | 20.6299 | 18.4923 | 10.3071 | 7.8906 |
| 0.5 | 0.5 | HD | 20.5974 | 18.9707 | 10.6805 | 9.6143 |
| 0.75 | 0.25 | HD | 20.6733 | 19.2346 | 10.8251 | 11.4226 |
| 0.9 | 0.1 | HD | 20.6801 | 19.3462 | 10.8708 | 12.2420 |

### Formule


$$f SAM = M SAM encoder (I)(1)$$

### Formule


$$f Agent = M agent encoder (I)(2)$$

### Formule


$$f Fused = M CM f Agent , f ′ SAM = Conv 1×1 f Agent ⊕ F bilinear (Conv 3×3 ( f SAM ))(3)$$

### Formule


$$Mask agent = M agent decoder ( f Fused )(4)$$

### Formule


$$p sparse = Arrange Conv 1×1 FACMs Avgpool Mask agent(5)$$

### Formule


$$p dense = Arrange Conv 1×1 FACMs Avgpool f ′ f used (6)$$

### Formule


$$Mask SAM = M SAM decoder p sparse , p dense(7)$$

### Formule


$$Mask pred = (1 -α)×Mask SAM + α × Mask agent(8)$$

### Formule


$$L all = L Agent + L pred(9)$$

### Formule


$$x aug = α × x + β (10)$$

### Formule


$$x ′ = M FCAM (x) = a × Conv 3×3 (x) + β + Conv 3×3 (x), status : ON 1 × Conv 3×3 (x) + 0 + Conv 3×3 (x), status : OFF (11)$$
