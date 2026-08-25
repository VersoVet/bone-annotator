# LVIS: A Dataset for Large Vocabulary Instance Segmentation

**Auteurs** : Agrim Gupta, Piotr Dollár, Ross Girshick
**Année** : 2019
**DOI** : 10.1109/cvpr.2019.00550

## Résumé

Progress on object detection is enabled by datasets that focus the research community's attention on open challenges. This process led us from simple images to complex scenes and from bounding boxes to segmentation masks. In this work, we introduce LVIS (pronounced 'el-vis'): a new dataset for Large Vocabulary Instance Segmentation. We plan to collect ∼2 million high-quality instance segmentation masks for over 1000 entry-level object categories in 164k images. Due to the Zipfian distribution of categories in natural images, LVIS naturally has a long tail of categories with few training samples. Given that state-of-the-art deep learning methods for object detection perform poorly in the low-sample regime, we believe that our dataset poses an important and exciting new scientific challenge.

## Méthodologie

{'study_design': "Pipeline d'annotation crowdsourcée itératif (processus de 'object spotting') permettant de découvrir la longue traîne de catégories apparaissant naturellement dans les images, sans utiliser d'algorithmes de machine learning pour automatiser l'étiquetage des données ; conception d'un jeu de données fédéré (fédération de nombreux petits jeux de données constituants, un par catégorie, chacun garantissant une annotation exhaustive pour cette catégorie)", 'intervention': None, 'control': None, 'primary_outcomes': ["Masques de segmentation d'instances de haute qualité pour plus de 1000 catégories d'objets"], 'secondary_outcomes': ['Qualité des masques (chevauchement et cohérence des contours) comparée à des annotateurs experts, à COCO et à ADE20K'], 'statistical_methods': ["Métrique AP (average precision) de style COCO, moyennée sur les catégories et différents seuils d'intersection sur union (IoU) des masques"], 'duration': None, 'setting': 'Annotation crowdsourcée ; premier LVIS Challenge basé sur v0.5 prévu au COCO Workshop à ICCV 2019'}

## Résultats

{'quantitative': [], 'qualitative_findings': ['La distribution des catégories varie entre le plus petit ensemble val et le plus grand ensemble test de LVIS v0.5', "Même avec un ensemble de catégories fixe, les ensembles d'évaluation plus petits peuvent présenter un biais vers un AP plus élevé", "L'impact de ce biais est plus important pour les catégories rares", 'Sur COCO, ce biais a un effet minimal', 'Sur LVIS, ce biais entraîne un AP mesuré sur le plus grand ensemble test inférieur à celui mesuré sur le plus petit ensemble val'], 'main_findings': ["L'AP mesuré sur LVIS v0.5 val ne se transfère pas directement à l'ensemble test en raison de biais liés à la taille de l'ensemble d'évaluation", "Les ensembles d'évaluation de plus petite taille tendent à surestimer l'AP, un phénomène plus marqué pour les catégories rares, ce qui affecte davantage LVIS que COCO"]}

## Conclusions

Contrairement aux jeux de données de détection équilibrés en classes, où l'AP se transfère presque parfaitement entre petits ensembles de validation et ensembles de test plus larges, un déséquilibre de classe important introduit un biais dans l'AP estimé sur des ensembles d'évaluation plus petits par rapport à des ensembles plus larges. Ce biais se manifeste empiriquement par une AP plus élevée sur val v0.5 que sur test v0.5. Bien qu'un petit ensemble de validation ait été inévitable pour LVIS v0.5, cette analyse pourrait conduire à étendre l'ensemble de validation avec davantage d'images dans la version v1.

## Annotation quality and complexity relative to experts.

|  |  | mask IoU | boundary quality |  | annotation | boundary complexity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dataset | comparison | mean | median | mean | median | dataset | source | mean | median |
| COCO | vs. experts expert1 vs. expert2 | 0.83 -0.87 0.91 -0.95 | 0.88 -0.91 0.96 -0.98 | 0.77 -0.82 0.92 -0.96 | 0.79 -0.88 0.97 -0.99 | COCO | dataset experts | 5.59 -6.04 6.94 -7.84 | 5.13 -5.51 5.86 -6.80 |
| ADE20K | dataset vs. experts expert1 vs. expert2 | 0.84 -0.88 0.90 -0.94 | 0.90 -0.93 0.95 -0.97 | 0.83 -0.87 0.90 -0.95 | 0.84 -0.92 0.99 -1.00 | ADE20K | dataset experts | 6.00 -6.84 6.34 -7.43 | 4.79 -5.31 4.83 -5.53 |
| LVIS | dataset vs. experts expert1 vs. expert2 | 0.90 -0.92 0.93 -0.96 | 0.94 -0.96 0.96 -0.98 | 0.87 -0.91 0.91 -0.96 | 0.93 -0.98 0.97 -1.00 | LVIS | dataset experts | 6.35 -7.07 7.13 -8.48 | 5.44 -6.00 5.91 -6.82 |
| (a) For each metric (mask IoU, boundary quality) and each statistic (mean, median), we show | (b) Comparison of annotation complexity. Boundary |
| a bootstrapped 95% confidence interval. LVIS has the highest quality across all measures. | complexity is perimeter divided by square root area [1]. |

## 8. Analysis of AP a function of different data sizes. Best viewed digitally. COCO-trained Mask R-CNN evaluated on LVIS annotations. Both annotations yield similar AP values.

| Mask R-CNN | test anno. | box AP | mask AP |
| --- | --- | --- | --- |
| ResNet-50-FPN | COCO | 38.2 | 34.1 |
| model id: 35859007 | LVIS | 38.8 | 34.4 |
| ResNet-101-FPN | COCO | 40.6 | 36.0 |
| model id: 35861858 | LVIS | 40.9 | 36.0 |
| ResNeXt-101-64x4d-FPN | COCO | 47.8 | 41.2 |
| model id: 37129812 | LVIS | 48.6 | 41.7 |

## Dataset Simulations. For insight into how AP changes with positive and negative sets sizes |P c | and |N c |, we randomly sample smaller evaluation sets (20 times) from COCO val2017 and recompute AP. In Fig. 8a we use all positive instances for evaluation, but vary |N c | between 50 and 5k. AP decreases somewhat (∼2% absolute) as we increase the number of negative images as the ratio of negative to positive examples grows with fixed |P c | and increasing |N c |. Next, in Fig. 8b we set |N c | = 50 and vary |P c |. We observe that even with a small positive set size of 80, AP is similar to the baseline with low variance.

| With |
| --- |
| smaller positive sets (down to 5) variance increases, but the |
| AP gap from 1st to 3rd quartile remains below 2% absolute. |
| A curious upward bias in AP appears, which we investigate |
| in §C.2. These simulations together with COCO detectors |
| tested on LVIS (Tab. 2) indicate that including smaller eval- |
| uation sets for each category is viable for evaluation. |

## Mask R-CNN with repeat factor sampling (with best settings from Table3a). The frequency threshold t controls the degree of resampling of rare categories (t=0 gives no resampling). Setting t>0 substantially improves APr and t=0.001 gives best overall results. The last row presents class aware sampling (CAS), an alternate oversampling method

| score thr det/img | AP | APr | APc | AP f | AP bb |
| --- | --- | --- | --- | --- | --- | --- |
| 0.050 | 100 | 14.8 | 0.8 | 10.9 | 25.3 | 14.8 |
| 0.050 | 300 | 15.7 | 0.8 | 12.1 | 26.1 | 15.6 |
| 0.001 | 300 | 20.8 | 3.3 | 20.7 | 27.9 | 20.3 |
| 0.000 | 300 | 20.9 | 3.4 | 20.9 | 27.9 | 20.4 |
| 0.050 | 100 | 14.8±0.19 0.6±0.21 11.0±0.36 25.2±0.10 14.8±0.17 |
| 0.000 | 300 | 21.0±0.17 3.2±0.35 21.3±0.45 27.7±0.12 20.5±0.21 |
| (a) Mask R-CNN baselines (ResNet-50-FPN backbone). Top rows: ad- |
| justing two inference-time hyper-parameters, the minimum score thresh- |
| old and the number of detections per image, leads to a gain of 6.1 AP over |
| the baseline using standard COCO hyper-parameters (row 1). The last |
| two rows show the mean and standard deviation from five training runs. |
| t | AP | APr | APc |  | AP f |
| 0 | 21.0±0.17 | 3.2±0.35 | 21.3±0.45 | 27.7±0.12 |
| 0.0001 | 21.2±0.14 | 4.5±0.47 | 21.5±0.37 | 27.6±0.14 |
| 0.0010 | 23.2±0.21 | 13.4±0.80 | 23.2±0.32 | 27.1±0.07 |
| 0.0100 | 21.8±0.25 | 9.8±1.27 | 22.7±0.48 | 25.6±0.13 |
| 0.1000 | 21.3±0.24 | 9.6±0.83 | 21.7±0.32 | 25.5±0.10 |
| CAS | 18.7±0.46 | 8.5±1.56 | 19.0±0.45 | 22.3±0.19 |
| (b) enhancement |  | AP | APr | APc | AP f |
| Table 3b best |  | 23.2±0.21 13.4±0.80 23.2±0.32 27.1±0.07 |
| + scale jitter |  | 24.4±0.06 14.5±0.67 24.3±0.37 28.4±0.12 |
| + ResNet-101 |  | 26.0±0.18 15.8±0.95 26.1±0.21 29.8±0.22 |
| + ResNeXt-101-32×8d 27.1±0.43 15.6±1.14 27.5±0.77 31.4±0.12 |
|  |  |  |  |  |  | 5 |

## Table 3c with a final validation AP of 27.1%.

| Percent of categories | 0 50 100 | val v0.5 15.6% 36.8% 47.6% | test v0.5 28.6% 29.5% 41.9% | rare common frequent | train v0.5 25.6% 36.9% 37.5% |
| --- | --- | --- | --- | --- | --- |
|  | 0 | 10000 20000 30000 40000 50000 60000 |
|  |  |  | Subset size (images) |  |  |
| Figure 12. The distribution of rare, common, and frequent cate- |
| gories (defined w.r.t. train v0.5) within random image subsets |
| of a given size changes as a function of that size. The shaded |
| region (imperceptible without zoom) illustrates one standard devi- |
| ation around the mean over 10 draws of subsets for each size. |

## AP bb @75 of a detector on three COCO categories when evaluated on random subsets of different sizes. Toasters are rare (fc = 0.002) while cats and dining tables appear more frequently. As in simulation, the AP can decreases with larger test set size, especially for rare categories.Figure13. AP bias as the size of the evaluation set is varied. Fixed Mask R-CNN model (Table3bbest + scale jitter) evaluated on different size subsets of test v0.5 (average over 30 random subsets). AP on the 5k subset is similar to AP on val v0.5. As we increase subset size we observe a systematic decrease in all AP metrics consistent with the simulated and observed bias described in the main text. We compare how AP transfers for three different models (Table3c) from val v0.5 to test v0.5. All AP metrics decrease but the ranking of the models remains consistent across val and test.

|  |  | Trained detector |  |
| --- | --- | --- | --- | --- | --- |
|  |  | cat, fc = 0.037 |  |  |  |
|  |  | toaster, fc = 0.002 |  |  |
|  |  | dining table, fc = 0.100 |  |  |
| (b) subset size AP APr APc AP f 5k 24.8±0.51 11.5±1.71 25.5±0.86 30.1±0.28 10k 22.1±0.31 10.5±0.66 22.9±0.56 29.2±0.20 15k 20.8±0.23 10.0±0.54 21.7±0.37 28.9±0.11 20k (full) 18.4 8.8 18.7 27.2 ResNet-50 ResNet-101 (a) model ResNeXt-101-32×8d | eval. set val test val test val test | AP 24.4 18.4 26.0 20.0 27.1 20.5 | APr 14.5 8.8 15.8 9.4 15.6 9.8 | APc 24.3 18.7 26.1 21.0 27.5 21.1 | AP f 28.4 27.2 29.8 28.7 31.4 30.0 |
| (b) |  |  |  |  |  |
