# Hierarchical image annotation using semantic hierarchies



## Resume


Hierarchical image annotation using semantic hierarchies

Semantic hierarchies have been introduced recently to improve image annotation. They was used as a framework for hierarchical image classification, and thus to improve classifiers accuracy and reduce the complexity of managing large scale data. In this paper, we investigate the contribution of semantic hierarchies for hierarchical image classification. We propose first a new method based on the hierarchy structure to train efficiently hierarchical classifiers. Our method, named One-Versus-Opposite-Nodes, allows decomposing the problem in several independent tasks and therefore scales well with large database. We also propose two methods for computing a hierarchical decision function that serves to annotate new image samples. The former is performed by a top-down classifiers voting, while the second is based on a bottom-up score fusion. The experiments on Pascal VOC'2010 dataset showed that our methods improve well the image annotation results.


## Raw_Full_Text


Chapter 5. Hierarchical Image Classiﬁcation using Semantic Hierarchies
5.1
Introduction
As introduced in Chapter 3, semantic hierarchies have been introduced recently to
improve image annotation. They were mostly used as a framework for hierarchical
image classiﬁcation, and thus to improve the classiﬁers accuracy and to reduce the
complexity of managing large scale data.
This chapter aims primarily to experimentally validate the proposed approach in
Chapter 3, which allows building semantic hierarchies dedicated to image annotation.
We propose therefore to investigate the contribution of semantic hierarchies, and
speciﬁcally our proposed approach for building hierarchies, for hierarchical image
classiﬁcation. Thus, we propose ﬁrst a method based on the hierarchy structure to
train eﬃciently hierarchical classiﬁers. Our method, named One-Versus-Opposite-
Nodes, allows decomposing the problem into several independent tasks and therefore
scales well with large databases.
We also propose t

Chapter 5. Hierarchical Image Classiﬁcation using Semantic Hierarchies
5.1
Introduction
As introduced in Chapter 3, semantic hierarchies have been introduced recently to
improve image annotation. They were mostly used as a framework for hierarchical
image classiﬁcation, and thus to improve the classiﬁers accuracy and to reduce the
complexity of managing large scale data.
This chapter aims primarily to experimentally validate the proposed approach in
Chapter 3, which allows building semantic hierarchies dedicated to image annotation.
We propose therefore to investigate the contribution of semantic hierarchies, and
speciﬁcally our proposed approach for building hierarchies, for hierarchical image
classiﬁcation. Thus, we propose ﬁrst a method based on the hierarchy structure to
train eﬃciently hierarchical classiﬁers. Our method, named One-Versus-Opposite-
Nodes, allows decomposing the problem into several independent tasks and therefore
scales well with large databases.
We also propose t

classes). Recently, many approaches have proposed to use semantic hierarchies
in order to improve image annotation. These hierarchies was used as a framework
for hierarchical image classiﬁcation, and thus to improve classiﬁers accuracy and to
reduce the complexity of managing large scale data. In this dissertation, we inves-
tigated the contribution of semantic hierarchies for hierarchical image classiﬁcation.
We proposed therefore a new method based on the hierarchy structure to train
eﬃciently hierarchical classiﬁers. Our method, named One-Versus-Opposite-Nodes,
allows decomposing the problem into several independent tasks and therefore it
scales well with large databases. We also proposed two methods for computing a
hierarchical decision function that served to annotate new image samples. The former
was performed using a top-down classiﬁers voting, while the second was based on a
bottom-up score fusion [Bannour and Hudelot, 2012c, Bannour and Hudelot, 2013b].
Signiﬁcance:
⇒Previous

classes). Recently, many approaches have proposed to use semantic hierarchies
in order to improve image annotation. These hierarchies was used as a framework
for hierarchical image classiﬁcation, and thus to improve classiﬁers accuracy and to
reduce the complexity of managing large scale data. In this dissertation, we inves-
tigated the contribution of semantic hierarchies for hierarchical image classiﬁcation.
We proposed therefore a new method based on the hierarchy structure to train
eﬃciently hierarchical classiﬁers. Our method, named One-Versus-Opposite-Nodes,
allows decomposing the problem into several independent tasks and therefore it
scales well with large databases. We also proposed two methods for computing a
hierarchical decision function that served to annotate new image samples. The former
was performed using a top-down classiﬁers voting, while the second was based on a
bottom-up score fusion [Bannour and Hudelot, 2012c, Bannour and Hudelot, 2013b].
Signiﬁcance:
⇒Previous

on relationships between image concepts, and also
other semantic relationships such as contextual and spatial relations. Fuzzy descrip-
tion logics are used as a formalism to represent our ontology and to deal with the
uncertainty and the imprecision of concept relationships.
In order to assess the eﬀectiveness of the built structured knowledge models, we
propose subsequently to use them in a framework for image annotation. We propose
therefore an approach, based on the structure of semantic hierarchies, to eﬀectively
perform hierarchical image classiﬁcation. Furthermore, we propose a generic approach
for image annotation combining machine learning techniques, such as hierarchical im-
age classiﬁcation, and fuzzy ontological-reasoning in order to achieve a semantically
relevant image annotation. Empirical evaluations of our approaches have shown sig-
niﬁcant improvement in the image annotation accuracy.
Keywords:
Automatic Image Annotation, Hierarchical Image Classiﬁcation, Multimedia

on relationships between image concepts, and also
other semantic relationships such as contextual and spatial relations. Fuzzy descrip-
tion logics are used as a formalism to represent our ontology and to deal with the
uncertainty and the imprecision of concept relationships.
In order to assess the eﬀectiveness of the built structured knowledge models, we
propose subsequently to use them in a framework for image annotation. We propose
therefore an approach, based on the structure of semantic hierarchies, to eﬀectively
perform hierarchical image classiﬁcation. Furthermore, we propose a generic approach
for image annotation combining machine learning techniques, such as hierarchical im-
age classiﬁcation, and fuzzy ontological-reasoning in order to achieve a semantically
relevant image annotation. Empirical evaluations of our approaches have shown sig-
niﬁcant improvement in the image annotation accuracy.
Keywords:
Automatic Image Annotation, Hierarchical Image Classiﬁcation, Multimedia

rieve valuable information about image context, and how to perform reasoning
using multimedia ontologies in order to reduce the uncertainty about image annota-
tions. We therefore propose to automatically build multimedia ontologies by mining
image databases to gather valuable information about image context. Thus, we show
that ontologies are not necessarily limited to be deﬁned by humans, as it was the case
for most of existing approaches in the multimedia domain. Thereby, we reduce the
scalability problem of ontology building.
In Chapter 5, we explore the contribution of semantic hierarchies for image an-
notation. A natural way to use semantic hierarchies is to operate within a framework
for hierarchical image classiﬁcation. Consequently, we propose a new approach based
on the semantic hierarchy structure to eﬃciently train the hierarchical classiﬁers, and
for computing an accurate hierarchical decision function which is thereafter used to
annotate previously unseen images.
In Chapt

rieve valuable information about image context, and how to perform reasoning
using multimedia ontologies in order to reduce the uncertainty about image annota-
tions. We therefore propose to automatically build multimedia ontologies by mining
image databases to gather valuable information about image context. Thus, we show
that ontologies are not necessarily limited to be deﬁned by humans, as it was the case
for most of existing approaches in the multimedia domain. Thereby, we reduce the
scalability problem of ontology building.
In Chapter 5, we explore the contribution of semantic hierarchies for image an-
notation. A natural way to use semantic hierarchies is to operate within a framework
for hierarchical image classiﬁcation. Consequently, we propose a new approach based
on the semantic hierarchy structure to eﬃciently train the hierarchical classiﬁers, and
for computing an accurate hierarchical decision function which is thereafter used to
annotate previously unseen images.
In Chapt

Chapter 3. Building Semantic Hierarchies Faithful to Image Semantics
3.2
Motivation for Using Semantic Hierarchies
As stated in Chapter 2, current approaches for automatic image annotation face sig-
niﬁcant problems to narrow the semantic gap. Indeed, these approaches allow to
adequately describe the visual content of images but are unable to extract image
semantics like humans do, i.e. they are limited to describe the perceptual manifesta-
tion of image semantics. Moreover, they are subject to the scalability problem when
dealing with broad content image databases [Liu et al., 2007, Deng et al., 2010].
A new trend to overcome the aforementioned problems is to use explicit semantic
structures, such as semantic hierarchies and ontologies. Speciﬁcally, semantic hier-
archies have shown to be very useful to narrow the semantic gap [Deng et al., 2010].
In particular, they provide a hierarchical semantic structure for image concepts that
can be used as a framework for image classiﬁcation. T

Chapter 3. Building Semantic Hierarchies Faithful to Image Semantics
3.2
Motivation for Using Semantic Hierarchies
As stated in Chapter 2, current approaches for automatic image annotation face sig-
niﬁcant problems to narrow the semantic gap. Indeed, these approaches allow to
adequately describe the visual content of images but are unable to extract image
semantics like humans do, i.e. they are limited to describe the perceptual manifesta-
tion of image semantics. Moreover, they are subject to the scalability problem when
dealing with broad content image databases [Liu et al., 2007, Deng et al., 2010].
A new trend to overcome the aforementioned problems is to use explicit semantic
structures, such as semantic hierarchies and ontologies. Speciﬁcally, semantic hier-
archies have shown to be very useful to narrow the semantic gap [Deng et al., 2010].
In particular, they provide a hierarchical semantic structure for image concepts that
can be used as a framework for image classiﬁcation. T

Processing  
Information 
Analysis 
Knowledge Driven Framework 
Image annotation 
Figure 1.7: Using structured knowledge models for image annotation.
We propose therefore a new methodology, based on the structure of semantic
hierarchies, to eﬃciently train hierarchical classiﬁers.
Our method allows decom-
posing the problem into several independent tasks and therefore it scales well with
large databases.
We also propose two methods for computing a hierarchical de-
cision function that serves to annotate new image samples.
The former is per-
formed using a top-down classiﬁers voting, while the second is based on a bottom-
12

Chapter 5. Hierarchical Image Classiﬁcation using Semantic Hierarchies
explored until reaching leaf concepts. Several paths in the hierarchy can be simultane-
ously explored, and thus a test image can be associated to many classes as illustrated
in Figure 5.6. For a given test image, if none of the leaf nodes of the explored paths
is reached, then the image is annotated with the leaf concept having the higher con-
ﬁdence value.
Algorithm 2: Top-Down Classiﬁers Voting method
Input:
SH: a semantic hierarchy,
ii: a test image,
xv
i : a visual representation of the image ii,
{Gcl(xv)}: the set of decision functions of the classiﬁers of concepts
cl ∈{C ∪C′}.
Result:
Ai = {cj | cj ∈{C ∪C′}, j ≥0}: predicted annotation for the image ii.
begin
Ai ←∅
Ω←{ cj | ∀cj ⊑⊤, ∄ck s.t. cj ⊑ck, ck ⊑⊤}
// (i.e., Ω←immediate children concepts of ⊤)
while (|Ω| ≥1) do
Υ ←∅
foreach (cl ∈Ω) do
if (Gcl(xv
i ) > 0) then
Υ ←Υ + cl
end
end
if (|Υ| = 0) then
Υ ←argmax
cl∈Ω
Gcl(xv
i )
end
Ai ←Ai ∪Υ
Ω←{ cj | ∀cl ∈Υ, c

Chapter 5. Hierarchical Image Classiﬁcation using Semantic Hierarchies
explored until reaching leaf concepts. Several paths in the hierarchy can be simultane-
ously explored, and thus a test image can be associated to many classes as illustrated
in Figure 5.6. For a given test image, if none of the leaf nodes of the explored paths
is reached, then the image is annotated with the leaf concept having the higher con-
ﬁdence value.
Algorithm 2: Top-Down Classiﬁers Voting method
Input:
SH: a semantic hierarchy,
ii: a test image,
xv
i : a visual representation of the image ii,
{Gcl(xv)}: the set of decision functions of the classiﬁers of concepts
cl ∈{C ∪C′}.
Result:
Ai = {cj | cj ∈{C ∪C′}, j ≥0}: predicted annotation for the image ii.
begin
Ai ←∅
Ω←{ cj | ∀cj ⊑⊤, ∄ck s.t. cj ⊑ck, ck ⊑⊤}
// (i.e., Ω←immediate children concepts of ⊤)
while (|Ω| ≥1) do
Υ ←∅
foreach (cl ∈Ω) do
if (Gcl(xv
i ) > 0) then
Υ ←Υ + cl
end
end
if (|Υ| = 0) then
Υ ←argmax
cl∈Ω
Gcl(xv
i )
end
Ai ←Ai ∪Υ
Ω←{ cj | ∀cl ∈Υ, c

Processing  
Information 
Analysis 
Knowledge Driven Framework 
Image annotation 
Figure 1.7: Using structured knowledge models for image annotation.
We propose therefore a new methodology, based on the structure of semantic
hierarchies, to eﬃciently train hierarchical classiﬁers.
Our method allows decom-
posing the problem into several independent tasks and therefore it scales well with
large databases.
We also propose two methods for computing a hierarchical de-
cision function that serves to annotate new image samples.
The former is per-
formed using a top-down classiﬁers voting, while the second is based on a bottom-
12

ics include: image retrieval, automatic im-
age annotation, hierarchical image classiﬁcation and knowledge-driven approaches for
image annotation. We also propose a thorough discussion of the related work in our
contribution chapters, so as to put our proposals into perspective.
The main contributions of this dissertation start with Chapter 3. Indeed, we
propose in Chapter 3 a new approach for building semantic hierarchies suitable for
image annotation. Our approach takes advantages of the diﬀerent image modalities to
compute an image-semantic measure between the diﬀerent concepts of the annotation
vocabulary. This measure is thereafter used to connect the concepts with a higher
semantic relatedness till the building of the ﬁnal hierarchy.
Chapter 4 proposes to go further in the use of structured knowledge models for
image annotation. Speciﬁcally, we address the following issues: how to extract and
store knowledge about image context in an eﬀective way, how to query the ontology
to ret

h for hierarchical image classiﬁcation using
semantic hierarchies. Our approach is based on the structure of the semantic hierar-
chy to eﬃciently train hierarchical classiﬁers, i.e. draws beneﬁts from the hierarchy
structure to decompose the training process into several independent and comple-
mentary sub-tasks. Thus, it allows to gain in eﬃciency and in complexity as it was
shown by the obtained results. We have also proposed two methods for computing
a hierarchical decision function serving to annotate previously unseen images. The
former is achieved by a top-down classiﬁers voting, while the second is based on a
bottom-up score fusion. Compared to other approaches, our methods have achieved
higher accuracy on Pascal VOC’2010 dataset. Speciﬁcally, the bottom-up score fu-
sion has shown signiﬁcant improvement in the classiﬁcation accuracy, as it allows
to reduce the inconsistency about classiﬁer decisions by the fusion of scores of the
classiﬁers belonging to a same path in the hier

ics include: image retrieval, automatic im-
age annotation, hierarchical image classiﬁcation and knowledge-driven approaches for
image annotation. We also propose a thorough discussion of the related work in our
contribution chapters, so as to put our proposals into perspective.
The main contributions of this dissertation start with Chapter 3. Indeed, we
propose in Chapter 3 a new approach for building semantic hierarchies suitable for
image annotation. Our approach takes advantages of the diﬀerent image modalities to
compute an image-semantic measure between the diﬀerent concepts of the annotation
vocabulary. This measure is thereafter used to connect the concepts with a higher
semantic relatedness till the building of the ﬁnal hierarchy.
Chapter 4 proposes to go further in the use of structured knowledge models for
image annotation. Speciﬁcally, we address the following issues: how to extract and
store knowledge about image context in an eﬀective way, how to query the ontology
to ret

h for hierarchical image classiﬁcation using
semantic hierarchies. Our approach is based on the structure of the semantic hierar-
chy to eﬃciently train hierarchical classiﬁers, i.e. draws beneﬁts from the hierarchy
structure to decompose the training process into several independent and comple-
mentary sub-tasks. Thus, it allows to gain in eﬃciency and in complexity as it was
shown by the obtained results. We have also proposed two methods for computing
a hierarchical decision function serving to annotate previously unseen images. The
former is achieved by a top-down classiﬁers voting, while the second is based on a
bottom-up score fusion. Compared to other approaches, our methods have achieved
higher accuracy on Pascal VOC’2010 dataset. Speciﬁcally, the bottom-up score fu-
sion has shown signiﬁcant improvement in the classiﬁcation accuracy, as it allows
to reduce the inconsistency about classiﬁer decisions by the fusion of scores of the
classiﬁers belonging to a same path in the hier

Chapter 3. Building Semantic Hierarchies Faithful to Image Semantics
Shen and Fan, 2010]. [Fan et al., 2008a] proposed an approach for hierarchical con-
cept learning, by incorporating concept ontology and multi-task learning in order
to exploit the strong inter-concept correlations. [Li et al., 2010] proposed a method
based on visual features and image tags to automatically build a ’semantivisual’ image
hierarchy.
To summarize, semantic hierarchies seem to have great potentials to improve the
image annotation, mostly through their explicit representation of concepts relation-
ships which may help understanding image semantics. However, to our knowledge,
none of the existing approaches have used the reasoning power of these hierarchies
in this context. Most of the proposals have focused on the problem of hierarchies
building, or have proposed to use them as a hierarchical framework for image classi-
ﬁcation.
3.2.4
Discussion
As we have seen in the previous sections, many approaches hav

elle, conceptuelle, et contextuelle pour la construction automa-
tique de hiérarchies sémantiques adaptées à l’annotation d’images. In Actes de
la conférence Reconnaissance des Formes et Intelligence Artiﬁcielle (RFIA 2012),
pages 462–469, Lyon, France.
[Bannour and Hudelot, 2012c] Bannour, H. and Hudelot, C. (2012c). Hierarchical
image annotation using semantic hierarchies.
In Proceedings of the 21st ACM
International Conference on Information and Knowledge Management (CIKM’12),
pages 2431–2434.
[Bannour and Hudelot, 2013a] Bannour, H. and Hudelot, C. (2013a). Building and
using fuzzy multimedia ontologies for semantic image annotation.
Multimedia
Tools and Applications (MTAP’13), pages 1–35. http://dx.doi.org/10.1007/
s11042-013-1491-z.
[Bannour and Hudelot, 2013b] Bannour, H. and Hudelot, C. (2013b). Construction
de hiérarchies sémantiques pour l’annotation d’images. Revue d’Intelligence Arti-
ﬁcielle (RIA’13), 27(1):11–37.
[Barnard et al., 2003] Barnard, K., Duygulu, P., Forsyth, D

elle, conceptuelle, et contextuelle pour la construction automa-
tique de hiérarchies sémantiques adaptées à l’annotation d’images. In Actes de
la conférence Reconnaissance des Formes et Intelligence Artiﬁcielle (RFIA 2012),
pages 462–469, Lyon, France.
[Bannour and Hudelot, 2012c] Bannour, H. and Hudelot, C. (2012c). Hierarchical
image annotation using semantic hierarchies.
In Proceedings of the 21st ACM
International Conference on Information and Knowledge Management (CIKM’12),
pages 2431–2434.
[Bannour and Hudelot, 2013a] Bannour, H. and Hudelot, C. (2013a). Building and
using fuzzy multimedia ontologies for semantic image annotation.
Multimedia
Tools and Applications (MTAP’13), pages 1–35. http://dx.doi.org/10.1007/
s11042-013-1491-z.
[Bannour and Hudelot, 2013b] Bannour, H. and Hudelot, C. (2013b). Construction
de hiérarchies sémantiques pour l’annotation d’images. Revue d’Intelligence Arti-
ﬁcielle (RIA’13), 27(1):11–37.
[Barnard et al., 2003] Barnard, K., Duygulu, P., Forsyth, D

Chapter 3. Building Semantic Hierarchies Faithful to Image Semantics
Shen and Fan, 2010]. [Fan et al., 2008a] proposed an approach for hierarchical con-
cept learning, by incorporating concept ontology and multi-task learning in order
to exploit the strong inter-concept correlations. [Li et al., 2010] proposed a method
based on visual features and image tags to automatically build a ’semantivisual’ image
hierarchy.
To summarize, semantic hierarchies seem to have great potentials to improve the
image annotation, mostly through their explicit representation of concepts relation-
ships which may help understanding image semantics. However, to our knowledge,
none of the existing approaches have used the reasoning power of these hierarchies
in this context. Most of the proposals have focused on the problem of hierarchies
building, or have proposed to use them as a hierarchical framework for image classi-
ﬁcation.
3.2.4
Discussion
As we have seen in the previous sections, many approaches hav

Chapter 5. Hierarchical Image Classiﬁcation using Semantic Hierarchies
Target concept  
Sheep 
Horse 
Cow 
Bovid 
Cat 
Dog 
Carnivore 
Bird 
Vertebrate 
Positive samples 
Negatives samples 
Figure 5.4:
Proposed method for training hierarchical classiﬁers:
One-Versus-
Opposite-Nodes (OVON).
Problem Formalization.
In a formal way, given:
• DB, an image database consisting of a set of pairs ⟨image/textual annotation⟩,
i.e. DB = {[i1, A1], [i2, A2], · · · , [iL, AL]}, where:
– I = ⟨i1, i2, · · · , iL⟩is the set of all images in DB,
– L is the number of images in the database.
– C = ⟨c1, c2, · · · , cN⟩is the annotation vocabulary used for annotating im-
ages in I,
– N is the size of the annotation vocabulary.
– Ai is a textual annotation consisting of a set of concepts {cj ∈C, j = 1..nii}
associated with a given image ii ∈DB.
• SH, a semantic hierarchy consisting of a set of |C| + |C′| concepts, such that
C ⊆C′ and {C ∪C′} ⊆SH,.
Our objective is to train a set of (|C ∪C′| −1) classiﬁers, w

..nii}
associated with a given image ii ∈DB.
• CO, a generic commonsense ontology containing N ′ concepts (C ), such that
C ⊆C . For this work, we used WordNet as a commonsense ontology.
Our objective is to build a semantic hierarchy (SH), consisting of a set of |C|+|C′|
concepts (s.t. C ∪C′ ⊆C , and C′ could be probably the empty set), dedicated to this
speciﬁc annotation problem, i.e. dependent on the initial annotation vocabulary. The
built semantic hierarchy should consider the previously deﬁned assumptions 1. The
proposed approach consists therefore in identifying C′ new concepts that link (and
subsume) all the concepts of C in a hierarchical structure that accurately represents
image semantics. Figure 3.5 illustrates the architecture of our approach for building
semantic hierarchies dedicated to image annotation.
64

Chapter 5. Hierarchical Image Classiﬁcation using Semantic Hierarchies
Target concept  
Sheep 
Horse 
Cow 
Bovid 
Cat 
Dog 
Carnivore 
Bird 
Vertebrate 
Positive samples 
Negatives samples 
Figure 5.4:
Proposed method for training hierarchical classiﬁers:
One-Versus-
Opposite-Nodes (OVON).
Problem Formalization.
In a formal way, given:
• DB, an image database consisting of a set of pairs ⟨image/textual annotation⟩,
i.e. DB = {[i1, A1], [i2, A2], · · · , [iL, AL]}, where:
– I = ⟨i1, i2, · · · , iL⟩is the set of all images in DB,
– L is the number of images in the database.
– C = ⟨c1, c2, · · · , cN⟩is the annotation vocabulary used for annotating im-
ages in I,
– N is the size of the annotation vocabulary.
– Ai is a textual annotation consisting of a set of concepts {cj ∈C, j = 1..nii}
associated with a given image ii ∈DB.
• SH, a semantic hierarchy consisting of a set of |C| + |C′| concepts, such that
C ⊆C′ and {C ∪C′} ⊆SH,.
Our objective is to train a set of (|C ∪C′| −1) classiﬁers, w

..nii}
associated with a given image ii ∈DB.
• CO, a generic commonsense ontology containing N ′ concepts (C ), such that
C ⊆C . For this work, we used WordNet as a commonsense ontology.
Our objective is to build a semantic hierarchy (SH), consisting of a set of |C|+|C′|
concepts (s.t. C ∪C′ ⊆C , and C′ could be probably the empty set), dedicated to this
speciﬁc annotation problem, i.e. dependent on the initial annotation vocabulary. The
built semantic hierarchy should consider the previously deﬁned assumptions 1. The
proposed approach consists therefore in identifying C′ new concepts that link (and
subsume) all the concepts of C in a hierarchical structure that accurately represents
image semantics. Figure 3.5 illustrates the architecture of our approach for building
semantic hierarchies dedicated to image annotation.
64

hey also can be used as a
formal framework for reasoning about the consistency of image annotation, and thus
for reducing the uncertainty introduced by machine learning algorithms.
Several approaches have been proposed to use, or also to build, semantic hier-
archies in order to improve image annotation. As introduced in Chapter 2, these
approaches can be mainly categorized in three:
1. Language-based
hierarchies:
based
on
textual
information1,2
[Wei and Ngo, 2007, Marszalek and Schmid, 2007, Torralba et al., 2008],
2. Visual
hierarchies
(called
also
visual
taxonomies):
based
on
low-
level image features [Marszalek and Schmid, 2008, Griﬃn and Perona, 2008,
Sivic et al., 2008, Bart et al., 2008], and
3. Semantic hierarchies: based on both textual and visual features [Li et al., 2010,
Fan et al., 2007].
3.2.1
Language-Based Hierarchies
Language-based hierarchies are concept hierarchies built using only conceptual infor-
mation, i.e. based on a similarity measure between concepts calculat

hey also can be used as a
formal framework for reasoning about the consistency of image annotation, and thus
for reducing the uncertainty introduced by machine learning algorithms.
Several approaches have been proposed to use, or also to build, semantic hier-
archies in order to improve image annotation. As introduced in Chapter 2, these
approaches can be mainly categorized in three:
1. Language-based
hierarchies:
based
on
textual
information1,2
[Wei and Ngo, 2007, Marszalek and Schmid, 2007, Torralba et al., 2008],
2. Visual
hierarchies
(called
also
visual
taxonomies):
based
on
low-
level image features [Marszalek and Schmid, 2008, Griﬃn and Perona, 2008,
Sivic et al., 2008, Bart et al., 2008], and
3. Semantic hierarchies: based on both textual and visual features [Li et al., 2010,
Fan et al., 2007].
3.2.1
Language-Based Hierarchies
Language-based hierarchies are concept hierarchies built using only conceptual infor-
mation, i.e. based on a similarity measure between concepts calculat


## Quote


Semantic Annotation of Image Resources in Digital Humanities