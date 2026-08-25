# LabelBOT: A Human-in-the-Loop Classification Assistance in the BIIGLE Image Annotation Tool

**Auteurs** : Gaby Kourie, Martin Zurowietz, Daniel Langenkamper, Davide Brembilla, Tim W. Nattkemper
**Année** : 2026
**DOI** : 10.1109/access.2026.3688574

## Résumé

In marine science and engineering, growing volumes of imaging data are used in exploration and monitoring. The process of manual annotation of this data (i.e. marking and describing objects of interest with labels), to extract quantitative data or to collect many examples for AI applications, is a very time-consuming task and requires a high level of expert experience to achieve annotations of sufficient quality and consistency. To address this challenge, we introduce LabelBOT, a human-in-the-loop classification annotation assistant that supports and accelerates the annotation process by providing relevant, real-time label suggestions. Rather than replacing human annotators, LabelBOT functions as a collaborative tool to reduce repetitive work, benefiting both experts and non-experts. LabelBOT operates on 384-dimensional feature vectors extracted using the DINOv2 self-supervised model and performs classification through cosine similarity-based Approximate-Nearest Neighbors (ANN) using t

## Méthodologie

{'study_design': "Processus divisé en deux étapes: Stage I, traitement de l'entrée (une ROI) pour générer un vecteur de caractéristiques transmis à Stage II; Stage II, utilisation du vecteur de caractéristiques pour effectuer une recherche vectorielle afin de trouver la ROI annotée la plus similaire dans la base de données", 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [], 'qualitative_findings': ["Une matrice de confusion a été calculée pour l'évaluation Top-1", "Une expérience additionnelle sur OBSEA a été menée en utilisant des vecteurs de caractéristiques à 512 dimensions générés avec BIOCLIP, afin d'évaluer l'impact de la représentation vectorielle des caractéristiques", "L'index HNSW pour la recherche ANN a été construit sur le split d'entraînement de chaque dataset"], 'main_findings': ["Présentation des résultats de l'évaluation de LabelBOT sur deux datasets, ainsi que de l'interface utilisateur finale implémentée", "Une analyse de workflow simulé a été conduite pour estimer la réduction de l'effort de sélection des labels lors de l'utilisation de LabelBOT"]}

## Conclusions

LabelBOT assists BIIGLE users by providing relevant Top-3 label suggestions that help reduce annotation effort and support informed decisions, especially in ambiguous cases Combining in-browser ONNX inference (with optional WebGPU acceleration) and fast HNSW-based nearest-neighbor search on the server side allows the system to respond in less than a second on average The efficient response time allows annotators to move quickly through large collections of images without waiting for slow server requests The user interface supports the workflow by keeping interactions simple and avoiding unnecessary steps Combining existing methods while paying attention to system performance and interface design can create an efficient and user-friendly annotation assistance tool Although this work focuses on marine imaging, the same approach can support many other fields where image annotation is still time-consuming

### Formule


$$Î = C(I , P) (1)$$

### Formule


$$Ĩ c (i) = Ĩ c (i) 255 -µ c σ c , c ∈ {R, G, B}, i = 1, . . . , 224 2(2)$$

### Formule


$$f input = ONNX DINOv2-ViT-S/14 (T Ĩ )(3)$$

### Formule


$$Accuracy = TP + TN TP + TN + FP + FN ,(4)$$

### Formule


$$Recall = TP TP + FN ,(5)$$

### Formule


$$Precision = TP TP + FP ,(6)$$

### Formule


$$F1 score = 2 • Precision • Recall Precision + Recall(7)$$

### Formule


$$AIT P = 1 n n i=1 IT P (T Ĩ ) (8) ART = 1 n n i=1 RT (r)(9)$$

### Formule


$$1) USABILITY 1)$$

### Formule


$$LST = 0.61 • 0 + 0.29 • 1 + 0.10 • 3.5 ≈ 0.64 s (10$$

### Formule


$$)$$
