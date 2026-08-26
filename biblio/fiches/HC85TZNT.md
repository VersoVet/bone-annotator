# Block Annotation: Better Image Annotation for Semantic Segmentation with Sub-Image Decomposition

**Auteurs** : Hubert Lin, Paul Upchurch, Kavita Bala
**Année** : 2020

## Résumé

Image datasets with high-quality pixel-level annotations are valuable for semantic segmentation: labelling every pixel in an image ensures that rare classes and small objects are annotated. However, full-image annotations are expensive, with experts spending up to 90 minutes per image. We propose block sub-image annotation as a replacement for full-image annotation. Despite the attention cost of frequent task switching, we find that block annotations can be crowdsourced at higher quality compared to full-image annotation with equal monetary cost using existing annotation tools developed for full-image annotation. Surprisingly, we find that 50% pixels annotated with blocks allows semantic segmentation to achieve equivalent performance to 100% pixels annotated. Furthermore, as little as 12% of pixels annotated allows performance as high as 98% of the performance with dense annotation. In weakly-supervised settings, block annotation outperforms existing methods by 3-4% (absolute) given eq

## Méthodologie

{'study_design': "Comparaison expérimentale de méthodes d'annotation (block annotation vs annotation complète d'image vs autres méthodes faiblement supervisées comme les scribbles, coarse annotations, bounding boxes, point clicks) et évaluation de leur impact sur la performance d'un réseau de segmentation sémantique", 'intervention': "Annotation de sous-images en blocs (block sub-image decomposition) à différents pourcentages de pixels annotés (1%, 5%, 12%, 50%, 100%), crowdsourcée avec des outils d'annotation existants conçus pour l'annotation complète d'image", 'control': "Annotation complète d'image (full-image annotation) à 100% des pixels, ainsi que méthodes faiblement supervisées existantes (MIL-FCN, WSSL, scribbles, coarse annotation, bounding boxes)", 'primary_outcomes': ['Performance de segmentation sémantique (mIOU)'], 'secondary_outcomes': ["Qualité de l'annotation crowdsourcée à coût monétaire équivalent", "Performance en conditions faiblement supervisées à temps d'annotation équivalent", 'Qualité de la reconstruction (inpainting) de la structure globale des images'], 'statistical_methods': [], 'duration': None, 'setting': "Crowdsourcing avec des annotateurs publics (crowdworkers), utilisant des outils d'annotation existants"}

## Résultats

{'quantitative': [{'outcome': 'Performance de segmentation avec 50% des pixels annotés par blocs', 'value': 'équivalente à 100%', 'unit': '% pixels annotés', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'we find that 50% pixels annotated with blocks allows semantic segmentation to achieve equivalent performance to 100% pixels annotated'}, {'outcome': 'Performance de segmentation avec 12% des pixels annotés par blocs', 'value': '98%', 'unit': '% de la performance avec annotation dense (100%)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'With 12% of pixels annotated with blocks, the segmentation performance (error) is within 98% (4%) of segmentation performance (error) with 100% of pixels annotated.'}, {'outcome': "Performance en apprentissage faiblement supervisé (comparaison à temps d'annotation équivalent)", 'value': '+3-4%', 'unit': 'points absolus mIOU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'In weakly-supervised settings, block annotation outperforms existing methods by 3-4% (absolute) given equivalent annotation time.'}, {'outcome': "Performance sur Pascal avec 1/10 du temps d'annotation", 'value': '97%', 'unit': '% de la performance en full-supervision (mIOU)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'On Pascal, 97% of full-supervision mIOU is achieved with 1/10 annotation time.'}, {'outcome': 'mIOU de MIL-FCN (image-level, méthode existante comparée)', 'value': '25.1', 'unit': 'mIOU (%)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'Annotations mIOU (%) MIL-FCN [46] Image-level 25.1'}, {'outcome': "Facteur de temps supplémentaire de l'annotation par blocs par rapport à l'annotation complète d'image", 'value': "jusqu'à 2.2×", 'unit': 'ratio de temps', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'Block annotation may use up to 2.2× the time of full-image annotation.'}, {'outcome': "Coût monétaire relatif de l'annotation de 1% des pixels par blocs par rapport à l'annotation complète", 'value': '100× moins cher', 'unit': 'ratio de coût', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'Based on our results in section 3.2, the cost of annotation for 1% of pixels with blocks will be 100× less than the cost of full-image annotation.'}, {'outcome': "Coût monétaire de Block-12% par rapport à l'annotation complète", 'value': '1/8', 'unit': 'ratio de coût', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'For semantic segmentation, Block-12% offers strong performance at 1/8th of the monetary cost.'}], 'qualitative_findings': ["Les annotations par blocs déplacent l'attention des régions catégorielles vers les régions spatiales, forçant l'annotation de régions complexes informatives plutôt que de privilégier des objets simples", "L'annotation par blocs s'apparente à la gamification et à la science citoyenne, où des tâches agréables mènent à un travail engageant et peu coûteux"], 'main_findings': ["Les block annotations peuvent être crowdsourcées à qualité plus élevée que l'annotation complète d'image à coût monétaire équivalent", "50% des pixels annotés par blocs suffisent pour une performance équivalente à 100% d'annotation dense", "12% des pixels annotés par blocs atteignent 98% de la performance de l'annotation dense complète", "En contexte faiblement supervisé, l'annotation par blocs surpasse les méthodes existantes de 3-4% (absolu) à temps d'annotation équivalent", 'Les images annotées par blocs peuvent être inpaintées efficacement avec des labels de haute qualité sans effort humain supplémentaire']}

## Conclusions

L'annotation par blocs (block annotation) est une alternative efficace à l'annotation complète d'image traditionnelle avec des crowdworkers publics Block-12% offre une performance solide pour 1/8 du coût monétaire Block-5% offre une performance compétitive en faible supervision à temps d'annotation équivalent aux méthodes existantes Block-50% devrait être utilisé pour une performance optimale de segmentation sémantique ou pour récupérer la structure globale via inpainting

## Table 1 contains additional statistics. Despite similar costs to annotate an image in blocks or in full, we show in section 4 that competitive performance is achieved with less than half of the blocks annotated per image. Study Details. For these experiments, we chose to use a synthetic dataset. While human annotations may contain mis-Block vs Full Annotation. Average statistics per image.

|  | Block | Full |
| --- | --- | --- |
| Error | 0.253 | 0.286 |
| Error (small regions) 0.636 | 0.677 |
| $ / hr | $1.40 / hr | $3.12 / hr |
| Total cost | $2.00 | $2.05 |
| Total cost (median) | $1.99 | $2.23 |
| # segments | 95.68 | 38.95 |
| $ / segment | $0.0215 | $0.0595 |

## Block annotation worker feedback. Free-form responses are aggregated over SUNCG and Cityscapes experiments, and collected at most once per worker. All 24 sentiments across all 19 worker responses are summarized.

| "Nice" "Good" "Great" | "Fun" "Happy" | "Easy" "Okay" | Release More HITs | Increase Pay |
| --- | --- | --- | --- | --- | --- |
| # 8 | 5 | 4 | 2 | 2 | 3 |

## Semantic segmentation performance when trained on all images. Training with block annotations uses fewer annotated pixels than full annotation but achieves equivalent performance.

|  | Optimal (Full) Block-50% | Block-12% |
| --- | --- | --- | --- |
| Cityscapes 77.7 | 77.7 | 74.6 |
| ADE20K | 37.4 | 37.2 | 36.1 |

## Weakly-supervised segmentation performance. Eval-

|  | -level | 38.2 |
| --- | --- | --- |
| point sup. [7] | Point | 46.1 |
| ScribbleSup [36] | Point | 51.6 |
| WSSL [45] | Box | 60.6 |
| BoxSup [15] | Box | 62.0 |
| ScribbleSup [36] | Scribble | 63.1 |
| Ours: Block-1% | Pixel-level Block | 61.2 |
| Ours: Block-5% | Pixel-level Block | 67.6 |
| Ours: Block-12% | Pixel-level Block | 68.4 |
| Full Supervision | Pixel-level Image | 69.6 |
| uated on Pascal VOC 2012 validation set. Original table from |
| [36]. Blocks (N%) indicates N% of image pixels (N pseudo- |
| checkerboard blocks) are labelled. |  |

## Weakly-supervised segmentation performance given equal annotation time. For time comparison of scribbles against other methods, please refer to [36].

| Cityscapes | Ours: Block (7 min) | Coarse (7 min [14]) | Full Supervision (90 min [14]) |
| --- | --- | --- | --- |
| mIOU (%) 72.1 | 68.8 | 77.7 |
| Pascal | Ours: Block (25 sec) | Scribbles (25 sec [36]) | Full Supervision (4 min [41]) |
| mIOU (%) 67.2 | 63.1 [36] | 69.6 |

## Block Selection vs Block-Inpainting Quality How does the checkerboard pattern compare to other block selection strategies as hints to the block-inpainting model? Intuitively, it is easier to infer labels for pixels that are close to pixels with known labels than for pixels that are further away. Consider a scenario in which every other pixel in an image is annotated. Reasonably good labels for the unannotated Block-inpainting with different types of hints. "Every other pixel" annotations are infeasible in practice. Relative performance of hints with respect to "every other pixel" hints is shown. Checkerboard blocks outperform no hints, random blocks (only boundaries within blocks), and random blocks (full blocks).

| Block Inpainting vs Automatic Segmentation. Consider |
| --- |
| a scenario in which a small number of pixels in a dataset |
| are annotated, and the remainder are automatically labelled |
| to produce dense annotations. Why should block inpaint- |
| ing be used instead of automatic segmentation? Full pixel- |
| level labels produced by block inpainting are superior to |
| automatic segmentation. On Cityscapes, automatic seg- |
| mentation achieves 78% validation mIOU while block in- |
| painting Block-50% annotations achieves 92% validation |
| mIOU. With Block-12% annotations, automatic segmenta- |
| tion achieves 75% validation mIOU while block inpainting |
| achieves 82% validation mIOU. |

### Formule


$$error rate = 1 K K c=1 (F P c + F N c ) (T P c + F P c + F N c )(1)$$

### Formule


$$µ (i,j) = g t=1 p (i,j) (y|I, W ) g(2)$$

### Formule


$$U (i,j) = g t=1 (p (i,j) (y|I, W ) -µ (i,j) ) 2 g -1(3)$$

### Formule


$$U (i,j) = U (i,j) m , where m = arg max k µ (i,j) k(4)$$
