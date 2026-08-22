# High-Resolution Colony Images of Clinically Isolated Bacteria for Automated Detection and Deep Learning.

**Auteurs** : Du J, Yang C, Sun M, Sun Q, Wang M, Ji X, Wang K, Xu J.
**Année** : 2026
**DOI** : 10.1038/s41597-026-07095-5

## Résumé

The observation and analysis of colonies on solid media are key steps in microbiological research. However, traditional manual interpretation methods are inefficient when handling large-scale samples and are prone to subjective bias, making it difficult to meet the demands for efficient, standardized, and traceable detection. Although AI and computer vision offer new opportunities for automated colony analysis, existing datasets are often small, inconsistently collected, and lack sufficient strain diversity, limiting model generalization. Here, we publicly release a large, normalized colony image dataset covering 19 bacterial species and 151 strains from diverse sources, with 50 images per species to capture within-species phenotypic diversity. Images were collected on a closed background under stable lighting and uniform shooting angles following strict protocols, then systematically annotated and augmented to improve usability. In total, the dataset contains 118,442 colony instances,

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## 2. Model performance on the test set (e.g., eca, enc, cst, mmo, etc.).

| types | all | aba | eco | kpn | sau | ses | sma | sep | efa | stm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Precision | 0.979 | 0.981 | 0.978 | 0.991 | 0.969 | 0.988 | 0.987 | 0.991 | 0.996 | 0.979 |
| Recall | 0.946 | 0.996 | 0.992 | 0.999 | 0.991 | 1.000 | 0.98 | 0.979 | 0.756 | 0.993 |
| F1-score | 0.962 | 0.988 | 0.985 | 0.995 | 0.980 | 0.994 | 0.983 | 0.985 | 0.860 | 0.986 |
| mAP50 | 0.98 | 0.995 | 0.995 | 0.994 | 0.995 | 0.995 | 0.989 | 0.991 | 0.94 | 0.994 |
| types | eca | enc | cst | mmo | bce | spy | sag | ppu | spn | bcp |
| Precision | 0.963 | 0.955 | 0.988 | 0.964 | 0.982 | 0.987 | 0.994 | 0.981 | 0.944 | 0.978 |
| Recall | 0.96 | 0.961 | 0.991 | 0.98 | 0.955 | 0.748 | 0.82 | 0.976 | 0.929 | 0.976 |
| F1-score | 0.961 | 0.958 | 0.989 | 0.972 | 0.968 | 0.851 | 0.899 | 0.978 | 0.936 | 0.977 |
| mAP50 | 0.991 | 0.976 | 0.995 | 0.988 | 0.976 | 0.91 | 0.947 | 0.986 | 0.968 | 0.987 |

### Formule


$$A R T I C L E I N P R E S$$
