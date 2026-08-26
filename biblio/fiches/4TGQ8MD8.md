# Combined expert-in-the-loop—random forest multiclass segmentation U-net based artificial intelligence model: evaluation of non-small cell lung cancer in fibrotic and non-fibrotic microenvironments

**Auteurs** : Anjali Saqi, Yucheng Liu, Michelle Garlin Politis, Mary Salvatore, Sachin Jambawalikar
**Année** : 2024
**DOI** : 10.1186/s12967-024-05394-2

## Résumé

Abstract Background The tumor microenvironment (TME) plays a key role in lung cancer initiation, proliferation, invasion, and metastasis. Artificial intelligence (AI) methods could potentially accelerate TME analysis. The aims of this study were to (1) assess the feasibility of using hematoxylin and eosin (H&E)-stained whole slide images (WSI) to develop an AI model for evaluating the TME and (2) to characterize the TME of adenocarcinoma (ADCA) and squamous cell carcinoma (SCCA) in fibrotic and non-fibrotic lung. Methods The cohort was derived from chest CT scans of patients presenting with lung neoplasms, with and without background fibrosis. WSI images were generated from slides of all 76 available pathology cases with ADCA (n = 53) or SCCA (n = 23) in fibrotic (n = 47) or non-fibrotic (n = 29) lung. Detailed ground-truth annotations, including of stroma (i.e., fibrosis, vessels, inflammation), necrosis and background, were performed on WSI and optimized via an expert-in-the-loop (EI

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

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
