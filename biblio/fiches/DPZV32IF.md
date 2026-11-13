# Quality Assured: Rethinking Annotation Strategies in Imaging AI



## Resume


Quality Assured: Rethinking Annotation Strategies in Imaging AI

AbstractThis paper does not describe a novel method. Instead, it studies an essential foundation for reliable benchmarking and ultimately real-world application of AI-based image analysis: generating high-quality reference annotations. Previous research has focused on crowdsourcing as a means of outsourcing annotations. However, little attention has so far been given to annotation companies, specifically regarding their internal quality assurance (QA) processes. Therefore, our aim is to evaluate the influence of QA employed by annotation companies on annotation quality and devise methodologies for maximizing data annotation efficacy. Based on a total of 57,648 instance segmented images obtained from a total of 924 annotators and 34 QA workers from four annotation companies and Amazon Mechanical Turk (MTurk), we derived the following insights: (1) Annotation companies perform better both in terms of quantity and quality compared to the widely used platform MTurk

Speeding up scientific imaging workflows: Design of automated image annotation tool

Deep Active Re-Labeling: Toward Noise-Resilient Annotation Efficiency

Towards a better understanding of annotation tools for medical imaging: a survey

Active learning based image annotation

Annotating Medical Image Data

A New Framework to Reduce Doctor&#x2019;s Workload for Medical Image Annotation

Accurate annotation of the medical image is the crucial step for image artificial intelligence (AI) clinical application. However, annotating medical image will incur a lot of annotation efforts and expense due to its high complexity and needing experienced doctors. In order to reduce the cost of annotation, several active learning methods have been proposed previously. However, the focus of these methods is to reduce the number of annotation candidates with little regard for doctor&#x2019;s workload, which is not enough for medical image annotation, since even annotating a small amount of data will take a lot of time for doctors. In order to effectively reduce the workload of doctors, we developed a new framework for medical image annotation. First, by combining active learning and U-shape network, we employed a suggestive annotation strategy to select the most effective annotation candidates. We then exploited a fine annotation platform to alleviate annotating efforts on each candida

An Interactive Annotation Method Based on Incremental Learning

Automatic Image Annotation Using Convex Deep Learning Models

Rethinking Crowdsourcing Annotation: Partial Annotation with Salient Labels for Multi-Label Image Classification

Annotated images are required for both supervised model training and evaluation in image classification. Manually annotating images is arduous and expensive, especially for multi-labeled images. A recent trend for conducting such laboursome annotation tasks is through crowdsourcing, where images are annotated by volunteers or paid workers online (e.g., workers of Amazon Mechanical Turk) from scratch. However, the quality of crowdsourcing image annotations cannot be guaranteed, and incompleteness and incorrectness are two major concerns for crowdsourcing annotations. To address such concerns, we have a rethinking of crowdsourcing annotations: Our simple hypothesis is that if the annotators only partially annotate multi-label images with salient labels they are confident in, there will be fewer annotation errors and annotators will spend less time on uncertain labels. As a pleasant surprise, with the same annotation budget, we show a multi-label image classifier supervised by images with

Partition sampling: an active learning selection strategy for large database annotation

AI-Enhanced Annotation Tool for Aneurysm Medical Image Labeling

Effective image annotation via active learning

Efficient annotation of image data sets for computer vision applications

Architecture to improve the accuracy of automatic image annotation systems

Automatic image annotation (AIA) is an image retrieval mechanism to extract relative semantic tags from visual content. So far, the improvement of accuracy in newly developed such methods have been about 1 or 2% in the F1‐score and the architectures seem to have room for improvement. Therefore, the authors designed a more detailed architecture for AIA and suggested new algorithms for its main parts. The proposed architecture has three main parts: feature extraction, learning, and annotation. They designed a novel learning method using machine learning and probability bases. In the annotation part, they suggest a novel method that gains the maximum benefit from the learning part. The combination of the proposed architecture, algorithms, and novel ideas resulted in new accuracy milestones in F1‐score on most commonly used datasets. In their architecture, N
                    <jats:sup>+</jats:sup>
                    measure which shows the number of tags with non‐z

HANOLISTIC: A Hierarchical Automatic Image Annotation System Using Holistic Approach


## Quote


Une combinaison de révision manuelle et de traitement morphologique d'image a été utilisée pour améliorer la qualité des masques d'annotation générés automatiquement

To validate the effectiveness of our proposed image annotation methodology within a crowdsourcing framework, a series of experiments were conducted focusing on machine learning results and assessing the consistency among annotators as measures of dataset quality.

To validate the effectiveness of our proposed image annotation methodology within a crowdsourcing framework, a series of experiments were conducted focusing on machine learning results and assessing the consistency among annotators as measures of dataset quality.


## Raw_Quality_Control.


During the annotation phase, we implemented a strategy where each image was annotated by three different individuals. This approach was designed to enhance the reliability of perspectives in the annotation process. In the quality assessment phase, labels that received consistent annotations from at least two out of the three annotators were adopted as the final label for the dataset. In cases where there was no consensus among the initial three annotators, a fourth annotator was introduced to reassess and provide an additional annotation for the image. This step was crucial in ensuring the accuracy and consistency of the labels in our dataset, thereby enhancing the overall quality of the annotated data.

During the annotation phase, we implemented a strategy where each image was annotated by three different individuals. This approach was designed to enhance the reliability of perspectives in the annotation process. In the quality assessment phase, labels that received consistent annotations from at least two out of the three annotators were adopted as the final label for the dataset. In cases where there was no consensus among the initial three annotators, a fourth annotator was introduced to reassess and provide an additional annotation for the image. This step was crucial in ensuring the accuracy and consistency of the labels in our dataset, thereby enhancing the overall quality of the annotated data.


## Insight


annotation quality: L'amélioration de la qualité des masques d'annotation générés automatiquement a reposé sur une combinaison de révision manuelle et de traitement morphologique d'image, illustrant une approche hybride entre correction humaine et post-traitement algorithmique.


## Raw_Conclusion


In this study, we developed and validated an innovative image annotation methodology within a crowdsourcing framework, significantly enhancing annotation consistency and accuracy. Our approach, grounded in knowledge representation, natural language processing, and computer vision, focuses on hierarchical categorization and detailed visual property analysis, offering a novel solution to challenges in dataset quality and semantic interpretation. Finally, our dataset will encompass multi-level labels, and can be used in multiple downstream tasks across vision and language domains, including fine-grained and zero-shot image recognition, image captioning, and image generation. Future research directions include developing automated and adaptive systems, exploring cross-domain applications, and enhancing training protocols.

In this study, we developed and validated an innovative image annotation methodology within a crowdsourcing framework, significantly enhancing annotation consistency and accuracy. Our approach, grounded in knowledge representation, natural language processing, and computer vision, focuses on hierarchical categorization and detailed visual property analysis, offering a novel solution to challenges in dataset quality and semantic interpretation. Finally, our dataset will encompass multi-level labels, and can be used in multiple downstream tasks across vision and language domains, including fine-grained and zero-shot image recognition, image captioning, and image generation. Future research directions include developing automated and adaptive systems, exploring cross-domain applications, and enhancing training protocols.

Another important focus area is incorporating more automation into the labeling process. With the use of AI technology, the time and effort needed for annotation tasks can be reduced while maintaining high accuracy levels. This automated approach could play a role in expanding the use of Spannotation for larger datasets.

Another important focus area is incorporating more automation into the labeling process. With the use of AI technology, the time and effort needed for annotation tasks can be reduced while maintaining high accuracy levels. This automated approach could play a role in expanding the use of Spannotation for larger datasets.


## Raw_Discussion


To validate the effectiveness of our proposed image annotation methodology within a crowdsourcing framework, a series of experiments were conducted focusing on machine learning results and assessing the consistency among annotators as measures of dataset quality.

To validate the effectiveness of our proposed image annotation methodology within a crowdsourcing framework, a series of experiments were conducted focusing on machine learning results and assessing the consistency among annotators as measures of dataset quality.


## Raw_Full_Text


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