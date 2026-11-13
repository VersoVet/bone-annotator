# Efficient labeling: is prompt-based annotation a viable alternative to manual labeling in endoscopy video segmentation?



## Resume


Efficient labeling: is prompt-based annotation a viable alternative to manual labeling in endoscopy video segmentation?

Progressive medical image annotation with convolutional neural network-based interactive segmentation method

An annotation tool for dermoscopic image segmentation

A learning-based hybrid tagging and browsing approach for efficient manual image annotation

ACTIVE DEEP ENSEMBLE LEARNING FRAMEWORK FOR AUTOMATED SURGICAL VIDEO SEGMENTATION AND EFFICIENT ANNOTATION IN MINIMALLY INVASIVE PROCEDURES

Surgical video analysis has become an essential component in computer-assisted interventions and clinical documentation. The rapid growth of minimally invasive surgery has produced large volumes of surgical recordings that require detailed frame-level annotations for training intelligent systems. Manual annotation of surgical videos remains a labor-intensive and time-consuming process that often requires expert knowledge. As a result, the development of automated annotation systems has become a critical research direction in medical image analysis. Existing segmentation and annotation approaches have faced limitations in handling complex surgical scenes, instrument occlusions, illumination variations, and tissue deformation. Conventional deep learning models often rely on large labelled datasets, whereas surgical datasets usually remain limited due to the difficulty of manual labeling. This challenge has reduced the reliability and scalability of automated surgical video segmentation s

Large-vocabulary segmentation for medical images with text prompts

Novel artificial intelligence-driven software significantly shortens the time required for annotation in computer vision projects

Background and study aims The contribution of artificial intelligence (AI) to endoscopy is rapidly expanding. Accurate labelling of source data (video frames) remains the rate-limiting step for such projects and is a painstaking, cost-inefficient, time-consuming process. A novel software platform, Cord Vision (CdV) allows automated annotation based on “embedded intelligence.” The user manually labels a representative proportion of frames in a section of video (typically 5 %), to create ‘micro-modelsʼ which allow accurate propagation of the label throughout the remaining video frames. This could drastically reduce the time required for annotation.  
          Methods We conducted a comparative study with an open-source labelling platform (CVAT) to determine speed and accuracy of labelling. 
          Results Across 5 users, CdV resulted in a significant increase in labelling performance (P < 0.001) compared to CVAT for bounding box placement. 
          Conclusions This advance represen

Medical Image Segmentation with Efficient Use of Annotations and Resources

Pseudo Label-based Multi-View Annotation for Semi-Supervised Medical Image Segmentation

Image Segmentation and Labeling Using Free-Form Semantic Annotation

A machine learning pipeline for automatic segmentation and grading on digital pathology images that is robust to annotation noise and uses dynamic sampling

VR-based annotation assistance system for volumetric medical image segmentation

An interactive tool for manual, semi-automatic and automatic video annotation

AI-Enhanced Annotation Tool for Aneurysm Medical Image Labeling

Annotating Medical Image Data


## Synthese


L'objectif principal de cette étude était de déterminer si un logiciel d'annotation vidéo piloté par l'intelligence artificielle, Cord Vision (CdV), pouvait réduire significativement le temps requis pour annoter des vidéos d'endoscopie digestive par rapport à une plateforme d'annotation manuelle open-source de référence, CVAT. Cette question est motivée par le constat que l'annotation manuelle frame-par-frame constitue un goulot d'étranglement majeur limitant le développement rapide d'algorithmes de vision par ordinateur en endoscopie, notamment pour la détection de polypes. Les hypothèses testées portaient sur trois axes : la vitesse d'annotation, la précision du placement des bounding boxes, et la proportion de travail pouvant être automatisée via des micro-modèles entraînés sur une fraction minime des données (environ 5 %) combinés à des algorithmes de tracking. Un objectif secondaire visait également à caractériser la relation entre le nombre de frames étiquetées manuellement et la qualité prédictive des micro-modèles générés.

La segmentation d’images médicales est freinée par le coût, le temps et les contraintes éthiques liés à l’annotation manuelle, ce qui motive le développement de méthodes few-shot ne reposant pas sur de vastes corpus annotés. Les auteurs positionnent SAM comme une alternative prometteuse, tout en soulignant que le fine-tuning classique exige encore trop de masques et que le prompting manuel demeure peu efficace. SAM-MPA est proposé pour adapter SAM à la segmentation few-shot via trois volets : sélection de supports représentatifs par clustering, propagation de masques par recalage non supervisé, puis génération automatique de prompts (points de premier plan/arrière-plan et boîtes englobantes). Les contributions rapportées indiquent des Dice de 82,07 % (Breast US) et 94,13 % (Chest X-ray) avec seulement 1 à 10 échantillons annotés. Les protocoles expérimentaux évaluent les réglages 1-, 5- et 10-shot (encodeur vit_b, recalage B-Spline, métrique Dice) et comparent le prompting automatique à des prompts manuels SAM ainsi qu’à PerSAM.

La segmentation d’images médicales est freinée par le coût, le temps et les contraintes éthiques liés à l’annotation manuelle, ce qui motive le développement de méthodes few-shot ne reposant pas sur de vastes corpus annotés. Les auteurs positionnent SAM comme une alternative prometteuse, tout en soulignant que le fine-tuning classique exige encore trop de masques et que le prompting manuel demeure peu efficace. SAM-MPA est proposé pour adapter SAM à la segmentation few-shot via trois volets : sélection de supports représentatifs par clustering, propagation de masques par recalage non supervisé, puis génération automatique de prompts (points de premier plan/arrière-plan et boîtes englobantes). Les contributions rapportées indiquent des Dice de 82,07 % (Breast US) et 94,13 % (Chest X-ray) avec seulement 1 à 10 échantillons annotés. Les protocoles expérimentaux évaluent les réglages 1-, 5- et 10-shot (encodeur vit_b, recalage B-Spline, métrique Dice) et comparent le prompting automatique à des prompts manuels SAM ainsi qu’à PerSAM.

Cette étude publiée en 2021 dans Endoscopy International Open évalue un logiciel d'annotation vidéo piloté par l'intelligence artificielle, Cord Vision (CdV), conçu pour réduire le temps considérable requis pour étiqueter manuellement des images en vue de l'entraînement de modèles de vision par ordinateur en endoscopie digestive. L'objectif principal était de comparer la vitesse et la précision d'annotation de CdV, qui repose sur des 'micro-modèles' entraînés sur une fraction représentative des images (environ 5 %) pour propager automatiquement les annotations, par rapport à CVAT (Computer Vision Annotation Tool), une plateforme open-source d'annotation manuelle de référence. Le design était une étude comparative appariée impliquant cinq annotateurs indépendants travaillant sur un sous-échantillon de vidéos de polypes issu du dataset Hyper-Kvasir, chargés de dessiner des bounding boxes autour des polypes identifiés sur les deux plateformes, avec analyse statistique par test de Wilcoxon sur données appariées. Sur une session de 120 minutes, CdV a permis d'étiqueter en moyenne 10674 ± 5388 frames contre seulement 2241 ± 810 frames avec CVAT (représentant moins de 10 % du dataset total), une différence statistiquement significative (P = 0.01). La vitesse moyenne d'annotation était de 121 frames/minute avec CdV contre 18.7 frames/minute avec CVAT, soit une augmentation de 6.4 fois (P = 0.04), et la dynamique globale d'étiquetage était également significativement plus rapide avec CdV (P < 0.001). Trois des cinq annotateurs ont réussi à épuiser entièrement le dataset du projet avec CdV en un temps moyen de 99.1 ± 15.2 minutes, alors qu'aucun n'y est parvenu avec CVAT. Fait notable, seulement 3.44 % ± 2.71 % des labels produits avec CdV étaient dessinés manuellement, le reste étant généré automatiquement par des modèles ou des algorithmes de tracking, bien qu'une révision manuelle de ces labels automatiques ait nécessité en moyenne 36.8 ± 12.8 minutes du temps alloué. L'expérience sur la qualité des micro-modèles a montré que la précision moyenne saturait entre 61.2 % et 65.2 % à partir d'environ 3900 frames étiquetées (seuil IoU 50:95), atteignant 95.9-97.1 % à un seuil IoU de 0.5, ce qui indique que les micro-modèles identifiaient rarement des régions complètement erronées comme polypes mais que les boîtes produites pouvaient nécessiter des ajustements fins. Les auteurs concluent qu'il s'agit de la première description d'un logiciel d'annotation vidéo pour l'endoscopie supprimant le besoin d'étiqueter chaque frame manuellement, avec une amélioration spectaculaire de l'efficacité, même en tenant compte du temps de révision additionnel. Les principales limites tiennent à la petite taille de l'échantillon (N=5 annotateurs), à l'absence de comparaison sur une tâche autre que la détection de polypes, et à la variabilité des stratégies individuelles adoptées par les annotateurs avec CdV, ce qui pourrait affecter la généralisabilité des gains d'efficacité mesurés.

L'essor du deep learning en imagerie médicale a considérablement accru la demande en données annotées de haute qualité, ces annotations (Ground-Truth) étant indispensables à l'entraînement, aux tests et à l'évaluation des modèles de diagnostic assisté par ordinateur (CAD). Les outils d'annotation se répartissent en trois modalités - manuelle, semi-automatique et automatique - et prennent en charge diverses techniques graphiques telles que les polygones, points, lignes, polylignes ou masques dessinés à main levée, appliquées à des tâches allant de la classification d'image à la segmentation au niveau du pixel. Une revue comparative de 13 outils d'annotation d'images médicales, évalués selon sept critères (plateforme, zoom, coût, formats d'entrée/sortie, types d'annotation graphique et méthode d'annotation), montre que malgré leur caractère chronophage et leur coût en ressources humaines expertes, les outils d'annotation manuelle demeurent les plus répandus dans le domaine médical. Les approches semi-automatiques et automatiques, quant à elles, permettraient de réduire le temps et les efforts requis tout en offrant de meilleurs résultats comparativement à l'annotation strictement manuelle. Cette étude compare 13 outils d'annotation d'images médicales testés personnellement par les auteurs selon sept critères (plateforme web/desktop, zoom, coût, types d'entrée/sortie, types d'annotation graphique et méthode d'annotation). Les résultats montrent des limitations variables selon les outils, notamment en matière de formats de fichiers médicaux supportés (3D-Slicer, ITK-SNAP et Supervisely acceptant le plus grand nombre de formats), de compatibilité multiplateforme et de gestion collaborative multi-annotateurs. Une expérience comparative sur un cas de segmentation de calcification artérielle mammaire a permis d'évaluer le temps et le coût de chaque outil, révélant que Ratsnake était le plus rapide et LabelMe le plus lent parmi les outils utilisant la méthode polygonale, tandis que les outils web (VIA, Supervisely, CVAT, LabelBox) présentent l'avantage de ne pas nécessiter d'espace mémoire local. Les auteurs concluent que les outils d'annotation manuelle restent les plus utilisés dans le domaine médical malgré leur coût en temps et en ressources humaines expertes, tandis que l'annotation semi-automatique et automatique offre un gain d'efficacité potentiel encore sous-exploité.


## Quote


This is the first description of software being used to annotate video frames for endoscopy, removing the need to have each frame labelled manually, and it showed a dramatic improvement in efficiency and task completion.

We presented an alternative and efficient way to annotate objects in videos with segmentation masks.

There is a need for innovative methodologies that enable annotation-efficient deep learning for medical imaging

Our annotation-efficient method greatly reduces the human labeling cost while achieving performances close to fully-supervised methods.


## Raw_Related_Work


Annotations. Recent large-scale natural image datasets [21,22,37,63] were annotated by crowdsourcing, weak supervision, or prompt-based interactive labeling. It relied on large pools of annotators and simplified 2D primitives. However, such strategies do not transfer to 3D medical imaging, especially annotating tumors, where voxel-wise annotation demands anatomical accuracy, cross-slice consistency, and domain-specific knowledge. Given these challenges, recent medical datasets speed up manual annotations through Active Learning [7,36,60,64] and Humanin-the-Loop [27,41,53]. These approaches improve annotation efficiency by prioritizing uncertain samples for expert refine. In contrast, our EM process make >95% expert refinement automated to further reduce the manual efforts. Datasets. Earlier pancreatic CT datasets [34,54] [47,48]. We address this limitation by introducing an iterative EM process that continually refines both data (PanTS-XL) and model (Flagship Model) quality. The model

Annotations. Recent large-scale natural image datasets [21,22,37,63] were annotated by crowdsourcing, weak supervision, or prompt-based interactive labeling. It relied on large pools of annotators and simplified 2D primitives. However, such strategies do not transfer to 3D medical imaging, especially annotating tumors, where voxel-wise annotation demands anatomical accuracy, cross-slice consistency, and domain-specific knowledge. Given these challenges, recent medical datasets speed up manual annotations through Active Learning [7,36,60,64] and Humanin-the-Loop [27,41,53]. These approaches improve annotation efficiency by prioritizing uncertain samples for expert refine. In contrast, our EM process make >95% expert refinement automated to further reduce the manual efforts. Datasets. Earlier pancreatic CT datasets [34,54] [47,48]. We address this limitation by introducing an iterative EM process that continually refines both data (PanTS-XL) and model (Flagship Model) quality. The model


## Methodologie


La segmentation d’images médicales est freinée par le coût, le temps et les contraintes éthiques liés à l’annotation manuelle, ce qui motive le développement de méthodes few-shot ne reposant pas sur de vastes corpus annotés. Les auteurs positionnent SAM comme une alternative prometteuse, tout en soulignant que le fine-tuning classique exige encore trop de masques et que le prompting manuel demeure peu efficace. SAM-MPA est proposé pour adapter SAM à la segmentation few-shot via trois volets : sélection de supports représentatifs par clustering, propagation de masques par recalage non supervisé, puis génération automatique de prompts (points de premier plan/arrière-plan et boîtes englobantes). Les contributions rapportées indiquent des Dice de 82,07 % (Breast US) et 94,13 % (Chest X-ray) avec seulement 1 à 10 échantillons annotés. Les protocoles expérimentaux évaluent les réglages 1-, 5- et 10-shot (encodeur vit_b, recalage B-Spline, métrique Dice) et comparent le prompting automatique à des prompts manuels SAM ainsi qu’à PerSAM.

La segmentation d’images médicales est freinée par le coût, le temps et les contraintes éthiques liés à l’annotation manuelle, ce qui motive le développement de méthodes few-shot ne reposant pas sur de vastes corpus annotés. Les auteurs positionnent SAM comme une alternative prometteuse, tout en soulignant que le fine-tuning classique exige encore trop de masques et que le prompting manuel demeure peu efficace. SAM-MPA est proposé pour adapter SAM à la segmentation few-shot via trois volets : sélection de supports représentatifs par clustering, propagation de masques par recalage non supervisé, puis génération automatique de prompts (points de premier plan/arrière-plan et boîtes englobantes). Les contributions rapportées indiquent des Dice de 82,07 % (Breast US) et 94,13 % (Chest X-ray) avec seulement 1 à 10 échantillons annotés. Les protocoles expérimentaux évaluent les réglages 1-, 5- et 10-shot (encodeur vit_b, recalage B-Spline, métrique Dice) et comparent le prompting automatique à des prompts manuels SAM ainsi qu’à PerSAM.


## Discussion


Les auteurs interprètent ces résultats comme la première démonstration qu'un logiciel d'annotation vidéo peut supprimer le besoin d'étiqueter chaque frame manuellement en endoscopie, avec une amélioration spectaculaire de l'efficacité et du taux de complétion des tâches par rapport à une plateforme manuelle de référence comme CVAT. Ils attribuent la supériorité de CdV notamment à la performance de son algorithme de tracking d'objets, plus robuste que les fonctionnalités de propagation de CVAT face aux trajectoires non linéaires des polypes en mouvement dans les vidéos. Sur le plan des implications pratiques, les auteurs soulignent que même en intégrant le temps additionnel nécessaire à la révision et à la correction des labels générés automatiquement (36.8 ± 12.8 minutes en moyenne), le temps global reste plusieurs fois inférieur à celui d'une plateforme manuelle, validant l'intérêt net de l'approche pour accélérer les projets d'analyse d'images par IA. Cette avancée est présentée comme une première étape précieuse pour la constitution de datasets annotés à grande échelle en endoscopie. Les limites principales concernent la petite taille de l'échantillon (5 annotateurs), la dépendance de la qualité des micro-modèles au volume de frames d'entraînement disponibles (avec dégradation notable en cas de faible nombre de labels), et l'hétérogénéité des stratégies d'utilisation adoptées par les annotateurs, qui n'a pas été formellement contrôlée dans l'analyse.


## Conclusion


There is a need for innovative methodologies that enable annotation-efficient deep learning for medical imaging