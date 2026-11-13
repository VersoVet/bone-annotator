# Reducing Annotation Effort by Identifying and Labeling Contextually Diverse Classes for Semantic Segmentation Under Domain Shift



## Resume


Reducing Annotation Effort by Identifying and Labeling Contextually Diverse Classes for Semantic Segmentation Under Domain Shift

Semantic segmentation with less annotation efforts

Supervised Learning of Semantic Classes for Image Annotation and Retrieval

Region-based Active Learning for Reducing Annotation Effort of ECG Waveform Segmentation

Semantic Image Segmentation Annotation Refinement Using SAM

Learning class-agnostic masks with cross-task refinement for weakly supervised semantic segmentation

AbstractWeakly supervised semantic segmentation (WSSS) commonly relies on Class Activation Mapping (CAM) to produce pseudo semantic labels using image-level annotations. However, because CAM maps often form sparse object regions with poor boundaries, they cannot provide sufficient segmentation supervision. Because off-the-shelf saliency maps can provide rich object boundaries that can be leveraged to improve semantic segmentation, we propose to jointly learn semantic segmentation and class-agnostic masks by using image-level annotations and off-the-shelf saliency maps as supervision. We also propose a cross-task label refinement mechanism, which takes advantage of the learned class-agnostic masks and semantic segmentation masks, to refine the pseudo labels and provide more accurate supervision to both tasks. Moreover, we introduce a new normalization method for CAM to generate more complete class-specific localization maps. The improved CAM maps complement our learned class-agnostic masks, leading to high-quality pseudo semantic segmentation labels. Extensive experiments demonstrate the effectiveness of the proposed approach, with state-of-the-art WSSS results established on PASCAL VOC 2012 and MS COCO.

Context Aware Image Annotation in Active Learning with Batch Mode

Simultaneous Segmentation and Anatomical Landmark Detection on 3D Data using Context-aware Multi-task Learning

Reducing Reliance on Expensive Annotations in Medical Image Segmentation Via Diffusion Models and Segment Anything Model

Image Segmentation and Labeling Using Free-Form Semantic Annotation

Learning to segment images with classification labels.

Two of the most common tasks in medical imaging are classification and segmentation. Either task requires labeled data annotated by experts, which is scarce and expensive to collect. Annotating data for segmentation is generally considered to be more laborious as the annotator has to draw around the boundaries of regions of interest, as opposed to assigning image patches a class label. Furthermore, in tasks such as breast cancer histopathology, any realistic clinical application often includes working with whole slide images, whereas most publicly available training data are in the form of image patches, which are given a class label. We propose an architecture that can alleviate the requirements for segmentation-level ground truth by making use of image-level labels to reduce the amount of time spent on data curation. In addition, this architecture can help unlock the potential of previously acquired image-level datasets on segmentation tasks by annotating a small number of regions of

Reducing annotation effort in digital pathology: A Co-Representation learning framework for classification tasks

Towards weakly supervised semantic segmentation by means of multiple instance and multitask learning

Revisiting Superpixels for Active Learning in Semantic Segmentation with Realistic Annotation Costs

Iterative Loop Method Combining Active and Semi-Supervised Learning for Domain Adaptive Semantic Segmentation

Learning with Limited Annotations: A Survey on Deep Semi-Supervised Learning for Medical Image Segmentation

Spannotation: Enhancing Semantic Segmentation for Autonomous Navigation with Efficient Image Annotation

Spannotation is an open source user-friendly tool developed for image annotation for semantic segmentation specifically in autonomous navigation tasks. This study provides an evaluation of Spannotation, demonstrating its effectiveness in generating accurate segmentation masks for various environments like agricultural crop rows, off-road terrains and urban roads. Unlike other popular annotation tools that requires about 40 seconds to annotate an image for semantic segmentation in a typical navigation task, Spannotation achieves similar result in about 6.03 seconds. The tools utility was validated through the utilization of its generated masks to train a U-Net model which achieved a validation accuracy of 98.27% and mean Intersection Over Union (mIOU) of 96.66%. The accessibility, simple annotation process and no-cost features have all contributed to the adoption of Spannotation evident from its download count of 2098 (as of February 25, 2024) since its launch. Future enhancements of Sp

Learning Weakly Supervised Semantic Segmentation Through Cross-Supervision and Contrasting of Pixel-Level Pseudo-Labels


## Raw_Introduction


The role of data annotation in semantic segmentation extends beyond mere labelling; it is the foundation for model training, especially in vision-based navigation systems. The importance of semantic segmentation in navigation is underscored by its ability to accurately differentiate between drivable and non-drivable regions. Several research utilized semantic segmentation for different navigation tasks showing its importance and the need for quality data annotation in this area of research. Readers are refereed to works that utilized semantic segmentation for autonomous navigation in on-road [21]- [23], off-road [21], [23], [24], indoor [25]- [28], farm-terrains [29], [30]. The limitations of current annotation methods and tools act as a bottleneck in the development and implementation of effective autonomous navigation systems.

The role of data annotation in semantic segmentation extends beyond mere labelling; it is the foundation for model training, especially in vision-based navigation systems. The importance of semantic segmentation in navigation is underscored by its ability to accurately differentiate between drivable and non-drivable regions. Several research utilized semantic segmentation for different navigation tasks showing its importance and the need for quality data annotation in this area of research. Readers are refereed to works that utilized semantic segmentation for autonomous navigation in on-road [21]- [23], off-road [21], [23], [24], indoor [25]- [28], farm-terrains [29], [30]. The limitations of current annotation methods and tools act as a bottleneck in the development and implementation of effective autonomous navigation systems.

Recently, there have been application of the use of neural network based approach for enhanced accuracy and efficiency in data annotation [17]- [20] for semantic segmentation and other purposes. Despite their advantages, these methods usually require some level of technical know-how, relatively high computational costs for developers and possibly cost for usage. Spannotation addresses these limitations by offering a simpler, yet efficient alternative for scenarios where intricate machine learning solutions may be impractical.

Recently, there have been application of the use of neural network based approach for enhanced accuracy and efficiency in data annotation [17]- [20] for semantic segmentation and other purposes. Despite their advantages, these methods usually require some level of technical know-how, relatively high computational costs for developers and possibly cost for usage. Spannotation addresses these limitations by offering a simpler, yet efficient alternative for scenarios where intricate machine learning solutions may be impractical.

In response to these challenges, 'Spannotation' [31] is introduced as an innovative algorithm designed to transform the annotation process for semantic segmentation in navigation tasks. Tailored specifically for binary segmentation, Spannotation excels at distinguishing between drivable and non-drivable regions across diverse environments, including off-road terrains, crop rows for small robots, and standard onroad scenarios. Its key advantages include being fast, easy to use, free, and requiring no technical know-how, making it an ideal tool for a wide range of users. This paper is structured to offer a comprehensive insight into Spannotation and its applications in semantic segmentation for vision-based navigation. Section [II] spells out the technical aspects and innovative approaches employed in Spannotation. In the Results section [III], the algorithm's efficacy is shown through various test cases and comparisons with existing tools. The ensuing Discussion delves into the implicat

In response to these challenges, 'Spannotation' [31] is introduced as an innovative algorithm designed to transform the annotation process for semantic segmentation in navigation tasks. Tailored specifically for binary segmentation, Spannotation excels at distinguishing between drivable and non-drivable regions across diverse environments, including off-road terrains, crop rows for small robots, and standard onroad scenarios. Its key advantages include being fast, easy to use, free, and requiring no technical know-how, making it an ideal tool for a wide range of users. This paper is structured to offer a comprehensive insight into Spannotation and its applications in semantic segmentation for vision-based navigation. Section [II] spells out the technical aspects and innovative approaches employed in Spannotation. In the Results section [III], the algorithm's efficacy is shown through various test cases and comparisons with existing tools. The ensuing Discussion delves into the implicat

To mitigate the annotation burden associated with traditional deep learning segmentation, few-shot segmentation has emerged as a promising paradigm. This approach lever-ages meta-learning principles to learn transferable knowledge from a set of base classes, enabling the model to rapidly adapt to unseen target classes with limited supervision. Typically, these methods involve a support set containing a few labeled examples of the target class, and a query image to be segmented. The model then utilizes the information from the support set to perform accurate segmentation on the query image. However, as Fig. 1 shows, most existing few-shot segmentation techniques still necessitate extensive labeled datasets for meta-training, indicating a substantial room for further improvement in reducing reliance on large-scale annotations.


## Quote


We also made use of the external dataset for geometric context estimation to further regularize our solution. By this we demonstrated that the amount of supervision required to learn a semantic segmentation classifier can be significantly reduced.

The role of data annotation in semantic segmentation extends beyond mere labelling; it is the foundation for model training, especially in vision-based navigation systems.

The role of data annotation in semantic segmentation extends beyond mere labelling; it is the foundation for model training, especially in vision-based navigation systems.

The proposed framework reduces the labeling effort by (i) utilizing spatial estimates about annotation costs inferred from a learned cost prediction CNN and (ii) by focusing on image regions promising high information content and low annotation costs in a global context.


## Raw_Full_Text


sur le ratio moyen de déséquilibre). 1
ABSTRACT
Rebalancing Label Distribution while Eliminating Inherent Waiting Time in Multi Label Active
Learning applied to Transformers.
Data annotation is crucial for machine learning, notably in technical domains, where the quality and
quantity of annotated data, significantly affect effectiveness of trained models. Employing humans
is costly, especially when annotating for multi-label classification, as instances may bear multiple
labels. Active Learning (AL) aims to alleviate annotation costs by intelligently selecting instances for
annotation, rather than randomly annotating. Recent attention on transformers has spotlighted the
potential of AL in this context. However, in practical settings, implementing AL faces challenges
beyond theory. Notably, the gap between AL cycles presents idle time for annotators. To address this
issue, we investigate alternative instance selection methods, aiming to maximize annotation efficiency
by seamlessly integ