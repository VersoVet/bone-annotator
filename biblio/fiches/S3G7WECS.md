# Active-Supervised Model for Intestinal Ulcers Segmentation Using Fuzzy Labeling.



## Resume


Active-Supervised Model for Intestinal Ulcers Segmentation Using Fuzzy Labeling.

Inflammatory bowel disease (IBD) is a chronic inflammatory condition of the intestines with a rising global incidence. Colonoscopy remains the gold standard for IBD diagnosis, but traditional image-scoring methods are subjective and complex, impacting diagnostic accuracy and efficiency. To address these limitations, this paper investigates machine learning techniques for intestinal ulcer segmentation, focusing on multi-category ulcer segmentation to enhance IBD diagnosis. We identified two primary challenges in intestinal ulcer segmentation: 1) labeling noise, where inaccuracies in medical image annotation introduce ambiguity, hindering model training, and 2) performance variability across datasets, where models struggle to maintain high accuracy due to medical image diversity. To address these challenges, we propose an active ulcer segmentation algorithm based on fuzzy labeling. A collaborative training segmentation model is designed to utilize pixel-wise confidence extracted from fuz

Fuzziness-based active learning framework to enhance hyperspectral image classification performance for discriminative and generative classifiers

Adapting Segment Anything Model for Ulcer Segmentation in Inflammatory Bowel Disease.

Inflammatory Bowel Disease (IBD) is a widespread gastrointestinal disorder characterized by inflammation and ulceration, affecting millions of individuals. Mucosal injury assessment through colonoscopy plays a crucial role in determining disease severity and therapeutic efficacy in IBD. This study draws inspiration from the Segment Anything Model (SAM) framework and tailors it for ulcer segmentation using a Parameter-Efficient Transfer Learning (PETL) approach and incorporating binary cross-entropy loss with boundary loss. Comparative assessments against state-of-the-art UNet-based convolutional neural network models underscore SAM's superior performance, especially when faced with limited training samples. Our ulcer segmentation models demonstrate Dice, IoU, and 95%HD scores of 61.92±0.69, 75.18±0.38, and 10.07±0.05 in the colon dataset, and 55.60±0.82, 77.00±0.67, and 7.74±0.23 in the ileum dataset, respectively. This study highlights the potential of our approach to significantly en

Retraction Note: Fuzzy rank correlation-based segmentation method and deep neural network for bone cancer identification

RETRACTED ARTICLE: Fuzzy rank correlation-based segmentation method and deep neural network for bone cancer identification

Suggestive Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

Recent Advancements and Future Prospects in Active Deep Learning for Medical Image Segmentation and Classification

Evaluating Iterative Deep Learning as a Labeling-Efficient Strategy for Tubular Segmentation in Digital Nephropathology

Active learning for accuracy enhancement of semantic segmentation with CNN-corrected label curations: Evaluation on kidney segmentation in abdominal CT.

Segmentation is fundamental to medical image analysis. Recent advances in fully convolutional networks has enabled automatic segmentation; however, high labeling efforts and difficulty in acquiring sufficient and high-quality training data is still a challenge. In this study, a cascaded 3D U-Net with active learning to increase training efficiency with exceedingly limited data and reduce labeling efforts is proposed. Abdominal computed tomography images of 50 kidneys were used for training. In stage I, 20 kidneys with renal cell carcinoma and four substructures were used for training by manually labelling ground truths. In stage II, 20 kidneys from the previous stage and 20 newly added kidneys were used with convolutional neural net (CNN)-corrected labelling for the newly added data. Similarly, in stage III, 50 kidneys were used. The Dice similarity coefficient was increased with the completion of each stage, and shows superior performance when compared with a recent segmentation netwo

Attention, Suggestion and Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

Fuzzy-Label Weighted Deep Learning Classification for CT Image Quality Evaluation.

This paper proposes a fuzzy-label weighted deep learning-based image classification approach for assessing computed tomography (CT) image quality. More specifically, we want to determine if a captured CT image passes Quality Assessment (QA) with a certain radiation dose. Our contributions here include proposing a fuzzy-label weighting method and introduces the concept of a "fuzzy-label" (to reflect the confidence of the ground-truth annotation by annotator) to aid in the training of deep learning-based image classification. We proposed an ensemble/assimilation method to determine the image quality at entire CT image-level using CT windowing (i.e. clipping of the CT image to 8-bit grayscale with respect to the various window-width (WW) and window-length (WL)), similar to what a human would do manually to assess the CT image quality in the factory setting. Experimental results showed that our proposed fuzzy-label weighted deep learning-based image classification approach (trained using a

Diminishing Uncertainty Within the Training Pool: Active Learning for Medical Image Segmentation.

Active learning is a unique abstraction of machine learning techniques where the model/algorithm could guide users for annotation of a set of data points that would be beneficial to the model, unlike passive machine learning. The primary advantage being that active learning frameworks select data points that can accelerate the learning process of a model and can reduce the amount of data needed to achieve full accuracy as compared to a model trained on a randomly acquired data set. Multiple frameworks for active learning combined with deep learning have been proposed, and the majority of them are dedicated to classification tasks. Herein, we explore active learning for the task of segmentation of medical imaging data sets. We investigate our proposed framework using two datasets: 1.) MRI scans of the hippocampus, 2.) CT scans of pancreas and tumors. This work presents a query-by-committee approach for active learning where a joint optimizer is used for the committee. At the same time,

On Combining Multiple-Instance Learning and Active Learning for Computer-Aided Detection of Tuberculosis.

The major advantage of multiple-instance learning (MIL) applied to a computer-aided detection (CAD) system is that it allows optimizing the latter with case-level labels instead of accurate lesion outlines as traditionally required for a supervised approach. As shown in previous work, a MIL-based CAD system can perform comparably to its supervised counterpart considering complex tasks such as chest radiograph scoring in tuberculosis (TB) detection. However, despite this remarkable achievement, the uncertainty inherent to MIL can lead to a less satisfactory outcome if analysis at lower levels (e.g., regions or pixels) is needed. This issue may seriously compromise the applicability of MIL to tasks related to quantification or grading, or detection of highly localized lesions. In this paper, we propose to reduce uncertainty by embedding a MIL classifier within an active learning (AL) framework. To minimize the labeling effort, we develop a novel instance selection mechanism that exploits

Dual Annotation Learning with Selective Uncertainty for Medical Image Segmentation with Noisy Labels

An improved algorithm for interactive medical image segmentation based on Intelligent scissors

Active learning for hierarchical multi-label classification

Model-data-driven adversarial active learning for brain tumor segmentation.

Active learning (AL) attempts to select informative samples in a dataset to minimize the number of required labels while maximizing the performance of the model. Current AL in segmentation tasks is limited to the expansion of popular classification-based methods including entropy, MC-dropout, etc. Meanwhile, most applications in the medical field are simply migrations that fail to consider the nature of medical images, such as high class imbalance, high domain difference, and data scarcity. In this study, we address these challenges and propose a novel AL framework for medical image segmentation task. Our approach introduces a pseudo-label-based filter addressing excessive blank patches in medical abnormalities segmentation tasks, e.g., lesions, and tumors, used before the AL selection. This filter helps reduce resource usage and allows the model to focus on selecting more informative samples. For the sample selection, we propose a novel query strategy that combines both model impact a

HiDiff: Hybrid Diffusion Framework for Medical Image Segmentation

Combining Image and Region Uncertainty-Based Active Learning for Melanoma Segmentation

Semi-supervised deep learning with malignet for bone lesion instance segmentation using bone scintigraphy

One challenge in applying deep learning to medical imaging is the lack of labeled data. Although large amounts of clinical data are available, acquiring labeled image data is difficult, especially for bone scintigraphy (i.e., 2D bone imaging) images. Bone scintigraphy images are generally noisy, and ground-truth or gold standard information from surgical or pathological reports may not be available. We propose a novel neural network model that can segment abnormal hotspots and classify bone cancer metastases in the chest area in a semi-supervised manner. Our proposed model, called MaligNet, is an instance segmentation model that incorporates ladder networks to harness both labeled and unlabeled data. Unlike deep learning segmentation models that classify each instance independently, MaligNet utilizes global information via an additional connection from the core network. To evaluate the performance of our model, we created a dataset for bone lesion instance segmentation using labeled an

Foundation model-guided multi-view semi-supervised CT segmentation of liver tumors in resource-constrained settings.

We present a label-efficient pipeline for CT auto-segmentation in resource-constrained settings. The framework couples a semi-supervised segmentation backbone with a foundation model-guided regularizer to strengthen the learning from scarce annotations. To better exploit volumetric context, we introduce a multi-view collaborative learning procedure that performs view-specific inference to form a unified supervision signal that suppresses view-dependent noise and improves mask fidelity. We evaluate on a public CT benchmark with varying numbers of labeled scans. In the highly label-limited regime, the approach yields strong accuracy with average Dice 83.79% for the liver and 60.08% for the tumor using 20 labeled cases, outperforms existing segmentation methods. By reducing contouring from hours to seconds, improving small-structure recovery and boundary fidelity, and requiring no interactive prompts, the method offers a plug-and-play path to deployment and a reliable basis for downstream

Progressive medical image annotation with convolutional neural network-based interactive segmentation method

Artificial Intelligence and Cellular Segmentation in Tissue Microscopy Images

Active learning using adaptable task-based prioritisation.

Supervised machine learning-based medical image computing applications necessitate expert label curation, while unlabelled image data might be relatively abundant. Active learning methods aim to prioritise a subset of available image data for expert annotation, for label-efficient model training. We develop a controller neural network that measures priority of images in a sequence of batches, as in batch-mode active learning, for multi-class segmentation tasks. The controller is optimised by rewarding positive task-specific performance gain, within a Markov decision process (MDP) environment that also optimises the task predictor. In this work, the task predictor is a segmentation network. A meta-reinforcement learning algorithm is proposed with multiple MDPs, such that the pre-trained controller can be adapted to a new MDP that contains data from different institutes and/or requires segmentation of different organs or structures within the abdomen. We present experimental results usin

Panoptic Segmentation and Labelling of Lumbar Spine Vertebrae using Modified Attention Unet

Segmentation and labeling of vertebrae in MRI images of the spine are critical for the diagnosis of illnesses and abnormalities. These steps are indispensable as MRI technology provides detailed information about the tissue structure of the spine. Both supervised and unsupervised segmentation methods exist, yet acquiring sufficient data remains challenging for achieving high accuracy. In this study, we propose an enhancing approach based on modified attention U-Net architecture for panoptic segmentation of 3D sliced MRI data of the lumbar spine. Our method achieves an impressive accuracy of 99.5\% by incorporating novel masking logic, thus significantly advancing the state-of-the-art in vertebral segmentation and labeling. This contributes to more precise and reliable diagnosis and treatment planning.

An Active Learning Pipeline for Biomedical Image Instance Segmentation with Minimal Human Intervention

Biomedical image segmentation is critical for precise structure delineation and downstream analysis. Traditional methods often struggle with noisy data, while deep learning models such as U-Net have set new benchmarks in segmentation performance. nnU-Net further automates model configuration, making it adaptable across datasets without extensive tuning. However, it requires a substantial amount of annotated data for cross-validation, posing a challenge when only raw images but no labels are available. Large foundation models offer zero-shot generalizability, but may underperform on specific datasets with unique characteristics, limiting their direct use for analysis. This work addresses these bottlenecks by proposing a data-centric AI workflow that leverages active learning and pseudo-labeling to combine the strengths of traditional neural networks and large foundation models while minimizing human intervention. The pipeline starts by generating pseudo-labels from a foundation model, w

Beyond Cats and Dogs: Semi-supervised Classification of fuzzy labels with overclustering

A long-standing issue with deep learning is the need for large and consistently labeled datasets. Although the current research in semi-supervised learning can decrease the required amount of annotated data by a factor of 10 or even more, this line of research still uses distinct classes like cats and dogs. However, in the real-world we often encounter problems where different experts have different opinions, thus producing fuzzy labels. We propose a novel framework for handling semi-supervised classifications of such fuzzy labels. Our framework is based on the idea of overclustering to detect substructures in these fuzzy labels. We propose a novel loss to improve the overclustering capability of our framework and show on the common image classification dataset STL-10 that it is faster and has better overclustering performance than previous work. On a real-world plankton dataset, we illustrate the benefit of overclustering for fuzzy labels and show that we beat previous state-of-the-ar


## Quote


This paper examining the bone cancer by using the Open-Access Medical Image Repositories dataset with the help of the intuitionistic fuzzy rank correlation along with deep neural networks.

The proposed methodology is divided into data pre-processing / cleaning, fine-tuning the BERT models, and developing the fuzzy-based ensemble of fine-tuned models.

Thus, the intuitionistic fuzzy rank correlation along with deep neural network-based tumor prediction system ensures high prediction rate (99.19%) while recognizing the bone cancer due to the low error rate along with the effective mathematical-based segmentation process.