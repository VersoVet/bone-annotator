# Bridging Species with AI: A Cross-Species Deep Learning Model for Fracture Detection and Beyond

**Auteurs** : Ahmed H, Berner D, Zhang Q, Verheyen K, Llabres-Diaz F
**Année** : 2026
**DOI** : 10.3390/bioengineering13020213

## Résumé

Fractures are a leading cause of morbidity and mortality in Thoroughbred racehorses, posing a significant threat to their welfare and careers. This study introduces a deep learning model specifically designed to facilitate fracture detection in equine athletes. By leveraging extensive training on human fracture data and refining the model with equine imaging, it highlights the transformative potential of transfer learning across species and medical contexts. This approach is not limited to equine fractures but could be adapted for use in detecting injuries or conditions in other veterinary species and even human healthcare applications. A comprehensive databank of radiographs, sourced from public archives and equine hospitals, was curated to encompass diverse conditions (fracture and non-fracture), ensuring robust pattern recognition. The architecture integrates a Vision Transformer for global context modelling with a ResNet backbone and loss function to optimize local feature extracti

## Méthodologie

{'study_design': "Pipeline de deep learning combinant collecte de données, prétraitement, architecture hybride de modèle (Vision Transformer pour la modélisation du contexte global et backbone ResNet pour l'extraction de caractéristiques locales), apprentissage par transfert cross-espèces (humain vers équin, puis validation féline), entraînement et évaluation", 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': 'Archives publiques de radiographies et hôpitaux équins'}

## Résultats

{'quantitative': [], 'qualitative_findings': [], 'main_findings': []}

## Conclusions

The study presents a modular, cross-species deep learning framework for fracture detection in equine fetlock radiographs, addressing a key gap in veterinary diagnostic imaging By leveraging transfer learning from large human radiographic datasets and fine-tuning on curated veterinary cases, the proposed pipeline achieved high performance in modality recognition, projection classification, and fracture localization, with strong generalization to feline and human datasets Fine-tuning on veterinary images did not degrade human diagnostic performance, supporting the use of human-to-veterinary transfer learning in data-limited settings While the current framework is optimized for dorsopalmar radiographs and fracture localization rather than full case-level diagnosis, it provides a robust proof of concept for scalable AI-assisted veterinary imaging With larger datasets, multi-view learning, and prospective clinical validation, this approach could support decision making in equine sports medicine and contribute to the development of shared benchmarks for veterinary imaging, helping to narrow the technological gap between human and animal healthcare

## A confusion matrix for modality classification (ViT-ResNet model). The classifier achieved an overall accuracy of 96.7%, with 93.9% sensitivity and 99.4% specificity for radiographs (XR), 100% sensitivity and 97.3% specificity for MRI, and 97.6% sensitivity and 98.5% specificity for CT. Misclassifications were limited and occurred mainly between XR and CT images.

| Predicted |
| --- |

## Confusion matrix for projection classification (UNI-based model). Fetlock vs. non-fetlock classification with 97.2% test accuracy, 98.3% sensitivity, and 96.4% specificity.

|  | Predicted |  |
| --- | --- | --- |
| Ground Truth | Fetlock | Non-Fetlock |
| Fetlock (120) | 118 | 2 |
| Non-Fetlock (84) | 3 | 81 |

## Confusion matrix for projection classification (UNI-based model) and detailed projection classification (oblique [DMPLO/DLPMO], dorsopalmar [DP], and lateromedial [LM]) showing strong differentiation of oblique and DP views, with reduced sensitivity for LM views due to anatomical overlap.

| Predicted |
| --- |

## Fracture detection performance in equine datasets. Results are reported as median values with interquartile ranges (IQRs) to reflect variation across individual images.

| Dataset | IoU (Median [IQR]) | Sensitivity (Median [IQR]) | Specificity (Median [IQR]) | Accuracy (Median [IQR]) |
| --- | --- | --- | --- | --- |
| Training (Hospital-acquired) | 0.76 [0.72-0.80] | 92.3% [89.5-94.1] | 86.4% [82.1-88.7] | 89.4% [85.8-91.4] |
| Training (Literature-derived) | 0.71 [0.65-0.75] | 84.0% [81.2-86.8] | 78.9% [75.3-82.4] | 81.5% [78.3-84.6] |
| Test set | 0.84 [0.80-0.87] | 88.5% [86.1-91.0] | 81.7% [79.0-84.2] | 85.1% [82.6-87.6] |

## Fracture detection performance across species from 10% test dataset. Results are reported as median values with interquartile ranges (IQRs) to reflect variation across individual images.

| Dataset | IoU (Median [IQR]) | Sensitivity (Median [IQR]) | Specificity (Median [IQR]) |
| --- | --- | --- | --- |
| Human | 0.79 [0.75-0.82] | 95.2% [93.0-97.1] | 92.8% [90.4-94.9] |
| Feline | 0.74 [0.70-0.77] | 87.6% [85.0-89.8] | 84.2% [81.5-86.7] |

### Formule


$$Q = XW Q , K = XW K , V = XW V where W Q , W K , W V ∈ R d×d k . Attention was then calculated as Attention(Q, K, V) = softmax( QK T √ d k )V$$

### Formule


$$L f ocal = - N ∑ i = 1 α i (1 -p i ) γ y i log(p i ) (1$$

### Formule


$$)$$

### Formule


$$L entropy = - N ∑ i = 1 p i (x)log(p i (x)),(2)$$

### Formule


$$L comb = L BCE + λyL IoU L BCE = -[ylog(p) + (1 -y)log(1 -p)] L IoU = 1 - |Bp ∩ B gt | |Bp∪ B gt |(3)$$
