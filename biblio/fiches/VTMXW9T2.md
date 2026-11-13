# Superpixel-Based Sparse Labeling for Efficient and Certain Medical Image Annotation



## Resume


Superpixel-Based Sparse Labeling for Efficient and Certain Medical Image Annotation

Pseudo Label-based Multi-View Annotation for Semi-Supervised Medical Image Segmentation

Annotating Medical Image Data

Every Annotation Counts: Multi-label Deep Supervision for Medical Image Segmentation

Medical Image Annotation

Medical Image Segmentation with Efficient Use of Annotations and Resources

Robust Learning-Based Parsing and Annotation of Medical Radiographs

An Annotation Sparsification Strategy for 3D Medical Image Segmentation via Representative Selection and Self-Training

Image segmentation is critical to lots of medical applications. While deep learning (DL) methods continue to improve performance for many medical image segmentation tasks, data annotation is a big bottleneck to DL-based segmentation because (1) DL models tend to need a large amount of labeled data to train, and (2) it is highly time-consuming and label-intensive to voxel-wise label 3D medical images. Significantly reducing annotation effort while attaining good performance of DL segmentation models remains a major challenge. In our preliminary experiments, we observe that, using partially labeled datasets, there is indeed a large performance gap with respect to using fully annotated training datasets. In this paper, we propose a new DL framework for reducing annotation effort and bridging the gap between full annotation and sparse annotation in 3D medical image segmentation. We achieve this by (i) selecting representative slices in 3D images that minimize data redundancy and save annotation effort, and (ii) self-training with pseudo-labels automatically generated from the base-models trained using the selected annotated slices. Extensive experiments using two public datasets (the HVSMR 2016 Challenge dataset and mouse piriform cortex dataset) show that our framework yields competitive segmentation results comparing with state-of-the-art DL methods using less than ∼20% of annotated data.

BoostMIS: Boosting Medical Image Semi-supervised Learning with Adaptive Pseudo Labeling and Informative Active Annotation

LabelMe: A Database and Web-Based Tool for Image Annotation

Residual Adaptive Sparse Hybrid Attention Transformer for Image Super Resolution

Learning with Limited Annotations: A Survey on Deep Semi-Supervised Learning for Medical Image Segmentation

Dual Annotation Learning with Selective Uncertainty for Medical Image Segmentation with Noisy Labels

Multi-frame image super-resolution reconstruction using sparse co-occurrence prior and sub-pixel registration

Label-Efficient Hybrid-Supervised Learning for Medical Image Segmentation

Due to the lack of expertise for medical image annotation, the investigation of label-efficient methodology for medical image segmentation becomes a heated topic. Recent progresses focus on the efficient utilization of weak annotations together with few strongly-annotated labels so as to achieve comparable segmentation performance in many unprofessional scenarios. However, these approaches only concentrate on the supervision inconsistency between strongly- and weakly-annotated instances but ignore the instance inconsistency inside the weakly-annotated instances, which inevitably leads to performance degradation.
 To address this problem, we propose a novel label-efficient hybrid-supervised framework, which considers each weakly-annotated instance individually and learns its weight guided by the gradient direction of the strongly-annotated instances, so that the high-quality prior in the strongly-annotated instances is better exploited and the weakly-annotated instances are depicted more precisely. Specially, our designed dynamic instance indicator (DII) realizes the above objectives, and is adapted to our dynamic co-regularization (DCR) framework further to alleviate the erroneous accumulation from distortions of weak annotations. Extensive experiments on two hybrid-supervised medical segmentation datasets demonstrate that with only 10% strong labels, the proposed framework can leverage the weak labels efficiently and achieve competitive performance against the 100% strong-label supervised scenario.

Suggestive Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

Active learning with noise modeling for medical image annotation

PyMIC: A deep learning toolkit for annotation-efficient medical image segmentation


## Quote


Annotation-Efficient Deep Learning for Medical Imaging

Annotation-Efficient Deep Learning for Medical Imaging

However, it differs in that sparse annotations involve pixel-wise precise labels on the annotated slices, as opposed to the coarse or incomplete labels typically used in WSSS.


## Methodologie


Cet article traite du problème central de l'annotation en segmentation sémantique d'images médicales, où l'étiquetage pixel par pixel par des experts cliniques, déjà coûteux dans des contextes non médicaux, devient un frein majeur du fait des contraintes de temps du personnel soignant. Les auteurs constatent que les approches existantes traitent séparément l'apprentissage semi-supervisé (données non annotées) et faiblement supervisé (labels de moindre qualité), alors que les scénarios cliniques réels combinent simultanément plusieurs types de supervision. Pour y répondre, ils proposent une nouvelle méthode de supervision profonde multi-label (Multi-label Deep Supervision) intégrant le signal d'apprentissage dans plusieurs couches d'un réseau UNet, puis l'étendent via deux approches de génération de pseudo-labels: Self-Taught Deep Supervision et sa variante la plus performante, Mean-Taught Deep Supervision, fondée sur un modèle mean-teacher apportant robustesse aux perturbations. L'évaluation méthodologique compare ces approches à plusieurs modèles de référence (Baseline, IIC Baseline, MIL et leurs variantes à supervision profonde) sur des jeux d'entraînement de taille très réduite (3, 6, 12 ou 24 images annotées), selon un protocole rigoureux avec plusieurs répartitions de données et écarts-types rapportés.


## Synthese


Cet article traite du problème central de l'annotation en segmentation sémantique d'images médicales, où l'étiquetage pixel par pixel par des experts cliniques, déjà coûteux dans des contextes non médicaux, devient un frein majeur du fait des contraintes de temps du personnel soignant. Les auteurs constatent que les approches existantes traitent séparément l'apprentissage semi-supervisé (données non annotées) et faiblement supervisé (labels de moindre qualité), alors que les scénarios cliniques réels combinent simultanément plusieurs types de supervision. Pour y répondre, ils proposent une nouvelle méthode de supervision profonde multi-label (Multi-label Deep Supervision) intégrant le signal d'apprentissage dans plusieurs couches d'un réseau UNet, puis l'étendent via deux approches de génération de pseudo-labels: Self-Taught Deep Supervision et sa variante la plus performante, Mean-Taught Deep Supervision, fondée sur un modèle mean-teacher apportant robustesse aux perturbations. L'évaluation méthodologique compare ces approches à plusieurs modèles de référence (Baseline, IIC Baseline, MIL et leurs variantes à supervision profonde) sur des jeux d'entraînement de taille très réduite (3, 6, 12 ou 24 images annotées), selon un protocole rigoureux avec plusieurs répartitions de données et écarts-types rapportés.

Cet article traite du problème central de l'annotation en segmentation sémantique d'images médicales, où l'étiquetage pixel par pixel par des experts cliniques, déjà coûteux dans des contextes non médicaux, devient un frein majeur du fait des contraintes de temps du personnel soignant. Les auteurs constatent que les approches existantes traitent séparément l'apprentissage semi-supervisé (données non annotées) et faiblement supervisé (labels de moindre qualité), alors que les scénarios cliniques réels combinent simultanément plusieurs types de supervision. Pour y répondre, ils proposent une nouvelle méthode de supervision profonde multi-label (Multi-label Deep Supervision) intégrant le signal d'apprentissage dans plusieurs couches d'un réseau UNet, puis l'étendent via deux approches de génération de pseudo-labels: Self-Taught Deep Supervision et sa variante la plus performante, Mean-Taught Deep Supervision, fondée sur un modèle mean-teacher apportant robustesse aux perturbations. L'évaluation méthodologique compare ces approches à plusieurs modèles de référence (Baseline, IIC Baseline, MIL et leurs variantes à supervision profonde) sur des jeux d'entraînement de taille très réduite (3, 6, 12 ou 24 images annotées), selon un protocole rigoureux avec plusieurs répartitions de données et écarts-types rapportés. L'analyse qualitative des résultats de segmentation (Fig. 4) confirme l'avantage de la supervision profonde multi-label par rapport à un modèle Baseline classique, cet effet étant particulièrement marqué dans les configurations à faible nombre d'annotations disponibles (3, 6, 12 ou 24 échantillons). La combinaison de la supervision profonde multi-label avec une approche semi-supervisée de type Mean-Teacher produit les meilleurs résultats visuels, notamment pour la délimitation des régions de fluide, y compris dans des scénarios d'annotation extrêmement limitée. À l'inverse, les autres méthodes comparées (IIC Baseline, MIL, Deeply Supervised IIC, Self-Taught Deep Supervision) échouent de manière importante à segmenter correctement ces mêmes régions lorsque le nombre d'échantillons annotés est très restreint. Ces observations qualitatives corroborent l'intérêt de la supervision profonde multi-label comme stratégie efficace pour l'apprentissage à partir d'annotations partielles ou rares en imagerie médicale. Cette étude introduit une nouvelle approche de segmentation d'images médicales capable d'exploiter des annotations hétérogènes, à savoir des labels pixel par pixel, des boîtes englobantes, des labels globaux et des images non annotées. Les auteurs montrent que le principe de supervision profonde, adapté pour délivrer des signaux de supervision jusque dans les couches intermédiaires à faible résolution spatiale, constitue un élément déterminant de la méthode. Un modèle élève-enseignant (student-teacher) est également introduit afin de stabiliser l'entraînement et d'améliorer la généralisation. Les expériences menées sur une application médicale complexe, avec un nombre variable d'échantillons annotés (3, 6, 12, 24), démontrent la flexibilité de l'approche ainsi que l'efficacité du concept de supervision profonde pour l'apprentissage semi-faiblement supervisé.


## Discussion


Cette étude introduit une nouvelle approche de segmentation d'images médicales capable d'exploiter des annotations hétérogènes, à savoir des labels pixel par pixel, des boîtes englobantes, des labels globaux et des images non annotées. Les auteurs montrent que le principe de supervision profonde, adapté pour délivrer des signaux de supervision jusque dans les couches intermédiaires à faible résolution spatiale, constitue un élément déterminant de la méthode. Un modèle élève-enseignant (student-teacher) est également introduit afin de stabiliser l'entraînement et d'améliorer la généralisation. Les expériences menées sur une application médicale complexe, avec un nombre variable d'échantillons annotés (3, 6, 12, 24), démontrent la flexibilité de l'approche ainsi que l'efficacité du concept de supervision profonde pour l'apprentissage semi-faiblement supervisé.


## Conclusion


We propose an effective non-iterative method for scribble-supervised segmentation in medical imaging. Our method attains a non-iterative training paradigm by means of a weight-sharing siamese architecture, wherein pseudo-masks reinforce network learning during training. Inspired by insights in consistency training, our designs to boost performance include the entropy regularization to obtain high-confidence pseudo-masks and the distorted augmentations to create discrepancy for consistency regularization. Besides, to complement scarce labeled pixels, we devise a memory bank that introduces extra cross-image ensemble features. Experimental results show that our method can bridge the gap between scribble-supervised and fully-supervised segmentation to some extent, and proves robust even to some undesirable scribbles. Thanks to its simplicity, the proposed method has the potential to be extended to 3D by using volumetric scribble-annotating approaches.


## Raw_Introduction


To address this challenge, many different approaches have been proposed in the recent years where users can use less time-consuming "sparse" annotations, such as scribbles and bounding boxes, to interactively prompt a pre-trained deep learning (DL) model to create "dense" annotations like detailed boundary masks [7,10,18]. While these approaches have shown to significantly reduce the annotation time per object, they require an expert to not just interactively create these annotations, but also fine-tune and validate them [7]. Therefore, there is a critical need for a data curation pipeline for medical image segmentation that would allow non-experts to annotate datasets with sparse annotations without the need for an expert in the loop. Recently, large DL foundation models trained in a selfsupervised manner on large-scale datasets on the order of a billion samples are revolutionizing the field of computer vision with their strong zero-shot generalizability [3,12,15]. This means that the

To address this challenge, many different approaches have been proposed in the recent years where users can use less time-consuming "sparse" annotations, such as scribbles and bounding boxes, to interactively prompt a pre-trained deep learning (DL) model to create "dense" annotations like detailed boundary masks [7,10,18]. While these approaches have shown to significantly reduce the annotation time per object, they require an expert to not just interactively create these annotations, but also fine-tune and validate them [7]. Therefore, there is a critical need for a data curation pipeline for medical image segmentation that would allow non-experts to annotate datasets with sparse annotations without the need for an expert in the loop. Recently, large DL foundation models trained in a selfsupervised manner on large-scale datasets on the order of a billion samples are revolutionizing the field of computer vision with their strong zero-shot generalizability [3,12,15]. This means that the


## Raw_Few-Shot_Medical_Image_Segmentation


Few-shot segmentation in natural image typically rely on extensive pre-training using labeled data from known semantic categories. This approach has influenced medical imaging, leading to the development of methods such as SE-Net [17], MRrNet [6], and GCN-DE [20], which utilize known category data to train efficient dual-branch interaction models. However, obtaining large-scale pre-labeled datasets in the medical domain is often impractical. To address this challenge, some researchers have turned to self-supervised learning techniques [3,8,14,22]. These approaches generate pseudo-labels through superpixel [5], enabling self-supervised pre-training. While this method reduces annotation costs, it still faces several limitations: (1) the necessity of a pre-training phase.

Few-shot segmentation in natural image typically rely on extensive pre-training using labeled data from known semantic categories. This approach has influenced medical imaging, leading to the development of methods such as SE-Net [17], MRrNet [6], and GCN-DE [20], which utilize known category data to train efficient dual-branch interaction models. However, obtaining large-scale pre-labeled datasets in the medical domain is often impractical. To address this challenge, some researchers have turned to self-supervised learning techniques [3,8,14,22]. These approaches generate pseudo-labels through superpixel [5], enabling self-supervised pre-training. While this method reduces annotation costs, it still faces several limitations: (1) the necessity of a pre-training phase.