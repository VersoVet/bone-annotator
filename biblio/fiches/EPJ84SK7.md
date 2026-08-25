# Context-guided fully convolutional networks for joint craniomaxillofacial bone segmentation and landmark digitization

**Auteurs** : Jun Zhang, Mingxia Liu, Li Wang, Si Chen, Peng Yuan, Jianfu Li, Steve Guo-Fang Shen, Zhen Tang, Ken-Chung Chen, James J. Xia, Dinggang Shen
**Année** : 2020
**DOI** : 10.1016/j.media.2019.101621

## Résumé

Inspecting a 3D object which shape has elastic manufacturing tolerances in order to find defects is a challenging and time-consuming task. This task usually involves humans, either in the specification stage followed by some automatic measurements, or in other points along the process. Even when a detailed inspection is performed, the measurements are limited to a few dimensions instead of a complete examination of the object. In this work, a probabilistic method to evaluate 3D surfaces is presented. This algorithm relies on a training stage to learn the shape of the object building a statistical shape model. Making use of this model, any inspected object can be evaluated obtaining a probability that the whole object or any of its dimensions are compatible with the model, thus allowing to easily find defective objects. Results in simulated and real environments are presented and compared to two different alternatives.

## Méthodologie

{'study_design': "Étude comparative entre l'algorithme proposé (basé sur un Statistical Shape Model, SSM) et deux méthodes d'évaluation industrielles alternatives couramment utilisées ; deux variantes de l'algorithme SSM sont également considérées : l'une utilisant uniquement l'information des points 3D (SSM-Points), l'autre incluant en plus le vecteur normal (SSM)", 'intervention': 'Évaluation de chaque surface avec les trois algorithmes (méthode SSM proposée et deux méthodes alternatives), incluant les deux variantes SSM-Points et SSM', 'control': "Les deux méthodes d'évaluation industrielles alternatives couramment utilisées, servant de comparaison à l'algorithme SSM proposé", 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': "Reconstruction 3D à partir de silhouettes multiples et modèles 3D acquis avec un dispositif breveté ZG3D, dans un contexte d'inspection industrielle de production"}

## Résultats

{'quantitative': [{'outcome': 'Détection des objets défectueux (méthode proposée SSM)', 'value': 'virtually 100%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': 'It is capable of virtually 100% detection of defective objects accepting 93.15% of the non-defective objects'}, {'outcome': 'Acceptation des objets non-défectueux (méthode proposée SSM)', 'value': '93.15', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': 'It is capable of virtually 100% detection of defective objects accepting 93.15% of the non-defective objects'}, {'outcome': 'Acceptation des objets non-défectueux (méthode kernel-hull)', 'value': '64.38', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': 'while the kernel-hull method just accepts 64.38%'}, {'outcome': "Nombre de répétitions d'inspection par objet", 'value': '25', 'unit': 'répétitions', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'Each of the objects has been inspected 25 times, so the variability of the device is also modelled during the process.'}], 'qualitative_findings': ['La méthode SSM proposée surpasse les alternatives (kernel-hull, C2C, SSM avec position uniquement) même lorsque les tolérances sont faibles et les déformations rigides, un scénario où les performances devraient théoriquement être similaires.', "Le SSM utilisant uniquement l'information de position montre une performance inférieure, et les résultats de C2C sont nettement en retrait par rapport aux autres algorithmes.", "Le jeu de données réel a été sélectionné avec une proportion d'objets défectueux plus élevée que la normale et des erreurs très proches de la limite d'acceptation, ce qui produit des résultats plus sévères que dans un processus industriel réel.", "Sur un objet avec un manque de matière trop fin, le kernel-hull échoue à détecter l'erreur (car dans la variabilité des objets de référence) alors que le SSM la détecte correctement grâce à l'information des vecteurs normaux locaux, bien que la position 3D soit jugée correcte.", "Sur un objet correct présentant des bosses (bulges) synthétiques inhabituellement grandes dues à la reconstruction 3D par silhouette, le SSM détecte incorrectement une erreur (faux positif) car ces bosses ne suivent pas une distribution gaussienne et n'ont pas été apprises pendant l'entraînement.", 'Le kernel-hull, suivant une stratégie maximum-minimum qui ignore la distribution statistique, ne détecte pas ces bosses comme erronées dans ce même cas.', "La disponibilité d'informations statistiques locales sur les positions des points et leurs vecteurs normaux à la surface est déterminante pour l'avantage de la méthode proposée.", "Bien que la comparaison kernel-hull soit légèrement meilleure dans certaines zones de fonctionnement de la courbe ROC, l'évaluation basée sur le modèle de forme statistique (SSM) est significativement meilleure pour détecter tous les échantillons défectueux à un taux de vrais positifs plus élevé, ce qui constitue le point de fonctionnement souhaité pour l'inspection industrielle."], 'main_findings': ["La méthode SSM proposée est significativement meilleure que les alternatives dans la plage la plus importante de la courbe ROC pour les opérations d'inspection industrielle.", 'La méthode proposée atteint une détection quasi-totale (100%) des objets défectueux tout en acceptant 93.15% des objets non-défectueux, contre seulement 64.38% pour le kernel-hull.', "L'utilisation d'informations locales (position et normales) permet au SSM d'apprendre la variabilité à un niveau fin, ce qui lui donne un avantage même dans des cas difficiles avec de faibles tolérances et des déformations rigides.", "Les limites de la méthode SSM concernent les cas d'outliers non gaussiens (bosses synthétiques dues à la reconstruction 3D), qui génèrent des faux positifs; une piste d'amélioration future consiste à combiner l'information de distribution des caméras avec les gaussiennes estimées par le SSM."]}

## Conclusions

A probabilistic method for training models and evaluating 3D surfaces with elastic manufacturing tolerances has been presented The training process makes use of correct objects to infer a model shape with variability, making possible to measure distances with the learned Statistical Shape Model (SSM) The evaluation relies on the SSM to analyse the 3D reconstructed object establishing a metric for each point against this model, and may be filtered against outliers to determine whether the inspected object is correct or not The proposed method has been compared with other alternatives in simulated and real environments using a ZG3D device, outperforming them for the industrial inspection use case The SSM based algorithm proved to be capable to work with rigid as well as elastic manufacturing tolerances, obtaining better results than the alternative algorithms in both cases

### Formule


$$SI p = ∑ q∈N p SI q D q ∑ q∈N p D q . (1$$

### Formule


$$)$$

### Formule


$$D M ( x) = ( x -µ) T S -1 ( x -µ).$$

### Formule


$$)2$$
