# Image annotation

**Auteurs** : Franco Marchesoni
**Année** : 2025
**DOI** : 10.70675/1a824e38zb1e5z43f9z9c78z57bdbd6cf48e

## Résumé

Data for training AI can be co-occurrent, simulated, or annotated. Co-occurrent data (e.g., past and future frames, audio-video pairs, text-image pairs, user histories) provides meaningful, abundant supervision suitable for generative models and recommendation systems. Simulated data offers infinite abundance, but its utility depends on the simulation quality. Often, neither type is available, necessitating annotations, particularly expensive expert annotations crucial for industrial solutions. This thesis focuses on image annotation efficiency, proposing Human-in-the-loop (HITL) learning: AI assists annotators, whose corrections iteratively improve the AI. Active learning (AL) complements HITL by selecting data strategically for annotation. The thesis investigates HITL theoretically and practically, developing tools incorporating these findings. The thesis has four parts: Part 1: Interactive Image Segmentation (IIS) * IIS accelerates mask annotation with minimal user interaction. Key

## Méthodologie

{'study_design': "Rapport narratif/notes d'expérience rédigées par une annotatrice experte pendant son travail d'annotation d'images avec l'outil LabelMe, traduites de l'espagnol vers l'anglais par Antonio Torralba", 'intervention': "Utilisation de l'outil d'annotation en ligne LabelMe pour délimiter (polygones) et nommer tous les objets présents dans chaque image de la base de données SUN", 'control': None, 'primary_outcomes': ["Difficultés rencontrées lors de l'annotation d'images", "Stratégies et heuristiques développées pour l'annotation cohérente"], 'secondary_outcomes': ['Gestion du vocabulaire et de la nomenclature des objets', 'Gestion des occlusions, objets non identifiables, réflexions, objets vus à travers des surfaces transparentes'], 'statistical_methods': [], 'duration': "De 2006/2007 jusqu'à la rédaction du document (non précisée exactement)", 'setting': "Travail réalisé dans une petite boutique de vêtements pendant les heures d'inactivité, en utilisant l'outil en ligne LabelMe"}

## Résultats

{'quantitative': [{'outcome': "Nombre d'objets annotés", 'value': 'plus de 250 000', 'unit': 'objets', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Forward by Antonio Torralba', 'source_quote': 'Since she started working with LabelMe, she has labeled more than 250,000 objects.'}, {'outcome': "Nombre d'étiquettes sur une image complexe (marché)", 'value': 'plus de 100', 'unit': 'labels', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Notes from an annotator', 'source_quote': 'Once I finished with this image there were more than 100 labels.'}], 'qualitative_findings': ["L'annotation d'images révèle des 'angles morts sémantiques' où l'on ne remarque pas notre ignorance du nom ou de la fonction d'objets tant qu'on n'est pas obligé de les nommer explicitement", "L'ordre d'annotation privilégié va des grandes surfaces (ciel, plafond, murs, sol) vers les petits éléments", "Les objets occlus sont systématiquement étiquetés avec le mot 'occluded' dans leur nom, sauf lorsque l'occlusion fait partie de l'apparence naturelle de l'objet (ex: livres sur une étagère)", "Les objets visibles derrière une vitre, un miroir ou une fenêtre fermée ne sont généralement pas annotés (règle personnelle de l'annotatrice)", "Les murs d'orientations différentes sont annotés comme des instances séparées même s'ils sont connectés", "L'annotatrice évite d'utiliser le pluriel et préfère annoter chaque instance séparément", 'Les images de marchés, cuisines de restaurant et scènes avec beaucoup de personnes sont parmi les plus difficiles à annoter en raison de la variabilité des objets ou du chevauchement des instances', "Le zoom avant/arrière peut créer de la confusion sur l'identité des objets (ex: confondre une porte avec un élément de cheminée, ou un mur avec un miroir)", "L'annotatrice a développé ses propres carnets de vocabulaire organisés par thèmes pour maintenir une nomenclature cohérente et éviter les synonymes", "Face à des objets non identifiables, l'annotatrice choisit souvent de les ignorer ou de sauter l'image entière"], 'main_findings': ["L'acte de voir n'est pas aussi effortless qu'on le croit; l'annotation d'images révèle les limites de notre compréhension visuelle et sémantique", "La cohérence terminologique (éviter les synonymes, nommer toujours de la même façon) est un défi majeur lorsque la liste des catégories n'est pas fixée à l'avance", "Le processus d'annotation, malgré les efforts de l'annotatrice, n'est pas exempt de bruit ('the process is not free of noise')", "Des règles pragmatiques et parfois arbitraires (ex: ne pas annoter les objets derrière des fenêtres fermées, distinguer 'plant' et 'flowers') sont nécessaires pour gérer les cas ambigus de façon cohérente"]}

## Conclusions

Ce document peut aider le lecteur à développer une intuition sur les problèmes qui surviennent lors de l'annotation d'images Cela ne dispense pas le lecteur d'annoter lui-même quelques images Avant de demander à un ordinateur de segmenter une image ou de reconnaître un objet, il faudrait essayer soi-même la tâche, ce qui rapproche d'une meilleure compréhension de si l'on donne à l'ordinateur une chance équitable de résoudre la tâche

### Formule


$$• Kitchen • Games • Bathroom • Furniture • Music • Machines • Vegetables • Office • Car • Animals • Boats • Clothing • Chairs and doors • Bed accessories • Things • Airplanes • Parks • Tools$$

### Formule


$$• Frying pan = sarten • Pitcher = jarra • Mug = jarra de cerveza • dishwasher = lavavajillas • Cutting board = tabla • washing machine = lavadora • Dish rack = escurreplatos • tumble dryer = secadora • Knife (set) = cuchillo • Spoon = cuchara • Fork = tenedor • Saltcellar = salero • Bowl = bol • Sink = fregadero • Strainer = colador • Extractor hood = campana • Water cooler =$$
