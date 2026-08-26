# Iterative Pseudo-Labeling with Deep Feature Annotation and Confidence-Based Sampling

**Auteurs** : Barbara C. Benato, Alexandru C. Telea, Alexandre X. Falcao
**Année** : 2021
**DOI** : 10.1109/sibgrapi54419.2021.00034

## Résumé

Training deep neural networks is challenging when large and annotated datasets are unavailable. Extensive manual annotation of data samples is time-consuming, expensive, and error-prone, notably when it needs to be done by experts. To address this issue, increased attention has been devoted to techniques that propagate uncertain labels (also called pseudo labels) to large amounts of unsupervised samples and use them for training the model. However, these techniques still need hundreds of supervised samples per class in the training set and a validation set with extra supervised samples to tune the model. We improve a recent iterative pseudo-labeling technique, Deep Feature Annotation (DeepFA), by selecting the most confident unsupervised samples to iteratively train a deep neural network. Our confidence-based sampling strategy relies on only dozens of annotated training samples per class with no validation set, considerably reducing user effort in data annotation. We first ascertain the best configuration for the baseline -a self-trained deep neural network -and then evaluate our confidence DeepFA for different confidence thresholds. Experiments on six datasets show that DeepFA already outperforms the self-trained baseline, but confidence DeepFA can considerably outperform the original DeepFA and the baseline.

## Méthodologie

{'study_design': "Approche itérative de pseudo-étiquetage semi-supervisé combinant un réseau de neurones profond primaire (VGG-16) et un modèle auxiliaire (projection t-SNE + classifieur semi-supervisé Optimum-Path Forest, OPFSemi) pour propager les labels aux échantillons non supervisés, avec une stratégie d'échantillonnage basée sur la confiance pour sélectionner les échantillons les plus fiables à chaque itération", 'intervention': 'Confidence DeepFA (conf-DeepFA) : sélection des échantillons non supervisés les plus confiants (selon différents seuils τ fixes de 0.7, 0.8, 0.9 et un seuil adaptatif τ = α) pour ré-entraîner itérativement le modèle primaire', 'control': 'Baseline self-trained VGG-16 (feature extraction et fine-tuning) et DeepFA original (propagation à tous les échantillons non supervisés sans filtrage par confiance)', 'primary_outcomes': ['Précision de propagation des pseudo-labels (propagation accuracy)', 'Précision de classification', 'Coefficient Kappa (κ)'], 'secondary_outcomes': ["Courbes d'apprentissage (perte et précision) sur les ensembles d'entraînement et de validation"], 'statistical_methods': ['Moyenne et écart-type sur trois splits différents', 'Comparaison de la précision de propagation et du κ entre méthodes et itérations'], 'duration': "Cinq itérations d'entraînement/pseudo-étiquetage", 'setting': "Expérimentation sur six jeux de données d'images avec VGG-16 pré-entraîné sur ImageNet"}

## Résultats

{'quantitative': [{'outcome': 'Amélioration de précision et κ avec feature extraction vs résultats de [20]', 'value': '20', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': "In general, VGG's feature extraction results show an increase of almost 20% in accuracy and κ for most datasets."}, {'outcome': 'Gain de κ et précision de propagation de conf-DeepFA vs DeepFA pour les datasets les plus difficiles', 'value': '5', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'However, we see a gain of almost 5% in κ and propagation accuracy for the most challenging datasets.'}, {'outcome': 'Gain de κ pour P.cysts avec impuretés', 'value': '>10', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'For P.cysts with impurities, the gain is actually higher than 10% in κ and 17% in propagation accuracy -for which DeepFA obtained worse results than VGG-16.'}, {'outcome': 'Gain de précision de propagation pour P.cysts avec impuretés', 'value': '17', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'For P.cysts with impurities, the gain is actually higher than 10% in κ and 17% in propagation accuracy -for which DeepFA obtained worse results than VGG-16.'}], 'qualitative_findings': ['Le choix optimal du seuil de confiance τ dépend du jeu de données et de sa difficulté', "Le dataset P.cysts avec impuretés est le plus difficile (sept classes, plus d'échantillons, presque 60% d'impuretés) et n'a pas été amélioré par l'échantillonnage basé sur la confiance"], 'main_findings': ['DeepFA surpasse déjà la baseline auto-entraînée', 'conf-DeepFA surpasse considérablement le DeepFA original et la baseline', "L'extraction de caractéristiques (feature extraction) donne de meilleurs résultats que le fine-tuning pour VGG-16 avec peu d'échantillons supervisés", 'Pour τ = 0.8, MNIST, H.larvae et P.cysts obtiennent les meilleurs résultats ; pour H.eggs sans impuretés, τ = 0.7 est meilleur ; pour P.cysts sans impuretés, τ = 0.9 et le seuil adaptatif τ = α donnent des résultats similaires et optimaux', 'Les résultats de κ et de précision de propagation diminuent légèrement après la troisième itération, suggérant une saturation de la méthode']}

## Conclusions

VGG-16 utilisé uniquement pour l'extraction de caractéristiques (sans fine-tuning) améliore la précision et le κ avec peu d'échantillons supervisés La stratégie d'échantillonnage basée sur la confiance appliquée à OPFSemi améliore la précision de propagation et le κ pour la plupart des jeux de données évalués Le gain apporté par certains seuils de confiance τ dépend du jeu de données, ce qui suggère une dépendance au contexte Les auteurs prévoient d'intégrer la connaissance de l'utilisateur pour un pseudo-étiquetage semi-automatique, et d'explorer davantage de jeux de données ainsi que d'autres stratégies semi-supervisées récentes

## TABLE I THREE

| dataset | class | # samples |
| --- | --- | --- |
| (i) Helminth larvae (2 classes) | S.stercoralis impurities total | 446 3068 3,514 |
|  | H.nana | 348 |
|  | H.diminuta | 80 |
|  | Ancilostomideo | 148 |
|  | E.vermicularis | 122 |
| (ii) Helminth eggs | A.lumbricoides | 337 |
| (9 classes) | T.trichiura | 375 |
|  | S.mansoni | 122 |
|  | Taenia | 236 |
|  | impurities | 3,444 |
|  | total | 5,112 |
|  | E.coli | 719 |
|  | E.histolytica | 78 |
|  | E.nana | 724 |
| (iii) Protozoan cysts | Giardia | 641 |
| (7 classes) | I.butschlii | 1,501 |
|  | B.hominis | 189 |
|  | impurities | 5,716 |
|  | total | 9,568 |

## OF SUPERVISED SAMPLES IN S FOR EACH CHOSEN DATASET.

|  | MNIST | H.eggs (w/o imp) | P. cysts (w/o imp) | H. larvae | H. eggs | P. cysts |
| --- | --- | --- | --- | --- | --- | --- |
| S | 50 | 17 | 38 | 35 | 51 | 95 |
| U | 3450 | 1220 | 2658 | 2424 | 3527 | 6602 |

## VGG-16 is trained on S. Deep features for S∪U from the last convolutional layer are projected in 2D with t-SNE, and used next for OPFSemi pseudo labeling from S to all samples in U . OPFSemi's pseudolabels are used to retrain VGG-16, and the network is tested on T (one iteration of DeepFA looping out of five); • conf-DeepFA τ =x : VGG-16 is trained on S. Deep features for S ∪ U from the last convolutional layer are projected in 2D with t-SNE, and used for OPFSemi pseudo labeling from S to U τ , for samples with confidence above τ = x. to U τ for samples with confidence above τ . τ is increased from 0.8 to 0.96 by 0.4 in each conf-DeepFA looping iteration. OPFSemi's pseudolabels are used to retrain VGG-16, and the network is tested on T . The looping has five iterations.

| We choose x = {0.7, 0.8, 0.9}. OPFSemi's pseudolabels |
| --- |

## FOR VGG-16 CONSIDERING FEATURE EXTRACTION AND FINE-TUNING. BEST VALUES PER METRIC AND DATASET IN BOLD.

| dataset | metric | VGG-16 f t | self-VGG-16 f t | VGG-16 f e | self-VGG-16 f e |
| --- | --- | --- | --- | --- | --- |
|  | acc | - | 0.447238 ± 0.146 | - | 0.586000 ± 0.007 |
| MNIST | acc | 0.629555 ± 0.037 | 0.441334 ± 0.149 | 0.614444 ± 0.015 | 0.592222 ± 0.020 |
|  | kappa | 0.588195 ± 0.041 | 0.378648 ± 0.166 | 0.571176 ± 0.017 | 0.546162 ± 0.023 |
| H.eggs (w/o imp) | prop. acc acc kappa | -0.790961 ± 0.050 0.752807 ± 0.060 | 0.758825 ± 0.088 0.779033 ± 0.095 0.735591 ± 0.113 | -0.738858 ± 0.054 0.693278 ± 0.060 | 0.744004 ± 0.114 0.774011 ± 0.131 0.734030 ± 0.153 |
| P.cysts (w/o imp) | prop. acc acc kappa | -0.561130 ± 0.093 0.324051 ± 0.175 | 0.399481 ± 0.010 0.400519 ± 0.011 0.020734 ± 0.021 | -0.736159 ± 0.027 0.626632 ± 0.039 | 0.648739 ± 0.111 0.650230 ± 0.101 0.483706 ± 0.170 |
|  | prop. acc | - | 0.897384 ± 0.031 | - | 0.912837 ± 0.038 |
| H.larvae | acc | 0.874566 ± 0.001 | 0.886572 ± 0.017 | 0.893523 ± 0.017 | 0.908689 ± 0.040 |
|  | kappa | 0.021406 ± 0.019 | 0.174158 ± 0.208 | 0.256836 ± 0.203 | 0.385892 ± 0.402 |
|  | prop. acc | - | 0.773803 ± 0.034 | - | 0.847308 ± 0.018 |
| H.eggs | acc | 0.858323 ± 0.013 | 0.775750 ± 0.034 | 0.848327 ± 0.017 | 0.850934 ± 0.014 |
|  | kappa | 0.734333 ± 0.019 | 0.519971 ± 0.114 | 0.713649 ± 0.030 | 0.714227 ± 0.038 |
|  | prop. acc | - | 0.730327 ± 0.022 | - | 0.817978 ± 0.004 |
| P.cysts | acc | 0.758853 ± 0.077 | 0.734239 ± 0.028 | 0.818182 ± 0.004 | 0.824800 ± 0.011 |
|  | kappa | 0.542967 ± 0.218 | 0.492070 ± 0.107 | 0.697633 ± 0.009 | 0.705397 ± 0.022 |

## FROM THE LAST ITERATION FOR PROPOSED EXPERIMENTS WITH FULLY LABEL PROPAGATION (DeepFA), AND CONFIDENCE-BASED LABEL PROPAGATION (conf-DeepFA) WITH CONFIDENCE HIGHER THAN τ = 0.7, CONFIDENCE HIGHER THAN τ = 0.8, CONFIDENCE HIGHER THAN τ = 0.9, AND ADAPTATIVE CONFIDENCE (FROM 0.80 TO 0.96 OVER 5 ITERATIONS). BEST VALUES PER DATASET IN BOLD.

| dataset | metric | DeepFA | conf-DeepFAτ=0.7 | conf-DeepFA τ =0.8 | conf-DeepFA τ =0.9 | conf-DeepFA τ =α |
| --- | --- | --- | --- | --- | --- | --- |
|  | prop. acc | 0.790000 ± 0.047 | 0.782286 ± 0.029 | 0.821714 ± 0.018 | 0.750000 ± 0.028 | 0.795429 ± 0.007 |
| MNIST | acc | 0.797778 ± 0.049 | 0.788000 ± 0.030 | 0.822666 ± 0.022 | 0.740222 ± 0.032 | 0.651778 ± 0.062 |
|  | kappa | 0.775103 ± 0.054 | 0.764348 ± 0.034 | 0.802863 ± 0.024 | 0.710961 ± 0.036 | 0.612766 ± 0.069 |
| H.eggs (w/o imp) | prop. acc acc kappa | 0.983293 ± 0.004 0.790961 ± 0.050 0.752807 ± 0.060 | 0.983832 ± 0.002 0.973007 ± 0.006 0.968042 ± 0.007 | 0.974401 ± 0.020 0.971123 ± 0.013 0.965848 ± 0.015 | 0.981945 ± 0.003 0.938481 ± 0.056 0.927708 ± 0.066 | 0.983832 ± 0.004 0.806654 ± 0.126 0.771216 ± 0.148 |
| P.cysts (w/o imp) | prop. acc acc kappa | 0.800569 ± 0.035 0.819493 ± 0.041 0.756949 ± 0.054 | 0.805143 ± 0.049 0.826413 ± 0.039 0.764035 ± 0.052 | 0.793274 ± 0.069 0.814590 ± 0.060 0.747127 ± 0.086 | 0.824060 ± 0.019 0.842561 ± 0.004 0.785441 ± 0.006 | 0.828141 ± 0.012 0.824394 ± 0.033 0.762919 ± 0.041 |
|  | prop. acc | 0.954182 ± 0.008 | 0.964213 ± 0.017 | 0.964349 ± 0.012 | 0.941846 ± 0.039 | 0.951471 ± 0.014 |
| H.larvae | acc | 0.955450 ± 0.002 | 0.959558 ± 0.015 | 0.965561 ± 0.004 | 0.958926 ± 0.014 | 0.943128 ± 0.010 |
|  | kappa | 0.789743 ± 0.010 | 0.800052 ± 0.099 | 0.837948 ± 0.029 | 0.804689 ± 0.082 | 0.705475 ± 0.069 |
|  | prop. acc | 0.936743 ± 0.011 | 0.936091 ± 0.005 | 0.937209 ± 0.008 | 0.931806 ± 0.007 | 0.930967 ± 0.006 |
| H.eggs | acc | 0.942634 ± 0.016 | 0.943938 ± 0.003 | 0.942634 ± 0.009 | 0.908518 ± 0.022 | 0.853107 ± 0.025 |
|  | kappa | 0.899307 ± 0.027 | 0.901604 ± 0.006 | 0.898922 ± 0.015 | 0.831488 ± 0.043 | 0.719695 ± 0.054 |
|  | prop. acc | 0.732716 ± 0.056 | 0.769748 ± 0.026 | 0.780300 ± 0.018 | 0.748843 ± 0.048 | 0.744811 ± 0.068 |
| P.cysts | acc | 0.740973 ± 0.056 | 0.792755 ± 0.027 | 0.816905 ± 0.027 | 0.818066 ± 0.022 | 0.731104 ± 0.082 |
|  | kappa | 0.580626 ± 0.092 | 0.652254 ± 0.051 | 0.699603 ± 0.054 | 0.689325 ± 0.039 | 0.450283 ± 0.243 |

### Formule


$$V (u) = C /(C(u) + C ) ∈ [0, 1] is assigned to the unsupervised sample u. Higher is C more confident OPFSemi is that L(u) is λ(s).$$
