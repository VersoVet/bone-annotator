# Fine-Tuned Segment Anything Model with Low-Rank Adaptation for Chest X-Ray Images.

**Auteurs** : Saeed S Alahmari, Michael R Gardner, Fawaz Alqahtani, Tawfiq Salem
**Année** : 2026
**DOI** : 10.3390/diagnostics16060847

## Résumé

Background: This paper investigates the use of the Segment Anything Model (SAM) for chest X-ray (CXR) image segmentation, with a focus on improving its performance using low-rank adaptation (LoRA). Methods: We evaluate three versions of SAM: two zero-shot methods (using coordinate and bounding box prompts) and a fine-tuned SAM using LoRA. To support these approaches, we also trained two standard convolutional neural networks (CNNs), U-Net and DeepLabv3+, to generate draft lung segmentations that serve as input prompts for the SAM methods. Our fine-tuning approach uses LoRA to add lightweight trainable adapters within the Transformer blocks of the SAM, allowing only a small subset of parameters to be updated. The rest of the SAM remains frozen, helping preserve its pre-trained knowledge while reducing memory and computational needs. We tested all models on a dataset of CXR images labeled for COVID-19, viral pneumonia, and normal cases. Results: Results show that fine-tuned SAM with LoRA outperforms zero-shot SAM methods and CNN baselines in terms of segmentation accuracy and efficiency. Conclusions: This demonstrates the potential of combining LoRA with SAM for practical and effective medical image segmentation.

## Méthodologie

{'study_design': 'Comparaison de trois approches basées sur SAM (zero-shot avec prompts de coordonnées, zero-shot avec prompts de boîtes englobantes, et fine-tuning avec LoRA) avec deux CNN de référence (U-Net et DeepLabv3+) pour la segmentation pulmonaire sur des images CXR', 'intervention': "Fine-tuning du SAM avec LoRA : ajout d'adaptateurs entraînables légers (low-rank) au sein des blocs Transformer du SAM, permettant de mettre à jour uniquement un petit sous-ensemble de paramètres tandis que le reste du modèle reste gelé", 'control': 'SAM zero-shot (prompts de coordonnées et de boîtes englobantes) et CNN de référence (U-Net, DeepLabv3+)', 'primary_outcomes': ['Accuracy (%)', 'Intersection over Union (IOU)', 'Dice coefficient', 'Precision', 'Recall', 'F1-score'], 'secondary_outcomes': ['Efficacité computationnelle / réduction des besoins en mémoire et calcul'], 'statistical_methods': [], 'duration': None, 'setting': "Données d'imagerie rétrospectives entièrement anonymisées obtenues depuis le système PACS institutionnel"}

## Résultats

{'quantitative': [{'outcome': 'Performance SAM zero-shot à 15 prompts de coordonnées', 'value': '56.2% accuracy, 0.409 IOU, 0.571 dice, 0.441 precision, 0.856 recall, 0.571 F1', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'Starting with 15 points, the SAM achieved 56.2% accuracy, 0.409 IOU, 0.571 dice coefficient, 0.441 precision, 0.856 recall, and 0.571 F1-score.'}, {'outcome': 'Performance SAM zero-shot à 60 prompts de coordonnées', 'value': '59.6% accuracy, 0.439 IOU, 0.599 dice, 0.463 precision, 0.891 recall, 0.599 F1', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'For example, at 60 coordinates, the accuracy rose to 59.6%, IOU to 0.439, dice coefficient to 0.599, precision to 0.463, recall to 0.891, and F1-score to 0.599.'}, {'outcome': 'Meilleure performance SAM zero-shot entre 90 et 105 prompts de coordonnées', 'value': "60.3-60.6% accuracy, jusqu'à 0.451 IOU, 0.611 dice (pic), 0.474 precision (pic), 0.916 recall (max), 0.611 F1 (max)", 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The best overall performance was observed between 90 and 105 coordinates, where accuracy plateaued at approximately 60.3-60.6%, IOU reached up to 0.451, dice coefficient peaked at 0.611, precision peaked at 0.474, recall reached the highest value at 0.916, and F1-score reached the highest value at 0.611.'}], 'qualitative_findings': ['Le SAM bounding box a montré des performances inférieures comparé aux autres approches lors de la visualisation comparative', 'Les performances de DeepLabv3 et du SAM fine-tuned étaient globalement similaires sur la visualisation'], 'main_findings': ['Le SAM fine-tuned avec LoRA surpasse les méthodes SAM zero-shot ainsi que les modèles CNN de référence (U-Net, DeepLabv3) sur les six métriques évaluées', "L'augmentation du nombre de prompts de coordonnées améliore progressivement la performance du SAM en zero-shot, avec un point de saturation autour de 75-90 coordonnées, au-delà duquel un léger déclin est observé pour certaines métriques", 'Le fine-tuning du SAM sur le jeu de données amène une amélioration substantielle et cohérente par rapport à toutes les autres configurations évaluées']}

## Conclusions

Le SAM fine-tuned avec LoRA a obtenu la meilleure performance globale en termes d'accuracy, IoU et dice coefficient par rapport aux approches SAM zero-shot et aux CNN de référence (U-Net, DeepLabv3+) LoRA constitue une méthode efficace pour obtenir une segmentation de haute qualité avec des ressources computationnelles limitées Ces résultats démontrent l'intérêt d'adapter des modèles de fondation comme le SAM à l'imagerie médicale

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
