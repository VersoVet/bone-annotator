# Semi-Supervised Semantic Annotator (S3A): Toward Efficient Semantic Image Labeling



## Resume


Semi-Supervised Semantic Annotator (S3A): Toward Efficient Semantic Image Labeling

Supervised Learning of Semantic Classes for Image Annotation and Retrieval

Image Segmentation and Labeling Using Free-Form Semantic Annotation

Pseudo Label-based Multi-View Annotation for Semi-Supervised Medical Image Segmentation

Semantic-Gap-Oriented Active Learning for Multilabel Image Annotation

Human-machine collaboration on data annotation of images by semi-automatic labeling

Semi-automatic video semantic annotation based on active learning

Semi-Supervised Semantic Image Segmentation with Self-correcting Networks

VAST (Volume Annotation and Segmentation Tool): Efficient Manual and Semi-Automatic Labeling of Large 3D Image Stacks

Semantic Image Segmentation Annotation Refinement Using SAM

Deep Active Re-Labeling: Toward Noise-Resilient Annotation Efficiency

DL-AAT: An Automatic Annotation Tool for Efficient Data Labeling in Vision-Based Systems

BoostMIS: Boosting Medical Image Semi-supervised Learning with Adaptive Pseudo Labeling and Informative Active Annotation

Unsupervised Segmentation Evaluation for Image Annotation


## Raw_Full_Text


tica-Perez, 2003, Monay and Gatica-Perez, 2004] pro-
posed to use Latent Semantic Analysis (LSA) and Probabilistic Latent Semantic
Analysis (PLSA) for image annotation.
2.4.2.3
Semi-Supervised Learning
Some recent work for image annotation have proposed to use semi-supervised learning
to draw beneﬁts from both, labeled and unlabeled (or weakly labeled) images. Indeed,
due to the lack of available labeled training data, semi-supervised learning is a good
33

tica-Perez, 2003, Monay and Gatica-Perez, 2004] pro-
posed to use Latent Semantic Analysis (LSA) and Probabilistic Latent Semantic
Analysis (PLSA) for image annotation.
2.4.2.3
Semi-Supervised Learning
Some recent work for image annotation have proposed to use semi-supervised learning
to draw beneﬁts from both, labeled and unlabeled (or weakly labeled) images. Indeed,
due to the lack of available labeled training data, semi-supervised learning is a good
33

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

ally
consistent image annotation.
3. To our knowledge, this is the ﬁrst attempt integrating such a complex reasoning
process, i.e using subsumption relationships, and also contextual and spatial
relationships.
4. Illustrate and test our approach on a public dataset assumed to be enough
representative of real current applications.
To sum up, in Chapters 3 and 4, we have proposed new approaches to build explicit
structured knowledge models about image semantics. In this chapter, we propose to
use these built knowledge models in a framework for reasoning over the outputs of
machine learning algorithms. Our objective is to provide a semantically consistent
image annotation while handling the imprecision of machine learning approaches.
6.3
Overview of the Proposed Framework
Image classiﬁcation is one of the most widely used technique for image annotation.
It consists in performing several binary SVM classiﬁers on an input image to ﬁnd to
which classes it belongs to. The annotation of an ima

ally
consistent image annotation.
3. To our knowledge, this is the ﬁrst attempt integrating such a complex reasoning
process, i.e using subsumption relationships, and also contextual and spatial
relationships.
4. Illustrate and test our approach on a public dataset assumed to be enough
representative of real current applications.
To sum up, in Chapters 3 and 4, we have proposed new approaches to build explicit
structured knowledge models about image semantics. In this chapter, we propose to
use these built knowledge models in a framework for reasoning over the outputs of
machine learning algorithms. Our objective is to provide a semantically consistent
image annotation while handling the imprecision of machine learning approaches.
6.3
Overview of the Proposed Framework
Image classiﬁcation is one of the most widely used technique for image annotation.
It consists in performing several binary SVM classiﬁers on an input image to ﬁnd to
which classes it belongs to. The annotation of an ima

Chapter 2. State of the Art on Image Annotation
Semantic level (visual
vs. semantics)
Reasoning capabilities
(implicit vs.
explicit
Knowledge)
Scalability
(image
number)
Scalability
(concept
number)
Visual CBIR
-
-
++++
-
Concept Detector
++
+
++++
+
Supervised Learning
++
+
++
++
Unsupervised Learning
+
+
+++
+++
Semi-Supervised Lear.
+
+
+++
++
Hierarchical Classif.
++
++
++++
+++
Information Fusion
++
++
+++
+++
LWO
+++
+++
+++
+++
HWO
++++
+++
+
+
Formal Ontologies
++++
++++
++++
++
Table 2.3: Comparison of the diﬀerent categories of approaches for image annotation.
50

Chapter 2. State of the Art on Image Annotation
Semantic level (visual
vs. semantics)
Reasoning capabilities
(implicit vs.
explicit
Knowledge)
Scalability
(image
number)
Scalability
(concept
number)
Visual CBIR
-
-
++++
-
Concept Detector
++
+
++++
+
Supervised Learning
++
+
++
++
Unsupervised Learning
+
+
+++
+++
Semi-Supervised Lear.
+
+
+++
++
Hierarchical Classif.
++
++
++++
+++
Information Fusion
++
++
+++
+++
LWO
+++
+++
+++
+++
HWO
++++
+++
+
+
Formal Ontologies
++++
++++
++++
++
Table 2.3: Comparison of the diﬀerent categories of approaches for image annotation.
50

Chapter 2. State of the Art on Image Annotation
Indeed, the use of explicit semantic structures, such as semantic hierarchies and
ontologies, seems to be essential to improve the image annotation and in order to
narrow the semantic gap. In this dissertation, we are interested in semantic image
annotation. These approaches aim at improving the image annotation by the use of
images content and structured knowledge models about image semantics. This in-
volves ﬁrst to capture and to model suitable knowledge models about image context,
and subsequently to build eﬀective tools using these knowledge models in order to im-
prove the image annotation process. The overall goal remains to narrow the semantic
and sensory gaps using the available visual features of images and relevant knowledge
sources, ultimately to satiate the user. Speciﬁcally, our concerns in this dissertation
are as follows. Firstly, we address the problem of building explicit knowledge models
dedicated to image annotation. S

Chapter 2. State of the Art on Image Annotation
Indeed, the use of explicit semantic structures, such as semantic hierarchies and
ontologies, seems to be essential to improve the image annotation and in order to
narrow the semantic gap. In this dissertation, we are interested in semantic image
annotation. These approaches aim at improving the image annotation by the use of
images content and structured knowledge models about image semantics. This in-
volves ﬁrst to capture and to model suitable knowledge models about image context,
and subsequently to build eﬀective tools using these knowledge models in order to im-
prove the image annotation process. The overall goal remains to narrow the semantic
and sensory gaps using the available visual features of images and relevant knowledge
sources, ultimately to satiate the user. Speciﬁcally, our concerns in this dissertation
are as follows. Firstly, we address the problem of building explicit knowledge models
dedicated to image annotation. S

d in
Chapter 3 - Section 3.2.4, our standpoint is that a semantic hierarchy dedicated to
image annotation should take account of the visual information, the conceptual in-
formation and the contextual one. Consequently, we propose a new image-semantic
measure which allows estimating the semantic similarity between image concepts,
and which incorporates the aforementioned information in order to provide a mean-
ingful measure of image semantics.
Subsequently, a new methodology, based on
the previously proposed measure and on a set of eﬀective rules, is proposed in or-
der to automatically build semantic hierarchies suitable for image annotation. This
contribution is detailed in Chapter 3, and has served for the following publications
[Bannour and Hudelot, 2012a, Bannour and Hudelot, 2012b].
Thereafter, we propose to go further in the modeling of image-concepts relation-
ships, and consequently the modeling of image semantics. We propose therefore a
new approach for building an ontology

d in
Chapter 3 - Section 3.2.4, our standpoint is that a semantic hierarchy dedicated to
image annotation should take account of the visual information, the conceptual in-
formation and the contextual one. Consequently, we propose a new image-semantic
measure which allows estimating the semantic similarity between image concepts,
and which incorporates the aforementioned information in order to provide a mean-
ingful measure of image semantics.
Subsequently, a new methodology, based on
the previously proposed measure and on a set of eﬀective rules, is proposed in or-
der to automatically build semantic hierarchies suitable for image annotation. This
contribution is detailed in Chapter 3, and has served for the following publications
[Bannour and Hudelot, 2012a, Bannour and Hudelot, 2012b].
Thereafter, we propose to go further in the modeling of image-concepts relation-
ships, and consequently the modeling of image semantics. We propose therefore a
new approach for building an ontology

re.
In this dissertation, we address the problem of automatic image annotation from
the perspective of building and using explicit semantic models, such as semantic hier-
archies and ontologies. Our overall goal is to narrow the semantic gap and to achieve
a semantically consistent image annotation. Indeed, recent eﬀorts on knowledge mod-
eling and knowledge-driven approaches for image annotation have shown that it is
possible to reduce the semantic gap.
Our concern in this thesis was therefore to
demonstrate this assumption, and to show how it would be possible to use these
explicit and structured knowledge models to improve image annotation.
The remaining of this chapter is structured as follows. The ﬁrst part reviews the
diﬀerent contributions proposed in this PhD work and their signiﬁcance. Speciﬁcally,
we focus on how these contributions can improve existing systems for image anno-
tation and what issues could be answered/narrowed using the proposed knowledge
models. In the second

re.
In this dissertation, we address the problem of automatic image annotation from
the perspective of building and using explicit semantic models, such as semantic hier-
archies and ontologies. Our overall goal is to narrow the semantic gap and to achieve
a semantically consistent image annotation. Indeed, recent eﬀorts on knowledge mod-
eling and knowledge-driven approaches for image annotation have shown that it is
possible to reduce the semantic gap.
Our concern in this thesis was therefore to
demonstrate this assumption, and to show how it would be possible to use these
explicit and structured knowledge models to improve image annotation.
The remaining of this chapter is structured as follows. The ﬁrst part reviews the
diﬀerent contributions proposed in this PhD work and their signiﬁcance. Speciﬁcally,
we focus on how these contributions can improve existing systems for image anno-
tation and what issues could be answered/narrowed using the proposed knowledge
models. In the second


## Raw_Introduction


We study how to improve labeling efficiency as well as extensibility, so that an annotation system can be easily adapted to new tasks. In most use cases, there are only three basic types of labels on an image: image-level tagging, bounding box, and polygon annotation. However, the semantic meanings of the annotations can differ dramatically between use cases. Therefore, we build a configurable annotation system that supports these three types of annotations. Moreover, we also introduce improvements to boost labeling efficiency, as described below. We tested our system in annotating real-world videos while extending it to additional types of labels, including drivable area and lane marking annotations. At the same time, we also collected efficient full-frame semantic instance segmentations. Our study shows that we can extend our labeling system to new types of annotation with minimal effort while still being able to label large-scale datasets.

We study how to improve labeling efficiency as well as extensibility, so that an annotation system can be easily adapted to new tasks. In most use cases, there are only three basic types of labels on an image: image-level tagging, bounding box, and polygon annotation. However, the semantic meanings of the annotations can differ dramatically between use cases. Therefore, we build a configurable annotation system that supports these three types of annotations. Moreover, we also introduce improvements to boost labeling efficiency, as described below. We tested our system in annotating real-world videos while extending it to additional types of labels, including drivable area and lane marking annotations. At the same time, we also collected efficient full-frame semantic instance segmentations. Our study shows that we can extend our labeling system to new types of annotation with minimal effort while still being able to label large-scale datasets.