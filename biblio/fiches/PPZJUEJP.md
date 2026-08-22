# Large-scale annotation dataset for fetal head biometry in ultrasound images.

**Auteurs** : Mahmood Alzubaidi, Marco Agus, Michel Makhlouf, Fatima Anver, Khalid Alyafei, Mowafa Househ
**Année** : 2023
**DOI** : 10.1016/j.dib.2023.109708

## Résumé

This dataset features a collection of 3832 high-resolution ultrasound images, each with dimensions of 959×661 pixels, focused on Fetal heads. The images highlight specific anatomical regions: the brain, cavum septum pellucidum (CSP), and lateral ventricles (LV). The dataset was assembled under the Creative Commons Attribution 4.0 International license, using previously anonymized and de-identified images to maintain ethical standards. Each image is complemented by a CSV file detailing pixel size in millimeters (mm). For enhanced compatibility and usability, the dataset is available in 11 universally accepted formats, including Cityscapes, YOLO, CVAT, Datumaro, COCO, TFRecord, PASCAL, LabelMe, Segmentation mask, OpenImage, and ICDAR. This broad range of formats ensures adaptability for various computer vision tasks, such as classification, segmentation, and object detection. It is also compatible with multiple medical imaging software and deep learning frameworks. The reliability of the

## Méthodologie

{'study_design': "Construction d'un jeu de données annoté par réutilisation et ré-annotation de deux bases d'images échographiques publiques existantes, avec redimensionnement des images, annotation via CVAT, et validation par deux itérations de révision par des experts médicaux utilisant ICC et Jaccard similarity", 'intervention': None, 'control': None, 'primary_outcomes': ["Accord inter-annotateurs mesuré par l'Intraclass Correlation Coefficient (ICC(2,1)) entre l'étudiant en doctorat et le Senior Attending Physician (1ère itération), puis entre l'étudiant et le Radiologic Technologist (2ème itération)", "Indice de similarité de Jaccard (JS) entre les mêmes paires d'annotateurs"], 'secondary_outcomes': ["Nombre d'instances par classe (brain, CSP, LV) dans le jeu de données final"], 'statistical_methods': ['Intraclass Correlation Coefficient ICC(2,1)', 'Jaccard similarity index (JS)'], 'duration': 'Database A: collecte entre octobre 2018 et avril 2019; Database B: collecte entre mai 2014 et mai 2015', 'setting': 'BCNatal (Hospital Clinic et Hospital Sant Joan de Deu, Barcelone, Espagne) pour Database A; Department of Obstetrics, Radboud University Medical Center, Nijmegen, Pays-Bas pour Database B'}

## Résultats

{'quantitative': [{'outcome': 'ICC moyen global, 1ère itération (Étudiant vs Senior Attending Physician)', 'value': '0.859', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Validation', 'source_quote': 'The overall average ICC for the first iteration is approximately 0.859, calculated as (0.847 + 0.986 + 0.670 + 0.932)/4.'}, {'outcome': 'JS moyen global, 1ère itération (Étudiant vs Senior Attending Physician)', 'value': '0.855', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Validation', 'source_quote': 'the overall average JS for the first iteration is approximately 0.855, calculated as (0.844 + 0.993 + 0.648 + 0.935)/4.'}, {'outcome': 'ICC moyen global, 2ème itération (Étudiant vs Radiologic Technologist)', 'value': '0.889', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Validation', 'source_quote': 'The overall average ICC for the second iteration is approximately 0.889, calculated as (0.884 + 0.903 + 0.842 + 0.926)/4.'}, {'outcome': 'JS moyen global, 2ème itération (Étudiant vs Radiologic Technologist)', 'value': '0.857', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Validation', 'source_quote': 'the overall average JS for the second iteration is approximately 0.857, calculated as (0.810 + 0.945 + 0.778 + 0.896)/4.'}, {'outcome': 'Accord annotation CSP, plan trans-ventriculaire vs trans-cérébelleux, 1ère itération', 'value': 'ICC=0.985 (trans-ventriculaire, meilleur) / ICC=0.792 (trans-cérébelleux, plus faible)', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Validation', 'source_quote': 'the highest agreement in the transventricular plane (ICC = 0.985, JS = 0.989) and the lowest in the transcerebellum plane (ICC = 0.792, JS = 0.818)'}, {'outcome': 'Accord annotation LV, plan trans-ventriculaire vs trans-cérébelleux, 1ère itération', 'value': 'ICC=0.974 (trans-ventriculaire, meilleur) / ICC=0.218 (trans-cérébelleux, plus faible)', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Validation', 'source_quote': 'a high agreement in the transventricular plane (ICC = 0.974, JS = 0.989) and a low agreement in the transcerebellum plane (ICC = 0.218, JS = 0.125)'}, {'outcome': 'Accord annotation CSP, 2ème itération', 'value': 'ICC=0.887 (diverse head images, meilleur) / ICC=0.853 (trans-thalamique, plus faible)', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Validation', 'source_quote': 'The highest agreement is in the diverse head images group (ICC = 0.887, JS = 0.840), and the lowest is in the transthalamic plane (ICC = 0.853, JS = 0.760).'}, {'outcome': 'Accord annotation LV, 2ème itération', 'value': 'ICC=0.855 (trans-ventriculaire, meilleur) / ICC=0.662 (trans-cérébelleux, plus faible)', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Validation', 'source_quote': 'the highest agreement in the transventricular plane (ICC = 0.855, JS = 0.958) and the lowest in the transcerebellum plane (ICC = 0.662, JS = 0.5)'}, {'outcome': "Nombre d'instances par classe dans le jeu de données", 'value': 'brain=3794, CSP=1865, LV=1512', 'unit': 'instances', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Data Description', 'source_quote': 'the brain class comprising 3794 instances, the CSP class containing 1865 instances, and the LV class totaling 1512 instances'}], 'qualitative_findings': ["Désaccord entre le Radiologic Technologist (favorable à l'exclusion) et le Senior Physician (favorable à l'inclusion) concernant les images de tête diverses prises à un âge gestationnel inférieur à 14 semaines; la décision d'inclusion a suivi la recommandation du Senior Physician"], 'main_findings': ["L'accord sur l'annotation de la classe brain est excellent (ICC et JS constamment à 1) dans toutes les groupes, aux deux itérations", 'Le dataset final comprend 3832 images échographiques haute résolution (959×661 pixels) de têtes fœtales, réparties en quatre groupes de plans fœtaux, disponibles en 11 formats']}

## Conclusions

Le jeu de données présente une fiabilité d'annotation élevée, avec des valeurs ICC moyennes de 0.859 et 0.889, et des valeurs JS de 0.855 et 0.857 sur deux itérations Le dataset constitue une ressource précieuse et réutilisable pour la recherche actuelle et future en imagerie médicale et vision par ordinateur, notamment en diagnostic prénatal, diagnostic clinique et interventions assistées par ordinateur L'implication d'experts médicaux et l'évaluation de la fiabilité inter-évaluateurs soulignent l'importance de ces étapes dans le développement d'un jeu de données robuste et précis pour les modèles de machine learning

## 2023  The Author(s). Published by Elsevier Inc.

|  | This is an open access article under the CC BY license |
| --- | --- |
|  | ( http://creativecommons.org/licenses/by/4.0/ ) |
| Specifications Table |  |
| Subject | Computer Vision and Pattern Recognition. |
| Specific subject area | Ultrasound Fetal head dataset for computer vision tasks in prenatal diagnostics. |
| Data format | Raw, Analyzed |
| Type of data | Table, Image |
| Data collection |  |

## An overview of existing Fetal head ultrasound image datasets including computer vision task, and number of class.

| Dataset ID | Dataset | Computer vision task | Number | Format | Size |
| --- | --- | --- | --- | --- | --- |
|  |  |  | of classes |  |  |
| A | Fetal_Plane_DB | Image Classification | 9 | PNG images with classes | 12400 |
| B | Fetal_head_HC | Image segmentation | 1 | PNG images with | 999 |
|  | 18_Grand |  |  | corresponding masks |  |
| C | Our dataset | Classification, Segmentation, | 3 | PNG images with the | 3832 |
|  |  | and object detection |  | following format: CityScapes, |  |
|  |  |  |  | Datumaro, COCO, CVAT, |  |
|  |  |  |  | ImageNet, LabelMe, |  |
|  |  |  |  | OpenImage, PASCAL, |  |
|  |  |  |  | Segmentation masks, |  |
|  |  |  |  | TFRecord, YOLO |  |

## Intraclass Correlation Coefficient (ICC) and Jaccard similarity (JS) values for inter-rater reliability by fetal plane.

| 1st iteration: Rater Reliability between Student and Physician |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fetal Plane Group | Number of images | Brain ICC | CSP ICC | LV ICC | Brain JS | CSP JS | LV JS |
| Trans-Thalamic | 1565 | 0.940 | 0.939 | 0.662 | 0.999 | 0.929 | 0.603 |
| Trans-Ventricular | 584 | 1.00 | 0.985 | 0.974 | 1.00 | 0.989 | 0.989 |
| Trans-Cerebellum | 684 | 1.00 | 0.792 | 0.218 | 1.00 | 0.818 | 0.125 |
| Diverse head images | 999 | 1.00 | 0.871 | 0.926 | 1.00 | 0.875 | 0.930 |
| 2nd iteration: Rater Reliability between Student and Radiologic Technologist |  |  |  |
| Trans-Thalamic | 301 | 1.00 | 0.853 | 0.80 | 1.00 | 0.760 | 0.67 |
| Trans-Ventricular | 110 | 1.00 | 0.854 | 0.855 | 1.00 | 0.878 | 0.958 |
| Trans-Cerebellum | 150 | 1.00 | 0.865 | 0.662 | 1.00 | 0.833 | 0.50 |
| Diverse head images | 200 | 1.00 | 0.887 | 0.892 | 1.00 | 0.840 | 0.849 |

### Formule


$$IC C ( 2 , 1 ) = M S between -M S within M S between + ( k -1 ) M S within$$

### Formule


$$JS ( A, B ) = | A ∩ B | | AB |(2)$$
