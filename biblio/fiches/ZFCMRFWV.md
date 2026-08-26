# A Semi-Automatic Magnetic Resonance Imaging Annotation Algorithm Based on Semi-Weakly Supervised Learning.

**Auteurs** : Shaolong Chen, Zhiyong Zhang
**Année** : 2024
**DOI** : 10.3390/s24123893

## Résumé

The annotation of magnetic resonance imaging (MRI) images plays an important role in deep learning-based MRI segmentation tasks. Semi-automatic annotation algorithms are helpful for improving the efficiency and reducing the difficulty of MRI image annotation. However, the existing semi-automatic annotation algorithms based on deep learning have poor pre-annotation performance in the case of insufficient segmentation labels. In this paper, we propose a semi-automatic MRI annotation algorithm based on semi-weakly supervised learning. In order to achieve a better pre-annotation performance in the case of insufficient segmentation labels, semi-supervised and weakly supervised learning were introduced, and a semi-weakly supervised learning segmentation algorithm based on sparse labels was proposed. In addition, in order to improve the contribution rate of a single segmentation label to the performance of the pre-annotation model, an iterative annotation strategy based on active learning was

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Effect of sparse pre-annotation interval S int on the performance of pre-annotation model. TB: tibia bone; TC: tibial cartilage.

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TB | 0.928 | 0.950 | 0.958 | 0.967 | 0.971 | 0.974 | 0.974 | 0.976 | 0.975 | 0.976 |
| TC | 0.744 | 0.788 | 0.798 | 0.800 | 0.803 | 0.794 | 0.811 | 0.804 | 0.809 | 0.804 |
| 4.2.2. Pseudo-Segmentation Label Self-Refinement |  |  |  |  |  |

## Comparison of the pseudo-segmentation label self-refinement with baseline (Baseline + PLSR) with baseline (Baseline) on tibia (TB) and tibial cartilage (TC) images.

| Sensors 2024, 24, x FOR PEER REVIEW |  | 11 of 15 |
| --- | --- | --- |
|  | Baseline | Baseline + PLSR |
| TB | 0.948 | 0.969 |
| TC | 0.764 | 0.785 |

## Comparison of the pseudo-segmentation label self-refinement with baseline (Baseline + PLSR) with baseline (Baseline) on tibia (TB) and tibial cartilage (TC) images.

|  | Baseline | Baseline + PLSR |
| --- | --- | --- |
| TB | 0.948 | 0.969 |
| TC | 0.764 | 0.785 |

## Comparison of different segmentation algorithms on tibia (TB), tibial cartilage (TC), femur bone (FB) and femoral cartilage (FC) images. Seq: equivalent segmentation annotation workload.

|  |  | TB | TC | FB | FC |
| --- | --- | --- | --- | --- | --- |
|  | 320 | 0.928 | 0.744 | 0.874 | 0.496 |
| FS | 1600 3200 | 0.976 0.977 | 0.808 0.817 | 0.977 0.980 | 0.854 0.866 |
|  | 4800 | 0.980 | 0.821 | 0.982 | 0.868 |
|  | 320 | 0.967 | 0.800 | 0.952 | 0.841 |
| FSS | 1600 | 0.977 | 0.815 | 0.979 | 0.865 |
|  | 2800 | 0.980 | 0.820 | 0.982 | 0.867 |
| WS | 741 | 0.948 | 0.764 | 0.935 | 0.829 |
| SWS | 1040 | 0.980 | 0.819 | 0.981 | 0.867 |
| 4.3.2. Iterative Model Update and Annotation Stage |  |  |

## Comparison of results of different iterative annotation strategies on tibia (TB), tibial cartilage (TC), femur bone (FB) and femoral cartilage (FC) images.

|  |  | TB | TC | FB | FC |
| --- | --- | --- | --- | --- | --- |
| 800 | IA AL | 0.981 0.982 | 0.820 0.823 | 0.981 0.982 | 0.868 0.873 |
| 1600 | IA AL | 0.982 0.983 | 0.822 0.831 | 0.981 0.983 | 0.871 0.873 |

### Formule


$$𝐿 = 𝐿 + 𝐿(1)$$

### Formule


$$𝐿 = (𝐺 , 𝑙𝑜𝑔(𝑄 , ) + (1 -𝐺 , )𝑙𝑜𝑔(1 -𝑄 , )) ,(2)$$

### Formule


$$𝐿 = 1 - 2 ∑ (𝐺 , 𝑄 , ) , ∑ (𝐺 , + 𝑄 , ) ,(3)$$

### Formule


$$𝐿 = (𝑤 𝐸 , 𝑙𝑜𝑔(𝑆 , ) + 𝑤 (1 -𝐸 , )𝑙𝑜𝑔(1 -𝑆 , )) ,(4)$$

### Formule


$$L area = L BCE + L DICE(1)$$

### Formule


$$L BCE = ∑ x, y G x, y log Q x, y + (1 -G x, y )log 1 -Q x, y(2)$$

### Formule


$$L DICE = 1 - 2∑ x, y G x, y Q x, y ∑ x, y G x, y + Q x, y(3)$$

### Formule


$$L edge = ∑ x, y w 0 E x, y log S x, y + w 1 (1 -E x, y )log 1 -S x, y(4)$$

### Formule


$$w 0 = ∑ x, y E x, y W H(5)$$

### Formule


$$w 1 = 1 -w 0 (6$$

### Formule


$$)$$

### Formule


$$𝐿𝑜𝑠𝑠 = 𝐿 + 𝐿(7)$$

### Formule


$$Loss PL = L P_BCE + L P_DICE(8)$$

### Formule


$$Loss SL = Loss PL + L P_edge (12) α = max E thres -E cur E thres , 0(13)$$

### Formule


$$β = min E cur E thres , 1(14)$$

### Formule


$$L P_edge = ∑ x, y w P0 F x, y log C x, y + w P1 (1 -F x, y )log 1 -C x, y(15)$$

### Formule


$$w P0 = ∑ x, y F x, y W H(16)$$

### Formule


$$w P1 = 1 -w P0(17)$$

### Formule


$$Dice i, m =    Dice(U i , U i+1 ), i = 1 (Dice(U i-1 , U i ) + Dice(U i , U i+1 ))/2, i = 2, 3, . . . , Nu -1 Dice(U i-1 , U i ), i = Nu (18$$

### Formule


$$)$$

### Formule


$$Dice = 2(A ∩ B) A ∪ B (19$$

### Formule


$$)$$
