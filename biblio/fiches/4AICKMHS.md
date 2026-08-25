# Few-shot Medical Image Segmentation with Cycle-resemblance Attention

**Auteurs** : Hao Ding, Changchang Sun, Hao Tang, Dawen Cai, Yan Yan
**Année** : 2022
**DOI** : 10.48550/arxiv.2212.03967

## Résumé

Recently, due to the increasing requirements of medical imaging applications and the professional requirements of annotating medical images, few-shot learning has gained increasing attention in the medical image semantic segmentation field. To perform segmentation with limited number of labeled medical images, most existing studies use Prototypical Networks (PN) and have obtained compelling success. However, these approaches overlook the query image features extracted from the proposed representation network, failing to preserving the spatial connection between query and support images. In this paper, we propose a novel self-supervised few-shot medical image segmentation network and introduce a novel Cycle-Resemblance Attention (CRA) module to fully leverage the pixel-wise relation between query and support medical images. Notably, we first line up multiple attention blocks to refine more abundant relation information. Then, we present CRAPNet by integrating the CRA module with a classic prototype network, where pixel-wise relations between query and support features are well recaptured for segmentation. Extensive experiments on two different medical image datasets, e.g., abdomen MRI and abdomen CT, demonstrate the superiority of our model over existing state-of-the-art methods.

## Méthodologie

{'study_design': "Proposition d'un réseau de segmentation d'images médicales few-shot auto-supervisé intégrant un module Cycle-Resemblance Attention (CRA) au sein d'un réseau prototype classique (CRAPNet). Le module CRA compare la similarité entre paires de pixels appariées de manière cycle-consistante entre images support et query, construisant une connexion support-query-support, et incorpore la relation entre chaque pixel et ses 'voisins' les plus similaires pour obtenir les prototypes.", 'intervention': "Introduction du module Cycle-Resemblance Attention (CRA), composé de plusieurs blocs d'attention alignés pour affiner les informations de relation, combiné à des opérations non-locales calculant une somme pondérée en chaque position de pixel pour les caractéristiques support et query", 'control': None, 'primary_outcomes': ["Performance de segmentation d'images médicales en few-shot"], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': "Segmentation sémantique d'images médicales (IRM abdominale et CT abdominale) en contexte few-shot learning"}

## Résultats

{'quantitative': [{'outcome': 'Amélioration moyenne de CRAPNet sur Abdominal-MR par rapport à la meilleure baseline (setting 1)', 'value': '0.95', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'compared with the best baseline, CRAPNet achieves a significant average improvement of 0.95%, and 2.5% in setting 1 and 2, respectively'}, {'outcome': 'Amélioration moyenne de CRAPNet sur Abdominal-MR par rapport à la meilleure baseline (setting 2)', 'value': '2.5', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'compared with the best baseline, CRAPNet achieves a significant average improvement of 0.95%, and 2.5% in setting 1 and 2, respectively'}], 'qualitative_findings': ['Sur le dataset Abdominal-CT, la performance de CRAPNet est significativement meilleure que toutes les baselines, sauf pour SSL-ALPNet sur les catégories Spleen et Liver.', 'CRAPNet surpasse systématiquement toutes les autres baselines pour les différents organes sur le dataset Abdominal-MR.', 'CRAPNet a une meilleure précision de classification moyenne sur le dataset Abdominal-CT.', "La supériorité de CRAPNet sur Abdominal-MR est attribuée à une meilleure qualité d'image de ce dataset comparé à Abdominal-CT.", 'Les résultats visuels (Figure 3, setting 1) montrent que le modèle produit une segmentation plus précise, notamment pour la rate (spleen) et le foie (liver) sur le dataset IRM.', "Pour le rein gauche (left kidney), le modèle obtient une meilleure prédiction sur la frontière (boundary) de l'organe."], 'main_findings': ["CRAPNet surpasse globalement les baselines de l'état de l'art (ALPNet, SSL-PANet, SSL-ALPNet, SSL-RPNet) en segmentation d'images médicales few-shot.", 'CRAPNet obtient une amélioration moyenne significative de 0.95% (setting 1) et 2.5% (setting 2) sur le dataset Abdominal-MR par rapport à la meilleure baseline.', 'CRAPNet produit des segmentations visuellement plus précises, en particulier au niveau des frontières des organes (ex: rein gauche) et pour la rate et le foie sur IRM.']}

## Conclusions

Proposition d'une nouvelle méthode basée sur les prototypes introduisant un module Cycle-Resemblance Attention (CRA) pour exploiter pleinement la relation pixel par pixel entre les images de requête et de support médicales Les relations spatiales pixel par pixel entre images de support et de requête peuvent être bien préservées, résolvant le problème de perte d'information spatiale dans le réseau prototypique Le réseau proposé obtient une amélioration considérable par rapport aux approches de l'état de l'art Sur le jeu de données abdominal-CT, la méthode obtient plus de 10% d'amélioration sur le score dice moyen pour tous les labels Les études d'ablation illustrent de manière extensive l'implémentation actuelle des différents composants à optimiser La méthode proposée est intuitive et efficace pour les tâches de segmentation sémantique d'images médicales avec des données annotées insuffisantes

## Experimental results (in Dice Score) on abdominal images in setting 1.

|  | Abdominal-CT | Abdominal-MRI |
| --- | --- | --- | --- | --- |
| Method | Kidneys LK RK | Spleen Liver Mean | Kidneys LK RK | Spleen Liver Mean |
| ALPNet [23] | 29.12 31.32 41.00 65.07 41.63 44.73 48.42 49.61 62.35 51.28 |
| SSL-PANet [23] | 56.52 50.42 55.72 60.86 57.88 58.83 60.81 61.32 71.73 63.17 |
| SSL-ALPNet [23] 72.36 71.81 70.96 78.29 73.35 81.92 85.18 72.18 76.10 78.84 |
| SSL-RPNet [34] | 65.14 66.73 64.01 72.99 67.22 71.46 81.96 73.55 75.99 75.74 |
| CRAPNet (Ours) | 74.69 74.18 70.37 75.41 73.66 81.95 86.42 74.32 76.46 79.79 |
|  | Abdominal-CT | Abdominal-MRI |
| Method | Kidneys LK RK | Spleen Liver Mean | Kidneys LK RK | Spleen Liver Mean |
| ALPNet-init [23] | 13.90 11.61 16.39 41.71 20.90 19.28 14.93 23.76 37.73 23.93 |
| ALPNet [23] | 34.96 30.40 27.73 47.37 35.11 53.21 58.99 52.18 37.32 50.43 |
| SSL-PANet [23] | 37.58 34.69 43.73 61.71 44.42 47.71 47.95 58.73 64.99 54.85 |
| SSL-ALPNet [23] 63.34 54.82 60.25 73.65 63.02 73.63 78.39 67.02 73.05 73.02 |
| CRAPNet (Ours) | 70.91 67.33 70.17 70.45 69.72 74.66 82.77 70.82 73.82 75.52 |

## . As can be seen, Experiments results (in Dice Score) on the number of Cyc-Resemblance blocks on abdominal MRI in setting 1.

| # of Blocks | LK | RK | Spleen Liver Mean |
| --- | --- | --- | --- |
| 1 | 80.39 82.42 74.52 71.93 77.30 |
| 5 | 81.95 86.42 74.32 76.46 79.79 |
| 7 | 82.08 83.93 73.35 73.16 78.13 |
| 9 | 80.27 83.93 73.61 74.28 78.02 |
| 12 | 82.41 85.84 71.88 73.02 78.29 |
| 15 | 80.71 86.00 73.88 72.67 78.31 |

## Experiments results (in Dice Score) on single branch implementation of attention block on abdominal MRI in setting 1.

|  | Abdominal CT |  |  | Abdominal MRI |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Support | SSF-ALPNet | Proposed | Ground Truth | Support | SSF-ALPNet | Proposed | Ground Truth |
| Left Kidney |  |  |  | Left Kidney |  |  |  |
| Right Kidney |  |  |  | Right Kidney |  |  |  |
| Spleen |  |  |  | Spleen |  |  |  |
| Liver |  |  |  | Liver |  |  |  |

### Formule


$$S = {(I i s , Y i s (l)), l ∈ L test } k i=1$$

### Formule


$$y s = 1 C(x) ∀i f (x q , x i s )g(x i s ),(1)$$

### Formule


$$y q = 1 C(x) ∀i f (x i s , x q )g(x q ),(2)$$

### Formule


$$x i s = f θ (I i s ),(3)$$

### Formule


$$x q = f θ (I q ).(4)$$

### Formule


$$g(x i s ) = W s x i s ,(5) g$$

### Formule


$$(x q ) = W q x q ,(6)$$

### Formule


$$z s = W s y s + x s ,(7)$$

### Formule


$$z q = W q y q + x q ,(8)$$

### Formule


$$A s = x i s (x q ) T ,(9)$$

### Formule


$$A q = x q (x i s ) T .(10)$$

### Formule


$$i * = argmax i A (i,j) .(11)$$

### Formule


$$j * = argmax j A (i * ,j) .(12)$$

### Formule


$$W s = softmax x i s (j) ⊙ x i s (j * ) ,(13)$$

### Formule


$$p (m,n) = r i=-r r j=-r W (h ′ ,w ′ ) (i, j) • z s (h + i, w + j),$$

### Formule


$$p i (l ĵ ) = h w Y i s (l ĵ )x i s (h, w) h w Y i s (l ĵ )(h, w) ,(15)$$

### Formule


$$S l j (h, w) = αp(l j ) ⊙ x q (h, w), (16$$

### Formule


$$)$$

### Formule


$$Y i (l 0 ) = 1 -Y i (l p ).$$

### Formule


$$L t seg (θ; S t , Q t ) = - 1 HW H h W w j∈0,p T g Y t (l j ) (h, w) • log Ŷt (l j )(h, w) ,(18)$$

### Formule


$$L t reg (θ; S ′ t , S t ) = - 1 HW H h W w j∈0,p Y t (l j )(h, w) • log Ȳt (l j )(h, w) .(19)$$

### Formule


$$L t (θ; S t , Q t ) = L t seg + λL t reg ,(20)$$
