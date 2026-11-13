# Building and Using Knowledge Models for Semantic Image Annotation



## Raw_Full_Text


reduce the complexity of the large-scale image annotation problem.
In this thesis, we propose a new methodology for building and using structured
knowledge models for automatic image annotation. Speciﬁcally, our ﬁrst proposals
deal with the automatic building of explicit and structured knowledge models, such
as semantic hierarchies and multimedia ontologies, dedicated to image annotation.
Thereby, we propose a new approach for building semantic hierarchies faithful to
image semantics. Our approach is based on a new image-semantic similarity mea-
sure between concepts and on a set of rules that allow connecting the concepts with
higher relatedness till the building of the ﬁnal hierarchy. Afterwards, we propose
to go further in the modeling of image semantics through the building of explicit
knowledge models that incorporate richer semantic relationships between image con-
cepts. Therefore, we propose a new approach for automatically building multimedia
ontologies consisting of subsumpti

reduce the complexity of the large-scale image annotation problem.
In this thesis, we propose a new methodology for building and using structured
knowledge models for automatic image annotation. Speciﬁcally, our ﬁrst proposals
deal with the automatic building of explicit and structured knowledge models, such
as semantic hierarchies and multimedia ontologies, dedicated to image annotation.
Thereby, we propose a new approach for building semantic hierarchies faithful to
image semantics. Our approach is based on a new image-semantic similarity mea-
sure between concepts and on a set of rules that allow connecting the concepts with
higher relatedness till the building of the ﬁnal hierarchy. Afterwards, we propose
to go further in the modeling of image semantics through the building of explicit
knowledge models that incorporate richer semantic relationships between image con-
cepts. Therefore, we propose a new approach for automatically building multimedia
ontologies consisting of subsumpti

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

Chapter 1. Introduction
Annotations of 
Images 
Training Dataset 
Data Processing  
Information 
Analysis 
Building Structured 
Knowledge Models 
Commonsense 
Knowledge Base 
Figure 1.6: From image data to structured knowledge Models.
Workﬂow of our
approaches for building structured knowledge models dedicated to image annotation.
1.3.2
Using Structured Knowledge Models for Image Annota-
tion
In order to make an eﬃcient use of the built structured knowledge models, we propose
in this dissertation to investigate the contribution of: i) semantic hierarchies, and ii)
DL ontologies and ontological reasoning, for image annotation. The overall workﬂow
of our methods is illustrated in Figure 1.7. Given a set of previously unseen (unla-
beled) images and a structured knowledge model dedicated to image annotation, our
approach allows to predict the set of concepts from the annotation vocabulary that
are relevant with respect to the image content/semantics.
Image annotation 
Image Dataset 
Data

Chapter 1. Introduction
Annotations of 
Images 
Training Dataset 
Data Processing  
Information 
Analysis 
Building Structured 
Knowledge Models 
Commonsense 
Knowledge Base 
Figure 1.6: From image data to structured knowledge Models.
Workﬂow of our
approaches for building structured knowledge models dedicated to image annotation.
1.3.2
Using Structured Knowledge Models for Image Annota-
tion
In order to make an eﬃcient use of the built structured knowledge models, we propose
in this dissertation to investigate the contribution of: i) semantic hierarchies, and ii)
DL ontologies and ontological reasoning, for image annotation. The overall workﬂow
of our methods is illustrated in Figure 1.7. Given a set of previously unseen (unla-
beled) images and a structured knowledge model dedicated to image annotation, our
approach allows to predict the set of concepts from the annotation vocabulary that
are relevant with respect to the image content/semantics.
Image annotation 
Image Dataset 
Data

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

Abstract
This dissertation aims at building and using knowledge-driven models in order
to improve the accuracy of automatic image annotation.
Currently, many image
annotation approaches are based on the automatic association between low-level or
mid-level visual features and semantic concepts using machine learning techniques.
Nevertheless, the only use of machine learning seems to be insuﬃcient to bridge the
well-known semantic gap problem, and therefore to achieve eﬃcient systems for auto-
matic image annotation. Structured knowledge models, such as semantic hierarchies
and ontologies, appear to be a good way to improve such approaches. These semantic
structures allow modeling many valuable semantic relations between concepts, as for
instance subsumption, contextual and spatial relationships. Indeed, these relation-
ships have been proved to be of prime importance for the understanding of image
semantics. Moreover, such structured knowledge models about high-level concepts
enable to

Chapter 1. Introduction
for building knowledge models should be adopted and which should incorporate
the diﬀerent image modalities (e.g. visual, conceptual, contextual, spatial, etc.)
in order to be relevant with respect to image semantics.
• The building of these knowledge models should be performed automatically,
using data mining techniques, in order to reduce the scalability problem of
knowledge building and to achieve a consistent representation of image seman-
tics.
Consequently, the proposed contributions involve capturing and modeling suitable
knowledge models about the image semantics, and thereafter building eﬀective tools to
exploit this knowledge in order to improve the image annotation process. The overall
goal remains to narrow the semantic gap using the available visual features of images
and relevant domain knowledge in order to support the varied search categories,
ultimately to satiate the user expectations.
Speciﬁcally, we address the following
issues:
1. The buildin

Abstract
This dissertation aims at building and using knowledge-driven models in order
to improve the accuracy of automatic image annotation.
Currently, many image
annotation approaches are based on the automatic association between low-level or
mid-level visual features and semantic concepts using machine learning techniques.
Nevertheless, the only use of machine learning seems to be insuﬃcient to bridge the
well-known semantic gap problem, and therefore to achieve eﬃcient systems for auto-
matic image annotation. Structured knowledge models, such as semantic hierarchies
and ontologies, appear to be a good way to improve such approaches. These semantic
structures allow modeling many valuable semantic relations between concepts, as for
instance subsumption, contextual and spatial relationships. Indeed, these relation-
ships have been proved to be of prime importance for the understanding of image
semantics. Moreover, such structured knowledge models about high-level concepts
enable to

Chapter 1. Introduction
for building knowledge models should be adopted and which should incorporate
the diﬀerent image modalities (e.g. visual, conceptual, contextual, spatial, etc.)
in order to be relevant with respect to image semantics.
• The building of these knowledge models should be performed automatically,
using data mining techniques, in order to reduce the scalability problem of
knowledge building and to achieve a consistent representation of image seman-
tics.
Consequently, the proposed contributions involve capturing and modeling suitable
knowledge models about the image semantics, and thereafter building eﬀective tools to
exploit this knowledge in order to improve the image annotation process. The overall
goal remains to narrow the semantic gap using the available visual features of images
and relevant domain knowledge in order to support the varied search categories,
ultimately to satiate the user expectations.
Speciﬁcally, we address the following
issues:
1. The buildin

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

Chapter 4. Building Fuzzy Multimedia Ontologies for Image Annotation
Training Dataset 
Knowledge 
Discovery 
Building Explicit 
Knowledge 
Building Multimedia 
Ontologies 
Multimedia 
Ontology for Image 
Annotation 
Visual 
Annotations of 
Images 
Conceptual 
Commonsense 
Knowledge base 
Spatial 
Contextual 
RBox 
ABox 
Figure 4.1: From image data to structured knowledge models: Architecture of our
approach for building multimedia ontologies dedicated to image annotation.
ontology, which raises the problem of scalability of the building of these knowledge
structures.
In order to answer these speciﬁc limitations, we propose in this work to build our
ontology as a knowledge base that contains explicit and structured knowledge about
image context. So that the structure of our ontology is representative of the image
semantics, we propose to use a Semantico-Visual speciﬁcation (which incorporates
the visual and conceptual semantics of image concepts) for designing our ontology.
In addition,

Chapter 1. Introduction
1.3
Contributions
As aforementioned, the aims of this thesis are twofold. As a ﬁrst step, we have focused
our contributions on providing eﬀective tools for the automatic building of structured
and explicit knowledge models dedicated to image annotation. This is intended to
propose structured knowledge models that are relevant with respect to image seman-
tics. Subsequently, we have concentrated our contributions on the eﬀective use of
these knowledge models in order to improve image annotation. Our ﬁnal purpose is
to narrow the semantic gap, i.e. decrease the gap between the visual content of images
and their meaning (image semantics). The achieved contributions in this dissertation
are detailed in the following subsections.
1.3.1
Building Explicit and Structured Knowledge Models for
Image Annotation
Our ﬁrst contribution in this dissertation deals with the automatic building of se-
mantic hierarchies for the purpose of image annotation. Indeed, as it is detaile

Chapter 1. Introduction
1.3
Contributions
As aforementioned, the aims of this thesis are twofold. As a ﬁrst step, we have focused
our contributions on providing eﬀective tools for the automatic building of structured
and explicit knowledge models dedicated to image annotation. This is intended to
propose structured knowledge models that are relevant with respect to image seman-
tics. Subsequently, we have concentrated our contributions on the eﬀective use of
these knowledge models in order to improve image annotation. Our ﬁnal purpose is
to narrow the semantic gap, i.e. decrease the gap between the visual content of images
and their meaning (image semantics). The achieved contributions in this dissertation
are detailed in the following subsections.
1.3.1
Building Explicit and Structured Knowledge Models for
Image Annotation
Our ﬁrst contribution in this dissertation deals with the automatic building of se-
mantic hierarchies for the purpose of image annotation. Indeed, as it is detaile

Chapter 4. Building Fuzzy Multimedia Ontologies for Image Annotation
Training Dataset 
Knowledge 
Discovery 
Building Explicit 
Knowledge 
Building Multimedia 
Ontologies 
Multimedia 
Ontology for Image 
Annotation 
Visual 
Annotations of 
Images 
Conceptual 
Commonsense 
Knowledge base 
Spatial 
Contextual 
RBox 
ABox 
Figure 4.1: From image data to structured knowledge models: Architecture of our
approach for building multimedia ontologies dedicated to image annotation.
ontology, which raises the problem of scalability of the building of these knowledge
structures.
In order to answer these speciﬁc limitations, we propose in this work to build our
ontology as a knowledge base that contains explicit and structured knowledge about
image context. So that the structure of our ontology is representative of the image
semantics, we propose to use a Semantico-Visual speciﬁcation (which incorporates
the visual and conceptual semantics of image concepts) for designing our ontology.
In addition,

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

Chapter 1. Introduction
proposed to model and to use explicit knowledge about image context in order
to answer to the above mentioned problems, as for instance [Hollink et al., 2004,
Maillot et al., 2004,
Popescu et al., 2007,
Fan et al., 2008a,
Hudelot et al., 2008,
Tousch et al., 2008, Wu et al., 2008, Simou et al., 2008, Dasiopoulou et al., 2009,
Fan et al., 2009, Straccia, 2010, Li et al., 2010]. We refer to these approaches as se-
mantic image annotation, which can be deﬁned as the set of methods mainly
based on the use of explicit semantic structures, such as semantic hierarchies and on-
tologies, in order to narrow the semantic gap. However, semantic image annotation
approaches are currently facing the following shortcomings:
• The availability of knowledge structures modeling the image semantics, or failing
that, their building or their learning.
Indeed, currently there are a number
of available knowledge resources which have been used for image annotation,
like WordNet [Fellba

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

Chapter 1. Introduction
proposed to model and to use explicit knowledge about image context in order
to answer to the above mentioned problems, as for instance [Hollink et al., 2004,
Maillot et al., 2004,
Popescu et al., 2007,
Fan et al., 2008a,
Hudelot et al., 2008,
Tousch et al., 2008, Wu et al., 2008, Simou et al., 2008, Dasiopoulou et al., 2009,
Fan et al., 2009, Straccia, 2010, Li et al., 2010]. We refer to these approaches as se-
mantic image annotation, which can be deﬁned as the set of methods mainly
based on the use of explicit semantic structures, such as semantic hierarchies and on-
tologies, in order to narrow the semantic gap. However, semantic image annotation
approaches are currently facing the following shortcomings:
• The availability of knowledge structures modeling the image semantics, or failing
that, their building or their learning.
Indeed, currently there are a number
of available knowledge resources which have been used for image annotation,
like WordNet [Fellba

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

Chapter 7. Conclusions and Future Research Directions
7.1
Contributions and their Signiﬁcance
As aforementioned, the aims of this thesis are twofold.
As a ﬁrst step, we have
focused our contributions on providing eﬀective tools for the automatic building of
structured and explicit knowledge models dedicated to image annotation. This is
intended to propose knowledge models that are representative of image semantics,
and allow modeling image contexts in an accurate way. Subsequently, we have con-
centrated our contributions on the eﬀective use of this knowledge in order to achieve
a more accurate image annotation.
Our ﬁnal purpose is to narrow the semantic
gap, i.e. decrease the gap between the visual content of images and their meaning
(image semantics). Therefore, the achieved contributions in this dissertation can be
categorized in two main topics: 1) the automatic building of explicit and structured
multimedia knowledge models, 2) the use of structured knowledge models to improve
ima

Chapter 7. Conclusions and Future Research Directions
7.1
Contributions and their Signiﬁcance
As aforementioned, the aims of this thesis are twofold.
As a ﬁrst step, we have
focused our contributions on providing eﬀective tools for the automatic building of
structured and explicit knowledge models dedicated to image annotation. This is
intended to propose knowledge models that are representative of image semantics,
and allow modeling image contexts in an accurate way. Subsequently, we have con-
centrated our contributions on the eﬀective use of this knowledge in order to achieve
a more accurate image annotation.
Our ﬁnal purpose is to narrow the semantic
gap, i.e. decrease the gap between the visual content of images and their meaning
(image semantics). Therefore, the achieved contributions in this dissertation can be
categorized in two main topics: 1) the automatic building of explicit and structured
multimedia knowledge models, 2) the use of structured knowledge models to improve
ima

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

Chapter 4. Building Fuzzy Multimedia Ontologies for Image Annotation
4.1
Introduction
In Chapter 3, we have proposed a new method for building semantic hierarchies suit-
able for image annotation. As aforementioned, semantic hierarchies enable only the
description of the subsumption relationships between concepts, which is actually in-
suﬃcient for modeling the rich semantics of multimedia content and reasoning about
it. Indeed, more sophisticated knowledge structures, i.e. richer in terms of semantic
relationships, are required in order to deal with big data currently available every-
where, and in order to provide eﬃcient systems for storing, indexing and retrieving
in this amount of data while satisfying semantic user expectations.
This chapter proposes an approach to build an ontology of spatial and contextual
information suitable for reasoning about the coherence of image annotation. Our ap-
proach uses ﬁrstly the visual and conceptual information in order to build a semantic
hier

Chapter 4. Building Fuzzy Multimedia Ontologies for Image Annotation
4.1
Introduction
In Chapter 3, we have proposed a new method for building semantic hierarchies suit-
able for image annotation. As aforementioned, semantic hierarchies enable only the
description of the subsumption relationships between concepts, which is actually in-
suﬃcient for modeling the rich semantics of multimedia content and reasoning about
it. Indeed, more sophisticated knowledge structures, i.e. richer in terms of semantic
relationships, are required in order to deal with big data currently available every-
where, and in order to provide eﬃcient systems for storing, indexing and retrieving
in this amount of data while satisfying semantic user expectations.
This chapter proposes an approach to build an ontology of spatial and contextual
information suitable for reasoning about the coherence of image annotation. Our ap-
proach uses ﬁrstly the visual and conceptual information in order to build a semantic
hier

that motivated our contributions. These issues will be discussed deeply
in the diﬀerent chapters of this dissertation.
• Existing knowledge models used for image annotation are based either on a
visual or textual speciﬁcation (e.g. based on WordNet). However, these knowl-
edge models, are they representative enough of image semantics? Would we not
need a more elaborated speciﬁcation (for example, by combining visual and
textual speciﬁcation) for modeling the image semantics?
• Ontology-driven approaches seem promising for narrowing the semantic gap.
However, knowledge representation in these models is a hard task9 and faces a
major scalability problem. Therefore, should we not rather focus on providing
methods that allow building ontologies (HWO, LWO or formal ontologies) in
automatic manner in order to scale with a large number of concepts?
• Currently, concept hierarchies (and respectively visual taxonomies) are the most
widely explored for semantic image annotation. These, constrai

that motivated our contributions. These issues will be discussed deeply
in the diﬀerent chapters of this dissertation.
• Existing knowledge models used for image annotation are based either on a
visual or textual speciﬁcation (e.g. based on WordNet). However, these knowl-
edge models, are they representative enough of image semantics? Would we not
need a more elaborated speciﬁcation (for example, by combining visual and
textual speciﬁcation) for modeling the image semantics?
• Ontology-driven approaches seem promising for narrowing the semantic gap.
However, knowledge representation in these models is a hard task9 and faces a
major scalability problem. Therefore, should we not rather focus on providing
methods that allow building ontologies (HWO, LWO or formal ontologies) in
automatic manner in order to scale with a large number of concepts?
• Currently, concept hierarchies (and respectively visual taxonomies) are the most
widely explored for semantic image annotation. These, constrai

Chapter 6. Multi-Stage Reasoning Framework for Image Annotation
annotation/interpretation, and they are usually limited to use hand-built knowledge
models. Moreover, they propose reasoning scenarios to deal with the problem of im-
ages annotation, but these scenarios are not tested on real data applications, and
consequently their eﬀectiveness is not assessed. However, this application domain,
i.e. knowledge-driven approaches for image annotation, is still in its infancy and we
believe that these approaches will be eﬀectively improved in the near future.
In this dissertation, we proposed a tentative to reduce the above limitations of
current approaches, i.e.:
1. Building multimedia ontologies dedicated to image annotation (proposed in
Chapter 4). Our approach rely on mining image databases in order to achieve
a representative knowledge base of image semantics (and respectively of a given
application domain).
2. The use of the reasoning power of ontologies in order to produce a semantic

of spatial and contextual information suit-
able for reasoning about the consistency of image annotation. Our approach uses
visual and conceptual information in order to build a semantic hierarchy that will
serve as a backbone of our ontology. Contextual and spatial information about im-
age concepts are afterwards incorporated in the ontology in order to model richer
semantic relationships between these concepts. Fuzzy description logics are used as
a formalism to represent our ontology and the inherent uncertainty and imprecision
of this kind of information. This work is the subject of Chapter 4, and is published
in [Bannour and Hudelot, 2013a].
Figure 1.6, illustrates the general workﬂow of the proposed approaches for building
structured knowledge models dedicated to image annotation.
11