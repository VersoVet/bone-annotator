# Segment anything model for medical image analysis: An experimental study

**Auteurs** : Maciej A. Mazurowski, Haoyu Dong, Hanxue Gu, Jichen Yang, Nicholas Konz, Yixin Zhang
**Année** : 2023
**DOI** : 10.1016/j.media.2023.102918

## Résumé

Training segmentation models for medical images continues to be challenging due to the limited availability of data annotations. Segment Anything Model (SAM) is a foundation model trained on over 1 billion annotations, predominantly for natural images, that is intended to segment user-defined objects of interest in an interactive manner. While the model performance on natural images is impressive, medical image domains pose their own set of challenges. Here, we perform an extensive evaluation of SAM's ability to segment medical images on a collection of 19 medical imaging datasets from various modalities and anatomies. In our experiments, we generated point and box prompts for SAM using a standard method that simulates interactive segmentation. We report the following findings: (1) SAM's performance based on single prompts highly varies depending on the dataset and the task, from IoU=0.1135 for spine MRI to IoU=0.8650 for hip X-ray. (2) Segmentation performance appears to be better for

## Méthodologie

{'study_design': "Comparaison expérimentale de trois algorithmes d'évaluation de surfaces 3D : la méthode proposée basée sur un modèle statistique de forme (SSM), en deux variantes (SSM-Points utilisant uniquement l'information de points 3D, et SSM incluant le vecteur normal), comparée à deux méthodes d'évaluation industrielles couramment utilisées", 'intervention': None, 'control': "Deux méthodes d'évaluation additionnelles couramment utilisées dans l'industrie", 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': "Chaque surface évaluée par les trois algorithmes ; pour les algorithmes entraînables, le même ensemble d'entraînement a été utilisé"}

## Résultats

{'quantitative': [{'outcome': 'Détection des objets défectueux par la méthode proposée (SSM)', 'value': 'virtuellement 100%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': 'It is capable of virtually 100% detection of defective objects accepting 93.15% of the non-defective objects'}, {'outcome': 'Acceptation des objets non défectueux par la méthode proposée (SSM) au point de détection ~100%', 'value': '93.15', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': 'It is capable of virtually 100% detection of defective objects accepting 93.15% of the non-defective objects'}, {'outcome': 'Acceptation des objets non défectueux par la méthode kernel-hull au même point de détection', 'value': '64.38', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': 'while the kernel-hull method just accepts 64.38%'}, {'outcome': "Nombre de répétitions d'inspection par objet", 'value': '25', 'unit': 'inspections/objet', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'Each of the objects has been inspected 25 times, so the variability of the device is also modelled during the process.'}], 'qualitative_findings': ["Le jeu de données réel est plus petit que le jeu de données synthétique afin d'assurer un étiquetage correct.", 'Les modèles du Good Validation set ont de faibles tolérances, rendant les résultats des méthodes plus similaires et le test plus difficile pour la méthode proposée.', "La méthode proposée surpasse les alternatives grâce à l'utilisation d'informations locales permettant d'apprendre la variabilité à un niveau fin.", "Le SSM utilisant uniquement l'information de position montre une performance plus faible que le SSM complet.", 'Les résultats de C2C sont nettement inférieurs à ceux des autres algorithmes.', "Le jeu de données a été sélectionné avec une proportion plus élevée que la normale d'objets défectueux et d'objets aux erreurs très faibles proches de la limite d'acceptation, ce qui rend les résultats plus mauvais que dans un processus industriel réel.", "Un processus d'inspection pourrait analyser une seconde fois les objets proches de la limite d'acceptation pour augmenter la précision.", "Sur un objet avec matière manquante trop fine, le SSM a détecté correctement l'erreur grâce aux vecteurs normaux locaux, alors que le kernel-hull n'a pas pu la détecter car elle se situait dans la variabilité des objets de référence.", "Sur un objet correct présentant des bulges synthétiques inhabituellement larges causés par la reconstruction 3D par silhouette, le SSM a détecté à tort ces bulges comme des erreurs car ils ne suivent pas une distribution gaussienne et n'ont pas été appris pendant l'entraînement.", "Le kernel-hull, suivant une stratégie maximum-minimum ignorant la distribution, n'a pas détecté ces bulges comme erronés.", 'La position et la taille de ces bulges pourraient être prédites en tenant compte de la distribution des caméras et de la forme des objets, information combinable avec les gaussiennes estimées par le SSM, mais cela est proposé comme travail futur.', 'La méthode proposée surpasse les autres solutions même dans les cas de déformations petites et de nature rigide, où les performances devraient pourtant être similaires.', "La disponibilité d'informations statistiques locales sur les positions des points et leurs vecteurs normaux à la surface est essentielle à cet avantage.", "Bien que la comparaison kernel-hull soit légèrement meilleure dans certaines zones de fonctionnement de la courbe ROC, le modèle de forme statistique est significativement meilleur pour détecter tous les échantillons défectueux à un taux de vrais positifs plus élevé, ce qui est le point de fonctionnement souhaité pour l'inspection industrielle."], 'main_findings': ["La méthode SSM proposée est significativement meilleure que les alternatives (kernel-hull, SSM position seule, C2C) dans la plage la plus importante de la courbe ROC pour l'inspection industrielle.", 'SSM atteint une détection quasi totale (100%) des objets défectueux tout en acceptant 93.15% des objets non défectueux, contre 64.38% pour kernel-hull.', "L'avantage clé de SSM provient de l'exploitation d'informations statistiques locales (positions des points et vecteurs normaux), permettant de détecter des défauts fins que kernel-hull manque.", "SSM peut générer des faux positifs sur des bulges synthétiques non gaussiens issus de la reconstruction 3D par silhouette, un point identifié comme piste d'amélioration future."]}

## Conclusions

A probabilistic method for training models and evaluating 3D surfaces with elastic manufacturing tolerances has been presented The training process makes use of correct objects to infer a model shape with variability, making possible to measure distances with the learned Statistical Shape Model (SSM) The evaluation relies on the SSM to analyse the 3D reconstructed object establishing a metric for each point against this model, and this evaluation may be filtered against outliers to determine whether the inspected object is correct or not The proposed method has been compared with other alternatives in simulated and real environments using a ZG3D device, outperforming them for the industrial inspection use case The SSM based algorithm proved to be capable to work with rigid as well as elastic manufacturing tolerances, obtaining better results than the alternative algorithms in both cases

### Formule


$$SI p = ∑ q∈N p SI q D q ∑ q∈N p D q . (1$$

### Formule


$$)$$

### Formule


$$D M ( x) = ( x -µ) T S -1 ( x -µ).$$

### Formule


$$)2$$
