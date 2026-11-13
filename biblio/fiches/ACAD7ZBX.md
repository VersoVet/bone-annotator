# OHIF -SAM2: Accelerating Radiology Workflows with Meta Segment Anything Model 2



## Resume


OHIF -SAM2: Accelerating Radiology Workflows with Meta Segment Anything Model 2

OHIF-SAM2: Accelerating Radiology Workflows with Segment Anything Model 2

The release of Segment Anything Models (SAM1 and SAM2) by Meta has significantly influenced various domains, including medical imaging. However, existing implementations of SAM primarily focus on standalone tools that require local installation and configuration, limiting accessibility and ease of use. In this work, we present the web-based extension of SAM2 integrated into the Open Health Imaging Foundation (OHIF) viewer. Our solution supports all SAM2 prompt types, including points and bounding boxes, and enables multi-label predictions. This web-based integration eliminates installation requirements, offering a more user-friendly interface. The implementation is open-source and available at https://github.com/CCI-Bonn/OHIF-SAM2.

RepViT-MedSAM: Efficient Segment Anything in the Medical Images

Medical SAM 2: Segment medical images as video via Segment Anything Model 2

Medical image segmentation plays a pivotal role in clinical diagnostics and treatment planning, yet existing models often face challenges in generalization and in handling both 2D and 3D data uniformly. In this paper, we introduce Medical SAM 2 (MedSAM-2), a generalized auto-tracking model for universal 2D and 3D medical image segmentation. The core concept is to leverage the Segment Anything Model 2 (SAM2) pipeline to treat all 2D and 3D medical segmentation tasks as a video object tracking problem. To put it into practice, we propose a novel \emph{self-sorting memory bank} mechanism that dynamically selects informative embeddings based on confidence and dissimilarity, regardless of temporal order. This mechanism not only significantly improves performance in 3D medical image segmentation but also unlocks a \emph{One-Prompt Segmentation} capability for 2D images, allowing segmentation across multiple images from a single prompt without temporal relationships. We evaluated MedSAM-2 on

Reducing manual workload in CT and MRI annotation with the Segment Anything Model 2.

BACKGROUND: Volumetric segmentation in CT and MRI is valuable for artificial intelligence workflows in radiology, yet creating the large, precisely annotated datasets required for training segmentation models remains laborious. METHODS: Here, we tested in simulation whether the foundation model “Segment Anything Model 2” (SAM 2) can reduce expert annotation workload. In our workflow, annotators provide a single box at the object’s center, and SAM 2 automatically segments the object across slices; annotators then review and correct the masks as needed. Workload reduction was defined as the proportion of SAM 2’s predicted segmentation masks that were accepted without modification. Downstream segmentation models were then trained on the SAM 2-assisted masks and compared with reference models trained on ground truth masks. RESULTS: For femoral bone segmentation in MRI and liver tumor segmentation in CT, 36,614 sagittal and 16,311 axial slices were annotated, with 30% and 53% of SAM 2-gener

Hemo-FS-SAM2: Few-Shot Tuning on Hemorrhage Segmentation of Segment Anything Model 2

Trans-SAM: Transfer Segment Anything Model to medical image segmentation with Parameter-Efficient Fine-Tuning

How Segment Anything Model (Sam) Boost Medical Image Segmentation: A Survey

A review of the Segment Anything Model (SAM) for medical image analysis: Accomplishments and perspectives

Biomedical SAM 2: Segment Anything in Biomedical Images and Videos

Medical image segmentation and video object segmentation are essential for diagnosing and analyzing diseases by identifying and measuring biological structures. Recent advances in natural domain have been driven by foundation models like the Segment Anything Model 2 (SAM-2). To explore the performance of SAM-2 in biomedical applications, we designed three evaluation pipelines for single-frame 2D image segmentation, multi-frame 3D image segmentation and multi-frame video segmentation with varied prompt designs, revealing SAM-2's limitations in medical contexts. Consequently, we developed BioSAM-2, an enhanced foundation model optimized for biomedical data based on SAM-2. Our experiments show that BioSAM-2 not only surpasses the performance of existing state-of-the-art foundation models but also matches or even exceeds specialist models, demonstrating its efficacy and potential in the medical domain.

Segment Anything Model (SAM) for Medical Image Segmentation: A Preliminary Review

Depthwise-Dilated Convolutional Adapters for Medical Object Tracking and Segmentation Using the Segment Anything Model 2

Recent advances in medical image segmentation have been driven by deep learning; however, most existing methods remain limited by modality-specific designs and exhibit poor adaptability to dynamic medical imaging scenarios. The Segment Anything Model 2 (SAM2) and its related variants, which introduce a streaming memory mechanism for real-time video segmentation, present new opportunities for prompt-based, generalizable solutions. Nevertheless, adapting these models to medical video scenarios typically requires large-scale datasets for retraining or transfer learning, leading to high computational costs and the risk of catastrophic forgetting. To address these challenges, we propose DD-SAM2, an efficient adaptation framework for SAM2 that incorporates a Depthwise-Dilated Adapter (DD-Adapter) to enhance multi-scale feature extraction with minimal parameter overhead. This design enables effective fine-tuning of SAM2 on medical videos with limited training data. Unlike existing adapter-bas

Segment Anything in Medical Images and Videos: Benchmark and Deployment

Recent advances in segmentation foundation models have enabled accurate and efficient segmentation across a wide range of natural images and videos, but their utility to medical data remains unclear. In this work, we first present a comprehensive benchmarking of the Segment Anything Model 2 (SAM2) across 11 medical image modalities and videos and point out its strengths and weaknesses by comparing it to SAM1 and MedSAM. Then, we develop a transfer learning pipeline and demonstrate SAM2 can be quickly adapted to medical domain by fine-tuning. Furthermore, we implement SAM2 as a 3D slicer plugin and Gradio API for efficient 3D image and video segmentation. The code has been made publicly available at \url{https://github.com/bowang-lab/MedSAM}.

ExpertsMedSAM: Faster Medical Image Segment Anything with Mixture-of-Experts

Vessel-SAM2: Adapting Segment Anything 2 for Patch-Free Retinal Vessel Segmentation in Ultra-High Resolution Fundus Images

Towards an automated Segment Anything Model (SAM) for lesion segmentation in oncological PET/CT images

The Role of Segment Anything Model (SAM) In Medical Image Segmentation: A Comprehensive Review

Comprehensive Multimodal Segmentation in Medical Imaging: Combining YOLOv8 with SAM and HQ-SAM Models

SAM2-Adapter: Evaluating &amp; Adapting Segment Anything 2 in Downstream Tasks: Camouflage, Shadow, Medical Image Segmentation, and More

The advent of large models, also known as foundation models, has significantly transformed the AI research landscape, with models like Segment Anything (SAM) achieving notable success in diverse image segmentation scenarios. Despite its advancements, SAM encountered limitations in handling some complex low-level segmentation tasks like camouflaged object and medical imaging. In response, in 2023, we introduced SAM-Adapter, which demonstrated improved performance on these challenging tasks. Now, with the release of Segment Anything 2 (SAM2)&amp;mdash;a successor with enhanced architecture and a larger training corpus&amp;mdash;we reassess these challenges. This paper introduces SAM2-Adapter, the first adapter designed to overcome the persistent limitations observed in SAM2 and achieve new state-of-the-art (SOTA) results in specific downstream tasks including medical image segmentation, camouflaged (concealed) object detection, and shadow detection. SAM2-Adapter builds on the SAM-Adapter

Segment anything model 2: an application to 2D and 3D medical images

Segment Anything Model (SAM) has gained significant attention because of its ability to segment various objects in images given a prompt. The recently developed SAM 2 has extended this ability to video inputs. This opens an opportunity to apply SAM to 3D images, one of the fundamental tasks in the medical imaging field. In this paper, we extensively evaluate SAM 2's ability to segment both 2D and 3D medical images by first collecting 21 medical imaging datasets, including surgical videos, common 3D modalities such as computed tomography (CT), magnetic resonance imaging (MRI), and positron emission tomography (PET) as well as 2D modalities such as X-ray and ultrasound. Two evaluation settings of SAM 2 are considered: (1) multi-frame 3D segmentation, where prompts are provided to one or multiple slice(s) selected from the volume, and (2) single-frame 2D segmentation, where prompts are provided to each slice. The former only applies to videos and 3D modalities, while the latter applies to

SAM2-Adapter: Evaluating & Adapting Segment Anything 2 in Downstream Tasks: Camouflage, Shadow, Medical Image Segmentation, and More

The advent of large models, also known as foundation models, has significantly transformed the AI research landscape, with models like Segment Anything (SAM) achieving notable success in diverse image segmentation scenarios. Despite its advancements, SAM encountered limitations in handling some complex low-level segmentation tasks like camouflaged object and medical imaging. In response, in 2023, we introduced SAM-Adapter, which demonstrated improved performance on these challenging tasks. Now, with the release of Segment Anything 2 (SAM2), a successor with enhanced architecture and a larger training corpus, we reassess these challenges. This paper introduces SAM2-Adapter, the first adapter designed to overcome the persistent limitations observed in SAM2 and achieve new state-of-the-art (SOTA) results in specific downstream tasks including medical image segmentation, camouflaged (concealed) object detection, and shadow detection. SAM2-Adapter builds on the SAM-Adapter's strengths, offe


## Synthese


Cette étude propose une preuve de concept pour intégrer le Segment Anything Model 2 (SAM 2) dans les flux d'annotation d'imagerie médicale volumétrique (CT et IRM), afin de réduire la charge de travail manuelle inhérente à la délinéation experte requise pour l'entraînement des modèles de segmentation profonde. Le protocole méthodologique repose sur quatre étapes : prétraitement des données, simulation d'un workflow d'annotation assisté par SAM 2 avec des degrés variables d'interaction utilisateur (à partir d'une seule boîte englobante placée sur la coupe centrale d'un objet), entraînement de modèles de segmentation en aval sur les masques ainsi générés, puis évaluation comparative de la réduction de charge de travail et de la performance des modèles par rapport à des modèles entraînés sur des masques de vérité terrain. Cette évaluation a été conduite sur deux cas d'usage représentatifs : la segmentation de l'os fémoral en IRM et celle des tumeurs hépatiques en CT. Les résultats indiquent que SAM 2 réduit substantiellement la charge de travail d'annotation manuelle tout en maintenant la performance des modèles de segmentation en aval, avec respectivement 30 % et 53 % des masques prédits par SAM 2 acceptés sans modification pour l'os fémoral et les tumeurs hépatiques, et des performances de segmentation comparables aux modèles de référence (DSC de 98,5 % contre 98,7 % pour l'os fémoral ; 77,3 % contre 77,0 % pour les tumeurs hépatiques).

Cette étude propose une preuve de concept pour intégrer le Segment Anything Model 2 (SAM 2) dans les flux d'annotation d'imagerie médicale volumétrique (CT et IRM), afin de réduire la charge de travail manuelle inhérente à la délinéation experte requise pour l'entraînement des modèles de segmentation profonde. Le protocole méthodologique repose sur quatre étapes : prétraitement des données, simulation d'un workflow d'annotation assisté par SAM 2 avec des degrés variables d'interaction utilisateur (à partir d'une seule boîte englobante placée sur la coupe centrale d'un objet), entraînement de modèles de segmentation en aval sur les masques ainsi générés, puis évaluation comparative de la réduction de charge de travail et de la performance des modèles par rapport à des modèles entraînés sur des masques de vérité terrain. Cette évaluation a été conduite sur deux cas d'usage représentatifs : la segmentation de l'os fémoral en IRM et celle des tumeurs hépatiques en CT. Les résultats indiquent que SAM 2 réduit substantiellement la charge de travail d'annotation manuelle tout en maintenant la performance des modèles de segmentation en aval, avec respectivement 30 % et 53 % des masques prédits par SAM 2 acceptés sans modification pour l'os fémoral et les tumeurs hépatiques, et des performances de segmentation comparables aux modèles de référence (DSC de 98,5 % contre 98,7 % pour l'os fémoral ; 77,3 % contre 77,0 % pour les tumeurs hépatiques). Cette étude de simulation en quatre étapes démontre que SAM 2, modèle de segmentation promptable généraliste, réduit substantiellement la charge de travail d'annotation manuelle dans des données d'imagerie médicale 3D, tout en préservant la performance des modèles de segmentation en aval, pour deux tâches représentatives : la segmentation de l'os fémoral en IRM et celle des tumeurs hépatiques en CT. Seules les régions inexactes des masques prédits par SAM 2 nécessitaient une correction manuelle, avec 30% des masques acceptés sans modification pour l'os fémoral et 53% pour les tumeurs hépatiques. La performance comparable des modèles entraînés sur des masques assistés par SAM 2 s'explique en partie par le fait que les écarts entre ces masques et la vérité terrain se situent souvent dans la plage de variabilité inter-évaluateurs typique, comme l'illustre le seuil de qualité modéré (DSC 74,0%) proche de la variabilité inter-évaluateurs rapportée pour les tumeurs hépatiques. Bien que le processus d'annotation ait été simulé plutôt que réalisé par des annotateurs humains, le protocole approximait un comportement réaliste, notamment par la variation des prompts en boîte englobante et par des corrections limitées aux erreurs majeures. Les auteurs soulignent des limites, dont l'absence de comparaison avec d'autres modèles de segmentation promptables et le caractère simulé de l'annotation, appelant à des études utilisateurs futures pour valider ces résultats en conditions réelles.


## Methodologie


Cette étude propose une preuve de concept pour intégrer le Segment Anything Model 2 (SAM 2) dans les flux d'annotation d'imagerie médicale volumétrique (CT et IRM), afin de réduire la charge de travail manuelle inhérente à la délinéation experte requise pour l'entraînement des modèles de segmentation profonde. Le protocole méthodologique repose sur quatre étapes : prétraitement des données, simulation d'un workflow d'annotation assisté par SAM 2 avec des degrés variables d'interaction utilisateur (à partir d'une seule boîte englobante placée sur la coupe centrale d'un objet), entraînement de modèles de segmentation en aval sur les masques ainsi générés, puis évaluation comparative de la réduction de charge de travail et de la performance des modèles par rapport à des modèles entraînés sur des masques de vérité terrain. Cette évaluation a été conduite sur deux cas d'usage représentatifs : la segmentation de l'os fémoral en IRM et celle des tumeurs hépatiques en CT. Les résultats indiquent que SAM 2 réduit substantiellement la charge de travail d'annotation manuelle tout en maintenant la performance des modèles de segmentation en aval, avec respectivement 30 % et 53 % des masques prédits par SAM 2 acceptés sans modification pour l'os fémoral et les tumeurs hépatiques, et des performances de segmentation comparables aux modèles de référence (DSC de 98,5 % contre 98,7 % pour l'os fémoral ; 77,3 % contre 77,0 % pour les tumeurs hépatiques).


## Insight


methodology: MedSAM-2 traite l'ensemble des tâches de segmentation d'images médicales, en 2D comme en 3D, comme un problème unifié de suivi d'objets vidéo, en s'appuyant sur l'architecture de Segment Anything Model 2 (SAM 2).

methodology: Le modèle Segment Anything Model 2 (SAM 2) de Meta AI, une méthode innovante de segmentation d'images et de vidéos, offre une précision élevée permettant une segmentation fiable des marqueurs sur des séquences continues d'images CBCT.


## Raw_Introduction


"It is all about how effectively and efficiently we can utilize the Segment Anything Model (SAM) for downstream tasks."

"It is all about how effectively and efficiently we can utilize the Segment Anything Model (SAM) for downstream tasks."


## Quote


we conduct three user studies to demonstrate that MedSAM2 substantially facilitates annotation workflows for high-throughput and efficient segmentation, substantially reducing the time and effort required for creating large-scale medical datasets in various imaging modalities