# Call for Papers IEEE Transactions on Medical Imaging Special Issue on Annotation-Efficient Deep Learning for Medical Imaging



## Quote


Annotation-Efficient Deep Learning for Medical Imaging

Annotation-Efficient Deep Learning for Medical Imaging

There is a need for innovative methodologies that enable annotation-efficient deep learning for medical imaging

Address the challenge of annotation-efficient deep learning for medical imaging with a holistic approach

Présentation invitée donnant un aperçu des approches existantes et présentant trois travaux récents sur la segmentation d’images médicales efficiente en annotations


## Synthese


Cet appel à contributions publié en 2020 par IEEE Transactions on Medical Imaging porte sur l’apprentissage profond économe en annotations pour l’imagerie médicale. L’objectif affiché est de traiter ce défi selon une approche holistique, en rassemblant des travaux méthodologiques innovants. Le document ne précise pas de design expérimental propre, car il s’agit d’un appel thématique et non d’une étude empirique. Il souligne néanmoins le besoin de méthodologies permettant un apprentissage profond performant malgré la rareté ou le coût des annotations médicales. La conclusion principale est qu’il existe un besoin d’approches innovantes pour rendre l’apprentissage profond plus économe en annotations en imagerie médicale.

L’objectif de cette présentation invitée est de donner un aperçu des approches d’apprentissage profond efficient en annotations pour la segmentation d’images médicales, en présentant notamment une approche fondée sur des images médicales synthétiques et trois travaux récents.

L’appel vise à aborder le défi de l’apprentissage profond économe en annotations pour l’imagerie médicale au moyen d’une approche holistique.

Cette présentation invitée propose un aperçu des approches d’apprentissage profond efficient en annotations pour la segmentation d’images médicales. L’objectif est de présenter des méthodes permettant de réduire le besoin d’annotations manuelles coûteuses, notamment via l’exploitation d’images médicales synthétiques. Trois travaux récents sont exposés : un apprentissage faiblement supervisé s’appuyant sur des informations extraites de comptes rendus radiologiques, un entraînement au moment du test de type synthetic-to-real pour l’adaptation de domaine non supervisée sans accès aux données sources, et une synthèse d’images guidée par pseudo-étiquettes pour l’apprentissage semi-supervisé. La présentation s’inscrit dans une perspective plus large visant à progresser vers une segmentation d’images médicales sans annotations. Il s’agit d’une contribution de synthèse et de cadrage plutôt que d’une étude expérimentale unique.

Le titre suggère que le document cherche à concevoir ou évaluer des méthodes permettant de diminuer la charge d’annotation nécessaire aux algorithmes d’apprentissage profond en imagerie médicale. Le contexte probable est celui du coût élevé des annotations expertes, mais aucun passage source ne permet de préciser la problématique clinique ou les hypothèses. Les tâches, modalités d’imagerie et méthodes comparées ne sont pas indiquées. L’objectif détaillé doit donc être extrait du résumé, de l’introduction et des chapitres de contribution du document complet [Unknown](zotero://select/library/items/2MJE3NC8).

Cette revue examine les solutions d’apprentissage profond conçues pour atténuer deux limitations majeures des jeux de données de segmentation d’images médicales : la rareté des annotations et leur faible qualité ou granularité. Malgré les progrès des architectures de segmentation, notamment dans les connexions résiduelles, les mécanismes d’attention et les modules hybrides, leurs performances demeurent fortement dépendantes de jeux de données annotés volumineux et fiables. Les approches recensées contre la rareté des annotations comprennent des méthodes semi-automatisées, telles que l’apprentissage actif et la segmentation interactive, ainsi que des méthodes automatisées exploitant des données non annotées, synthétiques ou issues de domaines similaires. La revue couvre également les stratégies adaptées aux annotations clairsemées, bruitées ou limitées au niveau de l’image, tout en soulignant que ces imperfections peuvent compromettre la généralisation en contexte clinique réel [Unknown](zotero://select/library/items/ZRSWCZE4).


## Conclusion


There is a need for innovative methodologies that enable annotation-efficient deep learning for medical imaging

Active learning is important to deep learning in medical image analysis since it effectively reduces the annotation costs incurred by human experts. This survey comprehensively reviews the core methods in deep active learning, its integration with different label-efficient techniques, and active learning works tailored to medical image analysis. In summary, we believe that deep active learning and its application in medical image analysis hold important academic value and clinical potential, with ample room for further development.


## Insight


novelty: L’appel à contributions met en avant l’apprentissage profond économe en annotations comme enjeu prioritaire pour l’imagerie médicale.

implications: L’appel souligne la nécessité de méthodologies innovantes permettant un apprentissage profond économe en annotations pour l’imagerie médicale.

methodology: Les modèles de deep learning peuvent être employés comme outils assistifs d'annotation d'images médicales, permettant à l'expert de se concentrer sur la vérification plutôt que sur la production manuelle des annotations, ce qui accélère le processus de labellisation des données.

novelty: La présentation articule un cadre d’apprentissage profond efficient en annotations pour la segmentation d’images médicales autour de l’exploitation d’images médicales synthétiques et de trois travaux récents complémentaires.

implications: KaIDA vise à renforcer les approches de deep learning supervisées en imagerie biomédicale, tout en ayant une application potentielle au-delà de ce domaine spécifique.
Les auteurs soulignent que l'amélioration du processus d'annotation d'images rendue possible par KaIDA a pour effet direct de renforcer la robustesse des approches de deep learning supervisées appliquées au traitement d'image biomédical, domaine dans lequel la qualité des annotations conditionne directement la performance des modèles entraînés. Cependant, ils précisent explicitement que cette portée n'est pas restreinte au cas d'usage biomédical, laissant entendre que KaIDA pourrait être appliqué à d'autres domaines nécessitant l'annotation d'images pour l'entraînement de modèles de deep learning (par exemple l'imagerie industrielle, agricole ou de télédétection, bien que ces domaines ne soient pas explicitement mentionnés dans les extraits fournis). Cette généralisabilité annoncée reste néanmoins à démontrer empiriquement au-delà des jeux de données d'exemple présentés (tumeurs, noyaux cellulaires, organes, graines).


## Discussion


La conclusion de cette revue souligne que l’apprentissage actif profond constitue un levier majeur pour réduire les coûts d’annotation par des experts humains en analyse d’images médicales. Les auteurs synthétisent les méthodes centrales de deep active learning, leur articulation avec d’autres approches parcimonieuses en labels, ainsi que les travaux spécifiquement adaptés au domaine médical, tout en discutant les défis actuels et les perspectives. Ils concluent que ce champ présente une valeur académique et un potentiel clinique importants, avec une marge substantielle de développement ultérieur. Les éléments expérimentaux associés indiquent notamment que les stratégies fondées sur la représentativité (ou enrichies en diversité) sont plus favorables sous budget faible et tâche très difficile, tandis que les approches fondées sur l’incertitude conviennent mieux à un budget d’annotation élevé.

Ces résultats suggèrent que l'apprentissage actif profond peut orienter efficacement les efforts d'annotation manuelle vers les zones d'images les plus informatives, réduisant ainsi le volume de données annotées nécessaire sans sacrifier la performance de segmentation. Cette approche présente un intérêt particulier dans le domaine biomédical, où l'annotation experte est coûteuse en temps et en ressources.


## Methodologie


Cette revue examine les solutions d’apprentissage profond conçues pour atténuer deux limitations majeures des jeux de données de segmentation d’images médicales : la rareté des annotations et leur faible qualité ou granularité. Malgré les progrès des architectures de segmentation, notamment dans les connexions résiduelles, les mécanismes d’attention et les modules hybrides, leurs performances demeurent fortement dépendantes de jeux de données annotés volumineux et fiables. Les approches recensées contre la rareté des annotations comprennent des méthodes semi-automatisées, telles que l’apprentissage actif et la segmentation interactive, ainsi que des méthodes automatisées exploitant des données non annotées, synthétiques ou issues de domaines similaires. La revue couvre également les stratégies adaptées aux annotations clairsemées, bruitées ou limitées au niveau de l’image, tout en soulignant que ces imperfections peuvent compromettre la généralisation en contexte clinique réel [Unknown](zotero://select/library/items/ZRSWCZE4).