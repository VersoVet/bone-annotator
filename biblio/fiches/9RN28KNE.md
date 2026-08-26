# Enhancing Diagnostic Images to Improve the Performance of the Segment Anything Model in Medical Image Segmentation

**Auteurs** : Luoyi Kong, Mohan Huang, Lingfeng Zhang, Lawrence Chan
**Année** : 2024
**DOI** : 10.3390/bioengineering11030270

## Résumé

Medical imaging serves as a crucial tool in current cancer diagnosis. However, the quality of medical images is often compromised to minimize the potential risks associated with patient image acquisition. Computer-aided diagnosis systems have made significant advancements in recent years. These systems utilize computer algorithms to identify abnormal features in medical images, assisting radiologists in improving diagnostic accuracy and achieving consistency in image and disease interpretation. Importantly, the quality of medical images, as the target data, determines the achievable level of performance by artificial intelligence algorithms. However, the pixel value range of medical images differs from that of the digital images typically processed via artificial intelligence algorithms, and blindly incorporating such data for training can result in suboptimal algorithm performance. In this study, we propose a medical image-enhancement scheme that integrates generic digital image processing and medical image processing modules. This scheme aims to enhance medical image data by endowing them with high-contrast and smooth characteristics. We conducted experimental testing to demonstrate the effectiveness of this scheme in improving the performance of a medical image segmentation algorithm.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

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
