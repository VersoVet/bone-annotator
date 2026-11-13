# Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM).



## Resume


Corrigendum to “Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM)”

Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM).

BackgroundComputed tomography (CT) is widely used in clinical diagnosis of lung diseases. The automatic segmentation of lesions in CT images aids in the development of intelligent lung disease diagnosis.ObjectiveThis study aims to address the issue of imprecise segmentation in CT images due to the blurred detailed features of lesions, which can easily be confused with surrounding tissues.MethodsWe proposed a promptable segmentation method based on an improved U-Net and Segment Anything model (SAM) to improve segmentation accuracy of lung lesions in CT images. The improved U-Net incorporates a multi-scale attention module based on a channel attention mechanism ECA (Efficient Channel Attention) to improve recognition of detailed feature information at edge of lesions; and a promptable clipping module to incorporate physicians' prior knowledge into the model to reduce background interference. Segment Anything model (SAM) has a strong ability to recognize lesions and pulmonary atelectasis

Tumor-SAM: segment anything model for semi-automatic lung tumor segmentation in CT

Towards an automated Segment Anything Model (SAM) for lesion segmentation in oncological PET/CT images

Lung segment anything model (LuSAM): a decoupled prompt-integrated framework for automated lung segmentation on chest x-Ray images.

Accurate lung segmentation in chest x-ray images plays a pivotal role in early disease detection and clinical decision-making. In this study, we introduce an innovative approach to enhance the precision of lung segmentation using the Segment Anything Model (SAM). Despite its versatility, SAM faces the challenge of prompt decoupling, often resulting in misclassifications, especially with intricate structures like the clavicle. Our research focuses on the integration of spatial attention mechanisms within SAM. This approach enables the model to concentrate specifically on the lung region, fostering adaptability to image variations and reducing the likelihood of false positives. This work has the potential to significantly advance lung segmentation, improving the identification and quantification of lung anomalies across diverse clinical contexts.

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

PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation

Automated Lesion Segmentation in Medical Imaging via Integration of nnU-Net Optimization and SAM Approach.

<h4>Background</h4>Deep learning has transformed medical imaging by enabling earlier and more accurate disease diagnosis. Lesion and tumor segmentation, essential for analyzing and tracking morphological changes, is commonly done with U-Net variants, though these often lack cross-domain generalization and do not fully leverage foundation models like the Segment Anything Model (SAM), which still requires manual intervention to define the region of interest (ROI).<h4>Objectives</h4>To enhance generalization and reduce manual intervention by combining the automatic optimization of nnU-Net with the precision of SAM.<h4>Design</h4>Experimental evaluation of a hybrid segmentation framework for lung nodule analysis.<h4>Methods</h4>We propose a novel approach integrating the automatic optimization capabilities of nnU-Net for lesion detection with the high-precision segmentation of SAM, eliminating the need for manual intervention by the clinician. The method was evaluated on the LIDC-IDRI data

Enhancing lung segmentation in chest X-rays via SAM with anatomical priors and boundary-aware loss.

Accurate lung segmentation in chest X-rays is a foundational step for computer-aided diagnosis of respiratory diseases such as pneumonia, tuberculosis, and lung cancer. While the Segment Anything Model (SAM) has demonstrated remarkable zero-shot segmentation capabilities on natural images, its direct application to medical imaging remains limited due to domain shift, low contrast, and ambiguous anatomical boundaries. To address these challenges, we propose a lightweight yet effective adaptation of SAM that integrates (i) a Mask Autoencoder (MAE) as an anatomical prior to enforce global shape consistency, and (ii) a composite loss function combining Binary Cross-Entropy (BCE), Dice, and Boundary losses to jointly optimize pixel-level accuracy, region overlap, and edge fidelity. Our parameter-efficient fine-tuning strategy trains only 0.3% of SAM's parameters, specifically the mask decoder, while freezing the image and prompt encoders. Evaluated on the MedSeg Chest X-ray Lung Dataset, ou

How Segment Anything Model (Sam) Boost Medical Image Segmentation: A Survey

Segment Anything Model (SAM) for Medical Image Segmentation: A Preliminary Review

TA-MedSAM: Text-augmented improved MedSAM for pulmonary lesion segmentation.

Accurate segmentation of lung lesions is critical for clinical diagnosis. Traditional methods rely solely on unimodal visual data, which limits the performance of existing medical image segmentation models. This paper introduces a novel approach, Text-Augmented Medical Segment Anything Module(TA-MedSAM), which enhances cross-modal representation capabilities through a vision-language fusion paradigm. This method significantly improves segmentation accuracy for pulmonary lesions with challenging characteristics including low contrast, blurred boundaries, complex morphology, and small size. Firstly, we introduce a lightweight Medical Segment Anything Model (MedSAM) image encoder and a pre-trained ClinicalBERT text encoder to extract visual and textual features, This design preserves segmentation performance while reducing model parameters and computational costs, thereby enhancing inference speed. Secondly, a Reconstruction Text Module is proposed to focus the model on lesion-centric tex

Foundational Segmentation Models and Clinical Data Mining Enable Accurate Computer Vision for Lung Cancer.

This study aims to assess the effectiveness of integrating Segment Anything Model (SAM) and its variant MedSAM into the automated mining, object detection, and segmentation (MODS) methodology for developing robust lung cancer detection and segmentation models without post hoc labeling of training images. In a retrospective analysis, 10,000 chest computed tomography scans from patients with lung cancer were mined. Line measurement annotations were converted to bounding boxes, excluding boxes < 1 cm or > 7 cm. The You Only Look Once object detection architecture was used for teacher-student learning to label unannotated lesions on the training images. Subsequently, a final tumor detection model was trained and employed with SAM and MedSAM for tumor segmentation. Model performance was assessed on a manually annotated test dataset, with additional evaluations conducted on an external lung cancer dataset before and after detection model fine-tuning. Bootstrap resampling was used to calculat

Zero-shot swift lung 4D CT segmentation via optimized Segment Anything Model

StructSAM: structure-aware prompt adaptation for robust lung cancer lesion segmentation in CT.

Accurate delineation of lung lesions in computed tomography (CT) scans is critical for diagnosis, staging, and treatment planning, yet remains a challenging task. While foundation models like the Segment Anything Model (SAM) excel in natural images, they often falter in medical imaging due to low contrast, ambiguous boundaries, and a lack of 3D context. To address these limitations, we propose StructSAM, a structure-aware prompt adaptation framework designed for robust volumetric segmentation, with a primary focus on lung cancer. StructSAM injects anatomical priors into the prompt pathway, employs a 3D inter-slice aggregator for volumetric consistency, and leverages PEFT for scalability. Experiments on the LIDC-IDRI dataset demonstrate that StructSAM achieves state-of-the-art accuracy on lung nodule segmentation, outperforming both classical architectures and SAM-based adaptations. Crucially, extended cross-organ evaluations on KiTS19 and MSD Pancreas datasets reveal that StructSAM eff

Trans-SAM: Transfer Segment Anything Model to medical image segmentation with Parameter-Efficient Fine-Tuning

ST-SAM: A Spatio-Temporal Enhanced Segment Anything Model for Echocardiogram Video Segmentation

SAM-guided Cross Pseudo Supervision Learning for Semi-supervised Medical Image Segmentation.

Precise identification of lesions in medical images is crucial for accurate diagnosis and successful treatment. Nevertheless, the limited availability of annotations, coupled with the intricate nature of lesion characteristics, imposes significant constraints on the model's representational capacity. The recently developed vision foundation model, Segment Anything Model (SAM), featuring its unique capability for prompt interaction, has demonstrated remarkable capabilities in natural image segmentation. However, it encounters performance degradation in medical scenarios due to the absence of domain-specific medical knowledge. To address the aforementioned issues, we propose a novel SAM-assisted semi-supervised framework for accurate lesion segmentation, even in scenarios with extremely limited annotations. Concretely, our approach adopts a dual-branch architecture, where each branch incorporates a SAM (ViT-Base) model fine-tuned with adapters. We further design a point prompts generator

SAMCT: Segment Any CT Allowing Labor-Free Task-Indicator Prompts.

Segment anything model (SAM), a foundation model with superior versatility and generalization across diverse segmentation tasks, has attracted widespread attention in medical imaging. However, it has been proved that SAM would encounter severe performance degradation due to the lack of medical knowledge in training and local feature encoding. Though several SAM-based models have been proposed for tuning SAM in medical imaging, they still suffer from insufficient feature extraction and highly rely on high-quality prompts. In this paper, we propose a powerful foundation model SAMCT allowing labor-free prompts and train it on a collected large CT dataset consisting of 1.1M CT images and 5M masks from public datasets. Specifically, based on SAM, SAMCT is further equipped with a U-shaped CNN image encoder, a cross-branch interaction module, and a task-indicator prompt encoder. The U-shaped CNN image encoder works in parallel with the ViT image encoder in SAM to supplement local features. Cr

Fine-Tuned Segment Anything Model with Low-Rank Adaptation for Chest X-Ray Images.

<b>Background:</b> This paper investigates the use of the Segment Anything Model (SAM) for chest X-ray (CXR) image segmentation, with a focus on improving its performance using low-rank adaptation (LoRA). <b>Methods:</b> We evaluate three versions of SAM: two zero-shot methods (using coordinate and bounding box prompts) and a fine-tuned SAM using LoRA. To support these approaches, we also trained two standard convolutional neural networks (CNNs), U-Net and DeepLabv3+, to generate draft lung segmentations that serve as input prompts for the SAM methods. Our fine-tuning approach uses LoRA to add lightweight trainable adapters within the Transformer blocks of the SAM, allowing only a small subset of parameters to be updated. The rest of the SAM remains frozen, helping preserve its pre-trained knowledge while reducing memory and computational needs. We tested all models on a dataset of CXR images labeled for COVID-19, viral pneumonia, and normal cases. <b>Results:</b> Results show that fin

LeSAM: Adapt Segment Anything Model for Medical Lesion Segmentation.

The Segment Anything Model (SAM) is a foundational model that has demonstrated impressive results in the field of natural image segmentation. However, its performance remains suboptimal for medical image segmentation, particularly when delineating lesions with irregular shapes and low contrast. This can be attributed to the significant domain gap between medical images and natural images on which SAM was originally trained. In this paper, we propose an adaptation of SAM specifically tailored for lesion segmentation termed LeSAM. LeSAM first learns medical-specific domain knowledge through an efficient adaptation module and integrates it with the general knowledge obtained from the pre-trained SAM. Subsequently, we leverage this merged knowledge to generate lesion masks using a modified mask decoder implemented as a lightweight U-shaped network design. This modification enables better delineation of lesion boundaries while facilitating ease of training. We conduct comprehensive experime


## Conclusion


Une nouvelle approche intégrant l'architecture nnU-Net avec le modèle SAM a été introduite, permettant la segmentation automatique de lésions dans les images médicales sans nécessiter de prompt manuel de la part des radiologues L'approche peut être appliquée à travers différents domaines d'imagerie médicale En s'appuyant sur l'architecture nnU-Net, aucune configuration manuelle de l'architecture ou du pipeline d'entraînement n'est nécessaire, ce qui généralise le problème et permet un gain de temps L'approche proposée a été appliquée à la segmentation des nodules pulmonaires, dont la détection précoce peut améliorer le pronostic de la maladie Des nodules de tailles variées peuvent être détectés pour analyse ultérieure Le modèle proposé est indépendant de l'architecture de base utilisée pour générer le masque de segmentation initial, car les bounding boxes de la région d'intérêt sont extraites automatiquement L'approche se concentre sur la région d'intérêt au niveau local, permettant à SAM d'obtenir une segmentation plus précise de la zone affectée Le modèle de segmentation proposé est particulièrement utile pour le développement d'un système CAD complet de segmentation et classification Les résultats obtenus avec les différents modèles de classification indiquent que le modèle proposé atteint une performance comparable à celle d'un expert dans la classification de la maladie


## Synthese


Les modèles de segmentation basés sur CNN ou ViT, bien qu'efficaces, restent spécifiques à une tâche et généralisent mal à travers la diversité des structures anatomiques visibles en tomodensitométrie (CT). Le Segment Anything Model (SAM), modèle de fondation de référence pour la segmentation, présente des performances dégradées sur les images médicales en raison de l'absence de données médicales à l'entraînement, d'une compréhension sémantique limitée et d'une perte d'information contextuelle locale liée à la taille de sa tokenisation. Les auteurs proposent SAMCT, qui associe le SAM original (gelé) à un sous-réseau CNN en forme de U et à un module d'interaction cross-branch permettant l'échange de sémantique globale et d'informations locales, ainsi qu'un encodeur de prompts task-indicator optionnel et léger pour une segmentation automatisée sans prompt manuel. Le modèle est validé sur CT5M, un jeu de données constitué de 1,1M d'images et 5M de masques issus de 30 jeux de données publics couvrant 118 objets anatomiques répartis sur la tête et le cou, le thorax, l'abdomen, le bassin, les lésions, les os et les vaisseaux. Les résultats expérimentaux montrent que SAMCT surpasse les modèles de fondation et les modèles spécifiques à la tâche de l'état de l'art, tant en versatilité qu'en généralisation.

L'objectif de cet article de synthèse est d'examiner comment les grands modèles de fondation en vision par ordinateur, en particulier le Segment Anything Model (SAM), peuvent être adaptés et exploités pour la segmentation du cancer en imagerie médicale, dans un contexte scientifique marqué par le succès de SAM sur des tâches de segmentation généralistes mais des performances insatisfaisantes lorsqu'il est appliqué tel quel à des images oncologiques. Les auteurs cherchent spécifiquement à cartographier les stratégies existantes d'adaptation de SAM (fine-tuning, PEFT, auto-prompting, modification de framework, adaptation aux modalités), à en évaluer les bénéfices et les limites pour le diagnostic du cancer, et à identifier les perspectives de développement futur, notamment pour la segmentation 3D et les approches multimodales. L'hypothèse implicite sous-tendant cette revue est que les modèles de fondation, malgré leurs limites actuelles, représentent une voie prometteuse pour améliorer la précision, la reproductibilité et l'efficience de la segmentation tumorale en pratique clinique, à condition de résoudre les défis techniques et éthiques identifiés.


## Methodologie


Les modèles de segmentation basés sur CNN ou ViT, bien qu'efficaces, restent spécifiques à une tâche et généralisent mal à travers la diversité des structures anatomiques visibles en tomodensitométrie (CT). Le Segment Anything Model (SAM), modèle de fondation de référence pour la segmentation, présente des performances dégradées sur les images médicales en raison de l'absence de données médicales à l'entraînement, d'une compréhension sémantique limitée et d'une perte d'information contextuelle locale liée à la taille de sa tokenisation. Les auteurs proposent SAMCT, qui associe le SAM original (gelé) à un sous-réseau CNN en forme de U et à un module d'interaction cross-branch permettant l'échange de sémantique globale et d'informations locales, ainsi qu'un encodeur de prompts task-indicator optionnel et léger pour une segmentation automatisée sans prompt manuel. Le modèle est validé sur CT5M, un jeu de données constitué de 1,1M d'images et 5M de masques issus de 30 jeux de données publics couvrant 118 objets anatomiques répartis sur la tête et le cou, le thorax, l'abdomen, le bassin, les lésions, les os et les vaisseaux. Les résultats expérimentaux montrent que SAMCT surpasse les modèles de fondation et les modèles spécifiques à la tâche de l'état de l'art, tant en versatilité qu'en généralisation.

La segmentation pulmonaire sur radiographies thoraciques constitue une étape essentielle du diagnostic, mais demeure complexe en raison des conditions d’acquisition, des altérations liées aux maladies et de la variabilité anatomique des poumons. Les travaux antérieurs ont principalement mobilisé des variantes de U-Net, des mécanismes d’attention, des architectures convolutives telles que DeepLab-v3+, ainsi que des modèles fondés sur les Transformers, avec des performances variables selon les jeux de données. L’étude compare trois modalités d’utilisation du Segment Anything Model (SAM) pour la segmentation pulmonaire : l’inférence zero-shot avec des invites de coordonnées, l’inférence zero-shot avec des boîtes englobantes et l’adaptation par fine-tuning au moyen de LoRA. Ces approches sont évaluées par rapport à U-Net et DeepLab-v3+, lesquels servent également à produire les segmentations préliminaires nécessaires à la génération des invites des méthodes zero-shot. Les données extraites indiquent que l’augmentation du nombre d’invites améliore les résultats zero-shot, mais que SAM adapté par LoRA obtient les meilleures performances globales en exactitude, en indice d’intersection sur union et en coefficient de Dice [Unknown](zotero://select/library/items/P2MJKTP8).


## Raw_Introduction


y do not need to be fine-tuned for medical imaging tasks and can operate directly out-of-the-box. The Segment Anything Model (SAM) is one such popular and open-source foundational model based on vision transformers (ViTs) with the ability for zero-shot semantic segmentation [8,12]. SAM works by interactively prompting images with sparse annotations, such as points or bounding boxes, to generate segmentation masks (Figure 1).

y do not need to be fine-tuned for medical imaging tasks and can operate directly out-of-the-box. The Segment Anything Model (SAM) is one such popular and open-source foundational model based on vision transformers (ViTs) with the ability for zero-shot semantic segmentation [8,12]. SAM works by interactively prompting images with sparse annotations, such as points or bounding boxes, to generate segmentation masks (Figure 1).


## Raw_Problem_Setup


Given a Segment Anything Model f SAM , we aim to apply f SAM to the current image sample x t to obtain segmentation masks according to the particular medical image segmentation task at hand. Since SAM and its variants require points and/or bounding boxes as prompts for generating segmentation masks, we assume that each object of interest in x t is given at least a prompt (e.g., a center point or a bounding box). This problem setup was utilized in previous work (e.g., [17,11]).

Given a Segment Anything Model f SAM , we aim to apply f SAM to the current image sample x t to obtain segmentation masks according to the particular medical image segmentation task at hand. Since SAM and its variants require points and/or bounding boxes as prompts for generating segmentation masks, we assume that each object of interest in x t is given at least a prompt (e.g., a center point or a bounding box). This problem setup was utilized in previous work (e.g., [17,11]).