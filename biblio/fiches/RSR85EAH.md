# Region‐Based Convolutional Neural Network‐Based Spine Model Positioning of X‐Ray Images

**Auteurs** : Le Zhang, Jiabao Zhang, Song Gao
**Année** : 2022
**DOI** : 10.1155/2022/7512445

## Résumé

<h4>Background</h4>Idiopathic scoliosis accounts for over 80% of all cases of scoliosis but has an unclear pathogenic mechanism. Many studies have introduced conventional image processing methods, but the results often fail to meet expectations. With the improvement and evolution of research in neural networks in the field of deep learning, many research efforts related to spinal reconstruction using the convolutional neural network (CNN) architecture of deep learning have shown promise.<h4>Purpose</h4>To investigate the use of CNN for spine modeling.<h4>Methods</h4>The primary technique used in this study involves Mask Region-based CNN (R-CNN) image segmentation and object detection methods as applied to spine model positioning of radiographs. The methods were evaluated based on common evaluation criteria for vertebral segmentation and object detection. Evaluations were performed using the loss function, mask loss function, classification loss function, target box loss function, avera

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Parameters for evaluating the experimental results of spine model positioning (lateral images).

|  | Accuracy | IoU = 0:75 Average precision (AP75) | Average recall (AR) |
| --- | --- | --- | --- |
| Spine segmentation | 99.8% | 81.6% | 63.8% |
| Bounding box | 99.8% | 90.1% | 90.0% |

### Formule


$$x i+1 = F x i , G i ð Þ+ Wx i :ð1Þ$$

### Formule


$$x k = 〠 k-1 j=i F x i , G i ð Þ+ x i ,ð2Þ$$

### Formule


$$ⅆl ⅆx i = ⅆl ⅆx k ⅆx k ⅆx i :ð3Þ$$

### Formule


$$ⅆl ⅆx i = ⅆl ⅆx k ⅆ ∑ k-1 j=i F x i , G i ð Þ+ x i ⅆx i = ⅆl ⅆx k 1 + ⅆ∑ k-1 j=i F x i , G i ð Þ ⅆx i ! :ð4Þ$$

### Formule


$$L = L cls + L box + L mask :ð5Þ$$
