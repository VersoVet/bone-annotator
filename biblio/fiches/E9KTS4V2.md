# Deep Learning-Based Automated Anatomical Landmark Detection and Saw Blade Size Prediction for Canine Tibial Plateau Leveling Osteotomy.

**Auteurs** : Kim TH, Lee JY, Kim HY.
**Année** : 2026
**DOI** : 10.3390/ani16111599

## Résumé

<h4>Objective</h4>To develop and validate a fully automated deep learning workflow that localizes key anatomical landmarks on standard canine hindlimb lateral radiographs, derives the tibial plateau angle (TPA), and recommends a saw blade size for tibial plateau leveling osteotomy (TPLO) preoperative planning.<h4>Study design</h4>Retrospective validation study.<h4>Animals</h4>Two hundred annotated lateral radiographs obtained from 130 dogs representing 14 breeds, with body weights ranging from 2.4 to 38.0 kg.<h4>Methods</h4>A customized four-stage U-Net was trained using three complementary grayscale representations (normalized, contrast-enhanced, and gamma-adjusted images) to detect five TPLO-related landmarks. A deterministic geometric module then calculated TPA and mapped the derived osteotomy geometry to the nearest clinically available saw blade class.<h4>Results</h4>The mean absolute error for TPA prediction was 1.34 ± 1.73°, and the median absolute error was 0.75°. Overall, 164/

## Méthodologie

{'study_design': 'Retrospective single-center study combining a U-Net-based landmark detector with a deterministic geometric module (hybrid deep learning + geometry pipeline).', 'intervention': None, 'control': 'Surgeon (single expert) reference annotations/measurements used as the reference standard for comparison.', 'primary_outcomes': ['Tibial plateau angle (TPA) measurement accuracy (mean absolute error vs. surgeon reference)', 'Saw blade size prediction agreement'], 'secondary_outcomes': ['Landmark localization error for five anatomical landmarks', "ICC(2,1) and Lin's concordance correlation coefficient for TPA", 'Bland-Altman bias for TPA'], 'statistical_methods': ['Mean absolute error (MAE)', 'Intraclass correlation coefficient ICC(2,1)', "Lin's concordance correlation coefficient", 'Bland-Altman analysis'], 'duration': None, 'setting': 'Single institution, retrospective radiograph dataset (200 radiographs: 160 training, 40 validation)'}

## Résultats

{'quantitative': [{'outcome': 'Mean absolute error for TPA', 'value': '1.34', 'unit': 'degrees', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Discussion', 'source_quote': 'Across the full cohort, the mean absolute error for TPA was 1.34 degrees'}, {'outcome': 'TPA agreement within 2 degrees of surgeon reference', 'value': '164 of 200 cases (82.0%)', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': '164 of 200 cases (82.0%) were within 2 degrees of the surgeon reference'}, {'outcome': 'TPA agreement within 4.8 degrees of surgeon reference', 'value': '188 of 200 cases (94.0%)', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': '188 of 200 cases (94.0%) were within 4.8 degrees, a commonly cited range for interobserver measurement variability'}, {'outcome': 'Exact saw blade size agreement', 'value': '175 of 200 cases (87.5%)', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Discussion', 'source_quote': 'Exact saw blade size agreement was achieved in 175 of 200 cases (87.5%), and all predictions remained within one adjacent clinical size class.'}, {'outcome': 'ICC(2,1) for TPA', 'value': '0.865', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': "ICC(2,1) was 0.865, and Lin's concordance correlation coefficient was 0.864, indicating that the pipeline preserved both case ordering and absolute TPA values to a clinically useful extent"}, {'outcome': "Lin's concordance correlation coefficient for TPA", 'value': '0.864', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': "Lin's concordance correlation coefficient was 0.864"}, {'outcome': 'Bland-Altman mean bias for TPA', 'value': '-0.39', 'unit': 'degrees', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'Bland-Altman analysis [36] showed a small mean bias of -0.39°, suggesting that the model did not demonstrate a strong systematic tendency toward overestimation or underestimation at the cohort level.'}, {'outcome': 'TPA mean absolute error by breed size - small breeds', 'value': '1.28', 'unit': 'degrees', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'TPA mean absolute error was 1.28° for small breeds, 1.41° for medium breeds, and 1.05° for the two large-breed cases'}, {'outcome': 'TPA mean absolute error by breed size - medium breeds', 'value': '1.41', 'unit': 'degrees', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'TPA mean absolute error was 1.28° for small breeds, 1.41° for medium breeds, and 1.05° for the two large-breed cases'}, {'outcome': 'TPA mean absolute error by breed size - large breeds', 'value': '1.05', 'unit': 'degrees', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'TPA mean absolute error was 1.28° for small breeds, 1.41° for medium breeds, and 1.05° for the two large-breed cases'}, {'outcome': 'Saw blade exact match accuracy - small breeds', 'value': '89.9', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'Saw blade exact match accuracy was 89.9% for small breeds and 84.8% for medium breeds.'}, {'outcome': 'Saw blade exact match accuracy - medium breeds', 'value': '84.8', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'Saw blade exact match accuracy was 89.9% for small breeds and 84.8% for medium breeds.'}, {'outcome': 'Cases exceeding the 4.8° TPA threshold, by breed size', 'value': 'small-breed n=6, medium-breed n=6', 'unit': 'count', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'Cases exceeding the 4.8° TPA threshold were equally distributed between small-breed (n = 6) and medium-breed (n = 6) dogs and did not cluster within specific breeds.'}, {'outcome': 'Maximum localization error for axis-related landmarks a1 and a2', 'value': 'exceeding 100', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'infrequent failures at the axis-related landmarks a1 and a2 engendered heavy-tailed error distributions, with maximum errors exceeding 100 mm in both cases'}], 'qualitative_findings': ['Median localization error was low across all five landmarks, indicating most radiographs were handled accurately.', 'Disagreements in saw blade size prediction occurred bidirectionally, indicating no significant bias toward overestimation or underestimation.', 'Rare large failures in axis-related landmarks (a1, a2) were attributed to a known heatmap-based landmark detection failure mode where the network generates a secondary activation peak at an anatomically plausible but incorrect location.'], 'main_findings': ['A hybrid pipeline combining a U-Net-based landmark detector with deterministic geometric rules achieved clinically meaningful TPA measurement accuracy comparable to reported interobserver variability.', 'Saw blade size prediction achieved high exact agreement (87.5%) with all predictions remaining within one adjacent clinical size class.', 'Performance was broadly consistent between small- and medium-breed subgroups, though rare large failures in axis-related landmarks (a1, a2) disproportionately affected TPA accuracy in a minority of cases.']}

## Conclusions

The proposed deep learning pipeline for automated TPA measurement and saw blade size prediction showed clinically meaningful performance, with TPA errors within the commonly reported range of interobserver variability in most cases and saw blade size predictions remaining within one adjacent clinical class across all 200 radiographs. The hybrid framework (learned landmark detector + deterministic geometric module) automated a key subjective step in TPLO planning while preserving interpretability and traceability of the final measurements. Performance metrics were broadly consistent between small- and medium-breed subgroups across 14 breeds spanning a body weight range of 2.4 to 38.0 kg. Future work should include multicenter external validation, prospective reader studies, and strategies for automatically flagging low-confidence cases for surgeon review.

## Definition and role of the five anatomical landmarks used in this study.

| Landmark | Anatomical Location | Definition |
| --- | --- | --- |
| a1 | Distal tibial joint center | Defines the tibial functional axis (distal point) |
| a2 | Intercondylar eminence | Defines the tibial functional axis (proximal point); saw placement center |
| b1 | Cranial point of the tibial plateau | Defines the tibial plateau line |
| b2 | Caudal point of the tibial plateau | Defines the tibial plateau line |
| c1 | Tibial tuberosity reference point | Geometric reference point for saw size calculation |

## Landmark localization error across the full dataset (n = 200).

| Landmark | Description | Mean (mm) Median (mm) SD (Standard Deviation)/Max (mm) |
| --- | --- | --- | --- | --- |
| a1 | Distal tibial joint center | 1.69 | 0.51 | 10.72/107.99 |
| a2 | Intercondylar eminence | 1.56 | 0.41 | 10.70/107.72 |
| b1 | Cranial tibial plateau point | 0.97 | 0.65 | 1.76/18.86 |
| b2 | Caudal tibial plateau point | 0.86 | 0.72 | 0.82/10.05 |
| c1 | Tibial tuberosity reference point | 0.47 | 0.40 | 0.31/1.83 |

## Summary of TPA prediction performance.

| Metric | Value |
| --- | --- |
| Valid cases | 200 |
| Reference TPA, mean ± SD (degrees) | 32.08 ± 4.32 |
| Predicted TPA, mean ± SD (degrees) | 31.69 ± 4.08 |
| Mean absolute error (degrees) | 1.34 ± 1.73 |
| Median absolute error (degrees) | 0.75 |
| Within 2 degrees | 164 (82.0%) |

## Reference Size (mm) Total Cases Exact Match AI Larger AI Smaller

| 10 | 16 | 14 (87.5%) | 2 (12.5%) | 0 (0.0%) |
| --- | --- | --- | --- | --- |
| 12 | 88 | 79 (89.8%) | 2 (2.3%) | 7 (8.0%) |
| 15 | 60 | 54 (90.0%) | 1 (1.7%) | 5 (8.3%) |
| 18 | 26 | 19 (73.1%) | 2 (7.7%) | 5 (19.2%) |
| 20 | 8 | 7 (87.5%) | 0 (0.0%) | 1 (12.5%) |
| 27 | 2 | 2 (100.0%) | 0 (0.0%) | 0 (0.0%) |
