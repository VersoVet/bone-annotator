# Intraoperative guidance of orthopaedic instruments using 3D correspondence of 2D object instance segmentations



## Resume


Intraoperative guidance of orthopaedic instruments using 3D correspondence of 2D object instance segmentations

Surgical Navigation Technology Based on Augmented Reality and Integrated 3D Intraoperative Imaging

A Unified Framework for 3D Organ Segmentation and Lesion Detection Based on Multi-Task Joint Learning

Progressive medical image annotation with convolutional neural network-based interactive segmentation method

Patch-Based Image Similarity for Intraoperative 2D/3D Pelvis Registration During Periacetabular Osteotomy

Periacetabular osteotomy is a challenging surgical procedure for treating developmental hip dysplasia, providing greater coverage of the femoral head via relocation of a patient's acetabulum. Since fluoroscopic imaging is frequently used in the surgical workflow, computer-assisted X-Ray navigation of osteotomes and the relocated acetabular fragment should be feasible. We use intensity-based 2D/3D registration to estimate the pelvis pose with respect to fluoroscopic images, recover relative poses of multiple views, and triangulate landmarks which may be used for navigation. Existing similarity metrics are unable to consistently account for the inherent mismatch between the preoperative intact pelvis, and the intraoperative reality of a fractured pelvis. To mitigate the effect of this mismatch, we continuously estimate the relevance of each pixel to solving the registration and use these values as weightings in a patch-based similarity metric. Limiting computation to randomly selected su

An improved algorithm for interactive medical image segmentation based on Intelligent scissors

Interactive image segmentation


## Insight


comparison: Cette approche 3D centrée sur l'os se distingue des méthodes CT et radiographiques bidimensionnelles antérieures par sa résistance intrinsèque aux erreurs de positionnement, un défi méthodologique classique en imagerie orthopédique vétérinaire.
Les techniques historiques de mesure des angles tibiaux, qu'elles soient radiographiques ou basées sur des reconstructions CT bidimensionnelles, nécessitent un alignement précis du membre par rapport au faisceau d'imagerie ou au plan de coupe, une exigence difficile à garantir en pratique clinique et source d'erreurs de mesure significatives en cas de mauvais positionnement. En introduisant un système de coordonnées 3D calculé directement à partir de la géométrie osseuse intrinsèque du patient, indépendamment de son orientation dans l'espace du scanner, cette étude propose une solution méthodologique qui contourne fondamentalement ce problème récurrent. La validation quantitative de cette indépendance, avec des différences de mesure inférieures à 1,3° même pour une déviation de positionnement extrême de 45°, constitue une preuve de concept solide de la supériorité de cette approche par rapport aux techniques 2D conventionnelles.

methodology: Le mécanisme d'attention en profondeur proposé permet au modèle de préserver la structure 3D des os malgré une architecture de prédiction basée sur des coupes 2D, évitant les incohérences inter-coupes même dans des régions anatomiques complexes comme la main ou la cheville.

methodology: Les instruments chirurgicaux guides conçus par CAO et imprimés en 3D ont significativement réduit le temps opératoire (de 40,6 ± 14,1 min à 26 ± 4,6 min, n=10, p<0,05) et amélioré la précision du placement de la fixation intramédullaire (de 71,6 ± 23,6 % à 98,3 ± 5,37 %, n=30, p<0,05) par rapport à une procédure sans instrument additionnel.

methodology: L’approche 2.5D repose sur trois U-Net 2D entraînés sur les coupes axiales, coronales et sagittales, combinés par un algorithme de vote pour produire la segmentation finale.


## Quote


Our approach uses multi-sectional CT slices from different orthogonal planes as input and then combines the 2D segmentation results from each plane in order to achieve a mandible segmentation in a 3D view.

Digital planning and 3D-printed guides may help maintain planned trajectories intraoperatively and reduce the risk of iatrogenic damage (45,46).

Objectively deriving three-dimensional angular values is complex, especially in a clinical setting, and an alternative approach is subjective segment orientation. This is a 3D assessment technique where, in Computer-Aided Design (CAD) software, subjective visual assessment of the optimal proximal and distal orientation of the bone in all planes is made


## Discussion


Cette revue narrative de la littérature vétérinaire montre que la convergence entre la simulation spécifique au receveur et les technologies d'impression 3D a bénéficié aux modèles anatomiques, aux instruments de coupe personnalisés (PSI) et aux implants sur mesure en orthopédie des petits animaux. Des options d'implants personnalisés ont été conçues et employées pour traiter des affections orthopédiques complexes ainsi que pour des chirurgies de révision, incluant le remplacement articulaire, les défauts osseux de taille critique, l'avancement de la tubérosité tibiale, le remplacement du sillon patellaire et les chirurgies de sauvetage de membre. Ces technologies constituent un outil précieux pour améliorer la précision du diagnostic, de la planification préopératoire, du choix ou de la conception de l'implant, ainsi que pour la réalisation d'un geste chirurgical plus précis. Sur la base des publications examinées, le recours aux modèles, aux PSI et aux implants orthopédiques sur mesure s'avère être une méthode efficace pour répondre à divers besoins cliniques en orthopédie vétérinaire, bien que les auteurs ne rapportent pas de données quantitatives agrégées permettant d'en établir la supériorité systématique sur les approches conventionnelles.

Cette étude expérimentale en deux phases démontre la faisabilité d'un modèle stable de défaut osseux segmentaire critique de 3 cm chez le fémur de Beagle, construit à l'aide de guides d'ostéotomie et d'instruments de fixation interne conçus par CAO et fabriqués par impression 3D. La phase in vitro comparative a établi la supériorité des instruments guides imprimés en 3D par rapport à une approche chirurgicale conventionnelle, tant en termes de réduction du temps opératoire que d'amélioration de la précision du placement de la fixation intramédullaire. La phase in vivo, menée chez trois Beagles sur un suivi de trois mois, a confirmé la stabilité mécanique du montage, l'ensemble des animaux ayant supporté une mise en charge précoce sans signe d'échec de l'implant. Ce modèle constitue ainsi une base méthodologique reproductible pour les recherches futures en régénération osseuse, en particulier pour l'ingénierie tissulaire des os portants, et illustre le potentiel des technologies CAO/impression 3D pour améliorer l'efficacité et la précision des procédures chirurgicales complexes.


## Synthese


L'imagerie par scintigraphie osseuse, bien qu'utilisée en première ligne pour détecter les métastases osseuses du cancer de la prostate, repose sur une interprétation subjective et sur une représentation bidimensionnelle d'une structure en réalité tridimensionnelle, comme en témoigne l'indice de scintigraphie osseuse (BSI). Le développement d'une quantification tridimensionnelle par PET/CT nécessite au préalable une segmentation précise, rapide et fiable du squelette à partir des données CT, un défi que les approches semi-automatisées existantes ne couvrent que partiellement. Les auteurs proposent une méthode de segmentation osseuse fondée sur un réseau de neurones convolutif (CNN), entraînée et validée par comparaison à des segmentations manuelles réalisées par un médecin expérimenté sur une cohorte de 146 patients (100 pour l'entraînement, 46 pour la validation), en utilisant l'indice de Sørensen-Dice pour évaluer la précision et la méthode de Bland-Altman pour évaluer la reproductibilité des calculs de volume. Cette approche constitue la première étape vers une quantification automatisée en 3D des métastases squelettiques par PET/CT.

L’introduction de l’article situe la segmentation de l’ombre osseuse en échographie comme une réponse aux limites de la fluoroscopie 2D en chirurgie orthopédique, notamment la difficulté de localisation tridimensionnelle des structures osseuses et l’exposition aux rayonnements ionisants. L’échographie 2D/3D y est présentée comme une alternative sûre, peu coûteuse et largement disponible, tout en soulignant les obstacles liés au bruit de chatoiement, aux réverbérations, à l’anisotropie, aux pertes de signal, au champ de vue limité et à la dépendance à l’opérateur. Les auteurs rappellent que des méthodes de segmentation et de recalage, y compris des approches d’apprentissage profond pour les surfaces osseuses, ont été proposées, mais qu’elles restent contraintes par le besoin de grands volumes de données d’entraînement et par une baisse de performance lorsque la qualité des images est faible ou que les données proviennent d’un autre constructeur. Dans ce contexte, l’information d’ombre acoustique — région de faible intensité suivant une surface osseuse de forte intensité — est décrite comme un attribut utile pour la segmentation, le guidage temps réel vers un plan diagnostique standardisé et le recalage avec le CT, l’IRM ou des modèles de forme statistiques. Enfin, les approches antérieures fondées sur l’intensité (cartes de confiance par marches aléatoires, analyse d’entropie, statistiques B-mode/RF) sont jugées insuffisamment robustes face aux artefacts et aux variations d’acquisition, ce qui motive le développement de méthodes plus adaptées aux données de faible qualité.

Cette revue narrative examine l'application des technologies de fabrication additive (impression 3D) dans le domaine de l'orthopédie vétérinaire des petits animaux, un secteur où les techniques chirurgicales conventionnelles atteignent souvent leurs limites face à des affections complexes telles que les pertes osseuses étendues, les non-unions ou malunions de fracture, les tumeurs, les déformations osseuses et les traumatismes de grande ampleur. Les auteurs situent l'impression 3D comme une extension logique de l'ingénierie tissulaire osseuse, permettant la conception de structures synthétiques tridimensionnelles adaptées aux besoins spécifiques du receveur, avec la possibilité d'intégration cellulaire et protéique. Un accent particulier est mis sur la variabilité anatomique interspécifique et interraciale propre à la médecine vétérinaire, qui accroît la pertinence des implants personnalisés par rapport à la médecine humaine où cette technologie est déjà plus largement documentée. L'article annonce une revue centrée sur les approches de fabrication additive et les spécificités de production des matériaux imprimés en 3D en chirurgie orthopédique vétérinaire, avec un focus principal sur le chien, extensible à d'autres espèces couramment rencontrées en pratique clinique. Cette revue narrative de la littérature vétérinaire montre que la convergence entre la simulation spécifique au receveur et les technologies d'impression 3D a bénéficié aux modèles anatomiques, aux instruments de coupe personnalisés (PSI) et aux implants sur mesure en orthopédie des petits animaux. Des options d'implants personnalisés ont été conçues et employées pour traiter des affections orthopédiques complexes ainsi que pour des chirurgies de révision, incluant le remplacement articulaire, les défauts osseux de taille critique, l'avancement de la tubérosité tibiale, le remplacement du sillon patellaire et les chirurgies de sauvetage de membre. Ces technologies constituent un outil précieux pour améliorer la précision du diagnostic, de la planification préopératoire, du choix ou de la conception de l'implant, ainsi que pour la réalisation d'un geste chirurgical plus précis. Sur la base des publications examinées, le recours aux modèles, aux PSI et aux implants orthopédiques sur mesure s'avère être une méthode efficace pour répondre à divers besoins cliniques en orthopédie vétérinaire, bien que les auteurs ne rapportent pas de données quantitatives agrégées permettant d'en établir la supériorité systématique sur les approches conventionnelles.

Dans le contexte de la chirurgie orthopédique assistée par ordinateur (CAOS), l’échographie apparaît comme une alternative intra-opératoire sans rayonnement ionisant à la fluoroscopie 2D/3D, dont l’information tridimensionnelle limitée, le coût et les risques radiologiques freinent l’usage. Toutefois, le faible rapport signal sur bruit, les artéfacts, le champ de vue restreint et l’épaisseur apparente des interfaces osseuses limitent encore son adoption clinique, d’où le besoin de méthodes automatiques de segmentation. Les approches fondées sur l’apprentissage profond (notamment U-net et FCN) ont déjà été explorées, avec des performances variables et souvent sans évaluation de la précision de localisation. Les auteurs proposent une CNN multimodale combinant images B-mode et caractéristiques de phase locale, validée sur 546 acquisitions in vivo chez 14 sujets sains, et rapportent un F-score moyen supérieur à 95 % ainsi qu’une erreur moyenne de localisation de 0,2 mm, la fusion tardive surpassant les autres stratégies de fusion.


## Methodologie


L'imagerie par scintigraphie osseuse, bien qu'utilisée en première ligne pour détecter les métastases osseuses du cancer de la prostate, repose sur une interprétation subjective et sur une représentation bidimensionnelle d'une structure en réalité tridimensionnelle, comme en témoigne l'indice de scintigraphie osseuse (BSI). Le développement d'une quantification tridimensionnelle par PET/CT nécessite au préalable une segmentation précise, rapide et fiable du squelette à partir des données CT, un défi que les approches semi-automatisées existantes ne couvrent que partiellement. Les auteurs proposent une méthode de segmentation osseuse fondée sur un réseau de neurones convolutif (CNN), entraînée et validée par comparaison à des segmentations manuelles réalisées par un médecin expérimenté sur une cohorte de 146 patients (100 pour l'entraînement, 46 pour la validation), en utilisant l'indice de Sørensen-Dice pour évaluer la précision et la méthode de Bland-Altman pour évaluer la reproductibilité des calculs de volume. Cette approche constitue la première étape vers une quantification automatisée en 3D des métastases squelettiques par PET/CT.

L’introduction de l’article situe la segmentation de l’ombre osseuse en échographie comme une réponse aux limites de la fluoroscopie 2D en chirurgie orthopédique, notamment la difficulté de localisation tridimensionnelle des structures osseuses et l’exposition aux rayonnements ionisants. L’échographie 2D/3D y est présentée comme une alternative sûre, peu coûteuse et largement disponible, tout en soulignant les obstacles liés au bruit de chatoiement, aux réverbérations, à l’anisotropie, aux pertes de signal, au champ de vue limité et à la dépendance à l’opérateur. Les auteurs rappellent que des méthodes de segmentation et de recalage, y compris des approches d’apprentissage profond pour les surfaces osseuses, ont été proposées, mais qu’elles restent contraintes par le besoin de grands volumes de données d’entraînement et par une baisse de performance lorsque la qualité des images est faible ou que les données proviennent d’un autre constructeur. Dans ce contexte, l’information d’ombre acoustique — région de faible intensité suivant une surface osseuse de forte intensité — est décrite comme un attribut utile pour la segmentation, le guidage temps réel vers un plan diagnostique standardisé et le recalage avec le CT, l’IRM ou des modèles de forme statistiques. Enfin, les approches antérieures fondées sur l’intensité (cartes de confiance par marches aléatoires, analyse d’entropie, statistiques B-mode/RF) sont jugées insuffisamment robustes face aux artefacts et aux variations d’acquisition, ce qui motive le développement de méthodes plus adaptées aux données de faible qualité.

Dans le contexte de la chirurgie orthopédique assistée par ordinateur (CAOS), l’échographie apparaît comme une alternative intra-opératoire sans rayonnement ionisant à la fluoroscopie 2D/3D, dont l’information tridimensionnelle limitée, le coût et les risques radiologiques freinent l’usage. Toutefois, le faible rapport signal sur bruit, les artéfacts, le champ de vue restreint et l’épaisseur apparente des interfaces osseuses limitent encore son adoption clinique, d’où le besoin de méthodes automatiques de segmentation. Les approches fondées sur l’apprentissage profond (notamment U-net et FCN) ont déjà été explorées, avec des performances variables et souvent sans évaluation de la précision de localisation. Les auteurs proposent une CNN multimodale combinant images B-mode et caractéristiques de phase locale, validée sur 546 acquisitions in vivo chez 14 sujets sains, et rapportent un F-score moyen supérieur à 95 % ainsi qu’une erreur moyenne de localisation de 0,2 mm, la fusion tardive surpassant les autres stratégies de fusion.


## Conclusion


La convergence de la simulation spécifique au receveur et des technologies d'impression 3D a bénéficié aux modèles anatomiques, aux instruments chirurgicaux spécifiques au patient (PSI) et aux implants personnalisés en orthopédie vétérinaire Les options d'implants sur mesure ont été conçues et utilisées pour certaines conditions orthopédiques complexes et chirurgies de révision en orthopédie vétérinaire La technologie 3D fournit à ce domaine un outil précieux pour un diagnostic et une planification préopératoire plus précis, la conception ou la sélection du type d'implant approprié, et l'exécution d'une chirurgie précise L'utilisation de modèles, de PSI et d'implants orthopédiques sur mesure s'est avérée être une méthode efficace pour traiter divers aspects de l'orthopédie vétérinaire, sur la base des articles publiés précédemment L'utilisation de la fabrication additive en médecine vétérinaire devrait continuer à croître et bénéficier non seulement aux receveurs vétérinaires mais aussi à la compréhension de la médecine individualisée

L'incorporation de la CAO et de l'impression 3D augmente significativement la stabilité tout en réduisant le temps chirurgical dans la construction du modèle animal, influençant significativement le succès du modèle de défaut osseux segmentaire chez le Beagle Les plaques de guidage d'ostéotomie et les instruments de fixation interne basés sur la CAO montrent un potentiel pour les recherches ultérieures sur la régénération osseuse, en particulier autour de l'ingénierie tissulaire osseuse portant charge L'utilisation de la CAO et de l'impression 3D pourrait fournir une assistance dans les procédures complexes pour améliorer l'efficacité et la précision globales


## Raw_Introduction


instance segmentation.

instance segmentation.


## Raw_|_Mipo:_Diaphyseal_Long_Bone_Fractures


wires, 34,35 transient intraoperative application of external fixators, 34,36,37 use of three-dimensional (3D) printed reduction guides, 38 and application of precontoured plates. 38


## Raw_Segmentation


iciency, addressing the fragmentation of task-specific models by training across diverse datasets and anatomical categories ( 90K unlabeled and 6K labeled CTs spanning 200+ categories), and introducing a zoom-out-zoom-in mechanism that drastically reduces the computational cost of volumetric inference while preserving precision. By combining semantic and spatial prompts, it also resolves the ambiguity of interactive segmentation, ensuring reliable results across both organs and lesions [141]. Together, they demonstrate that clinically deployable 3D FMs are both adaptable to new domains and robust across diverse anatomies.

iciency, addressing the fragmentation of task-specific models by training across diverse datasets and anatomical categories ( 90K unlabeled and 6K labeled CTs spanning 200+ categories), and introducing a zoom-out-zoom-in mechanism that drastically reduces the computational cost of volumetric inference while preserving precision. By combining semantic and spatial prompts, it also resolves the ambiguity of interactive segmentation, ensuring reliable results across both organs and lesions [141]. Together, they demonstrate that clinically deployable 3D FMs are both adaptable to new domains and robust across diverse anatomies.