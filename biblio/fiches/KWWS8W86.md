# Oil Palm Fruits Dataset in Plantations for Harvest Estimation Using Digital Census and Smartphone.

**Auteurs** : Suharjito, Naftali MG, Hugo G, Priyadi MRA, Asrol M, Utama DN.
**Année** : 2025
**DOI** : 10.1038/s41597-025-05227-x

## Résumé

This article presents a dataset of oil palm Fresh Fruit Bunches (FFBs) images from commercial plantations in Central Kalimantan, Indonesia, focusing on five maturity stages: Unripe, Underripe, Ripe, Flower, and Abnormal. The data collection involved smartphone video recordings of unharvested trees from multiple angles under varying conditions. Video frames were extracted and expertly annotated using Computer Vision Annotation Tool (CVAT), with annotations exported in Common Objects in Context (COCO) format suitable for object detection tasks. It has 10,207 images in its training set, 2,896 in the validation set, and 1,400 in the test set, which are supplemented using data augmentation to handle class imbalance and increase variation. These images have real-world complications arising from partial visibility, low contrast, occlusion, and blurriness. It forms the basis that will support the development of deep learning models for detection and classification of FFB, particularly for moni

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Dataset Type Dataset Settings FFB State Number of Classes Name of Classes Total Images

| Detection 11 | Single FFB per photo | Unharvested | 4 | 1045 (Very Raw), 1045 (Underripe), 1045 (Ripe II), 1045 (Overripe) | 4180 |
| --- | --- | --- | --- | --- | --- |
| Detection 12 | Oil palm plantation (close-up and distant views of the FFBs) | Unharvested | 2 | 240 (Ripe) and 250 (Unripe) | 490 |
| Classification 13 | Single FFB per photo | Harvested | 3 | 39 (Unripe), 40 (Ripe), and 41 (Overripe) | 120 |
| Classification 14 | Perpendicularly 1 meter above the ground Unharvested | 4 | 30 (Raw Bunch), 30 (Under Ripe Bunch), 60 (Ripe Bunch), 60 (Over Ripe Bunch) | 180 |
| Detection 15 | Multiple harvested oil palm (but mostly one fruit per picture) | Harvested | 6 | 1130 (Unripe), 1289 (Underripe), 1880 (Ripe), (Abnormal FFB) 1162 (Overripe), 473 (Empty Bunch), 1237 | 7171 |
| Classification 16 | Single FFB per photo | Harvested | 5 | 130 (Unripe), 131 (Underripe), 130 (Ripe), 130 (Overripe), 130 (Abnormal) | 653 |
| Detection (Our Dataset) | Oil palm plantation (close-up and distant views of the FFBs), unharvested | Unharvested | 5 | 2989 (Ripe), 1803 (Underripe), 7453 (Unripe), 1554 (Flower), 704 (Abnormal) | 14503 |

## Distribution of pre-processing dataset results.

|  | Train | Validation | Test |
| --- | --- | --- | --- |
| Ripe | 2354 | 443 | 192 |
| Underripe | 1324 | 298 | 181 |
| Unripe | 4990 | 1699 | 764 |
| Flower | 1121 | 251 | 182 |
| Abnormal | 418 | 205 | 81 |
| Total | 10207 | 2896 | 1400 |

## Effect of image augmentation on model performance.

|  | YOLOV8n | YOLOV8s |
| --- | --- | --- |
| Max Epoch | 100 | 100 |
| Batch size | 64 | 16 |
| Height | 640 | 640 |
| Width | 640 | 640 |
| Channels | 3 | 3 |
| Learning Rate | 0.01 | 0.01 |
| Optimizer | SGD | SGD |
| Momentum | 0.9 | 0.9 |
| Workers | 8 | 8 |
| Seed | 10 | 10 |

## Training, Validation, and Testing Results of YOLOv8 models.

|  | YOLOV8n YOLOV8s |
| --- | --- | --- |
| GPU used | 9.6gb | 4.5GB |
| mAP_0.5 | 0.735 | 0.745 |
| mAP_0.5:0.95 | 0.480 | 0.480 |
| Precision | 0.725 | 0.738 |
| Recall | 0.711 | 0.719 |
| F1 score | 0.718 | 0.728 |
| FPS | 90 | 36 |
| Train box loss | 0.690 | 0.684 |
| Train class loss | 0.460 | 0.563 |
| Train object loss | 1.175 | 1.135 |
| Val. box loss | 1.251 | 1.260 |
| Val. class loss | 0.924 | 0.923 |
| Val. object loss | 1.456 | 1.490 |
| Size model | 6MB | 21 mb |
