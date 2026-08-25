# Foundational Segmentation Models and Clinical Data Mining Enable Accurate Computer Vision for Lung Cancer.

**Auteurs** : Nathaniel C Swinburne, Christopher B Jackson, Andrew M Pagano, Joseph N Stember, Javin Schefflein, Brett Marinelli, Prashanth Kumar Panyam, Arthur Autz, Mohapar S Chopra, Andrei I Holodny, Michelle S Ginsberg
**Année** : 2025
**DOI** : 10.1007/s10278-024-01304-6

## Résumé

This study aims to assess the effectiveness of integrating Segment Anything Model (SAM) and its variant MedSAM into the automated mining, object detection, and segmentation (MODS) methodology for developing robust lung cancer detection and segmentation models without post hoc labeling of training images. In a retrospective analysis, 10,000 chest computed tomography scans from patients with lung cancer were mined. Line measurement annotations were converted to bounding boxes, excluding boxes < 1 cm or > 7 cm. The You Only Look Once object detection architecture was used for teacher-student learning to label unannotated lesions on the training images. Subsequently, a final tumor detection model was trained and employed with SAM and MedSAM for tumor segmentation. Model performance was assessed on a manually annotated test dataset, with additional evaluations conducted on an external lung cancer dataset before and after detection model fine-tuning. Bootstrap resampling was used to calculat

## Méthodologie

{'study_design': "Étude rétrospective utilisant la méthodologie MODS (mining, object detection, and segmentation) : conversion des annotations linéaires cliniques en boîtes englobantes, apprentissage teacher-student avec l'architecture YOLO pour l'étiquetage automatique des lésions non annotées, puis entraînement d'un modèle final de détection tumorale utilisé conjointement avec SAM et MedSAM pour la segmentation", 'intervention': 'Intégration de SAM et MedSAM (modèles de segmentation fondationnels) dans le pipeline MODS pour la segmentation tumorale, à partir des boîtes de détection générées par le modèle YOLO entraîné sur des données cliniques minées', 'control': None, 'primary_outcomes': ['F1 score du modèle de détection tumorale', 'Coefficient de similarité de Dice (DSC) de la segmentation tumorale (SAM et MedSAM)'], 'secondary_outcomes': ['Performance du modèle sur un jeu de données externe (LIDC-IDRI) avant et après fine-tuning du modèle de détection'], 'statistical_methods': ['Bootstrap resampling pour le calcul des intervalles de confiance à 95%'], 'duration': None, 'setting': 'Données cliniques PACS (Picture Archiving and Communication System), validation externe sur le jeu de données LIDC-IDRI'}

## Résultats

{'quantitative': [{'outcome': "Annotations linéaires minées et boîtes d'entraînement obtenues", 'value': "10789 annotations linéaires, 5403 boîtes d'entraînement", 'unit': 'nombre', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Data mining yielded 10,789 line annotations, resulting in 5403 training boxes.'}, {'outcome': 'F1 score du modèle de détection de base (interne)', 'value': '0.847', 'unit': 'F1 score', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The baseline detection model achieved an internal F1 score of 0.847, improving to 0.860 after self-labeling.'}, {'outcome': 'F1 score du modèle de détection après auto-étiquetage (self-labeling, interne)', 'value': '0.860', 'unit': 'F1 score', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The baseline detection model achieved an internal F1 score of 0.847, improving to 0.860 after self-labeling.'}, {'outcome': 'DSC de segmentation tumorale interne avec SAM', 'value': '0.842', 'unit': 'Dice similarity coefficient (DSC)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Tumor segmentation using the final detection model attained internal Dice similarity coefficients (DSCs) of 0.842 (SAM) and 0.822 (MedSAM).'}, {'outcome': 'DSC de segmentation tumorale interne avec MedSAM', 'value': '0.822', 'unit': 'Dice similarity coefficient (DSC)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Tumor segmentation using the final detection model attained internal Dice similarity coefficients (DSCs) of 0.842 (SAM) and 0.822 (MedSAM).'}, {'outcome': 'F1 score du modèle de détection après fine-tuning, validation externe', 'value': '0.832', 'unit': 'F1 score', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'After fine-tuning, external validation showed an F1 of 0.832 and DSCs of 0.802 (SAM) and 0.804 (MedSAM).'}, {'outcome': 'DSC de segmentation externe avec SAM (après fine-tuning)', 'value': '0.802', 'unit': 'Dice similarity coefficient (DSC)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'After fine-tuning, external validation showed an F1 of 0.832 and DSCs of 0.802 (SAM) and 0.804 (MedSAM).'}, {'outcome': 'DSC de segmentation externe avec MedSAM (après fine-tuning)', 'value': '0.804', 'unit': 'Dice similarity coefficient (DSC)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'After fine-tuning, external validation showed an F1 of 0.832 and DSCs of 0.802 (SAM) and 0.804 (MedSAM).'}, {'outcome': 'DSC maximal externe comparé aux modèles entraînés avec masques de vérité terrain LIDC-IDRI', 'value': '0.804 (modèle) vs 0.777 et 0.822 (modèles de référence)', 'unit': 'Dice similarity coefficient (DSC)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The resulting segmentation accuracy, with a maximum DSC of 0.804 on the external LIDC-IDRI test set, is comparable to models trained with LIDC-IDRI ground truth segmentation masks [22,23], which achieve DSCs of 0.777 and 0.822.'}], 'qualitative_findings': ['SAM performe mal lorsque des structures normales de densité similaire aux tumeurs (ex: vaisseaux sanguins sectionnés) sont adjacentes à la tumeur, entraînant leur inclusion erronée dans le masque tumoral', 'MedSAM produit des masques de morphologie globulaire aux frontières apparemment arbitraires englobant du tissu pulmonaire aéré adjacent', "Les scores les plus élevés des deux modèles correspondent typiquement à des tumeurs solides situées en périphérie pulmonaire, les deux modèles distinguant bien l'atélectasie et les côtes des lésions"], 'main_findings': ["L'intégration de modèles de segmentation fondationnels (SAM et MedSAM) dans le cadre MODS permet d'obtenir des modèles de détection et de segmentation du cancer du poumon très performants en utilisant uniquement des données cliniques minées", 'SAM et MedSAM constituent tous deux des modèles de segmentation fondationnels prometteurs pour les images de radiologie', 'MedSAM ne surpasse pas nécessairement SAM pour la segmentation des lésions en radiologie malgré son entraînement spécifique sur des images médicales', "Le fine-tuning avec un petit ensemble d'entraînement externe faiblement annoté (moins de 1000 images) améliore notablement la performance après dégradation liée au domain shift"]}

## Conclusions

L'étude démontre le développement de modèles de détection et de segmentation tumorale pulmonaire très efficaces uniquement à partir de données cliniques minées, soulignant l'utilité du cadre MODS pour créer des modèles de vision par ordinateur en radiologie applicables à diverses modalités et maladies L'intégration de la segmentation fondationnelle basée sur SAM rationalise cette méthodologie, accélérant le développement des modèles de radiologie et améliorant leur portabilité Les travaux futurs porteront sur des applications cliniques plus larges, avec un accent sur la validation prospective, l'affinement des modèles dans divers contextes cliniques, et l'intégration d'un apprentissage continu pour contrer la dérive des données

## Patient characteristicsUnless otherwise indicated, data are numbers of patients.

|  | Training group | Testing group | Total |
| --- | --- | --- | --- |
| Patient demographics |  |  |  |
| • No. of patients | 4052 | 125 | 4177 |
| • Mean age (y) | 68.6 ± 12.7 | 68.6 ± 13.8 | 68.6 ± 12.8 |
| • Sex | 2233 women, 1819 men | 68 women, 57 men | 2301 |
|  |  |  | women, |
|  |  |  | 1876 men |
| Lung cancer subtype |  |  |  |
| • Adenocarcinoma | 2506 | 70 | 2576 |
| • Squamous cell carcinoma | 454 | 15 | 469 |
| • Neuroendocrine | 148 | 6 | 154 |
| • Small cell carcinoma | 126 | 3 | 129 |
| • Other, multiple, or unavailable | 818 | 31 | 849 |
| No. of unique scans | 4400 | 136 | 4536 |
| Image slice thickness (mm) |  |  |  |
| • 5.0 | 13,378 | 381 | 13,759 |
| • 1.25 | 3640 | 168 | 3808 |
| • Other | 24 | 0 | 24 |
| Mean box length (cm) | 2.08 ± 1.09 | 2.15 ± 1.07 | 2.08 ± 1.09 |

## Results of manual inspection of mined and selflabeled image annotationsResults of manual inspection conducted on randomly selected subsets of both mined and self-labeled image annotations. In the mined image subset, other abnormalities consisted of bullae, esophageal masses, and the tracheal lumen diameter. In the self-labeled subset, other abnormalities consisted of bullae, loculated pleural fluid, apical pleural scarring, and regions of fibrosis. False positives observed in this subset were predominantly vessels imaged in cross-section and respiratory motion artifacts.

| Total boxes | Pulmonary nod- | Pleural masses | Lymph nodes | Other | False posi- |
| --- | --- | --- | --- | --- | --- |
|  | ules/masses |  |  |  | tives/spuri- |
|  |  |  |  |  | ous |
| Mined image subset (500 images) |  |  |  |  |
| 505 | Solid: 283 | 40 | 46 | 6 | 0 |
|  | Sub-solid: 130 |  |  |  |  |
| Self-labeled image subset (500 images) |  |  |  |  |
| 500 | Solid: 253 | 42 | 32 | 14 | 48 |
|  | Sub-solid: 111 |  |  |  |  |

## Tumor detection model performance Detection F1 scores obtained from the teacher and student tumor detection models using both the internal and external test sets. For assessment on the external dataset, the detection models were scored before and after fine-tuning. Values in bold represent the highest performance achieved for each test set.

| Model Internal test set | External LIDC-IDRI test set |
| --- | --- | --- |
| F1 score (95% CI) F1 score before | F1 score after fine- |
|  | fine-tuning (95% | tuning (95% CI) |
|  | CI) |  |
| Teacher 0.847 (0.812- | 0.723 (0.649- | 0.790 (0.723- |
| 0.880) | 0.800) | 0.852) |
| Student 0.860 (0.825-0.893) | 0.765 (0.679-0.841) | 0.832 (0.764-0.895) |
| CI, confidence interval; LIDC-IDRI, Lung Image Database Consor- |
| tium image collection |  |  |

## Integrated tumor detection and segmentation model performance

|  | Internal test set | External LIDC-IDRI test set |
| --- | --- | --- |
|  | DSC (95% CI) | DSC (95% CI) |
| Student detection | 0.842 (0.805-0.873) 0.802 (0.714-0.870) |
| model + SAM |  |
| Student detection | 0.822 (0.785-0.851) 0.804 (0.730-0.858) |
| model + Med- |  |
| SAM |  |
| Segmentation Dice similarity coefficients (DSCs) obtained from the |
| integrated tumor detection and segmentation models using both the |
| internal and external test sets. The top-performing detection mod- |
| els-student model for the internal test set and fine-tuned student |
| model for the external test set-were paired with SAM and Med- |
| SAM for segmentation. Bold values indicate the highest performance |
| for each test set. |  |
| CI, confidence interval; MedSAM, Segment Anything Model for |
| Medical Imaging; SAM, Segment Anything Model; LIDC-IDRI, Lung |
| Image Database Consortium image collection |
