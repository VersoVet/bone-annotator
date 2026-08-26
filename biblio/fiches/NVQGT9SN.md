# VisioFirm: Cross-Platform AI-assisted Annotation Tool for Computer Vision

**Auteurs** : Safouane El Ghazouali, Umberto Michelucci
**Année** : 2025

## Résumé

AI models rely on annotated data to learn pattern and perform prediction. Annotation is usually a labor-intensive step that require associating labels ranging from a simple classification label to more complex tasks such as object detection, oriented bounding box estimation, and instance segmentation. Traditional tools often require extensive manual input, limiting scalability for large datasets. To address this, we introduce VisioFirm, an open-source web application designed to streamline image labeling through AI-assisted automation. VisioFirm integrates state-of-the-art foundation models into an interface with a filtering pipeline to reduce human-in-the-loop efforts. This hybrid approach employs CLIP combined with pre-trained detectors like Ultralytics models for common classes and zero-shot models such as Grounding DINO for custom labels, generating initial annotations with low-confidence thresholding to maximize recall. Through this framework, when tested on COCO-type of classes,

## Méthodologie

{'study_design': "Présentation d'un outil (VisioFirm) et évaluation par benchmark comparant l'accélération matérielle (CPU vs GPU) et différents seuils de confiance sur un pipeline hybride combinant CLIP, détecteurs Ultralytics (YOLOv10), Grounding DINO (zero-shot) et SAM2", 'intervention': 'Pipeline de pré-annotation assisté par IA (VFPreAnnotator) utilisant un seuillage de confiance bas pour maximiser le rappel, une vérification sémantique via CLIP sur les régions détectées, un clustering par composantes connexes IoU-Graph pour supprimer les redondances, et une segmentation SAM2 accélérée par WebGPU', 'control': "Comparaison entre exécution CPU (Intel Core i9-12th-12900K) et GPU (NVIDIA RTX A6000, 48 Go VRAM), ainsi qu'entre seuils de confiance bas (0%) et plus élevés (50%)", 'primary_outcomes': ["Réduction de l'effort d'annotation manuelle", "Précision d'annotation (mAP@0.5)", "Latence d'inférence totale et par image"], 'secondary_outcomes': ['Taux de complétion des annotations', 'Distribution des classes annotées'], 'statistical_methods': ['Similarité cosinus et softmax pour la vérification sémantique CLIP', 'Intersection over Union (IoU) pour le clustering de composantes connexes', "mAP@0.5 pour l'évaluation de la précision d'annotation"], 'duration': None, 'setting': 'Expériences menées sur un CPU Intel Core i9-12th-12900K et un GPU NVIDIA RTX A6000 (48 GB VRAM)'}

## Résultats

{'quantitative': [{'outcome': "Réduction de l'effort manuel", 'value': '90%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Conclusion', 'source_quote': 'VisioFirm demonstrates up to 90% reduction in manual effort through benchmarks on diverse datasets, while maintaining high annotation accuracy'}, {'outcome': 'Vitesse de YOLOv10 comparée à Grounding DINO (seuils bas, GPU)', 'value': "jusqu'à 15x plus rapide", 'unit': 'facteur de vitesse', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Web Application Design', 'source_quote': 'For datasets with COCO-aligned classes, YOLOv10 is substantially faster than Grounding DINO (e.g., up to 15x at low thresholds on GPU), making it the preferred choice for common object annotation to optimize efficiency without compromising recall.'}, {'outcome': "Taux d'annotation complétée (exemple dashboard)", 'value': '93%', 'unit': '% images annotées', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Inference', 'source_quote': 'A pie chart depicting annotation completion status (e.g., 93% annotated across 100 images).'}, {'outcome': 'Seuil IoU pour clustering des détections redondantes', 'value': '> 0.9', 'unit': 'IoU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Pipeline Filtering and Post-Processing', 'source_quote': 'A graph G is constructed where nodes represent detections, and edges connect pairs with an Intersection over Union (IoU) greater than 0.9'}, {'outcome': 'Seuil de confiance bas pour maximiser le rappel', 'value': '10% ou moins', 'unit': '% confiance', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'VisioFirm Pre-annotator', 'source_quote': 'both with a low confidence threshold (such as 10% or less) to maximize recall'}], 'qualitative_findings': ['Les prédictions initiales sur des classes de type COCO se sont avérées majoritairement correctes', "Grounding DINO est efficace pour générer des propositions de labels sur des classes rares/non communes mais est plus lent sur l'ensemble du jeu de données"], 'main_findings': ["VisioFirm réduit l'effort manuel d'annotation jusqu'à 90% sur des jeux de données variés tout en préservant la qualité des annotations", "YOLOv10 est nettement plus rapide que Grounding DINO (jusqu'à 15x) pour les classes alignées sur COCO en utilisant l'accélération GPU", "La précision d'annotation (mAP@0.5) reste relativement stable mais avec quelques labels dupliqués, notamment lors de la segmentation combinant GroundingDINO Tiny et SAM2", "Des seuils de confiance plus élevés réduisent le nombre de détections à traiter, augmentant l'efficacité mais omettant certaines propositions de labels"]}

## Conclusions

VisioFirm est une application web open-source et multiplateforme qui répond aux défis de l'annotation de données intensive en main-d'œuvre en vision par ordinateur grâce à l'assistance IA Le pipeline de pré-annotation combinant détecteurs pré-entraînés et modèles zero-shot, avec seuillage à faible confiance et vérification sémantique CLIP, permet de maximiser le rappel tout en réduisant les redondances via le clustering IoU-Graph L'accélération côté navigateur via WebGPU pour la segmentation guidée par SAM2 permet des raffinements à la volée avec simplification de contour adaptative (Ramer-Douglas-Peucker)

## Summary of VisioFirm's Software Dependencies and Versions

| Component | Version | Description |
| --- | --- | --- |
| Python | 3.8+ | Core app designed on Python 3.10. |
| Flask | 2.0+ | Web framework for routing, authen- |
|  |  | tication, and API endpoints. |
| Ultralytics | 8.0+ | Library for YOLO model integration |
|  |  | and object detection inference. |
| Transformers | 4.30+ | Hugging Face library for Grounding |
|  |  | DINO and zero-shot models. |
| OpenAI-CLIP Latest | Semantic embedding model for label |
|  |  | verification and filtering. |
| Torch | 2.0+ | PyTorch framework for deep learn- |
|  |  | ing operations (CPU/GPU support). |
| NumPy | 1.24+ | Numerical computing for array ma- |
|  |  | nipulations in post-processing. |
| OpenCV | 4.8+ | Computer vision library for image |
|  |  | processing and contour handling. |
| NetworkX | 3.0+ | Graph library for IoU-based cluster- |
|  |  | ing algorithms. |
| SQLite3 | Standard Embedded database for local anno- |
|  |  | tation storage and queries. |

### Formule


$$(1)(2)$$

### Formule


$$s j = f(I k ) • g(l j ),(1)$$

### Formule


$$p j = exp(s j /τ) ∑ |L| m=1 exp(s m /τ) , (2$$

### Formule


$$)$$

### Formule


$$l * = arg max j p j .(3)$$

### Formule


$$IoU(b i , b j ) = |b i ∩ b j | |b i ∪ b j | , (4$$

### Formule


$$)$$

### Formule


$$A ij = w ij if j ∈ N i (k g ), 0 otherwise,(5)$$
