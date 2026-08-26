# ActiveLab: Active Learning with Re-Labeling by Multiple Annotators

**Auteurs** : Hui Wen Goh, Jonas Mueller
**Année** : 2023
**DOI** : 10.48550/arxiv.2301.11856

## Résumé

In real-world data labeling applications, annotators often provide imperfect labels. It is thus common to employ multiple annotators to label data with some overlap between their examples. We study active learning in such settings, aiming to train an accurate classifier by collecting a dataset with the fewest total annotations. Here we propose ActiveLab, a practical method to decide what to label next that works with any classifier model and can be used in pool-based batch active learning with one or multiple annotators. ActiveLab automatically estimates when it is more informative to re-label examples vs. labeling entirely new ones. This is a key aspect of producing high quality labels and trained models within a limited annotation budget. In experiments on image and tabular data, ActiveLab reliably trains more accurate classifiers with far fewer annotations than a wide variety of popular active learning methods.

## Méthodologie

{'study_design': "Comparaison expérimentale de méthodes model/modality-agnostic pour l'apprentissage actif pool-based avec annotateurs multiples ; chaque méthode sélectionne itérativement quels exemples labelliser via un score s_i différent, et les labels consensus pour tous les x_i sont calculés par vote majoritaire (Zheng et al., 2010)", 'intervention': 'ActiveLab : méthode qui estime quand ré-labelliser un exemple déjà annoté est plus informatif que labelliser un nouvel exemple', 'control': 'Méthodes de référence : Random, Good Random, Entropy (Cohn et al., 1996), Uncertainty (Cohn et al., 1996), Active Label Cleaning (Bernhardt et al., 2022), Disagreement/Ensemble (Seung et al., 1992)', 'primary_outcomes': ["Précision du classifieur entraîné en fonction du nombre total d'annotations collectées"], 'secondary_outcomes': [], 'statistical_methods': ['Vote majoritaire pour le calcul des labels consensus (Zheng et al., 2010)', 'Entropie des probabilités prédites par le modèle', 'Cross-entropie entre distributions de probabilités prédites et distribution empirique des labels des annotateurs (Bernhardt et al., 2022)', "Cross-entropie douce (soft cross entropy) entre prédictions des modèles individuels et estimation moyenne de l'ensemble (McCallum et al., 1998)"], 'duration': None, 'setting': "Données image et tabulaires (expériences mentionnées dans l'abstract, non détaillées dans les sections fournies)"}

## Résultats

{'quantitative': [], 'qualitative_findings': ["ActiveLab significantly outperforme les autres méthodes d'active learning, à la fois dans le cadre à modèle unique et dans le cadre ensembliste, comme illustré par les Figures 1, 2 et S1", "L'active learning avec des modèles d'ensemble produit une meilleure précision que celle obtenue avec des modèles uniques", "La précision d'un modèle unique lorsque les données sont collectées avec ActiveLab peut atteindre une performance comparable aux modèles d'ensemble, en particulier pour des modèles uniques performants comme dans la Figure 1", "ActiveLab est aussi la meilleure méthode pour le nettoyage actif des labels (re-labeling d'un dataset déjà labellisé), comme montré en Figure 3", 'ActiveLab surpasse la méthode de Bernhardt et al. (2022), spécifiquement conçue pour ce cadre de nettoyage de labels', "Contrairement à Bernhardt et al. (2022), les estimations d'ActiveLab tiennent compte du nombre d'annotations de chaque exemple et de la qualité des annotateurs à l'origine de ces annotations", "Les méthodes d'active learning existantes ne semblent pas adaptées à ce type de tâches de nettoyage de labels"], 'main_findings': ["ActiveLab surpasse significativement les autres méthodes d'active learning pour sélectionner des exemples à labelliser et re-labelliser, sur des données de modalités variées et avec différents types de classifieurs", "ActiveLab est la meilleure méthode pour l'active label cleaning, surpassant même une méthode conçue spécifiquement pour cette tâche (Bernhardt et al., 2022)"]}

## We have high-quality (i.e. ground truth) labels for the test set, which facilitates accurate evalu-Figure 1. Evaluating active learning methods on the Wall Robot dataset to train an: ExtraTrees classifier (left) or ensemble of 3 models (right). Curves show test accuracy after each active learning iteration, averaged over 5 runs with the standard deviation in results shaded.

|  |  | Model Accuracy of Single-Model Methods | Model Accuracy of Ensemble Methods |
| --- | --- | --- | --- | --- | --- | --- |
|  | 0.98 |  |  |  | 0.98 |
|  |  |  |  |  | 0.97 |
| Model Accuracy | 0.94 0.96 |  |  | Model Accuracy | 0.94 0.95 0.96 |
|  | 0.92 |  |  |  | 0.93 |
|  | 0.90 | 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 Iteration | 0.92 | Iteration 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 |
|  |  | Random Good Random | Entropy Uncertainty | ActiveLab | Disagrement (ensemble) | ActiveLab (ensemble) |

## Robot Complete. Similar to the Wall Robot Navigation tabular dataset, a key difference is that Wall Robot Complete has 2000 labeled examples in the initial training set, 1000 examples in the test set, and there is no unlabeled pool. As for Wall Robot Navigation, we collect additional labels for the 100 examples with the lowest active learning scores in each active learning round. Since all the examples already start out with some labels, this is a re-labeling (i.e. label cleaning) task, where we aim to obtain accurate consensus labels by having multiple annotators review the examples where this is necessary

|  |  | Model Accuracy of Single-Model Methods |  | Model Accuracy of Ensemble Methods |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0.85 |  |  |  |  |
|  | 0.80 |  |  |  |  | 0.925 |
| Model Accuracy | 0.50 0.55 0.60 0.65 0.70 0.75 | 0 1 2 3 4 5 6 7 8 9 10 11 12 Iteration | Model Accuracy | 0.775 0.800 0.900 0.825 0.850 0.875 | Iteration 0 1 2 3 4 5 6 7 8 9 10 11 12 |
|  |  | Random Good Random | Entropy Uncertainty | ActiveLab |  | Disagrement (ensemble) | ActiveLab (ensemble) |

## Thus we empirically investigate the question: At what degree of annotation-noise is there value in re-labeling when the size of U greatly exceeds our labeling budget?We consider two settings: one where we only label new examples in each active learning round (single label case), and another where we can re-label examples if ActiveLab chooses to do so (multiannotator label case). We run these approaches on a few variants of the Wall Robot Navigation dataset where we simulate annotators with different label noise rates. A higher noise rate annotator produces labels which are often wrong, while an annotator with noise rate 0 always selects labels that are correct. Similar to our previous Wall Robot benchmark, we conduct this experiment with an initial train set of 500 labeled examples, an unlabeled pool of 1500 examples, and test set of 1000 well-labeled examples. We label batches of 100 examples in each active learning round. Both single label and multiannotator label experiments start with the same labeled subset D (and always have the same annotator noise rates). In the single label experiment, active learning is done using the traditional entropy score only considering examples in U. In the multiannotator label experiment, active learning is done via ActiveLab, which often selects a mixture of examples from D and U to collect an additional label for. Figure 3. Evaluating active learning methods on the Wall Robot Complete dataset to train an: ExtraTrees classifier (left) or ensemble of 3 models (right). Curves show test accuracy after each iteration of re-labeling, averaged over 5 runs with the standard deviation shaded.

|  |  | Model Accuracy of Single-Model Methods | Model Accuracy of Ensemble Methods |
| --- | --- | --- | --- | --- | --- | --- |
|  | 0.98 |  |  |  | 0.980 |
|  |  |  |  |  | 0.975 |
| Model Accuracy | 0.94 0.96 |  |  | Model Accuracy | 0.960 0.965 0.970 |
|  | 0.92 |  |  |  | 0.955 |
|  |  |  |  |  | 0.950 |
|  | 0.90 | 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 Iteration | 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 Iteration |
|  |  | Random Good Random | Entropy Uncertainty | ActiveLab Active Label Cleaning | Disagrement (ensemble) | ActiveLab (ensemble) |
|  |  |  |  | Figure 4 reveals that across all annotator noise levels, the |

## Future work might seek to achieve further robustness by filtering bad annotators (e.g. based on their weights w j ) and data/labels from the training set D of each active learning round.

| on model predictions to infer what data is most |
| --- |
| informative, model-agnostic active learning methods will |
| improve automatically as supervised learning architectures |
| and training procedures continue to advance. More sophisti- |
| cated active learning methods designed for specific models |
| or training procedures will not enjoy these benefits and |
| may become irrelevant if incompatible with tomorrow's |
| state-of-the-art models. Unlike traditional model-agnostic |
| active learning that solely relies on model predictions to |
| determine which examples to label next, ActiveLab consid- |
| ers re-labeling examples x i ∈ D and estimates the value |
| of this based on additional information like the: number of |
| available annotations for x i , disagreement amongst these an- |
| notations, and relative trustworthiness of the trained model |
| vs. the annotators. Re-labeling facilitates more robust model |
| training when data annotators are imperfect. |

### Formule


$$x i ∈ D, with Y ij = ∅ if annotator A j did not label example i. Y i is the set of collected labels for example x i , with |Y i | = 0 if x i ∈ U. I j is the subset$$

### Formule


$$If x i ∈ D :$$

### Formule


$$s i = w M • p M,i, Yi + w Ā • 1 K + j∈Ji w j • p Aj ,i, Yi w M + w Ā + j∈Ji w j If x i ∈ U : s i = w M • max k p M,i,k + w Ā • 1 K w M + w Ā (2)$$

### Formule


$$w M p M,i,k * -p M,i,Yij > w j p Aj ,i,Yij -p Aj ,i,k *$$

### Formule


$$p Aj ,i,k ≈ p(Y i = k | Y ij ) := P when Y ij = k 1-P K-1$$

### Formule


$$w j := 1 - 1 -g j 1 -A MLC w M := 1 - 1 -A M 1 -A MLC • 1 n i∈D |J i |$$

### Formule


$$g j := i∈Ij ∈Ji, =j 1(Y ij = Y i ) i∈Ij (|J i | -1)$$

### Formule


$$A M := 1 |I + | i∈I+ 1 Y i = arg max k p M,i,k(3)$$

### Formule


$$A MLC := 1 |I + | i∈I+ 1(Y MLC = Y i )(4)$$

### Formule


$$I + := {i ∈ D : |J i | > 1}.$$

### Formule


$$i∈D K k=1 p emp (Y i = k | {Y ij } j∈Ji ) • log p (T ) M,i,k$$

### Formule


$$(T ) M,i,k = σ p M,i,k T for softmax σ(z k ) = e z k$$

### Formule


$$If x i ∈ D :$$

### Formule


$$s i = w Ā • 1 K + L =1 w M • p M ,i, Yi + j∈Ji w j • p Aj ,i, Yi w Ā + L =1 w M + j∈Ji w j If x i ∈ U : s i = w Ā • 1 K + L =1 w M • p M ,i, Yi w Ā + L =1 w M (6)$$

### Formule


$$w M := 1 - 1 -A M 1 -A MLC • 1 n i |J i |$$

### Formule


$$s i = x + |Y i | where x ∈ [0, 1]$$

### Formule


$$s i = K k=1 p M,i,k • log p M,i,k(7)$$

### Formule


$$s i = max k p M,i,k .$$

### Formule


$$s i = K k=1 p M,i,k • log p M,i,k(8)$$

### Formule


$$- K k=1 p emp (Y i = k | {Y ij } j∈Ji ) • log p M,i,k$$

### Formule


$$s i = - 1 L L =1 K k=1 p M ,i,k • p M,i,k(9)$$

### Formule


$$p M,i,k = 1 L L =1 p M ,i,k$$

### Formule


$$Wall$$

### Formule


$$s i = max k p M,i,k + 1 K 2 for x i ∈ U(10)$$
