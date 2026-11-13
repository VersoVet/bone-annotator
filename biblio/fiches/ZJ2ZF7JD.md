# Table 4: Overview of the intersection over union (IoU) threshold ranges achieved by the proposed cumulative transfer learning convolutional neural network (CNN) model and the you only look once version 8 (YOLOv8) model.



## Resume


Table 4: Overview of the intersection over union (IoU) threshold ranges achieved by the proposed cumulative transfer learning convolutional neural network (CNN) model and the you only look once version 8 (YOLOv8) model.

Object Detection using You Only Look Once (YOLO) Algorithm in Convolution Neural Network (CNN)

Figure 3: (1) Deep neural network architecture. (2) Convolutional neural network architecture. (3) Long short-term memory architecture. (4) Hybrid model (CNN-LSTM) architecture.

Deep learning object detection-based early detection of lung cancer.

The early diagnosis and accurate classification of lung cancer have a critical impact on clinical treatment and patient survival. The rise of artificial intelligence technology has led to breakthroughs in medical image analysis. The Lung-PET-CT-Dx public dataset was used for the model training and evaluation. The performance of the You Only Look Once (YOLO) series of models in the lung CT image object detection task is compared in terms of algorithms, and different versions of YOLOv5, YOLOv8, YOLOv9, YOLOv10, and YOLOv11 are examined for lung cancer detection and classification. The experimental results indicate that the prediction results of YOLOv8 are better than those of the other YOLO versions, with a precision rate of 90.32% and a recall rate of 84.91%, which proves that the model can effectively assist physicians in lung cancer diagnosis and improve the accuracy of disease localization and identification.

YOLO Nano: a Highly Compact You Only Look Once Convolutional Neural Network for Object Detection

YOLOv9 for fracture detection in pediatric wrist trauma X‐ray images

Abstract
                  
                    The introduction of YOLOv9, the latest version of the you only look once (YOLO) series, has led to its widespread adoption across various scenarios. This paper is the first to apply the YOLOv9 algorithm model to the fracture detection task as computer‐assisted diagnosis to help radiologists and surgeons to interpret X‐ray images. Specifically, this paper trained the model on the GRAZPEDWRI‐DX dataset and extended the training set using data augmentation techniques to improve the model performance. Experimental results demonstrate that compared to the mAP 50–95 of the current state‐of‐the‐art model, the YOLOv9 model increased the value from 42.16% to 43.73%, with an improvement of 3.7%. The implementation code is publicly available at
                    https://github.com/RuiyangJu/YOLOv9‐Fracture‐Detection
                    .


## Table


Tableau: Multiclass object detection performances of faster R-CNN and YOLOv5 for identification of maxillofacial fracture in each class. IoU intersection over union, AUC area under the precision-recall curve, AP average precision, mAP mean average precision.
| Models | Class | IoU (threshold) |
| --- | --- | --- |


## Raw_Maskrcnn_Evaluation


Intersection Over Union (IoU) of predicted masks. The number of pixels overlapping the ground-truth mask, normalized by the number of pixels in the union of both predicted and ground-truth masks. For each class, we only consider the set of ground-truth and predicted masks having the class label and report the ground-truth/predicted mask pairing that maximizes IoU. The MaskRCNN achieves IoU substantially greater than random-chance -indicating generated masks are semantically relevant and largely match ground-truth masks. The median IoU across all classes is 60% (10× higher than chance) with a maximum IoU of 85% for 'bus' and a minimum IoU of 42% for 'pole'. Comparatively, the maximum IoU with chance is 8% for the 'sky' class; the smallest improvement of the fine-tuned MaskRCNN over random chance is by 3× for the 'plant vertical' class.


## Quote


The confidence threshold of each proposed object detection model was taken as 0.25 (or 25%)... Meanwhile, the Intersection over Union (IoU) threshold of each proposed model was taken as 0.5 (or 50%).

Retrospective study analyzing 7,150 plain anteroposterior radiographs; a convolutional neural network (CNN) model known as You Only Look Once (YOLO)v8 was applied to identify fractures within radiographs, using image enhancement, data balancing, preprocessing techniques, and radiograph training via a YOLO-based framework

Compared with previous studies using 3D U-Net 10,14 , our Canal-Net achieved 0.87 of DSC and 0.80 of the mean intersection of union (IoU) while two previous studies reported 0.58 of DSC 10,14 and 0.58 of mean IoU 10,14 .

Five different versions of the YOLO model (YOLOv5, YOLOv8, YOLOv9, YOLOv10, and YOLOv11) were selected to evaluate their performances on a CT image dataset for lung cancer.


## Raw_Fewer_Annotated_Slices_Per_Volume_For_More_Volumes_Or_More


For each dataset, across different combinations of parameters (ρ, s), we generate sparse annotations from the corresponding dense annotations using the three slice selection methods described in Section 4.3. Each configuration is used to train models three times, resulting in 9 trials per (ρ, s) pair for each dataset. We evaluate the resultant models' performance using the average batched Intersection over Union (IoU), and report the mean and standard deviation in Tables 2 and3 under Appendix C. A reader-friendly visualization of the results is provided in Section 4.1.


## Insight


methodology: L'analyse de 20 études incluses dans cette revue de portée révèle une prédominance des modalités d'imagerie CT et IRM, avec les architectures de deep learning convolutionnel (U-Net, ResNet, YOLOv5) comme approches computationnelles dominantes.


## Raw_Object_Detection_Models.


The object detection algorithms used to construct the maxillofacial fracture detection models were the faster region convolutional neural network (faster R-CNN) and You Only Look Once (YOLO). The faster R-CNN is a two-step detection network that includes a feature extractor, region proposal network (RPN), region of interest (ROI) clustering, and classifier. This algorithm is the combination of the previous object detection system, Fast R-CNN, and RPNs into a single network to share their convolutional features leading to a more real-time object detection method, which improved the speed and accuracy in the object detection compared to basic R-CNN 25,26 . YOLOv5 used in this study is a one-stage object detection algorithm that uses a single network to directly predict object bounding boxes and class probability scores from images. YOLOv5 enables end-to-end training and real time speeds while maintaining high average precision. The detection speed is improved by avoiding the use of RPNs


## Raw_Hybrid_And_Hierarchical_Models


Hybrid models integrate CNNs with transformer layers as shown in Figure 1d, leveraging inductive biases of CNNs for local feature extraction and translation invariance, while exploiting transformers' capacity to capture global context through self-attention mechanisms [7]. Popular examples such as TransUNet [56], Swin-Unet [57], and UN-ETR [7] have demonstrated that these combinations can yield superior performance in tasks like organ segmentation and volumetric image analysis, particularly in data-limited regimes where pure transformer models tend to underperform [56,57]. Hybrid architectures also offer a practical means of scaling to high-resolution or 3D medical data, reducing the computational burden and data requirements associated with end-to-end transformer models.

Hybrid models integrate CNNs with transformer layers as shown in Figure 1d, leveraging inductive biases of CNNs for local feature extraction and translation invariance, while exploiting transformers' capacity to capture global context through self-attention mechanisms [7]. Popular examples such as TransUNet [56], Swin-Unet [57], and UN-ETR [7] have demonstrated that these combinations can yield superior performance in tasks like organ segmentation and volumetric image analysis, particularly in data-limited regimes where pure transformer models tend to underperform [56,57]. Hybrid architectures also offer a practical means of scaling to high-resolution or 3D medical data, reducing the computational burden and data requirements associated with end-to-end transformer models.


## Raw_Imitations_And_Future_Work


From an object perception perspective, the object detection and distance estimation module occasionally fail to detect certain obstacles. Since the YOLOv8 model trained on the COCO dataset was used, object recognition is limited to the 80 predefined classes in this dataset. Consequently, uncommon obstacles may not be detected reliably.


## Raw_Metric_Formula


Intersection-Over-Union / Jaccard Index

Intersection-Over-Union / Jaccard Index


## Resultats


La revue propose une synthèse comparative centrée sur FCN, U-Net et GAN, complétée par un inventaire des méthodes selon les organes et tissus pathologiques. Elle partage également des métriques d’évaluation et des datasets publics largement utilisés. Elle met en évidence des défis persistants liés au transfert clinique, à la qualité et à la variabilité des images, à la rareté des données annotées et aux limites des architectures et des fonctions de perte.