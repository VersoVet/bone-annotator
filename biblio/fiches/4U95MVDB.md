# Vision6D: 3D-to-2D Interactive Visualization and Annotation Tool for 6D Pose Estimation

**Auteurs** : Yike Zhang, Eduardo Davalos, Jack Noble
**Année** : 2025

## Résumé

Accurate 6D pose estimation has gained more attention over the years for robotics-assisted tasks that require precise interaction with physical objects. This paper presents an interactive 3D-to-2D visualization and annotation tool to support the 6D pose estimation research community. To the best of our knowledge, the proposed work is the first tool that allows users to visualize and manipulate 3D objects interactively on a 2D real-world scene, along with a comprehensive user study. This system supports robust 6D camera pose annotation by providing both visual cues and spatial relationships to determine object position and orientation in various environments. The annotation feature in Vision6D is particularly helpful in scenarios where the transformation matrix between the camera and world objects is unknown, as it enables accurate annotation of these objects' poses using only the camera intrinsic matrix. This capability serves as a foundational step in developing and training advanced

## Méthodologie

{'study_design': 'Étude utilisateur avec deux groupes de participants annotant des poses 6D sur des échantillons de deux jeux de données publics (Linemod et HANDAL), avec répétition des annotations pour évaluer la cohérence intra- et inter-personnelle', 'intervention': "Utilisation de l'outil Vision6D pour annoter des poses 6D d'objets 3D projetés sur des scènes 2D, en ajustant l'orientation et la position de l'objet via des contrôles interactifs jusqu'à correspondance avec le placement de l'objet dans l'image 2D ; certains scénarios incluaient des occlusions partielles pour simuler des environnements réels", 'control': None, 'primary_outcomes': ['Précision des annotations de pose 6D comparées aux poses de référence (ground-truth)'], 'secondary_outcomes': ["Consistance intra-personnelle (au sein d'un même individu)", 'Variabilité inter-personnelle (entre différents individus)', "Utilisabilité et efficacité de l'outil"], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [], 'qualitative_findings': ["La section décrit uniquement la méthodologie d'évaluation (métriques de variabilité intra-personnelle et inter-personnelle) sans présenter de résultats chiffrés"], 'main_findings': ["Le texte fourni ne contient aucun résultat quantitatif ou qualitatif concret : il décrit uniquement l'approche d'évaluation prévue (variabilité intra-personnelle et inter-personnelle) sans rapporter de données, valeurs, ou conclusions issues de cette évaluation"]}

## Conclusions

Vision6D est un outil interactif de visualisation 3D-to-2D et d'annotation de pose conçu pour soutenir la recherche dans le domaine de l'estimation de pose 6D Vision6D est particulièrement utile dans les scénarios où les données de pose de caméra ne sont pas disponibles ou ne peuvent pas être récupérées à partir de vidéos préenregistrées Vision6D a soutenu plusieurs études basées sur l'apprentissage profond, notamment celles proposées dans [24]-[28] Ses contributions ont fait progresser de manière significative la recherche dans divers domaines, tels que l'éducation et la santé Vision6D est développé comme une application de bureau multiplateforme, garantissant accessibilité et facilité d'utilisation L'outil permet aux utilisateurs de manipuler et d'annoter de manière interactive des objets 3D dans des scénarios de scène 2D, comblant l'écart entre les observations d'images 2D et le placement géométrique 3D Une étude utilisateur complète a démontré que Vision6D permet aux utilisateurs de produire des annotations de pose précises et efficaces Vision6D a le potentiel de devenir un outil polyvalent et largement utilisé pour l'annotation et la recherche de pose 6D

## , which summarizes the average annotation time recorded across 11 participants for the two datasets. As shown in the table,

| NASA-TLX Metric | NASA-TLX Metric |
| --- | --- |
| Metric Scores | Metric Scores |
| SUS Questions | SUS Questions |
| Adjusted Scores |  |
| Linemod Dataset |  |

### Formule


$$K =     f x 0 c x 0 0 f y c y 0 0 0 1 0 0 0 0 1     ,(1)$$

### Formule


$$R =   r 1 r 2 r 3 r 4 r 5 r 6 r 7 r 8 r 9   ,(2)$$

### Formule


$$P uvw =     f x 0 c x 0 0 f y c y 0 0 0 1 0 0 0 0 1         r 1 r 2 r 3 t 1 r 4 r 5 r 6 t 2 r 7 r 8 r 9 t 3 0 0 0 1         X Y Z 1    (3)$$

### Formule


$$D rot = arccos Tr(R T R ′ ) -1 2(4)$$

### Formule


$$D add = 1 N N ∑ i=1 ∥(R 1 v i + t 1 ) -(R 2 v i + t 2 )∥(5)$$
