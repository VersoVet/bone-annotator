# Diffusion-Based Anonymization and Foundation Model-Powered Semi-Automatic Image Annotation for Privacy-Protective Intelligent Connected Vehicle Traffic Data

**Auteurs** : Tong Wang, Hui Xie, Feng Gao, Zian Meng, Pengcheng Zhang, Guohao Duan
**Année** : 2026
**DOI** : 10.3390/wevj17020070

## Résumé

Large-scale collection and annotation of sensitive facial data in real-world traffic scenarios face significant hurdles regarding privacy protection, temporal consistency, and high costs. To address these issues, this work proposes an integrated method specifically designed for sensitive information anonymization and semi-automatic image annotation (AIA). Specifically, the Nullface anonymization model is applied to remove identity information from facial data while preserving non-identity attributes including pose, expression, and background that are relevant to downstream vision tasks. Secondly, the Qwen3-VL multimodal foundation model is combined with the Grounding DINO detection model to build an end-to-end annotation platform using the Dify workflow, covering data cleaning and automated labeling. A traffic-sensitive information dataset with diverse and complex backgrounds is then constructed. Subsequently, the systematic experiments on the WIDER FACE subset show that Nullface signi

## Méthodologie

{'study_design': "Étude expérimentale comparant des méthodes d'anonymisation (Nullface vs FAMS et Ciagan) et des méthodes d'annotation (manuelle, semi-automatique proposée, AWS) sur des données d'images de trafic", 'intervention': "Application du modèle de diffusion Nullface pour l'anonymisation faciale suivie d'une annotation semi-automatique combinant Qwen3-VL et Grounding DINO via le workflow Dify, puis entraînement du détecteur YOLOv8 sur les jeux de données annotés", 'control': "Annotation manuelle et méthode d'annotation automatique AWS (Amazon Web Services SageMaker Ground Truth) utilisées comme comparaison", 'primary_outcomes': ["Préservation de la pose de la tête et qualité d'image après anonymisation", "Précision de détection d'objets (accuracy) après annotation"], 'secondary_outcomes': ['Scores de confiance des prédictions du détecteur', 'Précision (precision) des modèles entraînés'], 'statistical_methods': [], 'duration': None, 'setting': 'Scénarios de trafic réel avec images capturées par caméras de véhicules connectés intelligents'}

## Résultats

{'quantitative': [{'outcome': 'Re-ID (reidentification) score - NullFace vs FAMS vs Ciagan on WIDER FACE and RealFace datasets', 'value': 'NullFace achieves the lowest Re-ID scores among the three methods on both datasets', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'Among them, NullFace achieves the lowest Re-ID scores on both datasets, indicating the most effective identity anonymization performance.'}, {'outcome': 'Head pose (pitch angle) quaternion angular distance - NullFace vs FAMS', 'value': 'NullFace slightly worse than FAMS on pitch angle metric', 'unit': 'quaternion angular distance', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'NullFace performs slightly worse than FAMS on the pitch angle metric but shows a clear improvement over Ciagan.'}, {'outcome': 'Head pose (pitch angle) quaternion angular distance - NullFace vs Ciagan', 'value': 'NullFace shows clear improvement over Ciagan', 'unit': 'quaternion angular distance', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'NullFace performs slightly worse than FAMS on the pitch angle metric but shows a clear improvement over Ciagan.'}, {'outcome': 'FID (Fréchet Inception Distance) - NullFace vs Ciagan on WIDER FACE and RealFace datasets', 'value': 'NullFace achieved the lowest FID on both datasets, substantially outperforming Ciagan', 'unit': 'FID score', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'The proposed method achieved the best result and yielded the lowest FID on both datasets, substantially outperforming Ciagan.'}, {'outcome': 'MUSIQ score difference between generated and original images - NullFace vs FAMS on WIDER FACE dataset', 'value': 'FAMS produced higher MUSIQ scores but larger MUSIQ distance from original images; NullFace retained original image quality with smaller distance', 'unit': 'MUSIQ score / distance', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'On the WIDER FACE dataset, methods like FAMS produced higher MUSIQ scores but generated larger MUSIQ distance from the original images because they performed visible enhancement.'}], 'qualitative_findings': ['All three anonymization methods reduce identity reidentification rates.', 'NullFace exhibits more stable performance in expression consistency and gaze direction error compared to FAMS and Ciagan.', 'NullFace effectively removes identity information while preserving the original facial geometry and semantic attributes, supporting downstream detection tasks.', 'By contrast, due to the inversion process, NullFace preserves the source image quality instead of applying unnatural enhancement.', 'In single-person conditions (occluded and extreme-angle faces), NullFace effectively anonymizes identity while preserving pose, expression, and background, with visually realistic outputs.', 'NullFace does not introduce obvious artifacts or geometric distortions, and does not break scene layout, accessories, or other details relevant to downstream tasks.', 'FAMS failed to preserve participant expressions.', 'Ciagan produced less realistic outputs and missed anonymization targets.', 'In two-person scenes, NullFace can anonymize multiple participants in the same image and generate internally consistent and mutually distinguishable new identities for each participant.', "Across different viewpoints, each participant's facial appearance remains coherent in expression and pose while background details are preserved.", 'Other methods often mix faces or produce inconsistent poses and expressions for multiple people.', 'NullFace remains stable in two-person scenes and produces high-quality anonymization, demonstrating stronger adaptation to complex scenarios and better privacy protection.'], 'main_findings': ['NullFace achieves the best identity anonymization (lowest Re-ID scores) among the compared methods on both WIDER FACE and RealFace datasets.', 'NullFace achieves the best image quality (lowest FID) among the compared methods, substantially outperforming Ciagan.', 'NullFace better preserves identity-independent attributes (pose, expression, gaze) and original image quality compared to FAMS and Ciagan, and generalizes well to single- and two-person scenes including occluded and extreme-angle faces.']}

## Conclusions

The NullFace diffusion anonymization method shows superior performance in complex traffic scenes, achieving the lowest reidentification rate while effectively preserving head pose, facial expression, and gaze direction. NullFace attains the lowest FID and MUSIQ scores, indicating superior visual quality, and outperforms mainstream techniques in producing high-quality and realistic anonymized images that remain close to the original image distribution while maintaining consistency across scenarios. The semi-AIA system, integrating Qwen3-VL, Grounding DINO, and Deepseek-R1, automates the full pipeline from data cleaning to standardized output, balancing processing efficiency and label quality. Detection metrics for models trained on data from this pipeline match those trained on manual labels and are significantly better than results from the AWS auto-labeling service. The tightly coupled anonymization and semi-AIA pipeline preserves downstream usability; YOLOv8 comparison experiments show that models trained on data processed and labeled by the proposed method retain detection performance comparable to pre-anonymization levels. The anonymization did not damage the geometric and semantic context critical for downstream vision tasks. This work fills a gap in applying generative anonymization and automatic annotation to real traffic scenes, providing a reference for future research on privacy protection and intelligent annotation for larger-scale, multimodal, and cross-domain traffic data.

## Comparison of the proposed method with existing methods.

| Comparison Dimensions | Existing Anonymization and Annotation Pipelines | Proposed Method |
| --- | --- | --- |
| Assumption on data distribution | Requires strong consistency between unlabeled and labeled data | No strict distribution consistency required |
| Unseen category annotation | Limited or unsupported | Supported |
| Generalization capability | Limited by training data coverage | Enhanced through large model capabilities |
| Suitability for the transportation domain | Limited | Validated and effective for transportation scenarios |
| Retain key |  |  |
| non-identity-related | Limited | Strength |
| attributes |  |  |

## Performance comparison of different annotation methods.

| Process Step Name | Single-Step Time Consumption |  |  |
| --- | --- | --- | --- |
| YOLO format label output | 233.484 ms | √ | √ |
| Total time | - | ≈14.92 s | ≈6.12 s |

## The number of images in the dataset before and after filtering.

| Original | Filtered Dataset |
| --- | --- | --- |
| Dataset Size | Easy | Medium |

## Nullface Hyperparameter Configuration.

| Parameter | Meaning | Value |
| --- | --- | --- |
| N | Number of diffusion steps | 100 |
| T skip | Number of steps to skip in the reverse process | 70 |
| λ id | Anonymization strength parameter | 1 |
| λ c f g | Guidance scale for diffusion | 10 |
| λ scl | IP-Adapter conditional channel strength coefficient | 1 |
| η |  |  |

## Comparison of face anonymization methods on the WIDER FACE dataset.

|  |  |  | Head Pose |  | Expression | Gaze |  | Image Quality |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Re-ID | Yaw | Pitch | Roll | Consistency | MAE | MUSIQ | MUSIQ Distance | FID | Light |
| Original image | 1 | 0 | -0 | 00 | - | - | 69.88 | 0 | 0 | 0 |
| NullFace | 0.29 | -0.92 | -0.4 | -0.41 | 0.95 | 9.96 | 69.98 | 0.10 | 33.09 | 0.93 |
| FAMS | 0.36 | -0.84 | 0.37 | -0.33 | 0.86 | 17.27 | 70.73 | 0.85 | 64.67 | 0.94 |
| Ciagan | 0.61 | -5.23 | 0.69 | 1.52 | 0.78 | 35.12 | 59.68 | 10.20 | 180.8 | 0.77 |

## Comparison of face anonymization methods on the RealFace dataset.

|  | Re-ID |  | Head Pose |  | Expression | Gaze |  | Image Quality |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Yaw | Pitch | Roll | Consistency | MAE | MUSIQ | MUSIQ Distance | FID | Light |
| Original image | 1 | 0 | 0 | 0 | - | - | 59.34 | 0 | 0 | 0 |
| NullFace | 0.14 | 0.08 | -0.25 | 0.02 | 0.98 | 5.11 | 58.88 | 0.34 | 19.24 | 0.99 |
| FAMS | 0.33 | -2.46 | -0.14 | -0.55 | 0.93 | 10.70 | 58.68 | 0.66 | 50.35 | 0.97 |
| Ciagan | 0.41 | -1.38 | -1.12 | -0.09 | 0.89 | 14.26 | 55.71 | -3.17 | 79.41 | 0.90 |

## Performance comparison of different annotation methods on the WIDER FACE and Real-Face dataset.

|  | Train mAP@50:95 | Test mAP@50:95 | P |  | R |  |  | F1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | WIDER FACE | RealFace | WIDER FACE | RealFace | WIDER FACE | RealFace | WIDER FACE | RealFace | WIDER FACE | RealFace |
| AWS | 42.81% | 43.27% | 42.98% | 43.10% | 90.08% | 91.69% | 84.37% | 86.05% | 83.68% | 84.26% |
| Proposed method | 43.12% | 43.95% | 43.63% | 44.02% | 91.05% | 92.14% | 85.21% | 86.57% | 85.72% | 85.12% |
| Manual annotations | 43.23% | 44.03% | 43.54% | 44.67% | 91.20% | 92.87% | 85.16% | 86.83% | 86.90% | 85.84% |

### Formule


$$z t = x t-1 -µ t (x t , c) σ t , t = T, . . . , 1(1)$$

### Formule


$$Input: Original image x 0 Initialize latent state x ← x 0 and noise trajectory Z ← ∅ for t = 1, T do Compute unconditional mean µ t (x t , c) Calculate noise term z t ← µ t (x t ,c) σ t Update state x ← x + σ t • z t Store z t in trajectory Z end for Return inverted latent x T and noise trajectory Z = {z t } T t-1$$

### Formule


$$εθ (x t , c id , ∅) = λ c f g • ϵ θ (x t , c id ) + 1 -λ c f g • ϵ θ (x t , ∅)(2)$$

### Formule


$$ϵ θ = M • εθ + (1 -M) • ϵ θ (x t , ∅)(3)$$

### Formule


$$error = arccos (g • ĝ) |g|•| ĝ| (4)$$

### Formule


$$FID = ∥µ r -µ g ∥ 2 2 + Tr Σ r + Σ g -2 Σ r Σ g$$

### Formule


$$P = 1 U U ∑ k=1 Correct(l k ) Predicted(l k ) (6) R = 1 U U ∑ k=1 Correct(l k ) Ground(l k )(7)$$

### Formule


$$F1 = 2PR P + R(8)$$
