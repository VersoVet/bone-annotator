# Verification of Convolutional Neural Network Cephalometric Landmark Identification

**Auteurs** : Moshe Davidovitch, Tatiana Sella-Tunis, Liat Abramovicz, Shoshana Reiter, Shlomo Matalon, Nir Shpack
**Année** : 2022
**DOI** : 10.3390/app122412784

## Résumé

Introduction: The mass-harvesting of digitized medical data has prompted their use as a clinical and research tool. The purpose of this study was to compare the accuracy and reliability of artificial intelligence derived cephalometric landmark identification with that of human observers. Methods: Ten pre-treatment digital lateral cephalometric radiographs were randomly selected from a university post-graduate clinic. The x- and y-coordinates of 21 (i.e., 42 points) hard and soft tissue landmarks were identified by 6 specialists, 19 residents, 4 imaging technicians, and a commercially available convolutional neural network artificial intelligence platform (CephX, Orca Dental, Hertzylia, Israel). Wilcoxon, Spearman and Bartlett tests were performed to compare agreement of human and AI landmark identification. Results: Six x- or y-coordinates (14.28%) were found to be statistically different, with only one being outside the 2 mm range of acceptable error, and with 97.6% of coordinates fou

## Méthodologie

{'study_design': 'Comparative study of AI (CNN, Algoceph®/CephX) versus human observer identification of 21 lateral cephalometric landmarks (42 x,y coordinates) on 10 digital lateral cephalometric radiographs', 'intervention': 'Automatic landmark point detection using Algoceph® CNN AI platform (Orca Dental, Hertzliya, Israel), each point plotted 5 times', 'control': 'Manual landmark plotting performed once by each of 30 human operators (7 experienced orthodontic faculty members, 9 third year and 10 first year orthodontic residents, and 4 imaging center technicians)', 'primary_outcomes': ['Agreement (x and y coordinate accuracy) between AI and human landmark identification'], 'secondary_outcomes': ['Differences in landmark identification agreement among sub-categories of human observers (specialists, residents, technicians)'], 'statistical_methods': ['Kolmogorov-Smirnov test for normality', 'Wilcoxon Rank Sum Test', "Spearman's Correlation", "Bartlett's Test", 'Repeated Measures Analysis of Variance'], 'duration': None, 'setting': 'University post-graduate orthodontic clinic'}

## Résultats

{'quantitative': [{'outcome': 'Coordonnées statistiquement différentes entre IA et opérateurs', 'value': '6 sur 42 (14.28%)', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'Six x-or y-coordinates (14.28%) were found to be statistically different, with only one being outside the 2 mm range of acceptable error, and with 97.6% of coordinates found to be within this range.'}, {'outcome': 'Erreur SoftpogY', 'value': '2.67 mm ± 2.55 mm', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'For SoftpogY the difference was found to be 2.67 mm ± 2.55 mm, whereas for the remaining landmarks the mean recognition error was less than 1.5 mm.'}, {'outcome': 'Coordonnées fortement corrélées entre IA et humains', 'value': '36 sur 42 (85.72%)', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': 'r > 0.90', 'source_section': 'Results', 'source_quote': 'comparison of agreement between AI landmark detection and the x and y coordinates of each landmark as selected by the human operators found that 36 out of 42 (85.72%) of these coordinates were found to be highly correlated (r > 0.90).'}, {'outcome': 'Corrélation des points aberrants (outliers)', 'value': 'r = 0.729-0.891', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': 'r = 0.729-0.891', 'source_section': 'Results', 'source_quote': 'The aforementioned outliers were found to be moderately correlated (r = 0.729-0.891) (Table 2).'}, {'outcome': 'Chevauchement absolu entre scores IA et humains', 'value': '0.99', 'unit': None, 'confidence_interval': None, 'p_value': 'p < 0.001', 'effect_size': None, 'source_section': 'Results', 'source_quote': 'It can be seen that absolute overlap between scores was found 0.99, p < 0.001) (Figure 5).'}, {'outcome': "Test de Bartlett pour l'IA", 'value': 'χ2 = 2.98', 'unit': None, 'confidence_interval': None, 'p_value': 'p = 0.98', 'effect_size': None, 'source_section': 'Results', 'source_quote': "Bartlett's Test to show differences in variances between AI and observers showed this to be small for both AI (χ 2 = 2.98, p = 0.98), and operators (χ 2 = 2.72, p = 0.96)."}, {'outcome': 'Test de Bartlett pour les opérateurs', 'value': 'χ2 = 2.72', 'unit': None, 'confidence_interval': None, 'p_value': 'p = 0.96', 'effect_size': None, 'source_section': 'Results', 'source_quote': "Bartlett's Test to show differences in variances between AI and observers showed this to be small for both AI (χ 2 = 2.98, p = 0.98), and operators (χ 2 = 2.72, p = 0.96)."}, {'outcome': "Différence PNSX entre sous-catégories d'observateurs", 'value': 'F(1,9) = 10.44', 'unit': None, 'confidence_interval': None, 'p_value': 'p = 0.01', 'effect_size': None, 'source_section': 'Results', 'source_quote': 'differences for PNSX were F(1,9) = 10.44, p = 0.01, and that first-year residents (M = 76.33, SD = 3.63) and third-year residents (M = 76.89, SD = 4.19) differed more (higher) in the vertical axes compared to specialists (M = 74.93, SD = 4.19) and technicians (M = 75.00, SD = 3.80).'}, {'outcome': "Différence SoftnoseY entre sous-catégories d'observateurs", 'value': 'F(1,9) = 9.80', 'unit': None, 'confidence_interval': None, 'p_value': 'p = 0.01', 'effect_size': None, 'source_section': 'Results', 'source_quote': 'For Softnose Y, F(1,9) = 9.80, p = 0.01, it was found that third-year residents (M = 44.32, SD = 7.03), specialists (M = 44.52, SD = 6.56) and imaging technicians (M = 44.71, SD = 6.12) differed on the y axes (lower) compared to first-year residents (M = 42.92, SD = 6.88).'}], 'qualitative_findings': [], 'main_findings': ['All landmark identification points were found to be statistically similar except SoftpogY, UpperlipY, OrbitaleX, PTMX, PorionY and BasaleX.', '36 out of 42 (85.7%) coordinates showed no statistically significant differences between AI and all human observers.', '97.6% of coordinates were found within the 2 mm range of acceptable error, with only one coordinate outside this range.']}

## Conclusions

The use of convolutional neural network artificial intelligence as a tool for cephalometric landmark identification was found to be highly accurate and can serve as an aid in orthodontic diagnosis. The convolutional neural network artificial intelligence method for determining lateral cephalometric landmark identification was found to be significantly correlated to human identification of 21 lateral cephalometric radiographic anatomic landmarks. This implies that this application of AI can be used to reduce the time expenditure and human error involved in performing this task manually.

## ). Description of hard and soft tissue cranial landmarks used for comparative evalu human and AI detection.

|  | Landmark | Definition |
| --- | --- | --- |
| 1 | Sella | Midpoint of sella turcica |
| 2 | Nasion | Most anterior point on frontonasal suture |
| 3 | Upper incisor tip (UI) | Tip of most prominent upper central incisor |
| 4 | Lower incisor tip (LI) | Tip of most prominent lower central incisor |
| 5 | B point | Deepest bony point on mandibular symphysis between pogonion fradentale |
| 6 | Pogonion (Pog) | Most anterior point of mandibular symphysis |
| 7 | Menton | Lowest point on mandibular symphysis |
| 8 | Articulare | Junction between inferior surface of the cranial base and the pos border of the ascending ramus of the mandible |
| 9 | A point | deepest point of premaxilla concavity bellow ANS |
| 10 | ANS | Tip of anterior nasal spine |
| 11 | PNS | Posterior limit of bony palate |
|  | Soft pogonion |  |

## Description of hard and soft tissue cranial landmarks used for comparative evaluation of human and AI detection.

|  | Landmark | Definition |
| --- | --- | --- |
| 1 | Sella | Midpoint of sella turcica |
| 2 | Nasion | Most anterior point on frontonasal suture |
| 3 | Upper incisor tip (UI) | Tip of most prominent upper central incisor |
| 4 | Lower incisor tip (LI) | Tip of most prominent lower central incisor |
| 5 | B point | Deepest bony point on mandibular symphysis between pogonion and infradentale |
| 6 | Pogonion (Pog) | Most anterior point of mandibular symphysis |
| 7 | Menton | Lowest point on mandibular symphysis |
|  |  | Junction between inferior surface of the cranial base and |
| 8 | Articulare | the posterior border of the ascending ramus of the |
|  |  | mandible |
| 9 | A point | deepest point of premaxilla concavity bellow ANS |
| 10 | ANS | Tip of anterior nasal spine |

## Cont.

|  | Landmark | Definition |
| --- | --- | --- |
| 11 | PNS | Posterior limit of bony palate |
| 12 | Soft pogonion (Softpog) | Most anterior soft tissue point of soft chin |
| 13 | Soft B | The deepest soft tissue point between chin and subnasale |
| 14 | Lower lip | The most anterior point of lower lip |
| 15 | Upper lip | The most anterior point of upper lip |
| 16 | Subnasale | The junction where base of the columella of the nose meets the upper lip |
| 17 | Softnose | Most anterior point of nose tip |
| 18 | Orbitale | Most inferior point on the orbital margin |
|  |  | The intersection of the inferior border of the foramen |
| 19 | PTM | rotundum with the posterior wall of the |
|  |  | pterygomaxillary fissure |
| 20 | Porion | Most superior point of outline of external auditory meatus |
| 21 | Basale | The most inferior point on the anterior border of the foramen magnum in the midsagittal plane |

## Differences and correlations between Algoceph (algoX and algoY) and the operators' average (avgX and avgY). Note: significant differences are marked in bold, p < 0.01. ** significant Spearmen correlations. r > 0.729, p < 0.01.

| Landmark X/Y Coordinate | Differences between Measurement Scores | Spearman Correlation | Mean Recognition Error |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | Mean | Std. Deviation | p |  | Mean (mm) ± SD |
|  | Sella avgX | 54.67 | 3.73 | 0.114 | 0.988 ** | 0.14 ± 0.39 |
| 1 | Sella algoX | 54.81 | 3.74 |  |  |
|  | Sella avgY | 139.04 | 6.61 | 0.959 | 0.903 ** | 0.05 ± 1.28 |
| 2 | Sella algoY | 138.99 | 6.51 |  |  |

## Cont.

| Landmark X/Y Coordinate | Differences between Measurement Scores | Spearman Correlation | Mean Recognition Error |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | Mean | Std. Deviation | p |  | Mean (mm) ± SD |
|  | Nasion avgX | 119.94 | 5.75 | 0.285 | 0.952 ** | 0.17 ± 1.23 |
| 3 | Nasion algoX | 119.78 | 6.58 |  |  |
|  | Nasion avY | 150.26 | 7.08 | 0.878 | 0.976 ** | 0.21 ± 1.27 |
| 4 | Nasion algoY | 150.05 | 6.30 |  |  |
|  | Ui avgX | 125.41 | 4.39 | 0.799 | 0.912 ** | 0.17 ± 1.04 |
| 5 | Ui algoX | 125.58 | 4.44 |  |  |
|  | Ui avgY | 73.52 | 6.92 | 0.721 | 0.988 ** | 0.25 ± 1.02 |
| 6 | Ui algoY | 73.26 | 6.33 |  |  |
|  | Li avgX | 122.10 | 4.38 | 0.445 | 0.927 ** | 0.19 ± 1.05 |
| 7 | Li algoX | 121.91 | 4.30 |  |  |
|  | Li avgY | 75.68 | 6.34 | 0.114 | 0.998 ** | 0.39 ± 0.77 |
| 8 | Li algoY | 76.07 | 5.81 |  |  |
|  | B point avgX | 115.18 | 6.03 | 0.878 | 0.964 ** | 0.04 ± 1.13 |
| 9 | B point algoX | 115.22 | 5.77 |  |  |
|  | B point avgY | 56.65 | 6.23 | 0.921 | 0.988 ** | 0.01 ± 0.65 |
| 10 | B point algoY | 56.65 | 5.91 |  |  |
|  | Pog avgX | 116.02 | 7.16 | 0.721 | 0.915 ** | 0.11 ± 1.00 |
| 11 | Pog algoX | 115.91 | 7.01 |  |  |
|  | Pog avgY | 43.80 | 7.38 | 0.657 | 0.988 ** | 1.18 ± 0.90 |
| 12 | Pog algoY | 42.61 | 7.32 |  |  |
|  | Menton avgX | 109.56 | 7.03 | 0.891 | 0.976 ** | 0.07 ± 0.86 |
| 13 | Menton algoX | 109.49 | 6.78 |  |  |
|  | Menton avgY | 37.95 | 7.75 | 0.721 | 0.998 ** | 0.12 ± 0.71 |
| 14 | Menton algoY | 37.83 | 7.42 |  |  |
|  | Articulare avgX | 42.62 | 2.62 | 0.959 | 0.879 ** | 0.08 ± 1.11 |
| 15 | Articulare algoX | 42.54 | 2.84 |  |  |
|  | Articulare avgY | 108.06 | 5.97 | 0.799 | 0.915 ** | 0.08 ± 2.29 |
| 16 | Articulare algoY | 108.14 | 4.50 |  |  |
|  | A point avgX | 121.51 | 4.55 | 0.444 | 0.903 ** | 0.15 ± 1.03 |
| 17 | A point algoX | 121.35 | 4.58 |  |  |
|  | A point avgY | 95.44 | 6.24 | 0.721 | 0.964 ** | 0.18 ± 1.16 |
| 18 | A point algoY | 95.26 | 5.22 |  |  |
|  | ANS avgX | 125.92 | 4.27 | 0.872 | 0.915 ** | 0.88 ± 1.25 |
| 19 | ANS algoX | 125.03 | 4.12 |  |  |
|  | ANS avgY | 100.68 | 6.58 | 0.884 | 0.988 ** | 0.43 ± 1.29 |
| 20 | ANS algoY | 100.25 | 5.61 |  |  |
|  | PNS avgX | 75.83 | 4.27 | 0.782 | 0.867 ** | 0.13 ± 1.40 |
| 21 | PNS agoX | 75.70 | 3.82 |  |  |

## Cont.

| Landmark X/Y Coordinate | Differences between Measurement Scores | Spearman Correlation | Mean Recognition Error |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | Mean | Std. Deviation | p |  | Mean (mm) ± SD |
|  | PNS avgY | 98.51 | 5.29 | 0.918 | 0.976 ** | 0.23 ± 1.46 |
| 22 | PNS algoY | 98.75 | 4.15 |  |  |
|  | Soft pog avgX | 126.92 | 6.66 | 0.086 | 0.964 ** | 0.48 ± 1.67 |
| 23 | Soft pog algoX | 127.40 | 5.88 |  |  |
|  | Soft pog avgy | 44.06 | 6.83 | 0.022 | 0.842 ** | 2.67 ± 2.55 |
| 24 | Soft pog algoy | 46.74 | 5.83 |  |  |
|  | Soft b avgX | 126.20 | 5.16 | 0.878 | 0.988 ** | 0.05 ± 1.25 |
| 25 | Soft b algoX | 126.15 | 4.68 |  |  |
|  | Soft b avgY | 57.78 | 6.76 | 0.203 | 0.988 ** | 0.45 ± 0.98 |
| 26 | Soft b algoY | 58.24 | 5.99 |  |  |
|  | Lower lip avgX | 134.90 | 4.40 | 0.959 | 0.891 ** | 0.04 ± 1.05 |
| 27 | Lower lip algoX | 134.95 | 4.42 |  |  |
|  | Lower lip avgY | 68.75 | 7.41 | 0.721 | 0.998 ** | 0.03 ± 0.88 |
| 28 | Lower lip algoY | 68.79 | 6.64 |  |  |
|  | Upper lip avgX | 137.73 | 4.58 | 0.169 | 0.939 ** | 0.31 ± 0.96 |
| 29 | Upper lip algoX | 137.41 | 4.83 |  |  |
|  | Upper lip avgY | 82.05 | 7.28 | 0.017 | 0.964 ** | 1.11 ± 1.16 |
| 30 | Upper lip algoY | 83.17 | 6.53 |  |  |
|  | Subnasale avgX | 136.32 | 4.44 | 0.541 | 0.915 ** | 0.10 ± 1.33 |
| 31 | Subnasale algoX | 136.43 | 4.75 |  |  |
|  | Subnasale avgY | 96.84 | 7.21 | 0.386 | 0.964 ** | 0.35 ± 1.42 |
| 32 | Subnasale algoY | 96.48 | 6.05 |  |  |
|  | Soft nose avgX | 150.25 | 5.35 | 0.381 | 0.976 ** | 0.30 ± 1.27 |
| 33 | Soft nose algoX | 150.55 | 5.96 |  |  |
|  | Soft nose avgY | 108.63 | 8.31 | 0.918 | 0.975 ** | 0.01 ± 0.75 |
| 34 | Soft nose algoY | 108.63 | 7.65 |  |  |
|  | Orbitale avgX | 105.67 | 3.90 | 0.037 | 0.976 ** | 1.07 ± 1.29 |
| 35 | Orbitale algoX | 106.74 | 4.56 |  |  |
|  | Orbitale avgY | 123.12 | 6.63 | 0.878 | 0.915 ** | 0.16 ± 1.09 |
| 36 | Orbitale algoY | 122.96 | 6.10 |  |  |
|  | PTM avgX | 70.19 | 4.03 | 0.028 | 0.939 ** | 0.99 ± 0.98 |
| 37 | PTM algoX | 71.19 | 4.38 |  |  |
|  | PTM avgY | 123.11 | 6.27 | 0.241 | 0.927 ** | 0.98 ± 1.95 |
| 38 | PTM algoY | 124.10 | 5.00 |  |  |
|  | Porion avgX | 32.75 | 2.57 | 0.285 | 0.729 ** | 0.64 ± 1.49 |
| 39 | Porion algoX | 32.11 | 3.25 |  |  |
|  | Porion avgY | 120.08 | 4.38 | 0.036 | 0.830 ** | 1.14 ± 1.41 |
| 40 | Porion algoY | 121.23 | 4.27 |  |  |

## Cont.

| Landmark X/Y Coordinate | Differences between Measurement Scores | Spearman Correlation | Mean Recognition Error |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | Mean | Std. Deviation | p |  | Mean (mm) ± SD |
|  | Basale avgX | 35.89 | 3.15 | 0.005 | 0.903 ** | 1.03 ± 0.90 |
| 41 | Basale algoX | 34.86 | 3.36 |  |  |
|  | Basale avgY | 100.71 | 5.18 | 0.959 | 0.976 ** | 0.02 ± 1.20 |
| 42 | Basale algoY | 100.74 | 4.83 |  |  |

## Mean measurement error (mm) of human vs. AI from early studies.

| Landmark | Liu et al. [19] | Hutton et al. [8] | Saad et al. [20] Tanikawa et al. [21] | Rudolph et al. [7] | CephX Algo |
| --- | --- | --- | --- | --- | --- | --- |
| Sella | 0.94 | 5.5 | 3.24 | 2.1 | 5.06 | 0.148 |
| Nasion | 2.32 | 5.6 | 2.95 | 1.7 | 2.57 | 0.27 |
| Orbitale | 5.28 | 5.5 | 3.4 | 2.24 | 2.46 | 1.08 |
| Porion | 2.43 | 7.3 | 3.48 | 3.63 | 5.67 | 1.3 |
| ANS | 2.9 | 3.8 | 2.7 | 2.32 | 2.64 | 0.97 |
| Point A | 4.29 | 3.3 | 2.54 | 2.13 | 2.33 | 0.23 |
| Point B | 3.96 | 2.6 | 2.22 | 3.12 | 1.85 | 0.04 |
| Pogonion | 2.53 | 2.7 | 3.65 | 1.91 | 1.85 | 1.18 |
| Menton | 1.9 | 2.7 | 4.4 | 1.59 | 3.09 | 0.12 |
| UI | 2.36 | 2.9 | 3.65 | 1.78 | NAD | 0.3 |
| LI | 2.86 | NAD | 3.14 | 1.81 | NAD | 0.35 |
