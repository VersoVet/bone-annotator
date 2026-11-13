# It's Not Just Labeling -- A Research on LLM Generated Feedback Interpretability and Image Labeling Sketch Features



## Raw_Research_Questions


To define the success of this research, several key steps must be taken. First, it is essential to generate a synthetic dataset that represents stroke-based labeling as 2D points within an image dataset. This dataset should closely simulate human labeling behavior to ensure realistic testing conditions. Next, a valid method must be established to quantify both the characteristics of sketch-based labeling and the accuracy of LLM-generated feedback. This includes extracting the features of the sketches in conveying labeling intent, as well as assessing the reliability of LLM feedback in interpreting these sketches. Finally, the results should demonstrate the correlation between image labeling and LLM-generated feedback. Additionally, the study should identify significant differences in LLM evaluation metrics when feedback is generated using different prompting strategies, highlighting how various prompt designs influence interpretability of LLM.

To define the success of this research, several key steps must be taken. First, it is essential to generate a synthetic dataset that represents stroke-based labeling as 2D points within an image dataset. This dataset should closely simulate human labeling behavior to ensure realistic testing conditions. Next, a valid method must be established to quantify both the characteristics of sketch-based labeling and the accuracy of LLM-generated feedback. This includes extracting the features of the sketches in conveying labeling intent, as well as assessing the reliability of LLM feedback in interpreting these sketches. Finally, the results should demonstrate the correlation between image labeling and LLM-generated feedback. Additionally, the study should identify significant differences in LLM evaluation metrics when feedback is generated using different prompting strategies, highlighting how various prompt designs influence interpretability of LLM.

• RQ1: How much sketch features from synthetic dataset can influence the interpretability of LLM's feedback generation by using different prompting strategies?

• RQ1: How much sketch features from synthetic dataset can influence the interpretability of LLM's feedback generation by using different prompting strategies?

• RQ2: What are the trade-offs among different prompting strategies for LLMs to evaluate images labeled by sketches.

• RQ2: What are the trade-offs among different prompting strategies for LLMs to evaluate images labeled by sketches.


## Raw_Constant


It's Not Just Labeling: A Research on LLM Generated Feedback Interpretability and Image Labeling Sketch Features11

It's Not Just Labeling: A Research on LLM Generated Feedback Interpretability and Image Labeling Sketch Features11


## Raw_Conclusion


d sketch-based interaction and LLM-generated feedback. This approach will allow for a comparison between human-drawn sketches and synthetic samples, providing deeper insights and verifying the feasibility of an LLM-powered sketch-based image labeling assistant.

d sketch-based interaction and LLM-generated feedback. This approach will allow for a comparison between human-drawn sketches and synthetic samples, providing deeper insights and verifying the feasibility of an LLM-powered sketch-based image labeling assistant.

In this research, we explored the influence of SR features from a synthetic dataset on the interpretability of LLMgenerated feedback and examined the trade-offs among different prompting strategies in evaluating images labeled by free-hand sketches. Through correlation analysis, the findings indicate that sketch features exhibit mostly weak or negligible correlations with LLM evaluation metrics including context precision, faithfulness, and answer relevancy.

In this research, we explored the influence of SR features from a synthetic dataset on the interpretability of LLMgenerated feedback and examined the trade-offs among different prompting strategies in evaluating images labeled by free-hand sketches. Through correlation analysis, the findings indicate that sketch features exhibit mostly weak or negligible correlations with LLM evaluation metrics including context precision, faithfulness, and answer relevancy.

These results suggest that while certain sketch attributes, such as stroke density, length, and angular features, may have a minor influence on LLM-generated feedback, their overall impact remains limited.

These results suggest that while certain sketch attributes, such as stroke density, length, and angular features, may have a minor influence on LLM-generated feedback, their overall impact remains limited.


## Raw_Methodologies


Finally, the extracted sketch recognition features and LLM evaluation metrics were statistically analyzed. The goals of this research were to examine whether certain sketch characteristics can influence LLM interpretability and explore how prompting strategies affect the nature and usefulness of LLM-generated feedback.

Finally, the extracted sketch recognition features and LLM evaluation metrics were statistically analyzed. The goals of this research were to examine whether certain sketch characteristics can influence LLM interpretability and explore how prompting strategies affect the nature and usefulness of LLM-generated feedback.

Subsequently, the labeled images from the synthetic dataset were processed by leveraging an LLM, and several distinct prompting strategies were employed to elicit LLM-generated feedback for each labeled image. This feedback was intended to assess, and guide annotations, thus enhancing annotation precision and reliability. The variations in the prompt strategies are specifically designed to explore how different prompts influence the quality and relevance of feedback provided by the LLM.

Subsequently, the labeled images from the synthetic dataset were processed by leveraging an LLM, and several distinct prompting strategies were employed to elicit LLM-generated feedback for each labeled image. This feedback was intended to assess, and guide annotations, thus enhancing annotation precision and reliability. The variations in the prompt strategies are specifically designed to explore how different prompts influence the quality and relevance of feedback provided by the LLM.

This section describes the methods used in the research to generate synthetic sketches for image labeling, prompting strategies, and quantification of image labeling and LLM performance. The following Figure 2 is a brief overview of the workflow of the methodologies.

This section describes the methods used in the research to generate synthetic sketches for image labeling, prompting strategies, and quantification of image labeling and LLM performance. The following Figure 2 is a brief overview of the workflow of the methodologies.


## Raw_Future_Directions


, which will further verify the validity and feasibility of LLM-powered sketch-based image labeling system.

, which will further verify the validity and feasibility of LLM-powered sketch-based image labeling system.


## Conclusion


Sketch recognition features from the synthetic dataset exhibit mostly weak or negligible correlations with LLM evaluation metrics (context precision, faithfulness, answer relevancy), indicating limited overall influence of sketch attributes on LLM-generated feedback interpretability. Certain attributes (stroke density, length, angular/rotational features, bounding-box related measures, endpoint distances) may have only minor/weak associations depending on prompting strategy. Adding a rubric does not necessarily improve interpretability metrics: few-shot basic outperforms few-shot rubric in context precision; zero-shot basic and few-shot basic consistently achieve higher faithfulness and answer relevancy than rubric-based strategies. Rubrics may impose constraints that reduce alignment and factual accuracy of LLM-generated responses; whether incorporating examples improves interpretability requires further research. Findings are preliminary given synthetic-data limitations; future work should add temporal/motion features and conduct user studies with real human sketches and attitudes toward LLM feedback to validate an LLM-powered sketch-based labeling assistant.

Sketch recognition features from the synthetic dataset exhibit mostly weak or negligible correlations with LLM evaluation metrics (context precision, faithfulness, answer relevancy), indicating limited overall influence of sketch attributes on LLM-generated feedback interpretability. Certain attributes (stroke density, length, angular/rotational features, bounding-box related measures, endpoint distances) may have only minor/weak associations depending on prompting strategy. Adding a rubric does not necessarily improve interpretability metrics: few-shot basic outperforms few-shot rubric in context precision; zero-shot basic and few-shot basic consistently achieve higher faithfulness and answer relevancy than rubric-based strategies. Rubrics may impose constraints that reduce alignment and factual accuracy of LLM-generated responses; whether incorporating examples improves interpretability requires further research. Findings are preliminary given synthetic-data limitations; future work should add temporal/motion features and conduct user studies with real human sketches and attitudes toward LLM feedback to validate an LLM-powered sketch-based labeling assistant.


## Raw_Data_Analysis


After calculating SR features and evaluation metrics based on the four prompting strategies for each image in the original image collection, we analyzed the dataset to answer the research questions. The first research question examined the correlation between SR features and the interpretability of LLM feedback, while the second investigated the trade-offs among different prompting strategies for evaluating sketch-based image labeling.

After calculating SR features and evaluation metrics based on the four prompting strategies for each image in the original image collection, we analyzed the dataset to answer the research questions. The first research question examined the correlation between SR features and the interpretability of LLM feedback, while the second investigated the trade-offs among different prompting strategies for evaluating sketch-based image labeling.


## Raw_Unnamed


Therefore, this research aims to discover the possibility of using a sketch-based interface and LLM to enhance image labeling performance through a synthetic dataset.

Therefore, this research aims to discover the possibility of using a sketch-based interface and LLM to enhance image labeling performance through a synthetic dataset.


## Quote


These results suggest that while certain sketch attributes, such as stroke density, length, and angular features, may have a minor influence on LLM-generated feedback, their overall impact remains limited.

These results suggest that while certain sketch attributes, such as stroke density, length, and angular features, may have a minor influence on LLM-generated feedback, their overall impact remains limited.