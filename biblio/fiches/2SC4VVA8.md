# Keypoint-Augmented Self-Supervised Learning for Medical Image Segmentation with Limited Annotation

**Auteurs** : Zhangsihao Yang, Mengwei Ren, Kaize Ding, Guido Gerig, Yalin Wang
**Année** : 2023
**DOI** : 10.52202/075280-2652

## Résumé

Pretraining CNN models (i.e., UNet) through self-supervision has become a powerful approach to facilitate medical image segmentation under low annotation regimes. Recent contrastive learning methods encourage similar global representations when the same image undergoes different transformations, or enforce invariance across different image/patch features that are intrinsically correlated. However, CNNextracted global and local features are limited in capturing long-range spatial dependencies that are essential in biological anatomy. To this end, we present a keypoint-augmented fusion layer that extracts representations preserving both short-and long-range self-attention. In particular, we augment the CNN feature map at multiple scales by incorporating an additional input that learns long-range spatial self-attention among localized keypoint features. Further, we introduce both global and local self-supervised pretraining for the framework. At the global scale, we obtain global representations from both the bottleneck of the UNet, and by aggregating multiscale keypoint features. These global features are subsequently regularized through image-level contrastive objectives. At the local scale, we define a distance-based criterion to first establish correspondences among keypoints and encourage similarity between their features. Through extensive experiments on both MRI and CT segmentation tasks, we demonstrate the architectural advantages of our proposed method in comparison to both CNN and Transformer-based UNets, when all architectures are trained with randomly initialized weights. With our proposed pretraining strategy, our method further outperforms existing SSL methods by producing more robust self-attention and achieving state-of-the-art segmentation results. The code is available at https://github.com/zshyang/kaf.git.

## Méthodologie

{'study_design': "Apprentissage auto-supervisé (SSL) pour le pré-entraînement d'un backbone UNet, suivi d'un finetuning avec annotation limitée, comparé à des architectures CNN et Transformer-based UNet entraînées avec poids initialisés aléatoirement", 'intervention': "Ajout d'une couche de fusion augmentée par points-clés (KAF layer) après chaque bloc convolutif du UNet, injectant l'auto-attention à longue portée via un Vision Transformer appliqué à des points-clés échantillonnés, combinée à des objectifs de pré-entraînement contrastifs globaux (sur la caractéristique bottleneck du UNet et la caractéristique globale agrégée des points-clés multi-échelle) et locaux (via un critère basé sur la distance pour établir des correspondances entre points-clés)", 'control': 'Backbones CNN-only et Transformer-based UNet entraînés avec poids initialisés aléatoirement, ainsi que méthodes SSL existantes', 'primary_outcomes': ['Performance de segmentation few-shot sous annotation limitée'], 'secondary_outcomes': ["Robustesse de l'auto-attention produite par le modèle"], 'statistical_methods': [], 'duration': None, 'setting': 'Trois jeux de données de segmentation IRM et CT'}

## Résultats

{'quantitative': [], 'qualitative_findings': ['Le modèle proposé produit une auto-attention plus robuste comparée aux méthodes SSL existantes'], 'main_findings': ["La couche KAF proposée obtient des résultats nettement meilleurs que les backbones CNN-only et/ou Transformer-based lorsqu'entraînée avec une annotation limitée", "Avec la stratégie de pré-entraînement proposée, la méthode surpasse les méthodes SSL existantes en produisant une auto-attention plus robuste et en atteignant des résultats de segmentation état de l'art", "Des expériences extensives sur trois jeux de données IRM et CT confirment l'avantage architectural de la couche proposée ainsi que des stratégies de pré-entraînement"]}

## Conclusions

La couche de fusion augmentée par points-clés incorpore avec succès les dépendances à longue portée dans le cadre de segmentation basé sur UNet Les objectifs SSL globaux et locaux proposés améliorent le pré-entraînement pour la segmentation d'images médicales sous annotation limitée

## Benchmark results on CHD and ACDC datasets under both random initialized weights, and pretrained weights from SSL. M is the number of patients used in supervised training. We perform 5-fold cross-validation and the mean (standard deviation) dice scores are reported.

|  |  |  | CHD (68 patients in total) |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Init. | Method | M =2 | M =6 | M =10 | M =15 | M =20 | M =30 | M =51 |
|  | UNet [52] | 0.184(.06) 0.508(.06) 0.584(.05) 0.627(.05) 0.658(.04) 0.693(.04) 0.754(.02) |
| Random | Swin-Unet [5] SwinUNETR [58] 0.345(.07) 0.565(.06) 0.638(.05) 0.682(.06) 0.711(.05) 0.725(.06) 0.785(.03) 0.291(.07) 0.543(.07) 0.624(.04) 0.675(.05) 0.717(.04) 0.732(.05) 0.784(.03) |
|  | Ours | 0.344(.05) 0.576(.07) 0.646(.03) 0.686(.03) 0.706(.03) 0.728(.04) 0.778(.03) |
|  | Rotation [18] | 0.171(.06) 0.488(.07) 0.575(.04) 0.625(.04) 0.651(.04) 0.691(.04) 0.749(.03) |
|  | PIRL [45] | 0.196(.07) 0.504(.08) 0.617(.05) 0.658(.03) 0.674(.04) 0.714(.04) 0.761(.03) |
| SSL pretrain | SimCLR [9] GLCL-global [7] GLCL-full [7] | 0.192(.06) 0.515(.06) 0.599(.06) 0.631(.05) 0.666(.05) 0.699(.05) 0.756(.03) 0.255(.10) 0.564(.04) 0.646(.03) 0.669(.04) 0.697(.04) 0.725(.04) 0.766(.03) 0.286(.06) 0.555(.07) 0.614(.06) 0.666(.04) 0.694(.04) 0.733(.04) 0.772(.03) |
|  | CAiD [56] | 0.265(.08) 0.581(.06) 0.647(.04) 0.684(.04) 0.700(.04) 0.737(.04) 0.771(.02) |
|  | PCL [72] | 0.356(.08) 0.600(.06) 0.661(.05) 0.686(.05) 0.716(.04) 0.735(.05) 0.774(.03) |
|  | Ours | 0.392(.06) 0.636(.06) 0.693(.03) 0.712(.03) 0.728(.04) 0.754(.04) 0.788(.03) |
|  |  |  | ACDC (100 patients in total) |  |  |  |
| Init. |  |  |  |  |  |  |  |  |

## Ablation study of our framework over (1) architecture design: the number of self-attention layers within the transformer (#T), scales to insert KAF layer (l 1 , • • • , l 4 ); and (2) pretraining hyperparameters (w 1 , w 2 , w 3 ). Five-fold cross-validation results on both datasets are reported.

| Init. | Exp |  | Architecture design |  |  | Pretraining | Dice |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | #T l1 l2 l3 l4 w1 w2 | w3 | CHD (M =15) ACDC (M =6) |
|  | A | 9 | 0 | 0 | 0 | 0 | - | - | - | 0.627(.05) | 0.782(.03) |
|  | B | 9 | 1 | 1 | 1 | 0 | - | - | - | 0.658(.04) | 0.806(.04) |
|  | C | 9 | 1 | 1 | 0 | 1 | - | - | - | 0.677(.04) | 0.817(.04) |
| Random | D E | 9 9 | 1 0 | 0 1 | 1 1 | 1 1 | -- | -- | -- | 0.667(.04) 0.666(.04) | 0.814(.04) 0.811(.04) |
|  | F | 9 | 1 | 1 | 1 | 1 | - | - | - | 0.686(.03) | 0.827(.05) |
|  | G | 6 | 1 | 1 | 1 | 1 | - | - | - | 0.690(.03) | 0.824(.03) |
|  | H | 3 | 1 | 1 | 1 | 1 | - | - | - | 0.677(.03) | 0.814(.03) |
|  | I | 9 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0.699(.04) | 0.867(.02) |
| SSL pretrain | J K | 9 9 | 1 1 | 1 1 | 1 1 | 1 1 | 0 1 | 1 1 | 0 0 | 0.701(.03) 0.711(.03) | 0.865(.02) 0.865(.01) |
|  | L | 9 | 1 | 1 | 1 | 1 | 1 | 1 | 0.01 | 0.712(.03) | 0.873(.01) |

## Segmentation results (dice scores) with different keypoint detection methods (M =2).

| Init. | Keypoint detector | CHD | ACDC |
| --- | --- | --- | --- |
| Random Init. SuperPoint [13] | 0.643(.04) 0.810(.02) |
|  | SIFT | 0.686(.03) 0.827(.05) |
| SSL Pretrain SuperPoint [13] | 0.703(.03) 0.865(.02) |
|  | SIFT | 0.712(.03) 0.873(.01) |

## Dice scores under different keypoint correspondence threshold values. Overall, we observe that the results are not sensitive to specific threshold values.

| Threshold | Dice |
| --- | --- |
| 5 | 0.689 (0.043) |
| 10 | 0.690 (0.031) |
| 15 | 0.684 (0.035) |
| 20 | 0.689 (0.036) |
| 25 | 0.684 (0.032) |
| 30 | 0.685 (0.033) |
| 35 | 0.690 (0.037) |
| 40 | 0.687 (0.037) |

## Segmentation results on Synapse dataset, where finetuning is done on M =2 subjects out of a total of 18 subjects.

| Init. | Method | Dice (M=2) |
| --- | --- | --- |
|  | Unet [52] | 0.253(.06) |
| Random | Swin-Unet [5] SwinUNETR [58] | 0.198(.04) 0.279(.06) |
|  | Ours | 0.289(.06) |
|  | PCL [72] | 0.306(.05) |
| SSL | Swin-Unet (with [72]) SwinUNETR (with [72]) | 0.210(.07) 0.304(.06) |
|  | Ours | 0.322(.06) |

## Performance comparison among standard UNet (UNet(c1)), a larger UNet with duplicated input channels (UNet(c2)), and UNet augmented with features derived from KAF (Ours). The results indicate that using a larger UNet slightly improves the segmentation performance. Our proposed KAF-enhanced UNet further boosts the performance significantly compared with UNet(c2).

| Sample M dataset | Method | mean/std | #params |
| --- | --- | --- | --- | --- |
| 15 | CHD | UNet(c1) 0.627(.05) | 7.8 M |
| 15 | CHD | UNet(c2) 0.646(.04) | 27.9 M |
| 15 | CHD | Ours | 0.712(.03) | 71.7 M |
| 6 | ACDC UNet(c1) 0.782(.03) | 17.5 M |
| 6 | ACDC UNet(c2) 0.796(.03) | 62.8 M |
| 6 | ACDC | Ours | 0.873(.01) 106.8 M |

## Additional assessment of weight of L local in pretraining to supplement Tab. 2 in the main text. The results are all from pretraining on CHD and finetuning at M = 15.

| w1 w2 | w3 | Dice |
| --- | --- | --- | --- |
| 1 | 1 | 0.1 | 0.702(.04) |
| 1 | 1 | 0.01 | 0.712(.03) |
| 1 | 1 | 0.001 0.708(.04) |
| 0 | 1 | 0.08 | 0.705(.03) |
| 0 | 1 | 0.04 | 0.705(.03) |
| 0 | 1 | 0.02 | 0.707(.03) |
| 0 | 1 | 0.01 | 0.700(.03) |
| 0 | 1 | 0.005 0.700(.03) |
| 0 | 1 | 0.001 0.705(.03) |
| 0 | 0 | 1 | 0.689(.04) |

## Segmentation results on CHD dataset from a random initialized FCN backbone. The column 'With KAF' indicates whether the proposed KAF layer is inserted to the backbone. The results demonstrate that the integration of the KAF layer tends to improve the mean values across different sample sizes, indicating an enhanced performance of the FCN when augmented with the KAF layer.

| Sample M With KAF Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | Mean/Std |
| --- | --- | --- | --- | --- | --- |
| 2 | -✓ | 0.2259 0.2133 0.3297 0.2517 0.2133 0.3392 0.3034 0.3794 0.297(.059) 0.311 0.3516 0.286(.056) |
| 6 | -✓ | 0.4441 0.5462 0.5427 0.5918 0.4854 0.522(.052) 0.4495 0.5603 0.5652 0.6286 0.5535 0.551(.058) |
| 10 | -✓ | 0.4866 0.5584 0.6393 0.6613 0.6094 0.591(.063) 0.5632 0.6209 0.6381 0.6718 0.6383 0.626(.036) |
| 15 | -✓ | 0.5938 0.6356 0.6702 0.6926 0.6499 0.648(.033) 0.6157 0.6163 0.7117 0.6936 0.6537 0.658(.039) |
| 20 | -✓ | 0.6318 0.6422 0.7102 0.7383 0.6356 0.672(.044) 0.6382 0.6541 0.7112 0.7309 0.6806 0.683(.034) |
| 30 | -✓ | 0.6339 0.6558 0.7498 0.7701 0.6685 0.696(.054) 0.6841 0.6671 0.7507 0.7708 0.6973 0.714(.040) |
| 51 | -✓ | 0.7125 0.7287 0.7693 0.7755 0.7559 0.748(.024) 0.7087 0.7324 0.7711 0.7813 0.7661 0.752(.027) |

## The complete five-fold Dice results for CHD and ACDC.

| Dataset Sample M Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | Mean/Std |
| --- | --- | --- | --- | --- | --- |
| CHD | 2 | 0.3085 0.3292 0.4649 0.4405 0.4178 0.392(.062) |
|  | 6 | 0.5370 0.6527 0.6707 0.7076 0.6119 0.636(.058) |
|  | 10 | 0.6382 0.6797 0.7252 0.7326 0.6900 0.693(.034) |
|  | 15 | 0.6668 0.6892 0.7519 0.7458 0.6844 0.712(.035) |
|  | 20 | 0.6738 0.7204 0.7629 0.7766 0.7051 0.728(.038) |
|  | 30 | 0.7291 0.7324 0.8001 0.8014 0.7093 0.754(.039) |
|  | 51 | 0.7385 0.7594 0.8148 0.8234 0.8048 0.788(.033) |
| ACDC | 2 | 0.7975 0.7027 0.7510 0.7097 0.7458 0.741(.034) |
|  | 6 | 0.8827 0.8941 0.8620 0.8596 0.8682 0.873(.013) |
|  | 10 | 0.9101 0.9086 0.8919 0.8709 0.8914 0.895(.014) |
|  | 15 | 0.9175 0.9076 0.9140 0.8932 0.9091 0.908(.008) |
|  | 20 | 0.9173 0.9152 0.9168 0.9101 0.9143 0.915(.003) |
|  | 30 | 0.9224 0.9232 0.9252 0.9162 0.9187 0.921(.003) |
|  | 80 | 0.9313 0.9285 0.9336 0.9255 0.9328 0.930(.003) |

## Significance tests.

|  | CHD (M=15) ACDC (M=6) |
| --- | --- | --- |
| Unet w/ random init. [52] | < 0.001 | « 0.001 |
| Ours w/ random init. |  |  |

### Formule


$$F l k ∈ R N ×C l from the dense convolutional feature map F l ∈ R W l ×H l ×C l$$

### Formule


$$F l o = Concat(F l , D l (F l s )).$$

### Formule


$$L i global = - 1 |Ω + i | j∈Ω + i log e sim(g i ,g j ) τ 2N k=1 1 i̸ =k • e sim(g i ,g k ) τ ,(1)$$

### Formule


$$F last from R W last ×H last ×C last to R 1×C last .$$

### Formule


$$U i = Concat(U 1 i , U 2 i , U 3 i , U 4 i ), and U j = Concat(U 1 j , U 2 j , U 3 j , U 4 j )$$

### Formule


$$L i local = - (a,b)∈M log P a, b - a∈I log Pa,Ni+1 - b∈J log PNj+1,b .(2)$$

### Formule


$$L total = w 1 • L P CL + w 2 • L global + w 3 • L local ,(3)$$

### Formule


$$M =2 M =6 M =10 M =15 M =20 M =30 M =80 Random UNet [$$

### Formule


$$M =2 M =6 M =10 M =15 M =20 M =30 M =51 Random SwinUNETR-$$

### Formule


$$M =2 M =6 M =10 M =15 M =20 M =30 M =80 Random SwinUNETR-$$
