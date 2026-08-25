# Learning the What and How of Annotation in Video Object Segmentation

**Auteurs** : Thanos Delatolas, Vicky Kalogeiton, Dim P. Papadopoulos
**Année** : 2024
**DOI** : 10.1109/wacv57701.2024.00680

## Résumé

Video Object Segmentation (VOS) is crucial for several applications, from video editing to video data generation. Training a VOS model requires an abundance of manually labeled training videos. The de-facto traditional way of annotating objects requires humans to draw detailed segmentation masks on the target objects at each video frame. This annotation process, however, is tedious and time-consuming. To reduce this annotation cost, in this paper, we propose EVA-VOS, a human-in-the-loop annotation framework for video object segmentation. Unlike the traditional approach, we introduce an agent that predicts iteratively both which frame ("What") to annotate and which annotation type ("How") to use. Then, the annotator annotates only the selected frame that is used to update a VOS module, leading to significant gains in annotation time. We conduct experiments on the MOSE and the DAVIS datasets and we show that: (a) EVA-VOS leads to masks with accuracy close to the human agreement 3.5× faster than the standard way of annotating videos; (b) our frame selection achieves state-of-the-art performance; (c) EVA-VOS yields significant performance gains in terms of annotation time compared to all other methods and baselines.

## Méthodologie

{'study_design': "Pipeline human-in-the-loop itératif combinant (a) un modèle régressant la qualité de segmentation pour sélectionner la frame à annoter (frame la plus distante de sa frame pré-annotée la plus proche), (b) une politique de RL profond sélectionnant le type d'annotation (clicks, scribbles, mask, etc.) en maximisant le gain de qualité de segmentation rapporté au temps d'annotation, (c) une mise à jour du module VOS après chaque annotation pour propager le masque à toute la vidéo.", 'intervention': 'EVA-VOS : agent combiné de sélection de frame ("What to annotate?") et de sélection du type d\'annotation ("How to annotate?"), utilisé de manière itérative pour guider l\'annotateur humain.', 'control': "Annotation manuelle traditionnelle (dessin d'un masque de segmentation détaillé à chaque frame échantillonnée) et méthode interactive de Caelles et al. [8] basée sur des scribbles et une sélection manuelle de la pire frame par l'annotateur.", 'primary_outcomes': ["Qualité de segmentation (J&F) des masques prédits en fonction du temps d'annotation humaine"], 'secondary_outcomes': ["Performance de la sélection de frame seule (état de l'art)", "Performance de la sélection du type d'annotation seule", 'Généralisation cross-dataset de EVA-VOS'], 'statistical_methods': ["Modèle de régression pour prédire la qualité d'un masque de segmentation", "Politique d'apprentissage par renforcement profond (deep RL) pour la sélection du type d'annotation"], 'duration': "Comparaisons rapportées jusqu'à 200 heures de temps d'annotation cumulé", 'setting': 'Expériences computationnelles sur les datasets vidéo publics MOSE [22] et DAVIS [58]'}

## Résultats

{'quantitative': [{'outcome': "Vitesse d'annotation pour atteindre une précision proche de l'accord humain", 'value': '3.5x', 'unit': 'facteur de vitesse', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Conclusion', 'source_quote': 'EVA-VOS leads to masks with accuracy close to the human agreement 3.5× faster than the standard way of annotating videos'}, {'outcome': "Comparaison des méthodes d'annotation sur MOSE (temps humain pour atteindre J&F = 0.75, 0.8, 0.85 ; J&F moyen jusqu'à 200 heures)", 'value': 'Données rapportées dans le Tableau 1, valeurs numériques non fournies dans le texte disponible', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results (Table 1)', 'source_quote': 'We report the human annotation time in hours for each method to reach different J &F values (0.75, 0.8, 0.85). We also report the average J &F up to 200 hours.'}], 'qualitative_findings': [], 'main_findings': ["EVA-VOS produit des masques dont la précision est proche de l'accord humain, 3.5 fois plus rapidement que l'annotation standard", "La méthode de sélection de frame proposée atteint des performances état de l'art", "EVA-VOS apporte des gains significatifs en temps d'annotation par rapport à toutes les autres méthodes et baselines testées"]}

## Conclusions

EVA-VOS constitue une alternative efficace à l'annotation manuelle traditionnelle des objets vidéo par masques de segmentation Le framework réduit significativement le temps d'annotation humaine total (accélération de 3.5×) tout en produisant des masques de segmentation de haute qualité Ces gains sont particulièrement démontrés sur le dataset MOSE, jugé plus exigeant

## at J &F = Avg J &F ↑

| Selection Selection | 0.75 0.80 0.85 ↓ |  |
| --- | --- | --- | --- |
| Mask-only Oracle ⋆ | 34.42 45.62 67.64 | 0.83 |
| Clicks-only Oracle ⋆ | 14.05 15.65 22.85 | 0.87 |
| Oracle ⋆ | Oracle ⋆ | 12.96 14.13 17.63 | 0.92 |
| Mask-only IVOS-W [86] 39.37 94.33 192.26 | 0.78 |
| Mask-only IVOS-W++ 40.53 59.81 113.93 | 0.79 |
| Mask-only L2-ResNet50 40.55 59.92 109.42 | 0.80 |
| Mask-only Random | 40.55 69.60 107.40 | 0.80 |
| Mask-only EVA-VOS | 32.55 53.26 80.71 | 0.82 |
| Random | Random | 24.08 36.10 65.84 | 0.85 |
| Clicks-only Random | 15.32 21.22 35.10 | 0.86 |
| EVA-VOS EVA-VOS | 14.24 17.25 29.80 | 0.87 |

### Formule


$$M t = {M t 1 , M t 2 , .$$

### Formule


$$f * = arg max i∈{1,2...N } min j∈{1,2...t} {d(E i , E j )}(1)$$

### Formule


$$r = SQ g+1 -SQ g tc .(2)$$

### Formule


$$s = pv • γ t θ a + c ,(3)$$
