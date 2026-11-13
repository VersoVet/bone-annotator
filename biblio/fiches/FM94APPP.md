# Lung Segment Anything Model (LuSAM): A Prompt-integrated Framework for Automated Lung Segmentation on ICU Chest X-Ray Images



## Resume


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

Lung segment anything model (LuSAM): a decoupled prompt-integrated framework for automated lung segmentation on chest x-Ray images.

Accurate lung segmentation in chest x-ray images plays a pivotal role in early disease detection and clinical decision-making. In this study, we introduce an innovative approach to enhance the precision of lung segmentation using the Segment Anything Model (SAM). Despite its versatility, SAM faces the challenge of prompt decoupling, often resulting in misclassifications, especially with intricate structures like the clavicle. Our research focuses on the integration of spatial attention mechanisms within SAM. This approach enables the model to concentrate specifically on the lung region, fostering adaptability to image variations and reducing the likelihood of false positives. This work has the potential to significantly advance lung segmentation, improving the identification and quantification of lung anomalies across diverse clinical contexts.

Tumor-SAM: segment anything model for semi-automatic lung tumor segmentation in CT

PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation

Automatic Lung Segmentation in Chest X-Ray Images Using SAM With Prompts From YOLO

Despite the impressive performance of current deep learning models in the field of medical imaging, transferring the lung segmentation task in X-ray images to clinical practice is still a pending task. In this study, the performance of a fully automatic framework for lung field segmentation in chest X-ray images was evaluated. The framework is rooted in the combination of the Segment Anything Model (SAM) with prompt capabilities, and the You Only Look Once (YOLO) model to provide effective prompts. Transfer learning, loss functions, and several validation strategies were thoroughly assessed. This provided a complete benchmark that enabled future research studies to fairly compare new segmentation strategies. The results achieved demonstrated significant robustness and generalization capability against the variability in sensors, populations, disease manifestations, device processing, and imaging conditions. The proposed framework was computationally efficient, could address bias in tra

Enhancing lung segmentation in chest X-rays via SAM with anatomical priors and boundary-aware loss.

Accurate lung segmentation in chest X-rays is a foundational step for computer-aided diagnosis of respiratory diseases such as pneumonia, tuberculosis, and lung cancer. While the Segment Anything Model (SAM) has demonstrated remarkable zero-shot segmentation capabilities on natural images, its direct application to medical imaging remains limited due to domain shift, low contrast, and ambiguous anatomical boundaries. To address these challenges, we propose a lightweight yet effective adaptation of SAM that integrates (i) a Mask Autoencoder (MAE) as an anatomical prior to enforce global shape consistency, and (ii) a composite loss function combining Binary Cross-Entropy (BCE), Dice, and Boundary losses to jointly optimize pixel-level accuracy, region overlap, and edge fidelity. Our parameter-efficient fine-tuning strategy trains only 0.3% of SAM's parameters, specifically the mask decoder, while freezing the image and prompt encoders. Evaluated on the MedSeg Chest X-ray Lung Dataset, ou

Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM).

BackgroundComputed tomography (CT) is widely used in clinical diagnosis of lung diseases. The automatic segmentation of lesions in CT images aids in the development of intelligent lung disease diagnosis.ObjectiveThis study aims to address the issue of imprecise segmentation in CT images due to the blurred detailed features of lesions, which can easily be confused with surrounding tissues.MethodsWe proposed a promptable segmentation method based on an improved U-Net and Segment Anything model (SAM) to improve segmentation accuracy of lung lesions in CT images. The improved U-Net incorporates a multi-scale attention module based on a channel attention mechanism ECA (Efficient Channel Attention) to improve recognition of detailed feature information at edge of lesions; and a promptable clipping module to incorporate physicians' prior knowledge into the model to reduce background interference. Segment Anything model (SAM) has a strong ability to recognize lesions and pulmonary atelectasis

ProtoSAM-3D: Interactive semantic segmentation in volumetric medical imaging via a Segment Anything Model and mask-level prototypes

TA-MedSAM: Text-augmented improved MedSAM for pulmonary lesion segmentation.

Accurate segmentation of lung lesions is critical for clinical diagnosis. Traditional methods rely solely on unimodal visual data, which limits the performance of existing medical image segmentation models. This paper introduces a novel approach, Text-Augmented Medical Segment Anything Module(TA-MedSAM), which enhances cross-modal representation capabilities through a vision-language fusion paradigm. This method significantly improves segmentation accuracy for pulmonary lesions with challenging characteristics including low contrast, blurred boundaries, complex morphology, and small size. Firstly, we introduce a lightweight Medical Segment Anything Model (MedSAM) image encoder and a pre-trained ClinicalBERT text encoder to extract visual and textual features, This design preserves segmentation performance while reducing model parameters and computational costs, thereby enhancing inference speed. Secondly, a Reconstruction Text Module is proposed to focus the model on lesion-centric tex

Towards an automated Segment Anything Model (SAM) for lesion segmentation in oncological PET/CT images

Corrigendum to “Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM)”

Segment Anything Model (SAM) for Medical Image Segmentation: A Preliminary Review

Foundational Segmentation Models and Clinical Data Mining Enable Accurate Computer Vision for Lung Cancer.

This study aims to assess the effectiveness of integrating Segment Anything Model (SAM) and its variant MedSAM into the automated mining, object detection, and segmentation (MODS) methodology for developing robust lung cancer detection and segmentation models without post hoc labeling of training images. In a retrospective analysis, 10,000 chest computed tomography scans from patients with lung cancer were mined. Line measurement annotations were converted to bounding boxes, excluding boxes < 1 cm or > 7 cm. The You Only Look Once object detection architecture was used for teacher-student learning to label unannotated lesions on the training images. Subsequently, a final tumor detection model was trained and employed with SAM and MedSAM for tumor segmentation. Model performance was assessed on a manually annotated test dataset, with additional evaluations conducted on an external lung cancer dataset before and after detection model fine-tuning. Bootstrap resampling was used to calculat

Fine-Tuned Segment Anything Model with Low-Rank Adaptation for Chest X-Ray Images.

<b>Background:</b> This paper investigates the use of the Segment Anything Model (SAM) for chest X-ray (CXR) image segmentation, with a focus on improving its performance using low-rank adaptation (LoRA). <b>Methods:</b> We evaluate three versions of SAM: two zero-shot methods (using coordinate and bounding box prompts) and a fine-tuned SAM using LoRA. To support these approaches, we also trained two standard convolutional neural networks (CNNs), U-Net and DeepLabv3+, to generate draft lung segmentations that serve as input prompts for the SAM methods. Our fine-tuning approach uses LoRA to add lightweight trainable adapters within the Transformer blocks of the SAM, allowing only a small subset of parameters to be updated. The rest of the SAM remains frozen, helping preserve its pre-trained knowledge while reducing memory and computational needs. We tested all models on a dataset of CXR images labeled for COVID-19, viral pneumonia, and normal cases. <b>Results:</b> Results show that fin

Trans-SAM: Transfer Segment Anything Model to medical image segmentation with Parameter-Efficient Fine-Tuning

CoroSAM: adaptation of the Segment Anything Model for interactive segmentation in Coronary angiograms.

X-ray Coronary Angiography (XCA) enables visualization of coronary arteries for disease and morphology assessment. Accurate segmentation of major coronary vessels is crucial for automated analysis of their geometric features but presents challenges due to anatomical complexity. This study introduces CoroSAM, an adaptation of the LiteMedSAM Foundation Model, employing parameter-efficient fine-tuning for interactive coronary artery segmentation in XCA images.

StructSAM: structure-aware prompt adaptation for robust lung cancer lesion segmentation in CT.

Accurate delineation of lung lesions in computed tomography (CT) scans is critical for diagnosis, staging, and treatment planning, yet remains a challenging task. While foundation models like the Segment Anything Model (SAM) excel in natural images, they often falter in medical imaging due to low contrast, ambiguous boundaries, and a lack of 3D context. To address these limitations, we propose StructSAM, a structure-aware prompt adaptation framework designed for robust volumetric segmentation, with a primary focus on lung cancer. StructSAM injects anatomical priors into the prompt pathway, employs a 3D inter-slice aggregator for volumetric consistency, and leverages PEFT for scalability. Experiments on the LIDC-IDRI dataset demonstrate that StructSAM achieves state-of-the-art accuracy on lung nodule segmentation, outperforming both classical architectures and SAM-based adaptations. Crucially, extended cross-organ evaluations on KiTS19 and MSD Pancreas datasets reveal that StructSAM eff

RepViT-MedSAM: Efficient Segment Anything in the Medical Images

ST-SAM: A Spatio-Temporal Enhanced Segment Anything Model for Echocardiogram Video Segmentation

LeSAM: Adapt Segment Anything Model for Medical Lesion Segmentation.

The Segment Anything Model (SAM) is a foundational model that has demonstrated impressive results in the field of natural image segmentation. However, its performance remains suboptimal for medical image segmentation, particularly when delineating lesions with irregular shapes and low contrast. This can be attributed to the significant domain gap between medical images and natural images on which SAM was originally trained. In this paper, we propose an adaptation of SAM specifically tailored for lesion segmentation termed LeSAM. LeSAM first learns medical-specific domain knowledge through an efficient adaptation module and integrates it with the general knowledge obtained from the pre-trained SAM. Subsequently, we leverage this merged knowledge to generate lesion masks using a modified mask decoder implemented as a lightweight U-shaped network design. This modification enables better delineation of lesion boundaries while facilitating ease of training. We conduct comprehensive experime

MedLSAM: Localize and segment anything model for 3D CT images.

Recent advancements in foundation models have shown significant potential in medical image analysis. However, there is still a gap in models specifically designed for medical image localization. To address this, we introduce MedLAM, a 3D medical foundation localization model that accurately identifies any anatomical part within the body using only a few template scans. MedLAM employs two self-supervision tasks: unified anatomical mapping (UAM) and multi-scale similarity (MSS) across a comprehensive dataset of 14,012 CT scans. Furthermore, we developed MedLSAM by integrating MedLAM with the Segment Anything Model (SAM). This innovative framework requires extreme point annotations across three directions on several templates to enable MedLAM to locate the target anatomical structure in the image, with SAM performing the segmentation. It significantly reduces the amount of manual annotation required by SAM in 3D medical imaging scenarios. We conducted extensive experiments on two 3D datas

The Role of Segment Anything Model (SAM) In Medical Image Segmentation: A Comprehensive Review

MedSAM2: Segment Anything in 3D Medical Images and Videos

Medical image and video segmentation is a critical task for precision medicine, which has witnessed considerable progress in developing task or modality-specific and generalist models for 2D images. However, there have been limited studies on building general-purpose models for 3D images and videos with comprehensive user studies. Here, we present MedSAM2, a promptable segmentation foundation model for 3D image and video segmentation. The model is developed by fine-tuning the Segment Anything Model 2 on a large medical dataset with over 455,000 3D image-mask pairs and 76,000 frames, outperforming previous models across a wide range of organs, lesions, and imaging modalities. Furthermore, we implement a human-in-the-loop pipeline to facilitate the creation of large-scale datasets resulting in, to the best of our knowledge, the most extensive user study to date, involving the annotation of 5,000 CT lesions, 3,984 liver MRI lesions, and 251,550 echocardiogram video frames, demonstrating t

FluoroSAM: A Language-promptable Foundation Model for Flexible X-ray Image Segmentation.

Language promptable X-ray image segmentation would enable greater flexibility for human-in-the-loop workflows in diagnostic and interventional precision medicine. Prior efforts have contributed task-specific models capable of solving problems within a narrow scope, but expanding to broader use requires additional data, annotations, and training time. Recently, language-aligned foundation models (LFMs) - machine learning models trained on large amounts of highly variable image and text data thus enabling broad applicability - have emerged as promising tools for automated image analysis. Existing foundation models for medical image analysis focus on scenarios and modalities where large, richly annotated datasets are available. However, the X-ray imaging modality features highly variable image appearance and applications, from diagnostic chest X-rays to interventional fluoroscopy, with varying availability of data. To pave the way toward an LFM for comprehensive and language-aligned analy


## Quote


In this study, a fully automatic framework for lung segmentation in CXR images was evaluated.

By using a foundational model (SAM) for automatic lung segmentation in CXRs and utilizing fully automated prompts from a YOLO model, the lung segmentation goals were effectively addressed.


## Conclusion


Foundation models, particularly MedSAM 2, show strong potential for advancing lung tumor segmentation MedSAM 2 is a promising candidate for real-world medical imaging applications due to superior segmentation performance and relatively low computational cost Continued research, including automated prompt generation and evaluation on larger, more diverse datasets, could support integration into clinical workflows and improve diagnostic accuracy and patient outcomes


## Raw_Introduction


Medical image segmentation is one of the most fundamental tasks in computer-assisted clinical decision support, forming the basis for many downstream applications from diagnosis to treatment planning and response assessment. However, developing medical image segmentation models requires a domain expert (e.g., a radiologist) to manually annotate different objects of interest across a training dataset consisting of hundreds of patients, making it an extremely labor-intensive and time-consuming task [7,19,20]. As a result, most datasets and segmentation models developed in Figure 1. Example of SAM on (a) abdominal CT, (b) hand x-ray, and (c) knee MRI. SAM can operate in either "segment anything" mode (column 2), where SAM automatically segments all potential objects of interest in an image, or "prompting" mode, where SAM can segment an object of interest using an interactive prompt like bounding boxes (column 3) or points (column 4).

Medical image segmentation is one of the most fundamental tasks in computer-assisted clinical decision support, forming the basis for many downstream applications from diagnosis to treatment planning and response assessment. However, developing medical image segmentation models requires a domain expert (e.g., a radiologist) to manually annotate different objects of interest across a training dataset consisting of hundreds of patients, making it an extremely labor-intensive and time-consuming task [7,19,20]. As a result, most datasets and segmentation models developed in Figure 1. Example of SAM on (a) abdominal CT, (b) hand x-ray, and (c) knee MRI. SAM can operate in either "segment anything" mode (column 2), where SAM automatically segments all potential objects of interest in an image, or "prompting" mode, where SAM can segment an object of interest using an interactive prompt like bounding boxes (column 3) or points (column 4).