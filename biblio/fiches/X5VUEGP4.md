# Manually Annotated Drone Imagery Dataset for Automatic Coastline Delineation.

**Auteurs** : Tanwari K, Terefenko P, Śledziowski J, Giza A.
**Année** : 2025
**DOI** : 10.1038/s41597-025-04685-7

## Résumé

Automatic delineation of coastline in coastal zones is an essential task for various applications including protection of coastal regions, disaster management, and planning. The lack of availability of manually annotated high resolution datasets tailored for AI in coastal research remains a concern. Therefore, we created an open source, UAV captured and high resolution RGB dataset named MADRID (Manually Annotated DRone Imagery Dataset). It was recorded during six-separate UAV fly-over flight paths in two different types of coasts in Poland, Miedzyzdroje - cliff coast and in Mrzezyno - dune coast. The dataset comprises of 3691 high-resolution images and each image is accompanied by manually provided coastline annotations utilizing novel polyline annotation technique for the first time. The data is pre-split into training and test data subsets suitable for semantic segmentation tasks. The output of this study has implications for protection of coastal regions and marine ecosystems, deliv

## Méthodologie

{'study_design': "Data descriptor : création d'un dataset d'imagerie UAV avec annotation manuelle par polyligne du trait de côte via l'outil CVAT, conversion des annotations en masques binaires, pré-découpage en sous-ensembles train/test, et validation technique par entraînement d'un modèle UNet de référence (baseline) pour la segmentation sémantique.", 'intervention': "Entraînement d'un modèle UNet de référence sur les images annotées avec techniques d'augmentation de données (bruit gaussien aléatoire, color jitter, flip aléatoire), chacune appliquée avec 50% de probabilité", 'control': None, 'primary_outcomes': ['Performance de segmentation sémantique du trait de côte (Overall Accuracy, Precision, Recall, F1 score, Dice score)'], 'secondary_outcomes': [], 'statistical_methods': ['Overall Accuracy (OA)', 'Precision (P)', 'Recall (R)', 'F1 score', 'Dice score'], 'duration': 'Données collectées entre 2022 et 2023, sur quatre saisons (hiver, printemps, automne, été), lors de six campagnes de vol UAV distinctes', 'setting': 'Deux sites côtiers polonais de la mer Baltique méridionale : Miedzyzdroje (côte à falaises) et Mrzezyno (côte à dunes)'}

## Résultats

{'quantitative': [{'outcome': 'Overall Accuracy du modèle UNet de référence pour la délimitation du trait de côte', 'value': '98.95%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Technical Validation', 'source_quote': 'achieving an overall accuracy of 98.95%'}, {'outcome': "Nombre d'images finales dans le dataset MADRID (tuiles compressées)", 'value': '3691', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Data Records', 'source_quote': '3691 tiles (JPEG format, 2560 × 1440 pixels) are compressed into the MADRID_v0.1_data.rar.'}, {'outcome': 'Répartition train/test du dataset', 'value': '3553 (train) / 323 (test)', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Data Records', 'source_quote': 'the data is pre-split into train and test subsets with 3553 (train samples) and 323 (test samples), respectively'}], 'qualitative_findings': ['Le score de Dice est relativement faible, ce qui pourrait indiquer une incapacité du modèle à délimiter correctement le trait de côte dans des environnements à forte marée'], 'main_findings': ['Création du premier dataset aérien complet utilisant des annotations manuelles par polyligne conçu spécifiquement pour la segmentation sémantique du trait de côte', "Le modèle UNet de référence constitue un point de départ efficace et précis pour la détection du trait de côte dans l'imagerie drone haute résolution", 'Le score de Dice relativement faible suggère des difficultés potentielles du modèle en environnement à forte marée']}

## Conclusions

Le dataset MADRID, structuré selon les principes FAIR, constitue une ressource utile pour automatiser la cartographie du trait de côte par IA Le modèle UNet de référence fourni avec le dataset atteint une précision globale de 98.95%, servant de point de départ efficace pour la détection du trait de côte Des algorithmes de détection de contours tels que HED et Canny Edge Detector pourraient améliorer les performances par rapport à U-Net dans de futures études

## Specifications for Zenmuse L1 sensor.

| Specification | Value |
| --- | --- |
| Spectrum (μm) | 0.4-0.7 |
| Image Resolution (px) 5472 × 3648 |
| Field of View (°) | 84 |
| Focal Length (mm) | 8.8 |
| Format | 1-inch CMOS |

## Environmental conditions during the fly over on 2022-01-11 as measured by the closest weather station in Szczecin Goleniow 53.56°N, 14.83°E (WGS 84 coordinate system, source: Poland weather history data at https://www.wunderground.com/history/daily/pl/glewice/EPSC/date/2022-1-11).

|  |  | Pressure | Temperature | Wind Speed |  | Sea Level Pressure |
| --- | --- | --- | --- | --- | --- | --- |
| Time | Cloud Cover | (in) | (°F) | (mph) | Wind Direction | (in) |
| 10AM GMT+2 | Overcast | 30.42 | 19 | 6 | ESE | 30.42 |
| 12PM GMT+2 | Overcast | 30.42 | 23 | 6 | SE | 30.42 |
