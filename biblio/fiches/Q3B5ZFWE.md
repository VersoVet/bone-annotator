# Swin-LiteMedSAM: A Lightweight Box-Based Segment Anything Model for Large-Scale Medical Image Datasets



## Resume


Swin-LiteMedSAM: A Lightweight Box-Based Segment Anything Model for Large-Scale Medical Image Datasets

Medical imaging is essential for the diagnosis and treatment of diseases, with medical image segmentation as a subtask receiving high attention. However, automatic medical image segmentation models are typically task-specific and struggle to handle multiple scenarios, such as different imaging modalities and regions of interest. With the introduction of the Segment Anything Model (SAM), training a universal model for various clinical scenarios has become feasible. Recently, several Medical SAM (MedSAM) methods have been proposed, but these models often rely on heavy image encoders to achieve high performance, which may not be practical for real-world applications due to their high computational demands and slow inference speed. To address this issue, a lightweight version of the MedSAM (LiteMedSAM) can provide a viable solution, achieving high performance while requiring fewer resources and less time. In this work, we introduce Swin-LiteMedSAM, a new variant of LiteMedSAM. This model i

SwiftMedSAM: An Ultra-lightweight Prompt-Based Universal Medical Image Segmentation Model for Highly Constrained Environments

Segment Anything Model (SAM) for Medical Image Segmentation: A Preliminary Review

RepViT-MedSAM: Efficient Segment Anything in the Medical Images

The Role of Segment Anything Model (SAM) In Medical Image Segmentation: A Comprehensive Review

Trans-SAM: Transfer Segment Anything Model to medical image segmentation with Parameter-Efficient Fine-Tuning

PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation

Efficient Medical Segmentation Anything Model for Robust Lightweight Segmentation under Imperfect Data in Embedded Healthcare.

Healthcare Industry 5.0 is accelerating the deployment of medical imaging intelligence on embedded and edge devices, where medical data are often imperfect due to acquisition noise, low-contrast regions, and boundary ambiguity, while computational budgets remain tight. Although the Segment Anything Model (SAM) provides promptable segmentation, its heavy encoder hinders edge deployment and its zero-shot behavior can be unreliable for specialized medical imaging scenarios. This paper presents an efficient and lightweight medical image segmentation pipeline tailored for embedded healthcare systems. We replace the SAM image encoder with an Efficient Vision Transformer (EfficientViT) backbone and introduce offline knowledge distillation to transfer domain-aware feature representations from the Medical Segment Anything Model (MedSAM) to a compact student network. To emulate imperfect supervision in practical use, bounding-box prompts are generated from ground truth masks with random per-side

Towards an automated Segment Anything Model (SAM) for lesion segmentation in oncological PET/CT images

A review of the Segment Anything Model (SAM) for medical image analysis: Accomplishments and perspectives

Segment anything model for medical images?

The Segment Anything Model (SAM) is the first foundation model for general image segmentation. It has achieved impressive results on various natural image segmentation tasks. However, medical image segmentation (MIS) is more challenging because of the complex modalities, fine anatomical structures, uncertain and complex object boundaries, and wide-range object scales. To fully validate SAM's performance on medical data, we collected and sorted 53 open-source datasets and built a large medical segmentation dataset with 18 modalities, 84 objects, 125 object-modality paired targets, 1050K 2D images, and 6033K masks. We comprehensively analyzed different models and strategies on the so-called COSMOS 1050K dataset. Our findings mainly include the following: (1) SAM showed remarkable performance in some specific objects but was unstable, imperfect, or even totally failed in other situations. (2) SAM with the large ViT-H showed better overall performance than that with the small ViT-B. (3) SA

Lung Segment Anything Model (LuSAM): A Prompt-integrated Framework for Automated Lung Segmentation on ICU Chest X-Ray Images

<jats:italic toggle="yes">Abstract
                  — The Segment Anything Model (SAM) is a
state-of-the-art deep learning architecture for image seg- mentation
that allows users to segment arbitrary objects in images using points,
or bounding boxes. SAM uses a novel two-stage approach that first
encodes the input image into a high-dimensional embedding, and then
generates object masks using the embedding and the input prompt. This
ap- proach allows SAM to produce high-quality segmentation even for
objects that were not seen during training, and to handle complex input
prompts with multiple objects and attributes. We evaluate SAM on the
open source Chest X- ray dataset known as Japanese Society of
Radiological Technology (JSRT) dataset and another dataset obtained from
Emory Hospital, Atlanta, Georgia,USA and show that it achieves
state-of-the-art performance in terms of Stability Score and Jaccard
Index including the perfor- mance across different demographic data

Foundational Segmentation Models and Clinical Data Mining Enable Accurate Computer Vision for Lung Cancer.

This study aims to assess the effectiveness of integrating Segment Anything Model (SAM) and its variant MedSAM into the automated mining, object detection, and segmentation (MODS) methodology for developing robust lung cancer detection and segmentation models without post hoc labeling of training images. In a retrospective analysis, 10,000 chest computed tomography scans from patients with lung cancer were mined. Line measurement annotations were converted to bounding boxes, excluding boxes < 1 cm or > 7 cm. The You Only Look Once object detection architecture was used for teacher-student learning to label unannotated lesions on the training images. Subsequently, a final tumor detection model was trained and employed with SAM and MedSAM for tumor segmentation. Model performance was assessed on a manually annotated test dataset, with additional evaluations conducted on an external lung cancer dataset before and after detection model fine-tuning. Bootstrap resampling was used to calculat

Segment anything model for few-shot medical image segmentation with domain tuning

Customized Segment Anything Model for Medical Image Segmentation

We propose SAMed, a general solution for medical image segmentation. Different from the previous methods, SAMed is built upon the large-scale image segmentation model, Segment Anything Model (SAM), to explore the new research paradigm of customizing large-scale models for medical image segmentation. SAMed applies the low-rank-based (LoRA) finetuning strategy to the SAM image encoder and finetunes it together with the prompt encoder and the mask decoder on labeled medical image segmentation datasets. We also observe the warmup finetuning strategy and the AdamW optimizer lead SAMed to successful convergence and lower loss. Different from SAM, SAMed could perform semantic segmentation on medical images. Our trained SAMed model achieves 81.88 DSC and 20.64 HD on the Synapse multi-organ segmentation dataset, which is on par with the state-of-the-art methods. We conduct extensive experiments to validate the effectiveness of our design. Since SAMed only updates a small fraction of the SAM par

An efficient segment anything model for the segmentation of medical images.

This paper introduces the efficient medical-images-aimed segment anything model (EMedSAM), addressing the high computational demands and limited adaptability of using SAM for medical image segmentation tasks. We present a novel, compact image encoder, DD-TinyViT, designed to enhance segmentation efficiency through an innovative parameter tuning method called med-adapter. The lightweight DD-TinyViT encoder is derived from the well-known ViT-H using a decoupled distillation approach.The segmentation and recognition capabilities of EMedSAM for specific structures are improved by med-adapter, which dynamically adjusts the model parameters specifically for medical imaging. We conducted extensive testing on EMedSAM using the public FLARE 2022 dataset and datasets from the First Hospital of Zhejiang University School of Medicine. The results demonstrate that our model outperforms existing state-of-the-art models in both multi-organ and lung segmentation tasks.

How Segment Anything Model (Sam) Boost Medical Image Segmentation: A Survey

Segment anything model for medical image analysis: An experimental study

Training segmentation models for medical images continues to be challenging due to the limited availability of data annotations. Segment Anything Model (SAM) is a foundation model trained on over 1 billion annotations, predominantly for natural images, that is intended to segment user-defined objects of interest in an interactive manner. While the model performance on natural images is impressive, medical image domains pose their own set of challenges. Here, we perform an extensive evaluation of SAM's ability to segment medical images on a collection of 19 medical imaging datasets from various modalities and anatomies. In our experiments, we generated point and box prompts for SAM using a standard method that simulates interactive segmentation. We report the following findings: (1) SAM's performance based on single prompts highly varies depending on the dataset and the task, from IoU=0.1135 for spine MRI to IoU=0.8650 for hip X-ray. (2) Segmentation performance appears to be better for

Segment Anything Model for Gastric Cancer.

ABSTRACT Background Gastric cancer is a biologically aggressive disease, accounting for a substantial proportion of cancer‐related deaths globally. Accurate localization of the lesion by artificial intelligence techniques helps timely and efficiently diagnose and treat. Segment Anything Model (SAM) has demonstrated considerable potential in medical image segmentation by displaying high performance in numerous image benchmark tests. However, its resource‐intensive nature limits feasibility in embedded medical contexts. Methods This study proposed GC‐SAM, a lightweight model for tumor segmentation. The architecture of GC‐SAM is innovatively proposed, including a knowledge distillation image encoder, prompt encoder, and mask decoder, which effectively replaces the conventional fixed and computationally intensive network components. Results Extensive experiments demonstrate that GC‐SAM significantly outperforms both classical segmentation models and recent state‐of‐the‐art networks. On the

Rethinking Few-Shot Medical Image Segmentation by SAM2: A Training-Free Framework with Augmentative Prompting and Dynamic Matching

The reliance on large labeled datasets presents a significant challenge in medical image segmentation. Few-shot learning offers a potential solution, but existing methods often still require substantial training data. This paper proposes a novel approach that leverages the Segment Anything Model 2 (SAM2), a vision foundation model with strong video segmentation capabilities. We conceptualize 3D medical image volumes as video sequences, departing from the traditional slice-by-slice paradigm. Our core innovation is a support-query matching strategy: we perform extensive data augmentation on a single labeled support image and, for each frame in the query volume, algorithmically select the most analogous augmented support image. This selected image, along with its corresponding mask, is used as a mask prompt, driving SAM2's video segmentation. This approach entirely avoids model retraining or parameter updates. We demonstrate state-of-the-art performance on benchmark few-shot medical image

ProtoSAM-3D: Interactive semantic segmentation in volumetric medical imaging via a Segment Anything Model and mask-level prototypes


## Synthese


S-SAM propose une adaptation efficace du Segment Anything Model (SAM) à la segmentation d'images médicales, en s'affranchissant du besoin de prompts experts tels que des points ou des boîtes englobantes. La méthode repose sur un fine-tuning basé sur la décomposition en valeurs singulières (SVD) de l'encodeur d'image de SAM, complété par une couche Text Affine Layer (TAL), des matrices de mise à l'échelle et de décalage, ainsi que l'entraînement des positional embeddings et des couches layernorm. Cette approche permet d'utiliser de simples noms de classes comme prompts textuels, à la place des annotations expertes habituellement requises. Évalué sur cinq jeux de données publics couvrant des modalités variées (endoscopie, radiographie, échographie, CT et histologie), S-SAM égale ou surpasse les méthodes état de l'art et les techniques d'adaptation existantes de SAM, tout en nécessitant significativement moins de paramètres entraînables. Les auteurs notent toutefois que la performance de S-SAM peut être affectée par des disparités de taille entre classes, ouvrant la voie à des travaux futurs sur des fonctions de perte pondérées.

L'étude vise à améliorer l'efficacité computationnelle et l'adaptabilité du Segment Anything Model (SAM) pour la segmentation d'images médicales, en développant un encodeur d'image léger (DD-TinyViT) et un mécanisme d'adaptation de paramètres (med-adapter) intégrés dans un nouveau modèle nommé EMedSAM.

Le Segment Anything Model (SAM), fondation pour la segmentation d’images naturelles, présente des performances insuffisantes en imagerie médicale, en raison de la composition du jeu SA-1B, principalement constitué de scènes naturelles. MedSAM, obtenu par fine-tuning de SAM sur un corpus multimodal, constitue une avancée, mais demeure limité par des déséquilibres de modalités, des difficultés sur les structures vasculaires ramifiées et une utilité restreinte des prompts textuels. Dans le cadre du défi CVPR 2024 MedSAM on Laptop, centré sur l’accélération de l’inférence de MedSAM, les auteurs privilégient la quantization-aware training (QAT) via le framework Xilinx Brevitas, plutôt que la post-training quantization, afin de préserver la précision après quantification. Leur approche aboutit à un LiteMedSAM quantifié déployé sur OpenVINO, avec une précision moyenne comparable, un meilleur équilibre inter-modalités et une efficacité d’inférence nettement améliorée sous le même backbone.

Cet article de Scientific Reports (2024) répond au défi de l'efficacité computationnelle et de la précision du Segment Anything Model (SAM) appliqué aux images médicales, un domaine où SAM standard sous-performe en conditions zero-shot par rapport à des modèles spécialisés comme MedSAM. Les auteurs proposent EMedSAM, une architecture combinant deux innovations: DD-TinyViT, un encodeur d'image léger (21M paramètres contre 632M pour le ViT-H original de SAM) obtenu par distillation découplée sur le jeu de données SA-1B, et le med-adapter, un mécanisme d'adaptation de paramètres inséré entre l'encodeur et le décodeur pour ajuster dynamiquement le modèle aux spécificités des images médicales. Le modèle a été évalué sur quatre jeux de données couvrant différentes modalités d'imagerie (scanner CT pulmonaire, mammographie X-ray, IRM cérébrale, segmentation abdominale multi-organes), incluant des données propres au First Hospital of Zhejiang University School of Medicine. Les résultats montrent qu'EMedSAM atteint des performances état de l'art sur 13 organes du jeu de données FLARE 2022 et sur la segmentation pulmonaire, l'encodeur léger n'entraînant pas de perte de précision significative tandis que la combinaison encodeur léger et med-adapter produit un effet synergique supérieur à chaque composant pris isolément. Les auteurs concluent qu'EMedSAM offre un compromis efficacité-précision meilleur que SAM et MedSAM, avec une généralisation robuste à travers les modalités et tâches de segmentation médicale testées.

Cet article s'inscrit dans le contexte de l'analyse d'images médicales, où la segmentation (extraction de régions d'intérêt telles qu'organes, tissus ou lésions) et la classification (détermination du type ou du grade de la maladie) constituent deux tâches fondamentales pour le diagnostic clinique, le suivi thérapeutique et l'évaluation de la réadaptation. Les auteurs soulignent que les modèles de deep learning conventionnels, bien que performants, restent spécifiques à une tâche et peinent à généraliser across les multiples modalités d'imagerie médicale (CT, endoscopie, IRM, échographie, microscopie), dont les caractéristiques d'intensité, de texture et de couleur diffèrent fortement. Face à cette limitation, et en s'appuyant sur les capacités de généralisation zero-shot et few-shot du modèle Segment Anything (SAM) ainsi que sur ses dérivés médicaux tels que Med-SAM et SAM-Med2D, les auteurs proposent deux contributions : SAM-AutoMed, un modèle de segmentation automatique substituant l'encodeur de prompts interactif par une architecture MobileNet v3 dotée d'un bloc SE amélioré, et SAM-MedCls, un modèle de classification exploitant l'encodeur de SAM-Med2D enrichi de modules d'attention. Ces deux modèles ont été évalués et comparés aux travaux de recherche les plus récents sur plusieurs jeux de données médicales.


## Raw_Introduction


y do not need to be fine-tuned for medical imaging tasks and can operate directly out-of-the-box. The Segment Anything Model (SAM) is one such popular and open-source foundational model based on vision transformers (ViTs) with the ability for zero-shot semantic segmentation [8,12]. SAM works by interactively prompting images with sparse annotations, such as points or bounding boxes, to generate segmentation masks (Figure 1).

y do not need to be fine-tuned for medical imaging tasks and can operate directly out-of-the-box. The Segment Anything Model (SAM) is one such popular and open-source foundational model based on vision transformers (ViTs) with the ability for zero-shot semantic segmentation [8,12]. SAM works by interactively prompting images with sparse annotations, such as points or bounding boxes, to generate segmentation masks (Figure 1).


## Methodologie


Le Segment Anything Model (SAM), fondation pour la segmentation d’images naturelles, présente des performances insuffisantes en imagerie médicale, en raison de la composition du jeu SA-1B, principalement constitué de scènes naturelles. MedSAM, obtenu par fine-tuning de SAM sur un corpus multimodal, constitue une avancée, mais demeure limité par des déséquilibres de modalités, des difficultés sur les structures vasculaires ramifiées et une utilité restreinte des prompts textuels. Dans le cadre du défi CVPR 2024 MedSAM on Laptop, centré sur l’accélération de l’inférence de MedSAM, les auteurs privilégient la quantization-aware training (QAT) via le framework Xilinx Brevitas, plutôt que la post-training quantization, afin de préserver la précision après quantification. Leur approche aboutit à un LiteMedSAM quantifié déployé sur OpenVINO, avec une précision moyenne comparable, un meilleur équilibre inter-modalités et une efficacité d’inférence nettement améliorée sous le même backbone.

Cet article s'inscrit dans le contexte de l'analyse d'images médicales, où la segmentation (extraction de régions d'intérêt telles qu'organes, tissus ou lésions) et la classification (détermination du type ou du grade de la maladie) constituent deux tâches fondamentales pour le diagnostic clinique, le suivi thérapeutique et l'évaluation de la réadaptation. Les auteurs soulignent que les modèles de deep learning conventionnels, bien que performants, restent spécifiques à une tâche et peinent à généraliser across les multiples modalités d'imagerie médicale (CT, endoscopie, IRM, échographie, microscopie), dont les caractéristiques d'intensité, de texture et de couleur diffèrent fortement. Face à cette limitation, et en s'appuyant sur les capacités de généralisation zero-shot et few-shot du modèle Segment Anything (SAM) ainsi que sur ses dérivés médicaux tels que Med-SAM et SAM-Med2D, les auteurs proposent deux contributions : SAM-AutoMed, un modèle de segmentation automatique substituant l'encodeur de prompts interactif par une architecture MobileNet v3 dotée d'un bloc SE amélioré, et SAM-MedCls, un modèle de classification exploitant l'encodeur de SAM-Med2D enrichi de modules d'attention. Ces deux modèles ont été évalués et comparés aux travaux de recherche les plus récents sur plusieurs jeux de données médicales.