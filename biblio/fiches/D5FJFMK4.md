# Deep Omni-Supervised Learning for Rib Fracture Detection From Chest Radiology Images.

**Auteurs** : Zhizhong Chai, Luyang Luo, Huangjing Lin, Pheng-Ann Heng, Hao Chen
**Année** : 2024
**DOI** : 10.1109/tmi.2024.3353248

## Résumé

Deep learning (DL)-based rib fracture detection has shown promise of playing an important role in preventing mortality and improving patient outcome. Normally, developing DL-based object detection models requires a huge amount of bounding box annotation. However, annotating medical data is time-consuming and expertise-demanding, making obtaining a large amount of fine-grained annotations extremely infeasible. This poses a pressing need for developing label-efficient detection models to alleviate radiologists' labeling burden. To tackle this challenge, the literature on object detection has witnessed an increase of weakly-supervised and semi-supervised approaches, yet still lacks a unified framework that leverages various forms of fully-labeled, weakly-labeled, and unlabeled data. In this paper, we present a novel omni-supervised object detection network, ORF-Netv2, to leverage as much available supervision as possible. Specifically, a multi-branch omni-supervised detection head is intr

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Comparison of different label assignment strategies on RibFrac.

| Method | D b | #scans used Dm D d | Du | Metrics mAP AP50 |
| --- | --- | --- | --- | --- | --- |
| HLA | 105 | 105 | 105 105 | 33.7 | 46.8 |
| SLA | 105 | 105 | 105 105 | 34.1 | 47.2 |
| DLA | 105 | 105 | 105 105 | 34.7 | 48.1 |

## Performance comparison of different classification branches in the omni-supervised detection head on RibFrac.

| Method | D b | #scans used Dm D d | Du | Metrics mAP AP50 |
| --- | --- | --- | --- | --- | --- |
| Box branch | 105 | 105 | 105 105 | 34.6 | 48.0 |
| Mask branch | 105 | 105 | 105 105 | 34.4 | 47.7 |
| Dot branch | 105 | 105 | 105 105 | 34.3 | 47.6 |
| Unlabeled branch 105 | 105 | 105 105 | 34.6 | 48.1 |
| Fusion | 105 | 105 | 105 105 | 34.7 | 48.1 |

## Comparison of different hyper-parameters in the sample weighting function on RibFrac.

| Method | α | β | Metrics mAP AP50 |
| --- | --- | --- | --- | --- |
| ORF-Netv2 | 1 | 1 | 32.8 | 46.0 |
| ORF-Netv2 0.5 | 1 | 34.5 | 47.6 |
| ORF-Netv2 | MI | 1 | 34.7 | 48.1 |
| ORF-Netv2 | 1 | 2 | 33.6 | 46.5 |
| ORF-Netv2 0.5 | 2 | 34.5 | 47.8 |

## Comparison with the SOTA on RibFrac. *: p-value < 0.05; **: p-value < 0.01.

| Index | Method | #scans used D b Dm D d Du mAP AP50 Metrics | P |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FCOS [23] | 105 | 0 | 0 | 0 | 30.9 | 42.5 | - |
| 2 | FCOS [23] | 105 105 | 0 | 0 | 33.8 | 46.9 | * |
| 3 | ORF-Netv2 | 105 105 | 0 | 0 | 33.8 | 47.3 | - |
| 4 | FCOS [23] | 105 | 0 | 105 | 0 | 31.4 | 43.1 | ** |
| 5 | ORF-Net [14] 105 | 0 | 105 | 0 | 31.8 | 44.7 | * |
| 6 | ORF-Netv2 | 105 | 0 | 105 | 0 | 32.0 | 45.4 | - |
| 7 | Π Model [41] 105 | 0 | 0 | 105 31.4 | 42.5 | * |
| 8 | STAC [9] | 105 | 0 | 0 | 105 31.3 | 43.2 | * |
| 9 | AALS [26] | 105 | 0 | 0 | 105 31.5 | 42.9 | ** |
| 10 | OXNet [12] | 105 | 0 | 0 | 105 31.1 | 43.1 | * |
| 11 | UT [8] | 105 | 0 | 0 | 105 31.4 | 43.5 | * |
| 12 | ORF-Net [14] 105 | 0 | 0 | 105 31.1 | 43.2 | * |
| 13 | ORF-Netv2 | 105 | 0 | 0 | 105 31.2 | 43.4 | - |
| 14 | Π Model [41] 105 | 0 | 105 105 32.8 | 45.0 | ** |
| 15 | STAC [9] | 105 | 0 | 105 105 33.4 | 44.9 | * |
| 16 | AALS [26] | 105 | 0 | 105 105 33.3 | 44.9 | * |
| 17 | OXNet [12] | 105 | 0 | 105 105 33.1 | 45.1 | * |
| 18 | UT [8] | 105 | 0 | 105 105 33.0 | 45.0 | * |
| 19 | ORF-Net [14] 105 | 0 | 105 105 32.9 | 45.3 | ** |
| 20 | ORF-Netv2 | 105 | 0 | 105 105 33.4 | 46.6 | - |
| 21 | Π Model [41] 105 105 | 0 | 105 33.4 | 46.9 | ** |
| 22 | STAC [9] | 105 105 | 0 | 105 33.6 | 45.9 | ** |
| 23 | AALS [26] | 105 105 | 0 | 105 33.5 | 46.8 | ** |
| 24 | OXNet [12] | 105 105 | 0 | 105 33.1 | 46.9 | ** |
| 25 | UT [8] | 105 105 | 0 | 105 33.3 | 47.0 | ** |
| 26 | ORF-Net [14] 105 105 | 0 | 105 33.7 | 47.1 | ** |
|  | ORF-Netv2 | 105 105 | 0 | 105 34.2 | 47.4 | - |
| 28 | Π Model [41] 105 105 105 105 34.0 | 47.0 | ** |
| 29 | STAC [9] | 105 105 105 105 33.8 | 46.5 | ** |
| 30 | AALS [26] | 105 105 105 105 33.8 | 47.2 | ** |
| 31 | OXNet [12] | 105 105 105 105 34.4 | 47.2 | * |
| 32 | UT [8] | 105 105 105 105 34.3 | 47.5 | * |
| 33 | ORF-Net [14] 105 105 105 105 34.2 | 47.5 | ** |
| 34 | ORF-Netv2 | 105 105 105 105 34.7 | 48.1 | - |

## Comparison with the SOTA on CRF. *: p-value < 0.05; **: p-value < 0.01.

| Method | D b | #scans used D d Du | Metrics mAP AP50 | p-value |
| --- | --- | --- | --- | --- | --- | --- |
| FCOS [23] | 224 | 0 | 0 | 39.9 | 53.7 | - |
| FCOS [23] | 224 450 | 0 | 41.3 | 54.4 | ** |
| ORF-Net [14] | 224 450 | 0 | 42.3 | 56.3 | ** |
| ORF-Netv2 | 224 450 | 0 | 42.6 | 57.0 | - |
| STAC [9] | 224 450 1104 | 40.0 | 56.1 | ** |
| UT [8] | 224 450 1104 | 42.6 | 56.3 | ** |
| Π Model [41] 224 450 1104 | 42.9 | 56.3 | ** |
| OXNet [12] | 224 450 1104 | 42.9 | 56.5 | ** |
| AALS [26] | 224 450 1104 | 43.4 | 57.2 | ** |
| ORF-Net [14] | 224 450 1104 | 44.3 | 59.1 | * |
| ORF-Netv2 | 224 450 1104 | 44.7 | 59.7 | - |

## Comparison with the SOTA on XRF. *: p-value < 0.05; **: p-value < 0.01.

| Method | D b | #scans used D d | Du | Metrics mAP AP50 | p-value |
| --- | --- | --- | --- | --- | --- | --- |
| FCOS [23] | 2154 | 0 | 0 | 14.4 | 24.2 | - |
| FCOS [23] | 2154 2154 | 0 | 15.7 | 26.3 | - |
| ORF-Net [14] | 2154 2154 | 0 | 17.4 | 28.5 | ** |
| ORF-Netv2 | 2154 2154 | 0 | 19.0 | 31.7 | - |
| Π Model [41] 2154 2154 2154 | 17.9 | 30.8 | ** |
| STAC [9] | 2154 2154 2154 | 18.3 | 29.1 | ** |
| AALS [26] | 2154 2154 2154 | 18.9 | 31.0 | ** |
| UT [8] | 2154 2154 2154 | 19.2 | 31.5 | * |
| OXNet [12] | 2154 2154 2154 | 19.1 | 32.0 | * |
| ORF-Net [14] | 2154 2154 2154 | 19.2 | 31.9 | * |
| ORF-Netv2 | 2154 2154 2154 | 19.4 | 32.8 | - |
| under different settings. With results in Table |  |

## Budget-aware omni-supervised rib fracture detection on RibFrac.

| Policy | D b | #scans used Dm D d | Du | Metrics mAP AP50 |
| --- | --- | --- | --- | --- | --- | --- |
| STRONG-B | 217 | 0 | 0 | 203 | 33.9 | 46.3 |
| STRONG-M | 0 | 105 | 0 | 315 | 31.9 | 43.8 |
| EQUAL | 72 | 97 | 35 | 216 | 31.9 | 44.1 |
| EQUAL-NUM | 57 | 57 | 57 | 249 | 32.3 | 45.0 |

## Comparison of different supervised object detectors on the box-labeled data from RibFrac.

| Method | #scans used D b | Metrics mAP AP50 |
| --- | --- | --- | --- |
| FCOS [23] | 105 | 30.7 | 42.5 |
| Faster RCNN [22] | 105 | 29.5 | 40.9 |
| RetinaNet [21] | 105 | 28.7 | 40.1 |
| Deformable DETR [46] | 105 | 28.5 | 38.9 |

### Formule


$$I b = (P m × P d × P u ) 1 3 , I m = (P b × P d × P u ) 1 3 , I d = (P b × P m × P u ) 1 3 , I u = (P b × P m × P d ) 1 3 .$$

### Formule


$$W d = N (I d ), W u = N (I u ).$$

### Formule


$$)2$$

### Formule


$$W b = N ((I b ) α × (IoU b ) β ), W m = N ((I m ) α × (IoU m ) β ),(3)$$

### Formule


$$L cls =        - S i (1 -P i ) γ log P i , W i ≥ t - S i (P i ) γ log (1 -P i ), W i < t(4)$$

### Formule


$$L cls =        - S i (W i ) γ (1 -P i ) γ log (1 -W i )P i , W i ≥ t - S i (1 -W i ) γ (P i ) γ log W i (1 -P i ) , W i < t$$

### Formule


$$L cls = - S i (W i ) γ (1 -P i ) γ log (1 -W i )P i +(1 -W i ) γ (P i ) γ log W i (1 -P i ) . (6$$

### Formule


$$)$$

### Formule


$$L ccls =        - S i (1 -P i ) γ log P i , i ∈ positives - S i (P i ) γ log (1 -P i ), i ∈ negatives(7)$$

### Formule


$$L ucls = - N j M j i (W ij ) γ (1 -P ij ) γ log (1 -W ij )P ij +(1 -W ij ) γ (P ij ) γ log W ij (1 -P ij ) ,(8)$$

### Formule


$$L reg = N j M j i L GIoU (h i , ĥi ),(9)$$

### Formule


$$L = (L b ucls + L b ccls + L b reg ) + (L m ucls + L m ccls + L m reg )+ (L d ucls + L d ccls ) + δ(L u ucls ) (10$$

### Formule


$$)$$
