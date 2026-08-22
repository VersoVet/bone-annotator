# DeepEM Playground: Bringing deep learning to electron microscopy labs.

**Auteurs** : Kniesel H, Poonam P, Payer T, Bergner T, Hermosilla P, Ropinski T.
**Année** : 2025
**DOI** : 10.1111/jmi.70005

## Résumé

Deep learning (DL) has transformed image analysis, enabling breakthroughs in segmentation, object detection, and classification. However, a gap persists between cutting-edge DL research and its practical adoption in electron microscopy (EM) labs. This is largely due to the inaccessibility of DL methods for EM specialists and the expertise required to interpret model outputs. To bridge this gap, we introduce DeepEM Playground, an interactive, user-friendly platform designed to empower EM researchers - regardless of coding experience - to train, tune, and apply DL models. By providing a guided, hands-on approach, DeepEM Playground enables users to explore the workings of DL in EM, facilitating both first-time engagement and more advanced model customisation. The DeepEM Playground lowers the barrier to entry and fosters a deeper understanding of deep learning, thereby enabling the EM community to integrate AI-driven analysis into their workflows more confidently and effectively.

## Méthodologie

{'study_design': "Article de présentation d'une plateforme logicielle (platform/tool paper) organisée autour de trois cas d'usage exemplaires illustrant l'application du DL à l'EM, regroupés en trois catégories de tâches : 'Image to Value(s)', 'Image to Image', et '2D to 3D'", 'intervention': "Développement et démonstration de la plateforme DeepEM Playground, incluant un workflow standardisé (Development et Inference), une interface d'annotation de données (CVAT), une infrastructure cloud (Lightning AI Studios), et une bibliothèque PyTorch (deepem) pour les contributions d'experts DL", 'control': None, 'primary_outcomes': ['Modèle de régression pour la quantification explicable de capsides virales (HCMV) via ResNet50 avec Grad-CAM', 'Segmentation sémantique de structures cellulaires via modèle ensemble basé sur U-Net', "Reconstruction tomographique auto-supervisée d'une série d'inclinaison STEM 2D en 3D"], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': 'Plateforme web basée sur infrastructure cloud (Lightning AI Studios), accessible à https://viscom-ulm.github.io/DeepEM/'}

## Résultats

{'quantitative': [], 'qualitative_findings': ["L'approche de reconstruction tomographique auto-supervisée (Section 2D to 3D) a montré des résultats prometteurs, en particulier pour supprimer l'effet du 'missing wedge', surpassant les techniques de reconstruction traditionnelles telles que Weighted Backprojection (WBP) et Simultaneous Iterative Reconstruction Technique (SIRT)", "L'utilisation d'un modèle ensemble pour la segmentation sémantique a montré une robustesse accrue, en particulier avec des jeux de données de petite taille (référence à l'étude 7)"], 'main_findings': ["DeepEM Playground permet aux chercheurs EM sans expérience en programmation d'entraîner, tester et développer des modèles DL", "La plateforme organise les cas d'usage EM en trois catégories de tâches : Image to Value(s), Image to Image, et 2D to 3D", "Le workflow intègre une interface d'annotation de données (CVAT) permettant aux utilisateurs d'annoter leurs propres données spécifiques au laboratoire", 'La plateforme fonctionne sur une infrastructure cloud (Lightning AI Studios), éliminant le besoin de ressources de calcul haute performance locales', 'Une bibliothèque PyTorch (deepem) facilite les contributions des experts DL pour étendre le workflow']}

## Conclusions

DeepEM Playground introduit de nouvelles opportunités de collaboration entre chercheurs EM et DL en fournissant une plateforme conviviale ne nécessitant pas d'expertise en programmation La plateforme permet aux chercheurs d'adapter facilement les cas d'usage aux besoins spécifiques de leur laboratoire en remplaçant simplement les données d'entraînement, grâce à des formats d'annotation d'image standardisés basés sur l'outil CVAT Le workflow standardisé facilite l'intégration des méthodes DL de pointe dans la recherche EM En exploitant Lightning AI Studios, la plateforme élimine les complexités et coûts des environnements et configurations GPU DeepEM Playground permet aux spécialistes EM d'exploiter les techniques DL pour une analyse plus précise, reproductible et efficace des données EM

### Formule


$$F I G U R E 1$$

### Formule


$$F I G U R E 3$$

### Formule


$$F I G U R E 5$$

### Formule


$$F I G U R E 6$$
