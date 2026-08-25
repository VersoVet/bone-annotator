# An automatic congenital radio-ulnar synostosis deformity evaluation method (CRUS-DE): integrating TLT-SAM and GPMM-R for landmark identification.

**Auteurs** : Liu L, Cui Y, Zhou T, Chen S, Guo Y, Zhou X.
**Année** : 2026
**DOI** : 10.1038/s41598-026-36638-4

## Résumé

Congenital Radio-Ulnar Synostosis (CRUS) causes difficulty in forearm rotation, which is treated using osteotomy. Effective preoperative planning of osteotomy requires automatic and objective quantification of deformity angles. In this paper, an automatic Congenital Radio-Ulnar Synostosis deformity evaluation method (CRUS-DE) is proposed. Initially, a method using threshold-layer tracking (TLT) and the segment anything model (SAM) is designed to recognize and segment the forearm from CT images. Subsequently, the Gaussian Process Morphable Model, in conjunction with refinement based on anatomical characteristics is developed to accurately identify forearm landmarks. Finally, the model automatically estimates deformity angles for quantitative assessment of CRUS. The forearm landmarks and deformity angles were successfully obtained from CT images based on CRUS-DE with average errors ranging from 0.98 to 1.55 mm and from 0.7° to 2.4°, respectively. No significant differences existed betwee

## Méthodologie

{'study_design': "Développement et validation d'une méthode automatique (CRUS-DE) combinant segmentation par threshold-layer tracking (TLT) et segment anything model (SAM), puis identification des repères anatomiques par Gaussian Process Morphable Model avec raffinement (GPMM-R), suivie d'un calcul automatique des angles de déformité, comparée à une méthode manuelle réalisée par des chirurgiens seniors", 'intervention': "Méthode automatique CRUS-DE (TLT-SAM pour la segmentation + GPMM-R pour l'identification des repères + quantification automatique des angles de déformité)", 'control': "Méthode manuelle de segmentation, d'identification des repères et de mesure des angles réalisée par des chirurgiens seniors (Global Truth)", 'primary_outcomes': ["Précision de la segmentation de l'avant-bras (IOU)", "Erreur moyenne d'identification des repères anatomiques (mm)", 'Erreur moyenne des angles de déformité estimés (degrés)'], 'secondary_outcomes': ['Différences significatives entre méthode automatique et méthode manuelle', 'Différences significatives entre avant-bras normal et avant-bras CRUS'], 'statistical_methods': ['Comparaison des différences (tests statistiques non détaillés explicitement dans le texte fourni)'], 'duration': None, 'setting': "Imagerie CT de l'avant-bras, contexte de planification préopératoire d'ostéotomie"}

## Résultats

{'quantitative': [{'outcome': "Consistance de la segmentation osseuse de l'avant-bras (TLT-SAM) vs méthode manuelle", 'value': 'IOU 0.929-0.991', 'unit': 'IOU', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'The segmented forearm bone masks by the TLT-SAM method have a high consistency with the manual method, with IOU ranging from 0.929~0.991.'}, {'outcome': "Erreur moyenne d'identification des repères anatomiques", 'value': '0.98 à 1.55', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Conclusion', 'source_quote': 'The accuracy of recognized landmarks is verified by comparing with the "Global Truth" labeled by senior surgeons, and the average error ranges from 0.98mm to 1.55mm.'}, {'outcome': 'Erreur moyenne des angles de déformité estimés', 'value': '0.7 à 2.4', 'unit': 'degrés', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The forearm landmarks and deformity angles were successfully obtained from CT images based on CRUS-DE with average errors ranging from 0.98 to 1.55mm and from 0.7° to 2.4°, respectively.'}, {'outcome': 'Angle DAR (déformité dans le plan sagittal) pour avant-bras CRUS', 'value': '17.9 à 24.8', 'unit': 'degrés', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The DAR and PAU were always positive (from 17.9 to 24.8° and from 12.0 to 17.9°, respectively), which indicated for the CRUS forearms, the distal forearm tended towards the palmar side.'}, {'outcome': 'Angle PAU (déformité dans le plan sagittal) pour avant-bras CRUS', 'value': '12.0 à 17.9', 'unit': 'degrés', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The DAR and PAU were always positive (from 17.9 to 24.8° and from 12.0 to 17.9°, respectively), which indicated for the CRUS forearms, the distal forearm tended towards the palmar side.'}], 'qualitative_findings': ["La segmentation aux deux extrémités de l'avant-bras était relativement incomplète mais avait peu d'effet sur l'identification des repères", 'Les repères étiquetés par les chirurgiens seniors sont subjectifs et introduisent une incertitude dans la planification préopératoire', "Le RAR (angle dans le plan coronal) était toujours positif et beaucoup plus grand pour le radius CRUS, en raison de la fusion du côté ulnaire de la tête radiale avec l'ulna proximal", "L'UAU était beaucoup plus grand pour l'ulna CRUS en raison de la dislocation de l'articulation radio-ulnaire distale"], 'main_findings': ["La méthode CRUS-DE permet une quantification automatique et fiable des angles de déformité chez les patients CRUS à partir d'images CT", "Aucune différence significative n'a été trouvée entre la méthode automatique et la méthode manuelle", 'Des différences significatives ont été trouvées dans les angles de déformité entre avant-bras normal et avant-bras CRUS', 'Le DAR est la déformité ayant le plus grand impact sur la CRUS selon la littérature']}

## Conclusions

La méthode CRUS-DE combinant TLT-SAM (segmentation) et GPMM-R (identification des repères) permet une quantification automatique fiable des déformités de la CRUS La méthode automatique présente une haute cohérence avec la méthode manuelle, sans différence significative Cette méthode est explicable et peut être utilisée en planification préopératoire, évaluation postopératoire de l'ostéotomie, et potentiellement en chirurgie assistée par robot

## Table 1 . Demographic data of cases included in the study.

| Gende r | Number Median | Age (years) IQR (Q1 to Range (min. to Q3) max.) |
| --- | --- | --- | --- | --- |
| Male | 15 | 5 | 2 (4 to 6) | 8 (2 to 10) |
| Femal e | 5 | 5 | 3 (2 to 5) | 5 (1 to 6) |

## Table 3 . Confusion matrix of surface points by two methods.

| ACCEPTED MANUSCRIPT |
| --- | --- | --- | --- |
| A R T I C L E | I N | P R E S S |
|  |  | Automated method |
|  |  | Radius | Ulna |

## Table 4 . Error of deformity angle quantification.

|  | Mean±std Range (Q1 to Q3) T value P value |
| --- | --- | --- | --- |
| RAR (°) | 2.2±1.4 | 1.2 to 3.5 | 1.644 0.108 |
| DAR (°) | 2.0±1.3 | 1.0 to 2.6 | -0.253 0.802 |
| IRAR (°) | 2.4±1.5 | 1.1 to 3.7 | -0.585 0.562 |
| UAU (°) | 0.7±0.5 | 0.4 to 1.1 | 1.337 0.189 |
| PAU (°) | 1.4±1.1 | 0.5 to 2.0 | 1.219 0.230 |
| IRAU (°) | 2.1±1.6 | 0.8 to 3.3 | -0.872 0.389 |

## T-test for deformity angles between normal and CRUS forearms.

|  | Normal forearm (Q1 to Q3) | CRUS forearm (Q1 to Q3) | T value | P value |
| --- | --- | --- | --- | --- |
| RAR (°) | 1.9 to 5.5 | 5.2 to 13.0 | 4.320 0.000 |
| DAR (°) | 1.7 to 7.1 | 17.9 to 24.8 | 6.529 0.000 |
| IRAR (°) | 5.1 to 9.0 | 29.4 to 68.9 | 3.339 0.002 |
| UAU (°) | -4.8 to -0.8 | -0.1 to 4.7 | 3.490 0.001 |
| PAU (°) | 0.1 to 6.8 | 12.0 to 17.9 | 3.775 0.001 |
| IRAU (°) | 6.5 to 10.8 | 67.8 to 128.1 | 9.384 0.000 |

### Formule


$$A R T I C L E I N P R E S S$$

### Formule


$$ACCEPTED MANUSCRIPT A R T I C L E I N P R E S S$$

### Formule


$$loss i = [ w P w S w R ][ | P i -P| | S i -S| | R i -R|] T (1)$$

### Formule


$$f k (p k ,q k ) = f k1 ⋅ f k2 = e -( (‖p k ,c k-1 1 ‖+‖q k ,c k-1 2 ‖) 2 2σ 2 1 + (‖p k ,q k ‖-d min ) 2σ2 2 )$$

### Formule


$$d min = min {‖p k ,q k ‖} , ∀p k ,q k ∈ C k(3)$$

### Formule


$$ACCEPTED MANUSCRIPT A R T I C L E I N P R E S S$$

### Formule


$$c(x) ∼ μ(x) + ∑ r i=1 α i λ i ϕ i (x),α i ∈ N(0,1)(4)$$

### Formule


$$argmin α 1 ,α 2 ,⋯,α r D [ C T ,μ + ∑ r i=1 α i λ i ϕ i ] +η∑ r i=1 α 2 i (5)$$

### Formule


$$lm = argmax p ‖p -O RP ‖ 2 ,p ∈ U(lm temp ) (6) ACCEPTED MANUSCRIPT A R T I C L E I N P R E S S$$

### Formule


$$IOU = A∩B A∪B (7)$$

### Formule


$$ACCEPTED MANUSCRIPT A R T I C L E I N P R E S S$$

### Formule


$$ACCEPTED MANUSCRIPT A R T I C L E I N P R E S S$$
