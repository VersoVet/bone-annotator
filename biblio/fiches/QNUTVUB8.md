# A deep learning-based iterative digital pathology annotation tool

**Auteurs** : Mustafa I. Jaber, Bing Song, Liudmila Beziaeva, Christopher W. Szeto, Patricia Spilman, Phil Yang, Patrick Soon‐Shiong
**Année** : 2021
**DOI** : 10.1101/2021.08.23.457396

## Résumé

ABSTRACT
                Well-annotated exemplars are an important prerequisite for supervised deep learning schemes. Unfortunately, generating these annotations is a cumbersome and laborious process, due to the large amount of time and effort needed. Here we present a deep-learning-based iterative digital pathology annotation tool that is both easy to use by pathologists and easy to integrate into machine vision systems. Our pathology image annotation tool greatly reduces annotation time from hours to a few minutes, while maintaining high fidelity with human-expert manual annotations. Here we demonstrate that our active learning tool can be used for a variety of pathology annotation tasks including masking tumor, stroma, and lymphocyte-rich regions, among others. This annotation automation system was validated on 90 unseen digital pathology images with tumor content from the CAMELYON16 database and it was found that pathologists’ gold standard masks were re-produced successfully using our tool. That is, an average of 2.7 positive selections (mouse clicks) and 8.0 negative selections (mouse clicks) were sufficient to generate tumor masks similar to pathologists’ gold standard in CAMELYON16 test WSIs. Furthermore, the developed image annotation tool has been used to build gold standard masks for hundreds of TCGA digital pathology images. This set was used to train a convolutional neural network for identification of tumor epithelium. The developed pan-cancer deep neural network was then tested on TCGA and internal data with comparable performance. The validated pathology image annotation tool described herein has the potential to be of great value in facilitating accurate, rapid pathological analysis of tumor biopsies.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Annotation tool performance evaluation

| F1 score | >0.60 >0.65 >0.70 >0.75 >0.80 >0.85 >0.90 |
| --- | --- |
| Tumor selections | 1.54 1.82 2.18 2.73 3.77 4.20 5.00 |
| Nontumor selections | 2.86 4.66 6.60 8.00 12.33 13.39 17.90 |
| % out of 90 WSIs | 100.0 100.0 100.0 98.89 95.56 87.78 75.56 |
