# Towards annotation-efficient segmentation via image-to-image translation

**Auteurs** : Eugene Vorontsov, Pavlo Molchanov, Matej Gazda, Christopher Beckham, Jan Kautz, Samuel Kadoury
**Année** : 2022
**DOI** : 10.1016/j.media.2022.102624

## Résumé

Often in medical imaging, it is prohibitively challenging to produce enough boundary annotations to train deep neural networks for accurate tumor segmentation. We propose the use of weak labels about whether an image presents tumor or whether it is absent to extend training over images that lack these annotations. Specifically, we propose a semi-supervised framework that employs unpaired image-to-image translation between two domains, presence vs. absence of cancer, as the unsupervised objective. We conjecture that translation helps segmentation-both require the target to be separated from the background. We encode images into two codes: one that is common to both domains and one that is unique to the presence domain. Decoding from the common code yields healthy images; decoding with the addition of the unique code produces a residual change to this image that adds cancer. Translation proceeds from presence to absence and vice versa. In the first case, the tumor is readded to the image and we successfully exploit the residual decoder to also perform segmentation. In the second case, unique codes are sampled, producing a distribution of possible tumors. To validate the method, we created challenging synthetic tasks and tumor segmentation datasets from public BRATS (brain, MRI) and LitS (liver, CT) datasets. We show a clear improvement (0.83 Dice on brain, 0.74 on liver) over baseline semi-supervised training with autoencoding (0.73, 0.66) and a mean teacher approach (0.75, 0.69), demonstrating the ability to generalize from smaller distributions of annotated samples.

## Méthodologie

{'study_design': "Framework semi-supervisé s'appuyant sur la traduction d'image à image (unpaired image-to-image translation) entre deux domaines (présence vs absence de cancer) comme objectif non supervisé. Les images sont encodées en deux codes latents : un code commun aux deux domaines et un code unique au domaine 'présence'. Le décodage du code commun produit une image saine ; l'ajout du code unique produit un changement résiduel ajoutant la tumeur. Le décodeur résiduel est réutilisé pour effectuer la segmentation.", 'intervention': 'Méthode proposée : traduction adversariale image-à-image avec un encodeur et deux décodeurs (commun et résiduel), incluant de nouvelles connexions de saut longues (long skip connections).', 'control': "Trois approches de référence (baselines) : (1) modèle encodeur-décodeur entièrement supervisé ('Segmentation only') ; (2) modèle semi-supervisé avec objectif d'autoencodage additionnel ('AE baseline') ; (3) approche semi-supervisée 'mean teacher' [21].", 'primary_outcomes': ['Score de segmentation (Dice) sur les tâches de segmentation de tumeur cérébrale (BRATS) et hépatique (LitS)'], 'secondary_outcomes': ['Performance sur des tâches de segmentation synthétiques'], 'statistical_methods': [], 'duration': None, 'setting': "Étude méthodologique/computationnelle utilisant des jeux de données publics d'imagerie médicale"}

## Résultats

{'quantitative': [{'outcome': 'Score Dice - segmentation tumeur cérébrale (BRATS, méthode proposée)', 'value': '0.83', 'unit': 'Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'We show a clear improvement (0.83 Dice on brain, 0.74 on liver) over baseline semi-supervised training with autoencoding (0.73, 0.66) and a mean teacher approach (0.75, 0.69)'}, {'outcome': 'Score Dice - segmentation tumeur hépatique (LitS, méthode proposée)', 'value': '0.74', 'unit': 'Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'We show a clear improvement (0.83 Dice on brain, 0.74 on liver) over baseline semi-supervised training with autoencoding (0.73, 0.66) and a mean teacher approach (0.75, 0.69)'}, {'outcome': 'Score Dice - AE baseline (autoencoding), brain / liver', 'value': '0.73 / 0.66', 'unit': 'Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'over baseline semi-supervised training with autoencoding (0.73, 0.66)'}, {'outcome': 'Score Dice - Mean teacher baseline, brain / liver', 'value': '0.75 / 0.69', 'unit': 'Dice', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'and a mean teacher approach (0.75, 0.69)'}], 'qualitative_findings': [], 'main_findings': ['La méthode proposée améliore clairement la segmentation par rapport aux baselines semi-supervisées (autoencodage et mean teacher) sur les tâches cérébrale et hépatique.', "La méthode démontre une capacité à généraliser à partir de distributions plus petites d'échantillons annotés."]}

## Conclusions

Une méthode de segmentation semi-supervisée exploitant la traduction image-à-image permet de tirer parti de données d'entraînement non segmentées (cas avec présence vs absence de l'objet d'intérêt). Cet objectif de traduction est similaire à la segmentation car les deux nécessitent de séparer l'objet cible de l'arrière-plan. La méthode a été validée sur la segmentation de tumeurs cérébrales (IRM), la segmentation de tumeurs hépatiques (CT), ainsi que sur des tâches de segmentation synthétiques, avec des améliorations significatives par rapport aux baselines supervisées et semi-supervisées.

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
