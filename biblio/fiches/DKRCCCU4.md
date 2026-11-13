# Mask-aware foundational-model embeddings for 18F-FDG-PET/CT prognosis in multiple myeloma.



## Resume


Mask-aware foundational-model embeddings for 18F-FDG-PET/CT prognosis in multiple myeloma.

To test whether internal memory states from a medical foundational segmentation model can serve as compact, mask-aware embeddings for predicting progression-free survival (PFS) in multiple myeloma (MM) from whole-body [

Ultra-low-dose 18F-FDG brain PET/MR denoising using deep learning and multi-contrast information

Multi-modal segment anything model (mmSAM) for tumor segmentation in multi-tracer oncologic PET/CT

Abstract Purpose Lesion segmentation is important in targeted radionuclide therapy dosimetry. In this study, we proposed a novel 2D multi-modal Segment Anything Model (mmSAM) for lesion segmentation in whole-body multi-tracer PET/CT images. Methods The AutoPET 2024 dataset, including 18F-PSMA (369 subjects), 18F-FDG (170 subjects) and 68Ga-PSMA (170 subjects) PET/CT images and their corresponding tumor masks, was used in this study. The 18F-PSMA PET/CT dataset was used as the primary dataset and was divided into 233: 36: 100 for training, validation and testing the mmSAM, using both PET and CT input. The transferability of the primary model was evaluated on 100 patients on other 2 datasets, without and with fine-tuning using 70 cases of 18F-FDG and 68Ga-PSMA respectively. Standard single modal 2D SAM with only PET input, 3D nnUNet with two-channel PET/CT input and the thresholding-based method were also implemented for comparison. Mean Dice, the 95th percentile Hausdorff distance (mean

Foundation Models Meet Medical Image Interpretation.

Facing challenges such as limited annotated data and insufficient model generalization in medical deep learning, foundation models (FMs) are reshaping the paradigm of medical image interpretation through large-scale pretraining and efficient fine-tuning. Unlike traditional models focused on single modality and task, FMs enable multi-modal representation and task-agnostic transfer, adapting to various downstream applications without extensive annotation or retraining. This paper systematically reviews the research progress on medical FMs, focusing on medical tasks, datasets, and evaluation metrics. It covers key interpretation tasks such as classification, segmentation, generation, and prognosis prediction. At the data level, it integrates multi-source data including 2-dimensional (2D)/3D medical imaging, vision-language data, electronic health records (EHRs), physiological signals, and bioinformatics data, and summarizes the evaluation metrics for each task. On this basis, the paper ca

18F-FDG Positron Emission Tomography - An Innovative Technique for the Diagnosis of a Canine Lameness.

<h4>Introduction</h4>Positron emission tomography (PET) imaging with fluorine-18-fluorodeoxyglucose (18F-FDG) is widely known for its use in the diagnosis and tracking of primary and metastatic tumors via uptake and retention of the radiopharmaceutical by hypermetabolic cells. 18F-FDG is also used to study the normal physiology of glucose uptake, metabolism, and muscle activity during and after exercise.<h4>Background</h4>A pilot study adding PET imaging to the diagnostic evaluation of canine patients undergoing computed tomography (CT) for mild or intermittent thoracic and pelvic limb lameness is ongoing. Dogs with an observable (grade 1-2/5) lameness that have undergone routine radiography and complete physical examination by board-certified veterinary surgeons and sports medicine and rehabilitation specialists are enrolled. Each patient undergoes leash walking for 15 min prior to premedication and induction of general anesthesia for the PET-CT examination. 18F-FDG is injected intrav

Large Foundation Model for Cancer Segmentation.

Recently, large language models such as ChatGPT have made huge strides in understanding and generating human-like text and have demonstrated considerable success in natural language processing. These foundation models also perform well in computer vision. However, there is a growing need to use these technologies for specific medical tasks, especially for identifying cancer in images. This paper looks at how these foundation models, such as the segment anything model, could be used for cancer segmentation, discussing the potential benefits and challenges of applying large foundation models to help with cancer diagnoses.

Foundation Models for Volumetric Medical Imaging: Opportunities, Challenges, and Future Directions

Foundation models, known as the large-scale, pretrained models capable of generalizing across diverse tasks, have significantly advanced the field of medical image analysis. While most early applications focused on 2D modalities, the unique challenges and opportunities associated with volumetric medical imaging have recently attracted growing interest. This study provides a comprehensive overview of the current landscape of foundation models tailored for volumetric medical image analysis, with a focus on CT, MRI, and PET imaging. We examine key components of these models, including 3D architectures, training strategies, and supported modalities. In addition, we highlight their contribution to major clinical tasks such as classification and prediction, segmentation, image registration, quality enhancement, and visual question answering. Critical challenges of these models, including high computational cost, limited and less diverse 3D datasets, and domain adaptation, are discussed alongside the promising solutions and future research directions. By synthesizing recent advances in volumetric foundation models and outlining key technical and clinical challenges, this review provides a thorough roadmap toward the development of scalable, generalizable, and clinically applicable AI systems for volumetric medical images.

FM-Adapt: Foundation model adaptation with photoacoustic-supervised learning for interventional ultrasound.

Foundation models (FMs), such as the Segment Anything Model (SAM), have remarkable capabilities for general-purpose segmentation tasks through large-scale pre-training. However, a substantial domain shift limits their effectiveness in complex medical imaging. Here we introduce FM-Adapt, the first parameter-efficient adaptation of a FM (SAM-based vision transformer) into a resolution-agnostic architecture with photoacoustic (PA)-supervised learning for dual-target interventional ultrasound (US) segmentation. We demonstrate FM-Adapt in the context of PA-supervised interventions, specifically for US-guided needle tracking and simultaneous target identification (breast tumor segmentation). We train once with this unified adaptation framework to produce two specialized model weights: USPA-SAM for real-time tracking of needles and BT-SAM for segmenting breast tumors. This framework utilizes frozen pre-trained encoder components and fine-tunes only the mask decoder, allowing the model to proc

Foundation Models for Biomedical Image Segmentation: A Survey

Adaptation of Foundation Models for Medical Image Analysis: Strategies, Challenges, and Future Directions

Foundation models (FMs) have emerged as a transformative paradigm in medical image analysis, offering the potential to provide generalizable, task-agnostic solutions across a wide range of clinical tasks and imaging modalities. Their capacity to learn transferable representations from large-scale data has the potential to address the limitations of conventional task-specific models. However, adaptation of FMs to real-world clinical practice remains constrained by key challenges, including domain shifts, limited availability of high-quality annotated data, substantial computational demands, and strict privacy requirements. This review presents a comprehensive assessment of strategies for adapting FMs to the specific demands of medical imaging. We examine approaches such as supervised fine-tuning, domain-specific pretraining, parameter-efficient fine-tuning, self-supervised learning, hybrid methods, and multimodal or cross-modal frameworks. For each, we evaluate reported performance gain


## Insight


methodology: Le PET-CT au 18F-FDG peut fournir des données physiologiques complémentaires aux techniques d’imagerie morphologique standard (radiographie, échographie, CT), potentiellement utiles pour détecter des anomalies musculaires subtiles non apparentes autrement.

methodology: Le PET/TDM au Na18F corégistré à l’IRM constitue une approche multimodale visant à détecter et quantifier les altérations osseuses pathologiques précoces dans un modèle canin de PTOA du genou induite par ACLT, en complément de l’évaluation morphologique par IRM.

feasibility: Le Na18F PET/CT corégistré à l’IRM apparaît comme un outil diagnostique réalisable pour visualiser et quantifier par SUV max le métabolisme osseux pathologique, de manière régionalisée, dans un modèle préclinique canin de PTOA du genou.


## Synthese


La tomographie par émission de positons au 18F-FDG, largement utilisée pour le diagnostic et le suivi des tumeurs primaires et métastatiques via la captation du radiotraceur par les cellules hypermétaboliques, trouve également des applications dans l’étude de la physiologie de l’uptake du glucose et de l’activité musculaire. Les données physiologiques supplémentaires fournies par le PET présentent un intérêt particulier en médecine du sport et en rééducation vétérinaire, car elles peuvent contribuer au diagnostic d’anomalies subtiles non détectables par radiographie ou échographie. Contrairement à l’échographie ou à l’IRM, le PET-CT permet un balayage corporel global avec localisation morphologique objective des lésions et mesures fonctionnelles quantifiables, utiles pour documenter la réponse thérapeutique dans des groupes musculaires difficiles à évaluer autrement. L’accessibilité croissante des équipements PET-CT intégrés dans les centres universitaires et de référence vétérinaires, associée à une demi-vie courte du fluor-18 (110 min) permettant la libération du patient le jour même, favorise l’emploi du 18F-FDG comme complément diagnostique aux findings CT chez les chiens présentant des pathologies d’épaule, de coude, du rachis lombaire ou des membres pelviens.

La tomographie par émission de positons au 18F-FDG, largement utilisée pour le diagnostic et le suivi des tumeurs primaires et métastatiques via la captation du radiotraceur par les cellules hypermétaboliques, trouve également des applications dans l’étude de la physiologie de l’uptake du glucose et de l’activité musculaire. Les données physiologiques supplémentaires fournies par le PET présentent un intérêt particulier en médecine du sport et en rééducation vétérinaire, car elles peuvent contribuer au diagnostic d’anomalies subtiles non détectables par radiographie ou échographie. Contrairement à l’échographie ou à l’IRM, le PET-CT permet un balayage corporel global avec localisation morphologique objective des lésions et mesures fonctionnelles quantifiables, utiles pour documenter la réponse thérapeutique dans des groupes musculaires difficiles à évaluer autrement. L’accessibilité croissante des équipements PET-CT intégrés dans les centres universitaires et de référence vétérinaires, associée à une demi-vie courte du fluor-18 (110 min) permettant la libération du patient le jour même, favorise l’emploi du 18F-FDG comme complément diagnostique aux findings CT chez les chiens présentant des pathologies d’épaule, de coude, du rachis lombaire ou des membres pelviens. Dans ce rapport de cas, les examens cliniques initiaux ont confirmé une boiterie chronique légère du membre thoracique droit sans en localiser la cause, ce qui a motivé la réalisation d’un PET-CT au 18F-FDG. L’analyse des images fusionnées, avec une fenêtre SUV étroite (0–5), a révélé une captation asymétrique du radiopharmaceutique dans le muscle fléchisseur ulnaire du carpe (FCU) droit (SUVmax 2,4 versus 1,0 controlatéral), interprétée comme le reflet d’une activité métabolique cellulaire accrue liée à une surutilisation compensatoire, une inflammation ou une lésion. L’échographie a ensuite mis en évidence deux foyers hypoéchogènes et des fibres musculaires irrégulières juste proximales à l’insertion sur l’os carpal accessoire, confirmant une déchirure du FCU droit coïncidant avec la zone d’IRU la plus intense. L’étendue de l’IRU délimitait une atteinte musculaire plus large que le foyer discret de rehaussement contrasté au CT. Les auteurs soulignent également des précautions méthodologiques spécifiques à l’imagerie PET-CT vétérinaire afin d’optimiser la détection d’une captation musculaire asymétrique pathologique.


## Methodologie


La tomographie par émission de positons au 18F-FDG, largement utilisée pour le diagnostic et le suivi des tumeurs primaires et métastatiques via la captation du radiotraceur par les cellules hypermétaboliques, trouve également des applications dans l’étude de la physiologie de l’uptake du glucose et de l’activité musculaire. Les données physiologiques supplémentaires fournies par le PET présentent un intérêt particulier en médecine du sport et en rééducation vétérinaire, car elles peuvent contribuer au diagnostic d’anomalies subtiles non détectables par radiographie ou échographie. Contrairement à l’échographie ou à l’IRM, le PET-CT permet un balayage corporel global avec localisation morphologique objective des lésions et mesures fonctionnelles quantifiables, utiles pour documenter la réponse thérapeutique dans des groupes musculaires difficiles à évaluer autrement. L’accessibilité croissante des équipements PET-CT intégrés dans les centres universitaires et de référence vétérinaires, associée à une demi-vie courte du fluor-18 (110 min) permettant la libération du patient le jour même, favorise l’emploi du 18F-FDG comme complément diagnostique aux findings CT chez les chiens présentant des pathologies d’épaule, de coude, du rachis lombaire ou des membres pelviens.


## Quote


Examiner comment les modèles de fondation, tels que le segment anything model, pourraient être utilisés pour la segmentation du cancer; Discuter des bénéfices potentiels de l'application de grands modèles de fondation pour aider aux diagnostics du cancer

A centroid-based masking technique incorporating features like the area and diameter of each vertebra to generate masks for each 2D slice of MR images • Modified attention UNET has been used for tumor segmentation incorporating multilabel masking for classifying the vertebra after 3D volume

This study evaluates the possibility of using foundation models for image segmentation as a basis for landmarking medical X-rays.

Therefore, in this study, we assess the feasibility of a novel approach of Na 18 F PET/CT coregistered with MRI to detect and quantify pathological bone changes in this canine model of PTOA.

This is achieved by incorporating our proposed Self-Sorting Memory Bank, which selects the most confident embeddings based on the confidence predictions (α, β, γ) from the mask decoder.

Les modèles de fondation comme SAM et le Segment-Everything-Everywhere Model montrent une adaptabilité et une efficacité exceptionnelles sur diverses tâches de segmentation en vision par ordinateur générale, mais leur application directe à la segmentation du cancer en imagerie médicale reste insatisfaisante en raison de défis spécifiques liés à la résolution, aux échelles, aux prompts et au fine-tuning.

This research focuses on improving model sensitivity to small-scale tumors and early-stage lesions, facilitating more effective early clinical screening.

Presented in Fig. 3 is a comparative visualization of lung segmentation masks, which displays chest X-ray images with three types of segmentation: initial MedSAM model predictions, refined outputs from the retrained HybridMS model, and expert-annotated ground truth masks.


## Raw_Overall_Architecture


embeddings and appended to the support memory to predict the pseudo-mask of the next slice. The details of each module are explained below.

embeddings and appended to the support memory to predict the pseudo-mask of the next slice. The details of each module are explained below.

As shown in Fig. 2, the proposed model comprised four key components: the feature extraction (FE) module, the pseudo-mask generation (PMG) module, the 3D memory encoding (3DM) module, and the pseudo-mask attention (PMA) module. The feature extraction module processed images from both the query and support sets, extracting multiscale features. The pseudo-mask generation module encoded the extracted image embeddings of the support set with the corresponding masks to generate support memories. These support memories were then fused with the query image embeddings and passed through a decoder to produce a pseudo-mask for the query image. The pseudo-mask attention module leveraged this pseudo-mask to generate a bounding box prompt, applied mask attention between the pseudo-mask and query embeddings, and outputed a segmentation map based on the box prompt, pseudo-mask and query embeddings. For the 3D memory encoding module, the prediction of the current slice was encoded to obtain the image

As shown in Fig. 2, the proposed model comprised four key components: the feature extraction (FE) module, the pseudo-mask generation (PMG) module, the 3D memory encoding (3DM) module, and the pseudo-mask attention (PMA) module. The feature extraction module processed images from both the query and support sets, extracting multiscale features. The pseudo-mask generation module encoded the extracted image embeddings of the support set with the corresponding masks to generate support memories. These support memories were then fused with the query image embeddings and passed through a decoder to produce a pseudo-mask for the query image. The pseudo-mask attention module leveraged this pseudo-mask to generate a bounding box prompt, applied mask attention between the pseudo-mask and query embeddings, and outputed a segmentation map based on the box prompt, pseudo-mask and query embeddings. For the 3D memory encoding module, the prediction of the current slice was encoded to obtain the image


## Conclusion


This exploratory study suggests that PET improves the ability to detect lesions and to determine the clinical significance of CT findings in dogs with elbow pain. 18F-NaF uptake in bone indicates active injury or stress modeling that is more likely to be associated with a current source of pain. PET could prove to be a valuable adjunctive imaging modality for patients with unlocalizable lameness, or localized bone pain with no identifiable structural lesions.

Na 18 F PET/CT coregistered with MRI is a feasible molecular imaging biomarker to assess knee osseous metabolic changes serially in an in vivo canine model of knee PTOA The approach brings a novel musculoskeletal preclinical imaging methodology that can provide unique insights into PTOA pathophysiology Jointly with previous 18 F-FDG observations, a noninvasive multimodal imaging methodology can investigate OA pathophysiology through molecular imaging biomarkers where bone changes and inflammation are major parameters to assess early PTOA