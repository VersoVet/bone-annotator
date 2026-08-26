# Combined expert-in-the-loop—random forest multiclass segmentation U-net based artificial intelligence model: evaluation of non-small cell lung cancer in fibrotic and non-fibrotic microenvironments

**Auteurs** : Anjali Saqi, Yucheng Liu, Michelle Garlin Politis, Mary Salvatore, Sachin Jambawalikar
**Année** : 2024
**DOI** : 10.1186/s12967-024-05394-2

## Résumé

Abstract
                Background
                The tumor microenvironment (TME) plays a key role in lung cancer initiation, proliferation, invasion, and metastasis. Artificial intelligence (AI) methods could potentially accelerate TME analysis. The aims of this study were to (1) assess the feasibility of using hematoxylin and eosin (H&amp;E)-stained whole slide images (WSI) to develop an AI model for evaluating the TME and (2) to characterize the TME of adenocarcinoma (ADCA) and squamous cell carcinoma (SCCA) in fibrotic and non-fibrotic lung.
              
                Methods
                The cohort was derived from chest CT scans of patients presenting with lung neoplasms, with and without background fibrosis. WSI images were generated from slides of all 76 available pathology cases with ADCA (n = 53) or SCCA (n = 23) in fibrotic (n = 47) or non-fibrotic (n = 29) lung. Detailed ground-truth annotations, including of stroma (i.e., fibrosis, vessels, inflammation), necrosis and background, were performed on WSI and optimized via an expert-in-the-loop (EITL) iterative procedure using a lightweight [random forest (RF)] classifier. A convolution neural network (CNN)-based model was used to achieve tissue-level multiclass segmentation. The model was trained on 25 annotated WSI from 13 cases of ADCA and SCCA within and without fibrosis and then applied to the 76-case cohort. The TME analysis included tumor stroma ratio (TSR), tumor fibrosis ratio (TFR), tumor inflammation ratio (TIR), tumor vessel ratio (TVR), tumor necrosis ratio (TNR), and tumor background ratio (TBR).
              
                Results
                The model’s overall classification for precision, sensitivity, and F1-score were 94%, 90%, and 91%, respectively. Statistically significant differences were noted in TSR (p = 0.041) and TFR (p = 0.001) between fibrotic and non-fibrotic ADCA. Within fibrotic lung, statistically significant differences were present in TFR (p = 0.039), TIR (p = 0.003), TVR (p = 0.041), TNR (p = 0.0003), and TBR (p = 0.020) between ADCA and SCCA.
              
                Conclusion
                The combined EITL—RF CNN model using only H&amp;E WSI can facilitate multiclass evaluation and quantification of the TME. There are significant differences in the TME of ADCA and SCCA present within or without background fibrosis. Future studies are needed to determine the significance of TME on prognosis and treatment.

## Méthodologie

{'study_design': "Développement et application d'un modèle d'IA combiné expert-in-the-loop (EITL) - random forest (RF) et segmentation multiclasse par réseau de neurones convolutionnel (CNN, type U-net) sur des WSI colorées à l'H&E, avec annotations de vérité terrain optimisées de manière itérative", 'intervention': "Modèle d'IA (EITL-RF-CNN) entraîné sur 25 WSI annotées provenant de 13 cas d'ADCA et de SCCA avec et sans fibrose, puis appliqué à la cohorte complète de 76 cas pour la segmentation tissulaire multiclasse (stroma, fibrose, vaisseaux, inflammation, nécrose, arrière-plan)", 'control': None, 'primary_outcomes': ['Performance de classification du modèle (précision, sensibilité, F1-score)', 'Ratios du microenvironnement tumoral : tumor stroma ratio (TSR), tumor fibrosis ratio (TFR), tumor inflammation ratio (TIR), tumor vessel ratio (TVR), tumor necrosis ratio (TNR), tumor background ratio (TBR)'], 'secondary_outcomes': [], 'statistical_methods': ['Comparaisons statistiques entre groupes fibrotique/non-fibrotique et entre ADCA/SCCA (tests de significativité avec valeurs p rapportées)', "Normalisation de couleur par densité optique (moyenne et variance) avant l'entraînement du modèle"], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'Précision globale de classification du modèle', 'value': '94%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results (Abstract)', 'source_quote': "The model's overall classification for precision, sensitivity, and F1-score were 94%, 90%, and 91%, respectively."}, {'outcome': 'Sensibilité globale de classification du modèle', 'value': '90%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results (Abstract)', 'source_quote': "The model's overall classification for precision, sensitivity, and F1-score were 94%, 90%, and 91%, respectively."}, {'outcome': 'F1-score global de classification du modèle', 'value': '91%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results (Abstract)', 'source_quote': "The model's overall classification for precision, sensitivity, and F1-score were 94%, 90%, and 91%, respectively."}, {'outcome': 'Tumor Stroma Ratio (TSR) entre ADCA fibrotique et non-fibrotique', 'value': None, 'unit': None, 'confidence_interval': None, 'p_value': 'p = 0.041', 'effect_size': None, 'source_section': 'Results (Abstract)', 'source_quote': 'Statistically significant differences were noted in TSR (p = 0.041) and TFR (p = 0.001) between fibrotic and non-fibrotic ADCA.'}, {'outcome': 'Tumor Fibrosis Ratio (TFR) entre ADCA fibrotique et non-fibrotique', 'value': None, 'unit': None, 'confidence_interval': None, 'p_value': 'p = 0.001', 'effect_size': None, 'source_section': 'Results (Abstract)', 'source_quote': 'Statistically significant differences were noted in TSR (p = 0.041) and TFR (p = 0.001) between fibrotic and non-fibrotic ADCA.'}, {'outcome': 'Tumor Fibrosis Ratio (TFR) entre ADCA et SCCA dans le poumon fibrotique', 'value': None, 'unit': None, 'confidence_interval': None, 'p_value': 'p = 0.039', 'effect_size': None, 'source_section': 'Results (Abstract)', 'source_quote': 'Within fibrotic lung, statistically significant differences were present in TFR (p = 0.039), TIR (p = 0.003), TVR (p = 0.041), TNR (p = 0.0003), and TBR (p = 0.020) between ADCA and SCCA.'}, {'outcome': 'Tumor Inflammation Ratio (TIR) entre ADCA et SCCA dans le poumon fibrotique', 'value': None, 'unit': None, 'confidence_interval': None, 'p_value': 'p = 0.003', 'effect_size': None, 'source_section': 'Results (Abstract)', 'source_quote': 'Within fibrotic lung, statistically significant differences were present in TFR (p = 0.039), TIR (p = 0.003), TVR (p = 0.041), TNR (p = 0.0003), and TBR (p = 0.020) between ADCA and SCCA.'}, {'outcome': 'Tumor Vessel Ratio (TVR) entre ADCA et SCCA dans le poumon fibrotique', 'value': None, 'unit': None, 'confidence_interval': None, 'p_value': 'p = 0.041', 'effect_size': None, 'source_section': 'Results (Abstract)', 'source_quote': 'Within fibrotic lung, statistically significant differences were present in TFR (p = 0.039), TIR (p = 0.003), TVR (p = 0.041), TNR (p = 0.0003), and TBR (p = 0.020) between ADCA and SCCA.'}, {'outcome': 'Tumor Necrosis Ratio (TNR) entre ADCA et SCCA dans le poumon fibrotique', 'value': None, 'unit': None, 'confidence_interval': None, 'p_value': 'p = 0.0003', 'effect_size': None, 'source_section': 'Results (Abstract)', 'source_quote': 'Within fibrotic lung, statistically significant differences were present in TFR (p = 0.039), TIR (p = 0.003), TVR (p = 0.041), TNR (p = 0.0003), and TBR (p = 0.020) between ADCA and SCCA.'}, {'outcome': 'Tumor Background Ratio (TBR) entre ADCA et SCCA dans le poumon fibrotique', 'value': None, 'unit': None, 'confidence_interval': None, 'p_value': 'p = 0.020', 'effect_size': None, 'source_section': 'Results (Abstract)', 'source_quote': 'Within fibrotic lung, statistically significant differences were present in TFR (p = 0.039), TIR (p = 0.003), TVR (p = 0.041), TNR (p = 0.0003), and TBR (p = 0.020) between ADCA and SCCA.'}], 'qualitative_findings': [], 'main_findings': ['Le modèle EITL-RF-CNN combiné basé uniquement sur des WSI H&E atteint une bonne performance de classification tissulaire multiclasse (précision 94%, sensibilité 90%, F1-score 91%)', 'Des différences significatives de TME existent entre ADCA fibrotique et non-fibrotique (TSR et TFR)', 'Des différences significatives de TME existent entre ADCA et SCCA au sein du poumon fibrotique (TFR, TIR, TVR, TNR, TBR)']}

## Conclusions

Le modèle combiné EITL-RF-CNN utilisant uniquement des WSI H&E peut faciliter l'évaluation et la quantification multiclasse du TME Il existe des différences significatives dans le TME de l'ADCA et du SCCA en présence ou en l'absence de fibrose de fond Des études futures sont nécessaires pour déterminer la signification du TME sur le pronostic et le traitement

## Imaging, demographics, available smoking status, specimen subtypes, and pathology diagnoses

| Lung Environment (Chest CT) | Fibrotic | Non- | Over- |
| --- | --- | --- | --- |
|  | Lung | fibrotic | all |
|  |  | Lung |  |
|  | 47 | 29 | 76 |
| Airways-centered fibrosis | 6 | N/A | 6 |
| Combined pulmonary fibrosis and | 2 | N/A | 2 |
| emphysema |  |  |  |
| Nonspecific interstitial pneumonia | 4 | N/A | 4 |
| Radiation fibrosis | 2 | N/A | 2 |
| Sarcoid | 2 | N/A | 2 |
| Usual interstitial pneumonia | 25 | N/A | 25 |
| Undetermined | 6 | N/A | 6 |
| Gender |  |  |  |
| Male | 32 | 13 | 45 |
| Female | 15 | 16 | 31 |
| Age |  |  |  |
| 50-59 |  | 2 | 2 |
| 60-69 | 7 | 4 | 11 |
| 70-79 | 17 | 12 | 29 |
| 80-89 | 13 | 8 | 21 |
| 90 and above | 10 | 3 | 13 |
| Smoking Status (Available) |  |  |  |
| Smoker | 11 | 12 | 23 |
| Non-smoker | 0 | 6 | 6 |
| Pathology Diagnosis |  |  |  |
| Adenocarcinoma | 28 | 25 | 53 |
| Squamous cell carcinoma | 19 | 4 | 23 |
| Specimen subtypes |  |  |  |
| Resection | 16 | 14 | 30 |
| Biopsy | 31 | 15 | 46 |
| Dominant Histology in Resections |  |  |  |
| Adenocarcinoma Resections | 12 | 14 | 26 |
| Well differentiated* | 0 | 0 | 0 |
| Moderately differentiated** | 12 | 11 | 23 |
| Poorly differentiated*** | 0 | 3 | 3 |
| Squamous cell carcinoma | 4 | 0 | 4 |

## Multiclass precision, sensitivity and F1

| Classes | Precision | Sensitivity (Recall) | F1-Score |
| --- | --- | --- | --- |
| Adenocarcinoma | 0.96 | 0.88 | 0.92 |
| Squamous | 0.94 | 0.88 | 0.91 |
| Stroma | 0.95 | 0.90 | 0.90 |
| Fibrosis | 0.98 | 0.73 | 0.90 |
| Vessels | 0.84 | 0.92 | 0.93 |
| Inflammation | 1.00 | 0.75 | 0.86 |
| Necrosis | 0.93 | 0.96 | 0.96 |
| Background Normal | 0.63 | 0.99 | 0.77 |
| Weighted Average | 0.94 | 0.90 | 0.91 |

### Formule


$$T SR = Stroma Stroma + T umor × 100%(1)$$

### Formule


$$T F R = F ibrosis F ibrosis + T umor × 100%(2)$$

### Formule


$$T IR = Inf lammation Inf lammation + T umor × 100%(3)$$

### Formule


$$T V R = V essels V essels + T umor × 100%(4)$$

### Formule


$$T NR = Necrosis Necrosis + T umor × 100%(5)$$

### Formule


$$T BR = Background Background + T umor × 100%(6)$$

### Formule


$$Recall (Sensitivity) = T P T P + F N (8) F 1 -score = 2 × Recall × P recision Recall + P recision(9)$$
