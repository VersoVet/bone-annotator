# Segmentation methods for quantifying X-ray Computed Tomography based biomarkers to assess hip fracture risk: a systematic literature review

**Auteurs** : Cristina Falcinelli, Vee San Cheong, Lotta M. Ellingsen, Benedikt Helgason
**Année** : 2024
**DOI** : 10.3389/fbioe.2024.1446829

## Résumé

BackgroundThe success of using bone mineral density and/or FRAX to predict femoral osteoporotic fracture risk is modest since they do not account for mechanical determinants that affect bone fracture risk. Computed Tomography (CT)-based geometric, densitometric, and finite element-derived biomarkers have been developed and used as parameters for assessing fracture risk. However, to quantify these biomarkers, segmentation of CT data is needed. Doing this manually or semi-automatically is labor-intensive, preventing the adoption of these biomarkers into clinical practice. In recent years, fully automated methods for segmenting CT data have started to emerge. Quantifying the accuracy, robustness, reproducibility, and repeatability of these segmentation tools is of major importance for research and the potential translation of CT-based biomarkers into clinical practice.MethodsA comprehensive literature search was performed in PubMed up to the end of July 2024. Only segmentation methods that were quantitatively validated on human femurs and/or pelvises and on both clinical and non-clinical CT were included. The accuracy, robustness, reproducibility, and repeatability of these segmentation methods were investigated, reporting quantitatively the metrics used to evaluate these aspects of segmentation. The studies included were evaluated for the risk of, and sources of bias, that may affect the results reported.FindingsA total of 54 studies fulfilled the inclusion criteria. The analysis of the included papers showed that automatic segmentation methods led to accurate results, however, there may exist a need to standardize reporting of accuracy across studies. Few works investigated robustness to allow for detailed conclusions on this aspect. Finally, it seems that the bone segmentation field has only addressed the concept of reproducibility and repeatability to a very limited extent, which entails that most of the studies are at high risk of bias.InterpretationBased on the studies analyzed, some recommendations for future studies are made for advancing the development of a standardized segmentation protocol. Moreover, standardized metrics are proposed to evaluate accuracy, robustness, reproducibility, and repeatability of segmentation methods, to ease comparison between different approaches.

## Méthodologie

{'study_design': "Recherche documentaire complète effectuée dans PubMed jusqu'à fin juillet 2024, avec évaluation quantitative de la précision, robustesse, reproductibilité et répétabilité des méthodes de segmentation, ainsi qu'une évaluation du risque de biais", 'intervention': None, 'control': None, 'primary_outcomes': ['Précision (accuracy) des méthodes de segmentation', 'Robustesse (robustness) des méthodes de segmentation', 'Reproductibilité (reproducibility) des méthodes de segmentation', 'Répétabilité (repeatability) des méthodes de segmentation'], 'secondary_outcomes': ['Risque de biais des études incluses'], 'statistical_methods': [], 'duration': "Recherche documentaire jusqu'à fin juillet 2024", 'setting': 'Revue de littérature basée sur PubMed'}

## Résultats

{'quantitative': [{'outcome': "Nombre d'études incluses", 'value': '54', 'unit': 'études', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Findings (Abstract)', 'source_quote': 'A total of 54 studies fulfilled the inclusion criteria.'}], 'qualitative_findings': ['Les méthodes de segmentation automatique ont conduit à des résultats précis', 'Il existe un besoin de standardiser le reporting de la précision entre les études', 'Peu de travaux ont étudié la robustesse pour permettre des conclusions détaillées', "Le domaine de la segmentation osseuse n'a abordé les concepts de reproductibilité et répétabilité que de manière très limitée", 'La plupart des études présentent un risque élevé de biais', 'Une seule étude sur la segmentation automatique a rapporté la robustesse en pourcentage de segmentations réussies, sans rapporter la robustesse à travers différents scanners', "Une étude ayant rapporté les différences inter-opérateurs a trouvé qu'elles étaient plus grandes pour la segmentation manuelle que pour un protocole de segmentation semi-automatique par graph cut (Pauchard et al., 2016)"], 'main_findings': ['Les outils de segmentation automatique développés à ce jour ont produit des résultats au moins aussi précis que les méthodes nécessitant une intervention manuelle', "Le développement d'outils de segmentation automatique a suffisamment mûri pour suggérer leur utilisation dans la quantification de biomarqueurs osseux basés sur l'image dans de larges cohortes cliniques", 'Seules quelques études ont systématiquement examiné la robustesse des méthodes de segmentation automatique', 'Des données limitées sont disponibles sur la reproductibilité et la répétabilité de ces méthodes']}

## Conclusions

Les outils de segmentation automatique sont au moins aussi précis que les méthodes semi-automatiques/manuelles et peuvent être utilisés pour quantifier des biomarqueurs osseux basés sur l'image dans de larges cohortes cliniques, car ils sont indépendants de l'opérateur et peu coûteux La robustesse, la reproductibilité et la répétabilité nécessitent une investigation plus approfondie dans les études futures Le développement de données CT en libre accès et de métriques standardisées pour quantifier la précision, la robustesse, la reproductibilité et la répétabilité est recommandé pour les futurs travaux L'accès aux données CT pourrait être fourni à condition que les méthodes développées ou validées sur ces données soient publiées en open source

## Continued) Literature overview of CT-derived densitometric (plain text) and geometric biomarkers (italic) used to classify osteoporotic hip fractures.

|  | cross- | Pre fracture | M; N=3347, Fx=42 vBMD-I; vBMD-C; vBMD-T; % | AUC=0.855 combining CT parameters |
| --- | --- | --- | --- | --- | --- |
|  | sectional MrOS | imaging |  | CV; minimum CSA in FN | AUC=0.853 for aBMD from DXA |
| Ito et al. (2010) | Two age-matched case- | Post fracture | F; N=40, Fx=20 | Hip axis length; CSMI; BR; | Study 1: OR=2.15 pvalue=0.07 for hip axis |
|  | control studies | imaging | F; N=32, Fx=16 | NSA; CSA | length |
|  |  |  |  |  | OR=1.52 pvalue=0.06 for CSMI |
|  |  |  |  |  | OR=2.56 pvalue=0.01 for BR |
|  |  |  |  |  | Study 2: OR=2.15 pvalue=0.11 for NSA |
|  |  |  |  |  | OR=1.47 pvalue=0.01 for cortical CSA |
| Johannesdottir et al. | Case-control study nested | Pre fracture | F; N=275, Fx=88 | Cth at the mid-FN in anatomical | F: HR=1.8 for SA Cth (any hip fracture) |
| (2011) ,a | within the prospective | imaging | M; N=166, Fx=55 | quadrants; vBMD | HR=1.8 for SA Cth (FN fracture) |
|  | study AGES |  |  |  | HR=2.1 for SA Cth (trochanteric fracture) |
|  |  |  |  |  | HR=1.9 for vBMD (any hip fracture) |
|  |  |  |  |  | HR=1.8 for vBMD (FN fracture) |
|  |  |  |  |  | HR=2.4 for vBMD (trochanteric fracture) |
|  |  |  |  |  | HR=1.8 for aBMD (any hip fracture) |
|  |  |  |  |  | HR=1.7 for aBMD (FN fracture) |
|  |  |  |  |  | HR=2.1 for aBMD (trochanteric fracture) |
|  |  |  |  |  | M: HR=3.6 for SA Cth (any hip fracture) |
|  |  |  |  |  | HR=3.5 for SA Cth (FN fracture) |
|  |  |  |  |  | HR=4.3 for SA Cth (trochanteric fracture) |
|  |  |  |  |  | HR=2.9 for vBMD (any hip fracture) |
|  |  |  |  |  | HR=2.9 for vBMD (FN fracture) |
|  |  |  |  |  | HR=3.2 for vBMD (trochanteric fracture) |
|  |  |  |  |  | HR=3.1 for aBMD (any hip fracture) |
|  |  |  |  |  | HR=2.7 for aBMD (FN fracture) |
|  |  |  |  |  | HR=4.4 for aBMD (trochanteric fracture) |
| Bousson et al. | Prospective | Post fracture | F; N=107, Fx=47 | vBMD-I FH; vBMD-T TR; | AUC=0.821 for vBMD-I FH + |
| (2011) | EFFECT | imaging |  | CortShaftThick; CortNeckThick | CortShaftThick |
|  |  |  |  |  | AUC=0.819 for vBMD-I FH + |
|  |  |  |  |  | CortNeckThick |
|  |  |  |  |  | AUC=0.803 for vBMD-T TR + |
|  |  |  |  |  | (Continued on following page) |
| Frontiers in Bioengineering and Biotechnology |  | 03 |  | frontiersin.org |

## Continued) Literature overview of CT-derived densitometric (plain text) and geometric biomarkers (italic) used to classify osteoporotic hip fractures.

| Reference | Study | Type of | Gender | CT-based biomarker | Performance |
| --- | --- | --- | --- | --- | --- |
|  |  | imaging | (F or M) |  |  |
|  |  |  | Subjects (N) |  |  |
|  |  |  | Cases (Fx) |  |  |
|  |  |  |  |  | AUC=0.88 for TR vBMD-T + FN CTh All + |
|  |  |  |  |  | SL vBMD-T SA + SL CortArea SP |
|  |  |  |  |  | AUC=0.88 for TR vBMD-T + FN CTh All + |
|  |  |  |  |  | SL vBMD-T SA + SL CortArea SP + SL BR |
|  |  |  |  |  | Comparison with aBMD NR |
| Khoo et al. (2020) ,a | Case-control study | Post fracture | F; N=546, Fx=285 | FN Delta, FN Sigma | AUC=0.87 for age, weight, height, FN |
|  |  | imaging |  |  | aBMD, FN Delta, and FN Sigma |
|  |  |  |  |  | AUC=0.84 for age, weight, height, and FN |
|  |  |  |  |  | aBMD |
| Wang et al. (2022) | Cross-sectional case- | Post fracture | F; N=562, Fx=236 | TH CTh; IT CTh; FH V; | All models were adjusted for age, height and |
|  | control study | imaging |  | THRCTM; FN CSA | weight: |
|  |  |  |  |  | AUC=0.805 for TH CTh + FH Vol + |
|  |  |  |  |  | THRCTM + FN CSA |
|  |  |  |  |  | AUC=0.728 for THCortThick + FH Vol+FN |
|  |  |  |  |  | CSA |
|  |  |  |  |  | AUC=0.735 for IT CTh + FH Vol + FN CSA |
|  |  |  |  |  | AUC=0.735 for IT CTh + FH Vol |
|  |  |  |  |  | AUC= 0.703 for IT CTh + FN CSA |
| a DXA was not used in this study, CT was also used to measure a DXA-equivalent hip aBMD |  |  |

## CT-based FE model-derived biomarkers used to classify hip fractures

| Reference | Study | Type of | Gender | Types of CT-based | Performance |
| --- | --- | --- | --- | --- | --- |
|  |  | imaging | (F or M) | biomarkers |  |
|  |  |  | Subjects (N) |  |  |
|  |  |  | Fractured |  |  |
|  |  |  | cases (Fx) |  |  |
| Orwoll et al. (2009) | Prospective MrOS | Pre fracture | M; N=250 | FE-strength, load-to-strength ratio | AUC=0.83 for FE strength |
|  |  | imaging | Fx=40 |  | AUC=0.79 for load-to-strength ratio |
|  |  |  |  |  | AUC=0.85 for aBMD |
|  |  |  |  |  | AUC=0.87 for FE strength +age + |
|  |  |  |  |  | BMI + clinical center |
|  |  |  |  |  | AUC=0.88 for load-to-strength ratio |
|  |  |  |  |  | + age + BMI+ clinical center |
|  |  |  |  |  | AUC=0.88 for aBMD +age + BMI |
|  |  |  |  |  | + clinical center |
| Amin et al. (2011) | Case-control study | Pre fracture | F; N=314, Fx=55 | FE-strength, load-to-strength ratio | F: AUC=0.84 for FE strength |
|  |  | imaging | M; N=266, Fx=28 |  | AUC=0.84 for load-to-strength ratio |
|  |  |  |  |  | AUC=0.85 for TH vBMD |
|  |  |  |  |  | AUC=0.84 for TH aBMD |
|  |  |  |  |  | M: AUC=0.78 for FE strength |
|  |  |  |  |  | AUC=0.77 for load-to-strength ratio |
|  |  |  |  |  | AUC=0.78 for TH vBMD |
|  |  |  |  |  | AUC=0.78 for TH aBMD |
| Kopperdahl et al. | Prospective | Pre fracture | F; N=608, Fx=108 | FE strength, load-to-strength ratio AUC=0.78 for FE strength (female) |
| (2014) ,a | AGES | imaging | M; N=440, Fx=63 |  | AUC=0.84 for FE strength (male) |
|  |  |  |  |  | AUC=0.80 for FE strength+age |
|  |  |  |  |  | (female) |
|  |  |  |  |  | AUC=0.86 for FE strength+age (male) |
| Nishiyama et al. | Case-control study | Post fracture | F; N=70, Fx=35 | FE strength, vBMD | Pooled fractures: AUC=0.87 for |
| (2014) |  | imaging |  |  | vBMD |
|  |  |  |  |  | AUC=0.89 for FE strength |
|  |  |  |  |  | AUC=0.94 for vBMD+FE strength |
|  |  |  |  |  | Neck Fractures: AUC=0.86 for |
|  |  |  |  |  | vBMD |
|  |  |  |  |  | AUC=0.94 for FE strength |
|  |  |  |  |  | AUC=0.94 for vBMD+FE strength |
|  |  |  |  |  | Trochanteric fractures: |
|  |  |  |  |  | AUC=0.83 for vBMD |
|  |  |  |  |  | AUC=0.79 for FE strength |
|  |  |  |  |  | AUC=0.86 for vBMD+FE strength |
| Falcinelli et al. | Case-control study | Post fracture | F; N=55, Fx=22 | FE strength | AUC=0.87 for FE strength in stance |
| (2014) |  | imaging |  |  | AUC=0.88 for FE strength in fall |
|  |  |  |  |  | AUC=0.73 for FN aBMD |
|  |  |  |  |  | AUC=0.79 for TH aBMD |
|  |  |  |  |  | AUC=0.75 for trochanteric aBMD |
| Qasim et al. (2016) | Retrospective study | Post fracture | F; N=100, Fx=50 | FE strength | AUC=0.75 for FE strength in stance |
|  |  | imaging |  |  | AUC=0.79 for FE strength in fall |
|  |  |  |  |  | AUC=0.75 for FN aBMD |
|  |  |  |  |  | AUC=0.74 for TH aBMD |
|  |  |  |  |  | AUC=0.79 for FE strength in stance |
|  |  |  |  |  | + aBMD |
|  |  |  |  |  | AUC=0.80 for FE strength in fall + |
|  |  |  |  |  | aBMD |
| Adams et al. (2018) | Retrospective case-cohort | Pre fracture | F; N=850 | FE strength | F: AUC=0.73 for FE strength |
|  | study preexisting | imaging | M; N=465 |  | AUC=0.72 for vBMD |
|  | FOCUS |  |  |  | AUC=0.72 for aBMD |
|  |  |  |  |  | M: AUC=0.75 for FE strength |
|  |  |  |  |  | AUC=0.71 for vBMD |
|  |  |  |  |  | AUC=0.73 for aBMD |
| Bhattacharya et al. | Retrospective study | Post fracture | F; N=98, Fx=49 | ARF0, | AUC=0.85 for ARF0 |
| (2019) |  | imaging |  | FE strength | AUC=0.82 for FE strength |
|  |  |  |  |  | AUC=0.75 for aBMD |
|  |  |  |  |  | (Continued on following page) |
| Frontiers in Bioengineering and Biotechnology |  |  |  | frontiersin.org |

## Continued) CT-based FE model-derived biomarkers used to classify hip fractures DXA was not used in this study, CT was also used to measure a DXA-equivalent hip aBMD b

| Reference | Study | Type of | Gender | Types of CT-based | Performance |
| --- | --- | --- | --- | --- | --- |
|  |  | imaging | (F or M) | biomarkers |  |
|  |  |  | Subjects (N) |  |  |
|  |  |  | Fractured |  |  |
|  |  |  | cases (Fx) |  |  |
| Enns-Bray et al. | Prospective | Pre fracture | F; N=254, Fx=95 | FE strain+fall probability | AUC=0.73 for FE strain+fall |
| (2019) ,a | AGES | imaging |  |  | AUC=0.70 for aBMD |
| Michalski et al. | Prospective study | Pre fracture | F; N=187, Fx=66 | TH vBMD-I, | Pooled: AUC=0.661 for TH vBMD-I |
| (2021) |  | imaging | M; N=303, Fx=57 | FE strength | AUC=0.675 for FE strength |
|  |  |  |  |  | AUC=0.675 for FE strength+TH |
|  |  |  |  |  | vBMD-I |
|  |  |  |  |  | F: AUC=0.664 for TH vBMD-I |
|  |  |  |  |  | AUC=0.679 for FE strength |
|  |  |  |  |  | AUC=0.693 for FE strength+TH |
|  |  |  |  |  | vBMD-I |
|  |  |  |  |  | M: AUC=0.65 for TH vBMD-I |
|  |  |  |  |  | AUC=0.618 for FE strength |
|  |  |  |  |  | AUC=0.644 for FE strength+TH |
|  |  |  |  |  | vBMD-I |
|  |  |  |  |  | Performance of DXA-based |
|  |  |  |  |  | aBMD NR |
| Fleps et al. (2022) ,a | Prospective | Pre fracture | F; N=362, Fx=142 | FE strength | F: AUC=0.74 for FE strength |
|  | AGES | imaging | M; N=239, Fx=59 |  | AUC=0.69 for aBMD |
|  |  |  |  |  | M: AUC=0.78 for FE strength |
|  |  |  |  |  | AUC=0.72 for aBMD |
| Cao et al. (2022) ,a | Prospective | Pre fracture | F; N=211, Fx=68 | FE ultimate strength, FE yield | Whole: AUC= 0.699 for aBMD + |
|  | AGES | imaging | M; N=134, Fx=42 | strength, FE energy to failure, PC1 | covariates b |
|  |  |  |  |  | AUC=0.738 for PC1 + aBMD + |
|  |  |  |  |  | covariates b |
|  |  |  |  |  | AUC= 0.724 for FE parameters |
|  |  |  |  |  | combined, aBMD + covariates b |
|  |  |  |  |  | AUC=0.754 for PC1 + aBMD |
|  |  |  |  |  | +covariates b |
|  |  |  |  |  | AUC=0.651 for FRAX |
|  |  |  |  |  | F: AUC= 0.608 for aBMD + |
|  |  |  |  |  | covariates b |
|  |  |  |  |  | AUC=0.623 for PC1 + aBMD + |
|  |  |  |  |  | covariates b |
|  |  |  |  |  | AUC= 0.669 for FE parameters |
|  |  |  |  |  | combined, aBMD + covariates b |
|  |  |  |  |  | AUC=0.71 for PC1 + aBMD |
|  |  |  |  |  | +covariates b |
|  |  |  |  |  | AUC=0.623 for FRAX |
|  |  |  |  |  | M: AUC= 0.727 for aBMD + |
|  |  |  |  |  | covariates b |
|  |  |  |  |  | AUC=0.745 for PC1 + aBMD + |
|  |  |  |  |  | covariates b |
|  |  |  |  |  | AUC= 0.724 for FE parameters |
|  |  |  |  |  | combined, aBMD + covariates b |
|  |  |  |  |  | AUC=0.825 for PC1 + aBMD |
|  |  |  |  |  | +covariates b |
|  |  |  |  |  | AUC=0.705 for FRAX |

## Segmentation methods developed for the pelvis from the studies included in the review. The table shows the following information: reference of study; number of datasets N and type of material segmented; type of CT scanner, scanning parameters, and image resolution; segmentation method; metrics used to evaluate accuracy, robustness, reproducibility and repeatability; and remarks. NR: not reported

|  | N datasets | CT-scanner, scanning | Metrics used for | Remarks |
| --- | --- | --- | --- | --- |
| Study | segmented, type of | parameters and | accuracy, robustness, |  |
|  | material | resolution | reproducibility and |  |
|  |  |  | repeatability |  |
| Threshold-based |  |  |  |  |
| Zoroofi et al. | 60 in-vivo CT datasets (120 hip | Device and scanning parameters NR | Accuracy: ASD (mm), average DSC | Automatic method |
| (2003) | joints) | 0.68x0.68x3 mm 3 0 segmentation | (%) | Manual segmentation as the ground |
|  | Among the 120 hip joints, THR | algorithm performs a resampling to | Robustness: NR | truth |
|  | had been performed on nine | 0.68x0.68x0.75 mm 3 | Reproducibility: NR | The developed method is not |
|  | cases. Hence 111 hip joints were |  | Repeatability: NR | publicly available |
|  | used for further evaluations |  |  | Average time: 7 min per hip; 9.5 s per |
|  | Hip joints classified in 4 groups: |  |  | slice |
|  | 1) acetabulum and the femoral |  |  |  |
|  | head are well separated from each |  |  |  |
|  | other; 2) acetabulum and femoral |  |  |  |
|  | head are close to each other; 3) |  |  |  |
|  | acetabulum and femoral head are |  |  |  |
|  | close to each other but the shape |  |  |  |
|  | of the femoral head is different |  |  |  |
|  | from that of a perfect ellipse, due |  |  |  |
|  | to pathology and malformation of |  |  |  |
|  | the pelvis and the femur; 4) |  |  |  |
|  | acetabulum and femoral head are |  |  |  |
|  | attached due to the severity of a |  |  |  |
|  | bone disease |  |  |  |
| Anstey et al. | A formaldehyde-fixed cadaveric | 16-slice CT scanner (Lightspeed+ | Accuracy: RMSE (mm), Average |  |
| (2011) | hemi-pelvis with all soft tissues | XCR, General Electric, Milwaukee, | Deviation (unsigned, mm), Average |  |
|  | intact | USA) | Deviation (signed, mm), Max |  |
|  |  | Slice thickness of 0.625 mm | Deviation (unsigned, mm) |  |
|  |  |  | Robustness: NR |  |
|  |  |  | Reproducibility: NR |  |
|  |  |  | Repeatability: NR |  |

## Continued) Segmentation methods developed for the pelvis from the studies included in the review. The table shows the following information: reference of study; number of datasets N and type of material segmented; type of CT scanner, scanning parameters, and image resolution; segmentation method; metrics used to evaluate accuracy, robustness, reproducibility and repeatability; and remarks. NR: not reported

|  | N datasets | CT-scanner, scanning | Metrics used for |
| --- | --- | --- | --- |
| Study | segmented, type of | parameters and | accuracy, robustness, |
|  | material | resolution | reproducibility and |
|  |  |  | repeatability |

## Continued) Segmentation methods developed for the pelvis from the studies included in the review. The table shows the following information: reference of study; number of datasets N and type of material segmented; type of CT scanner, scanning parameters, and image resolution; segmentation method; metrics used to evaluate accuracy, robustness, reproducibility and repeatability; and remarks. NR: not reported

|  | N datasets | CT-scanner, scanning | Metrics used for | Remarks |
| --- | --- | --- | --- | --- |
| Study | segmented, type of | parameters and | accuracy, robustness, |  |
|  | material | resolution | reproducibility and |  |
|  |  |  | repeatability |  |
|  |  | 0.744 mm while the inter-slice | Reproducibility: NR | performance of their approach. The |
|  |  | resolutions were 1.6 mm for all CT | Repeatability: NR | 30 CT data was randomly partitioned |
|  |  | data |  | into 15 equal size subsets. Of the |
|  |  |  |  | 15 subsets, each time a single subset |
|  |  |  |  | (2 CT data) was used as the test data |
|  |  |  |  | while the remaining 14 subsets were |
|  |  |  |  | used as training data. This process |
|  |  |  |  | was repeated 15 folds, with each one |
|  |  |  |  | of the 15 subsets used exactly once as |
|  |  |  |  | the test data. |
|  |  |  |  | Manual segmentation as the ground |
|  |  |  |  | truth |
|  |  |  |  | The developed method is not |
|  |  |  |  | publicly available |
|  |  |  |  | Computation time: 3.1 min for |
|  |  |  |  | segmentation of a hip joint |
| Chu et al. (2015b) | 30 in-vivo hip CT datasets | Device and scanning parameters NR | Accuracy: ASD (mm), DSC (%) | Automatic method |
|  |  | Intra-slice resolutions ranged from | Robustness: NR | FACTS (Fully Automatic CT |
|  |  | 0.576 mm to 0.744 mm while the | Reproducibility: NR | Segmentation): combining fast |
|  |  | inter-slice resolutions were | Repeatability: NR | random forest (RF) regression based |
|  |  | characterized by a constant value of |  | landmark detection, multi-atlas- |
|  |  | 1.6 mm |  | based segmentation, with articulated |
|  |  |  |  | statistical shape model (aSSM) based |
|  |  |  |  | fitting |
|  |  |  |  | Same data of (Chu et al., 2015a) but |
|  |  |  |  | different method. The method |
|  |  |  |  | proposed in this work requires |
|  |  |  |  | greater computation time and is less |
|  |  |  |  | accurate with respect to (Chu et al., |
|  |  |  |  | 2015a) |
|  |  |  |  | Manual segmentation as the ground |
|  |  |  |  | truth |
|  |  |  |  | The developed method is not |
|  |  |  |  | publicly available |
|  |  |  |  | Computation time: 7.9 min per hip |
| Hanaoka et al. | 50 in-vivo whole-torso CT | Device and scanning parameters NR | Accuracy: DSC (%), HD (mm), ADE | Automatic method |
| (2017) | datasets. All subjects had no bone | Voxel size: 0.977×0.977×1.250 mm | (mm) | Manual segmentation as the ground |
|  | diseases other than osteopenia. |  | Robustness: NR | truth |
|  |  |  | Reproducibility: NR | The developed method is not |
|  |  |  | Repeatability: NR | publicly available |
|  |  |  |  | Computation time: 15 min for one |
|  |  |  |  | segmentation task using 5 atlases, |
|  |  |  |  | 110 min when 39 atlases were used |
| Convolutional neural network |  |  |  |
| Wang et al. | 90 in-vivo abdominal CT from | For 50 datasets from CT | Accuracy: DSC | Automatic method |
| (2019) | two studies (50 from the CT | colonography: at least a 16 slice CT | Robustness: NR | Manual segmentation as the ground |
|  | colonography study, 40 from the | scanner, 0.5-1.0 mm collimation, | Reproducibility: NR | truth |
|  | lymph node study) | pitch of 0.98-1.5, matrix 512×512, | Repeatability: NR | The developed method is not |
|  |  | field-of-view to fit, 50 effective mAs, |  | publicly available |
|  |  | 120 kVp, standard reconstruction |  | For testing, the U-net prediction |
|  |  | algorithm, slice thicknesses of |  | takes 20-30 seconds to process a 3D |
|  |  | 1-1.25 mm with a 0.8 mm |  | volume, and the shape model |
|  |  | reconstruction interval. |  | estimation takes 2-3 minutes for each |
|  |  | NR for lymph node study |  | pass |
| Noguchi et al. | 32 in-vivo CT datasets i.e. | For the 32 CT datasets: Aquilion 64, | Accuracy: DSC, JAC | Automatic method |
| (2020) | 16 patients (for training and | Aquilion | Robustness: it has been proved by | To compare the proposed model |
|  | validation). Among the | ONE, Aquilion PRIME; Canon | considering three different datasets | with those of previous studies, the |
|  | 16 patients, 9 patients had known | Medical Systems, Otawara, Japan; | and testing three types of data | network was trained and validated |
|  | sites of bone metastases. | slice thickness was 0.5, 1.0, or 5.0 mm, | augmentation techniques | on a publicly available labelled |
|  | 20 in-vivo CT datasets (for testing | and axial in-plane image resolution | (conventional method, Mixup and | dataset (27 CT datasets). Of the |
|  | robustness on other data sources) | was 0.41-0.68 mm | RICAP) (DSC, JAC) | 27 examinations, 15 were used for |
|  |  | For the 20 CT datasets: Device and |  | training, 3 for validation, and 9 for |
|  |  |  |  | (Continued on following page) |
| Frontiers in Bioengineering and Biotechnology |  |  | frontiersin.org |

## Continued) Segmentation methods developed for the pelvis from the studies included in the review. The table shows the following information: reference of study; number of datasets N and type of material segmented; type of CT scanner, scanning parameters, and image resolution; segmentation method; metrics used to evaluate accuracy, robustness, reproducibility and repeatability; and remarks. NR: not reported

|  | N datasets | CT-scanner, scanning | Metrics used for | Remarks |
| --- | --- | --- | --- | --- |
| Study | segmented, type of | parameters and | accuracy, robustness, |  |
|  | material | resolution | reproducibility and |  |
|  |  |  | repeatability |  |
|  | 27 in-vivo CT public datasets | scanning parameters NR; slice | Reproducibility: NR | testing. |
|  | (20 patients) | thickness was 1 or 1.25 mm, and axial | Repeatability: NR | Manual segmentation as the ground |
|  |  | in-plane image resolution was |  | truth |
|  |  | 0.63-0.97 mm |  | The developed method is not |
|  |  | For the 27 CT public datasets: helical |  | publicly available |
|  |  | CT scanner (Philips, Amsterdam, |  | The training time was ~2 h per fold |
|  |  | The Netherlands); slice thickness of |  | for the 32 CT datasets. |
|  |  | 5 mm and axial in-plane image |  | Training time was approximately |
|  |  | resolution of 0.78 mm |  | 40 min per split for the 27 CT public |
|  |  |  |  | datasets |
| González | 30 in-vivo dual energy CT | Siemens SOMATOM, low energy | Accuracy: DSC | Automatic method |
| Sánchez et al. |  | (mostly 80 kV), high energy (mostly | Robustness: NR | Manual segmentation as the ground |
| (2020) |  | 150 kV), mixed images (around | Reproducibility: NR | truth |
|  |  | 120 kV) | Repeatability: NR | The developed method is publicly |
|  |  | Isotropic voxel size ranged |  | available |
|  |  | 0.67x0.67x1 mm 3 to |  | Computation time: 5 s |
|  |  | 0.977x0.977x1.0 mm 3 |  |  |
| Hiasa et al. (2020) | 20 in-vivo CT volumes scanned | Device and scanning parameters NR | Accuracy: DSC (%), AD (mm) | Automatic method |
|  | (Osaka University Hospital THA | Field of view 360 × 360 mm 2 , matrix | Robustness: NR | The Osaka University Hospital THA |
|  | dataset) | size 512 × 512 | Reproducibility: NR | dataset was used for training and |
|  |  | Slice intervals: 2.0 mm for the region | Repeatability: NR | cross-validation for the accuracy |
|  |  | including the pelvis and proximal |  | evaluation and prediction of the DSC |
|  |  | femur, 6.0 mm for the femoral shaft |  | coefficient |
|  |  | region, and 1.0 mm for the distal |  | Manual segmentation as the ground |
|  |  | femur region |  | truth |
|  |  |  |  | The developed method is not |
|  |  |  |  | publicly available |
|  |  |  |  | Average training time: 11 hours |
|  |  |  |  | Average computation time for the |
|  |  |  |  | inference on one CT volume with |
|  |  |  |  | about 500 2D slices was |
|  |  |  |  | approximately 2 minutes excluding |
|  |  |  |  | file loading, and the post-processing |
|  |  |  |  | took about 3 minutes |
| Jeuthe et al. | 8 in-vivo CT datasets for | 8 datasets at 120 kV, different | Accuracy: DSC | Automatic method |
| (2021) | development and 30 in-vivo CT | scanners, voxel size ranged from | Robustness: NR | MK2014v2, JS2016 and |
|  | datasets for testing | 0.7x0.7x1.0 mm 3 to 0.9x0.9x3.0 mm 3 | Reproducibility: NR | JS2018 algorithms |
|  |  | 30 datasets from Siemens | Repeatability: NR | Manual segmentation as the ground |
|  |  | SOMATOM Force scanner, 80 kV, |  | truth |
|  |  | 150 kV, voxel size ranged from |  | The developed method is not |
|  |  | 0.63x0.63x1.0 mm 3 to |  | publicly available |
|  |  | 0.98x0.98x1.0 mm 3 |  |  |
| Liu et al. (2021) | 1184 in-vivo 3D volumes (entire | Device and scanning parameters NR | Accuracy: DSC, HD (mm) | Automatic method |
|  | dataset) from 7 CT sub-datasets | Mean spacing entire CT dataset: | Robustness: Six deep networks have | Manual segmentation as the ground |
|  | (ABDOMEN 35, COLONOG | 0.78x0.78x1.46 (mm) | been trained, one network per single | truth |
|  | 731, MSD_T10 155, KITS19 44, |  | sub-dataset and tested on each sub- | The developed method is publicly |
|  | CERVIX 41, CLLINIC 103, |  | dataset: DSC, HD (mm) | available |
|  | CLINIC-metal 75) |  | Reproducibility: NR |  |
|  |  |  | Repeatability: NR |  |
| Xu et al. (2022) | 35 in-vivo CT scans from the | Device and scanning parameters NR | Accuracy: DSC (%), GapDSC (%), | Automatic method |
|  | Cancer Imaging Archive | (0.78±0.11) × (0.77±0.1) × | HD (#voxels) | Use of 2D image slices from different |
|  |  | (0.96±0.17) mm 3 | Robustness: NR | views helped to produce accurate |
|  |  |  | Reproducibility: NR | multi-segmentation despite the small |
|  |  |  | Repeatability: NR | dataset. |
|  |  |  |  | Post-processing step corrects for |
|  |  |  |  | misclassification near midline (e.g. left |
|  |  |  |  | or right pubis) |
|  |  |  |  | Pretraining (inferior segmentation) =2 |
|  |  |  |  | Fine tuning (uses accurate |
|  |  |  |  | segmentation) =2 |
|  |  |  |  | Initial predict then manual correct, |
|  |  |  |  | then repeat fine tuning process=2 |
|  |  |  |  | (Continued on following page) |
| Frontiers in Bioengineering and Biotechnology |  |  | frontiersin.org |

## Continued) Segmentation methods developed for the pelvis from the studies included in the review. The table shows the following information: reference of study; number of datasets N and type of material segmented; type of CT scanner, scanning parameters, and image resolution; segmentation method; metrics used to evaluate accuracy, robustness, reproducibility and repeatability; and remarks. NR: not reported

|  | N datasets | CT-scanner, scanning | Metrics used for | Remarks |
| --- | --- | --- | --- | --- |
| Study | segmented, type of | parameters and | accuracy, robustness, |  |
|  | material | resolution | reproducibility and |  |
|  |  |  | repeatability |  |
|  |  |  |  | Evaluation cases=21 |
|  |  |  |  | Manual segmentation as the ground |
|  |  |  |  | truth |
|  |  |  |  | The developed method is not publicly |
|  |  |  |  | available |
| Wu et al. (2022) | 815 in-vivo CT datasets from | Scanning parameter NR | Accuracy: DSC, HD (mm) | Automatic method |
|  | 5 sub-datasets: normal hip | Phillip CT Brilliance ICT with 1.00- | Robustness: evaluated using diseased | Manual segmentation as the ground |
|  | dataset, osteoarthritis (OA) hip- | mm slice thickness and | hip datasets (DSC, HD (mm)) | truth |
|  | joint dataset, dysplasic hip | 512×512 image resolution | Reproducibility: NR | Computation time: 23.7±1.0 s on a |
|  | (DDH) dataset, femoral neck |  | Repeatability: NR | Nvidia GeForce GTX TITAN X GPU |
|  | fracture (FNF) hip joint dataset, |  |  | The developed method is not |
|  | osteonecrosis of femoral head |  |  | publicly available |
|  | (ONFH) hip joint dataset |  |  |  |
| Zhai et al. (2023) | 81 in-vivo CT images | 31 CT scans acquired with the Somatom | Accuracy: DSC, HD95 (mm) | Automatic method |
|  | (31 preoperative images of | Definition Flash scanner (Siemens | Robustness: NR | Manual segmentation as the ground |
|  | diseased hips, and 50 healthy hip | Medical Solutions, Erlangen, Germany), | Reproducibility: NR | truth |
|  | images). Hip disorders of the | 120 kVp, 336 mA, 1 mm slice thickness, | Repeatability: NR | Computation time: 10 s |
|  | 31 cases included osteonecrosis of | 512 × 512 matrix size, 0.62-0.98 mm |  | The developed method is not |
|  | femoral head, osteoarthritis, | pixel spacing |  | publicly available |
|  | developmental dysplasia of the | 50 CT scans acquired with multidetector |  |  |
|  | hip, femoral neck fracture, and | row CT scanners, 120 kVp, 1-1.25 mm |  |  |
|  | bone tumors. | slice thickness, 512 × 512 matrix size, |  |  |
|  |  | 0.60-0.98 mm pixel spacing |  |  |
| Other methods |  |  |  |  |
| Guo et al. (2018) | 50 in-vivo hip CT datasets | Hip joints were acquired on a Philips | Accuracy: evaluated on 10 hip joints | Automatic method |
|  |  | Brilliance 64 CT scanner | for the three different segmentation | Bone segmentation framework based |
|  |  | 0.68x0.68x0.67 mm 3 | methods (ASD (mm), DSC (%), TPR | on a consideration of the surface |
|  |  |  | (%)) | normal direction |
|  |  |  | Robustness: NR | A comparison with two recently |
|  |  |  | Reproducibility: NR | published methods (Yokota's and |
|  |  |  | Repeatability: NR | Chandra's methods) |

## Segmentation methods developed for the pelvis from the studies included in the review. The table shows the quantitative results obtained from each study for evaluating accuracy, robustness, reproducibility and repeatability. NR: not reported.

|  | Accuracy | Robustness | Reproducibility Repeatability |
| --- | --- | --- | --- | --- |
| Study |  |  |  |  |
| Threshold-based |  |  |  |  |
| Zoroofi et al. (2003) | ASD 0.91 mm, average DSC (%) 93.89 | NR | NR | NR |
| Anstey et al. (2011) RMSE (mm): cadaver to segmentation 0.61, model | NR | NR | NR |
|  | to segmentation 0.49, cadaver to model 0.48. |  |  |  |
|  | Average Deviation (unsigned, mm): cadaver to |  |  |  |
|  | segmentation 0.58, model to segmentation 0.47, |  |  |  |
|  | cadaver to model 0.42 |  |  |  |
|  | Average Deviation (signed, mm): cadaver to |  |  |  |
|  | segmentation -0.49, model to segmentation -0.46, |  |  |  |
|  | cadaver to model -0.32 |  |  |  |
|  | Max Deviation (unsigned, mm): cadaver to |  |  |  |
|  | segmentation 1.62, model to segmentation 0.94, |  |  |  |
|  | cadaver to model 1.58 mm |  |  |  |
| Zhou et al. (2013) | JAC: 79.8% (range 74.4-83.0%) by global |  |  |  |
|  | threshold method, 85.6% (range 81.2-89.2%) by |  |  |  |
|  | FCM method, 89.1% (range 86.0-91.6%) by |  |  |  |
|  | Straka's method |  |  |  |

## Continued) Segmentation methods developed for the pelvis from the studies included in the review. The table shows the quantitative results obtained from each study for evaluating accuracy, robustness, reproducibility and repeatability. NR: not reported.

| , 0.98 proposed method |
| --- |

## Continued) Segmentation methods developed for the pelvis from the studies included in the review. The table shows the quantitative results obtained from each study for evaluating accuracy, robustness, reproducibility and repeatability. NR: not reported.

|  | Accuracy | Robustness | Reproducibility Repeatability |
| --- | --- | --- | --- | --- |
| Study |  |  |  |  |
| Liu et al. (2021) | 3D U-Net cascade with the deep network model | Six deep networks have been trained, one network | NR | NR |
|  | trained on entire dataset: | per single sub-dataset and tested on each sub- |  |  |
|  | -left hip DSC=0.989 and HD=4.24 mm | dataset: |  |  |
|  | -right hip DSC=0.991 and HD=3.03 mm | -best average DSC=0.989 |  |  |
|  |  | -best average HD=1.93 mm |  |  |
| Xu et al. (2022) | DSC=98.63±0.56 | NR | NR | NR |
|  | GapDSC=96.47±1.60 |  |  |  |
|  | HD (#voxels) =3.67±1.13 |  |  |  |
| Wu et al. (2022) | Normal hip dataset: | Diseased hip datasets: | NR | NR |
|  | -mean DSC=0.9899 | DSC=0.9355±0.0557 |  |  |
|  | -mean HD=5.26 ± 0.6 mm | HD=4.19±1.04 mm |  |  |
| Zhai et al. (2023) | Left hip: | NR | NR | NR |
|  | -DSC=0.9737±0.0075, HD95=2.03±0.14 (mm) |  |  |  |
|  | Right hip: |  |  |  |
|  | -DSC=0.9713±0.0170, HD95=2.07±0.26 (mm) |  |  |  |
| Other methods |  |  |  |  |
| Guo et al. (2018) | Accuracy on 10 hip joints for the three different | NR | NR | NR |
|  | segmentation methods |  |  |  |
|  | ASD (mm): |  |  |  |
|  | -pelvis: Yokota's 0.55±0.15, Chandra's 0.51±0.12, |  |  |  |
|  | proposed method 0.42±0.08 |  |  |  |
|  | -left femoral head: Yokota's 0.51±0.12, Chandra's |  |  |  |
|  | 0.46±0.10, proposed method 0.38±0.07 |  |  |  |
|  | -right femoral head: Yokota's 0.52±0.11, |  |  |  |
|  | Chandra's 0.47±0.12, proposed method 0.39±0.08 |  |  |  |
|  | DSC (%): |  |  |  |
|  | -pelvis: Yokota's 95.82±1.55, Chandra's |  |  |  |
|  | 96.47±1.42, proposed method 97.34±0.56 |  |  |  |
|  | -left femoral head: Yokota's 96.73±1.17, |  |  |  |
|  | Chandra's 97.34±1.26, proposed method |  |  |  |
|  | 98.06±0.58 |  |  |  |
|  | -right femoral head: Yokota's 96.26±1.12, |  |  |  |
|  | Chandra's 96.91±1.08, proposed method |  |  |  |
|  | 97.73±0.47 |  |  |  |
|  | TPR (%): |  |  |  |
|  | -pelvis: Yokota's 93.35±2.43, Chandra's |  |  |  |
|  | 93.98±3.02, proposed method 95.86±1.48 |  |  |  |
|  | -left femoral head: Yokota's 93.46±3.30, |  |  |  |
|  | Chandra's 94.80±2.92, proposed method |  |  |  |
|  | 96.34±1.27 |  |  |  |
|  | -right femoral head: Yokota's 93.92±2.86, |  |  |  |
|  | Chandra's 95.37±4.12, proposed method |  |  |  |
|  | 96.83±1.22 |  |  |  |
|  | Comparison of Yao's method with proposed |  |  |  |
|  | methos on 50 hip joints |  |  |  |
|  | ASD (mm): |  |  |  |
|  | -pelvis: proposed method 0.42±0.09, Yao's |  |  |  |
|  | 0.46±0.12 |  |  |  |
|  | -left femoral head: proposed method 0.38±0.05, |  |  |  |
|  | Yao's 0.42±0.06 |  |  |  |
|  | -right femoral head: proposed method 0.39±0.08, |  |  |  |
|  | Yao's 0.41±0.09 |  |  |  |
|  | DSC (%): |  |  |  |
|  | -pelvis: proposed method 97.32±0.52, Yao's |  |  |  |
|  | 95.71±0.71 |  |  |  |
|  | -left femoral head: proposed method 98.03±0.53, |  |  |  |
|  | Yao's 96.61±0.72 |  |  |  |
|  | -right femoral head: proposed method 97.72±0.33, |  |  |  |
|  | Yao's 96.68±0.62 |  |  |  |
|  | TPR (%): |  |  |  |
|  | -pelvis: proposed method 96.12±1.67, Yao's |  |  |  |
|  | 94.65±1.94 |  |  |  |
|  | -left femoral head: proposed method 96.77±1.82, |  |  |  |
|  | Yao's 95.05±2.24 |  |  |  |
|  | -right femoral head: proposed method 96.68±1.53, |  |  |  |
|  | Yao's 94.95±2.33 |  |  |  |
| Frontiers in Bioengineering and Biotechnology |  |  | frontiersin.org |

### Formule


$$)2016$$

### Formule


$$DSC 2 GT ∩ MS | | GT | |+ MS | | 2TP 2TP + FP + FNG$$

### Formule


$$HD max d A, B ( ), d B, A ( ) { } with d(A, B$$
