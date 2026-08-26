# Deep learning can automate chicken tibia-breaking strength quantification to improve animal welfare.

**Auteurs** : Tanmay Debnath, Peter Wilson, Ricardo Pong-Wong, Lindsey Plenderleith, Björn Andersson, Matthias Schmutz, Ian Dunn, James G D Prendergast
**Année** : 2026
**DOI** : 10.1016/j.psj.2026.106549

## Résumé

Bone damage is an important welfare issue in the poultry industry, yet large-scale phenotyping of chicken bone strength currently relies on time-consuming manual annotation of X-rays or destructive post-mortem testing. To address this, an end-to-end deep-learning pipeline was developed that automatically (i) segments the chicken tibiotarsus from lateral X-ray images (U-Net, Dice = 0.91) and (ii) predicts its breaking strength from pixel intensities alone. Using 916 curated bone images, the predictor achieved moderately high correlation with measured breaking strength (maximum Pearson's correlation of 0.74), exceeding the performance of a previous labour-intensive manual annotation method. Image-derived predictions were moderately heritable (h² ≈ 0.16) and exhibited an exceptionally high genetic correlation with the physical trait, indicating that selection on the model-derived phenotype is a good proxy to select for bone strength. The workflow therefore provides a potential rapid, non-

## Méthodologie

{'study_design': "Pipeline de deep learning end-to-end en deux étapes : (i) segmentation du tibiotarse à partir d'images radiographiques latérales via un modèle U-Net, (ii) prédiction de la force de rupture osseuse à partir des intensités de pixels de l'image segmentée.", 'intervention': None, 'control': "Comparaison avec une méthode antérieure d'annotation manuelle (labour-intensive manual annotation method), jugée moins performante que le modèle proposé.", 'primary_outcomes': ['Précision de segmentation du tibiotarse (coefficient de Dice)', 'Corrélation entre la force de rupture prédite par le modèle et la force de rupture mesurée physiquement (post-mortem)'], 'secondary_outcomes': ["Héritabilité (h²) du phénotype dérivé de l'image", "Corrélation génétique entre le phénotype dérivé de l'image et le trait physique de force de rupture"], 'statistical_methods': ['Corrélation de Pearson', "Estimation de l'héritabilité (h²)", 'Estimation de la corrélation génétique'], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'Précision de segmentation du tibiotarse (U-Net)', 'value': '0.91', 'unit': 'coefficient de Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'segments the chicken tibiotarsus from lateral X-ray images (U-Net, Dice = 0.91)'}, {'outcome': 'Corrélation entre force de rupture prédite et mesurée', 'value': '0.74', 'unit': 'coefficient de corrélation de Pearson', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': "the predictor achieved moderately high correlation with measured breaking strength (maximum Pearson's correlation of 0.74)"}, {'outcome': "Héritabilité du phénotype dérivé de l'image", 'value': '0.16', 'unit': 'h²', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Image-derived predictions were moderately heritable (h² ≈ 0.16)'}, {'outcome': "Taille de l'échantillon d'images osseuses utilisées", 'value': '916', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Using 916 curated bone images'}], 'qualitative_findings': ["Les prédictions dérivées de l'image ont montré une corrélation génétique exceptionnellement élevée avec le trait physique de force de rupture, sans valeur numérique précisée dans le texte fourni."], 'main_findings': ['Le modèle U-Net segmente le tibiotarse avec une précision élevée (Dice = 0.91)', 'Le prédicteur atteint une corrélation modérément élevée avec la force de rupture mesurée (Pearson max = 0.74), surpassant une méthode manuelle antérieure', "Le phénotype dérivé de l'image est modérément héritable (h² ≈ 0.16) et génétiquement fortement corrélé au trait physique, suggérant qu'il constitue un bon proxy pour la sélection génétique de la force osseuse"]}

## Conclusions

Le pipeline développé constitue une alternative potentiellement rapide, non invasive et génétiquement informative aux tests destructifs post-mortem pour évaluer la force osseuse des poulets Cette approche ouvre la voie à l'incorporation systématique de traits de qualité osseuse dans les programmes de sélection commerciaux, améliorant le bien-être animal à grande échelle

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
