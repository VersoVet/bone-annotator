# VR-based annotation assistance system for volumetric medical image segmentation

**Auteurs** : Mika Anttonen, Dongwann Kang
**Année** : 2025
**DOI** : 10.3837/tiis.2025.04.008

## Résumé

The application of Virtual Reality (VR) in the healthcare sector has been increasingly recognized, particularly in the realms of medical imaging and clinical skill training. Despite the variety of software and tools available for medical imaging on desktop platforms, their VR counterparts often lack advanced features, notably in the area of annotation tools. Existing VR annotation software, while capable of accelerating the annotation process, is hampered by framerate issues. In our work, we introduce two novel methods for annotating medical images in VR, designed to expedite the annotation process while maintaining a satisfactory framerate. Leveraging VR's capability to display medical images in three dimensions, our approach accelerates the area selection process and sustains a higher framerate by reducing the number of objects generated during annotation visualization. Our experiments revealed that our proposed method not only matches the speed of existing VR annotation software but also significantly reduces or even eliminates framerate problems, varying with the visualization technique implemented.

## Méthodologie

{'study_design': None, 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'Vitesse de visualisation Méthode 1 - création de 512 000 cubes', 'value': 'plus rapide que DIVA Cloud', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'While creating 512,000 cubes was quicker than reported speeds for DIVA Cloud, generating 1,000,000 cubes proved excessively slow, indicating that method 1 is more suitable for smaller annotations.'}, {'outcome': 'Vitesse de visualisation Méthode 1 - création de 1 000 000 cubes', 'value': 'excessivement lent', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'generating 1,000,000 cubes proved excessively slow, indicating that method 1 is more suitable for smaller annotations'}, {'outcome': 'Vitesse de visualisation Méthode 2 - comparaison avec Méthode 1 pour 100 000 cubes', 'value': 'méthode 2 plus rapide que méthode 1', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'In contrast, method 2 displayed remarkable speed, even with larger annotations of 1,000,000 cubes, outpacing method 1 for 100,000 cubes.'}, {'outcome': 'Seuil de framerate acceptable', 'value': '90', 'unit': 'FPS', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'The acceptable framerate threshold of 90 FPS is achieved at a frame timing of 11.1ms or lower.'}, {'outcome': 'Frame timing correspondant au seuil de 90 FPS', 'value': '11.1', 'unit': 'ms', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'The acceptable framerate threshold of 90 FPS is achieved at a frame timing of 11.1ms or lower.'}, {'outcome': 'Framerate avant visualisation (les deux méthodes)', 'value': 'valeurs recommandées atteintes', 'unit': 'FPS', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'Our results indicated that recommended framerate values were consistently met prior to visualization for both methods.'}, {'outcome': "Framerate Méthode 1 lors de la visualisation d'annotations", 'value': 'en baisse notable, sous le niveau recommandé (mais meilleur que DIVA Cloud)', 'unit': 'FPS', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'Despite a better performance than DIVA Cloud, the resulting framerate was still below the recommended level.'}, {'outcome': "Framerate Méthode 2 lors de la visualisation d'annotations", 'value': 'proche de 90 FPS, avec fluctuations occasionnelles', 'unit': 'FPS', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'Conversely, method 2 did not significantly impact the framerate, maintaining it close to the 90 FPS benchmark with occasional fluctuations.'}, {'outcome': 'Paramètres de distance testés', 'value': '25, 40, ou 50', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': 'During testing, we created cubic models within a defined area, with the distance parameter set variably at 25, 40, or 50, depending on the test case.'}], 'qualitative_findings': ["L'ajustement des paramètres SteamVR et VIVE console pouvait fluidifier le mouvement de la caméra, mais le mouvement des objets, y compris l'interaction avec le contrôleur, était affecté négativement avec la méthode 1.", "La sélection de zone n'a pas été évaluée quantitativement car elle est intrinsèquement dépendante de l'utilisateur.", "L'exportation des annotations a été évaluée simplement en termes de succès ou d'échec, car ce n'est pas un problème significatif dans les logiciels existants."], 'main_findings': ["La méthode 1 est plus adaptée aux petites annotations car sa vitesse de visualisation se dégrade rapidement avec la taille de l'annotation.", "La méthode 2 est nettement plus efficace pour la création d'annotations, même pour de grandes annotations (1 000 000 cubes).", "La méthode 2 est recommandée pour l'annotation d'images médicales en VR car elle maintient un framerate optimal proche de 90 FPS, contrairement à la méthode 1 dont le framerate chute sous le seuil recommandé lors de la visualisation."]}

## Conclusions

Ce papier a introduit une nouvelle méthode d'annotation d'images médicales en VR visant à résoudre les problèmes de vitesse et de framerate rencontrés dans les logiciels existants La méthode comprend trois composants intégraux : la sélection de zone, la visualisation d'annotation et l'exportation d'annotation Deux méthodes de visualisation distinctes ont été présentées et comparées, chacune avec ses propres forces et faiblesses Le programme a démontré une lecture rapide des valeurs pour la sélection de zone et une exportation réussie des annotations au format de fichier NIfTI L'une des méthodes de visualisation a résolu avec succès les problèmes de framerate associés à DIVA Cloud

## Testing results

| Resolution of medical image(modality) | Annotation size(pixels) | Visualization speed (seconds) Method 1 Method 2 | Framerate, frame timing/FPS Method 1 Method 2 |
| --- | --- | --- | --- | --- | --- |
|  | 125 000 | 5 | 2 | 13.0/76.9 | 10.5/95 |
| 512x512x372(CT) | 512 000 | 130 | 3 | 20.3/49.3 | 11.0/90.9 |
|  | 1 000 000 | 662 | 5 | 30.1/33.2 | 10.8/92 |
| 256x224x37(MR) | 125 000 512 000 | 5 125 | 2 2 | 11.8/83.3 19/52.6 | 10.4/96.1 11.0/90.9 |
|  | 1 000 000 | 640 | 4 | 28/35.7 | 10.9/91.7 |
|  | 125 000 | 6 | 2 | 12.4/80.6 | 10.4/96.2 |
| 512x512x37(MR) | 512 000 | 128 | 3 | 19.6/51 | 10.5/95 |
|  | 1 000 000 | 653 | 4 | 28.8/34.7 | 11.0/90.9 |
|  | 125 000 | 5 | 2 | 12.8/78.1 | 11.1/90.1 |
| 512x512x37(MR) | 512 000 | 127 | 3 | 19.6/51 | 10.6/94.3 |
|  | 1 000 000 | 655 | 4 | 28.4/35.2 | 10.5/95 |
|  | 125 000 | 5 | 2 | 12.9/77.5 | 10.8/92.6 |
| 512x371x169(CT) | 512 000 | 128 | 2 | 19.6/51 | 10.6/94.3 |
|  | 1 000 000 | 647 | 5 | 29.4/34 | 10.9/91.7 |
|  | 125 000 | 5 | 2 | 13.5/74.1 | 10.4/96.1 |
| 512x512x170(MR) | 512 000 | 107 | 3 | 20.3/49.3 | 10.6/94.3 |
|  | 1 000 000 | 648 | 4 | 30.2/33.1 | 10.2/98.0 |

### Formule


$$𝐻𝐻𝐻𝐻 = 𝑚𝑚𝑚𝑚𝑚𝑚 + 𝑏𝑏(1)$$
