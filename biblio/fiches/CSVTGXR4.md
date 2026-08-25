# Brain Tumor MRI Segmentation Method Based on Segment Anything Model

**Auteurs** : Bingyan Wei
**Année** : 2024
**DOI** : 10.18280/ria.380220

## Résumé

The precise segmentation of different types of brain tumor regions constitutes a critical task in medical image segmentation. Clinically, brain MRI contains abundant information, which can significantly assist doctors in the examination and diagnosis of brain tumor patients. With the advancement of artificial intelligence (AI) and computer technology, some foundational models have increasingly played a pivotal role in the field of computer vision. The Segment Anything Model (SAM) is a fundamental model in the realm of image segmentation, renowned for its exceptional zero-shot segmentation performance and transfer ability, achieving commendable results in natural image processing. To explore the efficacy of SAM in segmenting brain tumor MRI and address the issue of low segmentation accuracy due to uneven image grayscale, a method based on SAM feature fusion is proposed. Features fused from the Transformer and Convolutional Neural Network (CNN) are input into a mask decoder, leveraging the attention mechanism of the Transformer to more effectively capture the global relationships within images, thereby enhancing the precision of the output. Experiments have demonstrated that the method proposed in this study surpasses the segmentation performance of SAM alone, achieving precise segmentation of brain tumor MRI.

## Méthodologie

{'study_design': "Étude expérimentale comparative évaluant une méthode de segmentation basée sur SAM avec fusion de caractéristiques Transformer/CNN, comparée à SAM original (avec 2 points d'invite, 10 points d'invite, et segmentation automatique) et à d'autres modèles (U-net, Unet++, ResUnet, TransUnet) sur le jeu de données BraTS2021", 'intervention': "Ajout de couches de convolution et de mapping de caractéristiques à l'architecture originale de SAM, fusion des caractéristiques convolées avec les caractéristiques du Transformer dans l'encodeur d'image, puis injection dans le mask decoder", 'control': "SAM original (segmentation automatique et avec points d'invite), U-net, Unet++, ResUnet, TransUnet", 'primary_outcomes': ['Précision de segmentation (DSC - Dice Similarity Coefficient) sur les sous-régions ET, TC et WT'], 'secondary_outcomes': ["Effet du nombre de points d'invite sur la performance de segmentation"], 'statistical_methods': [], 'duration': None, 'setting': 'Jeu de données public BraTS2021, modalité T1'}

## Résultats

{'quantitative': [{'outcome': "Comparaison segmentation avec 2 points d'invite vs 10 points d'invite", 'value': 'Segmentation avec 10 points supérieure à 2 points', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'The segmentation results with 10 prompt points surpassed those with 2 prompt points, indicating that a greater number of prompt points leads to improved final segmentation outcomes.'}, {'outcome': 'Performance de la méthode proposée vs SAM original', 'value': 'DSC supérieur aux meilleurs résultats de segmentation obtenus', 'unit': 'DSC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'It is observed that the segmentation method of this study outperforms the original SAM prompt points and automatic segmentation methods in terms of segmentation effects, with DSC surpassing the best segmentation outcomes.'}, {'outcome': 'Performance de SAM par région tumorale (TC, WT, ET)', 'value': 'TC > WT > ET', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'SAM demonstrated the best segmentation effects on the TC, followed by the WT, and lastly the ET.'}], 'qualitative_findings': ['SAM présente de meilleures performances sur les objets ayant des contours plus nets, la TC ayant les contours les plus clairs parmi les trois régions'], 'main_findings': ['La méthode proposée (fusion Transformer + CNN dans SAM) surpasse la segmentation par SAM seul', 'Le modèle atteint ses meilleurs résultats de segmentation sur la région WT', "Augmenter le nombre de points d'invite améliore les résultats de segmentation de SAM"]}

## Conclusions

La méthode proposée, ajoutant convolution et mapping de caractéristiques à l'architecture SAM et fusionnant ces caractéristiques avec celles du Transformer dans l'encodeur d'image, permet une segmentation précise des tumeurs cérébrales La méthode proposée obtient une meilleure précision de segmentation des tumeurs cérébrales que la méthode SAM originale Augmenter le nombre de points d'invite (prompt points) de SAM améliore les résultats de segmentation

## Comparison of model segmentation results

| Method | ET | DSC TC | WT | ET | HD TC | WT | ET | ASSD TC | WT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| U-net [21] | 0.7192 | 0.7768 | 0.8106 | 29.6654 | 19.8751 | 28.3322 | 2.8832 | 2.6702 | 2.6570 |
| Unet++ [22] | 0.7015 | 0.7106 | 0.8009 | 27.9513 | 17.4712 | 27.7822 | 2.8832 | 2.6702 | 2.6570 |
| ResUnet [23] | 0.7006 | 0.7841 | 0.7816 | 28.3260 | 19.9965 | 27.9957 | 2.6780 | 2.9053 | 2.7256 |
| TransUNet [24] | 0.7439 | 0.7524 | 0.7860 | 27.1583 | 19.8313 | 28.1590 | 2.7792 | 2.6702 | 2.9205 |
| SAM 2 point | 0.3211 | 0.4194 | 0.4164 | 22.4959 | 22.9007 | 27.9233 | 2.9952 | 2.5032 | 2.9362 |
| SAM 10 point | 0.5199 | 0.6306 | 0.6453 | 16.470 | 16.3422 | 20.5195 | 2.7836 | 2.4395 | 2.5763 |
| SAM (auto) | 0.5915 | 0.7285 | 0.6989 | 12.5408 | 13.2353 | 17.2557 | 1.2528 | 2.8809 | 3.1699 |
| Our method (auto) | 0.7321 | 0.7503 | 0.8091 | 11.2536 | 18.1524 | 22.0658 | 1.1057 | 1.5216 | 1.1563 |

### Formule


$$𝐹 𝑛𝑒𝑤 𝑛 =⊕ [𝐶𝑜𝑛𝑣 3×3 (𝑅𝑒𝐿𝑈(𝐶𝑜𝑛𝑣 3×3 (𝐹 𝑛𝑒𝑤 𝑛-1 ))) , 𝐹 𝑛𝑒𝑤 𝑛-1 ](1)$$

### Formule


$$𝐹 𝑛𝑒𝑤 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 =⊕ (𝐹 𝑛𝑒𝑤 , 𝐹 𝑛𝑒𝑤 𝑛 )(2)$$

### Formule


$$𝐹 𝑠𝑝𝑎𝑡𝑖𝑎𝑙 𝑚𝑎𝑥 = 𝑀𝑎𝑥𝑝𝑜𝑜𝑙𝑖𝑛𝑔(𝐹 𝑛𝑒𝑤 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 )(3)$$

### Formule


$$𝐹 𝑚𝑎𝑝 𝑆𝑤𝑒𝑖𝑔ℎ𝑡 = 𝑅𝑒𝑠𝑎𝑝𝑒 [𝜎 [𝐶𝑜𝑛𝑣 1×1 (𝑐𝑜𝑛𝑐𝑎𝑡(𝐹 𝑠𝑝𝑎𝑡𝑖𝑎𝑙 𝑚𝑎𝑥 , 𝐹 𝑠𝑝𝑎𝑡𝑖𝑎𝑙 𝑎𝑣𝑒𝑟𝑎𝑔𝑒 ))]](5)$$

### Formule


$$𝐹 𝑛𝑒𝑤 𝑠𝑝𝑎𝑡𝑖𝑎𝑙 = ⨂[𝐹 𝑚𝑎𝑝 𝑆𝑤𝑒𝑖𝑔ℎ𝑡 , 𝐹 𝑛𝑒𝑤 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 ](6)$$

### Formule


$$𝐹 𝑓𝑢𝑠𝑖𝑜𝑛 =⊕ [𝑈𝑝 (𝑅𝑒𝐿𝑈 (𝐷𝑜𝑤𝑛(𝐹 𝑛𝑒𝑤 𝑠𝑝𝑎𝑡𝑖𝑎𝑙 ))) , 𝐹 𝑛𝑒𝑤 𝑠𝑝𝑎𝑡𝑖𝑎𝑙 ](7) 1 ( ( , ( )) ( , ( )))$$

### Formule


$$( ) ( ) A B A B s S A s S B d s S B d s S A S A S B    +  + (10)$$
