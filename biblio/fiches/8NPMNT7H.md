# TA-MedSAM: Text-augmented improved MedSAM for pulmonary lesion segmentation.



## Resume


TA-MedSAM: Text-augmented improved MedSAM for pulmonary lesion segmentation.

Accurate segmentation of lung lesions is critical for clinical diagnosis. Traditional methods rely solely on unimodal visual data, which limits the performance of existing medical image segmentation models. This paper introduces a novel approach, Text-Augmented Medical Segment Anything Module(TA-MedSAM), which enhances cross-modal representation capabilities through a vision-language fusion paradigm. This method significantly improves segmentation accuracy for pulmonary lesions with challenging characteristics including low contrast, blurred boundaries, complex morphology, and small size. Firstly, we introduce a lightweight Medical Segment Anything Model (MedSAM) image encoder and a pre-trained ClinicalBERT text encoder to extract visual and textual features, This design preserves segmentation performance while reducing model parameters and computational costs, thereby enhancing inference speed. Secondly, a Reconstruction Text Module is proposed to focus the model on lesion-centric tex

Corrigendum to “Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM)”

MedCLIP-SAM: Bridging Text and Image Towards Universal Medical Image Segmentation

U-MedSAM: Uncertainty-Aware MedSAM for Medical Image Segmentation

SAM & SAM 2 in 3D Slicer: SegmentWithSAM Extension for Annotating Medical Images

Rep-MedSAM: Towards Real-Time and Universal Medical Image Segmentation

Foundational Segmentation Models and Clinical Data Mining Enable Accurate Computer Vision for Lung Cancer.

This study aims to assess the effectiveness of integrating Segment Anything Model (SAM) and its variant MedSAM into the automated mining, object detection, and segmentation (MODS) methodology for developing robust lung cancer detection and segmentation models without post hoc labeling of training images. In a retrospective analysis, 10,000 chest computed tomography scans from patients with lung cancer were mined. Line measurement annotations were converted to bounding boxes, excluding boxes < 1 cm or > 7 cm. The You Only Look Once object detection architecture was used for teacher-student learning to label unannotated lesions on the training images. Subsequently, a final tumor detection model was trained and employed with SAM and MedSAM for tumor segmentation. Model performance was assessed on a manually annotated test dataset, with additional evaluations conducted on an external lung cancer dataset before and after detection model fine-tuning. Bootstrap resampling was used to calculat

Towards an automated Segment Anything Model (SAM) for lesion segmentation in oncological PET/CT images

PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation

Trans-SAM: Transfer Segment Anything Model to medical image segmentation with Parameter-Efficient Fine-Tuning

I-MedSAM: Implicit Medical Image Segmentation with Segment Anything

With the development of Deep Neural Networks (DNNs), many efforts have been made to handle medical image segmentation. Traditional methods such as nnUNet train specific segmentation models on the individual datasets. Plenty of recent methods have been proposed to adapt the foundational Segment Anything Model (SAM) to medical image segmentation. However, they still focus on discrete representations to generate pixel-wise predictions, which are spatially inflexible and scale poorly to higher resolution. In contrast, implicit methods learn continuous representations for segmentation, which is crucial for medical image segmentation. In this paper, we propose I-MedSAM, which leverages the benefits of both continuous representations and SAM, to obtain better cross-domain ability and accurate boundary delineation. Since medical image segmentation needs to predict detailed segmentation boundaries, we designed a novel adapter to enhance the SAM features with high-frequency information during Pa

Promptable segmentation of CT lung lesions based on improved U-Net and Segment Anything model (SAM).

BackgroundComputed tomography (CT) is widely used in clinical diagnosis of lung diseases. The automatic segmentation of lesions in CT images aids in the development of intelligent lung disease diagnosis.ObjectiveThis study aims to address the issue of imprecise segmentation in CT images due to the blurred detailed features of lesions, which can easily be confused with surrounding tissues.MethodsWe proposed a promptable segmentation method based on an improved U-Net and Segment Anything model (SAM) to improve segmentation accuracy of lung lesions in CT images. The improved U-Net incorporates a multi-scale attention module based on a channel attention mechanism ECA (Efficient Channel Attention) to improve recognition of detailed feature information at edge of lesions; and a promptable clipping module to incorporate physicians' prior knowledge into the model to reduce background interference. Segment Anything model (SAM) has a strong ability to recognize lesions and pulmonary atelectasis


## Insight


efficacy: MedSAM 2 apparaît comme le modèle le plus efficace pour la segmentation des tumeurs pulmonaires, combinant de meilleures performances de délimitation et un coût computationnel relativement faible par rapport aux architectures classiques et à MedSAM.

efficacy: MedSAM 2 a été identifié comme le modèle le plus efficace en termes de performance de segmentation et de coût computationnel, surpassant les modèles traditionnels pour la délimitation des tumeurs pulmonaires.

methodology: MedSAM, inspiré du Segment Anything Model, produit des segmentations médicales précises à partir d'annotations minimales et se distingue dans les scénarios complexes impliquant des formes organiques irrégulières, un faible contraste et des frontières anatomiques floues.

methodology: MedLSAM constitue un pipeline en deux étapes où MedLAM localise d'abord les structures anatomiques cibles dans des images médicales volumétriques, puis SAM ou MedSAM exploite les boîtes englobantes résultantes pour effectuer la segmentation.

methodology: La comparaison porte d’abord sur les performances globales de segmentation pulmonaire et tumorale, puis sur le coût computationnel et l’efficacité, avant d’examiner l’effet de la taille du jeu de données sur MedSAM 2.

methodology: MedSAM-2 traite les images médicales 3D et les flux d'images 2D comme des vidéos, s'appuyant sur un mécanisme de mémoire renforcée dérivé de SAM 2 pour la segmentation.


## Quote


we introduce I-MedSAM to enhance cross-domain ability and adaptability to diverse output resolutions in medical image segmentation

MedSAM demonstrates strong performance in challenging scenarios involving irregular organ shapes, low contrast, and blurred anatomical boundaries, making it a valuable tool for complex internal organ segmentation [10].

[Citation exacte indisponible.] Élément retenu : « Review of Application of SAM and Its Improved Models in Image Segmentation » ; « Étudier l’adaptation / le déploiement de SAM pour la segmentation médicale (dont cas type polyp segmentation) ».

Presented in Fig. 3 is a comparative visualization of lung segmentation masks, which displays chest X-ray images with three types of segmentation: initial MedSAM model predictions, refined outputs from the retrained HybridMS model, and expert-annotated ground truth masks.

MedLSAM is a two-stage pipeline: MedLAM localizes target structures within volumetric medical images, then SAM (or MedSAM) uses the resulting bounding boxes to perform segmentation.

Compared with previous fully-supervised segmentation models and SAM-based interactive models, MedSAM-2 demonstrated superior performance across all tested methods and achieved state-of-the-art results in both 2D and 3D medical image segmentation tasks.

MedSAM-2 is an advanced segmentation model based on SAM 2, treating all medical image segmentation tasks in 2D and 3D as a video object tracking problem


## Raw_Input


As shown in Table I, "SAM with post-process" and the fine-tuned SAM enhance the segmentation performance of the vanilla SAM. SAM2, when subjected to the same operations, will also improve segmentation performance. MedSAM2, which has been fine-tuned with a large number of medical images and masks, is expected to yield better results in the segmentation of pathological images. However, their performance is not very satisfactory, and they require a significant amount of manual prompt and post-processing work, with a high degree of human involvement and unstable performance.

As shown in Table I, "SAM with post-process" and the fine-tuned SAM enhance the segmentation performance of the vanilla SAM. SAM2, when subjected to the same operations, will also improve segmentation performance. MedSAM2, which has been fine-tuned with a large number of medical images and masks, is expected to yield better results in the segmentation of pathological images. However, their performance is not very satisfactory, and they require a significant amount of manual prompt and post-processing work, with a high degree of human involvement and unstable performance.


## Conclusion


EMedSAM surpasse les modèles état de l'art existants dans les tâches de segmentation multi-organes et de segmentation pulmonaire La combinaison de l'encodeur léger DD-TinyViT et du mécanisme med-adapter permet d'obtenir simultanément une meilleure efficacité (vitesse) et une meilleure précision de segmentation par rapport à SAM et MedSAM EMedSAM offre une généralisation robuste à travers diverses modalités d'imagerie médicale (CT, mammographie X-ray, IRM) et tâches de segmentation

Foundation models, particularly MedSAM 2, show strong potential for advancing lung tumor segmentation MedSAM 2 is a promising candidate for real-world medical imaging applications due to superior segmentation performance and relatively low computational cost Continued research, including automated prompt generation and evaluation on larger, more diverse datasets, could support integration into clinical workflows and improve diagnostic accuracy and patient outcomes


## Synthese


L'étude vise à développer un modèle de segmentation d'images médicales, ADA-SAM, capable de s'auto-prompter et de s'auto-corriger afin de réduire la dépendance aux grands ensembles de données annotées manuellement pour la segmentation des muscles quadriceps sur IRM.