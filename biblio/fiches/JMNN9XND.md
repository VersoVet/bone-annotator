# A deep learning segmentation strategy that minimizes the amount of manually annotated images.

**Auteurs** : Thierry Pécot, Alexander Alekseyenko, Kristin Wallace
**Année** : 2021
**DOI** : 10.12688/f1000research.52026.2

## Résumé

Deep learning has revolutionized the automatic processing of images. While deep convolutional neural networks have demonstrated astonishing segmentation results for many biological objects acquired with microscopy, this technology's good performance relies on large training datasets. In this paper, we present a strategy to minimize the amount of time spent in manually annotating images for segmentation. It involves using an efficient and open source annotation tool, the artificial increase of the training dataset with data augmentation, the creation of an artificial dataset with a conditional generative adversarial network and the combination of semantic and instance segmentations. We evaluate the impact of each of these approaches for the segmentation of nuclei in 2D widefield images of human precancerous polyp biopsies in order to define an optimal strategy.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

### Formule


$$1 2 1 2 1 2 ( ) ( ) ( ( ), ( )) . ( ) ( ) E GT E GT E GT O e O e IoU O e O e O e O e = ∩ ∪ An IoU(O GT (e 1 ), O E (e 2 )) equal to 0 implies that O GT (e 1 )$$

### Formule


$$1 1 2 1 1 2 1 2 1 2 1 1 2 2 2 1 2 2 ( ) ( ) ( ) ( ) 1, , , ( ) ( ) ( ) ( ) ( ) ( ) if ( ) *( ( ), ( )) ( ) ( ) ( ) ( ) ( ) 1, , , ( ) ( ) ( ) ( ) 0 otherwise. j j E GT E GT E E GT GT E GT E GT E GT E E GT GT E E GT GT i i O e O e O$$

### Formule


$$ > ∀ ∈    =  > ∀ ∈  ∩ ∩ ∪ ∪ ∩ ∩ ∪ ∩ ∪ ∪ … …   $$

### Formule


$$2 ( ) 1( ) , 2 ( ) ( ) ( ) TP t F t TP t FN t FP t × = × + + where 1 2 1 2 1 2 1 2 2 1 2 1 { } 1 { } 1 { } 1 } {1 , ,, , , , , , ( ) ( *( ( ), ( )) ), ( ) ( *$$

### Formule


$$∈ = > = < ∀ ∈ = < ∀ ∈ ∑ ∑ ∑ … … … … … … 1 1 1 and 1 if is true, ( ) 0 otherwise.  =   1 C C$$
