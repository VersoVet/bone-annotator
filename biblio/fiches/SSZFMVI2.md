# Automated detection of chewing movements in videofluoroscopic swallowing studies using deep learning for landmark detection and motion analysis.

**Auteurs** : Bandini A, Lasala A, Peladeau-Pigeon M, Dharmarathna I, Gandhi P
**Année** : 2026
**DOI** : 10.1016/j.compbiomed.2025.111361

## Résumé

Chewing plays a critical role in safe and effective swallowing by breaking food into manageable pieces and mixing it with saliva to form a cohesive bolus. Impairments in this process, commonly seen in older adults and individuals with neurological conditions, increase the risk of choking, aspiration, and malnutrition. Although the videofluoroscopic swallowing study (VFSS) is considered the gold standard for evaluating swallowing function, automated analysis of chewing during VFSS remains largely unexplored. Manual assessments are time-consuming, variable, and rarely integrated into standard clinical protocols.

## Méthodologie

{'study_design': 'Pipeline automatisé composé de trois modules interconnectés : (1) un réseau de neurones convolutif (CNN) pour la détection de points de repère (landmarks) sur les images VFSS ; (2) un second CNN pour segmenter la vidéo et établir la limite temporelle supérieure de la phase de traitement oral (avant le début de la phase pharyngée) ; (3) segmentation des mouvements de la mâchoire en événements candidats par détection des maxima locaux dans la trajectoire du landmark du menton, puis classification de ces événements en mastication ou non-mastication.', 'intervention': None, 'control': None, 'primary_outcomes': ['Détection des landmarks anatomiques dans les images VFSS', 'Segmentation de la phase de traitement oral (oral-processing phase)', 'Classification des événements de mouvement de mâchoire en mastication ou non-mastication'], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [], 'qualitative_findings': [], 'main_findings': []}

## Conclusions

Un pipeline entièrement automatisé pour l'analyse de la mastication en VFSS intégrant détection de landmarks, segmentation vidéo et classification de la mastication a été proposé et validé. Chaque étape du pipeline atteint une performance élevée, démontrant la faisabilité d'approches de machine learning et deep learning pour étudier les mouvements de la mâchoire et distinguer les mouvements masticatoires des non-masticatoires. Il s'agit, à la connaissance des auteurs, de la première approche entièrement automatisée pour étudier la mastication en VFSS. Cette approche jette les bases d'une étude automatisée et quantitative de la mastication en VFSS et de la mise en relation de la phase orale de traitement des aliments avec la phase pharyngée de la déglutition. L'utilisation de la régression par heatmap pour la détection de landmarks et du machine learning pour la classification de la mastication permet d'atteindre une haute précision tout en répondant aux défis clés du suivi du mouvement mandibulaire. Le pipeline de traitement automatisé est composé de 3 modules interconnectés, dont 1) la détection de landmarks.

## Table I for a summary): the VFSS Landmark Dataset and the VFSS Chewing Dataset.

| The VFSS Landmark Dataset comprised 3593 individual video frames from a total of |
| --- |
| 152 participants selected from previous ClinicalTrials.gov datasets collected in the Steele |
| Swallowing Lab: NCT04114617 (Healthy liquid swallowing): n = 77; NCT05594173 |
| (Healthy liquid and food ingestion): n = 20; NCT03192358 (ALS, Parkinson Disease): n |
| = 35; NCT04112940 (Head and Neck Cancer): n = 11; NCT04114604 (Spinal Cord Injury): |
| n = 9. These frames were used for the development of the landmark detection CNN. The |
| dataset was divided into: (1) a training set consisting of 2340 frames from 98 participants, |
| (2) a validation set with 623 frames from 26 participants, and (3) a test set containing 630 |
| frames from 28 participants. These frames were randomly sampled from video clips of |
| liquid swallows and selected to capture various jaw openings, ensuring that the CNN could |
| detect jaw landmarks in diverse positions. |
| The VFSS Chewing Dataset was used to develop and validate the chewing classification |
| module. This dataset included 36 video clips from 6 participants from NCT05594173 |
| (Healthy liquid and food ingestion). Although the 6 participants were included in the test |
| set of the VFSS Landmark Dataset, the 36 video clips of this dataset were entirely separate |
| and not included in the VFSS Landmark Dataset. The clips in the VFSS Chewing Dataset |

## Demographic information of participants included in each dataset. Non-chewing data for these participants included in the test set of the VFSS Landmark Dataset.

| Dataset | Split (frame number) | Male n Female n Total n Age (years) |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Mean StDev |
| VFSS Landmark Dataset Training (2340 frames) | 56 | 42 | 98 | 47.3 | 17.7 |
|  | Validation (623 frames) 11 | 15 | 26 | 59.5 | 15.8 |
|  | Test (630 frames) | 22 | 6 | 28 | 60.4 | 21.6 |
| VFSS Chewing Dataset | 17,441 frames | 5 a | 1 a | 6 a | 24.0 | 1.5 |
|  | Total | 89 | 63 | 152 | 50.7 | 19.4 |
| a |  |  |  |  |  |  |

## F1-scores of the chewing classification for different classifiers. The top rows show results obtained using automatically identified candidate chewing cycles, while the bottom rows present classification performance achieved when ground truth onset and offset times were used for each cycle. For both strategies, the topperforming approaches (i.e., highest F1-score) are highlighted in bold. Classifiers include Multi-Layer Perceptron (MLP), XGBoost (XGB), Random Forest (RF), and Recurrent Neural Networks with GRU and LSTM units.

| MLP XGB RF | GRU LSTM |
| --- | --- |
