# Deep Learning Method for Precise Landmark Identification and Structural Assessment of Whole-Spine Radiographs

**Auteurs** : Sung Hyun Noh, Gaeun Lee, Hyun‐Jin Bae, Ju Han, Su Jeong Son, Deok Ryong Kim, Jeong Yeon Park, Seung Kyeong Choi, Pyung Goo Cho, Sang Hyun Kim
**Année** : 2024
**DOI** : 10.3390/bioengineering11050481

## Résumé

This study measured parameters automatically by marking the point for measuring each parameter on whole-spine radiographs. Between January 2020 and December 2021, 1017 sequential lateral whole-spine radiographs were retrospectively obtained. Of these, 819 and 198 were used for training and testing the performance of the landmark detection model, respectively. To objectively evaluate the program's performance, 690 whole-spine radiographs from four other institutions were used for external validation. The combined dataset comprised radiographs from 857 female and 850 male patients (average age 42.2 ± 27.3 years; range 20-85 years). The landmark localizer showed the highest accuracy in identifying cervical landmarks (median error 1.5-2.4 mm), followed by lumbosacral landmarks (median error 2.1-3.0 mm). However, thoracic landmarks displayed larger localization errors (median 2.4-4.3 mm), indicating slightly reduced precision compared with the cervical and lumbosacral regions. The agreement

## Méthodologie

{'study_design': "Étude rétrospective de développement et validation d'un modèle de deep learning pour la localisation automatique de landmarks anatomiques sur radiographies latérales du rachis complet, avec entraînement, test interne et validation externe multicentrique", 'intervention': "Modèle de deep learning (localisateur de landmarks) appliqué aux radiographies pour identifier automatiquement les points anatomiques et calculer les paramètres d'alignement spinal", 'control': 'Mesures manuelles réalisées par deux experts humains servant de référence de comparaison', 'primary_outcomes': ['Précision de localisation des landmarks anatomiques (erreur de mesure en mm)', 'Accord entre le modèle de deep learning et les experts (coefficient de corrélation intraclasse)'], 'secondary_outcomes': ['Performance du modèle sur le jeu de validation externe', 'Comparaison statistique des paramètres entre les différents jeux de données'], 'statistical_methods': ['Coefficient de corrélation intraclasse (ICC)', 'Tests statistiques de comparaison entre datasets (non spécifiés précisément dans le texte fourni)'], 'duration': 'Données collectées entre janvier 2020 et décembre 2021', 'setting': 'Multicentrique (dataset principal + quatre institutions supplémentaires pour la validation externe)'}

## Résultats

{'quantitative': [{'outcome': 'Erreur de localisation des landmarks cervicaux', 'value': '1.5-2.4', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The landmark localizer showed the highest accuracy in identifying cervical landmarks (median error 1.5-2.4 mm)'}, {'outcome': 'Erreur de localisation des landmarks lombosacrés', 'value': '2.1-3.0', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'followed by lumbosacral landmarks (median error 2.1-3.0 mm)'}, {'outcome': 'Erreur de localisation des landmarks thoraciques', 'value': '2.4-4.3', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'However, thoracic landmarks displayed larger localization errors (median 2.4-4.3 mm), indicating slightly reduced precision compared with the cervical and lumbosacral regions.'}, {'outcome': 'Coefficient de corrélation intraclasse (accord modèle vs experts)', 'value': '>0.88', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The agreement between the deep learning model and two experts was good to excellent, with intraclass correlation coefficient values >0.88.'}, {'outcome': 'Nombre de paramètres sagittaux critiques mesurés', 'value': '15', 'unit': 'paramètres', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'Our study introduced a DL model that shows performance comparable to that of human observers in accurately measuring 15 critical sagittal spinal parameters across various spinal conditions.'}], 'qualitative_findings': [], 'main_findings': ['Le localisateur de landmarks montre la meilleure précision pour les landmarks cervicaux, suivis des landmarks lombosacrés, puis thoraciques', "L'accord entre le modèle et deux experts humains est bon à excellent", 'Le modèle performe bien sur le jeu de validation externe', 'Aucune différence statistique significative entre les datasets pour tous les paramètres']}

## Conclusions

Le système d'analyse d'alignement automatique proposé identifie les points anatomiques et les positions du rachis avec une haute précision Le système génère divers paramètres d'imagerie radiographique qui présentent une bonne corrélation avec les mesures manuelles Le modèle de deep learning est capable d'interpréter automatiquement et de manière cohérente les courbes sagittales du rachis

## Names and descriptions of landmarks annotated on whole-spine lateral X-ray.

| Name | Description |
| --- | --- |
| FH_1 | Center of the Femur head |
| FH_2 | Center of the Femur head |
| S_1 | Anterior point of the upper endplate of the sacrum |

## Cont.

| Name | Description |
| --- | --- |
| S_2 | Posterior point of the upper endplate of the sacrum |
| L1_1 | Anterior point of the upper endplate of the L1 vertebra |
| L1_2 | Posterior point of the upper endplate of the L1 vertebra |
| L4_1 | Anterior point of the upper endplate of the L4 vertebra |
| L4_2 | Posterior point of the upper endplate of the L4 vertebra |
| T4_1 | Anterior point of the upper endplate of the T4 vertebra |
| T4_2 | Posterior point of the upper endplate of the T4 vertebra |
| T12_1 | Anterior point of the lower endplate of the T12 vertebra |
| T12_2 | Posterior point of the lower endplate of the T12 vertebra |
| T1 | Center of the T1 vertebral body |
| Forehead | Forehead |
| FM_1 | Anterior point of the foramen magnum |
| FM_2 | Posterior point of the foramen magnum |
| ODT | Odontoid |
| Jaw | Jaw |
| C2_1 | Anterior |

## Cont.

| Name |
| --- |

## Inter-rater reliability between the two human experts and developed deep learning model.

| Parameters | R1 versus R2 | DL versus R1 | DL versus R2 |
| --- | --- | --- | --- |
| PI (°) | 0.978 | 0.891 | 0.889 |
| PT (°) | 0.981 | 0.923 | 0.915 |
| SS (°) | 0.962 | 0.905 | 0.897 |
| LL (°) | 0.957 | 0.921 | 0.915 |
| L4S1 (°) | 0.961 | 0.901 | 0.894 |
| TK (°) | 0.979 | 0.945 | 0.931 |
| TPA (°) | 0.945 | 0.894 | 0.884 |
| CBVA (°) | 0.951 | 0.907 | 0.901 |
| C2C7 (°) | 0.947 | 0.887 | 0.881 |
| TS (°) | 0.923 | 0.915 | 0.909 |
| TS-CL (°) | 0.914 | 0.909 | 0.897 |
| ODHA (°) | 0.928 | 0.903 | 0.891 |
| PI-LL (°) | 0.927 | 0.896 | 0.884 |
| SSA (°) | 0.944 | 0.945 | 0.925 |
| SVA (mm) | 0.957 | 0.912 | 0.902 |

## Inter-rater reliability between the two human experts and developed deep learning model.

| Parameters | R1 versus R2 | DL versus R1 | DL versus R2 |
| --- | --- | --- | --- |
| PI ( • ) | 0.978 | 0.891 | 0.889 |
| PT ( • ) | 0.981 | 0.923 | 0.915 |
| SS ( • ) | 0.962 | 0.905 | 0.897 |
| LL ( • ) | 0.957 | 0.921 | 0.915 |
| L4S1 ( • ) | 0.961 | 0.901 | 0.894 |
| TK ( • ) | 0.979 | 0.945 | 0.931 |
| TPA ( • ) | 0.945 | 0.894 | 0.884 |
| CBVA ( • ) | 0.951 | 0.907 | 0.901 |
| C2C7 ( • ) | 0.947 | 0.887 | 0.881 |
| TS ( • ) | 0.923 | 0.915 | 0.909 |
| TS-CL ( • ) | 0.914 | 0.909 | 0.897 |
| ODHA ( • ) | 0.928 | 0.903 | 0.891 |
| PI-LL ( • ) | 0.927 | 0.896 | 0.884 |
| SSA ( • ) | 0.944 | 0.945 | 0.925 |
| SVA (mm) | 0.957 | 0.912 | 0.902 |
| PI, pelvic incidence; PT, pelvic tilt; SS, sacral slope; LL, lumbar lordosis; L4S1, L4S1 lordosis; TK, thoracic kyphosis; |
| TPA, T1 pelvic angle; CBVA, chin-brow vertical angle; C2C7, C2C7 angle; TS, T1 slope; TS-CL, T1 slope-cervical |
| lordosis; ODHA, odontoid hip axis angle; PI-LL, pelvic incidence-lumbar lordosis; SSA, spino-sacral angle; SVA, |
| sagittal vertical axis. |  |  |  |

## Performance evaluation of the spinal parameters of the deep learning model.

|  |  |  | Correlation Analysis | Wilcoxon Signed-Rank Test |
| --- | --- | --- | --- | --- | --- |
| Parameters | Ground Truth | Parameter Error | R | p Value | p Value |
| PI ( • ) | 53.8 ± 18.8 • | 2.6 ± 3.1 • | 0.982 |  | 0.497 |
| PT ( • ) | 14.8 ± 11.3 • | 1.8 ± 2.2 • | 0.917 |  | 0.512 |
| SS ( • ) | 39.4 ± 7.9 • | 2.2 ± 3.4 • | 0.912 |  | 0.459 |
| LL ( • ) | 41.2 ± 17.3 • | 5.7 ± 3.5 • | 0.991 |  | 0.279 |
| L4S1 ( • ) | 30.7 ± 11.6 • | 4.5 ± 2.8 • | 0.857 |  | 0.247 |
| TK ( • ) | 27.2 ± 11.2 • | 5.5 ± 4.5 • | 0.812 |  | 0.078 |
| TPA ( • ) | 24.9 ± 23.2 • | 1.8 ± 1.1 • | 0.792 |  | 0.758 |
| CBVA ( • ) C2C7 ( • ) | 1.8 ± 5.2 • 13.6 ± 9.7 • | 0.7 ± 0.6 • 5.5 ± 6.5 • | 0.984 0.845 | <0.001 * | 0.678 0.598 |
| TS ( • ) | 22.8 ± 10.2 • | 5.7 ± 6.2 • | 0.784 |  | 0.084 |
| TS-CL ( • ) | 9.8 ± 2.4 • | 4.1 ± 5.9 • | 0.809 |  | 0.097 |
| ODHA ( • ) | 4.3 ± 5.4 • | 0.2 ± 0.2 • | 0.978 |  | 0.594 |
| PI-LL ( • ) | 12.1 ± 7.5 • | 3.0 ± 4.5 • | 0.962 |  | 0.596 |
| SSA ( • ) | 120.1 ± 12.4 • | 3.3 ± 2.5 • | 0.927 |  | 0.492 |
| SVA (mm) | 22.1 ± 19.2 mm | 3.0 ± 2.9 mm | 0.986 |  | 0.745 |
|  | PI, pelvic incidence; PT, pelvic tilt; SS, sacral slope; LL, lumbar lordosis; L4S1, L4S1 lordosis; TK, thoracic kyphosis; |
|  | TPA, T1 pelvic angle; CBVA, chin-brow vertical angle; C2C7, C2C7 angle; TS, T1 slope; TS-CL, T1 slope-cervical |
|  | lordosis; ODHA, odontoid hip axis angle; PI-LL, pelvic incidence-lumbar lordosis; SSA, spino-sacral angle; SVA, |
|  | sagittal vertical axis; * p value < 0.05. |  |  |  |

## Cont.

|  |  |  | External- | External- | External- | External- |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Parameters | Ground Truth | Parameter Error | Validation Dataset 1 | Validation Dataset 2 | Validation Dataset 3 | Validation Dataset 4 | p-Value |
|  |  |  | Error | Error | Error | Error |  |
| TPA ( • ) | 24.9 ± 23.2 • | 1.8 ± 1.1 • | 1.4 ± 1.8 • | 1.9 ± 1.7 • | 1.9 ± 1.9 • | 1.5 ± 1.1 • | 0.798 |
| CBVA ( • ) | 1.8 ± 5.2 • | 0.7 ± 0.6 • | 0.6 ± 0.4 • | 0.4 ± 0.2 • | 0.8 ± 1.4 • | 0.8 ± 1.0 • | 0.571 |
| C2C7 ( • ) | 13.6 ± 9.7 • | 5.5 ± 6.5 • | 4.6 ± 4.4 • | 5.4 ± 5.2 • | 4.8 ± 5.4 • | 5.8 ± 4.0 • | 0.435 |
| TS ( • ) | 22.8 ± 10.2 • | 5.7 ± 6.2 • | 4.4 ± 4.4 • | 5.1 ± 6.1 • | 5.7 ± 4.6 • | 5.4 ± 6.4 • | 0.645 |
| TS-CL ( • ) | 9.8 ± 2.4 • | 4.1 ± 5.9 • | 4.5 ± 6.3 • | 4.1 ± 5.3 • | 3.9 ± 4.4 • | 3.7 ± 4.8 • | 0.421 |
| ODHA ( • ) | 4.3 ± 5.4 • | 0.2 ± 0.2 • | 0.1 ± 0.4 • | 0.1 ± 0.2 • | 0.1 ± 0.3 • | 0.3 ± 0.9 • | 0.764 |
| PI-LL ( • ) | 12.1 ± 7.5 • | 3.0 ± 4.5 • | 3.1 ± 4.9 • | 2.0 ± 2.7 • | 2.4 ± 4.8 • | 2.1 ± 3.2 • | 0.841 |
| SSA ( • ) | 120.1 ± 12.4 • | 3.3 ± 2.5 • | 3.2 ± 2.6 • | 4.0 ± 2.48 • | 3.1 ± 2.4 • | 3.9 ± 2.5 • | 0.623 |
| SVA (mm) | 22.1 ± 19.2 mm | 3.0 ± 2.9 mm 2.0 ± 2.5 mm 2.9 ± 2.5 mm 2.7 ± 1.1 mm 2.9 ± 1.5 mm | 0.812 |
|  | PI, pelvic incidence; PT, pelvic tilt; SS, sacral slope; LL, lumbar lordosis; L4S1, L4S1 lordosis; TK, thoracic kyphosis; |
|  | TPA, T1 pelvic angle; CBVA, chin-brow vertical angle; C2C7, C2C7 angle; TS, T1 slope; TS-CL, T1 slope-cervical |
|  | lordosis; ODHA, odontoid hip axis angle; PI-LL, pelvic incidence-lumbar lordosis; SSA, spino-sacral angle; SVA, |
|  | sagittal vertical axis. |  |  |  |  |  |

### Formule


$$L = αL dice + βL wl(1)$$

### Formule


$$𝑦 = 𝑓𝑔(𝑌) * 𝑌 𝑦 = 𝑓𝑔 𝑌 * 𝑌 ℒ = 1 -𝐷𝑆𝐶(𝑦, 𝑦 )(3)$$

### Formule


$$𝐷𝑆𝐶(𝑦, 𝑦 ) = ∑[(𝑦 + 𝑦 ) * (𝑦 * 𝑦 > 0)] ∑ 𝑦 + ∑ 𝑦(4)$$

### Formule


$$f g(x) = 0, x ≤ 2σ 1, x > 2σ bg(x) = 1, x ≤ 2σ 0, x > 2σ L wl = ∑ W * Y -Ŷ W = f g(Y)/ ∑ ( f g(Y))+bg(Y)/ ∑ (bg(Y)) (2)$$

### Formule


$$y = f g(Y) * Y ŷ = f g Ŷ * Ŷ L dice = 1 -DSC(y, ŷ)(3)$$

### Formule


$$DSC(y, ŷ) = ∑[(y + ŷ) * (y * ŷ > 0)] ∑ y + ∑ ŷ (4)$$

### Formule


$$C2C7 C2C7 Angle (Cervical Lordosis Angle)$$
