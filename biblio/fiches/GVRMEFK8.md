# Segment Anything Model for Medical Image Segmentation: Current Applications and Future Directions

**Auteurs** : Yichi Zhang, Zhenrong Shen, Rushi Jiao
**Année** : 2024
**DOI** : 10.48550/arxiv.2401.03495

## Résumé

Due to the inherent flexibility of prompting, foundation models have emerged as the predominant force in the fields of natural language processing and computer vision. The recent introduction of the Segment Anything Model (SAM) signifies a noteworthy expansion of the prompt-driven paradigm into the domain of image segmentation, thereby introducing a plethora of previously unexplored capabilities. However, the viability of its application to medical image segmentation remains uncertain, given the substantial distinctions between natural and medical images. In this work, we provide a comprehensive overview of recent endeavors aimed at extending the efficacy of SAM to medical image segmentation tasks, encompassing both empirical benchmarking and methodological adaptations. Additionally, we explore potential avenues for future research directions in SAM's role within medical image segmentation. While direct application of SAM to medical image segmentation does not yield satisfactory performance on multi-modal and multi-target medical datasets so far, numerous insights gleaned from these efforts serve as valuable guidance for shaping the trajectory of foundational models in the realm of medical image analysis.

## Méthodologie

{'study_design': "Revue de la littérature synthétisant les travaux récents sur l'application de SAM (Segment Anything Model) à la segmentation d'images médicales, organisée en deux axes principaux: évaluation zero-shot et méthodes d'adaptation de SAM", 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [], 'qualitative_findings': ['La performance de SAM appliqué directement sans adaptation varie significativement selon les datasets et tâches médicales', 'SAM présente des difficultés à réaliser de manière cohérente et précise une segmentation zero-shot sur des jeux de données médicaux multi-modaux et multi-cibles', "La complexité et la diversité des modalités d'imagerie et des cibles d'intérêt affectent l'efficacité de segmentation de SAM, en particulier pour les objets à formes irrégulières, aux limites faibles, de petite taille ou à faible contraste", "Plusieurs études ayant exploré des stratégies d'adaptation appropriées ont amélioré les résultats de segmentation de SAM dans une certaine mesure, atteignant des performances compétitives par rapport aux modèles spécifiques à la tâche"], 'main_findings': ["L'application directe de SAM à la segmentation d'images médicales ne donne pas de performance satisfaisante sur des jeux de données médicaux multi-modaux et multi-cibles", "De nombreux enseignements tirés de ces efforts servent de guide précieux pour orienter la trajectoire des modèles de fondation dans le domaine de l'analyse d'images médicales", 'Malgré une performance actuelle parfois moins stable que celle des modèles spécifiques à la tâche, SAM possède un fort potentiel comme outil efficace pour faire progresser des applications cliniques importantes']}

## Conclusions

SAM a connu des développements sans précédent en segmentation d'images médicales au cours de l'année écoulée, faisant avancer significativement le développement de modèles de fondation universels pour l'analyse d'images médicales Cette revue vise à fournir à la communauté des perspectives précieuses sur la trajectoire du développement des modèles de fondation pour la segmentation d'images médicales Les auteurs anticipent que cette réflexion favorisera une compréhension plus approfondie des directions futures et inspirera de nouvelles recherches visant à créer une intelligence artificielle applicable cliniquement
