# Artificial Intelligence Accurately Detects Traumatic Thoracolumbar Fractures on Sagittal Radiographs.

**Auteurs** : Guillermo Sánchez Rosenberg, Andrea Cina, Giuseppe Rosario Schiró, Pietro Domenico Giorgi, Boyko Gueorguiev, Mauro Alini, Peter Varga, Fabio Galbusera, Enrico Gallazzi
**Année** : 2022
**DOI** : 10.3390/medicina58080998

## Résumé

Background and Objectives: Commonly being the first step in trauma routine imaging, up to 67% fractures are missed on plain radiographs of the thoracolumbar (TL) spine. The aim of this study was to develop a deep learning model that detects traumatic fractures on sagittal radiographs of the TL spine. Identifying vertebral fractures in simple radiographic projections would have a significant clinical and financial impact, especially for low- and middle-income countries where computed tomography (CT) and magnetic resonance imaging (MRI) are not readily available and could help select patients that need second level imaging, thus improving the cost-effectiveness. Materials and Methods: Imaging studies (radiographs, CT, and/or MRI) of 151 patients were used. An expert group of three spinal surgeons reviewed all available images to confirm presence and type of fractures. In total, 630 single vertebra images were extracted from the sagittal radiographs of the 151 patients—302 exhibiting a vertebral body fracture, and 328 exhibiting no fracture. Following augmentation, these single vertebra images were used to train, validate, and comparatively test two deep learning convolutional neural network models, namely ResNet18 and VGG16. A heatmap analysis was then conducted to better understand the predictions of each model. Results: ResNet18 demonstrated a better performance, achieving higher sensitivity (91%), specificity (89%), and accuracy (88%) compared to VGG16 (90%, 83%, 86%). In 81% of the cases, the “warm zone” in the heatmaps correlated with the findings, suggestive of fracture within the vertebral body seen in the imaging studies. Vertebras T12 to L2 were the most frequently involved, accounting for 48% of the fractures. A4, A3, and A1 were the most frequent fracture types according to the AO Spine Classification. Conclusions: ResNet18 could accurately identify the traumatic vertebral fractures on the TL sagittal radiographs. In most cases, the model based its prediction on the same areas that human expert classifiers used to determine the presence of a fracture.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Disease and procedure codes.

| Disease Codes | Procedure Codes |
| --- | --- |
| Fracture of thoracic spine | Thoracolumbar instrumentation |
| Fracture of thoracolumbar spine | Instrumentation lumbar spine |
| Fracture of lumbar spine | Instrumentation thoracic spine |
| Vertebra fracture | Osteosynthesis of the spine |
| Vertebra injury | Spinopelvic fixation |
|  | Kyphoplasty |
|  | Spinal fixation |

## Performance comparison of the two deep learning convolutional neural models ResNet18 and VGG16.

|  | Sensitivity | Specificity | Negative Predictive Value | Accuracy |
| --- | --- | --- | --- | --- |
| ResNet 18 | 0.91 | 0.89 | 0.89 | 0.88 |
| VGG16 | 0.90 | 0.83 | 0.89 | 0.86 |
