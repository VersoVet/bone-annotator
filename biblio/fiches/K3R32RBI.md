# Open RGB imaging workflow for morphological and morphometric analysis of fruits using deep learning: a case study on almonds.

**Auteurs** : Mas-Gómez J, Rubio M, Dicenta F, Martínez-García PJ.
**Année** : 2026
**DOI** : 10.1093/gigascience/giaf157

## Résumé

<h4>Background</h4>High-throughput phenotyping is addressing the current bottleneck in phenotyping within breeding programs. Imaging tools are becoming the primary resource for improving the efficiency of phenotyping processes and providing large datasets for genomic selection approaches. The advent of artificial intelligence (AI) brings new advantages by enhancing phenotyping methods using imaging, making them more accessible to breeding programs. In this context, we have developed an open Python workflow for analyzing morphology, color, and morphometric traits using AI, which can be applied to fruits and other plant organs.<h4>Results</h4>The workflow was implemented in almond (Prunus dulcis (Mill.) D. A. Webb), a species where breeding efficiency is critical due to its long breeding cycle. Over 25,000 kernels, more than 20,000 nuts, and over 600 individuals were phenotyped, making this the largest morphological study conducted in almond so far. The best segmentation and reconstructi

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Populations used in this study and the number of individuals studied per year

| Year | 2022 |  | 2023 |  | Unique genotypes |
| --- | --- | --- | --- | --- | --- | --- |
| Family | Shell | Kernel | Shell | Kernel | Shell | Kernel |
| Germplasm collection | 85 | 85 | 74 | 91 | 99 | 99 |
| Antoñeta × Marcona | 6 | 6 | 19 | 19 | 19 | 19 |
| Antoñeta × Penta | 161 | 161 | 142 | 142 | 183 | 183 |
| Antoñeta × Tardona | 57 | 57 | 56 | 53 | 71 | 70 |
| Florida × Marcona | 17 | 17 | 43 | 43 | 44 | 44 |
| Desmayo × R1000 | 198 | 198 | 187 | 194 | 223 | 223 |
| Marcona × S4017 | 0 | 0 | 26 | 27 | 26 | 27 |
| Total | 524 | 524 | 547 | 569 | 665 | 665 |

## Performance for different datasets and reconstruction methods, including reconstruction errors

|  |  |  |  | Total phenotyped | Error |
| --- | --- | --- | --- | --- | --- |
| Method | Dataset | Errors | Total elements | elements | percentage |
| Slice_predict_reconstruct + Watershed | Kernel-2022 | 5 | 10,184 | 10,180 | .05% |
|  | Kernel-2023 | 264 | 15,568 | 15,304 | .70% |
|  | Shell-2022 | 4 | 10,364 | 10,360 | .04% |
|  | Shell-2023 | 60 | 10,945 | 10,885 | .55% |
| SAHI | Kernel-2022 | 14 | 10,184 | 10,178 | .14% |
|  | Kernel-2023 | 139 | 15,568 | 15,429 | .89% |
|  | Shell-2022 | 304 | 10,364 | 10,288 | .93% |
|  | Shell-2023 | 44 | 10,945 | 10,902 | .40% |

### Formule


$$Y ijk = μ + G i + Y j + ε ijk (1)$$

### Formule


$$σ 2 G σ 2 G + σ 2 e (2$$

### Formule


$$)$$

### Formule


$$σ 2 G: Genetic variance σ 2 e: Residual variance$$
