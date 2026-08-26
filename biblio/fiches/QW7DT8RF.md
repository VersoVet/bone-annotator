# A survey on active learning and human-in-the-loop deep learning for medical image analysis

**Auteurs** : Samuel Budd, Emma C. Robinson, Bernhard Kainz
**Année** : 2021
**DOI** : 10.1016/j.media.2021.102062

## Résumé

Fully automatic deep learning has become the state-of-the-art technique for many tasks including image acquisition, analysis and interpretation, and for the extraction of clinically useful information for computer-aided detection, diagnosis, treatment planning, intervention and therapy. However, the unique challenges posed by medical image analysis suggest that retaining a human end user in any deep learning enabled system will be beneficial. In this review we investigate the role that humans might play in the development and deployment of deep learning enabled diagnostic applications and focus on techniques that will retain a significant input from a human end user. Human-in-the-Loop computing is an area that we see as increasingly important in future research due to the safety-critical nature of working in the medical domain. We evaluate four key areas that we consider vital for deep learning in the clinical practice: (1) Active Learning to choose the best data to annotate for optima

## Méthodologie

{'study_design': "Revue narrative (survey) de la littérature sur l'Active Learning et le Human-in-the-Loop Deep Learning appliqués à l'analyse d'images médicales, avec un focus sur la segmentation d'images. Les études sont catégorisées selon la nature de l'interaction humaine proposée et réparties selon trois défis clés identifiés par les auteurs (manque de données d'entraînement, 'the final percent', transparence/interprétabilité).", 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': "Analyse d'images médicales (notamment segmentation d'images médicales) en contexte clinique"}

## Résultats

{'quantitative': [{'outcome': "Réduction du coût d'annotation via AFT (Active Fine-Tuning) sur vidéos CIMT", 'value': "80% de réduction relative à l'entraînement à partir de zéro ; 50% relative à la sélection aléatoire de nouveaux échantillons", 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Future Prospective and Unanswered Questions', 'source_quote': 'reduce annotation cost by 80% relative to training from scratch and by 50% relative to random selection of new samples to be annotated (and used for fine-tuning)'}, {'outcome': "Nombre de clics utilisateur pour l'Annotation Unit (vidéos CIMT)", 'value': '6', 'unit': 'clics de souris', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Future Prospective and Unanswered Questions', 'source_quote': 'reducing annotating a CIMT video to just 6 user mouse clicks'}, {'outcome': 'Nombre de joueurs inscrits sur la plateforme de gamification EyeWire', 'value': '500,000', 'unit': 'joueurs', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Annotation Interface', 'source_quote': 'The gamification of this task has seen over 500,000 players sign up and the segmentations acquired have gone onto be used in several research works'}], 'qualitative_findings': ["L'eye-tracking permet de générer des données d'entraînement avec une performance quasi équivalente aux annotations manuelles traditionnelles", 'Les utilisateurs de la plateforme gamifiée EyeWire sont motivés principalement par la contribution scientifique plutôt que par une récompense monétaire', "Le biais introduit par les méthodes d'Active Learning peut être bénéfique lors de l'entraînement de modèles surparamétrés comme les réseaux de neurones avec peu de données"], 'main_findings': ["Trois défis clés freinent l'adoption du deep learning en pratique clinique : le manque de données d'entraînement annotées, 'the final percent' (nécessité d'une interprétation/correction interactive des prédictions), et le manque de transparence/interprétabilité", "L'Active Learning (pool-based, stream-based, membership query synthesis) permet d'atteindre des performances état de l'art avec moins d'annotations en sélectionnant les échantillons les plus informatifs", "Les mesures d'incertitude (least confident sampling, margin sampling, entropie) sont les principales heuristiques utilisées pour évaluer l'informativité des échantillons non annotés", "Le Transfer Learning et la Domain Adaptation réduisent significativement le nombre d'images annotées nécessaires pour de nouvelles tâches", "L'apprentissage continu à partir de flux de données pose un risque d'oubli catastrophique ('catastrophic forgetting'), nécessitant des stratégies telles que la consolidation élastique des poids (elastic weight consolidation)", "La combinaison future de l'Active Learning et du raffinement itératif dans un cadre unifié pourrait accélérer le processus d'annotation et améliorer la qualité initiale des résultats du modèle"]}

## Conclusions

L'implication directe des humains est amenée à jouer un rôle central dans le changement de paradigme induit par le deep learning pour les tâches cliniques Il existe un chevauchement suffisant entre les différentes méthodes présentées pour qu'elles soient considérées sous le même intitulé de 'Human-in-the-Loop computing' Les auteurs espèrent voir émerger de nouvelles méthodologies combinant les forces de l'Active Learning et du HITL computing en systèmes de bout en bout utilisables en pratique clinique Malgré des limites pratiques actuelles, de nombreuses solutions sont proposées et la recherche continue devrait mener à des systèmes de deep learning robustes et précis pour des tâches de routine

### Formule


$$x * LC = argmax x 1 -P θ (ŷ|x)$$

### Formule


$$x * M = argmin x P θ (ŷ 1 |x) -P θ (ŷ 2 |x)$$

### Formule


$$* E = argmax x - i P(y i |x)logP(y i |x)$$
