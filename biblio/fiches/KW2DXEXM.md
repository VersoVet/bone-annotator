# Automatic Lung Segmentation in Chest X-Ray Images Using SAM With Prompts From YOLO

**Auteurs** : Ebrahim Khalili, Blanca Priego-Torres, Antonio Leon-Jimenez, Daniel Sanchez-Morillo
**Année** : 2024
**DOI** : 10.1109/access.2024.3454188

## Résumé

Despite the impressive performance of current deep learning models in the field of medical imaging, transferring the lung segmentation task in X-ray images to clinical practice is still a pending task. In this study, the performance of a fully automatic framework for lung field segmentation in chest X-ray images was evaluated. The framework is rooted in the combination of the Segment Anything Model (SAM) with prompt capabilities, and the You Only Look Once (YOLO) model to provide effective prompts. Transfer learning, loss functions, and several validation strategies were thoroughly assessed. This provided a complete benchmark that enabled future research studies to fairly compare new segmentation strategies. The results achieved demonstrated significant robustness and generalization capability against the variability in sensors, populations, disease manifestations, device processing, and imaging conditions. The proposed framework was computationally efficient, could address bias in tra

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Table 6

| summarizes the model performance estimated |
| --- |
| using cross-dataset validation. |

### Formule


$$x i tl = min (x | x = 1) , y i tl = min (y | y = 1)(1)$$

### Formule


$$x i br = max (x | x = 1) , y i br = max (y | y = 1)(2)$$

### Formule


$$GIoU = | A ∩ B| | A ∪ B| - | C\(A ∪ B)| | C| (3)$$

### Formule


$$L = L F,γ + L T ,α,β(4)$$

### Formule


$$L F,γ = c SJ 1/γ (5) SJ = 1 - N i=1 p ic g ic + ε N i=1 p ic +g ic -N i=1 p ic g ic + ε (6) L T ,α,β = N i=1 p ic g ic + ε N i=1 p ic g ic + α N i=1 p ic g ic + β N i=1 p ic g ic + ε(7)$$

### Formule


$$Precision = TP TP + FP(8)$$
