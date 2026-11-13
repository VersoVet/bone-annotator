# ExpertsMedSAM: Faster Medical Image Segment Anything with Mixture-of-Experts



## Resume


ExpertsMedSAM: Faster Medical Image Segment Anything with Mixture-of-Experts

RepViT-MedSAM: Efficient Segment Anything in the Medical Images

SAM-Med3D-MoE: Towards a Non-Forgetting Segment Anything Model via Mixture of Experts for 3D Medical Image Segmentation

Rep-MedSAM: Towards Real-Time and Universal Medical Image Segmentation

Trans-SAM: Transfer Segment Anything Model to medical image segmentation with Parameter-Efficient Fine-Tuning

PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation

MedCLIP-SAM: Bridging Text and Image Towards Universal Medical Image Segmentation

U-MedSAM: Uncertainty-Aware MedSAM for Medical Image Segmentation

Segment Anything Model (SAM) for Medical Image Segmentation: A Preliminary Review

I-MedSAM: Implicit Medical Image Segmentation with Segment Anything

With the development of Deep Neural Networks (DNNs), many efforts have been made to handle medical image segmentation. Traditional methods such as nnUNet train specific segmentation models on the individual datasets. Plenty of recent methods have been proposed to adapt the foundational Segment Anything Model (SAM) to medical image segmentation. However, they still focus on discrete representations to generate pixel-wise predictions, which are spatially inflexible and scale poorly to higher resolution. In contrast, implicit methods learn continuous representations for segmentation, which is crucial for medical image segmentation. In this paper, we propose I-MedSAM, which leverages the benefits of both continuous representations and SAM, to obtain better cross-domain ability and accurate boundary delineation. Since medical image segmentation needs to predict detailed segmentation boundaries, we designed a novel adapter to enhance the SAM features with high-frequency information during Pa

How Segment Anything Model (Sam) Boost Medical Image Segmentation: A Survey

Human-Machine Collaboration for Medical Image Segmentation

Segment anything in medical images.

Medical image segmentation is a critical component in clinical practice, facilitating accurate diagnosis, treatment planning, and disease monitoring. However, existing methods, often tailored to specific modalities or disease types, lack generalizability across the diverse spectrum of medical image segmentation tasks. Here we present MedSAM, a foundation model designed for bridging this gap by enabling universal medical image segmentation. The model is developed on a large-scale medical image dataset with 1,570,263 image-mask pairs, covering 10 imaging modalities and over 30 cancer types. We conduct a comprehensive evaluation on 86 internal validation tasks and 60 external validation tasks, demonstrating better accuracy and robustness than modality-wise specialist models. By delivering accurate and efficient segmentation across a wide spectrum of tasks, MedSAM holds significant potential to expedite the evolution of diagnostic tools and the personalization of treatment plans.

A review of the Segment Anything Model (SAM) for medical image analysis: Accomplishments and perspectives

MedSAM2: Segment Anything in 3D Medical Images and Videos

Medical image and video segmentation is a critical task for precision medicine, which has witnessed considerable progress in developing task or modality-specific and generalist models for 2D images. However, there have been limited studies on building general-purpose models for 3D images and videos with comprehensive user studies. Here, we present MedSAM2, a promptable segmentation foundation model for 3D image and video segmentation. The model is developed by fine-tuning the Segment Anything Model 2 on a large medical dataset with over 455,000 3D image-mask pairs and 76,000 frames, outperforming previous models across a wide range of organs, lesions, and imaging modalities. Furthermore, we implement a human-in-the-loop pipeline to facilitate the creation of large-scale datasets resulting in, to the best of our knowledge, the most extensive user study to date, involving the annotation of 5,000 CT lesions, 3,984 liver MRI lesions, and 251,550 echocardiogram video frames, demonstrating t

SAM & SAM 2 in 3D Slicer: SegmentWithSAM Extension for Annotating Medical Images

Gray’s Anatomy for Segment Anything Model: Optimizing Grayscale Medical Images for Fast and Lightweight Segmentation

Segment Anything in Medical Images with nnUNet

Efficient Medical Segmentation Anything Model for Robust Lightweight Segmentation under Imperfect Data in Embedded Healthcare.

Healthcare Industry 5.0 is accelerating the deployment of medical imaging intelligence on embedded and edge devices, where medical data are often imperfect due to acquisition noise, low-contrast regions, and boundary ambiguity, while computational budgets remain tight. Although the Segment Anything Model (SAM) provides promptable segmentation, its heavy encoder hinders edge deployment and its zero-shot behavior can be unreliable for specialized medical imaging scenarios. This paper presents an efficient and lightweight medical image segmentation pipeline tailored for embedded healthcare systems. We replace the SAM image encoder with an Efficient Vision Transformer (EfficientViT) backbone and introduce offline knowledge distillation to transfer domain-aware feature representations from the Medical Segment Anything Model (MedSAM) to a compact student network. To emulate imperfect supervision in practical use, bounding-box prompts are generated from ground truth masks with random per-side

Medical Image Segmentation with Efficient Use of Annotations and Resources

The Role of Segment Anything Model (SAM) In Medical Image Segmentation: A Comprehensive Review

SwiftMedSAM: An Ultra-lightweight Prompt-Based Universal Medical Image Segmentation Model for Highly Constrained Environments

Research on Medical Image Segmentation Based on SAM and Its Future Prospects.

The rapid advancement of prompt-based models in natural language processing and image generation has revolutionized the field of image segmentation. The introduction of the Segment Anything Model (SAM) has further invigorated this domain with its unprecedented versatility. However, its applicability to medical image segmentation remains uncertain due to significant disparities between natural and medical images, which demand careful consideration. This study comprehensively analyzes recent efforts to adapt SAM for medical image segmentation, including empirical benchmarking and methodological refinements aimed at bridging the gap between SAM's capabilities and the unique challenges of medical imaging. Furthermore, we explore future directions for SAM in this field. While direct application of SAM to complex, multimodal, and multi-target medical datasets may not yet yield optimal results, insights from these efforts provide crucial guidance for developing foundational models tailored to

Accelerating vision foundation model for efficient medical image segmentation.

<h4>Background</h4>Segment anything model (SAM) has recently demonstrated tremendous potential in the artificial intelligence-based medical image segmentation. However, its outstanding performance is always accompanied by surging computation costs due to the extremely long patch sequences and their quadratic complexity in vision transformer, which hamper the development of real-time engineering applications.<h4>Purpose</h4>This work aims to accelerate SAM for medical image segmentation with better segmentation quality and less memory usage.<h4>Methods</h4>Instead of upscaling training images to larger resolutions to match the pre-trained SAM's input size, which may introduce image distortions, we propose a convolutional neural network (CNN)-assisted tuning strategy. This approach enables SAM to process smaller inputs directly, significantly reducing the number of patches and memory consumption. Moreover, based on the observation that the less-informative patches in medical images tend

ST-SAM: A Spatio-Temporal Enhanced Segment Anything Model for Echocardiogram Video Segmentation


## Quote


we introduce I-MedSAM to enhance cross-domain ability and adaptability to diverse output resolutions in medical image segmentation


## Raw_Introduction


The Segment Anything Model (SAM) [13], since its introduction, has drawn tremendous attention and effort in the field of medical image analysis. Image segmentation plays a critical role in medical AI systems, and there is a great potential in applying large vision models such as SAM to medical images. Pioneering medical AI studies have proposed (1) training a medical SAM [17,7], or (2) finetuning and/or adapting SAM for downstream medical image segmentation tasks [25,26]. Training a medical SAM requires acquiring a large volume of labeled medical images. There exist practical challenges in building SAM for medical image data, including variations in modalities (e.g., CT, MRI, Ultrasound), subjects (e.g., organs, tissues, cells), scales, annotation quality, and tasks. On the other hand, fine-tuning and/or adapting a general-purpose SAM to a particular medical image segmentation task, although a reasonable approach, can lead to the possibility of SAM losing its generalization capability

The Segment Anything Model (SAM) [13], since its introduction, has drawn tremendous attention and effort in the field of medical image analysis. Image segmentation plays a critical role in medical AI systems, and there is a great potential in applying large vision models such as SAM to medical images. Pioneering medical AI studies have proposed (1) training a medical SAM [17,7], or (2) finetuning and/or adapting SAM for downstream medical image segmentation tasks [25,26]. Training a medical SAM requires acquiring a large volume of labeled medical images. There exist practical challenges in building SAM for medical image data, including variations in modalities (e.g., CT, MRI, Ultrasound), subjects (e.g., organs, tissues, cells), scales, annotation quality, and tasks. On the other hand, fine-tuning and/or adapting a general-purpose SAM to a particular medical image segmentation task, although a reasonable approach, can lead to the possibility of SAM losing its generalization capability


## Raw_Conclusion


The practice of human experts rectifying AI-generated segmentation predictions is not uncommon in medical AI applications. This paper introduced a novel and practical method for enhancing the Segment Anything Model (SAM) for medical image segmentation. Rather than investing resources in time-consuming and energy-intensive offline fine-tuning, adaptation, or retraining of SAM for medical images, we advocated leveraging valuable feedback from human experts and harnessing the benefits of online learning for test-time improvement of Segment Anything (SA) in medical imaging scenes. Our proposed Auxiliary Online Learning (AuxOL) method is both effective and efficient. It eliminates the need for extensive tuning of SAM, offering potential utility across various downstream segmentation tasks. By capitalizing on human expertise and the adaptability of online learning, our method presents a promising avenue for advancing SAM-based medical image segmentation.

The practice of human experts rectifying AI-generated segmentation predictions is not uncommon in medical AI applications. This paper introduced a novel and practical method for enhancing the Segment Anything Model (SAM) for medical image segmentation. Rather than investing resources in time-consuming and energy-intensive offline fine-tuning, adaptation, or retraining of SAM for medical images, we advocated leveraging valuable feedback from human experts and harnessing the benefits of online learning for test-time improvement of Segment Anything (SA) in medical imaging scenes. Our proposed Auxiliary Online Learning (AuxOL) method is both effective and efficient. It eliminates the need for extensive tuning of SAM, offering potential utility across various downstream segmentation tasks. By capitalizing on human expertise and the adaptability of online learning, our method presents a promising avenue for advancing SAM-based medical image segmentation.