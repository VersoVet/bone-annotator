# Automating Ground Truth Annotations for Gland Segmentation Through Immunohistochemistry.

**Auteurs** : Tushar Kataria, Saradha Rajamani, Abdul Bari Ayubi, Mary Bronner, Jolanta Jedrzkiewicz, Beatrice S Knudsen, Shireen Y Elhabian
**Année** : 2023
**DOI** : 10.1016/j.modpat.2023.100331

## Résumé

Microscopic evaluation of glands in the colon is of utmost importance in the diagnosis of inflammatory bowel disease and cancer. When properly trained, deep learning pipelines can provide a systematic, reproducible, and quantitative assessment of disease-related changes in glandular tissue architecture. The training and testing of deep learning models require large amounts of manual annotations, which are difficult, time-consuming, and expensive to obtain. Here, we propose a method for automated generation of ground truth in digital hematoxylin and eosin (H&E)-stained slides using immunohistochemistry (IHC) labels. The image processing pipeline generates annotations of glands in H&E histopathology images from colon biopsy specimens by transfer of gland masks from KRT8/18, CDX2, or EPCAM IHC. The IHC gland outlines are transferred to coregistered H&E images for training of deep learning models. We compared the performance of the deep learning models to that of manual annotations using a

## Méthodologie

{'study_design': "Pipeline de traitement d'images générant des annotations de glandes dans des images H&E de biopsies coliques par transfert de masques de glandes issus de lames IHC (CK8/18, CDX2 ou EpCAM) co-enregistrées, utilisés pour entraîner des modèles de deep learning en segmentation glandulaire, testés en interne et sur des jeux de données publics externes.", 'intervention': "Génération automatique de masques de glandes par seuillage de l'intensité de coloration brune (IHC) et transfert vers l'image H&E correspondante, utilisée pour l'entraînement des modèles de deep learning.", 'control': 'Annotations manuelles de glandes réalisées par des pathologistes, utilisées comme référence de comparaison.', 'primary_outcomes': ['Score DICE de concordance entre les masques de glandes générés par le modèle (entraîné sur annotations IHC) et les annotations manuelles'], 'secondary_outcomes': ['Performance de généralisation des modèles sur les jeux de données publics GLAS et CRAG', "Effet de la technique d'échantillonnage de données mixtes sur l'adaptation à de nouvelles cohortes"], 'statistical_methods': ["Coefficient DICE (Dice score) pour l'évaluation de la segmentation"], 'duration': None, 'setting': 'Coloration IHC réalisée dans un laboratoire certifié CLIA/CAP ; évaluation sur cohorte interne et sur les jeux de données publics GLAS et CRAG (cancer colorectal).'}

## Résultats

{'quantitative': [{'outcome': 'Concordance des contours de glandes générés par EpCAM IHC avec les annotations manuelles', 'value': '0.89', 'unit': 'DICE', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Our results show that EpCAM IHC provides gland outlines that closely match manual gland annotations (DICE = 0.89) and are robust to damage by inflammation.'}, {'outcome': 'Score DICE moyen des meilleurs modèles sur GLAS et CRAG avec seulement 10% de cas annotés', 'value': '0.902 (GLAS), 0.89 (CRAG)', 'unit': 'DICE', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The best-performing models achieved average DICE scores of 0.902 and 0.89, respectively, on GLAS and CRAG colon cancer public datasets when trained with only 10% of annotated cases from either public cohort.'}, {'outcome': "Score DICE moyen sur les jeux de données publics avec méthode d'échantillonnage optimisée", 'value': '0.927 (CRAG), 0.922 (GLAS)', 'unit': 'DICE', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'We report average Dice scores on both public CRAG (Dice = 0.927) and GLAS (Dice = 0.922) datasets using an optimized data sampling method.'}, {'outcome': 'Comparaison avec scores DICE précédemment publiés', 'value': '0.902 et 0.909 (littérature antérieure)', 'unit': 'DICE', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The Dice scores we obtain are greater than previously reported Dice scores of 0.902 and 0.909'}, {'outcome': 'Quantité minimale de données annotées externes nécessaire pour améliorer la généralisation', 'value': '5% (<10 échantillons)', 'unit': "pourcentage de cas annotés / nombre d'échantillons", 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'a small amount of annotated external data from tissues in the target cohort (5 percent <10 samples) resulted in large performance increases and improved generalization'}], 'qualitative_findings': ['Les modèles entraînés sur des glandes normales performent significativement moins bien sur des glandes de cancer colique, ce qui est attribué à un biais de texture des modèles de deep learning', "L'ajout de données provenant de plusieurs sources réduit le biais du modèle par rapport à l'utilisation d'une seule source externe"], 'main_findings': ["EpCAM IHC fournit des contours de glandes proches des annotations manuelles (DICE = 0.89) et robustes aux dommages liés à l'inflammation", 'Des modèles entraînés avec seulement 10% des cas annotés des cohortes publiques atteignent des performances élevées (GLAS = 0.902, CRAG = 0.89)', "Une stratégie de mélange de données (cohorte interne + peu d'échantillons de la cohorte cible) surpasse les modèles entraînés sur 100% des données de la cohorte cible", 'Les annotations automatisées par marqueurs IHC spécifiques de type cellulaire peuvent remplacer en toute sécurité les annotations manuelles']}

## Conclusions

Les annotations de vérité terrain dérivées d'EpCAM et de CK8/18 atteignent le plus haut niveau de concordance avec les annotations manuelles pour la segmentation des glandes coliques La stratégie proposée de mélange de données pour l'adaptation de domaine surpasse systématiquement les approches hautement supervisées ou de fine-tuning classiques La méthode permet la collecte d'une quantité illimitée de données automatiquement annotées, éliminant le besoin d'annotation manuelle par les pathologistes Les auteurs prévoient d'étendre la méthodologie aux annotations de multiples types de cellules immunitaires et aux annotations nucléaires, dans le but d'automatiser l'évaluation de l'activité de la maladie dans les biopsies de MICI

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
