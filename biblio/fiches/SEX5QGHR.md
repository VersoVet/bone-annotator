# Dual Annotation Learning with Selective Uncertainty for Medical Image Segmentation with Noisy Labels



## Resume


Dual Annotation Learning with Selective Uncertainty for Medical Image Segmentation with Noisy Labels

Region Uncertainty Estimation for Medical Image Segmentation With Noisy Labels.

The success of deep learning in 3D medical image segmentation hinges on training with a large dataset of fully annotated 3D volumes, which are difficult and time-consuming to acquire. Although recent foundation models (e.g., segment anything model, SAM) can utilize sparse annotations to reduce annotation costs, segmentation tasks involving organs and tissues with blurred boundaries remain challenging. To address this issue, we propose a region uncertainty estimation framework for Computed Tomography (CT) image segmentation using noisy labels. Specifically, we propose a sample-stratified training strategy that stratifies samples according to their varying quality labels, prioritizing confident and fine-grained information at each training stage. This sample-to-voxel level processing enables more reliable supervision information to propagate to noisy label data, thus effectively mitigating the impact of noisy annotations. Moreover, we further design a boundary-guided regional uncertainty

Uncertainty‐aware iterative learning for noisy‐labeled medical image segmentation

<jats:title>Abstract</jats:title>
                  Medical image segmentation from noisy labels is an important task since obtaining high‐quality annotations is extremely difficult and expensive. There are a lot of approaches proposed for such task. However, some issues like the overfitting on noisy annotations, the limited learning of boundary features, and no consideration of the corrupted local pixels are still not solved. Therefore, a novel approach named uncertainty‐aware iterative learning (UaIL) is proposed for medical image segmentation with noisy labels. UaIL iteratively and jointly trains two deep networks using the original images and their argumented ones through a joint loss function including softened label loss, hard label loss and consistency loss, which encourages UaIL to produce segmentations that are robust to the perturbations in arbitrary semantic space. The uncertainty of labels is estimated based on the predictions in iterative learning, then the original labels

Active learning with noise modeling for medical image annotation

Learning with Limited Annotations: A Survey on Deep Semi-Supervised Learning for Medical Image Segmentation

Label refinement for noisy annotation in weakly supervised segmentation

Medical Image Segmentation with Efficient Use of Annotations and Resources

Annotation Ambiguity Aware Semi-Supervised Medical Image Segmentation

Pseudo Label-based Multi-View Annotation for Semi-Supervised Medical Image Segmentation

Annotation noise-aware semi-supervised and domain adaptive learning for 3D medical imaging

Active Label Refinement for Robust Training of Imbalanced Medical Image Classification Tasks in the Presence of High Label Noise

The robustness of supervised deep learning-based medical image classification is significantly undermined by label noise. Although several methods have been proposed to enhance classification performance in the presence of noisy labels, they face some challenges: 1) a struggle with class-imbalanced datasets, leading to the frequent overlooking of minority classes as noisy samples; 2) a singular focus on maximizing performance using noisy datasets, without incorporating experts-in-the-loop for actively cleaning the noisy labels. To mitigate these challenges, we propose a two-phase approach that combines Learning with Noisy Labels (LNL) and active learning. This approach not only improves the robustness of medical image classification in the presence of noisy labels, but also iteratively improves the quality of the dataset by relabeling the important incorrect labels, under a limited annotation budget. Furthermore, we introduce a novel Variance of Gradients approach in LNL phase, which c

Invited 2 - Annotation-Efficient Deep Learning for Medical Image Segmentation

An Annotation Sparsification Strategy for 3D Medical Image Segmentation via Representative Selection and Self-Training

Image segmentation is critical to lots of medical applications. While deep learning (DL) methods continue to improve performance for many medical image segmentation tasks, data annotation is a big bottleneck to DL-based segmentation because (1) DL models tend to need a large amount of labeled data to train, and (2) it is highly time-consuming and label-intensive to voxel-wise label 3D medical images. Significantly reducing annotation effort while attaining good performance of DL segmentation models remains a major challenge. In our preliminary experiments, we observe that, using partially labeled datasets, there is indeed a large performance gap with respect to using fully annotated training datasets. In this paper, we propose a new DL framework for reducing annotation effort and bridging the gap between full annotation and sparse annotation in 3D medical image segmentation. We achieve this by (i) selecting representative slices in 3D images that minimize data redundancy and save annotation effort, and (ii) self-training with pseudo-labels automatically generated from the base-models trained using the selected annotated slices. Extensive experiments using two public datasets (the HVSMR 2016 Challenge dataset and mouse piriform cortex dataset) show that our framework yields competitive segmentation results comparing with state-of-the-art DL methods using less than ∼20% of annotated data.

Efficient Deep-Learning-Assisted Annotation for Medical Image Segmentation

Image segmentation is a fundamental problem in medical image analysis.
Deep learning (DL) methods have achieved state-of-the-art (SOTA) results
in various medical image segmentation tasks. This success is largely
attributable to the use of large annotated datasets for training.
However, due to anatomical variations and complexity of medical image
data, annotations of large medical image datasets are not only
labor-intensive and time-consuming but also demand specialty-oriented
skills. In this paper, we report a novel segmentation quality assessment
(SQA) framework that combines active learning and assisted annotation to
dramatically reduce annotation effort both in image selection and
annotation querying from human experts. We propose a two-branch network
that integrates a spatial and channel-wise probability attention module
into the segmentation network to perform segmentation and predict
potential segmentation errors simultaneously. By directly assessing the
segmentation quality of

Active learning for medical image segmentation with stochastic batches.

The performance of learning-based algorithms improves with the amount of labelled data used for training. Yet, manually annotating data is particularly difficult for medical image segmentation tasks because of the limited expert availability and intensive manual effort required. To reduce manual labelling, active learning (AL) targets the most informative samples from the unlabelled set to annotate and add to the labelled training set. On the one hand, most active learning works have focused on the classification or limited segmentation of natural images, despite active learning being highly desirable in the difficult task of medical image segmentation. On the other hand, uncertainty-based AL approaches notoriously offer sub-optimal batch-query strategies, while diversity-based methods tend to be computationally expensive. Over and above methodological hurdles, random sampling has proven an extremely difficult baseline to outperform when varying learning and sampling conditions. This w

Active Learning With Sampling by Uncertainty and Density for Data Annotations

Suppressing label noise in medical image classification using mixup attention and self-supervised learning.

Deep neural networks (DNNs) have been widely applied in medical image classification and achieve remarkable classification performance. These achievements heavily depend on large-scale accurately annotated training data. However, label noise is inevitably introduced in the medical image annotation, as the labeling process heavily relies on the expertise and experience of annotators. Meanwhile, DNNs suffer from overfitting noisy labels, degrading the performance of models. Therefore, in this work, we innovatively devise a noise-robust training approach to mitigate the adverse effects of noisy labels in medical image classification. Specifically, we incorporate contrastive learning and intra-group mixup attention strategies into vanilla supervised learning. The contrastive learning for feature extractor helps to enhance visual representation of DNNs. The intra-group mixup attention module constructs groups and assigns self-attention weights for group-wise samples, and subsequently interp

Annotating Medical Image Data

Active Learning in Brain Tumor Segmentation with Uncertainty Sampling and Annotation Redundancy Restriction.

U-MedSAM: Uncertainty-Aware MedSAM for Medical Image Segmentation

Label-Efficient Hybrid-Supervised Learning for Medical Image Segmentation

Due to the lack of expertise for medical image annotation, the investigation of label-efficient methodology for medical image segmentation becomes a heated topic. Recent progresses focus on the efficient utilization of weak annotations together with few strongly-annotated labels so as to achieve comparable segmentation performance in many unprofessional scenarios. However, these approaches only concentrate on the supervision inconsistency between strongly- and weakly-annotated instances but ignore the instance inconsistency inside the weakly-annotated instances, which inevitably leads to performance degradation.
 To address this problem, we propose a novel label-efficient hybrid-supervised framework, which considers each weakly-annotated instance individually and learns its weight guided by the gradient direction of the strongly-annotated instances, so that the high-quality prior in the strongly-annotated instances is better exploited and the weakly-annotated instances are depicted more precisely. Specially, our designed dynamic instance indicator (DII) realizes the above objectives, and is adapted to our dynamic co-regularization (DCR) framework further to alleviate the erroneous accumulation from distortions of weak annotations. Extensive experiments on two hybrid-supervised medical segmentation datasets demonstrate that with only 10% strong labels, the proposed framework can leverage the weak labels efficiently and achieve competitive performance against the 100% strong-label supervised scenario.

Keypoint-Augmented Self-Supervised Learning for Medical Image Segmentation with Limited Annotation

Every Annotation Counts: Multi-label Deep Supervision for Medical Image Segmentation

Unsupervised Segmentation Evaluation for Image Annotation

Modeling annotator preference and stochastic annotation error for medical image segmentation


## Quote


Annotation-Efficient Deep Learning for Medical Imaging

Annotation-Efficient Deep Learning for Medical Imaging


## Synthese


Le segmentation d'images médicales constitue une tâche fondamentale pour de nombreuses applications biomédicales, mais les modèles d'apprentissage profond dépendent fortement d'annotations exhaustives de haute qualité, dont la production reste coûteuse en expertise, en temps et en main-d'œuvre. Pour pallier cette limite, les auteurs proposent un framework hybride-supervisé combinant, de façon itérative, un niveau supérieur d'Instance Importance Learning (DII) et un niveau inférieur de Dual Co-Regularization (DCR). Le module DII ajuste automatiquement le poids attribué à chaque instance faiblement annotée en s'appuyant sur la direction du gradient issue des quelques instances fortement annotées, ce qui permet de compenser l'incohérence entre instances faiblement labellisées. Le module DCR repose sur une architecture à double réseau entraînée de manière collaborative, chaque réseau étant supervisé à la fois par son annotation propre et par le masque pseudo-généré par l'autre branche, réduisant ainsi la distorsion inhérente aux labels faibles. Cette approche permet, avec seulement 10% de labels forts, d'atteindre une performance compétitive comparable à un scénario entièrement supervisé.

Le segmentation d'images médicales constitue une tâche fondamentale pour de nombreuses applications biomédicales, mais les modèles d'apprentissage profond dépendent fortement d'annotations exhaustives de haute qualité, dont la production reste coûteuse en expertise, en temps et en main-d'œuvre. Pour pallier cette limite, les auteurs proposent un framework hybride-supervisé combinant, de façon itérative, un niveau supérieur d'Instance Importance Learning (DII) et un niveau inférieur de Dual Co-Regularization (DCR). Le module DII ajuste automatiquement le poids attribué à chaque instance faiblement annotée en s'appuyant sur la direction du gradient issue des quelques instances fortement annotées, ce qui permet de compenser l'incohérence entre instances faiblement labellisées. Le module DCR repose sur une architecture à double réseau entraînée de manière collaborative, chaque réseau étant supervisé à la fois par son annotation propre et par le masque pseudo-généré par l'autre branche, réduisant ainsi la distorsion inhérente aux labels faibles. Cette approche permet, avec seulement 10% de labels forts, d'atteindre une performance compétitive comparable à un scénario entièrement supervisé. Cette conclusion présente un framework d'apprentissage hybride bi-niveau pour la segmentation d'images médicales, conçu pour tirer parti d'un grand nombre d'instances faiblement annotées associées à un nombre restreint d'instances fortement annotées. L'approche repose sur deux composantes complémentaires : l'algorithme d'apprentissage DII, qui ajuste automatiquement le poids attribué à chaque instance faiblement annotée en se guidant sur la direction du gradient issu des rares instances fortement annotées, ce qui permet de compenser l'incohérence entre instances ; et le framework DCR, qui combine un entraînement collaboratif et une régularisation de cohérence pour atténuer la distorsion inhérente aux annotations faibles. Les expériences menées démontrent que cette méthode surpasse nettement les approches état de l'art existantes et se rapproche des performances obtenues en supervision complète. Les auteurs concluent que ce framework constitue une solution prometteuse pour la segmentation d'images médicales dans des contextes où l'annotation exhaustive est coûteuse ou difficile à obtenir.


## Methodologie


Le segmentation d'images médicales constitue une tâche fondamentale pour de nombreuses applications biomédicales, mais les modèles d'apprentissage profond dépendent fortement d'annotations exhaustives de haute qualité, dont la production reste coûteuse en expertise, en temps et en main-d'œuvre. Pour pallier cette limite, les auteurs proposent un framework hybride-supervisé combinant, de façon itérative, un niveau supérieur d'Instance Importance Learning (DII) et un niveau inférieur de Dual Co-Regularization (DCR). Le module DII ajuste automatiquement le poids attribué à chaque instance faiblement annotée en s'appuyant sur la direction du gradient issue des quelques instances fortement annotées, ce qui permet de compenser l'incohérence entre instances faiblement labellisées. Le module DCR repose sur une architecture à double réseau entraînée de manière collaborative, chaque réseau étant supervisé à la fois par son annotation propre et par le masque pseudo-généré par l'autre branche, réduisant ainsi la distorsion inhérente aux labels faibles. Cette approche permet, avec seulement 10% de labels forts, d'atteindre une performance compétitive comparable à un scénario entièrement supervisé.