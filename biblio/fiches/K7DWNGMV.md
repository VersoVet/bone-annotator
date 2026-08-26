# Vessel-CAPTCHA: An efficient learning framework for vessel annotation and segmentation

**Auteurs** : Vien Ngoc Dang, Francesco Galati, Rosa Cortese, Giuseppe Di Giacomo, Viola Marconetto, Prateek Mathur, Karim Lekadir, Marco Lorenzi, Ferran Prados, Maria A. Zuluaga
**Année** : 2022
**DOI** : 10.1016/j.media.2021.102263

## Résumé

Deep learning techniques for 3D brain vessel image segmentation have not been as successful as in the segmentation of other organs and tissues. This can be explained by two factors. First, deep learning techniques tend to show poor performances at the segmentation of relatively small objects compared to the size of the full image. Second, due to the complexity of vascular trees and the small size of vessels, it is challenging to obtain the amount of annotated training data typically needed by deep learning methods. To address these problems, we propose a novel annotation-efficient deep learning vessel segmentation framework. The framework avoids pixel-wise annotations, only requiring weak patch-level labels to discriminate between vessel and non-vessel 2D patches in the training set, in a setup similar to the CAPTCHAs used to differentiate humans from bots in web applications. The user-provided weak annotations are used for two tasks: 1) to synthesize pixel-wise pseudo-labels for vessels and background in each patch, which are used to train a segmentation network, and 2) to train a classifier network. The classifier network allows to generate additional weak patch labels, further reducing the annotation burden, and it acts as a noise filter for poor quality images. We use this framework for the segmentation of the cerebrovascular tree in Time-of-Flight angiography (TOF) and Susceptibility-Weighted Images (SWI). The results show that the framework achieves state-of-the-art accuracy, while reducing the annotation time by ∼77% w.r.t. learning-based segmentation methods using pixel-wise labels for training.

## Méthodologie

{'study_design': None, 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'Vessel 2D-Unet DSC (this study vs. Livne et al., 2019)', 'value': '77.66 vs. 89.0', 'unit': 'DSC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'Vessel 2D-Unet and DeepVessel-Net report lower DSC (77.66 vs. 89.0 and 76.13 vs. 81.0, respectively) than the reported in (Livne et al., 2019;Tetteh et al., 2020)'}, {'outcome': 'DeepVessel-Net DSC (this study vs. Tetteh et al., 2020)', 'value': '76.13 vs. 81.0', 'unit': 'DSC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'Vessel 2D-Unet and DeepVessel-Net report lower DSC (77.66 vs. 89.0 and 76.13 vs. 81.0, respectively) than the reported in (Livne et al., 2019;Tetteh et al., 2020)'}, {'outcome': 'Vessel 2D-Unet 95HD (this study vs. Livne et al., 2019)', 'value': '12.6 vs 47.27', 'unit': '95HD', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'for Vessel 2D-Unet our results show a better 95HD (12.6 vs 47.27) and a comparable sub-voxel µD (0.60 vs 0.38)'}, {'outcome': 'Vessel 2D-Unet µD (sub-voxel) (this study vs. Livne et al., 2019)', 'value': '0.60 vs 0.38', 'unit': 'µD', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'a comparable sub-voxel µD (0.60 vs 0.38)'}, {'outcome': "Score moyen d'évaluation visuelle des segmentations SWI par les évaluateurs", 'value': '2.57', 'unit': 'average rating score', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'Their visual judgment an average rating score of 2.57 with an agreement κ=0.75.'}, {'outcome': "Accord inter-évaluateurs (kappa) sur l'évaluation visuelle des segmentations SWI", 'value': '0.75', 'unit': "κ (Cohen's kappa)", 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'Their visual judgment an average rating score of 2.57 with an agreement κ=0.75.'}, {'outcome': "Temps supplémentaire requis pour l'annotation SWI Vessel-CAPTCHA par rapport à TOF", 'value': '38', 'unit': '% de temps en plus', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'SWI Vessel-CAPTCHA annotation requires 38% more time than in TOF (94.5±11.5).'}, {'outcome': "Temps d'annotation TOF Vessel-CAPTCHA", 'value': '94.5±11.5', 'unit': 'min (moyenne ± écart-type)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'SWI Vessel-CAPTCHA annotation requires 38% more time than in TOF (94.5±11.5).'}, {'outcome': "Réduction du temps d'annotation SWI Vessel-CAPTCHA par rapport à l'annotation pixel-wise de référence", 'value': '71', 'unit': '% de temps en moins', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'SWI Vessel-CAPTCHA accounts for 71% less time than the pixel-wise annotation baseline (327.5±20.5 min, see Fig. 7).'}, {'outcome': "Temps d'annotation pixel-wise de référence", 'value': '327.5±20.5', 'unit': 'min (moyenne ± écart-type)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'SWI Vessel-CAPTCHA accounts for 71% less time than the pixel-wise annotation baseline (327.5±20.5 min, see Fig. 7).'}], 'qualitative_findings': ['Les méthodes classiques de segmentation vasculaire (Frangi, Sato, TV) montrent une performance faible sans post-traitement manuel, ce qui est une limitation connue de ces approches.', 'Le post-traitement manuel permet un saut important de performance, notamment en supprimant les faux positifs parasites et déconnectés, ce qui se reflète dans un HD faible (le meilleur parmi toutes les méthodes) et une baisse importante du 95HD, tandis que le µD reste relativement constant.', "Le post-traitement nécessite un haut niveau d'expertise et prend du temps.", "À l'exception du HD, les méthodes basées sur l'apprentissage montrent systématiquement une meilleure performance sur l'ensemble des mesures, sans différences statistiques entre elles, Vessel-CAPTCHA rapportant les meilleurs résultats parmi toutes les méthodes.", "Cela démontre que le framework proposé peut atteindre une performance état de l'art malgré l'utilisation d'annotations moins précises.", "Les meilleures mesures basées sur la distance suggèrent que les différences de DSC pourraient provenir du protocole d'annotation de la vérité terrain, où les données pourraient inclure des vaisseaux plus distaux, donc plus fins, plus susceptibles de ne pas être segmentés.", 'Cette hypothèse est confirmée par le DSC de DeepVesselNet sur données synthétiques.', 'Dans le cadre contrôlé, les résultats rapportés sont comparables à ceux de Tetteh et al., 2020.', "Globalement, SWI est plus complexe que TOF, entraînant davantage d'erreurs observées.", 'Les segmentations SWI ont tendance à manquer les petits vaisseaux, avec également une incidence élevée de faux positifs due à des sillons (sulci) et du bruit mal segmentés.', "Les évaluateurs ont jugé plus de 50% des segmentations comme bonnes, et une seule image a été considérée comme médiocre par l'un d'eux.", "Le temps d'annotation SWI plus élevé est attendu compte tenu de la complexité accrue des scans SWI : les petits vaisseaux nécessitent plus d'effort pour être identifiés et les vaisseaux présentent souvent une apparence similaire aux sillons."], 'main_findings': ["Vessel-CAPTCHA atteint une performance état de l'art en segmentation vasculaire malgré l'utilisation d'annotations faibles (weak labels), moins précises que les annotations complètes.", "Les méthodes basées sur l'apprentissage (learning-based) surpassent de manière constante les méthodes classiques de segmentation vasculaire (Frangi, Sato, TV) sur la plupart des mesures, sauf le HD.", 'Le post-traitement manuel améliore fortement les méthodes classiques mais reste coûteux en temps et en expertise.', "Vessel-CAPTCHA réduit considérablement le temps d'annotation par rapport à l'annotation pixel-wise traditionnelle (71% de réduction pour SWI), tout en maintenant une bonne qualité de segmentation jugée par des évaluateurs (score moyen 2.57, κ=0.75)."]}

## Conclusions

Vessel-CAPTCHA est un framework d'apprentissage efficace pour l'annotation et la segmentation de vaisseaux, basé sur des clics utilisateur simples sur des patches contenant des vaisseaux, à la manière des CAPTCHA d'images Le framework atteint des performances comparables aux approches d'apprentissage profond de l'état de l'art pour la segmentation de vaisseaux cérébraux, tout en réduisant la charge d'annotation de 77% en moyenne L'utilisation d'un réseau de segmentation 2D par patch (2D-WnetSeg) plutôt que des architectures 3D ou hybrides plus complexes améliore les performances en augmentant le ratio objet-d'intérêt/taille de l'image, ce qui est validé par les résultats inférieurs obtenus par les réseaux 3D Le réseau de classification (PnetCl), entraîné avec les mêmes tags fournis par l'utilisateur, permet d'agrandir l'ensemble d'entraînement sans effort d'annotation supplémentaire et peut servir de seconde opinion pour évaluer les segmentations Le désaccord entre le réseau de segmentation et le réseau de classification pourrait servir de mesure d'incertitude pour guider la révision manuelle des segmentations par un utilisateur Le framework proposé est suffisamment général pour être étendu à d'autres structures vasculaires, d'autres structures tubulaires complexes, ou à différentes modalités d'imagerie

## Table 1

| sel segmentation, which were generated following the method |
| --- |
| proposed in (Schneider et al., 2012). The vessel labels occupy |
| 2.1% of total intensities, highlighting the problem of vessels |
| being relatively small objects within a large image volume. |
| TOF Data. We use 100 TOF scans coming from two differ- |
| ent sources. Forty-two TOF subject scans, from retrospective |

## Main properties of data used and training and validation test sizes per data type

|  | Synthetic | TOF | SWI |
| --- | --- | --- | --- |
| Dataset size | 136 | 100 | 33 |
| Volume dimensions | 325 × 304 × 600 | 560 × 560 × 117 (Set 1) 480 × 480 × 288 |
|  |  | 576 × 768 × 232 (Set 2) |  |
| Voxel spacing | 1 × 1 × 1 mm 3 | 1 × 1 × 1 mm 3 (Set 1) | 1 × 1 × 1 mm 3 |
|  |  | 0.3 × 0.3 × 0.6 mm 3 (Set 2) |  |
| |T P | (patch size 32 × 32) | 7.18M | 770K | 30.6K |
| |T M | (patch size 96 × 96) | 1.04M | 110K | 10.2K |
| 1). The remaining 68 scans were obtained from the OASIS- |  |  |
| 3 database (LaMontagne et al., 2019) with volume dimensions |  |  |
| 576 × 768 × 232 and voxel size 0.3 × 0.3 × 0.6 mm 3 (Set 2). |  |  |

## Hyper-parameter setup for baseline networks

| Network | Hyper-parameters |
| --- | --- |
| Vessel 2D-Unet batch size: 64, lr: 1e-4, dropout: 0.0 |
| DeepVesselNet batch size: 10, lr: 1e-3, decay: 0.99, cube size: |
|  | 64 |
| WS-MIL | batch size: 100, lr: 1e-4, decay: 10e-5, |
|  | c 0 =c 1 =1, α = [1e-2, . . . , 0.1], β = 0.00 |
| AffinityNet | batch size: 16, lr: 1e-1 |
| 3D-Unet | lr: 1e-4, reduced by 0.5 every 10 epochs. |
|  | Stopped at 50 epochs if no improvements in the |
|  | validation error |
| VGG-16 | batch size: 64, lr: 1e-4 |
| ResNet | batch size: 64, lr: 1e-3 |

## 3D brain vessel segmentation methods accuracy in TOF. The bold font denotes best value, with underlined values not significantly different from it (α = 0.05). Classical methods and DeepVesselNet use 3D volumes as input. Vessel 2D-Unet and our framework use 2D patches as inputs. HD, 95HD and µD are reported in voxels.

| Method | DSC (↑) | HD (↓) | 95HD (↓) | µD (↓) |
| --- | --- | --- | --- | --- |
| Frangi-NP | 54.16±8.81 81.04±18.48 14.78±13.83 2.47±2.22 |
| Sato-NP | 55.75±7.15 78.60±16.37 11.53±12.01 2.17±1.07 |
| TV-NP | 68.41±5.01 60.23±10.08 10.97±11.72 2.10±1.00 |
| Frangi-PP | 68.44±3.15 20.60±10.91 | 9.01±10.38 2.36±2.01 |
| Sato-PP | 69.01±3.67 | 21.53±9.11 | 8.86±10.09 2.10±1.01 |
| TV-PP | 70.74±3.38 | 20.11±8.45 | 8.31±8.23 2.07±1.02 |
| Vessel 2D-Unet 77.66±4.32 74.78±16.73 12.60±18.16 0.60±0.11 |
| DeepVesselNet 76.13±5.51 75.32±12.94 | 4.32±1.16 1.65±0.26 |
| Vessel-CAPTCHA 79.32±3.02 | 51.70±5.92 | 4.06±1.50 0.50±0.09 |
| NP: No post-processing, PP: Post-processing |  |  |

## Comparison with partial labeling methods using TOF. The bold font denotes best value. Our framework uses 2D patches, Pseudo-labeling image slices and 3D-Unet image volumes as input.

|  | 3D-Unet | Pseudo-labeling Vessel-CAPTCHA |
| --- | --- | --- | --- |
| DSC (↑) | 68.50±3.37 | 54.99±5.86 | 79.32±3.02 |
| HD (↓) | 76.12±8.47 | 68.50±9.58 | 51.70±5.92 |
| 95HD (↓) 15.72±2.23 | 24.19±5.25 | 4.06±1.50 |
| µD (↓) | 2.56±1.44 | 4.48±1.67 | 0.50±0.09 |

## Classification network comparison in TOF and SWI. For each row, bold font denotes the best value, with underlined values not significantly different from it (α = 0.05) PnetCl Precision 92.48±1.54 93.66±1.48 94.82±0.48 94.91±1.04 TOF Recall 87.39±4.60 93.27±1.73 94.04±0.65 94.94±1.09 F-score 88.68±3.81 93.34±1.62 94.27±0.54 94.71±1.23 Precision 82.34±1.15 80.14±1.13 82.44±1.18 82.97±1.55 SWI Recall 77.45±4.17 79.39±3.35 74.35±5.35 79.30±4.07 F-score 78.76±3.39 79.17±2.31 76.42±4.63 80.31±3.31

| VGG-16 | ResNet | 2D-UnetCl 2D- |
| --- | --- | --- |

## 2D-WnetSeg vs single Unet performance using synthetic data.

| Measure 2D-WnetSeg One 2D-Unet |
| --- | --- | --- |
| DSC (↑) | 88.77±0.90 | 86.61±1.05 |
| HD (↓) | 40.31±2.95 | 41.18±4.32 |
| 95HD (↓) | 6.74±0.48 | 7.96±0.52 |
| µD (↓) | 0.91±0.06 | 1.08±0.07 |
| 4.4.2. The Role of the Segmentation Network |

## Performance summary considering segmentation accuracy, model complexity (Params, GFLOPs), and computational (training and prediction) and user intervention time in minutes. In classical models (NL), user intervention time is measured during inference. In learning-based models, it refers to the time used during training set annotation. For accuracy measures, the bold font denotes best value, with underlined values not significantly different from it (α = 0.05). No labels, FS: Fully supervised, LS: Limited supervision, NP: No post-processing, PP: Post-processing, NA: Not Available

|  | Method | DSC (↑) | Accuracy HD (↓) 95HD (↓) | µD (↓) | Complexity (↓) Params ×10 3 GFLOPs Train Predict User Time (↓) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Frangi-NP | 54.16±8.81 81.04±18.48 14.78±13.83 2.47±2.22 |  |  |  | 25 | 0 |
|  | Sato-NP | 55.75±7.15 78.60±16.37 11.53±12.01 2.17±1.07 |  |  |  | 25 | 0 |
| NL | TV-NP Frangi-PP | 68.41±5.01 60.23±10.08 10.97±11.72 2.10±1.00 68.44±3.15 20.60±10.91 9.01±10.38 2.36±2.01 | 1 | 1 | 0 | 35 25 | 0 25 |
|  | Sato-PP | 69.01±3.67 | 21.53±9.11 | 8.86±10.09 2.10±1.01 |  |  |  | 25 | 25 |
|  | TV-PP | 70.74±3.38 | 20.11±8.45 | 8.31±8.23 2.07±1.02 |  |  |  | 35 | 25 |
|  | Vessel 2D-Unet | 77.66±4.32 74.78±16.73 12.60±18.16 0.60±0.11 | 31.38 | 15.6 | 90 |
| FS | DeepVesselNet | 76.13±5.51 75.32±12.94 | 4.32±1.16 1.65±0.26 | 0.05 | NA | 960 | < 1 | 327 |
|  | 2D-WnetSeg | 76.63±4.26 80.69±23.20 13.15±19.67 2.13±2.37 | 16.34 | 25.90 | 90 |
| LS | 3D-Unet Pseudo-labeling | 68.50±3.37 54.90±5.86 | 76.12±8.47 68.50±9.58 | 15.72±2.23 2.56±1.44 24.19±5.25 4.48±1.67 | 16.21 1669.53 31.38 15.6 1090 60 | < 1 | 327 0 |
|  | PnetCl + K-means 64.96±4.76 Vessel-CAPTCHA 79.32±3.02 | 65.82±7.99 51.70±5.92 | 16.66±3.85 2.62±0.65 4.06±1.50 0.50±0.09 | 0.62 16.34 | 0.993 25.90 | 60 90 | ∼1 75.5 <1 |
| NL: |  |  |  |  |  |  |  |  |

### Formule


$$I ∈ I of size H × W × S , for each slice X s , s ∈ [1, . . . , S ],$$

### Formule


$$D k → R, where D k is a subset of the slice domain D k ⊂ [1, H]×[1, W].$$

### Formule


$$f (U k ) = 1 ⇐⇒ ∃(i, j) ∈ D k s.t. U k (i, j) = 1. (1$$

### Formule


$$M k (i, j) =        0 if f (U k ) = 0, K M( Xk (i, j)) otherwise, (2$$

### Formule


$$)$$

### Formule


$$T I M = {X s , M s } S s=1$$

### Formule


$$T P = {T I P } I∈I ,(3)$$

### Formule


$$T M = {T I M } I∈I ,(4)$$
