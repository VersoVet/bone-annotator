# iVS Dataset and ezLabel: A Dataset and a Data Annotation Tool for Deep Learning Based ADAS Applications



## Resume


iVS Dataset and ezLabel: A Dataset and a Data Annotation Tool for Deep Learning Based ADAS Applications

To overcome the limitations of standard datasets with data at a wide-variety of scales and captured in the various conditions necessary to train neural networks to yield efficient results in ADAS applications, this paper presents a self-built open-to-free-use ‘iVS dataset’ and a data annotation tool entitled ‘ezLabel’. The iVS dataset is comprised of various objects at different scales as seen in and around real driving environments. The data in the iVS dataset are collected by employing a camcorder in vehicles driving under different conditions, e.g., light, weather and traffic, and driving scenarios ranging from city traffic during peak and normal hours to freeway traffics during busy and normal conditions. Thus, the collected data are wide-ranging and captured all possible objects at various scales appearing in real-time driving situations. The data collected in order to build the dataset has to be annotated before use in training the CNNs and so this paper presents an open-to-free-

Smart Data Annotation: Accelerating Data Labeling Processes through Deep Learning

DL-AAT: An Automatic Annotation Tool for Efficient Data Labeling in Vision-Based Systems

Deep Learning and Data Labeling for Medical Applications

Adapl: Adaptive Pseudo Labeling for Deep Active Learning in Image Classification

Figure 1. CVAT annotation interface. Dataset class structure and label setup

ByLabel: A Boundary Based Semi-Automatic Image Annotation Tool

LabelMe: A Database and Web-Based Tool for Image Annotation

EasyLabel: A Semi-Automatic Pixel-wise Object Annotation Tool for Creating Robotic RGB-D Datasets

Developing robot perception systems for recognizing objects in the real-world requires computer vision algorithms to be carefully scrutinized with respect to the expected operating domain. This demands large quantities of ground truth data to rigorously evaluate the performance of algorithms. This paper presents the EasyLabel tool for easily acquiring high quality ground truth annotation of objects at the pixel-level in densely cluttered scenes. In a semi-automatic process, complex scenes are incrementally built and EasyLabel exploits depth change to extract precise object masks at each step. We use this tool to generate the Object Cluttered Indoor Dataset (OCID) that captures diverse settings of objects, background, context, sensor to scene distance, viewpoint angle and lighting conditions. OCID is used to perform a systematic comparison of existing object segmentation methods. The baseline comparison supports the need for pixel- and object-wise annotation to progress robot vision tow

An Image Labeling Tool and Agricultural Dataset for Deep Learning

We introduce a labeling tool and dataset aimed to facilitate computer vision research in agriculture. The annotation tool introduces novel methods for labeling with a variety of manual, semi-automatic, and fully-automatic tools. The dataset includes original images collected from commercial greenhouses, images from PlantVillage, and images from Google Images. Images were annotated with segmentations for foreground leaf, fruit, and stem instances, and diseased leaf area. Labels were in an extended COCO format. In total the dataset contained 10k tomatoes, 7k leaves, 2k stems, and 2k diseased leaf annotations.

Deep learning based active learning technique for data annotation and improve the overall performance of classification models

Deep Active Re-Labeling: Toward Noise-Resilient Annotation Efficiency

Active Deep Learning for Minimizing Annotation Costs in Industrial Defect Detection

Deep learning has demonstrated significant potential for industrial surface defect detection, yet its practical deployment is often constrained by the substantial costs associated with manual data annotation. This paper addresses the challenge of minimizing annotation expenses while maintaining high detection accuracy through active deep learning approaches. We propose a framework that strategically selects the most informative unlabeled samples for human annotation, thereby reducing the labeling effort without compromising model performance. A lightweight convolutional neural network architecture is designed to accelerate training and enhance regularization, while a novel uncertainty-based sampling strategy-employing Kullback-Leibler divergence between predictive distributions-identifies high-value samples for labeling. Experimental validation on the NEU-CLS steel surface dataset demonstrates that the proposed method achieves 97.8% classification accuracy using only 44% of labeled dat

LabelMe: Online Image Annotation and Applications

Iterative Pseudo-Labeling with Deep Feature Annotation and Confidence-Based Sampling

Computer Vision Annotation Tool

Deep Interactive Annotation to Support Hyperspectral Image Analysis

Annotation plays an essential and important role in the performance of
machine learning approaches. However, manually labeling objects
accurately is often time-consuming, especially when processing large
image data. To improve this process, we developed a deep learning-based
interactive annotation approach with application to hyperspectral
imagery. Specifically, a deep network with a metric-based loss function
will be pre-trained on a large training set. Encoding layers in the
network are used for dimensionality reduction as well as boosting
discriminability among pixels belonging to different classes in the
embedding space. Then, when new images are provided, the user can
provide (fast, easy, weak) annotations to indicate objects of interest
and fine-tune the pre-trained network to the task at hand. In this way,
the fine-tuned network can adapt for the new category and task.
Annotations can be iteratively modified and corrected. Once the model is
fine-tuned by quickly annotating a few


## Raw_Image_Labeling_Platform


Label Assistant [24] presents a sketch-based labeling tool to assist the annotation process in image segmentation tasks, especially for deep learning applications. The proposed workflow integrates various methods, including pre-labeling, image pre-processing, and post-assistance to aid annotators in labeling complex image datasets efficiently. The authors demonstrate the effectiveness of the workflow on two biomedical image segmentation datasets, showing that their approach reduces annotation effort while maintaining high-quality labels. However, they didn't provide feedback to users.

Label Assistant [24] presents a sketch-based labeling tool to assist the annotation process in image segmentation tasks, especially for deep learning applications. The proposed workflow integrates various methods, including pre-labeling, image pre-processing, and post-assistance to aid annotators in labeling complex image datasets efficiently. The authors demonstrate the effectiveness of the workflow on two biomedical image segmentation datasets, showing that their approach reduces annotation effort while maintaining high-quality labels. However, they didn't provide feedback to users.


## Quote


a web-based tool, FreeLabel, for interactive annotation that is shown to be intuitive and effective, with users obtaining high-quality segmentations in an average time of 60 seconds per object for the PASCAL dataset


## Discussion


Cette étude présente EasyLabel, une méthode semi-automatique d'annotation pixel par pixel de données RGB-D au niveau objet, qui exploite les décalages spatiaux dans les données de profondeur lors de l'ajout séquentiel d'objets dans une scène, sans nécessiter de modèles 3D d'objets ni de matériel autre qu'un capteur de profondeur unique. À partir de cet outil, les auteurs ont constitué l'Object Clutter Indoor Dataset (OCID, N=2346), un jeu de données couvrant une variété d'objets, d'arrière-plans et de conditions d'éclairage, permettant d'évaluer systématiquement des méthodes de segmentation d'objets face à l'encombrement (clutter), à la distance à la scène, aux structures de support et à la forme des objets. Les résultats montrent que les méthodes reposant principalement sur l'information RGB (par exemple GCUT) se dégradent particulièrement dans les scènes fortement encombrées, texturées ou présentant une faible différenciation chromatique entre objets et arrière-plan, tandis que les approches fondées sur la géométrie (par exemple LCCP) sont plus robustes dans ces conditions. Les travaux futurs visent à corriger le déséquilibre du jeu de données OCID, à l'enrichir de contenus plus exigeants pour les méthodes géométriques, et à étendre le volume de données annotées via la propagation d'étiquettes vers la reconstruction de scène (notamment en combinaison avec LabelFusion), afin d'atteindre l'échelle nécessaire à l'entraînement d'approches d'apprentissage profond.


## Conclusion


We introduced FreeLabel, an interactive interface for fast and high-quality annotation of image segmentation datasets. In contrast to annotation tools that require drawing polygons fully enclosing objects to be segmented, FreeLabel simplifies the user interactions to freehand scribbles and straight lines. By means of the unsupervised algorithm known as RGR, such inputs are grown into segmentation masks that tightly adhere to actual object boundaries. FreeLabel has a modular design and relies solely on open-source libraries, as we aim at a publicly available tool that can be easily adapted for annotation of a wide range of datasets. Its web-based arrangement can be deployed both locally or in external servers, allowing annotations through both private (confidential) or crowdsourced strategies. Our experiments demonstrate that segmentations with high overlap to ground-truth annotations of the PASCAL dataset can be obtained in a matter of seconds. Through short tutorial videos and a game-like version of FreeLabel, users quickly learned how to use the tool and were capable of properly annotating significantly different datasets.


## Raw_Related_Work


Annotation tools: Many efforts focus on improving annotation tools to generate more data for deep learning training, but most of the annotation tools are focusing on images. VIA [12] provides a simple yet powerful webpage-based tool for drawing bounding boxes and polygons on images. Later works such as PolygonRNN [13], [14] seek to utilize more advanced algorithms to facilitate and accelerate human annotations. For video annotation, VATIC [15] integrates tracking (mainly linear interpolation) to reduce annotating repeated entities in consecutive frames. For autonomous driving applications, Yu et al. propose Scalabel [16], a package of tools that support annotating bounding boxes and semantic masks on images. Few works have focused on building LiDAR annotation tools. The Apolloscape [6] dataset's annotation pipeline uses sensor fusion and image-based detection to generate labels through images. But their 3D annotations are for static backgrounds instead of moving objects. [17] adopts a

Annotation tools: Many efforts focus on improving annotation tools to generate more data for deep learning training, but most of the annotation tools are focusing on images. VIA [12] provides a simple yet powerful webpage-based tool for drawing bounding boxes and polygons on images. Later works such as PolygonRNN [13], [14] seek to utilize more advanced algorithms to facilitate and accelerate human annotations. For video annotation, VATIC [15] integrates tracking (mainly linear interpolation) to reduce annotating repeated entities in consecutive frames. For autonomous driving applications, Yu et al. propose Scalabel [16], a package of tools that support annotating bounding boxes and semantic masks on images. Few works have focused on building LiDAR annotation tools. The Apolloscape [6] dataset's annotation pipeline uses sensor fusion and image-based detection to generate labels through images. But their 3D annotations are for static backgrounds instead of moving objects. [17] adopts a


## Insight


methodology: Le DeepAL combine l’extraction de caractéristiques en haute dimension du deep learning avec le potentiel de l’active learning à réduire les coûts d’annotation, particulièrement prometteur lorsque les labels exigent une expertise élevée.


## Raw_Related_Works


Visual datasets are necessary for numerous recognition tasks in computer vision. Especially with the advent of deep learning methods, large scale visual datasets, such as [8,24,26], are essential for learning high-level image representations. They are generalpurpose and include millions of images with image-level categorical labels. These large datasets with image-level labels are useful in learning representations for image recognition, but most of the complex visual understanding tasks in the real world require more fine-grained recognition such as object localization and segmentation [10]. Our proposed dataset provides these multi-granularity annotations for more in-depth visual reasoning. In addition, we provide these annotations in the context of videos, which provides an additional dimension of visual information. Although large video datasets exist, such as [5,1,19], they usually are restricted to image-level labels.

Visual datasets are necessary for numerous recognition tasks in computer vision. Especially with the advent of deep learning methods, large scale visual datasets, such as [8,24,26], are essential for learning high-level image representations. They are generalpurpose and include millions of images with image-level categorical labels. These large datasets with image-level labels are useful in learning representations for image recognition, but most of the complex visual understanding tasks in the real world require more fine-grained recognition such as object localization and segmentation [10]. Our proposed dataset provides these multi-granularity annotations for more in-depth visual reasoning. In addition, we provide these annotations in the context of videos, which provides an additional dimension of visual information. Although large video datasets exist, such as [5,1,19], they usually are restricted to image-level labels.


## Raw_Full_Text


sur le ratio moyen de déséquilibre). 1
ABSTRACT
Rebalancing Label Distribution while Eliminating Inherent Waiting Time in Multi Label Active
Learning applied to Transformers.
Data annotation is crucial for machine learning, notably in technical domains, where the quality and
quantity of annotated data, significantly affect effectiveness of trained models. Employing humans
is costly, especially when annotating for multi-label classification, as instances may bear multiple
labels. Active Learning (AL) aims to alleviate annotation costs by intelligently selecting instances for
annotation, rather than randomly annotating. Recent attention on transformers has spotlighted the
potential of AL in this context. However, in practical settings, implementing AL faces challenges
beyond theory. Notably, the gap between AL cycles presents idle time for annotators. To address this
issue, we investigate alternative instance selection methods, aiming to maximize annotation efficiency
by seamlessly integ


## Raw_Introduction


In this paper, we propose an annotation process based on Active Learning (AL) [7,33] to make the data annotation process for learning deep pose estimation models faster and more cost-effective. Our AL based approach focus the annotation budget (time and cost) on the most valuable samples.

In this paper, we propose an annotation process based on Active Learning (AL) [7,33] to make the data annotation process for learning deep pose estimation models faster and more cost-effective. Our AL based approach focus the annotation budget (time and cost) on the most valuable samples.