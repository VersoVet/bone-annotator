# PhenoImageShare: an image annotation and query infrastructure.

**Auteurs** : Solomon Adebayo, Kenneth McLeod, Ilinca Tudose, David Osumi-Sutherland, Tony Burdett, Richard Baldock, Albert Burger, Helen Parkinson
**Année** : 2016
**DOI** : 10.1186/s13326-016-0072-2

## Résumé

High throughput imaging is now available to many groups and it is possible to generate a large quantity of high quality images quickly. Managing this data, consistently annotating it, or making it available to the community are all challenges that come with these methods.

## Méthodologie

{'study_design': "Développement d'une infrastructure logicielle composée de trois couches principales : l'interface utilisateur (UI), la couche d'intégration et les services backend", 'intervention': "Mise en place d'un service d'annotation et de requête d'images activé par ontologie, backé par un serveur Solr pour l'accès programmatique, avec un outil d'annotation en ligne (dessin de régions d'intérêt et annotation via un widget d'auto-suggestion basé sur une ontologie)", 'control': None, 'primary_outcomes': ["Nombre d'images fédérées accessibles via la plateforme", "Nombre de régions d'intérêt (ROI) annotées avec des termes d'ontologie d'anatomie ou de phénotype"], 'secondary_outcomes': ["Qualité de l'expérience de recherche sémantique (regroupement des options de filtrage par termes de haut niveau)", 'Capacités de recherche spatiale (relation part-of, et futures relations gauche/droite, dorsal/ventral, crânial/caudal)'], 'statistical_methods': [], 'duration': None, 'setting': 'European Bioinformatics Institute (EMBL-EBI), European Molecular Biology Laboratory, Wellcome Trust Genome Campus, Hinxton, UK'}

## Résultats

{'quantitative': [{'outcome': "Nombre d'images fédérées accessibles", 'value': '117982', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Introduction', 'source_quote': 'PhIS is species and imaging technology neutral and currently provides access to 117,982 images federated from four different data resources with 53,000 regions of interest (ROI) associated to anatomy or phenotype ontology term annotations.'}, {'outcome': "Nombre de régions d'intérêt (ROI) annotées", 'value': '53000', 'unit': 'ROI', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Introduction', 'source_quote': 'PhIS is species and imaging technology neutral and currently provides access to 117,982 images federated from four different data resources with 53,000 regions of interest (ROI) associated to anatomy or phenotype ontology term annotations.'}, {'outcome': "Nombre d'images avec accès à l'annotation (résumé de l'abstract)", 'value': '>100,000', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'PhenoImageShare now provides access to annotation for over 100,000 images for 2 species.'}], 'qualitative_findings': ["Lorsqu'une recherche est effectuée sur 'cardiovascular', les premières images retournées sont celles directement annotées avec des termes contenant 'cardiovascular', suivies des images annotées avec des parties du système cardiovasculaire comme 'blood vessel' ou 'heart'", "La recherche spatiale basique par relation part-of permet, par exemple, qu'une requête sur 'brain' retourne aussi des images annotées avec 'diencephalon'"], 'main_findings': ["PhIS fournit une infrastructure fédérée d'accès et d'annotation d'images phénotypiques accessible via GUI web et services web programmatiques", "La plateforme est neutre en termes d'espèce et de technologie d'imagerie et intègre actuellement des images de Drosophila et de trois projets de souris différents", "L'utilisation d'ontologies améliore l'expérience de recherche et permet une recherche spatiale basique via la relation part-of, avec des extensions futures prévues (gauche/droite, dorsal/ventral, crânial/caudal) issues de la Biological Spatial Ontology"]}

## Conclusions

La plateforme PhenoImageShare fournit l'infrastructure sous-jacente pour l'accès programmatique et des outils destinés aux biologistes, permettant la requête et l'annotation d'images fédérées PhIS s'appuie sur l'utilisation d'ontologies pour offrir la meilleure expérience de recherche et de raisonnement spatial La sortie d'un outil d'annotation activé par ontologie permettra à des projets comme IMPC de fédérer les tâches d'annotation d'images et fournira une plateforme de collaboration pour les annotateurs L'API de requête est exposée pour un accès programmatique, permettant d'envisager facilement des développements pour des options de requête avancées ou pour l'intégration dans d'autres ressources Les auteurs encouragent les propriétaires et générateurs de jeux de données d'images à exposer leurs données via PhIS, en tant que plateforme durable de partage d'images nécessitant un investissement minimal en disque et soutenant un modèle fédéré de partage de données d'images

## PhenoImageShare data

| Resource | Imported images | Life stages | Image types | Specie | Main annotation type |
| --- | --- | --- | --- | --- | --- |
| WTSI KOMP2 | 93861 | Embryo, adult | X-ray, macro photographs, histopathology, lacZ expression | Mus musculus | Ontological |
| TRACER | 702 | Embryo | Expression | Mus musculus | Controlled vocabulary |
| EMAGE | 3566 | Embryo | Expression | Mus musculus | Ontological |
| VFB | 19853 | Adult | Expression | Drosophila melanogaster | Ontological |
