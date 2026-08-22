# An annotated dataset of images of Chinese giant salamanders.

**Auteurs** : Yang X, Chen J, Lu D, Sun N, Xie M, Qian H.
**Année** : 2026
**DOI** : 10.1016/j.dib.2026.112552

## Résumé

The Chinese giant salamander is classified as a Class II protected species in China and is recognized as critically endangered by the International Union for Conservation of Nature (IUCN). Due to their unique behavioral patterns, wild Chinese giant salamanders are primarily nocturnal and inhabit areas characterized by complex terrain, which results in limited detection coverage and significant challenges in observation. Consequently, images of wild Chinese giant salamanders are exceedingly rare, and the scarcity of existing data impedes the advancement and application of deep learning-based object detection models. This study constructs and releases a specialized dataset for Chinese giant salamanders, comprising 1386 images and a total of 1397 annotated bounding boxes. All images represent diverse field scenarios and are meticulously annotated in accordance with YOLO (You Only Look Once) labeling specifications. Annotation files are provided in both PASCAL VOC (Visual Object Classes) a

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## ). Published by Elsevier Inc. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ) This dataset can facilitate the work of researchers for the research community to work in computer vision, research related to Chinese giant salamanders, and conservation bases related to Chinese giant salamanders.

| Specifications Table |  |
| --- | --- |
| Subject | Computer Sciences |
| Specific subject area | An annotated dataset of images of Chinese giant salamanders. |
| Type of data | image (jpg, png) and corresponding annotation file |
| Data collection | The image is a video extraction frame taken using an EOS RP (Canon Corporation, |
|  | Tokyo, Japan) camera and a surveillance camera of the TL-IPC642-A (Pulian |
|  | Technology Co., Ltd., Shenzhen, China) model. Each image of this dataset contains |
|  | at least one Chinese giant salamander, and there are 1386 images and 1397 |
|  | annotated bounding boxes in the entire dataset. |
| Data source location | Xianfeng County, Hubei Province, China |
| Data accessibility | Repository name: Mendeley Data |
|  | Data identification number: 10.17632/xzvdkhr4bg.1 |
|  | better Chinese giant |
| salamander detection models. |
| • The dataset presented includes photographs of Chinese giant salamanders taken in various |
| complex conditions in the wild. This dataset can be used for a variety of applications, such |
| as image processing, image segmentation, machine learning, and deep learning, for detecting |
| Chinese giant salamanders in the wild. |
| • The dataset contains annotated images of Chinese giant salamanders, providing a valuable |
| resource for developing and refining machine learning models for application in classification |
| and regression. The multiple standardized formats allow for easy integration of datasets into |
| object detection frameworks such as YOLO v8, YOLO v11, and more, supporting the training |
| and application of compatible models and facilitating research expansion and innovation. |
| • Object detection models trained using this dataset can be integrated into web applica- |
| tions, invoked within custom-developed software, or deployed on edge hardware after model |
| lightweighting. All these deployment methods enable real-time detection of Chinese giant |
| salamanders or large-scale image detection of Chinese giant salamanders. |
| • |  |

## Brief description of the dataset file.

| No. | Name | Type/Format | Description | Size |
| --- | --- | --- | --- | --- |
| 1 | Full dataset | Root folder | Easily packaged for download | 3.06GB |
| 2 | Original image | Compressed (.zip) folder: 1386 | Original camera image, | 941MB |
|  |  | JPG images | containing many images of |  |
|  |  |  | Chinese giant salamanders |  |
| 3 | Annotation file | Three subfolders: JSON, XML, | Annotate the original image | 1.23GB |
|  |  | and TXT, for single-class | with X-AnyLabeling and label it |  |
|  |  | annotation files for all images | as "Chinese giant salamander" |  |
|  |  |  | in the annotation file in a |  |
|  |  |  | different format |  |
| 4 | Image of a | The root folder contains three | According to the ratio of 7:2:1, | 941MB |
|  | Chinese giant | subfolders: image, label, | 1386 JPG format images are |  |
|  | salamander | Original image, and 1386 JPG | divided into "train", "test", and |  |
|  | marked for | images are included in | "val" for easy training |  |
|  | training | "Original image" |  |  |

## Distribution of images in the chinese giant salamander dataset under different shooting environments and lighting conditions.

| Shooting Environment | Lighting conditions | Number | proportion |
| --- | --- | --- | --- |
|  |  | (pieces) |  |
| Indoor Environment | Normal lighting | 30 | 2.16 % |
| Outdoor environment | Normal daylight | 572 | 41.27 % |
|  | illumination |  |  |
|  | Low-light environment | 784 | 56.57 % |
| Total |  | 1386 | 100 % |
