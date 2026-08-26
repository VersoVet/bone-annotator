# Fracture detection in pediatric wrist trauma X-ray images using YOLOv8 algorithm

**Auteurs** : Rui‐Yang Ju, Weiming Cai
**Année** : 2023
**DOI** : 10.1038/s41598-023-47460-7

## Résumé

Abstract
                  Hospital emergency departments frequently receive lots of bone fracture cases, with pediatric wrist trauma fracture accounting for the majority of them. Before pediatric surgeons perform surgery, they need to ask patients how the fracture occurred and analyze the fracture situation by interpreting X-ray images. The interpretation of X-ray images often requires a combination of techniques from radiologists and surgeons, which requires time-consuming specialized training. With the rise of deep learning in the field of computer vision, network models applying for fracture detection has become an important research topic. In this paper, we use data augmentation to improve the model performance of YOLOv8 algorithm (the latest version of You Only Look Once) on a pediatric wrist trauma X-ray dataset (GRAZPEDWRI-DX), which is a public dataset. The experimental results show that our model has reached the state-of-the-art (SOTA) mean average precision (mAP 50). Specifically, mAP 50 of our model is 0.638, which is significantly higher than the 0.634 and 0.636 of the improved YOLOv7 and original YOLOv8 models. To enable surgeons to use our model for fracture detection on pediatric wrist trauma X-ray images, we have designed the application “Fracture Detection Using YOLOv8 App” to assist surgeons in diagnosing fractures, reducing the probability of error analysis, and providing more useful information for surgery.

## Méthodologie

{'study_design': "Étude expérimentale de deep learning : entraînement, validation et test d'un modèle de détection d'objets (YOLOv8) sur un jeu de données d'images radiographiques, avec et sans augmentation de données, comparaison à des modèles de référence (YOLOv7, YOLOv7+CBAM, YOLOv7+GAM, YOLOv8 original)", 'intervention': "Entraînement du modèle YOLOv8 avec augmentation de données (ajustement du contraste et de la luminosité via la fonction addWeighted d'OpenCV, avec α=1.2 et γ=30), étendant le jeu d'entraînement de 14 204 à 28 408 images", 'control': 'Modèle YOLOv8 original sans augmentation de données ; modèles YOLOv7, YOLOv7 avec CBAM, YOLOv7 avec GAM', 'primary_outcomes': ['mean Average Precision (mAP 50)'], 'secondary_outcomes': ["Temps d'inférence (ms)", 'Précision et rappel par classe (fracture, metal, text, bone-anomaly)', 'Nombre de paramètres et FLOPs'], 'statistical_methods': ['Intersection over Union (IoU)', 'Precision-Recall Curve', 'F1-score', 'Task Aligned Assigner (TOOD)', 'Binary Cross-Entropy Loss', 'Distribution Focal Loss (DFL)', 'Complete IoU (CIoU) Loss'], 'duration': None, 'setting': 'Jeu de données public GRAZPEDWRI-DX (images radiographiques du poignet pédiatrique) ; entraînement sur GPU GeForce RTX 3080Ti 12GB'}

## Résultats

{'quantitative': [{'outcome': 'mAP 50 du modèle proposé (avec augmentation de données)', 'value': '0.638', 'unit': 'mAP50', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'mAP 50 of our model is 0.638, which is significantly higher than the 0.634 and 0.636 of the improved YOLOv7 and original YOLOv8 models.'}, {'outcome': 'mAP 50 du YOLOv7 amélioré', 'value': '0.634', 'unit': 'mAP50', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'mAP 50 of our model is 0.638, which is significantly higher than the 0.634 and 0.636 of the improved YOLOv7 and original YOLOv8 models.'}, {'outcome': 'mAP 50 du YOLOv8 original', 'value': '0.636', 'unit': 'mAP50', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'mAP 50 of our model is 0.638, which is significantly higher than the 0.634 and 0.636 of the improved YOLOv7 and original YOLOv8 models.'}, {'outcome': 'mAP 50 pour la classe bone-anomaly, modèle YOLOv8s de base', 'value': '0.11', 'unit': 'mAP50', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Ablation study', 'source_quote': 'On the opposite, the detection ability of bone-anomaly is poor, with mAP 50 of 0.11.'}, {'outcome': 'mAP 50 pour la classe bone-anomaly, avec augmentation de données', 'value': '0.169', 'unit': 'mAP50', 'confidence_interval': None, 'p_value': None, 'effect_size': 'augmentation de 53.6%', 'source_section': 'Ablation study', 'source_quote': 'Compared with YOLOv8s model, the mAP value predicted by the model using our training method for bone-anomaly increased from 0.11 to 0.169, an increase of 53.6%.'}, {'outcome': "mAP 50, YOLOv8m (taille d'image 640) avant/après augmentation", 'value': 'de 0.621 à 0.629', 'unit': 'mAP50', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Experimental results', 'source_quote': 'Specifically, when the input image size is 640, compared with YOLOv8m model and YOLOv8l model, the mAP 50 of our model improves from 0.621 to 0.629, and from 0.623 to 0.637, respectively.'}, {'outcome': "mAP 50, YOLOv8l (taille d'image 640) avant/après augmentation", 'value': 'de 0.623 à 0.637', 'unit': 'mAP50', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Experimental results', 'source_quote': 'Specifically, when the input image size is 640, compared with YOLOv8m model and YOLOv8l model, the mAP 50 of our model improves from 0.621 to 0.629, and from 0.623 to 0.637, respectively.'}, {'outcome': "Temps d'inférence CPU (YOLOv8m et YOLOv8l) avant/après augmentation", 'value': 'de 536.4 ms et 1006.3 ms à 685.9 ms et 1370.8 ms', 'unit': 'ms', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Experimental results', 'source_quote': 'Although the inference time on the CPU is increased from 536.4 ms and 1006.3 ms to 685.9 ms and 1370.8 ms, respectively, the number of parameters and FLOPs are the same'}, {'outcome': "Taille du jeu d'entraînement (avec augmentation de données)", 'value': '28408', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Proposed method', 'source_quote': 'where the training set is expanded to 28,408 X-ray images by data augmentation from the original 14,204 X-ray images.'}, {'outcome': 'Répartition du jeu de données', 'value': 'training 14204 (69.88%), validation 4094 (20.14%), test 2029 (9.98%)', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'Specifically, our training set consists of 14,204 images (69.88%), our validation set consists of 4,094 images (20.14%), and our test set consists of 2029 images (9.98%).'}, {'outcome': "Pourcentage d'images radiographiques mal interprétées (revue de la littérature)", 'value': '26%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Introduction', 'source_quote': 'According to the survey 7,8 , the percentage of X-ray images misinterpreted have reached 26%.'}], 'qualitative_findings': ['Le modèle a une bonne capacité de détection pour les fractures uniques, mais la précision est fortement affectée par les perforations métalliques et les fractures multiples denses'], 'main_findings': ['Le modèle proposé (YOLOv8 + augmentation de données) atteint une performance state-of-the-art (SOTA) en mAP 50 (0.638), supérieure au YOLOv7 amélioré (0.634) et au YOLOv8 original (0.636)', "L'augmentation de données (ajustement contraste/luminosité) améliore particulièrement la détection de la classe 'bone-anomaly', la plus difficile à détecter", "L'optimiseur SGD nécessite moins d'époques que Adam pour atteindre la meilleure performance, mais les différences de mAP et de temps d'inférence entre les deux sont faibles", "Le modèle YOLOv8s avec taille d'image 1024 a été retenu pour l'application finale en raison de ses performances", "Une application GUI nommée 'Fracture Detection Using YOLOv8 App' a été développée avec PySide6 pour assister les chirurgiens pédiatriques"]}

## Conclusions

L'application du modèle YOLOv8 avec augmentation de données à la détection de fractures du poignet pédiatrique permet d'atteindre des performances état de l'art (SOTA) en mAP 50 L'application développée ('Fracture Detection Using YOLOv8 App') vise à assister les chirurgiens pédiatriques dans l'interprétation des radiographies, réduire les erreurs de classification et fournir une meilleure base d'information pour la chirurgie Le modèle entraîné peut servir de modèle pré-entraîné pour la détection de fractures dans d'autres parties du corps que le poignet pédiatrique

## used data augmentation with YOLOv5 model to detect rib fractures in CXR images. And Burkow et al.

| Author | Task | Model | Dataset | mAP val 50 |
| --- | --- | --- | --- | --- |
| Guan et al. 38 | Thigh fracture detection DCFPN | 3842 thigh fracture X-ray radiographs | 0.821 |
| Wang et al. 39 | Thigh fracture detection R-CNN | 3842 thigh fracture X-ray radiographs | 0.878 |
| Guan et al. 40 | Arm fracture detection | R-CNN | Musculoskeletal-Radiograph (MURA) 41 0.620 |
| Wu et al. 42 | Bone fracture detection | FAMO | 9040 radiographs of various body parts | 0.774 |
| Ma and Luo 43 | Bone fracture detection | Faster R-CNN 1052 bone x-ray images | 0.884 |
| Xue et al. 44 | Hand fracture detection Faster R-CNN 3067 hand trauma x-ray images | 0.700 |
| Sha et al. 45 | Spine fracture detection Faster R-CNN 5134 spine fractures CT images | 0.733 |
| Sha et al. 46 | Spine fracture detection YOLOv2 | 5134 spine fractures CT images | 0.753 |

## Medical University of Graz provides a public dataset named GRAZPEDWRI-DX

| ν = | 4 π 2 (arctan | w gt h gt -arctan | w p h p ) 2 , |
| --- | --- | --- | --- |

## Validation results of YOLOv8 for each class on the GRAZPEDWRI-DX dataset when the input image size is 1024.

|  |  |  |  |  | mAP val | mAP val |
| --- | --- | --- | --- | --- | --- | --- |
| Class | Boxes Instances Precision Recall | 50 | 50-95 |
| All | 47435 9613 | 0.674 | 0.605 | 0.623 | 0.395 |
| Boneanomaly | 276 | 53 | 0.505 | 0.094 | 0.110 | 0.035 |
| Bonelesion | 45 | 8 | 0.629 | 0.250 | 0.416 | 0.212 |
| Fracture | 18090 3740 | 0.885 | 0.903 | 0.947 | 0.572 |
| Metal | 818 | 168 | 0.878 | 0.899 | 0.920 | 0.768 |
| Periostealreaction | 3453 | 697 | 0.645 | 0.684 | 0.689 | 0.357 |
| Pronatorsign | 567 | 104 | 0.561 | 0.713 | 0.611 | 0.338 |
| Softtissue | 464 | 89 | 0.324 | 0.315 | 0.251 | 0.125 |
| text | 23722 4754 | 0.961 | 0.984 | 0.991 | 0.750 |

## Validation results of our model for each class on the GRAZPEDWRI-DX dataset when the input image size is 1024.

|  |  |  |  |  | mAP val | mAP val |
| --- | --- | --- | --- | --- | --- | --- |
| Class | Boxes Instances Precision Recall | 50 | 50-95 |
| All | 47435 9613 | 0.694 | 0.592 | 0.631 | 0.402 |
| Boneanomaly | 276 | 53 | 0.510 | 0.151 | 0.169 | 0.076 |
| Bonelesion | 45 | 8 | 0.658 | 0.243 | 0.414 | 0.213 |
| Fracture | 18090 3740 | 0.899 | 0.896 | 0.947 | 0.569 |
| Metal | 818 | 168 | 0.898 | 0.890 | 0.924 | 0.780 |
| Periostealreaction | 3453 | 697 | 0.721 | 0.654 | 0.700 | 0.359 |
| Pronatorsign | 567 | 104 | 0.534 | 0.683 | 0.611 | 0.342 |
| Softtissue | 464 | 89 | 0.367 | 0.236 | 0.241 | 0.120 |
| text | 23722 4754 | 0.961 | 0.981 | 0.991 | 0.754 |

## Model performance comparison of YOLOv8 models using SGD and Adam optimizers. For training with the SGD optimizer, the initial learning rate is 1 ×10 -2 ; for training with the Adam optimizer, the initial learning rate is 1 ×10 -3 .

|  |  |  |  | mAP val | mAP val | Speed GPU |
| --- | --- | --- | --- | --- | --- | --- |
| Model | Size | Optimizer Best Epoch | 50 | 50-95 | RTX 3080Ti (ms) |
| YOLOv8s | 640 SGD | 56 | 0.611 | 0.389 | 4.4 |
| YOLOv8s | 640 Adam | 57 | 0.604 | 0.383 | 4.3 |
| YOLOv8s | 1024 SGD | 36 | 0.623 | 0.395 | 5.4 |
| YOLOv8s | 1024 Adam | 47 | 0.625 | 0.399 | 4.9 |
| YOLOv8m | 640 SGD | 52 | 0.621 | 0.396 | 4.9 |
| YOLOv8m | 640 Adam | 62 | 0.621 | 0.403 | 5.5 |
| YOLOv8m | 1024 SGD | 35 | 0.624 | 0.402 | 9.9 |
| YOLOv8m | 1024 Adam | 70 | 0.626 | 0.401 | 10.0 |

## Quantitative comparison of fracture detection when the input image size is 640. Speed means the total time of validate per image, and the total time includes the preprocessing, inference, and post-processing time.

| Model |
| --- |

## mAP val 50 mAP val 50-95 Speed CPU Intel Core i5 (ms) Speed GPU RTX 3080Ti (ms) PARAMS (M) FLOPs (B)

| YOLOv5n | 0.589 | 0.339 | \ | 2.8 | 1.77 | 4.2 |
| --- | --- | --- | --- | --- | --- | --- |
| YOLOv8n | 0.601 | 0.374 | 67.4 | 2.9 | 3.01 | 8.1 |
| Ours | 0.605 | 0.379 | 111.3 | 3.4 | 3.01 | 8.2 |
| YOLOv5s | 0.601 | 0.357 | \ | 3.3 | 7.03 | 15.8 |
| YOLOv8s | 0.604 | 0.383 | 191.5 | 4.3 | 11.13 | 28.5 |
| Ours | 0.612 | 0.392 | 285.1 | 4.9 | 11.13 | 28.7 |
| YOLOv5m | 0.613 | 0.371 | \ | 4.0 | 20.89 | 48.0 |
| YOLOv8m | 0.621 | 0.403 | 536.4 | 5.5 | 25.84 | 78.7 |
| Ours | 0.629 | 0.404 | 685.9 | 5.1 | 25.84 | 78.7 |
| YOLOv5l | 0.620 | 0.379 | \ | 5.6 | 46.15 | 107.8 |
| YOLOv8l | 0.624 | 0.403 | 1006.3 | 7.4 | 43.61 | 164.9 |
| Ours | 0.637 | 0.406 | 1370.8 | 7.2 | 43.61 | 164.9 |

## Quantitative comparison of fracture detection when the input image size is 1024. Speed means the total time of validate per image, and the total time includes the preprocessing, inference, and post-processing time.

|  | mAP val | mAP val | Speed CPU | Speed GPU |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Model | 50 | 50-95 | Intel Core i5 (ms) | RTX 3080Ti (ms) PARAMS (M) FLOPs (B) |
| YOLOv5n | 0.600 | 0.347 | \ | 3.2 | 1.77 | 4.2 |
| YOLOv8n | 0.605 | 0.387 | 212.1 | 3.3 | 3.01 | 8.1 |
| Ours | 0.608 | 0.391 | 260.4 | 4.4 | 3.01 | 8.1 |
| YOLOv5s | 0.622 | 0.371 | \ | 4.4 | 7.03 | 15.8 |
| YOLOv8s | 0.625 | 0.399 | 519.5 | 4.9 | 11.13 | 28.5 |
| Ours | 0.631 | 0.402 | 717.1 | 6.2 | 11.13 | 28.5 |
| YOLOv5m | 0.624 | 0.380 | \ | 7.1 | 20.89 | 48.0 |
| YOLOv8m | 0.626 | 0.401 | 1521.5 | 10.0 | 25.84 | 78.7 |
| Ours | 0.635 | 0.411 | 1724.4 | 9.4 | 25.85 | 78.7 |
| YOLOv5l | 0.626 | 0.378 | \ | 11.3 | 46.15 | 107.8 |
| YOLOv8l | 0.636 | 0.404 | 2671.1 | 15.1 | 43.61 | 164.9 |
| Ours | 0.638 | 0.415 | 3864.5 | 13.6 | 43.61 | 164.9 |

## Evaluation of wrist fracture detection with other state-of-the-art (SOTA) models on the GRAZPEDWRI-DX dataset.

|  |  |  |  | mAP val |
| --- | --- | --- | --- | --- |
| Model | Precision Recall F1 | 50 |
| YOLOv5 53 | 0.682 | 0.581 | 0.607 0.626 |
| YOLOv7 32 | 0.556 | 0.582 | 0.569 0.628 |
| YOLOv7 32 + CBAM 70 | 0.709 | 0.593 | 0.646 0.633 |
| YOLOv7 32 + GAM 71 | 0.745 | 0.574 | 0.646 0.634 |
| YOLOv8 36 | 0.694 | 0.679 | 0.623 0.636 |
| Ours | 0.734 | 0.592 | 0.635 0.638 |

### Formule


$$Output = Input 1 × α + Input 2 × β + γ ,$$

### Formule


$$t = s α × u β , (3) Loss n = -w y n log x n + 1 -y n log (1 -x n ) , (4) DFL(S n , S n+1 ) = -((y n+1 -y) log(S n ) + (y -y n ) log(S n+1 )), (5) S n = y n+1 -y y n+1 -y n , S n+1 = y -y n y n+1 -y n . (6$$

### Formule


$$) CIoU Loss = 1 -IoU + Distance 2 2 Distance 2 C + v 2 (1 -IoU) + ν ,(7)$$

### Formule


$$IoU = area(C) ∩ area(G) area(C) ∪ area(G) ,(9)$$

### Formule


$$Recall = T P T P + F N , Precision = T P T P + F P ,(10)$$

### Formule


$$F-score = 1 + β 2 × Precision × Recall β 2 × Precision + Recall (11) F 1 = 2 × Precision × Recall Precision + Recall = 2T P 2T P + F P + F N$$
