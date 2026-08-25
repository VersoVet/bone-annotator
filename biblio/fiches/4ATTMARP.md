# Automated Segmentation and Length Measurement of Metacarpal and Phalangeal Bones for Hand Radiograph Evaluation

**Auteurs** : Philip Gutberlet, Aron Kirchhoff, Eike Bolmer, Philipp Schmidt, Fabio Hellmann, Johannes Grün, Alexander Hustinx, Elisabeth André, Thomas Schultz, Klaus Mohnike
**Année** : 2025
**DOI** : 10.21203/rs.3.rs-8427266/v1

## Résumé

Abstract
                Evaluating hand and wrist radiographs is essential in pediatric endocrinology and clinical genetics, particularly for the assessment of suspected skeletal anomalies. In this study, we present  Auto-Bone-Caliper, an automated system for the segmentation and length measurement of metacarpal and phalangeal (M&amp;P) bones, trained and evaluated on public datasets comprising both normal and dysmorphic cases. We first introduce InstanceSAM, a two-stage framework that detects and segments all 19 M&amp;P bones in pediatric hand radiographs, achieving Dice scores of 98.7% for normal bones and 95.0% for dysmorphic bones. We further develop and evaluate three methods for bone-length estimation, identifying a k-means–based approach as the most accurate, with relative errors of 2.2% for normal bones and 4.5% for dysmorphic bones. Our automated pipeline, Auto-Bone-Caliper, integrates InstanceSAM with the k-means–based length estimation method. Additionally, we statistically compare measurements obtained using Auto-Bone-Caliper on an independent dataset with a healthy reference catalog of normal bone morphologies, observing a high level of agreement (Wasserstein-1 distance = 0.012). Finally, we demonstrate a clinical use case of Auto-Bone-Caliper by obtaining M&amp;P profiles for three genetic conditions, namely Turner syndrome, achondroplasia, and pseudohypoparathyroidism. Our results highlight the potential of the Auto-Bone-Caliper to streamline and standardize M&amp;P length measurement, providing an objective and reproducible tool suitable for clinical application.

## Méthodologie

{'study_design': "Étude de développement et de validation d'un pipeline d'apprentissage automatique (InstanceSAM, basé sur un modèle YOLO affiné suivi de SAM) pour la segmentation des 19 os M&P, associée à l'évaluation comparative de trois méthodes d'estimation de longueur osseuse (statistical shape modeling, bounding box, k-means), sur des données publiques normales et dysmorphiques", 'intervention': 'Application du pipeline automatisé Auto-Bone-Caliper (InstanceSAM + méthode k-means) pour la segmentation et la mesure des os M&P', 'control': 'Comparaison avec des valeurs de référence issues du catalogue de Poznanski (1984) pour des individus sains, et avec des méthodes de segmentation/mesure publiées antérieurement', 'primary_outcomes': ['Score de Dice pour la segmentation des os M&P (normaux et dysmorphiques)', 'Erreur relative de mesure de longueur des os M&P (normaux et dysmorphiques)'], 'secondary_outcomes': ["Distance de Wasserstein-1 entre les mesures d'Auto-Bone-Caliper et le catalogue de référence sain", 'Profils M&P pour trois conditions génétiques (Turner, achondroplasie, pseudohypoparathyroïdie)'], 'statistical_methods': ['Score de Dice', 'Erreur relative', 'Distance de Wasserstein-1', 'Calcul de Z-score pour les profils M&P'], 'duration': None, 'setting': 'Jeux de données publics de radiographies de main pédiatriques (dont GMDB et DHA)'}

## Résultats

{'quantitative': [{'outcome': 'Score de Dice de segmentation - os normaux (InstanceSAM)', 'value': '98.7', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'achieving Dice scores of 98.7% for normal bones and 95.0% for dysmorphic bones'}, {'outcome': 'Score de Dice de segmentation - os dysmorphiques (InstanceSAM)', 'value': '95.0', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'achieving Dice scores of 98.7% for normal bones and 95.0% for dysmorphic bones'}, {'outcome': 'Erreur relative de mesure de longueur - os normaux (méthode k-means)', 'value': '2.2', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'identifying a k-means-based approach as the most accurate, with relative errors of 2.2% for normal bones and 4.5% for dysmorphic bones'}, {'outcome': 'Erreur relative de mesure de longueur - os dysmorphiques (méthode k-means)', 'value': '4.5', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'identifying a k-means-based approach as the most accurate, with relative errors of 2.2% for normal bones and 4.5% for dysmorphic bones'}, {'outcome': 'Distance de Wasserstein-1 entre Auto-Bone-Caliper (DHA) et catalogue de référence sain', 'value': '0.012', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'observing a high level of agreement (Wasserstein-1 distance = 0.012)'}], 'qualitative_findings': ["InstanceSAM, bien qu'entraîné exclusivement sur des radiographies normales, généralise avec succès à des os dysmorphiques issus de patients atteints de divers troubles osseux", "Les profils M&P pour l'achondroplasie, la pseudohypoparathyroïdie et le syndrome de Turner illustrent le potentiel du système automatisé pour soutenir l'évaluation clinique des troubles osseux"], 'main_findings': ["InstanceSAM détecte et segmente les 19 os M&P avec des scores de Dice élevés, supérieurs à ceux rapportés dans des études antérieures (~95% et 93.9%) portant sur l'estimation de l'âge osseux", "La méthode k-means surpasse les approches SSM et bounding-box pour l'estimation de la longueur des os, avec une erreur de prédiction de l'axe osseux environ deux fois plus faible", "Auto-Bone-Caliper montre un fort accord avec le catalogue de référence de Poznanski (1984) sur un jeu de données indépendant (DHA), malgré des décennies d'écart de collecte et des méthodes de mesure différentes (caliper manuel vs image numérique)"]}

## Conclusions

Auto-Bone-Caliper constitue un système automatisé fiable pour la segmentation et la mesure de longueur des os M&P, applicable aux radiographies normales et dysmorphiques InstanceSAM, bien qu'entraîné uniquement sur des os normaux, généralise avec succès aux os dysmorphiques issus de divers troubles squelettiques La méthode k-means est la plus précise pour l'estimation de longueur osseuse et a été retenue comme composante du pipeline L'accord étroit entre les mesures d'Auto-Bone-Caliper et les valeurs de référence de Poznanski (1984) soutient la validité de l'outil Les solutions automatisées telles qu'Auto-Bone-Caliper ont le potentiel de standardiser et faciliter l'analyse du profil M&P, en assistant le diagnostic, le suivi et le dépistage des anomalies osseuses

## Performance of InstanceSAM. The Mean Dice score for all 19 bones and for each bone type is listed for both normal and dysmorphic hand radiographs.

| Bone | Normal [%] Dysmorphic [%] |
| --- | --- | --- |
| All 19 Bones | 98.7 | 95.0 |
| Metacarpal 1 | 99.0 | 97.1 |
| Metacarpal 2 | 98.6 | 97.4 |
| Metacarpal 3 | 98.3 | 97.5 |
| Metacarpal 4 | 98.3 | 97.1 |
| Metacarpal 5 | 98.8 | 97.1 |
| Proximal Phalanx 1 | 99.0 | 95.6 |
| Proximal Phalanx 2 | 99.3 | 97.4 |
| Proximal Phalanx 3 | 99.4 | 97.8 |
| Proximal Phalanx 4 | 99.3 | 97.5 |
| Proximal Phalanx 5 | 99.2 | 95.7 |
| Middle Phalanx 2 | 98.0 | 96.1 |
| Middle Phalanx 3 | 98.4 | 94.5 |
| Middle Phalanx 4 | 98.7 | 94.1 |
| Middle Phalanx 5 | 98.3 | 94.9 |
| Distal Phalanx 1 | 98.8 | 94.6 |
| Distal Phalanx 2 | 98.3 | 90.7 |
| Distal Phalanx 3 | 98.5 | 94.3 |
| Distal Phalanx 4 | 98.5 | 91.1 |
| Distal Phalanx 5 | 98.2 | 84.3 |

## Average relative length and axis angle errors in percentage [%] and degrees [°], respectively, for the three automatic length measurement methods.

| Method | Normal (n=20) | Dysmorphic (n=30) | Total (n=50) |
| --- | --- | --- | --- | --- |
|  | Length Angle Length | Angle | Length Angle |
| Statistical Shape Model | 3.1% | 5.6°6.4% | 10.3°5.1% | 8.4°B |
| ounding Box | 3.4% | 3.5°5.6% | 5.1°5.7% | 4.6°k |
| -means | 2.2% | 1.6°4.5% | 2.9°3.6% | 2.4°1 |

### Formule


$$R x,y = l x l y ,(1)$$

### Formule


$$∆R x,y = (R x,y -R ref x,y ) R ref x,y$$

### Formule


$$r m,x = l m,x19$$

### Formule


$$i=1 l m,i(3)$$

### Formule


$$z s x = r s x -r ref x σ ref x (4$$

### Formule


$$)$$
