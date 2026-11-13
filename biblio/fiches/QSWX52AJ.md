# Integration of a Video Annotation Tool into a coactive Learning and Working Environment



## Resume


Integration of a Video Annotation Tool into a coactive Learning and Working Environment

In this paper we describe pedagogic scenarios where the use of a video annotation tool could be of added value to the students' overall learning process. Furthermore, we introduce ViLM, a platform-independent tool for annotating videos collaboratively or on its own and how we integrated the tool in our university's LMS. Finally, we characterise potential research opportunities and learning scenarios where the tool may successfully be applied.

An interactive tool for manual, semi-automatic and automatic video annotation

An Interactive Annotation Method Based on Incremental Learning

Effective image annotation via active learning

Active learning based image annotation

Semi-automatic video semantic annotation based on active learning

Computer Vision Annotation Tool

Context Aware Image Annotation in Active Learning with Batch Mode

Learning the What and How of Annotation in Video Object Segmentation

Active learning with applications in biomedical document annotation

An interactive tool for semi-automated leaf annotation

PyTAGIT: a scalable and interactive human-in-the-loop tool for fast image annotation

Active learning with noise modeling for medical image annotation

A learning-based hybrid tagging and browsing approach for efficient manual image annotation

Image annotation

Data for training AI can be co-occurrent, simulated, or annotated. Co-occurrent data (e.g., past and future frames, audio-video pairs, text-image pairs, user histories) provides meaningful, abundant supervision suitable for generative models and recommendation systems. Simulated data offers infinite abundance, but its utility depends on the simulation quality. Often, neither type is available, necessitating annotations, particularly expensive expert annotations crucial for industrial solutions. This thesis focuses on image annotation efficiency, proposing Human-in-the-loop (HITL) learning: AI assists annotators, whose corrections iteratively improve the AI. Active learning (AL) complements HITL by selecting data strategically for annotation. The thesis investigates HITL theoretically and practically, developing tools incorporating these findings. The thesis has four parts: Part 1: Interactive Image Segmentation (IIS) * IIS accelerates mask annotation with minimal user interaction. Key

Toward Interactive Self-Annotation For Video Object Bounding Box: Recurrent Self-Learning And Hierarchical Annotation Based Framework

Active Learning With Sampling by Uncertainty and Density for Data Annotations


## Quote


we proposed an Interactive Self-Annotation framework to minimize time and human labor costs to annotate bounding box of video objects

We have presented this work as the first modular image annotation platform which seamlessly incorporates image annotation with annotation assistance, active learning and model training and evaluation.

We have presented this work as the first modular image annotation platform which seamlessly incorporates image annotation with annotation assistance, active learning and model training and evaluation.

Our contribution is a flexible pipeline concept to model semi-automatic image and video annotation. This approach allows to combine multiple annotation tools and machine learning algorithms as one process in a building block style.

The proposed work also shows how to maximize the effects of a few annotations, rather than using a deep learning model. In fact, the proposed active learning model can be combined with any machine learning methods, including a deep learning and non-deep learning model.

Une vidéo annotée manuellement sert de référence pour l’évaluation.

Une vidéo annotée manuellement sert de référence pour l’évaluation.

This model combines nearest neighbor approach along with active learning to annotate an unseen image.


## Discussion


Cet article propose un cadre d'annotation sémi-automatique pour vidéos personnelles fondé sur l'apprentissage actif, conçu pour être étendu à l'annotation multi-classes et à d'autres sémantiques telles que la détection d'événements moyennant des caractéristiques adaptées. Le cadre exploite conjointement des caractéristiques statistiques globales et locales afin de traiter la variance vidéo et le manque de données d'entraînement, et regroupe les plans vidéo par sur-segmentation en s'appuyant sur la similarité chromatique et l'ordre temporel, sous l'hypothèse d'une cohérence sémantique au sein de chaque groupe. Le centre de chaque cluster est utilisé comme donnée de test afin d'améliorer l'efficacité du processus d'annotation. Le schéma d'apprentissage actif représentatif proposé, qui tire parti de la distribution a priori de l'espace des caractéristiques approximée par les informations de clustering, obtient de meilleures performances que les schémas d'apprentissage actif classiques.

Cette conclusion présente la plateforme développée comme le premier outil modulaire d'annotation d'images intégrant à la fois l'assistance à l'annotation, l'apprentissage actif et un pipeline d'entraînement/évaluation de modèles. L'assistance à l'annotation, fondée sur une hiérarchie de référence et des images de référence, facilite l'identification d'objets spécifiques à un domaine et réduit ainsi la dépendance à des annotateurs spécialisés, ouvrant la tâche à un public plus large. L'apprentissage actif permet de hiérarchiser les images à annoter, diminuant la charge cognitive des annotateurs, tandis que l'architecture modulaire autorise l'intégration de nouveaux algorithmes de classification et fournit des statistiques de performance comparatives selon les sous-ensembles de données. Les auteurs indiquent que la plateforme continuera d'évoluer, avec des travaux en cours sur l'intégration de nouveaux modèles, l'amélioration des méthodes d'échantillonnage de l'apprentissage actif, la prise en charge d'annotations multiples par image et le calcul de l'accord inter-annotateurs, ainsi qu'une investigation future sur l'influence des propriétés des images sur les résultats des modèles.


## Conclusion


L'outil présenté constitue la première plateforme modulaire d'annotation d'images intégrant de façon transparente l'annotation assistée, l'active learning et l'entraînement/évaluation de modèles. L'assistance à l'annotation via hiérarchie de référence et images de référence réduit le besoin d'annotateurs spécialisés, ouvrant la possibilité que l'annotation soit réalisée par un plus large éventail de personnes. L'active learning priorise efficacement les images à annoter, réduisant la charge cognitive des annotateurs. L'approche modulaire permet l'incorporation de nouveaux algorithmes de classification d'images, et le pipeline d'entraînement/évaluation fournit des statistiques de performance comparatives entre algorithmes sur différents sous-ensembles de données. Des travaux futurs sont prévus : incorporation de nouveaux modèles d'annotation d'images, amélioration de l'active learning via différentes méthodes d'échantillonnage, support des annotations multiples sur une même image avec calcul de l'accord inter-annotateurs, et investigation de l'effet des propriétés des images sur les résultats des modèles.


## Synthese


Cette introduction situe le problème de l'annotation vidéo sémantique dans le contexte de la croissance rapide des contenus multimédias et souligne l'écart persistant entre les caractéristiques de bas niveau et les concepts sémantiques de haut niveau, qui limite l'efficacité de l'annotation automatique. L'annotation manuelle, bien que fiable pour capturer la sémantique, demeure coûteuse en temps et sujette aux erreurs humaines à l'échelle de grandes collections vidéo. Les auteurs positionnent l'apprentissage actif comme une alternative à l'échantillonnage aléatoire pour sélectionner de manière optimale les données à annoter, en s'appuyant sur des travaux antérieurs limités par leur restriction à des modèles linéaires uniformes peu adaptés à la grande variabilité des concepts sémantiques dans les vidéos personnelles. Ils proposent ainsi un cadre semi-automatique exploitant la cohérence locale du contenu vidéo et la relation temporelle entre les plans, combinant un modèle global pré-entraîné hors ligne avec un ajustement local en ligne pendant le processus d'apprentissage actif. Cet article propose un cadre d'annotation sémi-automatique pour vidéos personnelles fondé sur l'apprentissage actif, conçu pour être étendu à l'annotation multi-classes et à d'autres sémantiques telles que la détection d'événements moyennant des caractéristiques adaptées. Le cadre exploite conjointement des caractéristiques statistiques globales et locales afin de traiter la variance vidéo et le manque de données d'entraînement, et regroupe les plans vidéo par sur-segmentation en s'appuyant sur la similarité chromatique et l'ordre temporel, sous l'hypothèse d'une cohérence sémantique au sein de chaque groupe. Le centre de chaque cluster est utilisé comme donnée de test afin d'améliorer l'efficacité du processus d'annotation. Le schéma d'apprentissage actif représentatif proposé, qui tire parti de la distribution a priori de l'espace des caractéristiques approximée par les informations de clustering, obtient de meilleures performances que les schémas d'apprentissage actif classiques.