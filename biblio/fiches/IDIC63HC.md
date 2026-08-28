# Deep learning can automate chicken tibia-breaking strength quantification to improve animal welfare.

**Auteurs** : Debnath T, Wilson P, Pong-Wong R, Plenderleith L, Andersson B, Schmutz M, Dunn I, Prendergast JGD.
**Année** : 2026
**DOI** : 10.1016/j.psj.2026.106549

## Résumé

Bone damage is an important welfare issue in the poultry industry, yet large-scale phenotyping of chicken bone strength currently relies on time-consuming manual annotation of X-rays or destructive post-mortem testing. To address this, an end-to-end deep-learning pipeline was developed that automatically (i) segments the chicken tibiotarsus from lateral X-ray images (U-Net, Dice = 0.91) and (ii) predicts its breaking strength from pixel intensities alone. Using 916 curated bone images, the predictor achieved moderately high correlation with measured breaking strength (maximum Pearson's correlation of 0.74), exceeding the performance of a previous labour-intensive manual annotation method. Image-derived predictions were moderately heritable (h² ≈ 0.16) and exhibited an exceptionally high genetic correlation with the physical trait, indicating that selection on the model-derived phenotype is a good proxy to select for bone strength. The workflow therefore provides a potential rapid, non-

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## The descriptive statistics table. The table shows the distribution of data across our dataset.

| Features | Mean | Median | Standard | Minimum | Maximum |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Deviation | value | value |
| Measured | 224.88 | 212.31 | 73.73 | 66.53 | 697.31 |
| Tibia |  |  |  |  |  |
| breaking |  |  |  |  |  |
| strength |  |  |  |  |  |
| Tibia AUC | 83591.54 | 82725 | 9667 | 61039 | 135489 |
| scores |  |  |  |  |  |

### Formule


$$( Y 1 Y 2 ) = [ X 1 0 0 X 2 ]( b 1 b 2 ) + [ Z 1 0 0 Z 2 ]( u 1 u 2 ) + ( e 1 e 2 )$$

### Formule


$$( u 1 u 2 ) ∼ N ⎛ ⎝ 0, ⎛ ⎝ Aσ 2 u1 Aσ u1,2 Aσ u1,2 Aσ 2 u2 ⎞ ⎠ ⎞ ⎠ and ( e 1 e 2 ) ∼ N ⎛ ⎝ 0, ⎛ ⎝ Iσ 2 e1 Iσ e1,2 Iσ e1,2 Iσ 2 e2 ⎞ ⎠ ⎞ ⎠$$

### Formule


$$y 1 = X 1 b 1 + Z 1 u 1 + e 1 y 2 = X 2 b 2 + Z 2 u 2 + e 2$$

### Formule


$$h 2 1 = σ 2 u1 σ 2 u1 + σ 2 e1 h 2 2 = σ 2 u2 σ 2 u2 + σ 2 e2$$

### Formule


$$r g = σ u1,2 ̅̅̅̅̅̅̅̅̅̅̅̅ ̅ σ 2 u1 σ 2 u2 √$$
