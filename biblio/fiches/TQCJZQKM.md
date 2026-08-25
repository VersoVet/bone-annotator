# Image annotation

**Auteurs** : Franco Marchesoni
**Année** : 2025
**DOI** : 10.70675/1a824e38zb1e5z43f9z9c78z57bdbd6cf48e

## Résumé

Data for training AI can be co-occurrent, simulated, or annotated. Co-occurrent data (e.g., past and future frames, audio-video pairs, text-image pairs, user histories) provides meaningful, abundant supervision suitable for generative models and recommendation systems. Simulated data offers infinite abundance, but its utility depends on the simulation quality. Often, neither type is available, necessitating annotations, particularly expensive expert annotations crucial for industrial solutions. This thesis focuses on image annotation efficiency, proposing Human-in-the-loop (HITL) learning: AI assists annotators, whose corrections iteratively improve the AI. Active learning (AL) complements HITL by selecting data strategically for annotation. The thesis investigates HITL theoretically and practically, developing tools incorporating these findings. The thesis has four parts: Part 1: Interactive Image Segmentation (IIS) * IIS accelerates mask annotation with minimal user interaction. Key

## Méthodologie

{'study_design': "Récit personnel/réflexif rédigé par une annotatrice experte (Adela Barriuso) décrivant son expérience d'annotation d'images avec l'outil LabelMe, traduit de l'espagnol et structuré par Antonio Torralba, avec une introduction et une conclusion ajoutées par ce dernier.", 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': 'Utilisation de LabelMe depuis 2006 ; annotation systématique de la base SUN depuis 2007', 'setting': "Annotation d'images en ligne via l'outil LabelMe, réalisée par l'annotatrice pendant son temps libre dans sa boutique de vêtements"}

## Résultats

{'quantitative': [{'outcome': "Nombre d'objets annotés par l'annotatrice depuis le début de son travail avec LabelMe", 'value': 'more than 250,000', 'unit': 'objets', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Forward by Antonio Torralba', 'source_quote': 'Since she started working with LabelMe, she has labeled more than 250,000 objects.'}], 'qualitative_findings': ['Les objets visibles derrière un miroir, une fenêtre fermée ou une porte de placard vitrée ne sont jamais étiquetés.', "Une fenêtre entièrement occultée par un rideau est étiquetée 'curtain' et non 'window'.", "Les fleurs en pot sont étiquetées 'plant', tandis que les fleurs coupées dans un vase sont étiquetées 'flowers'.", "Le mot 'occluded' est ajouté au nom d'un objet partiellement caché par un autre, sauf lorsque l'occlusion correspond à l'apparence naturelle de l'objet (ex: dos de livres sur une étagère).", "Les murs d'orientations différentes sont toujours annotés comme des instances séparées, même s'ils sont connectés.", 'Les images contenant beaucoup de personnes, de marchés ou de cuisines de restaurant encombrées sont parmi les plus difficiles à annoter en raison de la densité et de la variabilité des objets.', "Le zoom avant/arrière est nécessaire pour le détail, mais peut créer de la confusion sur l'identité des objets, résolue en revenant à la taille originale de l'image.", "L'annotatrice tend à éviter le mot 'pluriel' et préfère annoter chaque instance séparément.", "Certains objets ne sont pas identifiables par l'annotatrice (nom ou fonction inconnus), auquel cas elle passe à l'image suivante plutôt que de deviner.", "L'annotatrice a développé ses propres notebooks organisés par thèmes (cuisine, jeux, salle de bain, meubles, etc.) pour maintenir une terminologie cohérente et éviter les synonymes."], 'main_findings': ["L'acte d'étiqueter des images force la prise de conscience de lacunes dans la compréhension visuelle qui passent inaperçues lors d'une vision quotidienne 'sans effort'.", "Les principales difficultés d'annotation proviennent de noms d'objets inconnus, de choix de dénomination ambigus, des occlusions, des scènes denses/encombrées et des objets derrière des surfaces réfléchissantes ou transparentes.", "L'annotatrice a développé des conventions personnelles (occlusion, miroirs, fenêtres, pluriels) pour garder une cohérence à travers des dizaines de milliers d'annotations.", "Après une longue pratique de l'annotation, la perception quotidienne du monde change (l'annotatrice voit des polygones délimitant les objets et devient particulièrement sensible aux occlusions)."]}

## Conclusions

Étiqueter des images soi-même, même à l'ère du crowd-sourcing permettant de grands jeux de données, reste précieux pour développer une intuition sur les représentations possibles et les limites de la tâche à résoudre. Avant de demander à un ordinateur de segmenter une image ou de reconnaître un objet, il faudrait essayer soi-même la tâche, ce qui permet de mieux juger si la tâche confiée à l'ordinateur est équitable et réalisable.

### Formule


$$• Kitchen • Games • Bathroom • Furniture • Music • Machines • Vegetables • Office • Car • Animals • Boats • Clothing • Chairs and doors • Bed accessories • Things • Airplanes • Parks • Tools$$

### Formule


$$• Frying pan = sarten • Pitcher = jarra • Mug = jarra de cerveza • dishwasher = lavavajillas • Cutting board = tabla • washing machine = lavadora • Dish rack = escurreplatos • tumble dryer = secadora • Knife (set) = cuchillo • Spoon = cuchara • Fork = tenedor • Saltcellar = salero • Bowl = bol • Sink = fregadero • Strainer = colador • Extractor hood = campana • Water cooler =$$
