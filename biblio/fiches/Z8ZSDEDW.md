# Rapid Image Labeling via Neuro-Symbolic Learning



## Raw_Conclusion


We present a rapid image labeling method based on neuro-symbolic learning. The proposed method uses pre-trained neural network models to extract visual attributes and use first-order inductive learning to infer labeling rules based on the visual attributes. This architecture disentangles perception from learning, enabling our method to be applied to new tasks by easily changing the pretrained visual attribute extractor. Besides, the declarative nature of logic rules enables users to directly inspect and edit the inferred labeling rules, explicitly embedding human expertise into the rules. The experiments show that our method can achieve outstanding performance on highly specialized domains under an extremely low resource setting while generalizing to other general domains with reasonable performance. ∨ has forehead color(X,grey) ∨ (has belly color(X,yellow) ∧ has nape color(X,buff)) ∨ (has nape color(X,grey) ∧ has primary color(X,yellow)) ∨ has shape(X,sandpiper-like) ∨ has leg color(X


## Raw_Introduction


In this paper, we propose a new neuro-symbolic approach called Rapid for image labeling in low-resource settings (e.g., less than 100 labeled images). The novelty of this framework lies in synergizing the strength of neural models (i.e., handling rich, complex image data) and the strength of inductive logic learning (i.e., learning from small datasets) to handle the image labeling challenge. Specifically, Rapid automatically infers logic rules from a small amount of labeled data, applies the inferred rules to label the unlabeled data, and solicits user feedback to refine the rules iteratively.

• We proposed a new neuro-symbolic learning framework that synergizes pre-trained computer vision models with inductive logic learning for rapid image labeling with a limited amount of training data; • We designed a new conflict-based informativeness metric for data selection in active learning; • We conducted comprehensive evaluations on four labeling tasks from different domains with user simulation and multiple baselines.

Deep learning models in computer vision require a large number of labeled images for training. While crowdsourcing is a commonly adopted method for image labeling, it is challenging to find and recruit crowd workers for specialized tasks that require domain expertise. To address this challenge, prior work has proposed to train automated image labeling models to reduce manual effort. [18] However, these methods still require domain experts to label many images to train the initial models [46,53]. For example, Asaoka et al. [5] proposed to leverage CNN and transfer learning to automatically label early glaucoma eye images. This model requires 4316 eye images for pre-training and 178 eye images for fine-tuning. Furthermore, when the model makes a labeling error, domain experts have a difficult time diagnosing and refining the model due to the lack of transparency of DL models [46].

Deep learning models in computer vision require a large number of labeled images for training. While crowdsourcing is a commonly adopted method for image labeling, it is challenging to find and recruit crowd workers for specialized tasks that require domain expertise. To address this challenge, prior work has proposed to train automated image labeling models to reduce manual effort. [18] However, these methods still require domain experts to label many images to train the initial models [46,53]. For example, Asaoka et al. [5] proposed to leverage CNN and transfer learning to automatically label early glaucoma eye images. This model requires 4316 eye images for pre-training and 178 eye images for fine-tuning. Furthermore, when the model makes a labeling error, domain experts have a difficult time diagnosing and refining the model due to the lack of transparency of DL models [46].


## Raw_Methods


Figure 2 gives an overview of our approach called Rapid. Rapid consists of three parts-(1) a pre-trained visual attribute extractor to extract basic, low-level visual attributes from images, (2) an inductive learner to infer logic labeling rules from the relationship between the visual attributes and the target classes, and (3) a multicriteria data selection module to select a small set of informative and diverse automatically labeled data for users to inspect and fix. Rapid works iteratively. It starts with a small initial set of training images created by human users. In each iteration, Rapid first extracts the visual attributes of each labeled image. Then, it takes as input the visual attributes and the corresponding class label of the images to infer a set of labeling rules for each class. The inferred rules are then applied to automatically generate labels for unannotated images. In case of contradicting labels, Rapid selects the corresponding label of the rule with the highest Cl


## Raw_Neuro-Symbolic_Learning


Unlike existing neuro-symbolic learning approaches in this category, we are the first to use inductive logic learning as the symbolic method for rule inference. In this way, we can explicitly model the logic of labeling rules. Furthermore, our approach is also the first to apply neuro-symbolic learning to image labeling.


## Raw_Domain_Context


The image labeling domain is integral to computer vision applications, enabling supervised machine learning models to recognize and interpret visual data by mapping spatial information in images with semantic labels. This process provides essential training data for computer vision systems used in areas like autonomous driving [8], healthcare diagnostics [6], and even micropalaeontology [11]. While traditional labeling methods are accurate, they are highly labor-intensive, requiring considerable human expertise and time [9]. Current efforts focus on developing interactive labeling tools that support both manual and semi-automated labeling, with enhancements in user interfaces, collaborative features, and gamification elements. Despite advancements, labeling remains a challenging and resource-intensive task, prompting continued research into efficient, scalable methods that can provide high-quality, large-scale annotations [23]. LabelMe [22] is an iconic example. It is a platform where

The image labeling domain is integral to computer vision applications, enabling supervised machine learning models to recognize and interpret visual data by mapping spatial information in images with semantic labels. This process provides essential training data for computer vision systems used in areas like autonomous driving [8], healthcare diagnostics [6], and even micropalaeontology [11]. While traditional labeling methods are accurate, they are highly labor-intensive, requiring considerable human expertise and time [9]. Current efforts focus on developing interactive labeling tools that support both manual and semi-automated labeling, with enhancements in user interfaces, collaborative features, and gamification elements. Despite advancements, labeling remains a challenging and resource-intensive task, prompting continued research into efficient, scalable methods that can provide high-quality, large-scale annotations [23]. LabelMe [22] is an iconic example. It is a platform where


## Raw_Experiment_Design_&_Setup


To answer RQ1, we measure the image labeling accuracy and efficiency of Rapid on four different image labeling tasks-two from highly specialized domains and two from common domains. Section 4.3 describes the four tasks and datasets. To represent the condition of learning from limited training data, for each task, we bootstrap Rapid with only 3 randomly sampled data instances with labels to learn the initial set of rules. In each following iteration, the active learning module selects 3 images and corrects their labels if wrong to refine the learned labeling rules. The choice of 3 is to simulate the rapid, incremental feedback from users. This process continues until the 20th iteration. Thus, for each task, Rapid is trained with in total 60 images. We compare Rapid with 6 baselines. Section 4.4 describes these baselines and their training procedures.

RQ3 aims to measure the effectiveness of adopting inductive logic learning for image labeling. To answer RQ3, we create four variants of Rapid by replacing the inductive logic learning module in Rapid with three statistical models-SVM, random forest, and XGBoost [7]-and a neural network. The design of these variants is inspired by existing frameworks such as Snorkel [31] and Concept Bottle Network [20], which use statistical models to make the final prediction based on symbolic representations extracted from raw input data. For the neural network variant, we adopt the design of the fully connected layers in ResNet-18 [15].


## Raw_Human_Feedback_In_Inductive_Logic_Learning


The overview of our image labeling approach.


## Raw_Related_Work_2.1_Image_Labeling


Reducing the human effort in image labeling has become increasingly important in recent years with the advent of deep learning, which requires a massive amount of labeled data to train a model. There has been a continuous effort to develop automated solutions for image labeling. The basic idea is to train a model with some labeled data and automatically assign labels to new data samples without further human involvement. Among these existing methods, fully-automated methods have attracted significant attention and achieved promising performance. Some methods exploit the similarity between unlabeled and label images [8]. Some methods resolve the problem of data scarcity by creating representations of images using auxiliary information such as corresponding captions [29], meta-data [24], or pseudo-labels generated by other models [39]. Despite the promising performance of these methods, they often lack generalizability to domains where data acquisition is challenging, as the models usual

To address these limitations, we design an interactive labeling system tailored for specialized domains. Our system uses the ILPbased image classification algorithm from RAPID [56]. However, RAPID lacks a user-friendly interface, which poses challenges for domain experts in effectively using the system. Therefore, we design a user interface to visualize labeling rules and enable experts to understand and edit the rules. We further propose a rule-level recommendation mechanism to assist in rule refinement. Compared to RAPID, our framework not only improves image labeling accuracy but also enhances interpretability, enabling domain experts to better understand and correct errors.

To address these limitations, we design an interactive labeling system tailored for specialized domains. Our system uses the ILPbased image classification algorithm from RAPID [56]. However, RAPID lacks a user-friendly interface, which poses challenges for domain experts in effectively using the system. Therefore, we design a user interface to visualize labeling rules and enable experts to understand and edit the rules. We further propose a rule-level recommendation mechanism to assist in rule refinement. Compared to RAPID, our framework not only improves image labeling accuracy but also enhances interpretability, enabling domain experts to better understand and correct errors.

ly require a substantial amount of data to learn the knowledge. Thus, some semi-automated labeling approaches use human efforts in the training or inference process to provide the information needed for training [37] or a coarse initial label [13]. Compared with existing work, our approach uses inductive logic learning to infer logic rules from a small amount of human-annotated data to label images.


## Raw_Cam_Generation


Image segmentation requires a huge amount of pixel-level labels, resulting in labeling burden, especially in medical images which need expert experience. Fortunately, supervised by image-level labels only, the CAMs can roughly locate the foreground regions and provide good seeds for segmentation. In this paper, we follow the main-stream approach to train a fully supervised classification model with image-level labels. We replace the stride with dilation in the last layer to increase the map size on ResNet-50. Meanwhile, we also use regularization terms, drop blocks, and data augmentation to guarantee a good performance. After training, we calculate the CAMs via the Grad-CAM method [16]:

Image segmentation requires a huge amount of pixel-level labels, resulting in labeling burden, especially in medical images which need expert experience. Fortunately, supervised by image-level labels only, the CAMs can roughly locate the foreground regions and provide good seeds for segmentation. In this paper, we follow the main-stream approach to train a fully supervised classification model with image-level labels. We replace the stride with dilation in the last layer to increase the map size on ResNet-50. Meanwhile, we also use regularization terms, drop blocks, and data augmentation to guarantee a good performance. After training, we calculate the CAMs via the Grad-CAM method [16]:


## Raw_Full_Text


Chapter 2. State of the Art on Image Annotation
alternative for automatically annotating large-scale image databases with semantic
concepts. In semi-supervised learning, a number of labeled examples are usually re-
quired for training an initial weakly useful predictor which is in turn used for exploiting
the unlabeled examples [Guillaumin et al., 2010]. Therefore, these approaches try to
tackle the image annotation problem by incorporating the information gathered from
labeled images in a large amount of unlabeled data. [Zhu, 2006] proposed a good
introduction to Semi-Supervised Learning (SSL).
Current semi-supervised learning based approaches can be categorized into three
main paradigms.
• In the ﬁrst, a generative model, such as Naive Bayes classiﬁers or a mixture of
Gaussians, is used to model the joint probability distribution over observations
and label sequences. The EM algorithm is then performed in order to model the
label estimation or the parameter estimation process [Guilla

Chapter 2. State of the Art on Image Annotation
alternative for automatically annotating large-scale image databases with semantic
concepts. In semi-supervised learning, a number of labeled examples are usually re-
quired for training an initial weakly useful predictor which is in turn used for exploiting
the unlabeled examples [Guillaumin et al., 2010]. Therefore, these approaches try to
tackle the image annotation problem by incorporating the information gathered from
labeled images in a large amount of unlabeled data. [Zhu, 2006] proposed a good
introduction to Semi-Supervised Learning (SSL).
Current semi-supervised learning based approaches can be categorized into three
main paradigms.
• In the ﬁrst, a generative model, such as Naive Bayes classiﬁers or a mixture of
Gaussians, is used to model the joint probability distribution over observations
and label sequences. The EM algorithm is then performed in order to model the
label estimation or the parameter estimation process [Guilla

., 2011], and artiﬁcial neural networks [Romdhane et al., 2010] are often
used to learn high-level concepts (i.e. semantic content) from low-level features (i.e.
visual content). This is achieved by collecting a set of positive and negative training
images for the concept of interest, and therefore a binary classiﬁer is trained to detect
this concept. The process is repeated for each concept of the annotation vocabulary.
These classiﬁers are then applied to all database images which are, accordingly, an-
notated with respect to the presence or absence of the concepts from the annotation
vocabulary.
Other approaches have attempted to address the problem more generally by
using unsupervised learning [Barnard and Forsyth, 2001, Duygulu et al., 2002,
Blei and Jordan, 2003, Lavrenko et al., 2003].
Usually, these approaches employ
probabilistic models to explain the co-occurrence between image features and se-
mantic labels.
The basic idea of these approaches is to introduce a set of latent

., 2011], and artiﬁcial neural networks [Romdhane et al., 2010] are often
used to learn high-level concepts (i.e. semantic content) from low-level features (i.e.
visual content). This is achieved by collecting a set of positive and negative training
images for the concept of interest, and therefore a binary classiﬁer is trained to detect
this concept. The process is repeated for each concept of the annotation vocabulary.
These classiﬁers are then applied to all database images which are, accordingly, an-
notated with respect to the presence or absence of the concepts from the annotation
vocabulary.
Other approaches have attempted to address the problem more generally by
using unsupervised learning [Barnard and Forsyth, 2001, Duygulu et al., 2002,
Blei and Jordan, 2003, Lavrenko et al., 2003].
Usually, these approaches employ
probabilistic models to explain the co-occurrence between image features and se-
mantic labels.
The basic idea of these approaches is to introduce a set of latent


## Quote


Annotation-Efficient Deep Learning for Medical Imaging

Annotation-Efficient Deep Learning for Medical Imaging

We extended the sparse-graph-based semisupervised learning method to multilabel setting by integrating the semantic correlation as the basic learning model.


## Synthese


L'article vise à concevoir une méthode d'annotation automatique d'images qui soit à la fois précise et rapide, condition jugée nécessaire pour un déploiement dans des applications réelles. Le contexte scientifique qui motive ce travail est le constat que les méthodes antérieures d'annotation d'images modélisent la relation image-label de façon trop simpliste, limitée à une présence ou absence binaire de labels, ce qui restreint leur capacité prédictive. Les auteurs formulent l'hypothèse que l'apprentissage explicite et soigné d'une interrelation image-label, via un cadre de régression combiné à une régularisation label-biased, permettrait d'obtenir une modélisation plus effective et significative que les approches à relations simples, tout en conservant une complexité computationnelle réduite grâce à une résolution en forme close.

Cet article, présenté à la conférence IEEE International Conference on Image Processing (ICIP) en 2014, s'attaque au problème de l'annotation automatique d'images en proposant une méthode fondée sur l'apprentissage explicite de l'interrelation image-label, plutôt que sur une simple relation binaire de présence/absence de labels. L'objectif est double : atteindre une précision élevée tout en garantissant un temps d'apprentissage rapide, condition nécessaire pour des applications réelles. La méthode formule le problème comme une régression entre le label groundtruth et l'information de label propagée linéairement à travers une matrice d'interrelation image-label apprise conjointement avec les similarités d'images précalculées à partir de features multiples, sans nécessiter de réduction de dimensionnalité. Une régularisation label-biased est intégrée pour renforcer les entrées correspondant à la présence effective de labels et supprimer celles correspondant à leur absence, ce qui permet d'apprendre une interrelation plus effective et significative. La fonction objectif finale, compacte, admet une solution en forme close (closed form), ce qui confère à la méthode un processus d'apprentissage nettement plus rapide que les approches itératives classiques. L'évaluation expérimentale est menée sur trois jeux de données benchmark de référence en annotation d'images : Corel5K, IAPRTC-12 et ESP game, avec les métriques standards mean precision (P), mean recall (R), F1 (F1 = 2PR/(P+R)) et N+ (nombre de labels avec un rappel non nul). Sur Corel5K, la méthode proposée surpasse significativement MSC, sa méthode source d'inspiration, avec un gain de 24% en mean precision, 31% en mean recall et 22 unités supplémentaires en N+, ce qui démontre que l'apprentissage soigné des interrelations image-label est nettement plus efficace que les relations simples de présence/absence. Comparée aux méthodes état de l'art TagProp et FastTag, la méthode proposée atteint des performances comparables sur les trois jeux de données, tout en offrant un temps d'apprentissage plus rapide, ce qui constitue son principal avantage pratique. Le seul résultat insatisfaisant concerne la mean precision sur ESP game, inférieure de 9% par rapport à TagProp et de 16% par rapport à FastTag, un écart que les auteurs attribuent notamment à la régularisation marginalized blank-out propre à FastTag qui améliore sa précision et son N+ au détriment du rappel. Trois hyperparamètres gouvernent le modèle (σ, β et λ), avec σ = 0,34 et λ = 10⁻⁴ identifiés empiriquement comme stables sur les trois datasets, tandis que β nécessite un réglage spécifique par dataset (seuils optimaux atteints au-delà de 0,2 pour Corel5K, 0,05 pour IAPRTC-12 et 0,0005 pour ESP game). Les auteurs concluent que la propagation linéaire de l'information de label via une matrice d'interrelation apprise conjointement avec les similarités d'images constitue une approche viable, offrant un compromis performance/rapidité favorable pour des applications réelles d'annotation d'images.


## Raw_Image_Labeling_Platform


Label Assistant [24] presents a sketch-based labeling tool to assist the annotation process in image segmentation tasks, especially for deep learning applications. The proposed workflow integrates various methods, including pre-labeling, image pre-processing, and post-assistance to aid annotators in labeling complex image datasets efficiently. The authors demonstrate the effectiveness of the workflow on two biomedical image segmentation datasets, showing that their approach reduces annotation effort while maintaining high-quality labels. However, they didn't provide feedback to users.

Label Assistant [24] presents a sketch-based labeling tool to assist the annotation process in image segmentation tasks, especially for deep learning applications. The proposed workflow integrates various methods, including pre-labeling, image pre-processing, and post-assistance to aid annotators in labeling complex image datasets efficiently. The authors demonstrate the effectiveness of the workflow on two biomedical image segmentation datasets, showing that their approach reduces annotation effort while maintaining high-quality labels. However, they didn't provide feedback to users.


## Raw_Rq2._Effectiveness_Of_Human_Feedback


3 samples, 2 means training with 6 samples, 3 means training with 9 samples, so on and so forth. Overall, Rapid achieves the highest image labeling accuracy (86.11%) with only 12 iterations and 36 images in total. While Rapid 𝑛𝑜-𝑎𝑙 achieves the same accuracy, it takes 7 more iterations and thus 21 more images to reach this accuracy. In this task, both Rapid 𝑛𝑜-𝑒𝑑𝑖𝑡 and Rapid 𝑛𝑜-𝑓 𝑒𝑒𝑑𝑏𝑎𝑐𝑘 takes significantly more iterations to achieve the final accuracy.