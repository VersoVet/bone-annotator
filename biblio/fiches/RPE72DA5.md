# Corrigendum to “Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM)”



## Resume


Corrigendum to “Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM)”

Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM).

BackgroundComputed tomography (CT) is widely used in clinical diagnosis of lung diseases. The automatic segmentation of lesions in CT images aids in the development of intelligent lung disease diagnosis.ObjectiveThis study aims to address the issue of imprecise segmentation in CT images due to the blurred detailed features of lesions, which can easily be confused with surrounding tissues.MethodsWe proposed a promptable segmentation method based on an improved U-Net and Segment Anything model (SAM) to improve segmentation accuracy of lung lesions in CT images. The improved U-Net incorporates a multi-scale attention module based on a channel attention mechanism ECA (Efficient Channel Attention) to improve recognition of detailed feature information at edge of lesions; and a promptable clipping module to incorporate physicians' prior knowledge into the model to reduce background interference. Segment Anything model (SAM) has a strong ability to recognize lesions and pulmonary atelectasis

Towards an automated Segment Anything Model (SAM) for lesion segmentation in oncological PET/CT images

Tumor-SAM: segment anything model for semi-automatic lung tumor segmentation in CT

Lung segment anything model (LuSAM): a decoupled prompt-integrated framework for automated lung segmentation on chest x-Ray images.

Accurate lung segmentation in chest x-ray images plays a pivotal role in early disease detection and clinical decision-making. In this study, we introduce an innovative approach to enhance the precision of lung segmentation using the Segment Anything Model (SAM). Despite its versatility, SAM faces the challenge of prompt decoupling, often resulting in misclassifications, especially with intricate structures like the clavicle. Our research focuses on the integration of spatial attention mechanisms within SAM. This approach enables the model to concentrate specifically on the lung region, fostering adaptability to image variations and reducing the likelihood of false positives. This work has the potential to significantly advance lung segmentation, improving the identification and quantification of lung anomalies across diverse clinical contexts.

Segment Anything Model (SAM) for Medical Image Segmentation: A Preliminary Review

PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation

TA-MedSAM: Text-augmented improved MedSAM for pulmonary lesion segmentation.

Accurate segmentation of lung lesions is critical for clinical diagnosis. Traditional methods rely solely on unimodal visual data, which limits the performance of existing medical image segmentation models. This paper introduces a novel approach, Text-Augmented Medical Segment Anything Module(TA-MedSAM), which enhances cross-modal representation capabilities through a vision-language fusion paradigm. This method significantly improves segmentation accuracy for pulmonary lesions with challenging characteristics including low contrast, blurred boundaries, complex morphology, and small size. Firstly, we introduce a lightweight Medical Segment Anything Model (MedSAM) image encoder and a pre-trained ClinicalBERT text encoder to extract visual and textual features, This design preserves segmentation performance while reducing model parameters and computational costs, thereby enhancing inference speed. Secondly, a Reconstruction Text Module is proposed to focus the model on lesion-centric tex

Automated Lesion Segmentation in Medical Imaging via Integration of nnU-Net Optimization and SAM Approach.

<h4>Background</h4>Deep learning has transformed medical imaging by enabling earlier and more accurate disease diagnosis. Lesion and tumor segmentation, essential for analyzing and tracking morphological changes, is commonly done with U-Net variants, though these often lack cross-domain generalization and do not fully leverage foundation models like the Segment Anything Model (SAM), which still requires manual intervention to define the region of interest (ROI).<h4>Objectives</h4>To enhance generalization and reduce manual intervention by combining the automatic optimization of nnU-Net with the precision of SAM.<h4>Design</h4>Experimental evaluation of a hybrid segmentation framework for lung nodule analysis.<h4>Methods</h4>We propose a novel approach integrating the automatic optimization capabilities of nnU-Net for lesion detection with the high-precision segmentation of SAM, eliminating the need for manual intervention by the clinician. The method was evaluated on the LIDC-IDRI data

How Segment Anything Model (Sam) Boost Medical Image Segmentation: A Survey

Enhancing lung segmentation in chest X-rays via SAM with anatomical priors and boundary-aware loss.

Accurate lung segmentation in chest X-rays is a foundational step for computer-aided diagnosis of respiratory diseases such as pneumonia, tuberculosis, and lung cancer. While the Segment Anything Model (SAM) has demonstrated remarkable zero-shot segmentation capabilities on natural images, its direct application to medical imaging remains limited due to domain shift, low contrast, and ambiguous anatomical boundaries. To address these challenges, we propose a lightweight yet effective adaptation of SAM that integrates (i) a Mask Autoencoder (MAE) as an anatomical prior to enforce global shape consistency, and (ii) a composite loss function combining Binary Cross-Entropy (BCE), Dice, and Boundary losses to jointly optimize pixel-level accuracy, region overlap, and edge fidelity. Our parameter-efficient fine-tuning strategy trains only 0.3% of SAM's parameters, specifically the mask decoder, while freezing the image and prompt encoders. Evaluated on the MedSeg Chest X-ray Lung Dataset, ou

ST-SAM: A Spatio-Temporal Enhanced Segment Anything Model for Echocardiogram Video Segmentation

StructSAM: structure-aware prompt adaptation for robust lung cancer lesion segmentation in CT.

Accurate delineation of lung lesions in computed tomography (CT) scans is critical for diagnosis, staging, and treatment planning, yet remains a challenging task. While foundation models like the Segment Anything Model (SAM) excel in natural images, they often falter in medical imaging due to low contrast, ambiguous boundaries, and a lack of 3D context. To address these limitations, we propose StructSAM, a structure-aware prompt adaptation framework designed for robust volumetric segmentation, with a primary focus on lung cancer. StructSAM injects anatomical priors into the prompt pathway, employs a 3D inter-slice aggregator for volumetric consistency, and leverages PEFT for scalability. Experiments on the LIDC-IDRI dataset demonstrate that StructSAM achieves state-of-the-art accuracy on lung nodule segmentation, outperforming both classical architectures and SAM-based adaptations. Crucially, extended cross-organ evaluations on KiTS19 and MSD Pancreas datasets reveal that StructSAM eff

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

A review of the Segment Anything Model (SAM) for medical image analysis: Accomplishments and perspectives

Trans-SAM: Transfer Segment Anything Model to medical image segmentation with Parameter-Efficient Fine-Tuning

Zero-shot swift lung 4D CT segmentation via optimized Segment Anything Model

Enhancing the Reliability of Segment Anything Model for Auto-Prompting Medical Image Segmentation with Uncertainty Rectification

The Segment Anything Model (SAM) has recently emerged as a groundbreaking foundation model for prompt-driven image segmentation tasks. However, both the original SAM and its medical variants require slice-by-slice manual prompting of target structures, which directly increase the burden for applications. Despite attempts of auto-prompting to turn SAM into a fully automatic manner, it still exhibits subpar performance and lacks of reliability especially in the field of medical imaging. In this paper, we propose UR-SAM, an uncertainty rectified SAM framework to enhance the reliability for auto-prompting medical image segmentation. Building upon a localization framework for automatic prompt generation, our method incorporates a prompt augmentation module to obtain a series of input prompts for SAM for uncertainty estimation and an uncertainty-based rectification module to further utilize the distribution of estimated uncertainty to improve the segmentation performance. Extensive experimen

Evaluating the efficacy of the Segment Anything Model (SAM) in streamlining dental cyst segmentation within CBCT volumes

Towards a general computed tomography image segmentation model for anatomical structures and lesions

SAM-guided Cross Pseudo Supervision Learning for Semi-supervised Medical Image Segmentation.

Precise identification of lesions in medical images is crucial for accurate diagnosis and successful treatment. Nevertheless, the limited availability of annotations, coupled with the intricate nature of lesion characteristics, imposes significant constraints on the model's representational capacity. The recently developed vision foundation model, Segment Anything Model (SAM), featuring its unique capability for prompt interaction, has demonstrated remarkable capabilities in natural image segmentation. However, it encounters performance degradation in medical scenarios due to the absence of domain-specific medical knowledge. To address the aforementioned issues, we propose a novel SAM-assisted semi-supervised framework for accurate lesion segmentation, even in scenarios with extremely limited annotations. Concretely, our approach adopts a dual-branch architecture, where each branch incorporates a SAM (ViT-Base) model fine-tuned with adapters. We further design a point prompts generator

Fine-Tuned Segment Anything Model with Low-Rank Adaptation for Chest X-Ray Images.

<b>Background:</b> This paper investigates the use of the Segment Anything Model (SAM) for chest X-ray (CXR) image segmentation, with a focus on improving its performance using low-rank adaptation (LoRA). <b>Methods:</b> We evaluate three versions of SAM: two zero-shot methods (using coordinate and bounding box prompts) and a fine-tuned SAM using LoRA. To support these approaches, we also trained two standard convolutional neural networks (CNNs), U-Net and DeepLabv3+, to generate draft lung segmentations that serve as input prompts for the SAM methods. Our fine-tuning approach uses LoRA to add lightweight trainable adapters within the Transformer blocks of the SAM, allowing only a small subset of parameters to be updated. The rest of the SAM remains frozen, helping preserve its pre-trained knowledge while reducing memory and computational needs. We tested all models on a dataset of CXR images labeled for COVID-19, viral pneumonia, and normal cases. <b>Results:</b> Results show that fin

LeSAM: Adapt Segment Anything Model for Medical Lesion Segmentation.

The Segment Anything Model (SAM) is a foundational model that has demonstrated impressive results in the field of natural image segmentation. However, its performance remains suboptimal for medical image segmentation, particularly when delineating lesions with irregular shapes and low contrast. This can be attributed to the significant domain gap between medical images and natural images on which SAM was originally trained. In this paper, we propose an adaptation of SAM specifically tailored for lesion segmentation termed LeSAM. LeSAM first learns medical-specific domain knowledge through an efficient adaptation module and integrates it with the general knowledge obtained from the pre-trained SAM. Subsequently, we leverage this merged knowledge to generate lesion masks using a modified mask decoder implemented as a lightweight U-shaped network design. This modification enables better delineation of lesion boundaries while facilitating ease of training. We conduct comprehensive experime

Foundational Segmentation Models and Clinical Data Mining Enable Accurate Computer Vision for Lung Cancer.

This study aims to assess the effectiveness of integrating Segment Anything Model (SAM) and its variant MedSAM into the automated mining, object detection, and segmentation (MODS) methodology for developing robust lung cancer detection and segmentation models without post hoc labeling of training images. In a retrospective analysis, 10,000 chest computed tomography scans from patients with lung cancer were mined. Line measurement annotations were converted to bounding boxes, excluding boxes < 1 cm or > 7 cm. The You Only Look Once object detection architecture was used for teacher-student learning to label unannotated lesions on the training images. Subsequently, a final tumor detection model was trained and employed with SAM and MedSAM for tumor segmentation. Model performance was assessed on a manually annotated test dataset, with additional evaluations conducted on an external lung cancer dataset before and after detection model fine-tuning. Bootstrap resampling was used to calculat

The Role of Segment Anything Model (SAM) In Medical Image Segmentation: A Comprehensive Review

RepViT-MedSAM: Efficient Segment Anything in the Medical Images


## Raw_Introduction


• We present UR-SAM, an Uncertainty Rectified Segment Anything Model by incorporating uncertainty estimation and rectification to enhance the robustness and reliability for auto-prompting medical image segmentation. • We propose to augment given prompts by adding perturbations with pre-defined ratios to estimate segmentation uncertainty based on the predictions of multi-prompt input, since the segmentation performance of SAM is sensitive to the input prompt. • We propose to utilize estimated segmentation uncertainty with class-specific confidence-based filtering to select out high uncertain regions for rectification to further improve the segmentation performance.

• We present UR-SAM, an Uncertainty Rectified Segment Anything Model by incorporating uncertainty estimation and rectification to enhance the robustness and reliability for auto-prompting medical image segmentation. • We propose to augment given prompts by adding perturbations with pre-defined ratios to estimate segmentation uncertainty based on the predictions of multi-prompt input, since the segmentation performance of SAM is sensitive to the input prompt. • We propose to utilize estimated segmentation uncertainty with class-specific confidence-based filtering to select out high uncertain regions for rectification to further improve the segmentation performance.


## Quote


[Citation exacte indisponible.] Élément retenu : « Review of Application of SAM and Its Improved Models in Image Segmentation » ; « Étudier l’adaptation / le déploiement de SAM pour la segmentation médicale (dont cas type polyp segmentation) ».