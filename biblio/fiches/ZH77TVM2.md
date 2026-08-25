# SegmentAnyBone: A universal model that segments any bone at any location on MRI.

**Auteurs** : Hanxue Gu, Roy Colglazier, Haoyu Dong, Jikai Zhang, Yaqian Chen, Zafer Yildiz, Yuwen Chen, Lin Li, Jichen Yang, Jay Willhite, Alex M Meyer, Brian Guo, Yashvi Atul Shah, Emily Luo, Shipra Rajput, Sally Kuehn, Clark Bulleit, Kevin A Wu, Jisoo Lee, Brandon Ramirez, Darui Lu, Jay M Levin, Maciej A Mazurowski
**Année** : 2025
**DOI** : 10.1016/j.media.2025.103469

## Résumé

Magnetic Resonance Imaging (MRI) is pivotal in radiology, offering non-invasive and high-quality insights into the human body. Precise segmentation of the MRIs into different organs and tissues would be very beneficial as it would allow more accurate measurements, which are essential for accurate diagnosis and effective treatment planning. Specifically, segmenting bones in MRI would allow for more quantitative assessments of musculoskeletal conditions, while such assessments are largely absent in current radiological practice. The difficulty of bone MRI segmentation is illustrated by the fact that limited algorithms are publicly available, and those contained in the literature typically address a specific anatomic area. In our study, we propose a versatile, publicly available deep learning model for bone segmentation in MRI at multiple standard MRI locations. The proposed model can operate in two modes: fully automated segmentation and prompt-based segmentation. Our contributions inclu

## Méthodologie

{'study_design': "Développement et évaluation d'un modèle de deep learning (SegmentAnyBone) basé sur l'extension du Segment Anything Model (SAM), pouvant fonctionner en mode segmentation automatique complète ou en mode segmentation basée sur des prompts, comparé à des architectures standards (Unet et variantes, modèles 3D, nn-Unet)", 'intervention': "Application de SegmentAnyBone incorporant des couches Adapter (Parameter Efficient FineTuning), une stratégie de prompting hybride, une branche d'attention de profondeur intégrant l'information de la 3ème dimension, et une augmentation par appariement de séquences non-T1 (T2, FLAIR) via mapping des annotations T1 par registration", 'control': 'Modèles standards de segmentation: Unet et ses variantes, modèles 3D-based, et nn-Unet', 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': "Entraînement conduit sur GPUs Nvidia RTX A6000, batch size de 8, 200 époques, optimiseur AdamW, taux d'apprentissage de 5e-4, phase de warmup des 200 premières itérations"}

## Résultats

{'quantitative': [{'outcome': 'DSC (Dice Similarity Coefficient) - Lumbar Spine', 'value': '73.5', 'unit': '%', 'confidence_interval': '95% CI [58.11%, 88.66%]', 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'the model exhibits a relatively lower performance level, recording a DSC of 73.5% (95% CI [58.11%, 88.66%])'}, {'outcome': 'IoU (Intersection over Union) - Lumbar Spine', 'value': '59.11', 'unit': '%', 'confidence_interval': '95% CI [40.45%, 77.8%]', 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'an IoU of 59.11% (95% CI [40.45%, 77.8%])'}], 'qualitative_findings': ['Le modèle présente des performances variables selon les localisations corporelles, avec une performance relativement plus faible dans la région de la colonne lombaire (Lumbar Spine)'], 'main_findings': ["SegmentAnyBone a été évalué dans divers scénarios : performance selon les localisations corporelles, comparaison externe avec d'autres méthodes, capacité de généralisation, bénéfices de l'utilisation simultanée de tous les types d'os par rapport à une utilisation individuelle, et performance en mode de segmentation interactive", 'Le modèle est globalement efficace mais certaines zones spécifiques, comme la colonne lombaire, nécessitent des améliorations supplémentaires']}

## Conclusions

SegmentAnyBone est une méthode novatrice qui atteint des performances état de l'art pour la segmentation des os sur IRM à travers différentes localisations corporelles et différentes séquences Le modèle atteint une performance moyenne de 86.87% DSC et 77.08% IoU en segmentant les os à travers différentes localisations corporelles, un score similaire à la variance causée par différents annotateurs SegmentAnyBone surpasse toutes les autres architectures standards en 2D et 3D lorsqu'il est testé sur la séquence T1 uniquement Le modèle se généralise bien à des cas non vus et peut être facilement adapté à d'autres tâches SegmentAnyBone excelle significativement dans des scénarios hors distribution (nouvelles localisations, séquences différentes, jeux de données externes), démontrant de robustes capacités d'apprentissage zero-shot SegmentAnyBone montre son efficacité en apprentissage few-shot, bénéficiant d'un pré-entraînement sur des volumes osseux annotés avant l'entraînement sur le jeu de données cible Le modèle valide le bénéfice d'obtenir un modèle globalement optimal pour tous les types d'os à travers différentes localisations corporelles plutôt qu'un modèle localement optimal pour une localisation spécifique SegmentAnyBone peut être utilisé de manière interactive grâce aux caractéristiques basées sur des prompts de SAM, et peut servir d'outil d'annotation précieux pour améliorer l'efficacité de l'annotation IRM Le mécanisme de depth-attention proposé permet d'intégrer l'information de dimension 3D dans la carte de caractéristiques d'une coupe et de préserver la structure 3D de l'os entre les coupes

## ∈ R C Z ×H Z ×W Z ). C Z represents the dimension of each embedding feature, and H Z and W Z signify the length and width of the latent feature embeddings, respectively. In the original SAM architecture, the image encoder processes

| Our proposed network includes two main branches: the 2D |
| --- |
| segmentation branch built and adapted based on the Seg- |
| ment Anything model (SAM), and the newly introduced 3D |
| low-resolution Attention branch. |
| 4.2.1 2D segmentation branch |
| SAM's Architecture. To elucidate our model's design |
| and the notations used in our study, we begin with an |
| overview of SAM's architecture. SAM consists of three |
| primary components: (1) image encoder: a vision trans- |
| former (ViT)-based component that encodes an input im- |
| age (denoted as X ∈ R H×W ) into a latent feature embed- |
| ding (Z |

## w) if P attn (h, w) <= p low α 2 * P attn (h, w) if P attn (h, w) > p low where p low = 0.05, and p high = 0.8, α 1 =

| p high p low = 16 and |
| --- |
| α 2 = |

## In particular, in the Ankle area, our model achieves impressive average performance with a DSC of 93.00% (95% Confidence Interval (CI) [92.10%, 93.84%]) and an IoU of 86.87% (95% CI [85.66%, 88.38%]). The performance in the Hip region is similarly strong, with a DSC of 91.88% (95% CI [88.92%, 94.79%]) and an IoU of 85.01% (95% CI [79.97%, 90.05%]). However, there is some variance in performance

| Our first evaluation focuses on the SegmentAnyBone model, |
| --- |
| with the best-performing model trained using a combined |
| dataset of T1 annotated cases and other paired cases. When |
| testing on annotated test cases on T1 sequences, the Seg- |
| mentAnyBone model demonstrates strong performance on |
| the test set, achieving an average Dice Similarity Coefficient |
| (DSC) of 86.36% and an average Intersection over Union |
| (IoU) of 77.08%. Figure 4 presents examples illustrating |
| our model's performance, showcasing both the quantitative |
| evaluation using DSC and IoU metrics, and a visual repre- |
| sentation of the predicted 3D bone volumes in comparison |
| with human annotations. The 3D visualizations show our |
| model's accuracy, with the predicted bone masks closely re- |
| sembling the bone shapes annotated by humans, even in |
| the complicated multi-bone and small-bone regions such as |
| Hand and Ankle. |

## SegmentAnybone 93.00 86.88 73.50 59.14 91.67 84.66 91.88 85.00 81.86 71.10 85.45 74.87 87.52 77.90 86.87 77.08 Comparison of performance across 2D and 3D segmentation methods on the test set when training on T1 and other paired sequences and testing on T1 only. "Lumbar" refers to "Lumbar Spine".

|  |  |  |  | Body location |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Method | Ankle | Lumbar | Knee | Hip | Elbow | Shoulder | Hand | Avg |
| 2D models |  |  |  |  |  |  |  |  |

### Formule


$$L T versky (α, β) = 1 - N i p i • g i N i p i • g i + α • N i p i • (1 -g i ) + β • N i (1 -p i ) • g i , (1)$$

### Formule


$$P V (h, w, d) = 0, if P V (h, w, d) <= ϵ attn .$$

### Formule


$$P attn-rescale (h, w) = α 1 * P attn (h,$$

### Formule


$$Z f use = g • Z + (1 -g) • F(Z • P attn ),(2)$$
