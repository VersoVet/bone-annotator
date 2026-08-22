# Supervised Learning of Semantic Classes for Image Annotation and Retrieval

**Auteurs** : Gustavo Carneiro, Antoni B. Chan, Pedro J. Moreno, Nuno Vasconcelos
**Année** : 2007
**DOI** : 10.1109/tpami.2007.61

## Résumé

A probabilistic formulation for semantic image annotation and retrieval is proposed. Annotation and retrieval are posed as classification problems where each class is defined as the group of database images labeled with a common semantic label. It is shown that, by establishing this one-to-one correspondence between semantic labels and semantic classes, a minimum probability of error annotation and retrieval are feasible with algorithms that are 1) conceptually simple, 2) computationally efficient, and 3) do not require prior semantic segmentation of training images. In particular, images are represented as bags of localized feature vectors, a mixture density estimated for each image, and the mixtures associated with all images annotated with a common semantic label pooled into a density estimate for the corresponding semantic class. This pooling is justified by a multiple instance learning argument and performed efficiently with a hierarchical extension of expectation-maximization. The benefits of the supervised formulation over the more complex, and currently popular, joint modeling of semantic label and visual feature distributions are illustrated through theoretical arguments and extensive experiments. The supervised formulation is shown to achieve higher accuracy than various previously published methods at a fraction of their computational cost. Finally, the proposed method is shown to be fairly robust to parameter tuning.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## 1 ; w 1 Þ; . . . ; ðI D ; w D Þg of image-caption pairs, where I i 2 T D with T D ¼ fI 1 ; . . . ; I D g, and w i & L, with L ¼ fw 1 ; . . . ; w T g. The steps of the training algorithm are: 1. For each semantic class w 2 L, a. Build a training image set TD & T D , where w 2 w i for all I i 2 TD . b. For each image I 2 TD , i. Decompose I into a set of overlapping 8 Â8 regions, extracted with a sliding window that moves by two pixels between consecutive samples (note that, in all experiments reported in this work, images were represented in the YBR color space). ii. Compute a feature vector, at each location of the three YBR color channels, by the applica-

| dimen- |
| --- |
| sional YBR-DCT vectors are concatenated |
| by interleaving the values of the YBR |
| feature components. This facilitates the |
| application of dimensionality reduction |
| techniques due to the well-known energy |
| compaction properties of the DCT. To |
| simplify notation, we hereafter replace |
| ½x |

### Formule


$$Y i ¼ 1; if I contains concept w i 0; otherwise: &ð1Þ$$

### Formule


$$P XjY i ðXj1ÞP Y i ð1Þ ! P XjY i ðXj0ÞP Y i ð0Þ;ð2Þ$$

### Formule


$$P X;W ðX; wÞ ¼ X S l¼1 P X;WjL ðX ; wjlÞP L ðlÞ;ð3Þ$$

### Formule


$$P X;W ðX ; wÞ ¼ X D l¼1 P XjL ðX jlÞP WjL ðwjlÞP L ðlÞ;ð5Þ$$

### Formule


$$P WjX ðwjX Þ ¼ P X;W ðX ; wÞ P X ðX Þ :ð6Þ$$

### Formule


$$P W jX ðijxÞ ¼ P XjW ðxjiÞP W ðiÞ P X ðxÞð7Þ$$

### Formule


$$i Ã ðX Þ ¼ arg max i P W jX ðijX Þ:ð8Þ$$

### Formule


$$j Ã ðw i Þ ¼ arg max j P XjW ðX j jiÞ;ð9Þ$$

### Formule


$$P XjL ðxjlÞ ¼ X 4 i¼1 i G x; l i ; l i À Á ;ð10Þ$$

### Formule


$$P X ðxÞ ¼ X D l¼1 P XjL ðxjlÞP L ðlÞ ¼ 1 D X D l¼1 X 4 i¼1 i G x; l i ; l i À Á ;$$

### Formule


$$P X ðxÞ ¼ X 4 i¼1 1 D X D l¼1 i G x; l i ; l i À Á ¼ 1 Gðx; w ; w Þ þ X 4 i¼2 i D X D l¼1 G x; l i ; l i À Á$$

### Formule


$$P X ðxÞ ¼ 1 Gðx; w ; w Þ þ ð1 À 1 Þ Z Gðx; ; Þp ; ð; Þdd;$$

### Formule


$$D!1 P X ðxÞ ¼ 1 Gðx; w ; w Þ þ ð1 À 1 Þ;$$

### Formule


$$KLð PXjW kP XjW Þ ¼ X x PXjWðxjwÞ$$

### Formule


$$i Ã ðXÞ ¼ arg max i P W jX ðijX Þ; if P W jX ðijX Þ > 0; otherwise; &ð11Þ$$

### Formule


$$P W jX ðijX$$

### Formule


$$P XjW ðxjiÞ ¼ 1 D i X Di l¼1 P XjL;W ðxjl; iÞ:ð13Þ$$

### Formule


$$ĥq i ¼ 1 D i X D i l¼1 h q i;l :$$

### Formule


$$P XjL;W ðxjl; iÞ ¼ X k k i;l G x; k i;l ; AE k i;l ;ð14Þ$$

### Formule


$$P XjW ðxjiÞ ¼ 1 D i X k X Di l¼1 k i;l G x; k i;l ; AE k i;l ;ð15Þ$$

### Formule


$$k j ; k j ; AE k j n o ; j ¼ 1; . . . ; D i ; k ¼ 1; . . . ; K:ð16Þ$$

### Formule


$$E-step: Compute h m jk ¼ Gð k j ; m c ; AE m c Þe À 1 2 tracefðAE m c Þ À1 AE k j g h i k j N m c P l Gð k j ; l c ; AE l c Þe À 1 2 tracefðAE l c Þ À1 AE k j g h i k j N l c ;ð17Þ$$

### Formule


$$ð m c Þ new ¼ P jk h m jk D i K ;ð18Þ$$

### Formule


$$ð m c Þ new ¼ X jk w m jk k j ; where w m jk ¼ h m jk k j P jk h m jk k j ;ð19Þ$$

### Formule


$$ðAE m c Þ new ¼ X jk w m jk AE k j þ ð k j À m c Þð k j À m c Þ T h i :ð20Þ$$

### Formule


$$P XjW ðxjI Þ ¼ X 8 k¼1 k I G x; k I ; AE k I À Á ;ð21Þ$$

### Formule


$$P XjW ðxjwÞ ¼ X 64 k¼1 k w G x; k w ; AE k w À Á :$$

### Formule


$$1. Step (1-b-i) of the training algorithm. 2. Step (1-b-ii) of the training algorithm. 3. For each class w i 2 L, compute log P W jX ðw i jBÞ ¼ log P XjW ðBjw i Þ þ log P W ðw i Þ À log P X ðBÞ;$$

### Formule


$$log P XjW ðBjw i Þ ¼ X x2B log P XjW ðxjw i Þ;$$

### Formule


$$P ðj; kÞ ¼ X k i¼j Iði mÞ m i À Á nÀm kÀi À Á n k À Á ;$$

### Formule


$$P ðj; kÞ % X k i¼j k i p i ð1 À pÞ kÀi ;$$
