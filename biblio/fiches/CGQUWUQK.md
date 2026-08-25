# Active Learning Enabled Low-Cost Cell Image Segmentation Using Bounding Box Annotation

**Auteurs** : yu zhu, Li Xu, Qiang Yang
**Année** : 2024
**DOI** : 10.2139/ssrn.4960393

## Résumé

Cell image segmentation is usually implemented using fully supervised deep learning methods, which heavily rely on extensive annotated training data. Yet, due to the complexity of cell morphology and the requirement for specialized knowledge, pixel-level annotation of cell images has become a highly labor-intensive task. To address the above problems, we propose an active learning framework for cell segmentation using bounding box annotations, which greatly reduces the data annotation cost of cell segmentation algorithms. First, we generate a box-supervised learning method (denoted as YOLO-SAM) by combining the YOLOv8 detector with the Segment Anything Model (SAM), which effectively reduces the complexity of data annotation. Furthermore, it is integrated into an active learning framework that employs the MC DropBlock method to train the segmentation model with fewer box-annotated samples. Extensive experiments demonstrate that our model saves more than ninety percent of data annotation time compared to mask-supervised deep learning methods.

## Méthodologie

{'study_design': "Développement et évaluation expérimentale d'une méthode de segmentation supervisée par boîtes englobantes (YOLO-SAM) intégrée dans un cadre d'apprentissage actif utilisant l'échantillonnage d'incertitude MC DropBlock, comparée à des méthodes supervisées par boîtes (BoxInst, BoxLevelset) et par masques (Mask R-CNN, SOLOv2)", 'intervention': "Entraînement du détecteur YOLOv8 (version medium, confidence 0.2, IoU pour NMS 0.5) combiné au Segment Anything Model (SAM, backbone ViT-B) pour générer des masques à partir de boîtes englobantes prédites, intégré dans une boucle d'apprentissage actif avec échantillonnage par incertitude MC DropBlock (probabilité de dropout 0.25, taille de bloc 7, 8 passes avant)", 'control': "Méthodes comparatives : BoxInst et BoxLevelset (supervision par boîtes), Mask R-CNN et SOLOv2 (supervision par masques), ainsi qu'un échantillonnage aléatoire dans le cadre d'apprentissage actif", 'primary_outcomes': ['Coefficient de Dice (DSC) mesurant la similarité entre le masque prédit et le masque de vérité terrain'], 'secondary_outcomes': ["Temps d'annotation des données comparé entre annotation par boîte et par masque"], 'statistical_methods': ['Optimiseur AdamW (lr initial 0.01, décroissance facteur 0.01, batch size 16, momentum 0.937, weight decay 0.0005)', 'Moyenne du DSC sur trois répétitions expérimentales', "Calcul de l'incertitude par combinaison multiplicative des composantes catégorie, boîte englobante et masque (Équations 1-4)"], 'duration': "150 époques d'entraînement par boucle d'apprentissage actif", 'setting': 'Expériences réalisées sur GPU NVIDIA GTX 3090 avec Python 3.8'}

## Résultats

{'quantitative': [{'outcome': 'Comparaison YOLO-SAM vs méthodes supervisées par boîte et par masque sur PanNuke, DSB2018, MoNuSeg (DSC)', 'value': None, 'unit': 'DSC', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, Comparison of Box-supervised Learning Approaches', 'source_quote': 'On all three datasets, YOLO-SAM outperforms the two representative box-supervised segmentation models, with substantial improvements in segmentation accuracy. Moreover, the performance of YOLO-SAM is almost comparable to the masksupervised method Mask R-CNN.'}, {'outcome': "Temps d'annotation d'une boîte englobante par rapport à un masque basé sur un polygone (COCO)", 'value': '8.8', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Introduction', 'source_quote': "Research has shown that annotating an object's bounding box in COCO only requires 8.8% of the time (7s vs. 79.2s) compared to annotating its mask based on polygons"}, {'outcome': "Réduction du temps d'annotation des données comparée aux méthodes supervisées par masque", 'value': 'plus de 90', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'Extensive experiments demonstrate that our model saves more than ninety percent of data annotation time compared to mask-supervised deep learning methods.'}], 'qualitative_findings': ['Les masques prédits par BoxInst présentent des instances cellulaires chevauchantes et non détectées', 'Les masques générés par BoxLevelset manquent de clarté au niveau des contours', 'YOLO-SAM détecte précisément les instances cellulaires et améliore la forme du masque de segmentation'], 'main_findings': ['YOLO-SAM surpasse les méthodes de segmentation supervisées par boîte de pointe (BoxInst, BoxLevelset) sur les trois jeux de données', 'La performance de YOLO-SAM est presque comparable à la méthode supervisée par masque Mask R-CNN', "La méthode combinée (YOLO-SAM + apprentissage actif avec MC DropBlock) atteint une performance quasi équivalente à l'apprentissage supervisé par masque en utilisant un minimum de données", "Le modèle final atteint la performance de Mask R-CNN en n'utilisant qu'une fraction du temps d'annotation"]}

## Conclusions

La combinaison synergique des annotations par boîtes englobantes et de l'apprentissage actif réduit significativement le coût d'annotation nécessaire pour entraîner un réseau de segmentation cellulaire La méthode YOLO-SAM, utilisant uniquement des annotations par boîtes englobantes, permet une segmentation cellulaire précise L'approche d'apprentissage actif basée sur MC DropBlock améliore significativement l'efficacité de l'amélioration de la performance du modèle La méthode proposée atteint la performance de Mask R-CNN tout en n'utilisant qu'une fraction du temps d'annotation, réduisant substantiellement le coût temporel d'annotation des données

## e. f (x| ƩL i )≈f (x|L). The details of our data augmentation algorithm are presented in Algorithm 1.

| Algorithm 1: Box-supervised Segmentation Method Based on Active Learning |
| --- | --- |
| Input: data-pool, sample-size, pre-training weight F 0 =0 |
| Output: DSC-list |
| 1: initia-data ← RandomlySample(data-pool, sample-size) |
| 2: L 0 ← Annotate(initia-data) |
| 9: for i ← 1 to loop do |
| 10: | sampled-image ←sampling-strategy (data-pool, sample-size) |
| 11: | L i ← Annotate(Sampled-image) |
| 12: | F i ← Train-YOLOv8(L i +L i-1 , F i-1 ) |
| 13: | Bbox-output ← F(validate-set) |
| 14: | Mask-output ← SAM(Bbox-output) |
| 15: | DSC ← Evaluate-YOLO-SAM(Mask-output) |
| 16: | DSC-list.insert(DSC) |
| 17: |  |

## Performance comparison of different cell segmentation algorithms on PanNuke, 2018DSB, MoNuSeg datasets. The best results are in bold.

|  | Method | PanNuke | 2018DSB | MoNuSeg |
| --- | --- | --- | --- | --- |
| Mask-supervised | Mask R-CNN | 81.02 | 86.26 | 75.75 |
| methods | SOLOv2 | 78.25 | 87.80 | 61.54 |
| Box-supervised methods | BoxInst Boxlevelset Ours(YOLO-SAM) | 69.80 75.81 80.90 | 77.37 83.73 88.39 | 62.52 76.28 78.01 |

## For example, on the Pannuke dataset, when our model achieves 99% of the performance of Mask R-CNN, the sampling method based on MC DropBlock 1 uses only 32.7% of the box-annotated samples, i.e., it uses only 32.7% *8.8%=2.9% of the annotation time. Thus, compared to mask-supervised segmentation algorithms, our model requires only a few percent of the annotation time to achieve high-performance segmentation, i.e., it saves more than ninety percent of the annotation time.

| 𝐴𝐴 = | 𝑁𝑁 𝑏𝑏 𝑁𝑁 𝑚𝑚 | × 8.8% |
| --- | --- | --- |

## Minimum annotation time used by each of the sampling methods of active learning on each of the three datasets when the model performance (DSC) reaches 99% of that of Mask-RCNN. The best results are in bold.

| Method | Datasets | PanNuke | 2018DSB | MoNuSeg |
| --- | --- | --- | --- | --- |
| MC DropBlock 1 | 2.9% | 4.1% | 2.7% |
| MC DropBlock 2 | 7.8% | 7.6% | 3.6% |
| MC DropBlock 3 | 4.5% | 5.1% | 3.6% |

### Formule


$$𝑐𝑐 𝑖𝑖 = 1 𝑡𝑡 ∑ [1 - -∑ 𝑃𝑃(𝑘𝑘 𝑖𝑖 )•log𝑃𝑃(𝑘𝑘 𝑖𝑖 ) 𝑚𝑚 𝑖𝑖=1 -∑ 1 𝑚𝑚 • 𝑚𝑚 𝑖𝑖=1 𝑙𝑙𝑙𝑙𝑙𝑙 1 𝑚𝑚 ] 𝑡𝑡 𝑖𝑖=1$$

### Formule


$$𝑐𝑐 𝑏𝑏 = 1 𝑡𝑡 • ∑ 𝐼𝐼𝐼𝐼𝐼𝐼�𝐵𝐵 � (𝑆𝑆), 𝐵𝐵(𝑠𝑠 𝑖𝑖 )� 𝑡𝑡 𝑖𝑖=1$$

### Formule


$$𝑐𝑐 𝑚𝑚 = 1 𝑡𝑡 • ∑ 𝐼𝐼𝐼𝐼𝐼𝐼 �𝑀𝑀 � (𝑆𝑆), 𝑀𝑀�𝑠𝑠 𝑗𝑗 �� 𝑡𝑡 𝑗𝑗=1$$

### Formule


$$𝑐𝑐 = 𝑐𝑐 𝑖𝑖 • 𝑐𝑐 𝑏𝑏 • 𝑐𝑐 𝑚𝑚 (4)$$
