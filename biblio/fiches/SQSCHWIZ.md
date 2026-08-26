# Cobb Angle Measurement of Spine from X-Ray Images Using Convolutional Neural Network

**Auteurs** : Ming‐Huwi Horng, Chan‐Pang Kuok, Min-Jun Fu, Chii-Jen Lin, Yung‐Nien Sun
**Année** : 2019
**DOI** : 10.1155/2019/6357171

## Résumé

Scoliosis is a common spinal condition where the spine curves to the side and thus deforms the spine. Curvature estimation provides a powerful index to evaluate the deformation severity of scoliosis. In current clinical diagnosis, the standard curvature estimation method for assessing the curvature quantitatively is done by measuring the Cobb angle, which is the angle between two lines, drawn perpendicular to the upper endplate of the uppermost vertebra involved and the lower endplate of the lowest vertebra involved. However, manual measurement of spine curvature requires considerable time and effort, along with associated problems such as interobserver and intraobserver variations. In this article, we propose an automatic system for measuring spine curvature using the anterior-posterior (AP) view spinal X-ray images. Due to the characteristic of AP view images, we first reduced the image size and then used horizontal and vertical intensity projection histograms to define the region of interest of the spine which is then cropped for sequential processing. Next, the boundaries of the spine, the central spinal curve line, and the spine foreground are detected by using intensity and gradient information of the region of interest, and a progressive thresholding approach is then employed to detect the locations of the vertebrae. In order to reduce the influences of inconsistent intensity distribution of vertebrae in the spine AP image, we applied the deep learning convolutional neural network (CNN) approaches which include the U-Net, the Dense U-Net, and Residual U-Net, to segment the vertebrae. Finally, the segmentation results of the vertebrae are reconstructed into a complete segmented spine image, and the spine curvature is calculated based on the Cobb angle criterion. In the experiments, we showed the results for spine segmentation and spine curvature; the results were then compared to manual measurements by specialists. The segmentation results of the Residual U-Net were superior to the other two convolutional neural networks. The one-way ANOVA test also demonstrated that the three measurements including the manual records of two different physicians and our proposed measured record were not significantly different in terms of spine curvature measurement. Looking forward, the proposed system can be applied in clinical diagnosis to assist doctors for a better understanding of scoliosis severity and for clinical treatments.

## Méthodologie

{'study_design': "Système automatique en quatre étapes : isolation de la région spinale (redimensionnement de l'image, histogrammes de projection d'intensité horizontale/verticale pour définir la région d'intérêt), détection des vertèbres par seuillage progressif à partir des informations d'intensité et de gradient, segmentation des vertèbres par CNN (comparaison de trois architectures : U-Net, Dense U-Net, Residual U-Net), puis reconstruction de l'image segmentée et calcul de l'angle de Cobb", 'intervention': "Application de trois architectures de réseaux de neurones convolutifs (U-Net, Dense U-Net, Residual U-Net) pour la segmentation automatique des vertèbres, suivie du calcul automatique de l'angle de Cobb", 'control': "Mesures manuelles de l'angle de Cobb réalisées deux fois (à t=1 et t=2) par deux orthopédistes différents", 'primary_outcomes': ['Qualité de la segmentation des vertèbres (comparaison des trois CNN)', 'Angle de Cobb calculé automatiquement vs mesures manuelles'], 'secondary_outcomes': [], 'statistical_methods': ['Analyse de variance à un facteur (one-way ANOVA)', 'Corrélation de rang de Spearman', 'Coefficient de similarité de Dice (DSC) pour évaluer la segmentation', 'Moyenne ± écart-type avec intervalle de confiance à 95%'], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'Comparaison des trois mesures (deux orthopédistes + système proposé) de la courbure spinale', 'value': None, 'unit': 'degrés (angle de Cobb)', 'confidence_interval': '95% confidence interval (mentionné en note du Tableau 6, valeurs non fournies dans le texte disponible)', 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion / Tableau 6', 'source_quote': 'e one-way ANOVA test also demonstrated that the three measurements including the manual records of two different physicians and our proposed measured record were not significantly different in terms of spine curvature measurement.'}], 'qualitative_findings': [], 'main_findings': ['Les résultats de segmentation du Residual U-Net étaient supérieurs à ceux des deux autres réseaux de neurones convolutifs testés (U-Net et Dense U-Net)', "Le test ANOVA à un facteur n'a montré aucune différence significative entre les trois mesures (deux orthopédistes et le système proposé) pour la mesure de la courbure spinale"]}

## Conclusions

Un système de mesure automatique pour évaluer la sévérité de la scoliose a été proposé, comprenant trois parties principales : isolation de la colonne vertébrale, segmentation des vertèbres, et mesure de l'angle de Cobb Le Residual U-Net a montré de meilleures performances de segmentation que le U-Net et le Dense U-Net Le système proposé n'est pas significativement différent des mesures manuelles de spécialistes et pourrait être utilisé en pratique clinique pour aider les médecins à évaluer la sévérité de la scoliose

## Definition of Cobb angle

| Cobb angle | Definition |
| --- | --- |
| 0 °-10 °Spinal curve |
| 10 °-20 °Mild scoliosis |
| 20 °-40 °Moderate scoliosis |
| >40 °Severe scoliosis |

## Figure 10: U-Net architecture of the proposed method.

|  | 1 64 64 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | 128 | 64 | 64 2 |
| 572 × 572 Input image tile | 570 × 570 | 568 × 568 |  |  |  |  | 392 × 392 | 390 × 390 | 388 × 388 | 388 × 388 | Output segmentation map |
|  |  |  |  | 128 | 128 |
|  |  |  |  |  |  |  |  | 256 128 |
|  |  |  | 284 2 | 282 2 | 280 2 |  | 200 2 | 198 2 | 196 2 |
|  |  |  |  |  |  |  | 256 256 | 512 256 |
|  |  |  |  |  | 140 2 | 138 2 | 136 2 | 104 2 | 102 2 | 100 2 |
|  |  |  |  |  |  |  |  | 68 2 | 66 2 512 512 64 2 | 1024 | 56 2 | 1024 | 54 2 512 | 52 2 |
|  |  |  |  |  |  |  |  | 32 2 | 30 2 | 28 2 |
|  | Conv 3 × 3, ReLU |  | Up-conv 2 × 2 |
|  | Copy and crop |  |  | Conv 1 × 1 |
|  | Max-pooling 2 × 2 |
|  |  |  |  |  |  |  |  | Figure 9: e original architecture of U-Net [19]. |
| 1 | 64 | 64 |  |  |  |  | 64 + 64 64 64 1 |
| 256 × 128 |  |  |  |  |  |  |  | 256 × 128 |
|  |  |  |  | 128 128 | 128 + 128 128 |
| 128 × 64 |  |  |  |  |  |  | 128 × 64 |
|  |  |  |  |  |  |  |  | 256 | 256 | 256 + 256 | 256 |
|  |  |  | 64 × 32 |  |  | 64 × 32 |
|  |  |  |  |  |  |  |  | 512 |
|  |  |  |  |  |  |  |  | 32 × 16 |
|  | Conv 3 × 3, ReLU (+ batch norm) | Upsampling |
|  | Conv 1 × 1 |  |  |  | Max-pooling 2 × 2 |
|  | Concatenation |  |

## Dice similarity coefficient (DSC) from 5-fold cross-validation of U-Net, Residual U-Net, and Dense U-Net.

| k-fold | Dice similarity coefficient (DSC) U-Net Residual U-Net Dense U-Net |
| --- | --- | --- | --- |
| k � 1 | 0.940 ± 0.036 | 0.952 ± 0.023 | 0.947 ± 0.028 |
| k � 2 | 0.942 ± 0.032 | 0.951 ± 0.029 | 0.947 ± 0.029 |
| k � 3 | 0.942 ± 0.033 | 0.952 ± 0.025 | 0.949 ± 0.028 |
| k � 4 | 0.941 ± 0.034 | 0.949 ± 0.030 | 0.947 ± 0.026 |
| k � 5 | 0.942 ± 0.035 | 0.952 ± 0.028 | 0.947 ± 0.030 |
| Average ± std. | 0.941 ± 0.034 | 0.951 ± 0.027 | 0.948 ± 0.028 |
| Parameter size 1.21 million | 1.19 million | 1.20 million |
| Training time | 0.34 hour | 0.77 hour | 2.33 hour |
| Testing time (each image) | 0.03 second | 0.05 second | 0.07 second |

## Results of spine curvature with Cobb method and manual method.

|  |  |  | Observer 1 (expert) |  |  |  | Observer 2 (novice) |  | Cobb method (MBR) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Image | Upper vertebrae t � 1 t � 2 t � 1 t � 2 Lower vertebrae | Cobb angle t � 1 t � 2 | Upper vertebrae t � 1 t � 2 t � 1 t � 2 Lower vertebrae | Cobb angle t � 1 t � 2 | Upper vertebrae | Lower vertebrae | Cobb angle |
| 1 | T8 | T8 | L2 | L2 | -16.8 -16.9 | T8 | T8 | L1 | L1 | -15.0 -15.2 | T8 | L5 | -20.1 |
| 2 | T6 | T9 | L1 | L1 | 6.4 | 6.1 | T10 | T10 | L1 | L1 | 13.7 | 13.7 | T6 | T12 | 7.8 |
| 3 | T2 | T10 | L1 | L2 | 9.9 | 6.2 | T4 | T4 | L2 | L2 | 11.6 | 11.6 | T3 | L2 | 10.1 |
| 4 | T9 | T10 | L4 | L4 | 11.9 | 16.9 | T9 | T9 | L4 | L4 | 13.9 | 13.9 | T11 | L4 | 15.9 |
| 5 | T11 | T10 | L4 | L4 | 15.9 | 14.5 | T11 | T11 | L4 | L4 | 11.6 | 11.6 | T12 | L4 | 9.1 |
| 6 | T11 | T9 | L4 | L4 | -19.2 -16.8 T10 | T10 | L4 | L4 | -15.1 -15.1 | T11 | L3 | -15.1 |
| 7 | T12 | T11 | L4 | L4 | -8.1 | -12.3 | T9 | T9 | L4 | L4 | -12.0 -12.0 | T6 | L2 | -5.2 |
| 8 | T12 | T11 | L4 | L4 | -9.1 | -8.2 | T9 | T9 | L4 | L4 | -13.5 -13.5 | T12 | L2 | -11.0 |
| 9 | T10 | T10 | L4 | L4 | -19.8 -15.6 T11 | T11 | L4 | L4 | -20.6 -20.6 | T9 | L3 | -14.8 |
| 10 | T11 | T12 | L4 | L4 | 10.2 | 11.0 | T12 | T12 | L4 | L4 | 10.9 | 10.9 | T12 | L3 | 10.8 |
| 11 | T5 | - | L1 | - | -8.4 | 0 | T7 | T7 | L2 | L2 | -4.2 | -4.2 | T1 | T12 | -7.2 |
| 12 | T5 | T5 | L2 | L1 | 13.5 | 8.7 | T4 | T4 | L3 | L3 | 9.3 | 9.3 | T1 | L2 | 11.1 |
| 13 | T10 | T10 | L4 | L4 | 15.1 | 14.0 | T10 | T10 | L4 | L4 | 14.4 | 14.4 | T9 | L5 | 13.5 |
| 14 | T9 | T9 | L4 | L4 | -15.4 -12.1 T10 | T10 | L4 | L4 | -13.8 -13.8 | T2 | L5 | -14.2 |
| 15 |  |  | No scoliosis |  |  | T4 | T4 | T12 | T12 | -7.4 | -7.4 | T4 | T10 | -7.7 |
| 16 | T9 | T11 | L4 | L4 | -14.2 -15.0 | T7 | T7 | L4 | L4 | -20.2 -20.2 | T7 | L4 | -18.9 |
| 17 | T1 | T4 | T7 | T12 | 5.9 | 8.4 | T2 | T2 | T12 | T12 | 13.4 | 13.6 | T2 | T12 | 11.3 |
| 18 | T7 | T6 | L1 | L3 | 14.7 | 8.3 | T6 | T6 | L4 | L4 | 7.0 | 7.1 | T9 | L1 | 7.6 |
| 19 | T11 | T9 | L5 | L5 | -6.9 | -9.6 | T4 | T4 | L5 | L5 | -11.5 -11.7 | T2 | L5 | -12.4 |
| 20 | T3 | T2 | T8 | T11 | 7.1 | 8.5 | T4 | T4 | T6 | T6 | 8.8 | 8.5 | T3 | T6 | 9.8 |
| 21 | T12 | T10 | L5 | L4 | 11.1 | 9.9 | C3 | C3 | L2 | L2 | 15.3 | 16.2 | T3 | L3 | 13.8 |
| 22 | T7 | T7 | L4 | L4 | 12.9 | 13.0 | T2 | T2 | L4 | L4 | 16.8 | 16.9 | T3 | L3 | 18.1 |
| 23 | T8 | T8 | L3 | L4 | 11.3 | 13.8 | T11 | T11 | L5 | L5 | 15.5 | 15.6 | T11 | L3 | 9.4 |
| 24 | T7 | T9 | L4 | L4 | -14.1 -14.0 | T5 | T5 | L5 | L5 | -21.8 -22.1 | T2 | L3 | -13.5 |
| 25 | T9 | T8 | L3 | L3 | -16.2 -14.5 | T6 | T6 | L3 | L3 | -10.3 | -9.9 | T11 | L2 | -10.7 |
| 26 | T8 | T8 | L3 | L3 | -8.2 | -8.0 | T7 | T7 | L2 | L2 | -6.4 | -6.3 | T2 | L2 | -5.6 |
| 27 | T5 | T5 | L3 | L4 | -17.3 -17.3 | T5 | T5 | L3 | L3 | -15.8 -15.0 | T1 | L3 | -15.2 |
| 28 | T11 | T11 | L4 | L3 | 18.4 | 15.7 | T12 | T12 | L4 | L4 | 22.4 | 23.1 | T12 | L4 | 16.6 |
| 29 |  |  | No scoliosis |  |  | T3 | T3 | T10 | T10 | -5.2 | -5.1 | T2 | L4 | -6.6 |
| 30 | T9 | T9 | L4 | L4 | -11.7 | -9.9 | T5 | T5 | L4 | L4 | -14.2 -14.1 | T6 | L4 | -8.7 |
| 31 | T11 | T12 | L4 | L4 | -6.9 | -7.7 | T3 | T3 | L1 | L1 | 10.0 | 10.1 | L1 | L4 | -7.4 |
| 32 | T11 | T10 | L4 | L4 | -5.9 | -6.0 | T5 | T5 | L5 | L5 | -6.2 | -7.1 | T1 | L3 | -9.1 |
| 33 | T9 | T9 | L4 | L4 | -16.7 -16.0 | T8 | T8 | L4 | L4 | -14.0 -13.3 | T11 | L4 | -12.5 |
| 34 | T12 | T12 | L4 | L4 | 10.3 | 12.1 | T12 | T12 | L4 | L4 | 10.0 | 9.7 | T1 | L3 | 9.9 |
| 35 | T5 | T7 | L1 | L2 | 15.7 | 16.4 | T5 | T5 | L1 | L1 | 17.0 | 17.9 | T5 | L1 | 13.8 |

## e statistical data of a MBR Cobb measurement.

| Variable | Observer (expert) | Observer (novice) | MBR (proposed method) |
| --- | --- | --- | --- |
| Cobb's angle | -0.703 ± 12.552 (-19.8 to 18.4) | -0.106 ± 13.582(-21.8 to 22.4) | -0.694 ± 12.091(-20.1 to 18.1) |
| Intrareliability (ICC) | 0.936 (expert-novice) | 0.9710 (expert-MBR) | 0.940 (novice-MBR) |
| Pearson correlation coefficient | 0.944 (expert-novice) | 0.971 (expert-MBR) | 0.948 (novice-MBR) |

### Formule


$$f t (y) � 0, if p t (y) > 0, 1, otherwise, 􏼨(1)$$

### Formule


$$P(y) � 􏽘 15 t�1 f t (y).$$

### Formule


$$h x l 􏼁 � W T * x l + b,(3)$$

### Formule


$$F x l , w l 􏼁 � f h x l 􏼁 􏼁 � max 0, h x l 􏼁 􏼁,(4)$$

### Formule


$$x l+1 � x l + F x l , w l,k 􏼐 􏼑,(5)$$

### Formule


$$x l � H l x 0 , x 1 , . . . , x l-1 􏼂 􏼃 􏼁,(6)$$

### Formule


$$L2 loss � 􏽐 N i�0 y i -h x i 􏼁 􏼁 2 N , (7$$

### Formule


$$)$$

### Formule


$$φ � max tan -1 m i -m j 1 + m i × m j 􏼠 􏼡 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼌 􏼨 􏼩, (i, j) ∈ (a, b) | a ∈ N, b ∈ N, b -a ≥ 2 and b ≤ N { }, (8$$

### Formule


$$)$$

### Formule


$$ρ � 1 - 6􏽐 n i�1 x i -y i 􏼁 2 n n 2 -1 ( ) , (10$$

### Formule


$$)$$
