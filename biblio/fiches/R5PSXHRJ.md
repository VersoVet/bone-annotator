# Veterinary fracture diagnosis: a deep learning model for dogs long bone fractures.

**Auteurs** : Ashraf Sobhy Saber, Ibrahim Selim, Heba Askr, Ahmed Elbahgy, Ahmed Ashraf, Ahmed Eldweek, Mostafa Safwat, Mohamed Elsayed, Ahmed AboRashed, Aboul Ella Hassanien
**Année** : 2026
**DOI** : 10.1038/s41598-026-50387-4

## Résumé

Bone fractures in dogs are common orthopaedic conditions that require accurate diagnosis and rapid intervention. Traditional radiographic interpretation is often time consuming and is subject to variability, emphasizing the need for automated diagnostic tools. This paper represents a deep learning model based on classification of long bone fractures in dogs using medical conventional radiographic images. The proposed model uses a convolutional neural network (CNN), specifically ResNet50 to improve detection and fracture classification. Comparative analysis with other deep learning architectures, including VGG16 and MobileNeTV2, shows the excellent ResNet50 performance. To address the challenge of limited annotated veterinary radiographic datasets, the actual data strategy of augmentation is implemented, which increases the generalization of the model. In addition, the segment model of anything (SAM) is integrated for automated fracture segmentation, allowing precise location and improv

## Méthodologie

{'study_design': 'Modèle proposé en trois phases : (1) description et pré-traitement des données (segmentation avec SAM, augmentation de données, équilibrage des données, division du jeu de données), (2) extraction de caractéristiques et entraînement du modèle avec ResNet50, (3) évaluation des performances', 'intervention': 'Classification des fractures des os longs (classes oblique et overriding) via un réseau de neurones convolutif ResNet50, comparé à VGG16, VGG19, EfficientNetB0, Xception, MobileNetV2 et DenseNet121', 'control': 'Autres modèles pré-entraînés (VGG16, VGG19, EfficientNetB0, Xception, MobileNetV2, DenseNet121) utilisés comme comparateurs', 'primary_outcomes': ['Accuracy (exactitude)', 'Precision (précision)', 'Recall/Sensitivity (rappel)', 'F1-score', 'AUC (Area Under the Curve)'], 'secondary_outcomes': ["Efficacité computationnelle (MFLOPS, temps d'inférence, consommation mémoire, taille du modèle, consommation d'énergie)"], 'statistical_methods': ['Matrices de confusion', 'Courbes ROC et score AUC', "Comparaisons par paires avec p-values (test de significativité des différences d'AUC)", "Analyse d'ablation"], 'duration': None, 'setting': 'Développement sur ordinateur personnel avec CPU Intel(R) Core(TM) i5-10300H, GPU Nvidia GTX 1650, RAM 8 GB, stockage SSD 500 GB, Windows 11, Python 3, TensorFlow 2.18.1'}

## Résultats

{'quantitative': [{'outcome': 'Accuracy (ResNet50, après pré-traitement)', 'value': '99.76%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'Experimental results show that the ResNet50 achieves high classification performance with an accuracy of 99.76%, accuracy of 99.53%, 100% and F1-score 99.76%, overcoming other competing architecture.'}, {'outcome': 'Precision (ResNet50)', 'value': '99.53%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'The ResNet50 achieves an exceptional accuracy of 99.76%, precision of 99.53%, recall 100% and F1-score 99.76%.'}, {'outcome': 'Recall (ResNet50)', 'value': '100%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'The ResNet50 achieves an exceptional accuracy of 99.76%, precision of 99.53%, recall 100% and F1-score 99.76%.'}, {'outcome': 'F1-score (ResNet50)', 'value': '99.76%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'The ResNet50 achieves an exceptional accuracy of 99.76%, precision of 99.53%, recall 100% and F1-score 99.76%.'}, {'outcome': 'Accuracy EfficientNetB0', 'value': '99.10%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'overcome competitors such as EfficientNetB0 (accuracy: 99.10%) and Xception (accuracy: 99.53%).'}, {'outcome': 'Accuracy Xception', 'value': '99.53%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'overcome competitors such as EfficientNetB0 (accuracy: 99.10%) and Xception (accuracy: 99.53%).'}, {'outcome': 'AUC ResNet50', 'value': '1', 'unit': 'AUC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'the ResNet50 shows the best classification performance and robustness, reaches the highest score AUC of 1.'}, {'outcome': 'AUC MobileNetV2', 'value': '≈0.96', 'unit': 'AUC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'Other models such as MobileNetV2 and Densenet121, reach a decent score of approximately 0.96 and 0.93, but show slightly greater overlapping of the class prediction.'}, {'outcome': 'AUC DenseNet121', 'value': '≈0.93', 'unit': 'AUC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'Other models such as MobileNetV2 and Densenet121, reach a decent score of approximately 0.96 and 0.93, but show slightly greater overlapping of the class prediction.'}, {'outcome': 'AUC VGG16', 'value': '0.72', 'unit': 'AUC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'the VGG16 works the least efficiently, with a significantly lower AUC 0.72.'}, {'outcome': 'Comparaison ROC-AUC ResNet50 vs autres architectures', 'value': 'significatif', 'unit': None, 'confidence_interval': None, 'p_value': '< 0.005', 'effect_size': None, 'source_section': 'Result analysis and discussion', 'source_quote': 'Based on the pairwise comparisons summarized in Table 4, all reported p-values are below 0.005, indicating that the differences in ROC-AUC between ResNet50 and each of the other evaluated architectures are statistically significant at the 0.5% level'}, {'outcome': 'Inference time EfficientNetB0', 'value': '0.0858', 'unit': 's', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Computational efficiency analysis', 'source_quote': 'the EfectiveNetB0 records the lowest MFLOPS (753.30) and the fastest inference time (0.0858s)'}, {'outcome': 'Inference time ResNet50', 'value': '0.1004', 'unit': 's', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Computational efficiency analysis', 'source_quote': 'the proposed Resnet50 follows with 802.10 MFLOPS and an inference time of 0.1004s, reaching the lowest memory consumption (98.93 MB), model size (11.67 MB) and energy consumption (11177 J).'}, {'outcome': 'Accuracy ResNet50 avant pré-traitement (ablation)', 'value': '0.8333', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Ablation analysis', 'source_quote': 'Before preliminary processing, the proposed ResNet50 shows strong results with an accuracy of 0.8333 and F1-score 0.8889, which exceeds most of the other competing models.'}, {'outcome': 'Accuracy ResNet50 après pré-traitement (ablation)', 'value': '0.9976', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Ablation analysis', 'source_quote': 'After using the pre-processing methodology, the model achieves the highest score across all metrics with an accuracy of 0.9976, the accuracy of 0.9953, the invocation of 1.0 and F1-score 0.9976, indicating almost perfect classification performance.'}], 'qualitative_findings': ["Les courbes de perte montrent une trajectoire descendante constante, indiquant un processus d'apprentissage réussi du modèle proposé", 'ResNet50 présente le moins de faux positifs tout en maintenant un bon équilibre entre vrais positifs et vrais négatifs', "VGG16 et VGG19, bien qu'efficaces pour identifier les cas positifs, produisent un nombre plus élevé de faux positifs"], 'main_findings': ['ResNet50 surpasse les autres architectures pré-entraînées (VGG16, VGG19, EfficientNetB0, Xception, MobileNetV2, DenseNet121) en classification des fractures des os longs chez le chien', "L'intégration de SAM pour la segmentation et l'augmentation de données améliore significativement la performance du modèle", 'ResNet50 offre le meilleur compromis entre efficacité computationnelle et précision parmi les architectures évaluées']}

## Conclusions

Le modèle de deep learning proposé, basé sur ResNet50, permet une classification automatisée efficace des fractures obliques et overriding chez le chien Les résultats obtenus préparent la voie au développement d'outils pilotés par l'IA pour soutenir les vétérinaires dans le diagnostic des fractures, menant à des évaluations plus rapides et précises et à de meilleurs soins des patients Les recherches futures devraient se concentrer sur la résolution des limites identifiées, l'amélioration de l'interprétabilité du modèle et le transfert de ces résultats prometteurs vers des applications cliniquement pertinentes

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
