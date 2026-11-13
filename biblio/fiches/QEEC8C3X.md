# Explainable artificial intelligence (XAI) in deep learning-based medical image analysis



## Resume


Explainable artificial intelligence (XAI) in deep learning-based medical image analysis

AI applications to medical images: From machine learning to deep learning

A review on deep learning in medical image analysis

Explainable AI in Orthopedics: Challenges, Opportunities, and Prospects

While artificial intelligence (AI) has made many successful applications in various domains, its adoption in healthcare lags a little bit behind other high-stakes settings. Several factors contribute to this slower uptake, including regulatory frameworks, patient privacy concerns, and data heterogeneity. However, one significant challenge that impedes the implementation of AI in healthcare, particularly in orthopedics, is the lack of explainability and interpretability around AI models. Addressing the challenge of explainable AI (XAI) in orthopedics requires developing AI models and algorithms that prioritize transparency and interpretability, allowing clinicians, surgeons, and patients to understand the contributing factors behind any AI-powered predictive or descriptive models. The current contribution outlines several key challenges and opportunities that manifest in XAI in orthopedic practice. This work emphasizes the need for interdisciplinary collaborations between AI practitione

Interactive Explainable Deep Learning Model Informs Prostate Cancer Diagnosis at MRI.

Background Clinically significant prostate cancer (PCa) diagnosis at MRI requires accurate and efficient radiologic interpretation. Although artificial intelligence may assist in this task, lack of transparency has limited clinical translation. Purpose To develop an explainable artificial intelligence (XAI) model for clinically significant PCa diagnosis at biparametric MRI using Prostate Imaging Reporting and Data System (PI-RADS) features for classification justification. Materials and Methods This retrospective study included consecutive patients with histopathologic analysis-proven prostatic lesions who underwent biparametric MRI and biopsy between January 2012 and December 2017. After image annotation by two radiologists, a deep learning model was trained to detect the index lesion; classify PCa, clinically significant PCa (Gleason score ≥ 7), and benign lesions (eg, prostatitis); and justify classifications using PI-RADS features. Lesion- and patient-based performance were assesse

Medical Image Detection and Recognition Using Machine Learning and Deep Learning

Machine Learning/Deep Learning in Medical Image Processing

Explainable Deep Learning Models in Medical Image Analysis

Deep learning methods have been very effective for a variety of medical diagnostic tasks and have even outperformed human experts on some of those. However, the black-box nature of the algorithms has restricted their clinical use. Recent explainability studies aim to show the features that influence the decision of a model the most. The majority of literature reviews of this area have focused on taxonomy, ethics, and the need for explanations. A review of the current applications of explainable deep learning for different medical imaging tasks is presented here. The various approaches, challenges for clinical deployment, and the areas requiring further research are discussed here from a practical standpoint of a deep learning researcher designing a system for the clinical end-users.

A survey on deep learning in medical image analysis

CAIPI in Practice: Towards Explainable Interactive Medical Image Classification

Would you trust physicians if they cannot explain their decisions to you? Medical diagnostics using machine learning gained enormously in importance within the last decade. However, without further enhancements many state-of-the-art machine learning methods are not suitable for medical application. The most important reasons are insufficient data set quality and the black-box behavior of machine learning algorithms such as Deep Learning models. Consequently, end-users cannot correct the model's decisions and the corresponding explanations. The latter is crucial for the trustworthiness of machine learning in the medical domain. The research field explainable interactive machine learning searches for methods that address both shortcomings. This paper extends the explainable and interactive CAIPI algorithm and provides an interface to simplify human-in-the-loop approaches for image classification. The interface enables the end-user (1) to investigate and (2) to correct the model's predict

Application of Artificial Intelligence in Medical Imaging

Role of artificial intelligence in medical image analysis.

<h4>Abstract</h4>With the emergence of deep learning techniques based on convolutional neural networks, artificial intelligence (AI) has driven transformative developments in the field of medical image analysis. Recently, large language models (LLMs) such as ChatGPT have also started to achieve distinction in this domain. Increasing research shows the undeniable role of AI in reshaping various aspects of medical image analysis, including processes such as image enhancement, segmentation, detection in image preprocessing, and postprocessing related to medical diagnosis and prognosis in clinical settings. However, despite the significant progress in AI research, studies investigating the recent advances in AI technology in the aforementioned aspects, the changes in research hotspot trajectories, and the performance of studies in addressing key clinical challenges in this field are limited. This article provides an overview of recent advances in AI for medical image analysis and discusses

A comprehensive survey on deep active learning in medical image analysis.


## Quote


we presented an explainable artificial intelligence (XAI) for the detection and classification of clinically significant PCa at biparametric MRI, where computer-based decisions are made transparent with textual explanations and heat map visualization based on Prostate Imaging Reporting and Data System

showing significant promise for explainable AI applications in medical image analysis

To contextualize our approach within the broader landscape of medical XAI techniques reviewed by Bhati et al. [9], we performed explainability analyses to ensure model transparency and evaluate whether decisions were based on clinically meaningful features.

To address explainable artificial intelligence (XAI), a Gradient-based Class Activation Mapping (Grad-CAM) method was used to examine how the model makes predictions from input images.

L'IA explicable (xAI), via des méthodes comme la Layer-wise Relevance Propagation et des heatmaps, permet de rendre les décisions de l'IA interprétables par les humains

By leveraging advanced algorithms and big data, AI enables the automation of image analysis, offering the potential to improve diagnostic accuracy, reproducibility and efficiency [9,15,24].


## Conclusion


The study provides proof-of-concept for an interactive, explainable AI (XAI) model that reliably detects and classifies prostatic lesions at biparametric MRI. The XAI assisted nonexpert readers by explaining and visualizing its decision-making using well-established PI-RADS imaging features via a custom interface, overcoming the 'black-box' design of prior convolutional neural networks. Such explainable tools may facilitate informed decision-making in AI-assisted radiologic image analysis and support clinical translation of AI in prostate MRI diagnosis.

L'IA transforme rapidement l'imagerie tumorale, améliorant significativement le diagnostic du cancer, la planification thérapeutique et la prédiction pronostique, mais son adoption clinique généralisée reste conditionnée par la résolution des problèmes de qualité des données, de transparence, d'éthique et de réglementation Les recherches futures devraient se concentrer sur l'optimisation des algorithmes d'IA, la collaboration interdisciplinaire, l'intégration de données multimodales (imagerie, génomique, clinique) et la validation clinique extensive via des essais prospectifs multicentriques L'IA explicable (XAI) et des cadres réglementaires robustes combinant évaluation des risques avant mise sur le marché et surveillance post-commercialisation ne sont plus optionnels mais fondamentaux pour garantir la sécurité et l'équité de l'IA en oncologie


## Raw_Methods


Large language models have significantly advanced the healthcare domain, enhancing tasks such as medical diagnosis and patient monitoring. However, the complexity of these models necessitates interpretability for reliable decision-making [83]. This section discusses "eXplainable and Interpretable Artificial Intelligence" (XIAI) and examines recent XIAI methods by their functionality and scope. Despite challenges such as the difficulty in quantifying interpretability and the lack of standardized evaluation metrics, opportunities exist in integrating XIAI to add interpretability for LLMs in healthcare. Notable XIAI methods include SHAP [84], which quantifies feature contributions, LIME [85,86], which generates interpretable models through input perturbations, t-SNE for visualizing high-dimensional data [87], attention mechanisms that highlight key features [15], and knowledge graphs that structure contextual relationships [88], all of which provide crucial insights into model decision-ma


## Insight


positioning: Les analyses d'explicabilité menées ont été contextualisées par rapport au paysage plus large des techniques XAI médicales recensées par Bhati et al., situant ainsi l'approche dans la littérature existante sur l'interprétabilité en imagerie médicale.

methodology: L'analyse par IA explicable (XAI) a montré que les modèles s'appuient sur des repères anatomiques cliniquement pertinents (espace inter-arcades pour les bitewings, zones interdentaires pour les périapicales, structures osseuses pour les panoramiques, vue latérale du viscérocrâne pour les céphalométriques) pour établir leur décision de classification.


## Raw_Model_Used_Dataset_Isic_2016_Isic_2017


demand for explainable AI in medical diagnostics, where trust and transparency are paramount. Moreover, the active learning component enables domain experts to guide the model by selecting relevant features, which ensures that the explanations are grounded in clinical knowledge. This collaborative approach between AI systems and medical practitioners could significantly enhance diagnostic workflows.

demand for explainable AI in medical diagnostics, where trust and transparency are paramount. Moreover, the active learning component enables domain experts to guide the model by selecting relevant features, which ensures that the explanations are grounded in clinical knowledge. This collaborative approach between AI systems and medical practitioners could significantly enhance diagnostic workflows.


## Synthese


Cette revue narrative examine comment l'intelligence artificielle (IA) peut soutenir et augmenter le radiologue, en particulier le radiopédiatre, dans un environnement de travail complexe marqué par une charge informatique croissante. Les auteurs décrivent les différents types d'IA utilisés en radiologie, comparent leurs modes de résolution de problèmes à ceux de l'intelligence humaine, et présentent le concept d'IA explicable (explainable AI, xAI) comme solution au problème des systèmes fonctionnant en 'boîte noire'. L'analyse est illustrée par une expérience personnelle des auteurs portant sur le développement, depuis 2018, d'un algorithme de deep learning entraîné sur 258866 radiographies pédiatriques pour la détection automatique de fractures. Les résultats montrent que l'IA peut détecter des anomalies invisibles à l'œil humain et améliorer l'efficacité et la reproductibilité des mesures, mais que son manque de traçabilité pose des problèmes juridiques et de responsabilité. Les auteurs concluent que des méthodes de xAI, comme la Layer-wise Relevance Propagation et les heatmaps, associées au concept de 'causability', sont nécessaires pour rendre les décisions de l'IA interprétables, tout en affirmant que la décision diagnostique finale doit rester du ressort exclusif du radiologue humain.


## Resultats


Afin de garantir la transparence des modèles et d'évaluer si les décisions reposaient sur des caractéristiques cliniquement pertinentes, les auteurs ont mené des analyses d'explicabilité (XAI) sur l'ensemble du pipeline expérimental unifié, s'appuyant sur MLflow et Optuna pour l'entraînement et l'évaluation cohérents de tous les modèles (ResNet-50, EfficientNetB0, MobileNetV3-Small, SVM et XGBoost). Deux techniques complémentaires, représentatives des catégories basées sur le gradient et sur l'attribution de caractéristiques, ont été appliquées : Grad-CAM pour les réseaux de neurones convolutifs et SHAP pour les modèles d'apprentissage automatique classiques. Cette démarche s'inscrit dans le paysage plus large des techniques XAI médicales recensées par Bhati et al., permettant de situer l'approche proposée par rapport aux méthodes existantes en matière d'interprétabilité des modèles de détection du cancer du sein par mammographie.


## Raw_Explainability_In_Ai


XAI provides a framework for understanding, validating, and trusting AI models. By identifying the most influential features and revealing decision-making patterns, XAI techniques such as SHAP help bridge the gap between complex neural network models and human understanding, enabling safer and more reliable deployment of AI systems in critical applications. In Chapter 6, we leverage SHAP as the XAI method to explain AI decisions and identify the root causes of anomalies for anomaly resolution in ZSM systems. In the next section, we delve into the details of GenAI.

XAI provides a framework for understanding, validating, and trusting AI models. By identifying the most influential features and revealing decision-making patterns, XAI techniques such as SHAP help bridge the gap between complex neural network models and human understanding, enabling safer and more reliable deployment of AI systems in critical applications. In Chapter 6, we leverage SHAP as the XAI method to explain AI decisions and identify the root causes of anomalies for anomaly resolution in ZSM systems. In the next section, we delve into the details of GenAI.