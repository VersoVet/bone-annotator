# Toward automatic C-arm positioning for standard projections in orthopedic surgery

**Auteurs** : Lisa Kausch, Sarina Thomas, Holger Kunze, Maxim Privalov, Sven Y. Vetter, Jochen Franke, Andreas H. Mahnken, Lena Maier‐Hein, Klaus Maier‐Hein
**Année** : 2020
**DOI** : 10.1007/s11548-020-02204-0

## Résumé

AbstractPurposeGuidance and quality control in orthopedic surgery increasingly rely on intra-operative fluoroscopy using a mobile C-arm. The accurate acquisition of standardized and anatomy-specific projections is essential in this process. The corresponding iterative positioning of the C-arm is error prone and involves repeated manual acquisitions or even continuous fluoroscopy. To reduce time and radiation exposure for patients and clinical staff and to avoid errors in fracture reduction or implant placement, we aim at guiding—and in the long-run automating—this procedure.MethodsIn contrast to the state of the art, we tackle this inherently ill-posed problem without requiring patient-individual prior information like preoperative computed tomography (CT) scans, without the need of registration and without requiring additional technical equipment besides the projection images themselves. We propose learning the necessary anatomical hints for efficient C-arm positioning fromin silicosimulations, leveraging masses of 3D CTs. Specifically, we propose a convolutional neural network regression model that predicts 5 degrees of freedom pose updates directly from a first X-ray image. The method is generalizable to different anatomical regions and standard projections.ResultsQuantitative and qualitative validation was performed for two clinical applications involving two highly dissimilar anatomies, namely the lumbar spine and the proximal femur. Starting from one initial projection, the mean absolute pose error to the desired standard pose is iteratively reduced across different anatomy-specific standard projections. Acquisitions of both hip joints on 4 cadavers allowed for an evaluation on clinical data, demonstrating that the approach generalizes without retraining.ConclusionOverall, the results suggest the feasibility of an efficient deep learning-based automated positioning procedure, which is trained on simulations. Our proposed 2-stage approach for C-arm positioning significantly improves accuracy on synthetic images. In addition, we demonstrated that learning based on simulations translates to acceptable performance on real X-rays.

## Méthodologie

{'study_design': None, 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [], 'qualitative_findings': [], 'main_findings': []}

## Conclusions

The original article has been corrected.
