# Multi-Faceted Consistency learning with active cross-labeling for barely-supervised 3D medical image segmentation.



## Resume


Multi-Faceted Consistency learning with active cross-labeling for barely-supervised 3D medical image segmentation.

Deep learning-driven 3D medical image segmentation generally necessitates dense voxel-wise annotations, which are expensive and labor-intensive to acquire. Cross-annotation, which labels only a few orthogonal slices per scan, has recently emerged as a cost-effective alternative that better preserves the shape and precise boundaries of the 3D object than traditional weak labeling methods such as bounding boxes and scribbles. However, learning from such sparse labels, referred to as barely-supervised learning (BSL), remains challenging due to less fine-grained object perception, less compact class features and inferior generalizability. To tackle these challenges and foster collaboration between model training and human expertise, we propose a Multi-Faceted ConSistency learning (MF-ConS) framework with a Diversity and Uncertainty Sampling-based Active Learning (DUS-AL) strategy, specifically designed for the active BSL scenario. This framework combines a cross-annotation BSL strategy, wh

Few Slices Suffice: Multi-faceted Consistency Learning with Active Cross-Annotation for Barely-Supervised 3D Medical Image Segmentation

Mtcl: Multi-Task Consistency Learning for Semi-Supervised 3d Medical Image Segmentation

Learning with Limited Annotations: A Survey on Deep Semi-Supervised Learning for Medical Image Segmentation

BoostMIS: Boosting Medical Image Semi-supervised Learning with Adaptive Pseudo Labeling and Informative Active Annotation

Active learning for medical image segmentation with stochastic batches.

The performance of learning-based algorithms improves with the amount of labelled data used for training. Yet, manually annotating data is particularly difficult for medical image segmentation tasks because of the limited expert availability and intensive manual effort required. To reduce manual labelling, active learning (AL) targets the most informative samples from the unlabelled set to annotate and add to the labelled training set. On the one hand, most active learning works have focused on the classification or limited segmentation of natural images, despite active learning being highly desirable in the difficult task of medical image segmentation. On the other hand, uncertainty-based AL approaches notoriously offer sub-optimal batch-query strategies, while diversity-based methods tend to be computationally expensive. Over and above methodological hurdles, random sampling has proven an extremely difficult baseline to outperform when varying learning and sampling conditions. This w

COLosSAL: A Benchmark for Cold-start Active Learning for 3D Medical Image Segmentation

Medical image segmentation is a critical task in medical image analysis. In recent years, deep learning based approaches have shown exceptional performance when trained on a fully-annotated dataset. However, data annotation is often a significant bottleneck, especially for 3D medical images. Active learning (AL) is a promising solution for efficient annotation but requires an initial set of labeled samples to start active selection. When the entire data pool is unlabeled, how do we select the samples to annotate as our initial set? This is also known as the cold-start AL, which permits only one chance to request annotations from experts without access to previously annotated data. Cold-start AL is highly relevant in many practical scenarios but has been under-explored, especially for 3D medical segmentation tasks requiring substantial annotation effort. In this paper, we present a benchmark named COLosSAL by evaluating six cold-start AL strategies on five 3D medical image segmentation

Unsupervised Segmentation of 3D Medical Images Based on Clustering and Deep Representation Learning

Annotation noise-aware semi-supervised and domain adaptive learning for 3D medical imaging

Learning Weakly Supervised Semantic Segmentation Through Cross-Supervision and Contrasting of Pixel-Level Pseudo-Labels

Adaptive Annotation Correlation Based Multi-Annotation Learning for Calibrated Medical Image Segmentation

Multi-granularity learning of explicit geometric constraint and contrast for label-efficient medical image segmentation and differentiable clinical function assessment

Cross Prompting Consistency with Segment Anything Model for Semi-supervised Medical Image Segmentation

Semi-supervised learning (SSL) has achieved notable progress in medical image segmentation. To achieve effective SSL, a model needs to be able to efficiently learn from limited labeled data and effectively exploiting knowledge from abundant unlabeled data. Recent developments in visual foundation models, such as the Segment Anything Model (SAM), have demonstrated remarkable adaptability with improved sample efficiency. To harness the power of foundation models for application in SSL, we propose a cross prompting consistency method with segment anything model (CPC-SAM) for semi-supervised medical image segmentation. Our method employs SAM's unique prompt design and innovates a cross-prompting strategy within a dual-branch framework to automatically generate prompts and supervisions across two decoder branches, enabling effectively learning from both scarce labeled and valuable unlabeled data. We further design a novel prompt consistency regularization, to reduce the prompt position sens

An Annotation Sparsification Strategy for 3D Medical Image Segmentation via Representative Selection and Self-Training

Image segmentation is critical to lots of medical applications. While deep learning (DL) methods continue to improve performance for many medical image segmentation tasks, data annotation is a big bottleneck to DL-based segmentation because (1) DL models tend to need a large amount of labeled data to train, and (2) it is highly time-consuming and label-intensive to voxel-wise label 3D medical images. Significantly reducing annotation effort while attaining good performance of DL segmentation models remains a major challenge. In our preliminary experiments, we observe that, using partially labeled datasets, there is indeed a large performance gap with respect to using fully annotated training datasets. In this paper, we propose a new DL framework for reducing annotation effort and bridging the gap between full annotation and sparse annotation in 3D medical image segmentation. We achieve this by (i) selecting representative slices in 3D images that minimize data redundancy and save annotation effort, and (ii) self-training with pseudo-labels automatically generated from the base-models trained using the selected annotated slices. Extensive experiments using two public datasets (the HVSMR 2016 Challenge dataset and mouse piriform cortex dataset) show that our framework yields competitive segmentation results comparing with state-of-the-art DL methods using less than ∼20% of annotated data.

Label-driven weakly-supervised learning for multimodal deformable image registration

Spatially aligning medical images from different modalities remains a challenging task, especially for intraoperative applications that require fast and robust algorithms. We propose a weakly-supervised, label-driven formulation for learning 3D voxel correspondence from higher-level label correspondence, thereby bypassing classical intensity-based image similarity measures. During training, a convolutional neural network is optimised by outputting a dense displacement field (DDF) that warps a set of available anatomical labels from the moving image to match their corresponding counterparts in the fixed image. These label pairs, including solid organs, ducts, vessels, point landmarks and other ad hoc structures, are only required at training time and can be spatially aligned by minimising a cross-entropy function of the warped moving label and the fixed label. During inference, the trained network takes a new image pair to predict an optimal DDF, resulting in a fully-automatic, label-fr

Scalable histopathological image analysis via active learning.

Training an effective and scalable system for medical image analysis usually requires a large amount of labeled data, which incurs a tremendous annotation burden for pathologists. Recent progress in active learning can alleviate this issue, leading to a great reduction on the labeling cost without sacrificing the predicting accuracy too much. However, most existing active learning methods disregard the "structured information" that may exist in medical images (e.g., data from individual patients), and make a simplifying assumption that unlabeled data is independently and identically distributed. Both may not be suitable for real-world medical images. In this paper, we propose a novel batch-mode active learning method which explores and leverages such structured information in annotations of medical images to enforce diversity among the selected data, therefore maximizing the information gain. We formulate the active learning problem as an adaptive submodular function maximization probl

Weakly supervised machine learning

Abstract
                  Supervised learning aims to build a function or model that seeks as many mappings as possible between the training data and outputs, where each training data will predict as a label to match its corresponding ground‐truth value. Although supervised learning has achieved great success in many tasks, sufficient data supervision for labels is not accessible in many domains because accurate data labelling is costly and laborious, particularly in medical image analysis. The cost of the dataset with ground‐truth labels is much higher than in other domains. Therefore, it is noteworthy to focus on weakly supervised learning for medical image analysis, as it is more applicable for practical applications. In this review, the authors give an overview of the latest process of weakly supervised learning in medical image analysis, including incomplete, inexact, and inaccurate supervision, and introduce the related works on different applications for medical image analysis. Related concepts are illustrated to help readers get an overview ranging from supervised to unsupervised learning within the scope of machine learning. Furthermore, the challenges and future works of weakly supervised learning in medical image analysis are discussed.


## Quote


Semi-supervised learning has been widely applied to medical image segmentation tasks since it alleviates the heavy burden of acquiring expert-examined annotations and takes the advantage of unlabeled data which is much easier to acquire

In this study, we develope a novel low-rank modeling-based multi-label active learning method for selecting informative examples for medical image annotation.

The precise delineation of medical imagery furnishes pivotal and discerning data for medical practitioners for suitable diagnostic evaluations, monitoring disease evolution, and formulating effective treatment strategies. Supervised methods based on deep learning have achieved a remarkable performance in medical image segmentation [1]. However, these methods largely benefit from extensive annotation datasets [2], and acquiring pixel-level annotations on a broad scale frequently demands a significant time investment and specialized knowledge, and entails substantial expenses. To alleviate the dependence on a large amount of annotated data, semi-supervised learning (SemiSL) and contrastive learning (CL) complement each other and are widely used in medical image segmentation. However, these methods have two obvious shortcomings: (i) Relying on pretext tasks leads to a poor generalization ability. ... (ii) The lack of supervision signal leads to an overfitting problem.


## Conclusion


Semi-supervised learning has been widely applied to medical image segmentation tasks since it alleviates the heavy burden of acquiring expert-examined annotations and takes the advantage of unlabeled data which is much easier to acquire. This survey provides a taxonomy of existing deep semi-supervised learning methods for medical image segmentation tasks, grouping them into three main categories: pseudo labels, unsupervised regularization, and knowledge priors. Beyond summarizing technical novelties, the survey analyses and discusses the empirical results of these methods on several public benchmark datasets. The authors hope this review could inspire the research community to explore solutions for this challenge and further promote developments in this impactful area of research.


## Insight


methodology: L'apprentissage semi-supervisé (UA-MT, SASSNet, ACTION++) et faiblement supervisé (CCNN, DFTNet, Cluster-Re-Supervision) permettent de réduire la dépendance aux grands ensembles de données annotées en segmentation d'images médicales, mais restent sensibles à la qualité des labels.

rationale: L'apprentissage semi-supervisé est largement adopté en segmentation d'images médicales car il réduit la dépendance aux annotations expertes coûteuses tout en exploitant des données non labellisées plus faciles à acquérir.