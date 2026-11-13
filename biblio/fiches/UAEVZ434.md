# Gastrointestinal Lesion Image Segmentation Network Based on U-Net with Segment Anything Model: Gliu-Net



## Resume


Gastrointestinal Lesion Image Segmentation Network Based on U-Net with Segment Anything Model: Gliu-Net

Ssm-Net: Semi-Supervised Multi-Task Network for Joint Lesion Segmentation and Classification from Pancreatic Eus Images

Gray’s Anatomy for Segment Anything Model: Optimizing Grayscale Medical Images for Fast and Lightweight Segmentation

melSeg: An Adaptation of Segment Anything Model for Skin Lesion Segmentation

Automated Lesion Segmentation in Medical Imaging via Integration of nnU-Net Optimization and SAM Approach.

<h4>Background</h4>Deep learning has transformed medical imaging by enabling earlier and more accurate disease diagnosis. Lesion and tumor segmentation, essential for analyzing and tracking morphological changes, is commonly done with U-Net variants, though these often lack cross-domain generalization and do not fully leverage foundation models like the Segment Anything Model (SAM), which still requires manual intervention to define the region of interest (ROI).<h4>Objectives</h4>To enhance generalization and reduce manual intervention by combining the automatic optimization of nnU-Net with the precision of SAM.<h4>Design</h4>Experimental evaluation of a hybrid segmentation framework for lung nodule analysis.<h4>Methods</h4>We propose a novel approach integrating the automatic optimization capabilities of nnU-Net for lesion detection with the high-precision segmentation of SAM, eliminating the need for manual intervention by the clinician. The method was evaluated on the LIDC-IDRI data

Brain Tumor MRI Segmentation Method Based on Segment Anything Model

Adapting Segment Anything Model for Ulcer Segmentation in Inflammatory Bowel Disease.

Inflammatory Bowel Disease (IBD) is a widespread gastrointestinal disorder characterized by inflammation and ulceration, affecting millions of individuals. Mucosal injury assessment through colonoscopy plays a crucial role in determining disease severity and therapeutic efficacy in IBD. This study draws inspiration from the Segment Anything Model (SAM) framework and tailors it for ulcer segmentation using a Parameter-Efficient Transfer Learning (PETL) approach and incorporating binary cross-entropy loss with boundary loss. Comparative assessments against state-of-the-art UNet-based convolutional neural network models underscore SAM's superior performance, especially when faced with limited training samples. Our ulcer segmentation models demonstrate Dice, IoU, and 95%HD scores of 61.92±0.69, 75.18±0.38, and 10.07±0.05 in the colon dataset, and 55.60±0.82, 77.00±0.67, and 7.74±0.23 in the ileum dataset, respectively. This study highlights the potential of our approach to significantly en

GLFSU-Net: Global and Local Features Fusion Using Separable U-Net to Improve Anatomical Landmark Detection in 2D X-Ray Radiography ImagesGLFSU-Net: Improving Anatomical Landmark Detection in 2D X-Ray Radiography Images

Segment Anything Model for Gastric Cancer.

ABSTRACT Background Gastric cancer is a biologically aggressive disease, accounting for a substantial proportion of cancer‐related deaths globally. Accurate localization of the lesion by artificial intelligence techniques helps timely and efficiently diagnose and treat. Segment Anything Model (SAM) has demonstrated considerable potential in medical image segmentation by displaying high performance in numerous image benchmark tests. However, its resource‐intensive nature limits feasibility in embedded medical contexts. Methods This study proposed GC‐SAM, a lightweight model for tumor segmentation. The architecture of GC‐SAM is innovatively proposed, including a knowledge distillation image encoder, prompt encoder, and mask decoder, which effectively replaces the conventional fixed and computationally intensive network components. Results Extensive experiments demonstrate that GC‐SAM significantly outperforms both classical segmentation models and recent state‐of‐the‐art networks. On the

Segment Anything in Medical Images with nnUNet

Medical Image Segmentation Review: The Success of U-Net

Corrigendum to “Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM)”

Medical Image Segmentation Review: The success of U-Net

Medical Image Segmentation Foundation Models. CVPR 2024 Challenge: Segment Anything in Medical Images on Laptop


## Quote


This challenges the most recent pretrained models like the Segment-Anything Model (Kirillov et al., 2023) to segment keel bone from the whole-body x-ray images. For that reason, we opted to train an all-new model based on U-net

U-Net apparaît comme un choix prédominant pour développer des architectures de segmentation biomédicale adaptées à plusieurs modalités.; La mutabilité et la modularité de U-Net permettent son intégration avec des modèles tels qu’AlexNet, VGGNet, ResNet, GoogLeNet, MobileNet et DenseNet.

The deep learning approaches especially U-Net has great potential to influence the clinical applications involving automated biomedical imaging segmentation. [...] it is believed that U-Net based models would be widely applied to address various challenging problems experienced in the biomedical image segmentation for developing real world computer-aided diagnosis systems.

While a convolutional ensemble model (comprising VGG-16, Inception, ResNet, and EfficientNet architectures) was used for image classification, U-Net architecture was used for segmentation. The DL-trained AI model was developed to identify teeth, evaluate remaining periodontal bone height, and compare results with clinician assessments.

U-Net apparaît comme un choix prédominant pour développer des architectures de segmentation biomédicale adaptées à plusieurs modalités.; La mutabilité et la modularité de U-Net permettent son intégration avec des modèles tels qu'AlexNet, VGGNet, ResNet, GoogLeNet, MobileNet et DenseNet.; Les architectures génériques telles que nn-UNet, U-Net++ et MR-Unet peuvent être validées sur plusieurs modalités, mais il reste difficile d'obtenir des performances optimales pour toutes les tâches de segmentation.

nnU-Net is a framework for medical image segmentation. It utilizes a self-adapting approach to optimize hyperparameters, including preprocessing, loss optimization during training, and post-processing operations.


## Synthese


Cette enquête bibliographique porte sur les variantes de U-Net dédiées à la segmentation d’images biomédicales. Les articles ont été identifiés via Google Scholar à l’aide de la chaîne de recherche SS1, puis sélectionnés selon la qualité des revues ou conférences, le cite score et la contribution scientifique ; certaines prépublications issues d’arXiv ont également été retenues. Les travaux retenus ont été classés selon une catégorisation inter-modalité et intra-modalité, afin d’analyser la conception architecturale des variantes de U-Net, les performances rapportées et les pistes d’amélioration face aux défis propres à chaque modalité. L’analyse souligne le rôle prédominant de U-Net, sa modularité permettant l’intégration avec des réseaux tels qu’AlexNet, VGGNet, ResNet, GoogLeNet, MobileNet et DenseNet, ainsi que la difficulté, pour des architectures génériques comme nn-UNet, U-Net++ et MR-Unet, d’atteindre des performances optimales sur l’ensemble des tâches de segmentation. Dans leur conclusion, Siddique et al. soulignent le potentiel des approches d’apprentissage profond, et en particulier de U-Net, pour les applications cliniques de segmentation automatisée d’images biomédicales. Présenté comme une avancée fondatrice, U-Net a ouvert la voie à de nombreuses architectures visant l’identification et la localisation de régions ou sous-régions cibles. L’article examine ainsi des variantes adaptées aux avancées récentes et aux spécificités de différentes modalités d’imagerie, chacune proposant des développements propres aux défis associés. Les auteurs estiment enfin que les modèles fondés sur U-Net devraient être largement mobilisés pour traiter des problèmes complexes de segmentation biomédicale et contribuer au développement de systèmes d’aide au diagnostic en conditions réelles.

Cette enquête bibliographique porte sur les variantes de U-Net dédiées à la segmentation d’images biomédicales. Les articles ont été identifiés via Google Scholar à l’aide de la chaîne de recherche SS1, puis sélectionnés selon la qualité des revues ou conférences, le cite score et la contribution scientifique ; certaines prépublications issues d’arXiv ont également été retenues. Les travaux retenus ont été classés selon une catégorisation inter-modalité et intra-modalité, afin d’analyser la conception architecturale des variantes de U-Net, les performances rapportées et les pistes d’amélioration face aux défis propres à chaque modalité. L’analyse souligne le rôle prédominant de U-Net, sa modularité permettant l’intégration avec des réseaux tels qu’AlexNet, VGGNet, ResNet, GoogLeNet, MobileNet et DenseNet, ainsi que la difficulté, pour des architectures génériques comme nn-UNet, U-Net++ et MR-Unet, d’atteindre des performances optimales sur l’ensemble des tâches de segmentation.

Cette revue de littérature retrace l'essor du réseau U-net, une architecture de deep learning conçue pour la segmentation d'images, depuis sa proposition initiale par Ronneberger et al. en 2015 jusqu'à ses multiples variantes appliquées à l'imagerie médicale. L'architecture U-net repose sur un chemin de contraction (encodeur) couplé à un chemin d'expansion (décodeur) reliés par des concaténations de caractéristiques, ce qui lui confère une forme symétrique en U et lui permet de produire des cartes de segmentation détaillées à partir d'un nombre limité d'échantillons d'entraînement, une contrainte fréquente en imagerie médicale. Les auteurs ont recensé les publications relatives à U-net depuis 2017 dans les bases de données IEEE, Springer et Elsevier, avec une date de coupure fixée au 04/01/2020, afin d'identifier les principales variantes architecturales (U-net de base, U-net 3D, U-net++, U-net en cascade, avec blocs résiduels, denses, d'attention ou d'inception) et leurs domaines d'application anatomiques. Cette cartographie méthodologique montre que U-net a été appliqué à un large éventail de structures et pathologies, incluant le foie, le poumon, le cœur, le pancréas, les os, le cerveau et les lésions d'AVC, chaque application combinant souvent l'architecture de base à une ou plusieurs modifications structurelles. Cette synthèse de la littérature consacrée à U-net dans l'analyse d'images médicales met en évidence la place centrale occupée par la segmentation, identifiée par plusieurs enquêtes comme la tâche canonique la plus recherchée dans ce domaine. Les auteurs soulignent que la valeur singulière de U-net réside dans sa forte modularité et sa mutabilité, qui permettent d'intégrer une grande diversité de méthodes d'apprentissage profond tout en conservant son architecture de haut niveau, élargissant ainsi son spectre d'applications. L'imagerie par résonance magnétique (IRM) apparaît comme la modalité la plus fréquemment étudiée, bien que la revue documente une variété notable d'autres types d'images et de domaines d'application, incluant des tâches connexes à la segmentation. Les auteurs concluent que la croissance soutenue des publications relatives à U-net depuis 2017 confirme son statut de technique de référence en diagnostic par imagerie médicale, et anticipent que ce modèle demeurera l'une des voies majeures de développement futur malgré les défis persistants de l'analyse d'images fondée sur l'apprentissage profond.

Cette revue de littérature retrace l'essor du réseau U-net, une architecture de deep learning conçue pour la segmentation d'images, depuis sa proposition initiale par Ronneberger et al. en 2015 jusqu'à ses multiples variantes appliquées à l'imagerie médicale. L'architecture U-net repose sur un chemin de contraction (encodeur) couplé à un chemin d'expansion (décodeur) reliés par des concaténations de caractéristiques, ce qui lui confère une forme symétrique en U et lui permet de produire des cartes de segmentation détaillées à partir d'un nombre limité d'échantillons d'entraînement, une contrainte fréquente en imagerie médicale. Les auteurs ont recensé les publications relatives à U-net depuis 2017 dans les bases de données IEEE, Springer et Elsevier, avec une date de coupure fixée au 04/01/2020, afin d'identifier les principales variantes architecturales (U-net de base, U-net 3D, U-net++, U-net en cascade, avec blocs résiduels, denses, d'attention ou d'inception) et leurs domaines d'application anatomiques. Cette cartographie méthodologique montre que U-net a été appliqué à un large éventail de structures et pathologies, incluant le foie, le poumon, le cœur, le pancréas, les os, le cerveau et les lésions d'AVC, chaque application combinant souvent l'architecture de base à une ou plusieurs modifications structurelles.


## Insight


methodology: Le système d’aide au diagnostic reposait sur un modèle d’ensemble convolutionnel (VGG-16, Inception, ResNet et EfficientNet) pour la classification d’images et sur une architecture U-Net pour la segmentation, afin d’identifier les dents, d’évaluer la hauteur osseuse parodontale résiduelle et de comparer les résultats aux évaluations des cliniciens.


## Discussion


Dans leur conclusion, Siddique et al. soulignent le potentiel des approches d’apprentissage profond, et en particulier de U-Net, pour les applications cliniques de segmentation automatisée d’images biomédicales. Présenté comme une avancée fondatrice, U-Net a ouvert la voie à de nombreuses architectures visant l’identification et la localisation de régions ou sous-régions cibles. L’article examine ainsi des variantes adaptées aux avancées récentes et aux spécificités de différentes modalités d’imagerie, chacune proposant des développements propres aux défis associés. Les auteurs estiment enfin que les modèles fondés sur U-Net devraient être largement mobilisés pour traiter des problèmes complexes de segmentation biomédicale et contribuer au développement de systèmes d’aide au diagnostic en conditions réelles.


## Methodologie


Cette enquête bibliographique porte sur les variantes de U-Net dédiées à la segmentation d’images biomédicales. Les articles ont été identifiés via Google Scholar à l’aide de la chaîne de recherche SS1, puis sélectionnés selon la qualité des revues ou conférences, le cite score et la contribution scientifique ; certaines prépublications issues d’arXiv ont également été retenues. Les travaux retenus ont été classés selon une catégorisation inter-modalité et intra-modalité, afin d’analyser la conception architecturale des variantes de U-Net, les performances rapportées et les pistes d’amélioration face aux défis propres à chaque modalité. L’analyse souligne le rôle prédominant de U-Net, sa modularité permettant l’intégration avec des réseaux tels qu’AlexNet, VGGNet, ResNet, GoogLeNet, MobileNet et DenseNet, ainsi que la difficulté, pour des architectures génériques comme nn-UNet, U-Net++ et MR-Unet, d’atteindre des performances optimales sur l’ensemble des tâches de segmentation.

Cette revue de littérature retrace l'essor du réseau U-net, une architecture de deep learning conçue pour la segmentation d'images, depuis sa proposition initiale par Ronneberger et al. en 2015 jusqu'à ses multiples variantes appliquées à l'imagerie médicale. L'architecture U-net repose sur un chemin de contraction (encodeur) couplé à un chemin d'expansion (décodeur) reliés par des concaténations de caractéristiques, ce qui lui confère une forme symétrique en U et lui permet de produire des cartes de segmentation détaillées à partir d'un nombre limité d'échantillons d'entraînement, une contrainte fréquente en imagerie médicale. Les auteurs ont recensé les publications relatives à U-net depuis 2017 dans les bases de données IEEE, Springer et Elsevier, avec une date de coupure fixée au 04/01/2020, afin d'identifier les principales variantes architecturales (U-net de base, U-net 3D, U-net++, U-net en cascade, avec blocs résiduels, denses, d'attention ou d'inception) et leurs domaines d'application anatomiques. Cette cartographie méthodologique montre que U-net a été appliqué à un large éventail de structures et pathologies, incluant le foie, le poumon, le cœur, le pancréas, les os, le cerveau et les lésions d'AVC, chaque application combinant souvent l'architecture de base à une ou plusieurs modifications structurelles.


## Conclusion


Section Conclusion: The deep learning approaches especially U-Net has great potential to influence the clinical applications involving automated biomedical imaging segmentation. Section Conclusion: With U-Net being a breakthrough development, it sets up the foundation for the development of novel architectures concerning the identification and localization of the target regions or sub-regions. Section Conclusion: Each U-Net variant features unique developments over the challenges incurred due to different modalities. Section Conclusion: With such high utility and potential of the U-Net models, it is believed that U-Net based models would be widely applied to address various challenging problems experienced in the biomedical image segmentation for developing real world computer-aided diagnosis systems.