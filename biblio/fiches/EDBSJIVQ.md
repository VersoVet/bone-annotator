# Tumor-SAM: segment anything model for semi-automatic lung tumor segmentation in CT



## Resume


Tumor-SAM: segment anything model for semi-automatic lung tumor segmentation in CT

Towards an automated Segment Anything Model (SAM) for lesion segmentation in oncological PET/CT images

SAM3D: zero-shot semi-automatic segmentation in 3D medical images with the segment anything model

Lung segment anything model (LuSAM): a decoupled prompt-integrated framework for automated lung segmentation on chest x-Ray images.

Accurate lung segmentation in chest x-ray images plays a pivotal role in early disease detection and clinical decision-making. In this study, we introduce an innovative approach to enhance the precision of lung segmentation using the Segment Anything Model (SAM). Despite its versatility, SAM faces the challenge of prompt decoupling, often resulting in misclassifications, especially with intricate structures like the clavicle. Our research focuses on the integration of spatial attention mechanisms within SAM. This approach enables the model to concentrate specifically on the lung region, fostering adaptability to image variations and reducing the likelihood of false positives. This work has the potential to significantly advance lung segmentation, improving the identification and quantification of lung anomalies across diverse clinical contexts.

Segment Anything Model (SAM) for Medical Image Segmentation: A Preliminary Review

Segmentation of 3D brain tumor images using the segmentation anything model

Segment Anything Model for Gastric Cancer.

ABSTRACT Background Gastric cancer is a biologically aggressive disease, accounting for a substantial proportion of cancer‐related deaths globally. Accurate localization of the lesion by artificial intelligence techniques helps timely and efficiently diagnose and treat. Segment Anything Model (SAM) has demonstrated considerable potential in medical image segmentation by displaying high performance in numerous image benchmark tests. However, its resource‐intensive nature limits feasibility in embedded medical contexts. Methods This study proposed GC‐SAM, a lightweight model for tumor segmentation. The architecture of GC‐SAM is innovatively proposed, including a knowledge distillation image encoder, prompt encoder, and mask decoder, which effectively replaces the conventional fixed and computationally intensive network components. Results Extensive experiments demonstrate that GC‐SAM significantly outperforms both classical segmentation models and recent state‐of‐the‐art networks. On the

Corrigendum to “Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM)”

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

Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM).

BackgroundComputed tomography (CT) is widely used in clinical diagnosis of lung diseases. The automatic segmentation of lesions in CT images aids in the development of intelligent lung disease diagnosis.ObjectiveThis study aims to address the issue of imprecise segmentation in CT images due to the blurred detailed features of lesions, which can easily be confused with surrounding tissues.MethodsWe proposed a promptable segmentation method based on an improved U-Net and Segment Anything model (SAM) to improve segmentation accuracy of lung lesions in CT images. The improved U-Net incorporates a multi-scale attention module based on a channel attention mechanism ECA (Efficient Channel Attention) to improve recognition of detailed feature information at edge of lesions; and a promptable clipping module to incorporate physicians' prior knowledge into the model to reduce background interference. Segment Anything model (SAM) has a strong ability to recognize lesions and pulmonary atelectasis

When SAM Meets Medical Images: An Investigation of Segment Anything Model (SAM) on Multi-phase Liver Tumor Segmentation

Learning to segmentation without large-scale samples is an inherent capability of human. Recently, Segment Anything Model (SAM) performs the significant zero-shot image segmentation, attracting considerable attention from the computer vision community. Here, we investigate the capability of SAM for medical image analysis, especially for multi-phase liver tumor segmentation (MPLiTS), in terms of prompts, data resolution, phases. Experimental results demonstrate that there might be a large gap between SAM and expected performance. Fortunately, the qualitative results show that SAM is a powerful annotation tool for the community of interactive medical image segmentation.

Foundational Segmentation Models and Clinical Data Mining Enable Accurate Computer Vision for Lung Cancer.

This study aims to assess the effectiveness of integrating Segment Anything Model (SAM) and its variant MedSAM into the automated mining, object detection, and segmentation (MODS) methodology for developing robust lung cancer detection and segmentation models without post hoc labeling of training images. In a retrospective analysis, 10,000 chest computed tomography scans from patients with lung cancer were mined. Line measurement annotations were converted to bounding boxes, excluding boxes < 1 cm or > 7 cm. The You Only Look Once object detection architecture was used for teacher-student learning to label unannotated lesions on the training images. Subsequently, a final tumor detection model was trained and employed with SAM and MedSAM for tumor segmentation. Model performance was assessed on a manually annotated test dataset, with additional evaluations conducted on an external lung cancer dataset before and after detection model fine-tuning. Bootstrap resampling was used to calculat

Zero-shot swift lung 4D CT segmentation via optimized Segment Anything Model

Semi-automated segmentation of magnitude images in 4D flow MR scans using segment anything model 2 (SAM 2)

ST-SAM: A Spatio-Temporal Enhanced Segment Anything Model for Echocardiogram Video Segmentation

The Role of Segment Anything Model (SAM) In Medical Image Segmentation: A Comprehensive Review

Trans-SAM: Transfer Segment Anything Model to medical image segmentation with Parameter-Efficient Fine-Tuning

Enhancing lung segmentation in chest X-rays via SAM with anatomical priors and boundary-aware loss.

Accurate lung segmentation in chest X-rays is a foundational step for computer-aided diagnosis of respiratory diseases such as pneumonia, tuberculosis, and lung cancer. While the Segment Anything Model (SAM) has demonstrated remarkable zero-shot segmentation capabilities on natural images, its direct application to medical imaging remains limited due to domain shift, low contrast, and ambiguous anatomical boundaries. To address these challenges, we propose a lightweight yet effective adaptation of SAM that integrates (i) a Mask Autoencoder (MAE) as an anatomical prior to enforce global shape consistency, and (ii) a composite loss function combining Binary Cross-Entropy (BCE), Dice, and Boundary losses to jointly optimize pixel-level accuracy, region overlap, and edge fidelity. Our parameter-efficient fine-tuning strategy trains only 0.3% of SAM's parameters, specifically the mask decoder, while freezing the image and prompt encoders. Evaluated on the MedSeg Chest X-ray Lung Dataset, ou

PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation

Evaluating segment anything model (SAM) on MRI scans of brain tumors.

Addressing the challenge of automatically segmenting anatomical structures from brain images has been a long-standing problem, attributed to subject- and image-based variations and constraints in available data annotations. The Segment Anything Model (SAM), developed by Meta, is a foundational model trained to provide zero-shot segmentation outputs with or without interactive user inputs, demonstrating notable performance on various objects and image domains without explicit prior training. This study evaluated SAM's performance in brain tumor segmentation using two publicly available Magnetic Resonance Imaging (MRI) datasets. The study analyzed SAM's standalone segmentation as well as its performance when provided user interaction through point prompts and bounding box inputs. SAM exhibited versatility across configurations and datasets, with the bounding box consistently outperforming others in achieving superior localized precision, with average Dice scores of 0.68 for TCGA and 0.56

Evaluating the efficacy of the Segment Anything Model (SAM) in streamlining dental cyst segmentation within CBCT volumes

Automated volumetric lung segmentation of thoracic CT images using fully convolutional neural network

Segment Anything Model (SAM) for Radiation Oncology

In this study, we evaluate the performance of the Segment Anything Model (SAM) in clinical radiotherapy. Our results indicate that SAM's 'segment anything' mode can achieve clinically acceptable segmentation results in most organs-at-risk (OARs) with Dice scores higher than 0.7. SAM's 'box prompt' mode further improves the Dice scores by 0.1 to 0.5. Considering the size of the organ and the clarity of its boundary, SAM displays better performance for large organs with clear boundaries but performs worse for smaller organs with unclear boundaries. Given that SAM, a model pre-trained purely on natural images, can handle the delineation of OARs from medical images with clinically acceptable accuracy, these results highlight SAM's robust generalization capabilities with consistent accuracy in automatic segmentation for radiotherapy. In other words, SAM can achieve delineation of different OARs at different sites using a generic automatic segmentation model. SAM's generalization capabilitie

RepViT-MedSAM: Efficient Segment Anything in the Medical Images


## Synthese


L'objectif de cet article de synthèse est d'examiner comment les grands modèles de fondation en vision par ordinateur, en particulier le Segment Anything Model (SAM), peuvent être adaptés et exploités pour la segmentation du cancer en imagerie médicale, dans un contexte scientifique marqué par le succès de SAM sur des tâches de segmentation généralistes mais des performances insatisfaisantes lorsqu'il est appliqué tel quel à des images oncologiques. Les auteurs cherchent spécifiquement à cartographier les stratégies existantes d'adaptation de SAM (fine-tuning, PEFT, auto-prompting, modification de framework, adaptation aux modalités), à en évaluer les bénéfices et les limites pour le diagnostic du cancer, et à identifier les perspectives de développement futur, notamment pour la segmentation 3D et les approches multimodales. L'hypothèse implicite sous-tendant cette revue est que les modèles de fondation, malgré leurs limites actuelles, représentent une voie prometteuse pour améliorer la précision, la reproductibilité et l'efficience de la segmentation tumorale en pratique clinique, à condition de résoudre les défis techniques et éthiques identifiés.

Cette étude propose GC-SAM, un réseau de segmentation léger dérivé du modèle Segment Anything (SAM) et spécifiquement conçu pour la segmentation du cancer gastrique, dont l'encodeur d'images a été compressé par distillation de connaissances (modèle enseignant ViT-b, modèle étudiant ViT-s) tandis que l'encodeur de prompts et le décodeur de masques ont été affinés par fine-tuning. Évalué sur une cohorte interne de 2487 cas ainsi que sur un jeu de données externe (TCGA), GC-SAM surpasse à la fois les réseaux de segmentation classiques, les méthodes avancées récentes et les variantes basées sur SAM, atteignant un Dice de 0,8186 et un mIoU de 0,6504 en interne. Par rapport au modèle SAM original, GC-SAM réduit le nombre de paramètres de 89,2 % et le temps d'inférence de 83,6 %, tout en améliorant simultanément la précision (Dice +5,9 %, mIoU +79,6 %, Pixel Acc +8,6 %). Sur le jeu de données externe TCGA, le modèle maintient des performances élevées (Dice 0,8350, Pixel Acc 0,8210), démontrant une capacité de généralisation robuste en transfert zero-shot. Ces résultats positionnent GC-SAM comme une solution précise et efficiente pour la segmentation du cancer gastrique, ouvrant une voie prometteuse vers le déploiement de modèles d'apprentissage profond sur dispositifs médicaux embarqués.

Cet article de Wei (2024) porte sur la segmentation automatique des tumeurs cérébrales en IRM à partir du Segment Anything Model (SAM), dont la précision est limitée par l'hétérogénéité des niveaux de gris des images médicales. Les auteurs proposent une méthode enrichissant l'architecture SAM par des couches de convolution et de mapping de caractéristiques, dont les sorties sont fusionnées avec les caractéristiques du Transformer au sein de l'encodeur d'image avant injection dans le mask decoder. Cette approche est évaluée sur le jeu de données BraTS2021 et comparée à SAM seul (avec 2 points d'invite, 10 points d'invite, et en mode automatique) ainsi qu'à des architectures de référence telles que U-net, Unet++, ResUnet et TransUnet. Les résultats montrent que la méthode proposée surpasse SAM seul, avec les meilleures performances obtenues sur la région tumorale WT, et que l'augmentation du nombre de points d'invite améliore les résultats de segmentation de SAM. L'étude conclut que la fusion des caractéristiques Transformer et CNN dans l'encodeur d'image permet une segmentation plus précise des tumeurs cérébrales que SAM original, tout en soulignant que seule la modalité T1 a été validée, sans exploitation du contexte inter-coupes, ouvrant la voie à des travaux futurs sur la segmentation multimodale 3D.


## Discussion


Cette étude propose GC-SAM, un réseau de segmentation léger dérivé du modèle Segment Anything (SAM) et spécifiquement conçu pour la segmentation du cancer gastrique, dont l'encodeur d'images a été compressé par distillation de connaissances (modèle enseignant ViT-b, modèle étudiant ViT-s) tandis que l'encodeur de prompts et le décodeur de masques ont été affinés par fine-tuning. Évalué sur une cohorte interne de 2487 cas ainsi que sur un jeu de données externe (TCGA), GC-SAM surpasse à la fois les réseaux de segmentation classiques, les méthodes avancées récentes et les variantes basées sur SAM, atteignant un Dice de 0,8186 et un mIoU de 0,6504 en interne. Par rapport au modèle SAM original, GC-SAM réduit le nombre de paramètres de 89,2 % et le temps d'inférence de 83,6 %, tout en améliorant simultanément la précision (Dice +5,9 %, mIoU +79,6 %, Pixel Acc +8,6 %). Sur le jeu de données externe TCGA, le modèle maintient des performances élevées (Dice 0,8350, Pixel Acc 0,8210), démontrant une capacité de généralisation robuste en transfert zero-shot. Ces résultats positionnent GC-SAM comme une solution précise et efficiente pour la segmentation du cancer gastrique, ouvrant une voie prometteuse vers le déploiement de modèles d'apprentissage profond sur dispositifs médicaux embarqués.