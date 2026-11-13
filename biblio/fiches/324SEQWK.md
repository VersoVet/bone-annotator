# Progressive medical image annotation with convolutional neural network-based interactive segmentation method



## Resume


Progressive medical image annotation with convolutional neural network-based interactive segmentation method

An improved algorithm for interactive medical image segmentation based on Intelligent scissors

A survey of recent interactive image segmentation methods

Medical Image Segmentation with Efficient Use of Annotations and Resources

HAL-IA: A Hybrid Active Learning framework using Interactive Annotation for medical image segmentation

Interactive image segmentation

A shortest path approach to interactive medical image segmentation

Volumetric memory network for interactive medical image segmentation

Robust interactive image segmentation via iterative refinement

Suggestive Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

VR-based annotation assistance system for volumetric medical image segmentation

Deep learning medical image segmentation

Visual and structural feature combination in an interactive machine learning system for medical image segmentation

An annotation tool for dermoscopic image segmentation

PyMIC: A deep learning toolkit for annotation-efficient medical image segmentation

Medical image denoising using convolutional neural networks

Active learning with noise modeling for medical image annotation

Large-vocabulary segmentation for medical images with text prompts

Attention, Suggestion and Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

Learning normalized inputs for iterative estimation in medical image segmentation

Learning With Context Feedback Loop for Robust Medical Image Segmentation

Interactive deep-learning-based interface for brain tumour segmentation

AdaResU-Net: Multiobjective adaptive convolutional neural network for medical image segmentation

DeepEdit: Deep Editable Learning for Interactive Segmentation of 3D Medical Images

Automatic segmentation of medical images is a key step for diagnostic and interventional tasks. However, achieving this requires large amounts of annotated volumes, which can be tedious and time-consuming task for expert annotators. In this paper, we introduce DeepEdit, a deep learning-based method for volumetric medical image annotation, that allows automatic and semi-automatic segmentation, and click-based refinement. DeepEdit combines the power of two methods: a non-interactive (i.e. automatic segmentation using nnU-Net, UNET or UNETR) and an interactive segmentation method (i.e. DeepGrow), into a single deep learning model. It allows easy integration of uncertainty-based ranking strategies (i.e. aleatoric and epistemic uncertainty computation) and active learning. We propose and implement a method for training DeepEdit by using standard training combined with user interaction simulation. Once trained, DeepEdit allows clinicians to quickly segment their datasets by using the algorit

Annotating Medical Image Data

Clisp: A Robust Interactive Segmentation Framework for Pathological Images.

Recently, automatic segmentation algorithms based on deep learning have achieved promising results on various pathological image segmentation tasks. However, the inherent data-hungry nature of these methods and the high cost of annotating pathological images make them difficult to apply to practical clinical tasks. To address this problem, many studies have explored interactive segmentation methods to reduce the cost of annotating pathological images, which replace pixel-by-pixel annotation operations with clicks or other user instructions. Despite their effectiveness, most of these methods only utilize small-scale data resulting in poor generalization ability for different tasks or segmentation objects. In this paper, we propose a robust Click-based Interactive Segmentation framework for low-cost and interactive annotation of Pathological images, named Clisp. To improve the generalization ability, we construct a multi-source pathological image annotation dataset including around 79,00


## Raw_Résumé


La segmentation d'images médicales peut s'effectuer manuellement, automatiquement ou à l'aide d'algorithmes de segmentation semi-automatique (interactifs). Les segmentations obtenues sont généralement employées à des fins diagnostiques ou pour diverses tâches ultérieures, comme la génération de modèles 3D en réalité augmentée (RA) chirurgicale, à l'instar du travail présenté ici. Étant donné l'importance critique des applications médicales, les algorithmes de segmentation interactive sont mieux adaptés au contexte clinique. Cela s'explique par l'intervention de l'expert médical, qui peut, le cas échéant, corriger la segmentation proposée par le modèle. Par conséquent, pour optimiser ces corrections, il importe que le modèle sache interpréter les interventions de l'utilisateur et en déduire l'intention sous-jacente, aspect qui n'est pas pleinement pris en compte par les approches actuelles. Les systèmes d'annotation efficaces recourent généralement à un prédicteur neuronal d'annotation

La segmentation d'images médicales peut s'effectuer manuellement, automatiquement ou à l'aide d'algorithmes de segmentation semi-automatique (interactifs). Les segmentations obtenues sont généralement employées à des fins diagnostiques ou pour diverses tâches ultérieures, comme la génération de modèles 3D en réalité augmentée (RA) chirurgicale, à l'instar du travail présenté ici. Étant donné l'importance critique des applications médicales, les algorithmes de segmentation interactive sont mieux adaptés au contexte clinique. Cela s'explique par l'intervention de l'expert médical, qui peut, le cas échéant, corriger la segmentation proposée par le modèle. Par conséquent, pour optimiser ces corrections, il importe que le modèle sache interpréter les interventions de l'utilisateur et en déduire l'intention sous-jacente, aspect qui n'est pas pleinement pris en compte par les approches actuelles. Les systèmes d'annotation efficaces recourent généralement à un prédicteur neuronal d'annotation


## Methodologie


Cet article distingue les approches automatiques et interactives de segmentation d'image médicale, soulignant que les premières nécessitent des connaissances a priori sur la forme et l'apparence des objets, difficiles à généraliser face à la variabilité et au bruit inhérents aux modalités d'imagerie médicale. Les méthodes interactives, telles que l'intelligent scissors, le live wire ou les modèles de contours actifs, permettent d'exploiter l'expertise de l'utilisateur mais posent un dilemme entre précision de la segmentation et charge de travail imposée à l'utilisateur. Les auteurs proposent une méthode fondée sur la recherche de plus court chemin, capable de segmenter à la fois des régions fermées et des contours ouverts. Cette méthode est évaluée sur deux applications médicales (images IVUS et OCT) disposant de vérités terrain pour une comparaison quantitative, ainsi que sur un ensemble d'images génériques de la base Berkeley Image Database afin d'illustrer sa polyvalence. Les résultats montrent que l'approche proposée surpasse qualitativement des méthodes de référence telles que le graph-cut, le seeded star graph-cut, Grab Cut et la recherche de graphe en couches, notamment dans les cas difficiles où les couleurs sont proches de l'arrière-plan ou les contours ambigus.


## Synthese


Cet article distingue les approches automatiques et interactives de segmentation d'image médicale, soulignant que les premières nécessitent des connaissances a priori sur la forme et l'apparence des objets, difficiles à généraliser face à la variabilité et au bruit inhérents aux modalités d'imagerie médicale. Les méthodes interactives, telles que l'intelligent scissors, le live wire ou les modèles de contours actifs, permettent d'exploiter l'expertise de l'utilisateur mais posent un dilemme entre précision de la segmentation et charge de travail imposée à l'utilisateur. Les auteurs proposent une méthode fondée sur la recherche de plus court chemin, capable de segmenter à la fois des régions fermées et des contours ouverts. Cette méthode est évaluée sur deux applications médicales (images IVUS et OCT) disposant de vérités terrain pour une comparaison quantitative, ainsi que sur un ensemble d'images génériques de la base Berkeley Image Database afin d'illustrer sa polyvalence. Les résultats montrent que l'approche proposée surpasse qualitativement des méthodes de référence telles que le graph-cut, le seeded star graph-cut, Grab Cut et la recherche de graphe en couches, notamment dans les cas difficiles où les couleurs sont proches de l'arrière-plan ou les contours ambigus.