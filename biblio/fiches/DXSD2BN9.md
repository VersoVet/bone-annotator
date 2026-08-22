# Veterinary fracture diagnosis: a deep learning model for dogs long bone fractures.

**Auteurs** : Saber AS, Selim I, Askr H, Elbahgy A, Ashraf A, Eldweek A, Safwat M, Elsayed M, AboRashed A, Hassanien AE.
**Année** : 2026
**DOI** : 10.1038/s41598-026-50387-4

## Résumé

Bone fractures in dogs are common orthopaedic conditions that require accurate diagnosis and rapid intervention. Traditional radiographic interpretation is often time consuming and is subject to variability, emphasizing the need for automated diagnostic tools. This paper represents a deep learning model based on classification of long bone fractures in dogs using medical conventional radiographic images. The proposed model uses a convolutional neural network (CNN), specifically ResNet50 to improve detection and fracture classification. Comparative analysis with other deep learning architectures, including VGG16 and MobileNeTV2, shows the excellent ResNet50 performance. To address the challenge of limited annotated veterinary radiographic datasets, the actual data strategy of augmentation is implemented, which increases the generalization of the model. In addition, the segment model of anything (SAM) is integrated for automated fracture segmentation, allowing precise location and improv

## Méthodologie

{'study_design': "Modèle proposé en trois phases: (1) description et pré-traitement des données (segmentation via Segment Anything Model, augmentation de données, équilibrage des classes, division du dataset), (2) extraction des caractéristiques et entraînement du modèle avec ResNet50, (3) évaluation de la performance et comparaison avec d'autres architectures pré-entraînées (VGG16, VGG19, EfficientNetB0, Xception, MobileNetV2, DenseNet121).", 'intervention': 'Classification des fractures des os longs (oblique vs overriding) via un CNN ResNet50 entraîné sur des images radiographiques segmentées et augmentées.', 'control': 'Comparaison avec six autres architectures de deep learning pré-entraînées: VGG16, VGG19, EfficientNetB0, Xception, MobileNetV2 et DenseNet121.', 'primary_outcomes': ['Accuracy', 'Precision', 'Sensitivity/Recall', 'Specificity', 'F1-score'], 'secondary_outcomes': ['AUC (Area Under the Curve)', 'MFLOPS', "Temps d'inférence", 'Consommation mémoire', 'Taille du modèle', 'Consommation énergétique'], 'statistical_methods': ['Comparaisons par paires (pairwise comparisons) des AUC avec calcul de p-values', 'Matrices de confusion', 'Courbes ROC'], 'duration': None, 'setting': 'PC personnel avec CPU Intel(R) Core (TM) i5-10300H, GPU Nvidia GTX 1650, RAM 8 GB, stockage SSD 500 GB, sous Windows 11 64-bit, développé en Python 3 avec TensorFlow 2.18.1.'}

## Résultats

{'quantitative': [{'outcome': 'Performance de classification ResNet50 (accuracy, précision, recall, F1-score)', 'value': 'Accuracy 99.76%, Precision 99.53%, Recall 100%, F1-score 99.76%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'The ResNet50 achieves an exceptional accuracy of 99.76%, precision of 99.53%, recall 100% and F1-score 99.76%.'}, {'outcome': 'Comparaison accuracy avec autres modèles', 'value': 'EfficientNetB0: 99.10%, Xception: 99.53%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'overcome competitors such as EfficientNetB0 (accuracy: 99.10%) and Xception (accuracy: 99.53%)'}, {'outcome': 'AUC ResNet50', 'value': '1', 'unit': 'AUC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'reaches the highest score AUC of 1'}, {'outcome': 'AUC autres modèles (MobileNetV2, DenseNet121, VGG16)', 'value': 'MobileNetV2 ≈0.96, DenseNet121 ≈0.93, VGG16 0.72', 'unit': 'AUC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'Other models such as MobileNetV2 and Densenet121, reach a decent score of approximately 0.96 and 0.93, but show slightly greater overlapping of the class prediction. In particular, the VGG16 works the least efficiently, with a significantly lower AUC 0.72.'}, {'outcome': "Significativité statistique des différences d'AUC entre ResNet50 et les autres architectures", 'value': 'p < 0.005 pour toutes les comparaisons', 'unit': None, 'confidence_interval': None, 'p_value': 'p<0.005', 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'Based on the pairwise comparisons summarized in Table 4, all reported p-values are below 0.005, indicating that the differences in ROC-AUC between ResNet50 and each of the other evaluated architectures are statistically significant at the 0.5% level'}, {'outcome': 'Ablation - performance avant pré-traitement', 'value': 'Accuracy 0.8333, F1-score 0.8889', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Ablation analysis', 'source_quote': 'Before preliminary processing, the proposed ResNet50 shows strong results with an accuracy of 0.8333 and F1-score 0.8889, which exceeds most of the other competing models.'}, {'outcome': 'Ablation - performance après pré-traitement', 'value': 'Accuracy 0.9976, Precision 0.9953, Recall 1.0, F1-score 0.9976', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Ablation analysis', 'source_quote': 'After using the pre-processing methodology, the model achieves the highest score across all metrics with an accuracy of 0.9976, the accuracy of 0.9953, the invocation of 1.0 and F1-score 0.9976, indicating almost perfect classification performance.'}, {'outcome': 'Efficacité computationnelle ResNet50', 'value': "802.10 MFLOPS, temps d'inférence 0.1004s, mémoire 98.93 MB, taille du modèle 11.67 MB, énergie 11177 J", 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Computational efficiency analysis', 'source_quote': 'the proposed Resnet50 follows with 802.10 MFLOPS and an inference time of 0.1004s, reaching the lowest memory consumption (98.93 MB), model size (11.67 MB) and energy consumption (11177 J)'}], 'qualitative_findings': ['Les courbes de perte (loss) montrent une trajectoire descendante constante, indiquant un apprentissage réussi du modèle proposé.', 'Le ResNet50 présente le plus faible nombre de faux positifs tout en maintenant un bon équilibre entre vrais positifs et vrais négatifs, contrairement à VGG16 et VGG19 qui produisent davantage de faux positifs.'], 'main_findings': ['ResNet50 surpasse les autres architectures de deep learning testées (VGG16, VGG19, EfficientNetB0, Xception, MobileNetV2, DenseNet121) pour la classification des fractures des os longs chez le chien.', "L'intégration de Segment Anything Model (SAM) pour la segmentation automatisée améliore la précision et la généralisation du modèle.", "La stratégie d'augmentation et d'équilibrage des données permet de pallier le manque de données annotées vétérinaires."]}

## Conclusions

This research provides an efficient deep learning model for the automated classification of oblique and overriding fractures in dogs. The promising results obtained with ResNet50, VGG16, EfectItB0, Desnet121, Xception and VGG19 are preparing a way for the development of AI-driven tools to support veterinary doctors in fracture diagnostics, leading to faster, more accurate assessment and improved patient care.

## Small dataset, lack of generalizability. The model's performance may be limited by dataset quality, hyperparameter tuning methods, and the lack of detailed patient history or fracture types. Further work is needed to improve generalizability and optimize preprocessing steps. A summary of the current literature for AI models in identifying of long bone fractures in Dogs.

| Ref. Year Model | Performance | Limitations |
| --- | --- | --- | --- |
| 12 | SVM (RBF Kernel), | SVM: 97.85% accuracy, MLP: 99.15% accuracy |  |
|  | MLP |  |  |
| 13 | ResNet50, AlexNet, and GoogLeNet | The F1 scores: AlexNet: 0.75, ResNet50: 0.80, GoogLeNet: 0.88. | The model's performance is relatively small, and further work is needed to develop comprehensive support tools for veterinarians. |
|  | R-CNN, SSD R-CNN: Accuracy: 74%, F1 Score: 85%. | Potential for improvement in accuracy; Limited to images classified in Phase 1; Lower accuracy compared to the first study; Lowest performance among the three approaches |
| 16 | ResNet50, Faster RNN, | ResNet50 with Binary Classification = 96.5% , ResNet50 Multi-class Classification = 87.7% , | The models' detection capabilities (especially Faster RNN) are limited to fracture location identification. Potential issues may arise from dataset variability and image quality. |
|  | DL model: YOLOv8 and VGG16. | F1 score : YOLOv8 = 80%, VGG16 = 72.22% | Data augmentation can improve performance but cannot fully capture the complexity of Conventional radiographic images. Both YOLOv8 and VGG16 are DL models with limited interpretability. |
|  | RCNN, CNN | F1 score: RNN = up to 99%, CNN = up to 97% | The study focuses on binary classification of fractured vs. healthy bones, but clinical fractures vary in type and severity, requiring more detailed classification. |

## Comparison between the proposed ResNet50 model versus other state-of-the-art models.

| Parameter |  | Settings |  |
| --- | --- | --- | --- |
| Learning rate |  | 0.0001 |  |
| Optimizer |  | Adam optimizer |
| Batch size |  | 64 |  |
| Loss function |  | Binary cross entropy |
| Number of Epochs | 50 |  |
| Patience in early stopping 5 |  |
| Image size |  | 224 width * 224 heights |
| Splitting ratio |  | 80% train, 10% validate, 10% test |
| Model | Accuracy Precision Recall F1 score |
| ResNet50 | 0.9976 | 0.9953 | 1.0000 0.9976 |
| VGG19 | 0.9917 | 0.9906 | 0.9929 0.9918 |
| VGG16 | 0.9929 | 0.9953 | 0.9906 0.9929 |
| MobileNetV2 0.9765 | 0.9753 | 0.9729 0.9764 |
| Xception | 0.9953 | 0.9953 | 0.9953 0.9953 |
| EfficientNetB0 0.9910 | 0.9976 | 1.0000 0.9910 |
| DenseNet121 0.9965 | 0.9976 | 0.9953 0.9965 |

## Model MFLOPs Inference time (Second / image) Memory consumption (MB) Model size (MB)

|  |  |  |  | Energy consumption |
| --- | --- | --- | --- | --- |
|  |  |  |  | (J) |
| VGG19 | 39038.39 0.1447 | 147.29 | 81.16 | 66,152 |
| VGG16 | 30713.49 0.1088 | 120.84 | 59.92 | 51,503 |
| MobileNetV2 | 1614.04 0.1550 | 247.03 | 98.56 | 28,864 |
| Xception | 16771.72 0.1536 | 339.58 | 87.65 | 58,729 |
| EfficientNetB0 | 753.30 0.0858 | 119.89 | 18.83 | 15,479 |
| DenseNet121 | 5701.47 0.1628 | 229.96 | 30.26 | 32,637 |
| ResNet50 (proposed) | 802.10 0.1004 | 98.93 | 11.67 | 11,177 |

## Computational efficiency analysis of the proposed modified ResNet50 versus other DL models.

| ResNet50 vs. MobileNetV2 | 1.00 | 0.96 | 0.001 |
| --- | --- | --- | --- |
| ResNet50 vs. DenseNet121 | 1.00 | 0.93 | 0.004 |
| ResNet50 vs. InceptionV3 | 1.00 | 0.95 | 0.003 |
| ResNet50 vs. EfficientNetB0 | 1.00 | 0.94 | 0.004 |
| ResNet50 vs. Xception | 1.00 | 0.92 | 0.002 |
| ResNet50 vs. VGG16 | 1.00 | 0.72 | 0.001 |

## Comparison (paired, same test set) AUC (ResNet50) AUC (Other model) p-value (paired AUC test)

| ResNet50 vs. MobileNetV2 | 0.98 | 0.96 | 0.004 |
| --- | --- | --- | --- |
| ResNet50 vs. DenseNet121 | 0.98 | 0.93 | 0.003 |
| ResNet50 vs. InceptionV3 | 0.98 | 0.95 | 0.004 |
| ResNet50 vs. EfficientNetB0 | 0.98 | 0.94 | 0.005 |
| ResNet50 vs. Xception | 0.98 | 0.92 | 0.002 |
| ResNet50 vs. VGG16 | 0.98 | 0.72 | 0.001 |

## Pairwise ROC-AUC comparisons vs. ResNet50 (before image preprocessing) .

|  | Before image |  |  | After image |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | pre-processing |  |  | pre-processing |  |
| Model | Accuracy Precision Recall F1 Score Accuracy Precision Recall F1 score |
| VGG19 | 0.6667 | 0.6667 | 1.0 | 0.8000 | 0.9917 | 0.9906 | 0.9929 0.9918 |
| VGG16 | 0.6667 | 0.6667 | 1.0 | 0.8000 | 0.9929 | 0.9953 | 0.9906 0.9929 |
| MobileNetV2 | 0.6667 | 0.6667 | 1.0 | 0.8000 | 0.9765 | 0.9753 | 0.9729 0.9764 |
| Xception | 0.8333 | 0.8000 | 1.0 | 0.8889 | 0.9953 | 0.9953 | 0.9953 0.9953 |
| EfficientNetB0 | 0.6667 | 1.000 | 0.5 | 0.6667 | 0.9910 | 0.9976 | 1.0000 0.9910 |
| DenseNet121 | 0.6667 | 0.6667 | 1.0 | 0.8000 | 0.9965 | 0.9976 | 0.9953 0.9965 |
| ResNet50 (proposed) 0.8333 | 0.8000 | 1.0 | 0.8889 | 0.9976 | 0.9953 | 1.000 0.9976 |

### Formule


$$F P )(2)$$

### Formule


$$Sensitivity ∨ Recall = T P/(T P + F N)(3)$$

### Formule


$$Specif icity = T N/(T N + F P )(4)$$

### Formule


$$F 1score = 2 × (( precision × recall)/(precision + recall ))(5)$$
