# OXI: An online tool for visualization and annotation of satellite time series data



## Resume


OXI: An online tool for visualization and annotation of satellite time series data

Satellite telemetry data is a special case of multivariate time series characterized by large volumes (in terms of both the number of series and samples), varying sampling rates (including time gaps), redundant sensors, and many interconnections between the series. Special tools are needed to handle visualization, analysis, and, most importantly, annotation of such data. Manually prepared annotations are crucial when designing and evaluating algorithms for satellite telemetry analysis, including anomaly detection in telemetry data. Although there are many applications for time series analysis, there are no tools that would smoothly handle typical satellite telemetry and at the same time provide a free user-friendly interface accessible from any computer without the need for installation, registration, data sharing, or special training. As a solution to this technology gap, we propose the web-based OXI tool written in JavaScript and publicly available at https://oxi.kplabs.pl/. Based on

An interactive tool for manual, semi-automatic and automatic video annotation

Computer Vision Annotation Tool

LabelMe: Online Image Annotation and Applications

An annotation tool for dermoscopic image segmentation

Speeding up scientific imaging workflows: Design of automated image annotation tool

LabelMe: A Database and Web-Based Tool for Image Annotation

Efficient annotation of image data sets for computer vision applications

Annotating Medical Image Data

An interactive tool for semi-automated leaf annotation

PyTAGIT: a scalable and interactive human-in-the-loop tool for fast image annotation

BDD100K: A Diverse Driving Video Database with Scalable Annotation Tooling.

Diverse Image Annotation

DL-AAT: An Automatic Annotation Tool for Efficient Data Labeling in Vision-Based Systems

vesselr: Gradient and Vesselness Tools for Arrays and NIfTI Images

Web watch: radiographic anatomy on the web

Towards a better understanding of annotation tools for medical imaging: a survey


## Insight


methodology: L'outil couvre à la fois l'annotation spatiale d'images (rectangle, cercle, ellipse, polygone, point, polyligne) et l'annotation temporelle de contenus audio et vidéo.

implications: Les auteurs recommandent l'ajout futur d'une timeline pour améliorer la navigation vidéo, la gestion de l'occlusion entre AOI et la description des relations entre zones annotées.
Au-delà des limitations techniques liées au suivi non-linéaire des objets, les auteurs identifient trois besoins d'amélioration relevant spécifiquement de l'utilisabilité (usability) de l'outil, motivant l'implémentation future d'une timeline. Premièrement, une timeline améliorerait la navigation au sein du fichier vidéo, facilitant le repérage temporel des séquences à annoter. Deuxièmement, elle permettrait d'organiser les AOI selon leur profondeur relative, de sorte que les zones occultées soient correctement positionnées derrière d'autres AOI, ce qui est particulièrement pertinent dans les scènes de vidéosurveillance à forte densité d'objets. Troisièmement, cette fonctionnalité permettrait de décrire explicitement les relations entre AOI, ouvrant la voie à des annotations sémantiquement plus riches, potentiellement utiles pour des analyses relationnelles ou d'interaction entre objets suivis.


## Quote


This library uses annotation tools from the common WSI viewing software Aperio ImageScope [27] for annotation and display of the network predictions. Training, prediction and validation of the network is done via a single python script with a command line interface

To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking.

To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking.

a web-based tool, FreeLabel, for interactive annotation that is shown to be intuitive and effective, with users obtaining high-quality segmentations in an average time of 60 seconds per object for the PASCAL dataset

To assist annotation in more industries, we also provide domainspecific models for remote sensing, medical imaging, industrial quality inspection, and temporal-aware model for videos.

The usage statistics indicate how image annotation is currently performed with a tool such as BIIGLE and how image annotation tools as well as the marine imaging community could further evolve.


## Resultats


VIA se présente comme un outil léger, autonome et hors ligne, prenant en charge diverses formes d'annotation spatiale d'images ainsi que l'annotation temporelle de contenus audio et vidéo. Il permet l'export des annotations en JSON et CSV, le travail collaboratif sur de grands jeux de données, et propose une vue en grille facilitant un flux de travail hybride combinant annotation automatique et correction manuelle.


## Table


Tableau: • NVivo • Oudjat is dedicated to the manual annotation facial expressions of emotion(FEE) • Redesigning video analysis: an interactive ink annotation tool • Rethinking Engagement with Online News through Social and Visual Co-Annotation • Sirio, orione and pan: an integrated web system for ontology-based video search and annotation • Stabilized Annotations for Mobile Remote Assistance • SVAT • The MESH mobile video annotation tool • Timelinely • Tool Eval: Rapid Model-Driven Annotation and Evaluation for Object Detection in Videos • ToolScape: Enhancing the Learning Experience of How-to Videos • VACA: a tool for qualitative video analysis • VAnnotator: Annotations as multiple perspectives of video content • VATIC • VCode and VData: Illustrating a new Framework for Supporting the Video Annotation Workflow • VIA: The VIA Annotation Software for Images, Audio and Video • ViBAT • VideoAnt • VideoJot: A Multifunctional Video Annotation Tool • VidOR: Annotating Objects and Relations in User-Generated Videos • ViTBAT: Video Tracking and Behavior Annotation Tool • VoTT

Tableau: • NVivo • Oudjat is dedicated to the manual annotation facial expressions of emotion(FEE) • Redesigning video analysis: an interactive ink annotation tool • Rethinking Engagement with Online News through Social and Visual Co-Annotation • Sirio, orione and pan: an integrated web system for ontology-based video search and annotation • Stabilized Annotations for Mobile Remote Assistance • SVAT • The MESH mobile video annotation tool • Timelinely • Tool Eval: Rapid Model-Driven Annotation and Evaluation for Object Detection in Videos • ToolScape: Enhancing the Learning Experience of How-to Videos • VACA: a tool for qualitative video analysis • VAnnotator: Annotations as multiple perspectives of video content • VATIC • VCode and VData: Illustrating a new Framework for Supporting the Video Annotation Workflow • VIA: The VIA Annotation Software for Images, Audio and Video • ViBAT • VideoAnt • VideoJot: A Multifunctional Video Annotation Tool • VidOR: Annotating Objects and Relations in User-Generated Videos • ViTBAT: Video Tracking and Behavior Annotation Tool • VoTT


## Raw_Related_Work


Annotation tools: Many efforts focus on improving annotation tools to generate more data for deep learning training, but most of the annotation tools are focusing on images. VIA [12] provides a simple yet powerful webpage-based tool for drawing bounding boxes and polygons on images. Later works such as PolygonRNN [13], [14] seek to utilize more advanced algorithms to facilitate and accelerate human annotations. For video annotation, VATIC [15] integrates tracking (mainly linear interpolation) to reduce annotating repeated entities in consecutive frames. For autonomous driving applications, Yu et al. propose Scalabel [16], a package of tools that support annotating bounding boxes and semantic masks on images. Few works have focused on building LiDAR annotation tools. The Apolloscape [6] dataset's annotation pipeline uses sensor fusion and image-based detection to generate labels through images. But their 3D annotations are for static backgrounds instead of moving objects. [17] adopts a

Annotation tools: Many efforts focus on improving annotation tools to generate more data for deep learning training, but most of the annotation tools are focusing on images. VIA [12] provides a simple yet powerful webpage-based tool for drawing bounding boxes and polygons on images. Later works such as PolygonRNN [13], [14] seek to utilize more advanced algorithms to facilitate and accelerate human annotations. For video annotation, VATIC [15] integrates tracking (mainly linear interpolation) to reduce annotating repeated entities in consecutive frames. For autonomous driving applications, Yu et al. propose Scalabel [16], a package of tools that support annotating bounding boxes and semantic masks on images. Few works have focused on building LiDAR annotation tools. The Apolloscape [6] dataset's annotation pipeline uses sensor fusion and image-based detection to generate labels through images. But their 3D annotations are for static backgrounds instead of moving objects. [17] adopts a