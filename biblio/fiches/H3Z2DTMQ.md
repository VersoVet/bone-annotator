# Cograph Regularized Collective Nonnegative Matrix Factorization for Multilabel Image Annotation

**Auteurs** : Juli Zhang, Zhanzhuang He, Junyi Zhang, Tao Dai
**Année** : 2019
**DOI** : 10.1109/access.2019.2925891

## Résumé

Automatic image annotation is an effective and straightforward way to facilitate many applications in computer vision. However, manually annotating images is a computation-expensive and labor-intensive task. To address these problems, this paper proposes a novel approach by using a cograph regularized collective nonnegative matrix factorization method to annotate images, which is referred to as CG-CNMF; CG-CNMF maximizes the annotation consistency for each image and minimizes the semantic gap for good annotation performance. To reduce the computation cost, this method formulates the annotation problem as a recommending issue and uses nonnegative matrix factorization (NMF) to recover the image-to-label relation for the testing images. Moreover, to find the most similar latent image features and latent label features during the matrix factorization, it exploits the image-to-image relation and label-to-label relation by utilizing the visual content information of images and the semantic c

## Méthodologie

{'study_design': "Proposition d'une méthode de factorisation matricielle non-négative collective régularisée par cographes (CG-CNMF), évaluée expérimentalement sur trois jeux de données d'images multilabel en comparaison avec des méthodes existantes", 'intervention': "Application de la méthode CG-CNMF, qui construit une matrice image-label, une matrice de similarité d'images et une matrice de cooccurrence de labels, puis factorise ces trois matrices simultanément en exploitant des caractéristiques visuelles basées CNN et des informations sémantiques", 'control': 'Méthodes existantes comparées : TagProp, NMF-KNN, 2PKNN, CCA-KNN, FastTag, MLDL, JEC, RMLF', 'primary_outcomes': ['Precision (P)', 'Recall (R)', 'F1 score (F1)', 'N+'], 'secondary_outcomes': [], 'statistical_methods': ['Nonnegative matrix factorization (NMF)', 'Collective matrix factorization', 'Régularisation par graphe de Laplace (Laplace matrix regularization)', 'Mise à jour multiplicative (multiplicative updating)'], 'duration': None, 'setting': "Expériences menées sur trois jeux de données d'images multilabel (Corel5K, IAPR TC12, ESP) avec des ratios d'entraînement de 20%, 50% et 80%"}

## Résultats

{'quantitative': [{'outcome': 'Gain en F1 score de CG-CNMF vs CCA-KNN sur Corel5K (20% training)', 'value': '3.4%', 'unit': 'pourcentage', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'It attains 3.4% achievement under F1 score for Corel5k, 1.6% achievement for IAPR TC12 and 0.7% for ESP when compared with CCA-KNN.'}, {'outcome': 'Gain en F1 score de CG-CNMF vs CCA-KNN sur IAPR TC12 (20% training)', 'value': '1.6%', 'unit': 'pourcentage', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'It attains 3.4% achievement under F1 score for Corel5k, 1.6% achievement for IAPR TC12 and 0.7% for ESP when compared with CCA-KNN.'}, {'outcome': 'Gain en F1 score de CG-CNMF vs CCA-KNN sur ESP (20% training)', 'value': '0.7%', 'unit': 'pourcentage', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'It attains 3.4% achievement under F1 score for Corel5k, 1.6% achievement for IAPR TC12 and 0.7% for ESP when compared with CCA-KNN.'}, {'outcome': 'Comparaison CG-CNMF vs MLDL sur Corel5K (20% training)', 'value': 'MLDL inférieur de 0.3% en F1', 'unit': 'pourcentage', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'MLDL achieves the second-best performance in the F1 score measure, which is slightly worse (0.3%) than the proposed approach.'}, {'outcome': 'Gain en F1 score de FastTag vs JEC sur Corel5K', 'value': '8.4%', 'unit': 'pourcentage', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'this method achieves 8.4% gains compared with JEC in F1 on Corel5k.'}, {'outcome': 'Gain en F1 score de RMLF vs JEC sur Corel5K', 'value': '7%', 'unit': 'pourcentage', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'RMLF achieves a large margin (7%) in F1 compared with JEC on Corel5k.'}], 'qualitative_findings': ["JEC est la méthode la moins performante parmi toutes les méthodes comparées, en raison de sa forte dépendance aux caractéristiques d'image et de la pondération égale de ces caractéristiques", "Sur le jeu de données à 50% d'entraînement, MLDL est la meilleure méthode sur Corel5K, tandis que CG-CNMF est la meilleure sur ESP", "À 80% de données d'entraînement, CG-CNMF obtient les meilleurs résultats sur la plupart des mesures parmi les trois jeux de données", "FastTag est la méthode KNN-based la moins performante car elle privilégie la vitesse d'annotation à la précision"], 'main_findings': ["CG-CNMF surpasse significativement les autres méthodes en F1 score sur les trois jeux de données lorsque le ratio d'entraînement est de 20%", "Les caractéristiques CNN utilisées pour construire la similarité d'image basée sur le contenu visuel améliorent significativement la performance d'annotation", "L'exploitation simultanée des trois relations (image-label, image-image, label-label) réduit le fossé sémantique et améliore les performances d'annotation", "La performance de CG-CNMF s'améliore à mesure que le ratio des données d'entraînement augmente (20% à 80%)", 'CG-CNMF est plus efficace en termes de calcul en raison de la représentation de rang faible (low-rank) offerte par la NMF']}

## Conclusions

CG-CNMF, formulé comme un problème de recommandation de labels, factorise la matrice image-label incomplète en exploitant les relations image-image et label-label pour traiter les problèmes de parcimonie, de fossé sémantique, d'étiquetage faible et de déséquilibre des classes L'utilisation de caractéristiques visuelles basées sur les réseaux de neurones profonds (CNN) permet de réduire davantage le fossé sémantique La performance d'annotation dépend principalement des matrices de caractéristiques latentes d'image et de label, obtenues en combinant similarité sémantique et visuelle pour les images, ainsi que cooccurrence visuelle et sémantique pour les labels Les résultats expérimentaux confirment l'efficacité de cette approche combinée

### Formule


$$S VS x i ,x j = < sx i , sx j > sx i sy i (1)$$

### Formule


$$W U i,j = sim(l(x i ), l(x j$$

### Formule


$$)2$$

### Formule


$$sim(l(x i ), l(x j )) = < l(x i ), l(x j ) > l(x i ) l(x j ) ,(3)$$

### Formule


$$O 1 = 1 2 m i,j=1 u i -u j 2 W U ij = Tr(U T L U U ) (4$$

### Formule


$$)$$

### Formule


$$vsim(l a , l b ) = 1 T P K S (I (l a ), I (l b )) = 1 T P T P i=1,j=1 S I (I i (l a ), I j (l b ))(5)$$

### Formule


$$W V ij =$$

### Formule


$$O 2 = 1 2 n i,j=1 v i -v j 2 W v ij = Tr(V T L V V )$$

### Formule


$$L V = D V -W V is the Laplacian matrix, D V is a diagonal matrix and D V ii = n j=1 W V ij .$$

### Formule


$$sim(l i , l j ) = < t :i , t :j > t :i t :j(6)$$

### Formule


$$L JWNMF (U , V , P, Z ) s.t.U ≥0,V ≥0,P≥0,Z ≥0, = 1 2 Y (R -UV T ) 2 F + α 2 S -UP T 2 F + β 2 C -VZ T 2 F + λ U 2 Tr(U T L U U ) + λ V 2 Tr(V T L V V ) + λ 2 ( U 2 F + V 2 F + P 2 F + Z 2 F ) (7$$

### Formule


$$)$$

### Formule


$$Y ij Y ij = 1, if R ij is observed; 0, if R ij is unobserved.$$

### Formule


$$L(U ) = 1 2 Y (R -UV T ) 2 F + α 2 S -UP T 2 F + λ U 2 Tr(U T L U U ) + λ 2 U 2 F s.t. U ≥ 0$$

### Formule


$$∂L(U ) ∂U = -Y RV + Y (UV T )V -αSP + αUP T P + λ U L U U + λU$$

### Formule


$$M + ij = ( M ij + M ij ) 2, M - ij = ( M ij -M ij ) 2.$$

### Formule


$$U ij ← U ij [Y RV + αSP + λ U L - U U ] ij [Y (UV T )V + αUP T P + λ U L + U U + λU ] ij (8) 2) UPDATE FOR V$$

### Formule


$$L(V ) = 1 2 Y (R -UV T ) 2 F + β 2 C -VZ T 2 F + λ V 2 Tr(V T L V V ) + λ 2 V 2 F s.t. V ≥ 0$$

### Formule


$$V ij ← V ij [(Y R) T U + βC T V + λ V L - V V ] ij [Y (UV T ) T U + βVZ T Z + λ V L + V V + λV ] ij (9)$$

### Formule


$$L(P) = 1 2 S -UP T 2 F + λ 2 P 2 F L(Z ) = 1 2 C -VZ T 2 F + λ 2 Z 2 F$$

### Formule


$$∂L(P) ∂P = -S T U + PU T U + λP ∂L(Z ) ∂Z = -C T V + ZV T V + λZ$$

### Formule


$$P ij ← P ij S T U ij PU T U + λP ij (10$$

### Formule


$$)$$

### Formule


$$Z ij ← Z ij C T V j ZV T V + λZ jj (11$$

### Formule


$$)$$

### Formule


$$Output: U ≥ 0, V ≥ 0, Z ≥ 0, P ≥ 0, R ≥ 0 Initialize: U 0 ≥ 0, V 0 ≥ 0, P 0 ≥ 0, Z 0 ≥ 0 1: Construct weight matrix Y according R, Y ij = 1 if R ij can$$

### Formule


$$precision(li) = N correct N labeled , recall(li) = N correct N all F 1 -score(l i ) = 2 Pr ecision(l i ) × Re call(l i ) Pr ecision(l i ) + Re call(l i )$$
