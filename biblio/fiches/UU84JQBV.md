# DeNTNet: Deep Neural Transfer Network for the detection of periodontal bone loss using panoramic dental radiographs

**Auteurs** : Jae‐Young Kim, Hong-Seok Lee, In‐Seok Song, Kyu-Hwan Jung
**Année** : 2019
**DOI** : 10.1038/s41598-019-53758-2

## Résumé

in this study, a deep learning-based method for developing an automated diagnostic support system that detects periodontal bone loss in the panoramic dental radiographs is proposed. the presented method called Dentnet not only detects lesions but also provides the corresponding teeth numbers of the lesion according to dental federation notation. Dentnet applies deep convolutional neural networks(cnns) using transfer learning and clinical prior knowledge to overcome the morphological variation of the lesions and imbalanced training dataset. With 12,179 panoramic dental radiographs annotated by experienced dental clinicians, DeNTNet was trained, validated, and tested using 11,189, 190, and 800 panoramic dental radiographs, respectively. Each experimental model was subjected to comparative study to demonstrate the validity of each phase of the proposed method. When compared to the dental clinicians, DeNTNet achieved the F1 score of 0.75 on the test set, whereas the average performance of dental clinicians was 0.69.Periodontal disease caused by dental bacterial infection is one of the most common human diseases affecting gums and the support structure of the teeth. Periodontitis is an inflammatory disease which can result in periodontal bone loss (PBL) and ultimately leads to loosening or loss of teeth if not diagnosed and treated properly 1 . Therefore, early detection and management of PBL plays a crucial role in improving the clinical outcome of periodontal disease. To acquire valuable information for the diagnosis and treatment planning of PBL, radiological exams, including bitewing, periapical, and panoramic radiographs, have been widely used in clinical practices. While intra-oral images such as bitewing and periapical radiographs have been routinely taken for the diagnosis of PBL, extra-oral panoramic radiographs which capture the entire mouth have been widely used for their advantages over intra-oral images such as lower radiation exposure, better patient comfort, faster and easier procedure, and wider field of view 2,3 . However, detecting and diagnosing PBL in panoramic dental radiographs is considered a difficult task with a low intra and inter-examiner agreement rate due to their complex structures and low resolution 4 as shown in Fig. 1.Deep convolutional neural networks (DCNNs) have recently been actively adopted in medical image analysis with successful applications to computer-aided detection (CADe) and diagnosis (CADx) [5][6][7][8] . While the majority of these studies focus on analyzing images from radiology, pathology, dermatology, and ophthalmology, studies dealing with various dental imaging modalities using DCNNs have also been conducted recently 9 . In addition to the aforementioned works which focus on caries and plaque, some studies also deal with periodontal disease 10,11 . Lee et al. 10 used intra-oral images for the detection of periodontally compromised teeth, whereas Krois et al. 11 proposed a DCNN-based method for the detection of PBL in panoramic dental radiographs. The proposed method in Krois et al. 11 however has some limitations: their DCNN is trained using manually cropped teeth patches, the dataset used in their study is small, and their DCNN architecture is shallow.In this study, we develop a fully automated method to detect PBL in panoramic dental radiographs. By exploiting transfer learning and lesion correlation prior information, the proposed DCNN named DeNTNet is able to accurately detect PBL, outperforming human experts when tested on data consisting of all teeth types. To be more clinically applicable, DeNTNet is trained to predict the existence of PBL for each tooth and is thus capable of providing the teeth

## Méthodologie

{'study_design': "Étude de développement et validation d'un modèle d'apprentissage profond (réseau de neurones convolutif profond, DCNN) nommé DeNTNet, utilisant le transfer learning et des connaissances cliniques a priori pour la détection de la PBL", 'intervention': 'Application de DeNTNet (DCNN) sur les radiographies panoramiques dentaires pour détecter la PBL et identifier les dents atteintes selon la notation de la Fédération Dentaire', 'control': 'Comparaison avec les diagnostics posés par des cliniciens dentaires expérimentés', 'primary_outcomes': ['Score F1 de détection de la PBL par DeNTNet comparé à celui des cliniciens dentaires'], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': "Korea University Anam Hospital (étude approuvée par le comité d'éthique institutionnel, IRB No. 2016AN0267, avec renonciation au consentement éclairé)"}

## Résultats

{'quantitative': [{'outcome': 'Performance moyenne des cinq cliniciens dentaires - AUROC', 'value': '0.85', 'unit': 'AUROC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'The average performance of five dental clinicians was 0.85 in AUROC'}, {'outcome': 'Performance moyenne des cinq cliniciens dentaires - F1 score', 'value': '0.69', 'unit': 'F1 score', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': '0.69 in F1 score'}, {'outcome': 'Performance moyenne des cinq cliniciens dentaires - Sensibilité', 'value': '0.78', 'unit': 'sensitivity', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': '0.78 in sensitivity'}, {'outcome': 'Performance moyenne des cinq cliniciens dentaires - Spécificité', 'value': '0.92', 'unit': 'specificity', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': '0.92 in specificity'}, {'outcome': 'Performance moyenne des cinq cliniciens dentaires - PPV', 'value': '0.62', 'unit': 'positive predictive value', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': '0.62 in PPV'}, {'outcome': 'Performance moyenne des cinq cliniciens dentaires - NPV', 'value': '0.96', 'unit': 'negative predictive value', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': '0.96 in NPV'}, {'outcome': 'F1 score de DeNTNet - réglage équilibré (balanced setting)', 'value': '0.74', 'unit': 'F1 score', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'The balanced setting, which was selected to maximize the F1 score, achieved the F1 score of 0.74'}, {'outcome': 'F1 score de DeNTNet - réglage haute sensibilité (high sensitivity setting)', 'value': '0.71', 'unit': 'F1 score', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'high sensitivity and high specificity settings achieved F1 scores of 0.71 and 0.73, respectively'}, {'outcome': 'F1 score de DeNTNet - réglage haute spécificité (high specificity setting)', 'value': '0.73', 'unit': 'F1 score', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'high sensitivity and high specificity settings achieved F1 scores of 0.71 and 0.73, respectively'}], 'qualitative_findings': ['Le DeNTNet de base (baseline), entraîné directement à partir du radiographe original sans transfer learning ni auxiliary loss, a montré une performance comparable à la moyenne des cinq cliniciens dentaires.', "L'application de l'entraînement multi-phase proposé (ROI segmentation, pre-training pour transfer learning, auxiliary loss, et classification ensembliste) a permis à DeNTNet de surpasser les cliniciens dentaires en termes de F1 score.", 'Le point de fonctionnement à haute sensibilité a été choisi de sorte que la spécificité soit proche de celle du pire clinicien dentaire, tandis que le point de fonctionnement à haute spécificité a été choisi de sorte que la sensibilité de DeNTNet soit proche de celle du pire clinicien dentaire.', "Les performances de chaque clinicien humain ont été calculées en comparant la décision de l'expert (présence/absence de PBL) sur la dent cible avec le vote majoritaire parmi les experts humains, utilisé comme vérité terrain.", 'Les performances du modèle ont été obtenues à partir de ses prédictions de classification au niveau des dents, avec différents points de fonctionnement variables.'], 'main_findings': ['DeNTNet, avec son entraînement multi-phase complet, surpasse les cliniciens dentaires en termes de F1 score sur la tâche de détection de la perte osseuse parodontale (PBL) au niveau des dents.', "La version de base de DeNTNet (sans transfer learning ni auxiliary loss) atteint une performance comparable à celle des cliniciens dentaires en moyenne, ce qui souligne l'importance des composantes d'entraînement multi-phase proposées pour dépasser la performance humaine."]}

## Conclusions

A fully automated method for PBL detection with tooth numbering in panoramic dental radiographs was proposed Through the multi-step training framework, the proposed model was able to achieve a PBL detection performance superior to that of dental clinicians This approach is expected to substantially benefit clinical practices by improving the efficiency of diagnosing PBL and reducing the workload involved in reporting tooth numbers

## Performance comparison of the proposed method and human clinicians on the test dataset. AUROC is the area under receiver operating characteristic curve, F1 score is the harmonic mean of the precision and recall, PPV is the positive predictive value, and NPV is the negative predictive value. The performance of DeNTNet was measured with various operating point settings.

| Performance Measure | AUROC | F1 score Sensitivity | Specificity | PPV NPV |
| --- | --- | --- | --- | --- | --- | --- |
| Clinician 1 | 0.84 | 0.69 | 0.74 | 0.93 | 0.65 | 0.95 |
| Clinician 2 | 0.84 | 0.68 | 0.75 | 0.92 | 0.61 | 0.96 |
| Clinician 3 | 0.85 | 0.68 | 0.80 | 0.91 | 0.59 | 0.96 |
| Clinician 4 | 0.87 | 0.70 | 0.83 | 0.91 | 0.61 | 0.97 |
| Clinician 5 | 0.85 | 0.70 | 0.78 | 0.92 | 0.64 | 0.96 |
| Clinician Average | 0.85 | 0.69 | 0.78 | 0.92 | 0.62 | 0.96 |
| DeNTNet(Baseline) | 0.92 | 0.66 | 0.66 | 0.94 | 0.65 | 0.94 |
| DeNTNet(Balanced setting) | 0.95 | 0.75 | 0.77 | 0.95 | 0.73 | 0.96 |
| DeNTNet(High sensitivity setting) | 0.95 | 0.71 | 0.87 | 0.90 | 0.60 | 0.97 |
| DeNTNet(High specificity setting) | 0.95 | 0.73 | 0.74 | 0.96 | 0.77 0.95 |

## ROI Segmentation Pre-trained Weight Auxiliary Loss Ensembled Network Incisor Canine Premolar Molar All Teeth

|  |  |  |  | 0.64 | 0.67 | 0.69 | 0.65 | 0.66 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| √ |  |  |  | 0.71 | 0.68 | 0.68 | 0.67 | 0.68 |
| √ | √ |  |  | 0.73 | 0.71 | 0.67 | 0.69 | 0.70 |
| √ | √ | √ |  | 0.74 | 0.72 | 0.69 | 0.73 | 0.72 |
| √ | √ | √ | √ | 0.72 | 0.70 | 0.75 | 0.80 | 0.75 |

### Formule


$$∑ =        ≥ ∈ … ∈ … = y y C i N j T 1 if 0 otherwise , { 1, , }, {1, 2, , }(1)$$

### Formule


$$ij l L ij l R 1$$

### Formule


$$∑ ∑ λ = - + - - + L y n y y n w ( , ) 1 [ log (1 )log(1 )] 2 , (2$$

### Formule


$$) R R R i i R i R i R i R k k 2 ŷ ŷ ŷ$$

### Formule


$$ŷ ŷ ŷ ŷ ŷ L y n y y ( , )1$$

### Formule


$$S S S i i S i S i S i S i S i S ∑ = - - + - - γ γ$$

### Formule


$$∑ =        ≥ y y C 1 if 0 otherwise (4) i S l i S l S ,$$

### Formule


$$= f f f { , } C A B$$

### Formule


$$∑ ∑ λ = -    - + - -    + γ γ ŷ ŷ ŷ ŷ ŷ ( ) ( ) ( ) ( ) L y N y y n w , 1 1 l og 1 l og 1 2 (5) C j C j C i ij C ij C ij C ij C ij C ij C k k 2$$

### Formule


$$α α =          ∈ + - ∈ ŷ f x j In Ca f x f x j Pr Mo ( ), i f { , } ( ) (1 ) ( ) if { , }(6)$$

### Formule


$$j j A j A j B ROI ROI R OI/2$$

### Formule


$$∑ = - = * = ′ ′ ′ ŷ ŷ L y c c c Z y C ( , , )( ) , 1 (7)$$

### Formule


$$2 1$$

### Formule


$$β = + ⋅ + ⋅ ∈ ∈ ŷ ŷ ŷ ŷ { } L y L y L y c L y c ( , ) ( , )(1 ( , , ) 1 ( , , )] (8)$$

### Formule


$$F j j C j j j U Aux j j j jL A ux j j j { }$$
