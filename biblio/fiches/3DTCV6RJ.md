# Adapting SAM2 Model from Natural Images for Tooth Segmentation in Dental Panoramic X-Ray Images.

**Auteurs** : Zifeng Li, Wenzhong Tang, Shijun Gao, Yanyang Wang, Shuai Wang
**Année** : 2024
**DOI** : 10.3390/e26121059

## Résumé

Dental panoramic X-ray imaging, due to its high cost-effectiveness and low radiation dose, has become a widely used diagnostic tool in dentistry. Accurate tooth segmentation is crucial for lesion analysis and treatment planning, helping dentists to quickly and precisely assess the condition of teeth. However, dental X-ray images often suffer from noise, low contrast, and overlapping anatomical structures, coupled with limited available datasets, leading traditional deep learning models to experience overfitting, which affects generalization ability. In addition, high-precision deep models typically require significant computational resources for inference, making deployment in real-world applications challenging. To address these challenges, this paper proposes a tooth segmentation method based on the pre-trained SAM2 model. We employ adapter modules to fine-tune the SAM2 model and introduce ScConv modules and gated attention mechanisms to enhance the model's semantic understanding and

## Méthodologie

{'study_design': "Étude méthodologique/computationnelle : adaptation du modèle pré-entraîné SAM2 via des modules adaptateurs, intégration de modules ScConv et d'attention à portes dans les connexions de saut (skip connections), formant le modèle S2AgScUNet ; puis distillation de connaissances du modèle S2AgScUNet (enseignant) vers un modèle léger LightUNet (élève)", 'intervention': "Modèle S2AgScUNet : encodeur SAM2 pré-entraîné affiné avec des modules adaptateurs, modules ScConv et mécanismes d'attention à portes ; puis distillation de connaissances vers LightUNet", 'control': 'Modèle UNet traditionnel utilisé comme comparaison', 'primary_outcomes': ['Précision de segmentation (IoU)', 'Robustesse du modèle avec jeux de données limités'], 'secondary_outcomes': ['Nombre de paramètres du modèle', "Temps d'inférence", 'Faisabilité de déploiement sur dispositifs de périphérie (edge devices)'], 'statistical_methods': [], 'duration': None, 'setting': 'Expérimentation computationnelle sur le jeu de données UFBA-UESC'}

## Résultats

{'quantitative': [{'outcome': "Comparaison des paramètres et du temps d'inférence de LightUNet par rapport à UNet", 'value': "1.6% des paramètres, 24.0% du temps d'inférence", 'unit': 'pourcentage', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'LightUNet achieves comparable performance to UNet, but with only 1.6% of its parameters and 24.0% of the inference time, demonstrating its feasibility for deployment on edge devices.'}, {'outcome': 'Nombre de paramètres de LightUNet vs UNet', 'value': '490 000 (LightUNet) vs 31,05 millions (UNet)', 'unit': 'nombre de paramètres', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': "we used knowledge distillation to achieve performance comparable to the UNet model while reducing the number of parameters to only 490,000, compared to UNet's 31.05 million, enabling deployment on edge devices."}], 'qualitative_findings': ["Les valeurs alpha (métrique basée sur les poids du modèle, théorie de Charles H. Martin) montrent que deux composants d'UNet dépassent 6 (indiquant un surapprentissage potentiel), tandis que les trois composants de S2AgScUNet se situent entre 2 et 6, ce qui indique une meilleure généralisation."], 'main_findings': ["S2AgScUNet surpasse significativement le modèle UNet traditionnel sur plusieurs métriques telles que l'IoU", "L'introduction de SAM2 atténue efficacement les problèmes de surapprentissage liés aux petits jeux de données dans le domaine de la segmentation dentaire", "LightUNet atteint une performance comparable à UNet avec seulement 1,6% de ses paramètres et 24,0% de son temps d'inférence"]}

## Conclusions

Le modèle S2AgScUNet proposé améliore efficacement la performance de segmentation des dents en intégrant l'encodeur SAM2 pré-entraîné, le module ScConv et l'attention à portes dans les connexions de saut S2AgScUNet surpasse le modèle UNet traditionnel sur plusieurs métriques, notamment l'IoU, sur le jeu de données UFBA-UESC La capacité d'apprentissage hiérarchique des caractéristiques de SAM2 améliore significativement la robustesse du modèle, en particulier sur les jeux de données à petit échantillon, en réduisant le surapprentissage La distillation de connaissances permet d'obtenir une performance comparable à UNet tout en réduisant le nombre de paramètres à seulement 490 000 (contre 31,05 millions pour UNet), permettant un déploiement sur des dispositifs de périphérie

## based on the pre-trained SAM2 model: This

|  | modules were introduced before the |
| --- | --- |
|  | skip connections to reduce redundancy in feature extraction. We also applied gated |
|  | attention in the skip connections to further enhance detail segmentation, resulting in a |
|  | model suitable for small-sample dental segmentation datasets, named S2AgScUNet. |
|  | Experimentally, on the UFBA-UESC dataset [3], the S2AgScUNet model achieved an |
|  | IoU score of 0.8612, surpassing the 0.8477 achieved by the UNet model. |
| • | We employ a knowledge distillation approach to create a more efficient model suitable |
|  | for practical deployment. We use the fine-tuned model as the teacher model and then |
|  | create a lightweight model called LightUNet, which has the same architecture as the |
|  | UNet model but only 0.016 times its parameters. The inference time on the entire test |
|  | set is only 0.24 times that of UNet. |
|  | In conclusion, this work mainly makes the following contributions: |
| • | Proposed S2AgScUNet paper introduces |
|  | S2AgScUNet, which leverages the pre-trained SAM2 model as an encoder, combined |
|  | with ScConv modules and gated attention mechanisms, providing an effective solution |
|  | for dental panoramic X-ray image segmentation under limited sample conditions. |
| • | Effectively |

## alleviated the overfitting problem in tooth segmentation: By

| incorpo- |
| --- |
| rating the pre-trained SAM2 model with hierarchical feature learning capabilities, |
| the proposed method significantly reduces overfitting in dental X-ray small-sample |
| datasets, enhancing both the model's generalization ability and robustness. |
| • |

## Significant improvement in segmentation performance: Experimental results

| on |
| --- |
| the UFBA-UESC dataset demonstrate that the S2AgScUNet model significantly out- |
| performs the traditional UNet model in multiple metrics, such as IoU and Dice, |
| particularly excelling in capturing details and segmenting complex structures. |
| • |

## Efficient deployment on edge devices using knowledge distillation: To facilitate

| deployment on edge devices, we utilized knowledge distillation to achieve compa- |
| --- |
| rable performance to the UNet model, while reducing the parameter count to only |
| 0.49 million compared to UNet's 31.05 million parameters, making our model more |
| efficient and lightweight. |

## Description of the UFBA-UESC dataset.

| Category | 32 Teeth | Restoration Dental Appliance | Images | Used Images |
| --- | --- | --- | --- | --- |
| 1 | ✓ | ✓ | 73 | 24 |
| 2 | ✓ | ✓ | 220 | 72 |
| 3 | ✓ |  | 45 | 15 |
| 4 | ✓ |  | 140 | 32 |
| 5 |  | ✓ | 120 | 37 |
| 6 |  | ✓ | 170 | 30 |
| 7 |  | ✓ | 115 | 33 |
| 8 |  | ✓ | 457 | 140 |
| 9 |  |  | 45 | 7 |
| 10 |  |  | 115 | 35 |
| Total |  |  | 1500 | 425 |

## Performance comparison among different models. The bold values represent the best performance for each metric. The S2AgScUNet model achieved the best results in all performance metrics. Meanwhile, the lightweight model LightUNet, with significantly reduced parameters and computational complexity, still achieved comparable performance to the UNet model. The parameter count and computational complexity of the S2ScAgUNet model are not comparable due to the use of a large pre-trained model, and therefore, we used "N/A" in the table to represent these metrics. "P": Params; "F": FLOPs.

| Model | P(M) | F(G) | IOU | Dice | Precision | Recall | F1 Score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UNet | 31.05 198.66 | 0.8477 | 0.9176 | 0.9188 | 0.9164 | 0.9176 |
| SegFormer | 13.68 | 15.40 | 0.8196 | 0.9009 | 0.8940 | 0.9079 | 0.9009 |
| MaNet | 35.86 | 54.18 | 0.8257 | 0.9046 | 0.9074 | 0.9018 | 0.9046 |
| CeNet | 13.40 126.98 | 0.8460 | 0.9165 | 0.9205 | 0.9126 | 0.9165 |
| S2AgScUNet | N/A | N/A | 0.8612 | 0.9254 | 0.9239 | 0.9270 | 0.9254 |
| LightUNet | 0.49 | 3.20 | 0.8443 | 0.9156 | 0.9160 | 0.9151 | 0.9156 |

### Formule


$$X i ∈ R C i × H 2 i+1 × W 2 i+1 , (i ∈ {1, 2, 3, 4})$$

### Formule


$$Y A g = σ(W R ReLu(W S X S + W D X D )) ⊙ X D(2)$$

### Formule


$$DecoderBlock(X) = ReLU(BN(Conv(ReLU(BN(Conv(X))))))(3)$$

### Formule


$$L CE = - N ∑ i=1 y i log( ŷi )(4)$$

### Formule


$$L KD = α • L CE (y, ŷs ) + (1 -α) • T 2 • L KL (σ( ŷt /T), σ( ŷs /T))(5)$$

### Formule


$$IoU = TP TP + FP + FN(6)$$

### Formule


$$Dice = 2 × TP 2 × TP + FP + FN(7)$$

### Formule


$$Precision = TP TP + FP(8)$$

### Formule


$$Recall = TP TP + FN(9)$$

### Formule


$$F1 Score = 2 × Precision × Recall Precision + Recall(10)$$
