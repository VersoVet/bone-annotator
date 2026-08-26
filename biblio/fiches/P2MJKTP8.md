# Fine-Tuned Segment Anything Model with Low-Rank Adaptation for Chest X-Ray Images.

**Auteurs** : Alahmari SS, Gardner MR, Alqahtani F, Salem T.
**Année** : 2026
**DOI** : 10.3390/diagnostics16060847

## Résumé

<b>Background:</b> This paper investigates the use of the Segment Anything Model (SAM) for chest X-ray (CXR) image segmentation, with a focus on improving its performance using low-rank adaptation (LoRA). <b>Methods:</b> We evaluate three versions of SAM: two zero-shot methods (using coordinate and bounding box prompts) and a fine-tuned SAM using LoRA. To support these approaches, we also trained two standard convolutional neural networks (CNNs), U-Net and DeepLabv3+, to generate draft lung segmentations that serve as input prompts for the SAM methods. Our fine-tuning approach uses LoRA to add lightweight trainable adapters within the Transformer blocks of the SAM, allowing only a small subset of parameters to be updated. The rest of the SAM remains frozen, helping preserve its pre-trained knowledge while reducing memory and computational needs. We tested all models on a dataset of CXR images labeled for COVID-19, viral pneumonia, and normal cases. <b>Results:</b> Results show that fin

## Méthodologie

{'study_design': "Étude comparative de trois approches SAM (SAM zero-shot avec prompts par coordonnées, SAM zero-shot avec prompts par bounding box, SAM fine-tuné avec LoRA) et de deux CNN de référence (U-Net, DeepLabv3+) pour la segmentation pulmonaire sur images CXR. L'approche de fine-tuning utilise LoRA pour ajouter des adaptateurs entraînables légers dans les blocs Transformer du SAM, en ne mettant à jour qu'un petit sous-ensemble de paramètres, le reste du SAM restant gelé.", 'intervention': 'Fine-tuning du SAM via LoRA (adaptateurs légers entraînables dans les blocs Transformer, reste du modèle gelé)', 'control': 'Méthodes SAM zero-shot (prompts par coordonnées et par bounding box) et CNN de référence (U-Net, DeepLabv3+)', 'primary_outcomes': ['Accuracy de segmentation', 'Intersection over Union (IoU)', 'Coefficient de Dice', 'Précision', 'Rappel', 'F1-score'], 'secondary_outcomes': [], 'statistical_methods': ['Accuracy', 'Intersection over Union (IOU)', 'Coefficient de Dice', 'Précision', 'Rappel', 'F1-score'], 'duration': None, 'setting': "Données d'imagerie rétrospectives et entièrement anonymisées provenant du système PACS institutionnel"}

## Résultats

{'quantitative': [{'outcome': 'Performance SAM zero-shot avec 15 coordonnées', 'value': '56.2% accuracy, 0.409 IOU, 0.571 dice, 0.441 précision, 0.856 rappel, 0.571 F1-score', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'Starting with 15 points, the SAM achieved 56.2% accuracy, 0.409 IOU, 0.571 dice coefficient, 0.441 precision, 0.856 recall, and 0.571 F1-score.'}, {'outcome': 'Performance SAM zero-shot avec 60 coordonnées', 'value': '59.6% accuracy, 0.439 IOU, 0.599 dice, 0.463 précision, 0.891 rappel, 0.599 F1-score', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'at 60 coordinates, the accuracy rose to 59.6%, IOU to 0.439, dice coefficient to 0.599, precision to 0.463, recall to 0.891, and F1-score to 0.599.'}, {'outcome': 'Meilleure performance SAM zero-shot (90-105 coordonnées)', 'value': "60.3-60.6% accuracy, IOU jusqu'à 0.451, dice 0.611, précision 0.474, rappel 0.916, F1-score 0.611", 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The best overall performance was observed between 90 and 105 coordinates, where accuracy plateaued at approximately 60.3-60.6%, IOU reached up to 0.451, dice coefficient peaked at 0.611, precision peaked at 0.474, recall reached the highest value at 0.916, and F1-score reached the highest value at 0.611.'}], 'qualitative_findings': ['Le SAM bounding box a sous-performé par rapport aux autres approches lors de la comparaison visuelle', 'Les performances de DeepLabv3 et du SAM fine-tuné étaient globalement similaires sur la visualisation'], 'main_findings': ['Le SAM fine-tuné avec LoRA surpasse le SAM zero-shot ainsi que U-Net et DeepLabv3 sur les six métriques évaluées', "L'augmentation du nombre de prompts par coordonnées améliore la performance du SAM zero-shot jusqu'à un point de saturation situé entre 75 et 90 coordonnées, au-delà duquel les gains diminuent voire déclinent légèrement", "L'adaptation du SAM au domaine cible améliore à la fois la classification pixel par pixel et la cohérence spatiale des contours des objets"]}

## Conclusions

Le SAM fine-tuné avec LoRA obtient la meilleure performance globale en termes d'accuracy, d'IoU et de coefficient de Dice, comparé aux approches SAM zero-shot et aux CNN de référence (U-Net, DeepLabv3+) La conception des prompts améliore les résultats du SAM zero-shot, mais reste inférieure à l'approche fine-tunée LoRA constitue une méthode efficace pour adapter des modèles de fondation comme le SAM à l'imagerie médicale, permettant une segmentation de haute qualité avec des ressources computationnelles limitées Les travaux futurs exploreront l'extension de cette approche à d'autres modalités d'imagerie et tâches, afin de réduire davantage les besoins d'annotation et de soutenir des applications cliniques évolutives

## Summary of image dataset and source.

| Image Class | Number of Images | Source |
| --- | --- | --- | --- | --- | --- |
|  | COVID-19 |  | 552 |  | KKH |
|  | Normal |  | 511 |  | KKH |
| Viral Pneumonia |  | 549 |  | Chowdhury [33] |
| COVID-19 | Pneumonia | Normal |
| Image | Mask | Image | Mask | Image | Mask |
| Original |  |  |  |  |  |
| Cropped |  |  |  |  |  |

## Performance of SAM using prompts with different numbers of coordinates, starting at 15 with an increment of 15 coordinates up to 105 coordinates.

| Number of Coordinates Accuracy % | IoU | Dice Coefficient | Precision | Recall | F1 Score |
| --- | --- | --- | --- | --- | --- | --- |
| 15 | 56.2 | 0.409 | 0.571 | 0.441 | 0.856 | 0.571 |
| 30 | 57.1 | 0.414 | 0.575 | 0.443 | 0.859 | 0.575 |
| 45 | 58.2 | 0.427 | 0.587 | 0.452 | 0.879 | 0.587 |
| 60 | 59.6 | 0.439 | 0.599 | 0.463 | 0.891 | 0.599 |
| 75 | 60.3 | 0.445 | 0.605 | 0.469 | 0.899 | 0.605 |
| 90 | 60.6 | 0.450 | 0.610 | 0.473 | 0.908 | 0.610 |
| 105 | 60.3 | 0.451 | 0.611 | 0.474 | 0.916 | 0.611 |

## Comparison between the segmentation performance of U-Net, DeepLabv3, and SAM.

| Number of Coordinates | Accuracy % | IoU | Dice Coef | Precision | Recall | F1 Score |
| --- | --- | --- | --- | --- | --- | --- |
| U-Net [5] | 57.6 | 0.313 | 0.470 | 0.427 | 0.576 | 0.470 |
| DeepLabv3+ [35] | 95.1 | 0.862 | 0.925 | 0.928 | 0.926 | 0.925 |
| SAM zero-shot bounding box | 76.2 | 0.569 | 0.718 | 0.594 | 0.933 | 0.718 |
| SAM zero-shot (90 coord) | 60.6 | 0.450 | 0.610 | 0.473 | 0.908 | 0.610 |
| Fine-tuned SAM + LoRA | 95.8 | 0.882 | 0.937 | 0.955 | 0.922 | 0.937 |
