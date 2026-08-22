# A novel open-source ultrasound dataset with deep learning benchmarks for spinal cord injury localization and anatomical segmentation.

**Auteurs** : Kumar A, Kotkar K, Jiang K, Bhimreddy M, Davidar D, Weber-Levine C, Krishnan S, Kerensky MJ, Liang R, Leadingham KK
**Année** : 2025
**DOI** : 10.1038/s41598-025-16275-z

## Résumé

While deep learning has catalyzed breakthroughs across numerous domains, its broader adoption in clinical settings is inhibited by the costly and time-intensive nature of data acquisition and annotation. To further facilitate medical machine learning, we present an ultrasound dataset of 10,223 brightness-mode (B-mode) images consisting of sagittal slices of porcine spinal cords (N = 25) before and after a contusion injury. We additionally benchmark the performance metrics of several state-of-the-art object detection algorithms to localize the site of injury and semantic segmentation models to label the anatomy for comparison and creation of task-specific architectures. Finally, we evaluate the zero-shot generalization capabilities of the segmentation models on human ultrasound spinal cord images to determine whether training on our porcine dataset is sufficient for accurately interpreting human data. Our results show that the YOLOv8 detection model outperforms all evaluated models for

## Méthodologie

{'study_design': "Étude expérimentale de développement et benchmarking de modèles d'apprentissage profond (détection d'objets et segmentation sémantique) sur un dataset échographique porcine, avec évaluation de la généralisation zero-shot sur des images humaines.", 'intervention': "Lésion par contusion induite par chute de poids (20, 40 ou 60 grammes depuis une hauteur de 17 cm) après laminectomie chez le porc ; acquisition d'images échographiques B-mode avant et après lésion à l'aide d'un système Canon Aplio i800 avec transducteurs i22LH8 (20 MHz) ou i18LX5 (12 MHz).", 'control': "Images de moelle épinière saine (pré-lésion) comparées aux images post-lésion ; comparaison des modèles d'apprentissage profond avec une approche traditionnelle de traitement d'image (seuillage/contours).", 'primary_outcomes': ['Mean Average Precision (mAP50 et mAP50-95) pour la localisation de la lésion', 'Mean Intersection over Union (MIoU) et Mean Dice coefficient pour la segmentation anatomique'], 'secondary_outcomes': ['Average Recall (AR)', 'Vitesse (frames per second, FPS)', 'Charge de calcul CPU/GPU', 'Implantability score (score composite précision/vitesse/charge de calcul)', 'Généralisation zero-shot aux images humaines'], 'statistical_methods': ['mAP (mean Average Precision) à différents seuils IoU', 'Average Recall (AR)', 'Intersection over Union (IoU) moyen', 'Mean Dice coefficient', "Comparaison avec une méthode traditionnelle de traitement d'image (IoU moyen)"], 'duration': 'Collecte de données sur deux ans (2021-2022)', 'setting': "Johns Hopkins University (expérimentation animale approuvée par l'Animal Care and Use Committee, SW20M221) et Johns Hopkins Hospital (collecte de données humaines approuvée par l'IRB, IRB00273900)"}

## Résultats

{'quantitative': [{'outcome': 'mAP50-95 - YOLOv8 (localisation de la lésion)', 'value': '0.606', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Results', 'source_quote': 'Our results show that the YOLOv8 detection model outperforms all evaluated models for injury localization, achieving a mean Average Precision (mAP50-95) score of 0.606.'}, {'outcome': 'mAP50 - Faster RCNN et YOLOv8', 'value': '0.985 (Faster RCNN), 0.979 (YOLOv8)', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Injury localization', 'source_quote': 'it is evident that Faster RCNN and YOLOv8 show the strongest performance, achieving a mAP50 score of 0.985 and 0.979, respectively.'}, {'outcome': 'mAP50-95 - Faster RCNN', 'value': '0.524', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Injury localization', 'source_quote': 'These models also achieve the highest mAP50-95 score, which is a much more stringent metric for assessing model performance compared to mAP50, at 0.524 for Faster RCNN and 0.606 for YOLOv8.'}, {'outcome': 'Average Recall (AR) - YOLOv8', 'value': '0.644', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Injury localization', 'source_quote': 'YOLOv8 also attains the highest AR score at 0.644.'}, {'outcome': "IoU moyen - méthode de traitement d'image traditionnelle", 'value': '0.2034', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Injury localization', 'source_quote': 'On the same test set used to evaluate the deep learning models, this traditional method achieved an average IoU of 0.2034.'}, {'outcome': 'Implantability score - YOLOv8 (CPU et GPU)', 'value': '0.870 (CPU), 0.867 (GPU)', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Injury localization', 'source_quote': 'Our results indicate that YOLOv8 has optimal characteristics for injury localization for automatic monitoring with ultrasound-based implants for both CPU and GPU based applications, with a CPU implantability score of 0.870 and GPU implantability score of 0.867.'}, {'outcome': 'Mean Dice score - DeepLabv3 (anatomie porcine, données non vues)', 'value': '0.587', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Results, Spinal cord segmentation', 'source_quote': 'Our results indicate that DeepLabv3 outperforms all other segmentation models in terms of accuracy on porcine anatomy, with a Mean Dice score of 0.587'}, {'outcome': "Mean Dice score - SAMed (généralisation à l'anatomie humaine)", 'value': '0.445', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Results, Spinal cord segmentation', 'source_quote': 'SAMed generalizes best to human anatomy, achieving a Mean Dice score of 0.445.'}, {'outcome': 'Dice coefficient - TransUNet, classe moelle épinière (humain)', 'value': '0.853', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Spinal cord segmentation', 'source_quote': 'TransUNet generalizes best to human spinal cord, with a Dice coefficient of 0.853 for the spinal cord class.'}, {'outcome': 'Implantability score - SwinUNet (CPU) et DeepLabv3 (GPU) pour segmentation', 'value': '0.699 (SwinUNet, CPU), 0.702 (DeepLabv3, GPU)', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Spinal cord segmentation', 'source_quote': 'SwinUNet outperforms all other models for CPU-based chips with an implantability score of 0.699 and DeepLabv3 achieves the highest score for GPU-based devices at 0.702.'}], 'qualitative_findings': ["L'approche traditionnelle de traitement d'image a une performance raisonnable sur une image unique mais les règles manuelles pour créer les labels de tissus mous ne généralisent pas bien entre sujets et angles d'acquisition", 'Tous les modèles évalués montrent une performance réduite sur les images contenant les complexes dura/pia et dura/ventral, probablement en raison de leur faible fréquence dans le dataset', 'SegFormer, TransUNet, SwinUNet et SAMed ont pu segmenter la moelle épinière avec une haute précision (Dice > 0.74) malgré des changements drastiques de géométrie de la moelle chez les patients humains'], 'main_findings': ['YOLOv8 surpasse tous les modèles évalués pour la localisation de la lésion (hématome)', "DeepLabv3 atteint la plus haute précision sur l'anatomie porcine non vue pour la segmentation", "SAMed atteint le meilleur score de généralisation zero-shot à l'anatomie humaine", "Les méthodes traditionnelles de traitement d'image sont nettement moins performantes que les modèles d'apprentissage profond pour la localisation et la segmentation"]}

## Conclusions

Le déploiement de l'IA et de la vision par ordinateur dans l'analyse d'images échographiques présente un potentiel remarquable pour rationaliser le diagnostic de la lésion médullaire, avec des améliorations significatives de la qualité d'image, de la précision diagnostique et de l'accessibilité La mise à disposition publique de ce dataset unique vise à faciliter les efforts de vision par ordinateur en imagerie médicale L'automatisation du diagnostic par échographie peut enrichir les workflows cliniques pour des traitements personnalisés sans surcharger les cliniciens Les avancées en vision par ordinateur basée sur l'apprentissage profond permettent d'évaluer automatiquement ce flux continu de données morphologiques, permettant un changement de paradigme dans les soins cliniques

## Anatomy Pixel instances Instances across images

| Dorsal Space | 397,350,611 | 10,223 |
| --- | --- | --- |
| Dura | 142,857,955 | 9814 |
| Pia | 142,721,894 | 9839 |
| CSF | 118,161,757 | 9613 |
| Dura/Pia complex | 57,124,376 | 2732 |
| Spinal cord | 812,894,511 | 10,223 |
| Hematoma | 69,727,644 | 5756 |
| Dura/Ventral Complex 58,152,053 | 2671 |
| Ventral Space | 89,571,059 | 6099 |
| Background | 18,992,200 | 6385 |

## . Because the porcine and human spinal cord have similar anatomical structures and immune

|  |  |  |  |  | Training |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model | Encoder # of parameters Learning rate Batch size | epochs | Optimizer | Loss function |
| Faster RCNN ResNet50 41,299,161 | 0.004935 | 4 | 60 | SGD | Cross entropy + smooth L1 |
| SSD300 | ResNet50 24,641,780 | 0.002571 | 32 | 20 | SGD | Cross entropy + smooth L1 |
| SSD512 | ResNet50 24,641,780 | 0.000251 | 8 | 20 | SGD | Cross entropy + smooth L1 |
| RetinaNet | ResNet50 36,352,630 | 0.000099 | 8 | 60 | SGD | Focal loss |
| DETR | ResNet50 41,524,954 | 0.000011 | 8 | 200 | AdamW | Cross entropy + smooth L1 |
| YOLOv7 | E-ELAN 37,196,556 | 0.000123 | 32 | 75 | Adam | Binary cross entropy + mean square error |
| YOLOv8 | CSPNet | 25,856,899 | 0.000422 | 48 | 80 | AdamW + SGD | Binary cross entropy + distribution focal loss + complete intersection over union |

## Performance of object detection models on unseen porcine spinal cord ultrasound images to detect the site of injury. Highest performance values are in bold.

| Model | Encoder |  | # of |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | mAP50 mAP50-95 AR | CPU |  |  | GPU |  |
|  |  |  |  | FPS | Load (%) Implantability score FPS | Load (%) Implantability score |
| Faster RCNN 0.985 | 0.524 | 0.594 1.53 | 33 | 0.676 | 14.98 | 62 | 0.613 |
| SSD300 | 0.669 | 0.207 | 0.249 23.12 36 | 0.735 | 147.62 27 | 0.766 |
| SSD512 | 0.874 | 0.274 | 0.324 23.46 26 | 0.866 | 125.03 18 | 0.853 |
| RetinaNet | 0.912 | 0.264 | 0.426 1.89 | 32 | 0.646 | 17.66 | 48 | 0.616 |
| DETR | 0.787 | 0.251 | 0.453 19.78 15 | 0.812 | 114.35 26 | 0.772 |
| YOLOv7 | 0.923 | 0.439 | 0.499 19.54 20 | 0.865 | 80.13 | 28 | 0.777 |
| YOLOv8 | 0.979 | 0.606 | 0.644 17.85 22 | 0.870 | 115.31 27 | 0.867 |

## parameters Learning rate Batch size Training epochs Optimizer Loss function

| SegFormer MiT-B5 | 84,601,034 | 0.000972 | 4 | 75 | AdamW | Cross entropy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U-Net | ResNet50 | 31,044,106 | 0.003011 | 8 | 50 | SGD | Cross entropy |
| DeepLabv3 ResNet50 | 41,998,420 | 0.000334 | 4 | 100 | AdamW | Cross entropy |
| TransUNet ResNet50 + ViT_B16 105,323,306 | 0.004468 | 24 | 200 | SGD | Cross entropy + dice |
| Swin-UNet Swin-T | 27,153,156 | 0.061411 | 16 | 100 | SGD | Cross entropy + dice |
| SAMed | SAM ViT-B | 91,866,903 | 0.002840 | 24 | 200 | AdamW | Cross entropy + dice |

## Performance of semantic segmentation models on unseen porcine and human spinal cord ultrasound images. Highest performance values are in bold.

|  | Porcine | Porcine |  | Human | Human |
| --- | --- | --- | --- | --- | --- | --- |
|  | anatomy | spinal cord | anatomy | spinal cord | CPU | GPU |
|  | MIoU Dice IoU | Dice MIoU Dice IoU | Dice FPS | Load (%) Implantability score FPS | Load (%) Implantability score |
| SegFormer 0.493 0.570 0.906 0.950 0.232 0.308 0.666 0.773 3.66 23 | 0.548 | 23.50 45 | 0.513 |
| U-Net | 0.476 0.553 0.867 0.928 0.253 0.349 0.609 0.722 6.06 32 | 0.563 | 62.37 41 | 0.668 |
| DeepLabv3 0.515 0.587 0.910 0.952 0.200 0.289 0.506 0.656 4.76 27 | 0.568 | 64.11 35 | 0.702 |
| TransUNet 0.500 0.573 0.921 0.958 0.298 0.388 0.758 0.853 4.33 35 | 0.532 | 40.85 34 | 0.609 |
| SwinUNet 0.490 0.562 0.913 0.954 0.309 0.401 0.692 0.783 12.75 31 | 0.699 | 63.36 34 | 0.690 |
| SAMed | 0.497 0.574 0.908 0.951 0.347 0.445 0.616 0.740 5.40 37 | 0.535 | 29.43 35 | 0.563 |

### Formule


$$Implantability Score = mAP50 2 + FPSnorm 4 + 1 -Load 4 (1)$$
