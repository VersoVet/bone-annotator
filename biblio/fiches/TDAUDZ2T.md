# Towards annotation-efficient segmentation via image-to-image translation

**Auteurs** : Eugene Vorontsov, Pavlo Molchanov, Matej Gazda, Christopher Beckham, Jan Kautz, Samuel Kadoury
**Année** : 2022
**DOI** : 10.1016/j.media.2022.102624

## Résumé

Often in medical imaging, it is prohibitively challenging to produce enough boundary annotations to train deep neural networks for accurate tumor segmentation. We propose the use of weak labels about whether an image presents tumor or whether it is absent to extend training over images that lack these annotations. Specifically, we propose a semi-supervised framework that employs unpaired image-to-image translation between two domains, presence vs. absence of cancer, as the unsupervised objective. We conjecture that translation helps segmentation-both require the target to be separated from the background. We encode images into two codes: one that is common to both domains and one that is unique to the presence domain. Decoding from the common code yields healthy images; decoding with the addition of the unique code produces a residual change to this image that adds cancer. Translation proceeds from presence to absence and vice versa. In the first case, the tumor is readded to the image and we successfully exploit the residual decoder to also perform segmentation. In the second case, unique codes are sampled, producing a distribution of possible tumors. To validate the method, we created challenging synthetic tasks and tumor segmentation datasets from public BRATS (brain, MRI) and LitS (liver, CT) datasets. We show a clear improvement (0.83 Dice on brain, 0.74 on liver) over baseline semi-supervised training with autoencoding (0.73, 0.66) and a mean teacher approach (0.75, 0.69), demonstrating the ability to generalize from smaller distributions of annotated samples.

## Méthodologie

{'study_design': "Framework semi-supervisé employant la traduction d'image à image non appariée entre deux domaines (présence vs absence de cancer) comme objectif non supervisé, combinée à un objectif de segmentation supervisé sur les cas annotés.", 'intervention': "Encodage des images en deux codes latents : un code commun aux deux domaines et un code unique au domaine 'présence'. Décodage du code commun pour produire une image 'saine' ; décodage avec ajout du code unique pour produire un changement résiduel (additif) ajoutant la tumeur. Le décodeur résiduel est réutilisé pour effectuer la segmentation, avec ajout de connexions de saut longues (long skip connections).", 'control': "Comparaison à trois approches de référence : (1) un modèle encodeur-décodeur entièrement supervisé ('Segmentation only') ; (2) le même modèle en semi-supervisé avec un décodeur additionnel à objectif d'autoencodage ('AE baseline') ; (3) une approche semi-supervisée de type mean teacher ('Mean teacher').", 'primary_outcomes': ['Score de Dice pour la segmentation des tumeurs (cerveau et foie)'], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'Score de Dice - segmentation tumeur cérébrale (BRATS)', 'value': '0.83', 'unit': 'Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'We show a clear improvement (0.83 Dice on brain, 0.74 on liver) over baseline semi-supervised training with autoencoding (0.73, 0.66) and a mean teacher approach (0.75, 0.69)'}, {'outcome': 'Score de Dice - segmentation tumeur hépatique (LitS)', 'value': '0.74', 'unit': 'Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'We show a clear improvement (0.83 Dice on brain, 0.74 on liver) over baseline semi-supervised training with autoencoding (0.73, 0.66) and a mean teacher approach (0.75, 0.69)'}, {'outcome': 'Score de Dice baseline autoencoding - cerveau', 'value': '0.73', 'unit': 'Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'over baseline semi-supervised training with autoencoding (0.73, 0.66)'}, {'outcome': 'Score de Dice baseline autoencoding - foie', 'value': '0.66', 'unit': 'Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'over baseline semi-supervised training with autoencoding (0.73, 0.66)'}, {'outcome': 'Score de Dice baseline mean teacher - cerveau', 'value': '0.75', 'unit': 'Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'and a mean teacher approach (0.75, 0.69)'}, {'outcome': 'Score de Dice baseline mean teacher - foie', 'value': '0.69', 'unit': 'Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'and a mean teacher approach (0.75, 0.69)'}], 'qualitative_findings': [], 'main_findings': ['La méthode proposée surpasse clairement les approches de référence semi-supervisées (autoencoding et mean teacher) sur les tâches de segmentation cérébrale et hépatique.', "La méthode démontre une capacité à généraliser à partir de distributions plus petites d'échantillons annotés."]}

## Conclusions

We propose a semi-supervised segmentation method that makes use of image-to-image translation in order to leverage unsegmented training data with cases presenting the object (P) of interest and cases in which it is absent (A). We argue that this objective is similar to segmentation because they both require disentangling the target object from the background. Indeed, we validate our method on brain tumor segmentation in MR images, liver tumor segmentation in CT images, as well as synthetic segmentation tasks, where we achieve significant improvements over supervised and semi-supervised baselines.

## Segmentation Dice scores for the brain, liver, and synthetic data when annotations are available for only 1% of the data: mean (standard deviation) across three runs.

|  | Brain | Liver | Synthetic | Synthetic | Synthetic |
| --- | --- | --- | --- | --- | --- |
|  | 240×120 | 240×240 | 48×48 simple 48×48 hard | 128×128 |
| Only segmentation | 0.69 (0.04) | 0.66 (0.01) | 0.61 (0.01) | 0.36 (0.01) | 0.15 (0.01) |
| AE baseline | 0.73 (0.04) | 0.66 (0.02) | 0.75 (0.01) | 0.49 (0.02) | 0.57 (0.02) |
| Mean teacher | 0.75 (0.01) | 0.69 (0.02) | 0.83 (0.02) | 0.56 (0.01) | 0.70 (0.01) |
| Proposed | 0.83 (0.01) 0.74 (0.01) | 0.84 (0.00) | 0.60 (0.01) | 0.74 (0.02) |
| Proposed (sep dec) | 0.79 (0.00) | 0.69 (0.02) | 0.83 (0.01) | 0.62 (0.01) | 0.73 (0.02) |

## Ablation experiments on (a) the normalization layers used in the encoder and the decoder of the proposed model ("IN": instance norm, "LN": layer norm, "BN" batch norm

| Normalization | Dice | Translation | Dice |
| --- | --- | --- | --- |
| IN : LN | 0.83 (0.01) | P → A, A → P | 0.83 (0.01) |
| IN : IN | 0.83 (0.01) | P → A | 0.79 (0.02) |
| LN : LN | 0.78 (0.02) | no translation | 0.75 (0.02) |
| BN : BN | 0.80 (0.03) |  |  |
| (a) |  | (b) |  |

### Formule


$$[c A , u A ] = f (x A ), [c P , u P ] = f (x P ).(1)$$

### Formule


$$x PA = g com (c P ),(2)$$

### Formule


$$x PP = x PA + ∆ PA ,$$

### Formule


$$)3$$

### Formule


$$y = g seg (c P , u P ), = (ĝ res • s)(c P , u P ), (4$$

### Formule


$$)$$

### Formule


$$x APA = g com (c AP ), [c AP , u AP ] = f (x AP ).(5)$$

### Formule


$$L total = L seg + λ rec L rec + λ lat L lat + λ cyc L cyc + λ adv L adv .(6)$$

### Formule


$$L seg = Dice(y, ŷ).(7)$$

### Formule


$$L rec = L rec (x P , x PP ) + L rec (x A , x AA ).(8)$$

### Formule


$$[c AP , u AP ] = f (x AP ) [c PA , u PA ] = f (x PA ) [c AA , u AA ] = f (x AA ) [c PP , u PP ] = f (x PP ) L lat = L lat (c A , c AP ) + L lat (c P , c PA ) + L lat (c A , c AA ) + L lat (c P , c PP ) + L lat (u P , u PP ) + L lat (u, u AP ), (9$$

### Formule


$$)$$

### Formule


$$L cyc = L rec (x A , x APA ).(10)$$

### Formule


$$L adv = d∈{A,P } min G max D -E x d ∼p d [min(0, D d (x d ) -1)] -E xd ∼p d [min(0, -D d (G d (x d )) -1)] -E xd ∼p d D d (G d (x d )) ,(11)$$
