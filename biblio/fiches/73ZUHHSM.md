# Deep Learning for Video Fluoroscopic Swallowing Study Analysis: A Survey on Classification, Detection, and Segmentation Techniques

**Auteurs** : Ahmed Fakhry, Sarah Mary Antony, Eunhee Park, Jong Taek Lee
**Année** : 2025
**DOI** : 10.1109/access.2025.3573282

## Résumé

Deep learning has significantly advanced the analysis of Video Fluoroscopic Swallowing Study data, an essential diagnostic tool for dysphagia assessment. This review explores recent applications of deep learning across key VFSS analysis tasks, including classification, detection, and segmentation. Classification methods utilizing convolutional neural networks achieve high accuracy, ranging from 91.7% to 95.98%, and Area Under the ROC Curve scores between 0.71 and 0.97, thus enhancing the consistency and reliability of swallowing phase identification. Detection approaches employing advanced deep learning architectures effectively localize anatomical landmarks and temporal swallowing events, reaching Mean Average Precision values of up to 0.89 and tracking errors as low as 2.38 pixels. Segmentation techniques based on variants of U-Net and related architectures accurately delineate critical anatomical regions, with Dice Similarity Coefficients ranging from 0.67 to 0.90. Collectively, these advances substantially improve VFSS interpretation by increasing accuracy, reducing subjective variability, and streamlining clinical workflows. This survey summarizes recent methodologies and discusses strategies for dataset collection and preprocessing, including both proprietary and limited publicly available datasets, discusses ongoing challenges such as computational demands and dataset diversity, and highlights future directions in leveraging deep learning to enhance dysphagia diagnosis and treatment.

## Méthodologie

{'study_design': "Revue de la littérature structurée autour de trois tâches principales d'apprentissage profond appliquées au VFSS : classification, détection et segmentation, couvertes respectivement dans les sections II, IV et V", 'intervention': None, 'control': None, 'primary_outcomes': ['Performance des modèles de classification des phases de déglutition (accuracy, AUC)', 'Performance des modèles de détection des repères anatomiques et événements temporels (mAP, erreur de suivi)', 'Performance des modèles de segmentation des régions anatomiques (Dice Similarity Coefficient)'], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'Précision (accuracy) des méthodes de classification basées sur CNN', 'value': '91.7% à 95.98%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Classification methods utilizing convolutional neural networks achieve high accuracy, ranging from 91.7% to 95.98%'}, {'outcome': 'Area Under the ROC Curve (AUC) des méthodes de classification', 'value': '0.71 à 0.97', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Area Under the ROC Curve scores between 0.71 and 0.97, thus enhancing the consistency and reliability of swallowing phase identification'}, {'outcome': 'Mean Average Precision (mAP) des approches de détection', 'value': "jusqu'à 0.89", 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Detection approaches employing advanced deep learning architectures effectively localize anatomical landmarks and temporal swallowing events, reaching Mean Average Precision values of up to 0.89'}, {'outcome': 'Erreur de suivi (tracking error) des approches de détection', 'value': 'aussi bas que 2.38', 'unit': 'pixels', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'tracking errors as low as 2.38 pixels'}, {'outcome': 'Dice Similarity Coefficient (DSC) des techniques de segmentation', 'value': '0.67 à 0.90', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Segmentation techniques based on variants of U-Net and related architectures accurately delineate critical anatomical regions, with Dice Similarity Coefficients ranging from 0.67 to 0.90'}], 'qualitative_findings': ["L'intégration de l'apprentissage profond dans l'analyse VFSS favorise des méthodes d'évaluation standardisées, assurant des résultats cohérents et reproductibles à travers différents contextes cliniques", "L'automatisation de l'analyse VFSS réduit substantiellement le temps que les cliniciens consacrent à l'interprétation des résultats"], 'main_findings': ["Les méthodes de classification basées sur CNN (VGG, I3D, ResNet) atteignent une haute précision pour l'identification des phases de déglutition", 'Les approches de détection (SSD, HRNet) localisent efficacement les repères anatomiques et événements temporels de déglutition', 'Les techniques de segmentation basées sur U-Net et ses variantes délimitent précisément les régions anatomiques critiques (bolus, os hyoïde)', "Ces avancées améliorent substantiellement l'interprétation VFSS en augmentant la précision, en réduisant la variabilité subjective et en simplifiant les flux de travail cliniques"]}

## Conclusions

L'apprentissage profond a considérablement fait progresser l'analyse VFSS en automatisant les tâches de classification, détection et segmentation, améliorant la précision et l'efficacité diagnostiques L'utilisation de modèles avancés comme I3D et VGG-16 pour la classification de phase, SSD pour la détection de repères anatomiques, et les approches basées sur U-Net pour la segmentation rend les évaluations VFSS plus objectives et précises Des orientations prometteuses existent pour améliorer l'applicabilité clinique et la robustesse des méthodes d'apprentissage profond, notamment l'intégration avec d'autres modalités d'imagerie, le développement de systèmes IA légers en temps réel, et l'amélioration de l'interprétabilité Surmonter les limitations actuelles des jeux de données sera essentiel pour développer des modèles qui se généralisent efficacement à des populations de patients variées

## Evaluation results for detection models, including mAP, IoU, sample size, age range, and study descriptions for various VFSS detection tasks.

| a slightly higher accuracy of 95.98% on the same dataset. | across multiple thresholds. Higher mAP values indicate better |
| --- | --- | --- | --- | --- | --- |
| Lee et al. [37] applied the Xception model for airway invasion | object detection and localization. |  |
| detection, achieving 93.2% accuracy on a dataset comprising 319 samples. Similarly, Lee et al. [8] utilized the VGG model for pharyngeal phase detection, reporting an accuracy of | mAP = | 1 Q | Q q=1 | AP q | (5) |
| 93.20% and an AUC of 0.89 on a dataset of 324 samples, with participants averaging 70.67 ± 14.73 years in age. Kim et al. [7] adopted the Mobilenet architecture for pen-etration and aspiration detection, achieving 94.74% accuracy and an AUC of 0.94, using a dataset of 190 samples with an | Intersection over Union (IoU): It is also widely used in detection tasks, assessing the extent of overlap between predicted and ground truth bounding boxes. It is critical for evaluating detection algorithms. |
| average participant age of 66.83 ± 15.47 years. In contrast, Iida et al. [38] opted for a modified LeNet architecture for | IoU = | Area of Overlap Area of Union | (6) |
| aspiration detection, achieving 91.7% accuracy and an AUC |  |  |  |  |  |
| of 0.97 on a smaller dataset of 129 samples, with participants | 2) EXPERIMENTAL RESULTS |  |  |  |
| averaging 52.88 ± 31.68 years in age. Finally, Ryu et al. [39] |  |  |  |  |  |
| employed the BiFPN U-Net model for predicting aspiration |  |  |  |  |  |
| risk and oral feeding outcomes, achieving an AUC of 0.71 on |  |  |  |  |  |
| a dataset of 85 samples, though the age group of participants |  |  |  |  |  |
| was not specified. Collectively, these studies illustrate the |  |  |  |  |  |
| versatility and effectiveness of deep learning models in |  |  |  |  |  |
| addressing various VFSS classification tasks, catering to |  |  |  |  |  |
| diverse clinical challenges and medical conditions. |  |  |  |  |  |
| B. DETECTION |  |  |  |  |  |
| 1) EVALUATION METRICS |  |  |  |  |  |
| Mean Average Precision (mAP): It evaluates the ranking |  |  |  |  |  |
| performance in detection tasks by summarizing precision |  |  |  |  |  |

## Table 6

| summarizes the evaluation metrics for various |
| --- |
| detection and tracking methods, focusing on their mAP and |
| IoU values across different VFSS tasks. Zhang et al. [40] |
| employed the SSD model for hyoid bone detection and local- |
| ization, achieving an impressive mAP of 0.89 on a dataset of |
| 265 samples, with participants averaging 64.83± 13.56 years |
| in age. Their method effectively identified the hyoid bone's |
| position within VFSS images but did not report IoU values. |

### Formule


$$AUC = 1 0 TPR(FPR) d(FPR)(2)$$

### Formule


$$TPR = TP TP + FN(3)$$

### Formule


$$FPR = FP FP + TN (4)$$
