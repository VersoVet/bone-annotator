# A multi-spectral myelin annotation tool for machine learning based myelin quantification [version 4; peer review: 2 approved]

**Auteurs** : Abdulkerim Çapar, Dursun Ali Ekinci, Umut Engin Ayten, Sibel Çimen, Zeynep Aladağ, Behçet Uğur Töreyin, Bilal Ersen Kerman
**Année** : 2023
**DOI** : 10.12688/f1000research.27139.4

## Résumé

Myelin is an essential component of the nervous system and myelin damage causes demyelination diseases. Myelin is a sheet of oligodendrocyte membrane wrapped around the neuronal axon. In the fluorescent images, experts manually identify myelin by co-localization of oligodendrocyte and axonal membranes that fit certain shape and size criteria. Because myelin wriggles along x-y-z axes, machine learning is ideal for its segmentation. However, machine-learning methods, especially convolutional neural networks (CNNs), require a high number of annotated images, which necessitate expert labor. To facilitate myelin annotation, we developed a workflow and software for myelin ground truth extraction from multi-spectral fluorescent images. Additionally, to the best of our knowledge, for the first time, a set of annotated myelin ground truths for machine learning applications were shared with the community.

## Méthodologie

{'study_design': "Développement d'un outil logiciel (CEMotate) et d'un workflow pour la visualisation et l'annotation manuelle assistée de pixels candidats de myéline (issus du logiciel CEM), permettant la co-visualisation d'images RGB-composite par section z, de la sortie CEM, et des marquages d'experts", 'intervention': 'Utilisation de CEMotate pour évaluer les pixels candidats de myéline (identifiés par colocalisation entre canaux oligodendrocyte et neurone) et décider de leur conservation ou suppression, avec possibilité de comparaison entre deux experts annotant indépendamment', 'control': None, 'primary_outcomes': ["Extraction de ground truths de myéline annotées pour l'entraînement de modèles de machine learning"], 'secondary_outcomes': ["Temps nécessaire au processus d'annotation comparé à une méthode manuelle classique", 'Facilitation de la comparaison inter-experts'], 'statistical_methods': [], 'duration': "Environ 5 jours pour l'annotation complète (contre plusieurs semaines estimées sans l'outil)", 'setting': "Analyse d'images de bioimagerie fluorescente multi-spectrale"}

## Résultats

{'quantitative': [{'outcome': "Nombre d'images de caractéristiques (feature images) extraites", 'value': 'plus de 30 000', 'unit': 'feature images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Introduction', 'source_quote': 'More than 30,000 feature images were extracted from these five images and were used for testing various machine-learning methods'}, {'outcome': "Durée du processus d'annotation", 'value': 'environ 5 jours (vs plusieurs semaines estimées)', 'unit': 'jours', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Introduction', 'source_quote': 'The entire process, which would have taken several weeks, took approximately 5 days.'}], 'qualitative_findings': ["Les conclusions sur l'outil et sa performance sont jugées adéquatement supportées par les résultats présentés"], 'main_findings': ["CEMotate accélère l'annotation d'images multi-spectrales", "L'outil permet la visualisation simultanée d'une image RGB-composite par section z, de la sortie CEM et des marquages experts", "L'outil facilite la comparaison et la validation inter-experts en permettant la superposition des annotations de deux experts", 'Cinq images annotées et plus de 30 000 feature images ont été générées et partagées comme ressource pour la communauté']}

## Conclusions

CEMotate accélère l'annotation d'images multi-spectrales, illustré ici par l'annotation de la myéline identifiée comme colocalisation des membranes neuronales et oligodendrocytaires selon certains critères Les fonctionnalités de visualisation de CEMotate simplifient la collaboration et la validation inter-experts Les ground truths de myéline accompagnant le manuscrit constituent une ressource pour les chercheurs travaillant sur la segmentation de la myéline et d'autres structures dans des images multi-spectrales

## Table 1 . Time comparison to detect myelin in five images for CEM and ML Approach. CEM ML Approach 9

| Time (~) 43 min | 1.04 sec |
| --- | --- |

## Table 1 . Time comparison to detect myelin in five images for CEM and ML Approach CEM ML Approach 9

| Time (~) |
| --- |
| 43 min |
| 1.04 sec |

## Table 2 . Time comparison for ImageJ and CEMotate annotation ImageJ CEMotate

| Time (~) |
| --- |
| 35 hours |
| 20 hours |

## Table 3 . Experts' average precisions on candidate myelin pixels of five images Expert 1 Expert 2

| Average Precisions |
| --- |
| 36.23% |
| 60.54% |
