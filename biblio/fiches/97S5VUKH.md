# Annotix: An Integrated Desktop Platform for Multi-Modal Data Annotation, Collaborative Labeling, and End-to-End Machine Learning Training



## Resume


Annotix: An Integrated Desktop Platform for Multi-Modal Data Annotation, Collaborative Labeling, and End-to-End Machine Learning Training

The preparation of annotated datasets remains a critical bottleneck in the machine learning (ML) pipeline. Existing tools are fragmented across cloud-hosted services, self-hosted web applications, and lightweight desktop tools—none simultaneously ad-dressing diverse annotation modalities, offline-first operation, integrated training, and serverless collaboration. We present Annotix, an open-source, cross-platform desktop application built on a Rust backend (Tauri 2) and React 19 frontend, designed to unify the entire ML data preparation workflow within a single privacy-preserving environ-ment. To evaluate its practical utility, we conducted a controlled annotation efficiency study using 60 synthetic images (bounding box and mask tasks) annotated by three expert evaluators across Annotix, CVAT, and Label Studio, analyzed via Krus-kal-Wallis with Dunn–Bonferroni post-hoc tests, and a heuristic usability evaluation over standardized tasks on real medical images (retinographies and otoscop

Cross-Model Image Annotation Platform with Active Learning

We have seen significant leapfrog advancement in machine learning in recent decades. The central idea of machine learnability lies on constructing learning algorithms that learn from good data. The availability of more data being made publicly available also accelerates the growth of AI in recent years. In the domain of computer vision, the quality of image data arises from the accuracy of image annotation. Labeling large volume of image data is a daunting and tedious task. This work presents an End-to-End pipeline tool for object annotation and recognition aims at enabling quick image labeling. We have developed a modular image annotation platform which seamlessly incorporates assisted image annotation (annotation assistance), active learning and model training and evaluation. Our approach provides a number of advantages over current image annotation tools. Firstly, the annotation assistance utilizes reference hierarchy and reference images to locate the objects in the images, thus re

Deep Learning-Based Annotation Transfer between Molecular Imaging Modalities: An Automated Workflow for Multimodal Data Integration

Hands-On Tutorial: Labeling with LLM and Human-in-the-Loop

Training and deploying machine learning models relies on a large amount of human-annotated data. As human labeling becomes increasingly expensive and time-consuming, recent research has developed multiple strategies to speed up annotation and reduce costs and human workload: generating synthetic training data, active learning, and hybrid labeling. This tutorial is oriented toward practical applications: we will present the basics of each strategy, highlight their benefits and limitations, and discuss in detail real-life case studies. Additionally, we will walk through best practices for managing human annotators and controlling the quality of the final dataset. The tutorial includes a hands-on workshop, where attendees will be guided in implementing a hybrid annotation setup. This tutorial is designed for NLP practitioners from both research and industry backgrounds who are involved in or interested in optimizing data labeling projects.

Smart Data Annotation: Accelerating Data Labeling Processes through Deep Learning

LabelMe: Online Image Annotation and Applications

LabelMe: A Database and Web-Based Tool for Image Annotation

VisioFirm: Cross-Platform AI-assisted Annotation Tool for Computer Vision

AI models rely on annotated data to learn pattern and perform prediction. Annotation is usually a labor-intensive step that require associating labels ranging from a simple classification label to more complex tasks such as object detection, oriented bounding box estimation, and instance segmentation. Traditional tools often require extensive manual input, limiting scalability for large datasets. To address this, we introduce VisioFirm, an open-source web application designed to streamline image labeling through AI-assisted automation. VisioFirm integrates state-of-the-art foundation models into an interface with a filtering pipeline to reduce human-in-the-loop efforts. This hybrid approach employs CLIP combined with pre-trained detectors like Ultralytics models for common classes and zero-shot models such as Grounding DINO for custom labels, generating initial annotations with low-confidence thresholding to maximize recall. Through this framework, when tested on COCO-type of classes,

ActiveLab: Active Learning with Re-Labeling by Multiple Annotators

In real-world data labeling applications, annotators often provide imperfect labels. It is thus common to employ multiple annotators to label data with some overlap between their examples. We study active learning in such settings, aiming to train an accurate classifier by collecting a dataset with the fewest total annotations. Here we propose ActiveLab, a practical method to decide what to label next that works with any classifier model and can be used in pool-based batch active learning with one or multiple annotators. ActiveLab automatically estimates when it is more informative to re-label examples vs. labeling entirely new ones. This is a key aspect of producing high quality labels and trained models within a limited annotation budget. In experiments on image and tabular data, ActiveLab reliably trains more accurate classifiers with far fewer annotations than a wide variety of popular active learning methods.

Callico: a Versatile Open-Source Document Image Annotation Platform

This paper presents Callico, a web-based open source platform designed to simplify the annotation process in document recognition projects. The move towards data-centric AI in machine learning and deep learning underscores the importance of high-quality data, and the need for specialised tools that increase the efficiency and effectiveness of generating such data. For document image annotation, Callico offers dual-display annotation for digitised documents, enabling simultaneous visualisation and annotation of scanned images and text. This capability is critical for OCR and HTR model training, document layout analysis, named entity recognition, form-based key value annotation or hierarchical structure annotation with element grouping. The platform supports collaborative annotation with versatile features backed by a commitment to open source development, high-quality code standards and easy deployment via Docker. Illustrative use cases - including the transcription of the Belfort munic


## Conclusion


L'outil présenté constitue la première plateforme modulaire d'annotation d'images intégrant de façon transparente l'annotation assistée, l'active learning et l'entraînement/évaluation de modèles. L'assistance à l'annotation via hiérarchie de référence et images de référence réduit le besoin d'annotateurs spécialisés, ouvrant la possibilité que l'annotation soit réalisée par un plus large éventail de personnes. L'active learning priorise efficacement les images à annoter, réduisant la charge cognitive des annotateurs. L'approche modulaire permet l'incorporation de nouveaux algorithmes de classification d'images, et le pipeline d'entraînement/évaluation fournit des statistiques de performance comparatives entre algorithmes sur différents sous-ensembles de données. Des travaux futurs sont prévus : incorporation de nouveaux modèles d'annotation d'images, amélioration de l'active learning via différentes méthodes d'échantillonnage, support des annotations multiples sur une même image avec calcul de l'accord inter-annotateurs, et investigation de l'effet des propriétés des images sur les résultats des modèles.

La plateforme présentée est décrite comme la première plateforme d'annotation d'images modulaire intégrant assistance à l'annotation, apprentissage actif et entraînement/évaluation de modèles L'assistance par hiérarchie et images de référence réduit le besoin d'annotateurs spécialisés en ouvrant l'annotation à un public plus large L'apprentissage actif priorise les images à annoter, réduisant la charge cognitive des annotateurs L'approche modulaire permet d'intégrer de nouveaux algorithmes de classification d'images et fournit des statistiques de performance comparatives entre modèles et sous-ensembles de données

Les auteurs présentent ce travail comme la première plateforme d'annotation d'images modulaire intégrant simultanément l'assistance à l'annotation, l'apprentissage actif et l'entraînement/évaluation de modèles L'assistance à l'annotation via hiérarchie et images de référence aide grandement les annotateurs à identifier les objets, notamment pour des objets spécifiques à un domaine, réduisant le besoin d'annotateurs spécialisés L'apprentissage actif priorise les images à annoter, réduisant la charge cognitive des annotateurs L'approche modulaire permet l'incorporation de nouveaux algorithmes de classification d'images Le pipeline d'entraînement et d'évaluation des modèles fournit des statistiques sur la performance des différents algorithmes sur différents sous-ensembles de données


## Insight


methodology: La plateforme proposée constitue le premier outil modulaire intégrant simultanément assistance à l'annotation d'images, apprentissage actif et pipeline d'entraînement/évaluation de modèles au sein d'un même système.

methodology: La plateforme développée constitue le premier outil modulaire combinant assistance à l'annotation, apprentissage actif et pipeline d'entraînement/évaluation de modèles au sein d'un même système.

design: ActiveLab est conçu comme une méthode générale et facile à implémenter, applicable à tout modèle de classification ou ensemble de modèles, à différentes modalités de données, ainsi qu'à des scénarios où l'ensemble des annotateurs évolue dans le temps, à l'apprentissage actif traditionnel et au nettoyage actif de labels.


## Discussion


Les auteurs concluent en présentant leur plateforme comme la première solution modulaire intégrant à la fois l'annotation d'images, l'assistance à l'annotation via hiérarchie de référence, l'apprentissage actif et un pipeline d'entraînement et d'évaluation de modèles. Cette approche modulaire permet d'incorporer de nouveaux algorithmes de classification d'images et de comparer leurs performances sur différents sous-ensembles de données. Les auteurs soulignent que l'assistance à l'annotation réduit le besoin d'annotateurs spécialisés pour les objets spécifiques à un domaine, tandis que l'apprentissage actif diminue la charge cognitive en priorisant les images à annoter. Le développement futur portera sur l'intégration de nouveaux modèles, l'amélioration des méthodes d'échantillonnage pour l'apprentissage actif, le support des annotations multiples par image avec calcul de l'accord inter-annotateurs, ainsi que l'étude de l'influence des propriétés des images sur les résultats des modèles.

Cette conclusion présente une plateforme modulaire d'annotation d'images qui intègre pour la première fois assistance à l'annotation, apprentissage actif et pipeline d'entraînement/évaluation de modèles. L'assistance via une hiérarchie de référence et des images de référence facilite l'identification d'objets spécifiques à un domaine, réduisant le besoin d'annotateurs spécialisés, tandis que l'apprentissage actif priorise les images à annoter afin de diminuer la charge cognitive des annotateurs. L'architecture modulaire permet d'intégrer de nouveaux algorithmes de classification d'images et fournit des statistiques de performance comparatives sur différents sous-ensembles de données. Les auteurs annoncent des développements futurs portant sur l'intégration de nouveaux modèles, l'amélioration des méthodes d'échantillonnage pour l'apprentissage actif, le support d'annotations multiples par image avec calcul d'accord inter-annotateurs, ainsi qu'une investigation approfondie de l'influence des propriétés des images sur les résultats des modèles.

Cette conclusion présente la plateforme développée comme le premier outil modulaire d'annotation d'images intégrant à la fois l'assistance à l'annotation, l'apprentissage actif et un pipeline d'entraînement/évaluation de modèles. L'assistance à l'annotation, fondée sur une hiérarchie de référence et des images de référence, facilite l'identification d'objets spécifiques à un domaine et réduit ainsi la dépendance à des annotateurs spécialisés, ouvrant la tâche à un public plus large. L'apprentissage actif permet de hiérarchiser les images à annoter, diminuant la charge cognitive des annotateurs, tandis que l'architecture modulaire autorise l'intégration de nouveaux algorithmes de classification et fournit des statistiques de performance comparatives selon les sous-ensembles de données. Les auteurs indiquent que la plateforme continuera d'évoluer, avec des travaux en cours sur l'intégration de nouveaux modèles, l'amélioration des méthodes d'échantillonnage de l'apprentissage actif, la prise en charge d'annotations multiples par image et le calcul de l'accord inter-annotateurs, ainsi qu'une investigation future sur l'influence des propriétés des images sur les résultats des modèles.


## Quote


A very general approach, ActiveLab can be used: with any type of classifier model (or ensemble of multiple models) and data modality, for active learning with multiple annotators where the set of annotators changes over time, for traditional active learning where each example is labeled at most once (Appendix D), and for active label cleaning where all data is already labeled by at least one annotator

These models can be used as an assistive tool, automatically annotating the data, where the user can focus more on checking the actual annotations. This can speed up the whole annotation process, making the data labelling more effective.

We have presented this work as the first modular image annotation platform which seamlessly incorporates image annotation with annotation assistance, active learning and model training and evaluation.

We have presented this work as the first modular image annotation platform which seamlessly incorporates image annotation with annotation assistance, active learning and model training and evaluation.


## Raw_Conclusion


Our contributions from this paper are two-fold: 1) a robust video annotation system as well as 2) a comprehensive large-scale driving dataset with extensive annotations. First, the annotation system is an improvement over existing solutions in terms of efficiency and extensibility. Our annotation system incorporates different kinds of labeling heuristics to improve productivity, and can be extended to different types of image annotation. With this production-ready annotation system, we are able to label a driving video dataset that is larger and more diverse than existing datasets. This dataset comes with comprehensive annotations that are necessary for a complete driving system. Moreover, experiments show that this new dataset is more challenging and more comprehensive than existing ones, and can serve as a good benchmark for domain adaption due to its diversity. This will serve to help the research community with understanding on how different scenarios affect existing algorithms' pe

Our contributions from this paper are two-fold: 1) a robust video annotation system as well as 2) a comprehensive large-scale driving dataset with extensive annotations. First, the annotation system is an improvement over existing solutions in terms of efficiency and extensibility. Our annotation system incorporates different kinds of labeling heuristics to improve productivity, and can be extended to different types of image annotation. With this production-ready annotation system, we are able to label a driving video dataset that is larger and more diverse than existing datasets. This dataset comes with comprehensive annotations that are necessary for a complete driving system. Moreover, experiments show that this new dataset is more challenging and more comprehensive than existing ones, and can serve as a good benchmark for domain adaption due to its diversity. This will serve to help the research community with understanding on how different scenarios affect existing algorithms' pe

Callico represents a significant advancement in the field of document recognition, providing a robust, open source platform designed to meet the complex requirements of annotating digitised documents. Through its innovative features such as dual display annotation, collaborative annotation capabilities and flexibility in handling different annotation tasks, Callico addresses the critical need for high quality data generation in machine learning and deep learning projects. The case studies presented in this paper highlight Callico's potential to transform document recognition tasks by improving efficiency, data quality and collaboration across domains.

Callico represents a significant advancement in the field of document recognition, providing a robust, open source platform designed to meet the complex requirements of annotating digitised documents. Through its innovative features such as dual display annotation, collaborative annotation capabilities and flexibility in handling different annotation tasks, Callico addresses the critical need for high quality data generation in machine learning and deep learning projects. The case studies presented in this paper highlight Callico's potential to transform document recognition tasks by improving efficiency, data quality and collaboration across domains.


## Synthese


Ce document présente un tutoriel de pointe consacré aux stratégies hybrides d'annotation de données combinant humains et modèles de langage (LLM), destiné aux praticiens en NLP issus de la recherche et de l'industrie. L'objectif est de présenter les fondements de la génération de données synthétiques, de l'active learning et du labeling hybride, tout en discutant de leurs avantages, limites et cas d'usage concrets. Le format proposé est une session en présentiel d'une demi-journée, structurée en sept parties, incluant un atelier pratique de 30 minutes sur Google Colab permettant d'implémenter une annotation hybride combinant la plateforme de crowdsourcing Toloka et le prompting/fine-tuning d'un LLM sur un jeu de données de classification multiclasse. S'agissant d'une proposition de tutoriel et non d'une étude empirique, aucun résultat quantitatif n'est rapporté. Les auteurs concluent néanmoins que le maintien d'un humain dans la boucle reste essentiel pour garantir la qualité des annotations, et que les approches hybrides permettent de réduire le budget d'étiquetage tout en améliorant la précision, les bénéfices de ces stratégies l'emportant sur les risques d'une dépendance excessive à l'automatisation.


## Raw_Full_Text


Rééquilibrer la distribution des labels tout en éliminant le temps
d’attente inhérent dans l’apprentissage actif multi-label appliqué
aux transformers
Maxime Arens1, 2
Lucile Callebert2
Jose G. Moreno1
Mohand Boughanem1
(1) IRIT, Toulouse University, UMR 5505 CNRS, 31400 Toulouse, France
(2) Synapse Développement, 7 Boulevard de la Gare, 31500 Toulouse, France
maxime.arens@gmail.com
RÉSUMÉ
L’annotation des données est cruciale pour l’apprentissage automatique, notamment dans les domaines
techniques, où la qualité et la quantité des données annotées affectent significativement l’efficacité des
modèles entraînés. L’utilisation de personnel humain est coûteuse, surtout lors de l’annotation pour
la classification multi-label, les instances pouvant être associées à plusieurs labels. L’apprentissage
actif (AA) vise à réduire les coûts d’annotation en sélectionnant intelligemment des instances pour
l’annotation, plutôt que de les annoter de manière aléatoire. L’attention récente portée aux tr


## Raw_Introduction


We study how to improve labeling efficiency as well as extensibility, so that an annotation system can be easily adapted to new tasks. In most use cases, there are only three basic types of labels on an image: image-level tagging, bounding box, and polygon annotation. However, the semantic meanings of the annotations can differ dramatically between use cases. Therefore, we build a configurable annotation system that supports these three types of annotations. Moreover, we also introduce improvements to boost labeling efficiency, as described below. We tested our system in annotating real-world videos while extending it to additional types of labels, including drivable area and lane marking annotations. At the same time, we also collected efficient full-frame semantic instance segmentations. Our study shows that we can extend our labeling system to new types of annotation with minimal effort while still being able to label large-scale datasets.