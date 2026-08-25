# Automating Ground Truth Annotations for Gland Segmentation Through Immunohistochemistry.

**Auteurs** : Tushar Kataria, Saradha Rajamani, Abdul Bari Ayubi, Mary Bronner, Jolanta Jedrzkiewicz, Beatrice S Knudsen, Shireen Y Elhabian
**Année** : 2023
**DOI** : 10.1016/j.modpat.2023.100331

## Résumé

Microscopic evaluation of glands in the colon is of utmost importance in the diagnosis of inflammatory bowel disease and cancer. When properly trained, deep learning pipelines can provide a systematic, reproducible, and quantitative assessment of disease-related changes in glandular tissue architecture. The training and testing of deep learning models require large amounts of manual annotations, which are difficult, time-consuming, and expensive to obtain. Here, we propose a method for automated generation of ground truth in digital hematoxylin and eosin (H&E)-stained slides using immunohistochemistry (IHC) labels. The image processing pipeline generates annotations of glands in H&E histopathology images from colon biopsy specimens by transfer of gland masks from KRT8/18, CDX2, or EPCAM IHC. The IHC gland outlines are transferred to coregistered H&E images for training of deep learning models. We compared the performance of the deep learning models to that of manual annotations using a

## Méthodologie

{'study_design': "Pipeline de traitement d'image générant des annotations de glandes dans des images H&E de biopsies coliques par transfert de masques de glandes obtenus à partir de coupes IHC (CK8/18, CDX2, ou EpCAM) co-enregistrées ; entraînement et évaluation de modèles de deep learning de segmentation de glandes, comparaison à des annotations manuelles sur un jeu de test interne et sur deux jeux de données publics (GLAS, CRAG)", 'intervention': "Utilisation de masques de glandes générés automatiquement à partir de marqueurs IHC (seuillage de l'intensité de coloration brune) transférés sur images H&E, comme vérité terrain pour l'entraînement des modèles de deep learning", 'control': 'Annotations manuelles de glandes réalisées par des pathologistes', 'primary_outcomes': ['Score DICE de concordance entre les segmentations générées par les modèles entraînés sur données IHC et les annotations manuelles'], 'secondary_outcomes': ['Généralisation des modèles sur des jeux de données publics externes (GLAS, CRAG)', "Performance avec technique d'échantillonnage de données mixtes (cohorte interne + petit nombre d'échantillons annotés externes)"], 'statistical_methods': ['Score DICE'], 'duration': None, 'setting': 'Laboratoire certifié CLIA/CAP pour la coloration IHC ; jeu de test interne de biopsies plus jeux de données publics GLAS et CRAG'}

## Résultats

{'quantitative': [{'outcome': 'Concordance entre masques EpCAM IHC et annotations manuelles de glandes', 'value': '0.89', 'unit': 'score DICE', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Our results show that EpCAM IHC provides gland outlines that closely match manual gland annotations (DICE = 0.89) and are robust to damage by inflammation.'}, {'outcome': 'Score DICE moyen sur le jeu de données public GLAS (10% de cas annotés)', 'value': '0.902', 'unit': 'score DICE', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The best-performing models achieved average DICE scores of 0.902 and 0.89, respectively, on GLAS and CRAG colon cancer public datasets when trained with only 10% of annotated cases from either public cohort.'}, {'outcome': 'Score DICE moyen sur le jeu de données public CRAG (10% de cas annotés)', 'value': '0.89', 'unit': 'score DICE', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The best-performing models achieved average DICE scores of 0.902 and 0.89, respectively, on GLAS and CRAG colon cancer public datasets when trained with only 10% of annotated cases from either public cohort.'}, {'outcome': "Score DICE moyen sur le jeu de données public CRAG avec méthode d'échantillonnage optimisée", 'value': '0.927', 'unit': 'score DICE', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'We report average Dice scores on both public CRAG (Dice = 0.927) and GLAS (Dice = 0.922) datasets using an optimized data sampling method.'}, {'outcome': "Score DICE moyen sur le jeu de données public GLAS avec méthode d'échantillonnage optimisée", 'value': '0.922', 'unit': 'score DICE', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'We report average Dice scores on both public CRAG (Dice = 0.927) and GLAS (Dice = 0.922) datasets using an optimized data sampling method.'}], 'qualitative_findings': ['Les modèles entraînés sur des glandes normales performent significativement moins bien sur des glandes de cancer colique, illustrant un biais de texture des modèles de deep learning', 'Un faible pourcentage de données annotées externes de la cohorte cible (moins de 10 échantillons, ~5%) permet une amélioration importante des performances et de la généralisation', "Les modèles entraînés sur des données mixtes (cohorte interne + quelques images de la cohorte cible) surpassent les modèles entraînés sur 100% des données d'entraînement de la cohorte cible", "L'ajout de données provenant de plusieurs sources réduit le biais du modèle par rapport à une seule source externe"], 'main_findings': ["EpCAM IHC fournit des contours de glandes qui correspondent étroitement aux annotations manuelles (DICE = 0.89) et sont robustes aux dommages liés à l'inflammation", 'Les meilleurs modèles atteignent des scores DICE moyens de 0.902 (GLAS) et 0.89 (CRAG) avec seulement 10% de cas annotés', "Les annotations automatisées par marqueurs IHC spécifiques d'un type cellulaire peuvent remplacer sans risque les annotations manuelles", "La combinaison d'annotations automatisées IHC d'une cohorte unique avec un petit nombre de cas annotés manuellement de cohortes multi-institutionnelles permet d'entraîner des modèles qui généralisent bien à des sources de données diverses"]}

## Conclusions

La méthode proposée permet la collecte d'une quantité illimitée de données automatiquement annotées, éliminant le besoin d'annotation manuelle par les pathologistes Les annotations dérivées d'EpCAM et de CK8/18 atteignent le plus haut niveau de concordance avec les annotations manuelles pour la segmentation des glandes coliques dans le cadre des MICI La stratégie de mélange de données proposée pour l'adaptation de domaine surpasse systématiquement d'autres approches hautement supervisées et de fine-tuning pour la segmentation de glandes Les auteurs prévoient d'étendre la méthodologie à l'annotation de multiples types de cellules immunitaires et à l'annotation nucléaire, dans le but ultime d'automatiser l'évaluation de l'activité de la maladie dans les biopsies de MICI

## Binary IHC masks against manual gland. Binary masks generated by IHC markers listed in the first column. The masks are overlaid on manual gland annotations to calculate Dice score and Jaccard index

|  | Dice | Jaccard |
| --- | --- | --- |
| CDX2 | 0.807 | 0.6775 |
| EpCAM 0.8631 | 0.7656 |
| CK8/18 0.8395 | 0.7245 |

### Formule


$$threshold_value = mean(DAB_channel) -standard_devation(DAB_channel)(1)$$

### Formule


$$Dice = 2 * P * GT P + GT Jaccard = P ∩ GT P ∪ GT$$
