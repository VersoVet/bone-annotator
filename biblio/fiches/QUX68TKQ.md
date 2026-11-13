# HEPHA: A Mixed-Initiative Image Labeling Tool for Specialized Domains



## Resume


HEPHA: A Mixed-Initiative Image Labeling Tool for Specialized Domains

Image labeling is an important task for training computer vision models. In specialized domains, such as healthcare, it is expensive and challenging to recruit specialists for image labeling. We propose HEPHA, a mixed-initiative image labeling tool that elicits human expertise via inductive logic learning to infer and refine labeling rules. Each rule comprises visual predicates that describe the image. HEPHA enables users to iteratively refine the rules by either direct manipulation through a visual programming interface or by labeling more images. To facilitate rule refinement, HEPHA recommends which rule to edit and which predicate to update. For users unfamiliar with visual programming, HEPHA suggests diverse and informative images to users for further labeling. We conducted a within-subjects user study with 16 participants and compared HEPHA with a variant of HEPHA and a deep learning-based approach. We found that HEPHA outperforms the two baselines in both specialized-domain and g


## Raw_Abstract


Image labeling is an important task for training computer vision models. In specialized domains, such as healthcare, it is expensive and challenging to recruit specialists for image labeling. We propose HEPHA, a mixed-initiative image labeling tool that elicits human expertise via inductive logic learning to infer and refine labeling rules. Each rule comprises visual predicates that describe the image. HEPHA enables users to iteratively refine the rules by either direct manipulation through a visual programming interface or by labeling more images. To facilitate rule refinement, HEPHA recommends which rule to edit and which predicate to update. For users unfamiliar with visual programming, HEPHA suggests diverse and informative images to users for further labeling. We conducted a within-subjects user study with 16 participants and compared

Image labeling is an important task for training computer vision models. In specialized domains, such as healthcare, it is expensive and challenging to recruit specialists for image labeling. We propose HEPHA, a mixed-initiative image labeling tool that elicits human expertise via inductive logic learning to infer and refine labeling rules. Each rule comprises visual predicates that describe the image. HEPHA enables users to iteratively refine the rules by either direct manipulation through a visual programming interface or by labeling more images. To facilitate rule refinement, HEPHA recommends which rule to edit and which predicate to update. For users unfamiliar with visual programming, HEPHA suggests diverse and informative images to users for further labeling. We conducted a within-subjects user study with 16 participants and compared


## Raw_Unnamed


Figure 1: HEPHA is a mixed-initiative tool that supports image labeling by eliciting labeling knowledge from domain experts. Starting with a small set of labeled images, HEPHA generates labeling rules and applies them to all unlabeled images during the Rule Inference stage. Users can then apply their domain expertise to iteratively correct labels or directly edit the inferred rules to improve image labeling accuracy during the Rule Refinement stage.

Figure 1: HEPHA is a mixed-initiative tool that supports image labeling by eliciting labeling knowledge from domain experts. Starting with a small set of labeled images, HEPHA generates labeling rules and applies them to all unlabeled images during the Rule Inference stage. Users can then apply their domain expertise to iteratively correct labels or directly edit the inferred rules to improve image labeling accuracy during the Rule Refinement stage.


## Raw_Introduction


To address these limitations, we propose a mixed-initiative image labeling tool called HEPHA. HEPHA elicits the labeling knowledge from domain experts as first-order logic rules via inductive logic programming (ILP) [37]. Each labeling rule is composed of visual predicates that describe the image, such as objects detected in the image. HEPHA automatically applies these rules to new images to infer their labels. Compared with DL-based labeling methods, HEPHA has two unique advantages. First, ILP only requires a small number of instances, such as 5 images, to infer a logic rule, which makes it much easier to bootstrap the labeling process. Second, the labeling rules are inherently interpretable. Users can easily figure out why HEPHA infers a certain label for an image, diagnose a labeling error, and make corrections.

To address these limitations, we propose a mixed-initiative image labeling tool called HEPHA. HEPHA elicits the labeling knowledge from domain experts as first-order logic rules via inductive logic programming (ILP) [37]. Each labeling rule is composed of visual predicates that describe the image, such as objects detected in the image. HEPHA automatically applies these rules to new images to infer their labels. Compared with DL-based labeling methods, HEPHA has two unique advantages. First, ILP only requires a small number of instances, such as 5 images, to infer a logic rule, which makes it much easier to bootstrap the labeling process. Second, the labeling rules are inherently interpretable. Users can easily figure out why HEPHA infers a certain label for an image, diagnose a labeling error, and make corrections.

• We developed HEPHA, a mixed-initiative interaction system that enables users to label images by interpreting the labeling process and refining labeling rules according to human expertise. • We investigated three recommendation features to assist and guide users during the image labeling and rule refinement process. • We did a within-subjects user study to evaluate the usefulness and efficiency of different features in HEPHA.

• We developed HEPHA, a mixed-initiative interaction system that enables users to label images by interpreting the labeling process and refining labeling rules according to human expertise. • We investigated three recommendation features to assist and guide users during the image labeling and rule refinement process. • We did a within-subjects user study to evaluate the usefulness and efficiency of different features in HEPHA.

hat HEPHA is a useful and efficient image labeling tool. Refined by human expertise, inductive logic labeling rules can effectively enhance the image labeling process.

hat HEPHA is a useful and efficient image labeling tool. Refined by human expertise, inductive logic labeling rules can effectively enhance the image labeling process.


## Raw_Conclusion


We present HEPHA, a mixed-initiative system that automates image labeling by generating and applying labeling rules through Inductive Logic Programming (ILP). HEPHA integrates a visual programming interface to enhance interpretability, enabling users to edit labeling rules based on their domain expertise. In addition, the system offers three recommendation mechanisms to guide and assist users in rule refinement. By enabling users to debug and take control of the automated labeling process, HEPHA allows them to leverage their knowledge to achieve accurate image labeling with minimal training data and human effort. To evaluate the usefulness and performance of HEPHA, we conducted a within-subjects user study with 16 participants on two specialized-domain datasets and two general-domain datasets. Our user study results demonstrated that users were able to achieve more accurate image labeling when using HEPHA. Furthermore, the labeling process was also faster comparing HEPHA with the deep

We present HEPHA, a mixed-initiative system that automates image labeling by generating and applying labeling rules through Inductive Logic Programming (ILP). HEPHA integrates a visual programming interface to enhance interpretability, enabling users to edit labeling rules based on their domain expertise. In addition, the system offers three recommendation mechanisms to guide and assist users in rule refinement. By enabling users to debug and take control of the automated labeling process, HEPHA allows them to leverage their knowledge to achieve accurate image labeling with minimal training data and human effort. To evaluate the usefulness and performance of HEPHA, we conducted a within-subjects user study with 16 participants on two specialized-domain datasets and two general-domain datasets. Our user study results demonstrated that users were able to achieve more accurate image labeling when using HEPHA. Furthermore, the labeling process was also faster comparing HEPHA with the deep


## Quote


We present HEPHA, a mixed-initiative system that automates image labeling by generating and applying labeling rules through Inductive Logic Programming (ILP). HEPHA integrates a visual programming interface to enhance interpretability, enabling users to edit labeling rules based on their domain expertise. In addition, the system offers three recommendation mechanisms to guide and assist users in rule refinement.

We present HEPHA, a mixed-initiative system that automates image labeling by generating and applying labeling rules through Inductive Logic Programming (ILP). HEPHA integrates a visual programming interface to enhance interpretability, enabling users to edit labeling rules based on their domain expertise. In addition, the system offers three recommendation mechanisms to guide and assist users in rule refinement.

HEPHA elicits the labeling knowledge from domain experts as first-order logic rules via inductive logic programming (ILP) [37]. Each labeling rule is composed of visual predicates that describe the image, such as objects detected in the image. HEPHA automatically applies these rules to new images to infer their labels.

HEPHA elicits the labeling knowledge from domain experts as first-order logic rules via inductive logic programming (ILP) [37]. Each labeling rule is composed of visual predicates that describe the image, such as objects detected in the image. HEPHA automatically applies these rules to new images to infer their labels.


## Raw_User_Study


To understand how people interact with HEPHA in image labeling tasks, we conducted a within-subjects evaluation. The study was designed to compare HEPHA with its variant and a baseline deep learning approach across specialized and general domains.

To understand how people interact with HEPHA in image labeling tasks, we conducted a within-subjects evaluation. The study was designed to compare HEPHA with its variant and a baseline deep learning approach across specialized and general domains.


## Discussion


HEPHA est un système d’étiquetage d’images en initiative mixte qui génère et applique des règles via la programmation logique inductive (ILP), complétées par une interface de programmation visuelle et trois mécanismes de recommandation destinés à soutenir le raffinement des règles par l’utilisateur. Dans une étude utilisateur intra-sujets menée auprès de 16 participants sur deux jeux de données de domaines spécialisés et deux de domaines généraux, HEPHA a été comparé à ResNet ainsi qu’à une variante sans fonctions d’édition des règles. Les exactitudes moyennes d’étiquetage rapportées pour HEPHA se situaient entre 87,43 % et 91,42 %, pour des durées d’étiquetage comprises entre 13 et 17 minutes. Selon les auteurs, HEPHA a significativement surpassé l’approche d’apprentissage profond en exactitude et en temps sur l’ensemble des tâches ; toutefois, aucune valeur p, aucun intervalle de confiance ni aucune taille d’effet ne sont fournis dans les données extraites. Les auteurs attribuent ces gains à l’interprétabilité de l’interface et à la possibilité d’intégrer l’expertise de domaine dans le processus d’étiquetage, en particulier lorsque les grands ensembles d’entraînement sont difficiles à constituer.

HEPHA est un système d’étiquetage d’images en initiative mixte qui génère et applique des règles via la programmation logique inductive (ILP), complétées par une interface de programmation visuelle et trois mécanismes de recommandation destinés à soutenir le raffinement des règles par l’utilisateur. Dans une étude utilisateur intra-sujets menée auprès de 16 participants sur deux jeux de données de domaines spécialisés et deux de domaines généraux, HEPHA a été comparé à ResNet ainsi qu’à une variante sans fonctions d’édition des règles. Les exactitudes moyennes d’étiquetage rapportées pour HEPHA se situaient entre 87,43 % et 91,42 %, pour des durées d’étiquetage comprises entre 13 et 17 minutes. Selon les auteurs, HEPHA a significativement surpassé l’approche d’apprentissage profond en exactitude et en temps sur l’ensemble des tâches ; toutefois, aucune valeur p, aucun intervalle de confiance ni aucune taille d’effet ne sont fournis dans les données extraites. Les auteurs attribuent ces gains à l’interprétabilité de l’interface et à la possibilité d’intégrer l’expertise de domaine dans le processus d’étiquetage, en particulier lorsque les grands ensembles d’entraînement sont difficiles à constituer.


## Raw_Tasks


To evaluate HEPHA's effectiveness in specialized domains, we constructed two datasets specifically for these areas. Each dataset allowed us to measure performance in more focused, domain-specific tasks. We also included two datasets from general domains to assess HEPHA's generalizability across broader, more widely applicable contexts, ensuring that HEPHA performs well not only in specialized tasks but also in diverse, non-domain-specific scenarios. We designed four labeling tasks, with each task targeting one of these datasets. Specifically, the tasks involved the following four datasets:

To evaluate HEPHA's effectiveness in specialized domains, we constructed two datasets specifically for these areas. Each dataset allowed us to measure performance in more focused, domain-specific tasks. We also included two datasets from general domains to assess HEPHA's generalizability across broader, more widely applicable contexts, ensuring that HEPHA performs well not only in specialized tasks but also in diverse, non-domain-specific scenarios. We designed four labeling tasks, with each task targeting one of these datasets. Specifically, the tasks involved the following four datasets:


## Raw_Recommendation_Mechanisms


Labeling Recommendations by Multi-criteria Active Learning. For users unfamiliar with visual programming interfaces, directly editing rules can be challenging. To simplify this process, HEPHA allows users to refine rules by providing additional image examples for learning and rule regeneration. HEPHA uses the multi-criteria active learning algorithm from RAPID [56] to suggest images for labeling based on their diversity and informativeness, using vectorized visual predicates rather than raw pixel data.

Labeling Recommendations by Multi-criteria Active Learning. For users unfamiliar with visual programming interfaces, directly editing rules can be challenging. To simplify this process, HEPHA allows users to refine rules by providing additional image examples for learning and rule regeneration. HEPHA uses the multi-criteria active learning algorithm from RAPID [56] to suggest images for labeling based on their diversity and informativeness, using vectorized visual predicates rather than raw pixel data.


## Raw_Design_Goals


DG1. Optimizing Efficiency with Limited Data Current deep learning methods often require large amounts of labeled data to achieve high accuracy [24,35,39,41]. However, in specialized domains like medical imaging, obtaining such large datasets can be challenging and expensive [14]. Therefore, our primary goal is to design a system that can produce accurate labels with a small amount of training data. HEPHA addresses this by using ILP to infer labeling rules, significantly reducing the initial data requirements compared to deep learning approaches.

DG1. Optimizing Efficiency with Limited Data Current deep learning methods often require large amounts of labeled data to achieve high accuracy [24,35,39,41]. However, in specialized domains like medical imaging, obtaining such large datasets can be challenging and expensive [14]. Therefore, our primary goal is to design a system that can produce accurate labels with a small amount of training data. HEPHA addresses this by using ILP to infer labeling rules, significantly reducing the initial data requirements compared to deep learning approaches.

In developing HEPHA, we identified four key design objectives. These were informed by our analysis of existing image labeling methodologies [8,32,57], prior research on image labeling tasks [6,47,51], and our empirical experience in the field.


## Raw_System_Architecture


HEPHA comprises three components: the pre-trained visual predicate extractor, the backend algorithm, and the interactive refinement user interface, as shown in Figure 2. For each image labeling task, users first define the predicates based on their domain knowledge and import corresponding pre-trained computer vision models for visual predicate extraction. Based on the user-defined predicates, the backend algorithm uses inductive logic programming to search for suitable image labeling rules and apply them to autolabel images (detailed in Section 4.3). HEPHA proposes a novel user interface that visualizes the logic of the image labeling rules and presents the image labeling results. Users can correct labels in a gallery view and directly edit rules through a visual programming interface (detailed in Section 4.2 and Section 4.4).

HEPHA comprises three components: the pre-trained visual predicate extractor, the backend algorithm, and the interactive refinement user interface, as shown in Figure 2. For each image labeling task, users first define the predicates based on their domain knowledge and import corresponding pre-trained computer vision models for visual predicate extraction. Based on the user-defined predicates, the backend algorithm uses inductive logic programming to search for suitable image labeling rules and apply them to autolabel images (detailed in Section 4.3). HEPHA proposes a novel user interface that visualizes the logic of the image labeling rules and presents the image labeling results. Users can correct labels in a gallery view and directly edit rules through a visual programming interface (detailed in Section 4.2 and Section 4.4).