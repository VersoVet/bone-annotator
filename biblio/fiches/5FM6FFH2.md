# RIL-Contour: a Medical Imaging Dataset Annotation Tool for and with Deep Learning.

**Auteurs** : Kenneth A Philbrick, Alexander D Weston, Zeynettin Akkus, Timothy L Kline, Panagiotis Korfiatis, Tomas Sakinis, Petro Kostandy, Arunnit Boonrod, Atefeh Zeinoddini, Naoki Takahashi, Bradley J Erickson
**Année** : 2019
**DOI** : 10.1007/s10278-019-00232-0

## Résumé

Deep-learning algorithms typically fall within the domain of supervised artificial intelligence and are designed to "learn" from annotated data. Deep-learning models require large, diverse training datasets for optimal model convergence. The effort to curate these datasets is widely regarded as a barrier to the development of deep-learning systems. We developed RIL-Contour to accelerate medical image annotation for and with deep-learning. A major goal driving the development of the software was to create an environment which enables clinically oriented users to utilize deep-learning models to rapidly annotate medical imaging. RIL-Contour supports using fully automated deep-learning methods, semi-automated methods, and manual methods to annotate medical imaging with voxel and/or text annotations. To reduce annotation error, RIL-Contour promotes the standardization of image annotations across a dataset. RIL-Contour accelerates medical imaging annotation through the process of annotation

## Méthodologie

{'study_design': "Article descriptif présentant le développement d'un outil logiciel (RIL-Contour) et d'une méthodologie associée (Annotation by Iterative Deep Learning, AID)", 'intervention': "Développement d'un logiciel utilisant un moteur de plugins pour charger et exécuter des modèles de deep learning (Keras/Tensorflow) au runtime afin d'automatiser l'annotation d'images médicales", 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': "Environnement de recherche collaboratif impliquant analystes d'images, radiologistes et data scientists/ingénieurs"}

## Résultats

{'quantitative': [], 'qualitative_findings': ["RIL-Contour permet l'exécution de modèles Keras/Tensorflow via un moteur de plugin qui charge le modèle, normalise/transforme l'imagerie d'entrée, exécute le modèle et transforme la sortie en annotations voxel RIL-Contour", "RIL-Contour supporte les visualisations SAM et Grad-CAM pour les couches convolutionnelles et d'activation avec fonctions d'activation non linéaires", "RIL-Contour gère l'association entre données d'imagerie et métadonnées d'annotation pour des datasets stockés sur le système de fichiers ou dans un système MIRMAID", 'Contrairement à DeepInfer (basé sur Docker), RIL-Contour interagit directement avec les modèles, permettant des visualisations avancées basées sur la réécriture du modèle et le calcul de sorties/gradients de couches arbitraires'], 'main_findings': ["RIL-Contour a été conçu pour accélérer l'annotation d'imagerie médicale via trois moyens : simplifier le travail collaboratif sur de grands datasets, permettre l'utilisation directe de modèles de deep learning pour l'annotation automatisée, et faciliter la visualisation/compréhension des modèles de deep learning", "La méthodologie AID (Annotation by Iterative Deep Learning) permet d'annoter, entraîner et utiliser itérativement des modèles de deep learning pendant le développement d'un dataset", "RIL-Contour standardise les définitions d'annotations (nom de ROI, RadLex ID, valeur de masque voxel) de façon cohérente à travers tout le dataset"]}

## Conclusions

RIL-Contour accélère l'annotation de datasets d'imagerie médicale pour le deep learning en standardisant les définitions d'annotations et en facilitant l'application de modèles de deep learning pour l'annotation automatisée de texte et de voxels RIL-Contour supporte des workflows collaboratifs et accélère l'annotation via le processus AID, où des modèles de deep learning sont itérativement entraînés et utilisés pour générer des annotations provisoires ensuite éditées si nécessaire
