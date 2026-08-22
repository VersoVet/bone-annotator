# Foundation Models Meet Medical Image Interpretation.

**Auteurs** : Jiao L, Hao J, Li R, Li L, Liu X, Liu F, Ma W, Chen P, Huang Z, Yang J
**Année** : 2026
**DOI** : 10.34133/research.1024

## Résumé

Facing challenges such as limited annotated data and insufficient model generalization in medical deep learning, foundation models (FMs) are reshaping the paradigm of medical image interpretation through large-scale pretraining and efficient fine-tuning. Unlike traditional models focused on single modality and task, FMs enable multi-modal representation and task-agnostic transfer, adapting to various downstream applications without extensive annotation or retraining. This paper systematically reviews the research progress on medical FMs, focusing on medical tasks, datasets, and evaluation metrics. It covers key interpretation tasks such as classification, segmentation, generation, and prognosis prediction. At the data level, it integrates multi-source data including 2-dimensional (2D)/3D medical imaging, vision-language data, electronic health records (EHRs), physiological signals, and bioinformatics data, and summarizes the evaluation metrics for each task. On this basis, the paper ca

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## The division information of the VisDrone2019 dataset.

| DataSet Resolution Number of images |
| --- | --- |
| Train | 1024*1024 4548 |
| Val | 1024*1024 973 |
| Test | 1024*1024 994 |

## 50-95 (%) FPS Gfloats

| 2015 Fast-rcnn 16 | / | / | / | 87.2 | 47.3 | / | / |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2020 YOLOv5 42 | n | 90.3 | 85 | 91.1 | 52.5 | 69.44 | 7.2 |
| 2021 YOLOx 43 | tiny | / | / | 86.6 | 48 | / | 6.5 |
| 2022 YOLOv6 44 | n | 90.5 | 84.7 | 90.9 | 52.2 | 86.21 | 11.9 |
| 2023 YOLOv8 45 | n | 90.3 | 84.8 | 90.8 | 51.9 | 99.01 | 8.2 |
| 2023 RT-DETR 46 | l | 79.2 | 73.2 | 76.8 | 25.1 | / | 103.4 |
| 2024 YOLOv9 13 | t | 90.6 | 85.2 | 91.4 | 53.3 | 65.79 | 7.9 |
| 2024 YOLOv10 27 | n | 90.5 | 85.6 | 91.1 | 52.6 | 86.96 | 8.4 |
| 2024 YOLOv11 47 | n | 90.3 | 85.2 | 91.3 | 53.1 | 94.34 | 6.6 |
| 2024 LSKA 48 | n | 90.6 | 84.6 | 91.2 | 52.7 | 106.38 5.9 |
| 2024 PCSA-YOLO 49 | n | 90.3 | 84.1 | 90.9 | 52.8 | 84.03 | 7.0 |
| 2025 YOLOv12 50 | n | 90.6 | 85 | 91.4 | 52.9 | 73.5 | 6.5 |
| 2025 YOLOv13 51 | n | 90.8 | 84.9 | 91.6 | 53.8 | 57.47 | 6.4 |
| 2025 Mamba-WheatNet(proposed) n | 90.9 | 85.9 | 91.8 | 53.0 | 85.47 | 7.9 |

## Comparison of Mamba-WheatNet with other advanced models in GWHD-2021 DataSet. complex agricultural scenes. In terms of inference speed, Mamba-WheatNet operates at 85.47 FPS, closely matching the throughput of YOLOv8-n (99.01 FPS), YOLOv11-n (94.34 FPS), and YOLOv6-n (86.21 FPS), while significantly outpacing YOLOv13-n (57.47 FPS) and YOLOv12-n (73.5 FPS). Although it does not attain the peak frame rates of the fastest nano-scale detectors such as YOLOv8-n or YOLOv11-n. The FPS metric indicates that it can support real-time detection in practical agricultural environments.

| Method | Scale Precision (%) Recall (%) mAP50 (%) mAP 50-95 (%) Gfloats |
| --- | --- | --- | --- | --- | --- | --- |
| YOLOv8+c2f-DCNv3 | n | 90.4 | 84.4 | 91 | 53.2 | 7.9 |
| YOLOv8+EMA | n | 90.5 | 82.4 | 90.1 | 52.6 | 8.2 |
| YOLOv8+C2f-FLA | n | 90.6 | 84.4 | 91.1 | 53.2 | 8.2 |
| YOLOv8+RDSBlock(proposed) n | 91.3 | 85.6 | 91.8 | 54 | 9.2 |
| YOLOv8+BVSSBlock(proposed) n | 91.5 | 86 | 92.2 | 54.4 | 8.5 |

## presents the results of the ablation experiments. We are able to analyze the effectiveness of the LDWhead, Adown, RDSBlock and BVSSBlock based on the data presented in the table. Specifically, the addition of lightweight detection head LDWhead and downsampling

| Year Method | Scale Precision (%) Recall (%) mAP50 (%) mAP 50-95 (%) Gfloats |
| --- | --- | --- | --- | --- | --- | --- |
| 2020 YOLOv5 42 | n | 44.0 | 32.2 | 32.6 | 18.7 | 7.2 |
| 2021 YOLOv6 44 | n | 40.6 | 30.7 | 30.3 | 17.6 | 11.9 |
| 2023 YOLOv8 45 | n | 45.3 | 33.0 | 33.2 | 19.2 | 8.2 |
| 2024 YOLOv9 13 | t | 44.3 | 33.3 | 33.1 | 19.4 | 7.8 |
| 2024 YOLOv10 27 | n | 44.1 | 32.8 | 32.2 | 19.5 | 6.7 |
| 2024 YOLOv11 47 | n | 44.0 | 33.5 | 33.1 | 19.1 | 6.6 |
| 2024 LSKA 48 | n | 45.8 | 33.7 | 34.1 | 19.8 | 5.9 |
| 2024 PCSA-YOLO 49 | n | 42.6 | 31.1 | 31.1 | 17.5 | 7.0 |
| 2025 YOLOv12 50 | n | 46.2 | 33.2 | 34 | 20 | 6.5 |
| 2025 YOLOv13 51 | n | 43.6 | 32.8 | 32.8 | 18.9 | 6.4 |
| 2025 Mamba-WheatNet(proposed) n | 48.2 | 35.7 | 35.9 | 21.2 | 7.9 |

## Method LDHead Adown RDSBlock BVSSBlock mAP50 (%) mAP 50-95 (%) F1

| - | - | - | - | - | 90.8 | 51.9 | 87.46 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ✓ | - | - | - | 91.3 | 52.7 | 87.74 |
| 2 | ✓ | ✓ | - | - | 91.1 | 52.2 | 87.65 |
| 3 | ✓ | ✓ | ✓ | - | 91.3 | 52.7 | 87.71 |
| 4 | ✓ | ✓ | ✓ | ✓ | 91.8 | 53.0 | 88.32 |

### Formule


$$h ′ (t) = Ah(t) + Bx(t)(1)$$

### Formule


$$y(t) = Ch(t)(2)$$

### Formule


$$A = exp(∆A)(3)$$

### Formule


$$B = (∆A) -1 (exp(∆A) -I) • ∆B(4)$$

### Formule


$$h ′ (t) = Ah(t) + Bx(t) (5$$

### Formule


$$)$$

### Formule


$$y(t) = Ch(t)(6)$$

### Formule


$$K = (CB, CAB, . . . , CA K B, . . .) (7) y = x * K (8)$$

### Formule


$$1: x h , xw ← Split(X, dim = 2) 2: x h ← AvgPool(x h ), xw ← AvgPool(xw) 3: X ′ ← Conv1(x h + xw) 4: X ′ ← BN(DWConv(X ′ )) 5: X ′ ← Act(X ′ ) 6: x h , xw ← Split(X ′ , dim = 2) 7: x h ← SS2D(x h ), xw ← SS2D(xw) 8: x h ← BN(DWConv(x h )), xw ← BN(DWConv(xw)) 9: Y ← Conv1(x h + xw)$$

### Formule


$$xa = conv(conv(xa) + conv(xa1) + xa2) (12$$

### Formule


$$)$$

### Formule


$$Y = conv(xa + x b )(13)$$

### Formule


$$Recall = T P T P + F N(15)$$

### Formule


$$F 1 = 2 × Precision × Recall Precision + Recall(16)$$

### Formule


$$AP = ˆ1 0 P (R)dR(17)$$

### Formule


$$F P S = 1 preprocess + inference + postprocess(18)$$
