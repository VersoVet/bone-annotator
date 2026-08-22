# INTERACTIVE CHANGE DETECTION USING HIGH RESOLUTION REMOTE SENSING IMAGES BASED ON ACTIVE LEARNING WITH GAUSSIAN PROCESSES

**Auteurs** : Hui Ru, Huai Yu, Pingping Huang, Wen Yang
**Année** : 2016
**DOI** : 10.5194/isprs-annals-iii-7-141-2016

## Résumé

Abstract. Although there have been many studies for change detection, the effective and efficient use of high resolution remote sensing images is still a problem. Conventional supervised methods need lots of annotations to classify the land cover categories and detect their changes. Besides, the training set in supervised methods often has lots of redundant samples without any essential information. In this study, we present a method for interactive change detection using high resolution remote sensing images with active learning to overcome the shortages of existing remote sensing image change detection techniques. In our method, there is no annotation of actual land cover category at the beginning. First, we find a certain number of the most representative objects in unsupervised way. Then, we can detect the change areas from multi-temporal high resolution remote sensing images by active learning with Gaussian processes in an interactive way gradually until the detection results do not change notably. The artificial labelling can be reduced substantially, and a desirable detection result can be obtained in a few iterations. The experiments on Geo-Eye1 and WorldView2 remote sensing images demonstrate the effectiveness and efficiency of our proposed method.

## Méthodologie

{'study_design': "Méthode interactive de détection de changement combinant segmentation en superpixels (SLIC), extraction de caractéristiques (descripteur de couleur discriminant + descripteur SIFT), calcul de similarité par noyau d'intersection d'histogramme, sélection initiale d'échantillons (K-means choisi), puis classification supervisée itérative par apprentissage actif avec processus gaussiens jusqu'à stabilisation des résultats", 'intervention': "Étiquetage manuel itératif ('change' / 'no change') des échantillons les plus représentatifs sélectionnés par différentes stratégies de requête (sélection aléatoire, moyenne prédictive, incertitude), ajoutés progressivement à l'ensemble d'entraînement", 'control': None, 'primary_outcomes': ['Détection des zones de changement entre images multi-temporelles à haute résolution'], 'secondary_outcomes': ["Comparaison de l'efficacité de différents descripteurs (couleur, structure, combiné)", "Comparaison des stratégies de requête d'apprentissage actif", 'Temps de calcul selon la stratégie utilisée'], 'statistical_methods': ['Coefficient Kappa (mesure de concordance entre résultats détectés et valeur de référence)', 'Algorithme Expectation-Maximization (EM)', 'K-means clustering', 'Processus gaussiens (Gaussian processes)'], 'duration': '40 itérations', 'setting': 'Expériences réalisées sous MATLAB sur images satellites Geo-Eye1 et WorldView2'}

## Résultats

{'quantitative': [{'outcome': "Nombre d'itérations maximum fixé pour l'expérience", 'value': '40', 'unit': 'itérations', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'In this experiment, we set the number of iteration to 40.'}, {'outcome': "Proportion d'échantillons totaux étiquetés manuellement", 'value': '5%', 'unit': 'pourcentage des échantillons totaux', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'In the whole process, about 5% of total samples are labelled with user.'}], 'qualitative_findings': ["La concaténation du descripteur de couleur discriminant et du descripteur SIFT est plus efficace que l'utilisation d'un seul descripteur", "'The predictive mean' et 'the uncertainty' sont des stratégies de requête relativement meilleures pour la détection de changement sur images de télédétection à haute résolution"], 'main_findings': ["La méthode proposée permet de détecter les changements avec un nombre réduit d'échantillons étiquetés manuellement", "La combinaison des descripteurs de couleur et de structure (SIFT) améliore les résultats de détection de changement par rapport à l'utilisation d'un seul descripteur", "Certaines stratégies de requête d'apprentissage actif (moyenne prédictive, incertitude) surpassent la sélection aléatoire"]}

## Conclusions

La méthode d'apprentissage actif avec processus gaussiens permet de détecter efficacement les changements dans des images de télédétection à haute résolution sans nécessiter d'annotation initiale des catégories de couverture du sol L'annotation manuelle peut être réduite substantiellement tout en obtenant un résultat de détection satisfaisant en peu d'itérations Les expériences sur images Geo-Eye1 et WorldView2 démontrent l'efficacité et l'efficience de la méthode proposée

### Formule


$$HIK d d K x x  xx (1)$$

### Formule


$$n N   , n$$

### Formule


$$() i i y f    x , i$$

### Formule


$$    1 * 2 * * T n x k y      K I (2)     1 2 * 2 2 * ** * * T n n x k k k         K I($$

### Formule


$$    () * () * ârg m n î i i x U x U     (4)$$

### Formule


$$        () () 1 ( ) ( ) 2 * * 2 * { 1,1} * 1 ârg max min 1 î i impact i i n y x U x y k U x                    K I (8)$$
