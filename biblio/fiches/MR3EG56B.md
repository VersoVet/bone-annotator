# Enhancing Diagnostic Images to Improve the Performance of the Segment Anything Model in Medical Image Segmentation

**Auteurs** : Luoyi Kong, Mohan Huang, Lingfeng Zhang, Lawrence Chan
**Année** : 2024
**DOI** : 10.3390/bioengineering11030270

## Résumé

Medical imaging serves as a crucial tool in current cancer diagnosis. However, the quality of medical images is often compromised to minimize the potential risks associated with patient image acquisition. Computer-aided diagnosis systems have made significant advancements in recent years. These systems utilize computer algorithms to identify abnormal features in medical images, assisting radiologists in improving diagnostic accuracy and achieving consistency in image and disease interpretation. Importantly, the quality of medical images, as the target data, determines the achievable level of performance by artificial intelligence algorithms. However, the pixel value range of medical images differs from that of the digital images typically processed via artificial intelligence algorithms, and blindly incorporating such data for training can result in suboptimal algorithm performance. In this study, we propose a medical image-enhancement scheme that integrates generic digital image processing and medical image processing modules. This scheme aims to enhance medical image data by endowing them with high-contrast and smooth characteristics. We conducted experimental testing to demonstrate the effectiveness of this scheme in improving the performance of a medical image segmentation algorithm.

## Méthodologie

{'study_design': "Étude comparative expérimentale évaluant différentes méthodes de prétraitement d'image (égalisation d'histogramme, ajustement de fenêtre/niveau, et méthode proposée combinant les deux par fusion pondérée) sur la performance de segmentation hépatique via MedSAM", 'intervention': "Prétraitement des images par la méthode proposée, combinant les résultats de l'amélioration globale (égalisation d'histogramme) et de l'amélioration locale (ajustement de fenêtre/largeur) de manière pondérée (image fusionnée/'blended image')", 'control': "Images prétraitées par égalisation d'histogramme seule et images prétraitées par ajustement de fenêtre (window level/width) seul", 'primary_outcomes': ['Performance de segmentation hépatique par MedSAM (IoU, dice)'], 'secondary_outcomes': ['Accuracy, precision, recall, sensitivity, F1, specificity'], 'statistical_methods': ['Comparaison de métriques de segmentation (IoU, dice coefficient, accuracy, precision, recall, sensitivity, F1, specificity) entre méthodes de prétraitement'], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': "Différence de performance : égalisation d'histogramme vs méthode proposée", 'value': 'IoU: -0.081; dice: -0.0502; accuracy: -0.0082; precision: 0.1033; recall: -0.0199; sensitivity: -0.0199; F1: 0.0502; specificity: 0.01', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The experimental results also demonstrate that histogram equalization with lower contrast performs worse in segmentation accuracy compared to higher-contrast window adjustment and the proposed method (IoU: -0.081; dice: -0.0502; accuracy: -0.0082; precision: 0.1033; recall: -0.0199; sensitivity: -0.0199; F1: 0.0502; specificity: 0.01).'}, {'outcome': 'Différence de performance : ajustement de fenêtre vs méthode proposée', 'value': 'IoU: -0.0345; dice: -0.024; accuracy: -0.0027; precision: -0.0355; recall: +0.0009; sensitivity: 0.0009; F1: -0.024; specificity: -0.0028', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'Furthermore, window adjustment, which is susceptible to edge-disturbing noise, also yields lower segmentation accuracy compared to the proposed method (IoU: -0.0345; dice: -0.024; accuracy: -0.0027; precision: -0.0355; recall: +0.0009; sensitivity: 0.0009; F1: -0.024; specificity: -0.0028).'}, {'outcome': 'Nombre de métriques où la méthode proposée obtient le meilleur score', 'value': '6 sur 8', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'Table 3 presents the performance of different liver segmentation image preprocessing methods using MedSAM. The proposed method achieves the highest scores in six out of eight evaluation metrics, only slightly lagging window adjustment in terms of recall and sensitivity.'}, {'outcome': 'Accuracy du masque de segmentation hépatique obtenu via la méthode proposée + MedSAM', 'value': '> 90%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'The liver region mask obtained through the proposed preprocessing method and MedSAM achieved an accuracy of over 90%, making it highly suitable for practical application in hospital diagnosis processes.'}], 'qualitative_findings': ["L'égalisation d'histogramme produit des masques avec la plage de valeurs de pixels la plus large, entraînant des bords flous pour la région hépatique", "L'ajustement de fenêtre est sensible au bruit interférent avec les bords, provoquant des contours de région irréguliers", 'La méthode proposée produit des masques avec des contours lisses, contrairement aux autres méthodes'], 'main_findings': ["La méthode proposée (fusion pondérée d'égalisation d'histogramme et d'ajustement de fenêtre) obtient les meilleurs scores sur 6 des 8 métriques d'évaluation", 'La méthode proposée conserve un contraste élevé tout en enrichissant les détails sombres, réduisant le bruit et fournissant des bords plus lisses', "Comparée à l'égalisation d'histogramme, la méthode proposée présente un contraste plus élevé dans la région cible et met davantage en valeur les bords et textures", "Comparée à l'ajustement de fenêtre, la méthode proposée offre un meilleur contrôle du bruit et un meilleur lissage des bords"]}

## Conclusions

La méthode de prétraitement proposée, combinant amélioration globale et locale de manière pondérée, obtient de bons résultats avec faible bruit et contraste élevé Les six métriques d'évaluation atteignent des valeurs optimales, prouvant l'efficacité de l'approche de prétraitement proposée Les avantages en termes de score IoU et coefficient dice sont les plus significatifs, indiquant un meilleur recouvrement avec la vérité terrain et moins de faux positifs Le masque de région hépatique obtenu via la méthode proposée et MedSAM atteint une précision supérieure à 90%, la rendant adaptée à une application pratique en diagnostic hospitalier La qualité des données détermine la limite supérieure de la performance du modèle ; les améliorations du modèle ne peuvent qu'approcher cette limite

## Server configuration and environment.

| Server configuration and Environment |  |
| --- | --- |
| OS | Ubuntu 22.04.3 LTS |
| CPU | 32 13th Gen Intel(R) Core(TM) i9-13900K |
| GPU | NVIDIA GeForce RTX 4090 × 2 |
| RAM | 32 GB DDR5 × 4 |

## The scores of liver segmentation using MedSAM on medical images obtained using three different preprocessing methods.

| Proposed Method |
| --- |

## Cont.

| Normalization |
| --- |

### Formule


$$1 , ,, , ( ( ) ( )$$

### Formule


$$( ) ( )) t t x y N t x y S t x y E t x y W t I I cN I cS I cE I cW I            (1)$$

### Formule


$$2 2 , exp( ( ) / ) x y N cN I k   (2)$$

### Formule


$$1 , ,, , ( ( ) ( )$$

### Formule


$$( ) ( )) t t x y N t x y S t x y E t x y W t I I cN I cS I cE I cW I           (1)$$

### Formule


$$2 2 , exp( ( ) / ) x y N cN I k   (2)$$

### Formule


$$I t+1 = I t + λ(cN x,y ∇ N (I t ) + cS x,y ∇ S (I t ) + cE x,y ∇ E (I t ) + cW x,y ∇ W (I t ))(1)$$

### Formule


$$cN x,y = exp(-∥∇ N (I)∥ 2 /k 2 ) (2) cS x,y = exp(-∥∇ S (I)∥ 2 /k 2 ) (3) cE x,y = exp(-∥∇ E (I)∥ 2 /k 2 ) (4) cW x,y = exp(-∥∇ W (I)∥ 2 /k 2 )(5)$$

### Formule


$$h(r k ) = n k(6)$$

### Formule


$$P(r k ) = h(r k ) N(7)$$

### Formule


$$s k = k ∑ j=0 P(r j ), k = 0, 1, . . . , 255(8)$$

### Formule


$$p k ← s k × (L -1)(9)$$

### Formule


$$HU = pixel × slope + intercept (10$$

### Formule


$$)$$

### Formule


$$slope = g w (11) intercept = ( w 2 -c) × g w(12)$$

### Formule


$$WindowLeveling(x) =        0, x < c -w 2 g w × x + ( w 2 -c) × g w , c -w 2 ≤ x ≤ c + w 2 255, x > c + w 2 (13)$$

### Formule


$$N × N.$$
