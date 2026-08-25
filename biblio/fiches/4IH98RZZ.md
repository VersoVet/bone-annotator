# Enhanced landmark detection model in pelvic fluoroscopy using 2D/3D registration loss

**Auteurs** : Chou Mo, Yehyun Suh, J. Ryan Martin, Daniel Moyer
**Année** : 2026
**DOI** : 10.1117/12.3085922

## Résumé

Automated landmark detection offers an efficient approach for medical professionals to understand patient anatomic structure and positioning using intra-operative imaging. While current detection methods for pelvic fluoroscopy demonstrate promising accuracy, most assume a fixed Antero-Posterior view of the pelvis. However, orientation often deviates from this standard view, either due to repositioning of the imaging unit or of the target structure itself. To address this limitation, we propose a novel framework that incorporates 2D/3D landmark registration into the training of a U-Net landmark prediction model. We analyze the performance difference by comparing landmark detection accuracy between the baseline U-Net, U-Net trained with Pose Estimation Loss, and U-Net fine-tuned with Pose Estimation Loss under realistic intra-operative conditions where patient pose is variable.

## Méthodologie

{'study_design': "Étude comparative expérimentale de trois architectures/stratégies d'entraînement d'un modèle U-Net pour la détection de landmarks pelviens sur images de fluoroscopie simulées, avec intégration d'une perte d'estimation de pose issue du recalage 2D/3D", 'intervention': 'Entraînement du U-Net avec Pose Estimation Loss (PEL), soit seule, soit en combinaison (composite) avec la perte de segmentation, soit par fine-tuning séquentiel après un pré-entraînement standard par segmentation', 'control': 'U-Net de référence (baseline) entraîné uniquement avec une perte de segmentation par entropie croisée pixel par pixel', 'primary_outcomes': ['Précision de détection des landmarks (RMSE - Root Mean Square Error) entre coordonnées prédites et coordonnées de vérité terrain'], 'secondary_outcomes': ["Convergence du modèle pendant l'entraînement", 'Capacité de généralisation entre jeu de données interne et externe'], 'statistical_methods': ['RMSE (Root Mean Square Error)', "Optimisation L-BFGS pour le recalage de pose dans la boucle d'entraînement"], 'duration': None, 'setting': 'Étude méthodologique/technique en imagerie médicale, utilisant des images DRR (Digitally Reconstructed Radiograph) générées via DiffDRR à partir de scans CT'}

## Résultats

{'quantitative': [{'outcome': 'RMSE - U-Net baseline (interne)', 'value': '8.58', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The baseline U-Net achieved mean RMSE values of 8.58 mm and 5.58 mm on internal and external datasets, respectively.'}, {'outcome': 'RMSE - U-Net baseline (externe)', 'value': '5.58', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The baseline U-Net achieved mean RMSE values of 8.58 mm and 5.58 mm on internal and external datasets, respectively.'}, {'outcome': 'RMSE - U-Net fine-tuné avec PEL (interne)', 'value': '8.45 (amélioration de 1.5%)', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The U-Net fine-tuned with PEL showed consistent improvements, achieving 8.45 mm (1.5% improvement) and 5.09 mm (8.8% improvement) on the respective datasets.'}, {'outcome': 'RMSE - U-Net fine-tuné avec PEL (externe)', 'value': '5.09 (amélioration de 8.8%)', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The U-Net fine-tuned with PEL showed consistent improvements, achieving 8.45 mm (1.5% improvement) and 5.09 mm (8.8% improvement) on the respective datasets.'}, {'outcome': "Augmentation d'erreur - U-Net entraîné avec PEL composite (relatif au baseline)", 'value': 'environ 2.4x (interne) et 2.1x (externe)', 'unit': 'ratio', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'the U-Net trained with composite PEL had approximately 2.4 and 2.1 times increases in error relative to the baseline.'}, {'outcome': 'Convergence - U-Net entraîné exclusivement avec PEL', 'value': 'Divergence (DIV)', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The U-Net trained exclusively using PEL failed to converge during training, leading to divergence (shown as "DIV" in Table 1).'}, {'outcome': 'Réduction de RMSE entre jeu interne et externe - baseline', 'value': '35%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The baseline U-Net achieved a 35% reduction in RMSE on external data (5.58mm compared to 8.58mm), while the fine-tuned method demonstrated a 40% improvement (5.09mm versus 8.45mm).'}, {'outcome': 'Réduction de RMSE entre jeu interne et externe - modèle fine-tuné', 'value': '40%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The baseline U-Net achieved a 35% reduction in RMSE on external data (5.58mm compared to 8.58mm), while the fine-tuned method demonstrated a 40% improvement (5.09mm versus 8.45mm).'}], 'qualitative_findings': ["La détérioration de performance du modèle à perte composite pourrait s'expliquer par un conflit entre objectifs d'optimisation : la perte de segmentation favorise des distributions de probabilité lisses et en forme de blob, tandis que la PEL pousse vers des distributions pointues et ponctuelles pour réduire l'erreur de recalage géométrique", "L'échec de convergence du modèle entraîné uniquement avec PEL suggère que cette perte seule ne fournit pas une structure de gradient adéquate pour un apprentissage efficace depuis une initialisation aléatoire"], 'main_findings': ['Le U-Net fine-tuné avec Pose Estimation Loss (PEL) après un pré-entraînement par segmentation surpasse le U-Net de référence sur les jeux de données interne et externe', "L'entraînement conjoint (perte composite combinant segmentation et PEL) dégrade significativement la performance par rapport au baseline", "L'entraînement exclusif avec PEL depuis une initialisation aléatoire ne converge pas", 'Tous les modèles montrent une meilleure performance sur le jeu de données externe (sujets non vus) que sur le jeu de données interne']}

## Conclusions

L'intégration de contraintes de recalage 2D/3D via une perte d'estimation de pose peut améliorer la précision de détection de landmarks lorsqu'elle est mise en œuvre par fine-tuning séquentiel plutôt que par optimisation conjointe Le fine-tuning du U-Net de référence pendant une seule époque permet d'atteindre une précision de recalage supérieure sur les jeux de test interne et externe La performance dégradée des méthodes à perte composite et à PEL seule souligne l'importance d'un curriculum d'entraînement approprié pour les tâches d'imagerie médicale La méthode séquentielle préserve la compréhension spatiale acquise lors de l'entraînement par segmentation tout en incorporant des contraintes géométriques pour une meilleure précision de localisation Ces résultats établissent un cadre viable pour incorporer des contraintes anatomiques 3D dans la détection de landmarks 2D, illustrant que la cohérence géométrique peut être efficacement exploitée pour améliorer la précision clinique via de meilleurs ajouts d'optimisation

### Formule


$$li = (x i , ŷi ) = W -1 x=0 H-1 y=0 x • softmax(h i ) (x,y) , W -1 x=0 H-1 y=0 y • softmax(h i ) (x,y)(1)$$

### Formule


$$(h i ) (x,y) = exp(h i (x, y)/τ ) x ′ ,y ′ exp(h i (x ′ , y ′ )/τ )(2)$$

### Formule


$$θ * = arg min θ L(θ).(3)$$

### Formule


$$L(θ) = N i=1 li (θ) -l i 2(4)$$

### Formule


$$R = I + sin(θ) • K + (1 -cos(θ)) • K 2(5)$$

### Formule


$$K =   0 -r z ry rz 0 -r x -r y rx 0  (6)$$

### Formule


$$p ′ i = Rp i + t (7) li = 1 z ′ i K 11 x ′ i + K 13 z ′ i K 22 y ′ i + K 23 z ′ i (8$$

### Formule


$$)$$

### Formule


$$p ′ i = (x ′ i , y ′ i , z ′ i )$$

### Formule


$$L composite = L seg + λ • L pose (9$$

### Formule


$$)$$

### Formule


$$L pose = 1 6 6 j=1 (θ j -θ * j ) 2(10)$$
