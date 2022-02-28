# Base de connaissance : Microlearning

## Présentation

Ce projet s’inscrit dans le cadre de la filière entrepreneuriale et du cours de connaissances et raisonnement. Capsule est une plateforme de micro learning dont l’objectif est d’améliorer la rétention d’information et l’amusement pendant l’apprentissage.

Le micro learning est un concept qui consiste à diviser un cours en une multitude de petits modules de quelques minutes. Décomposer la connaissance en petits morceaux aide à augmenter l’attention et permet un taux de rétention plus élevé. Par exemple, la recherche montre que le micro-apprentissage peut entraîner une augmentation significative des taux de réussite aux examens (jusqu’à 18%).

La plateforme d’apprentissage, que nous décrivons dans ce projet dans une ontologie, est ouverte au grand public et devra, à terme, couvrir des thématiques variées telles que la biologie, l’histoire ou l’astronomie. Chaque thématique peut contenir plusieurs cours. Par exemple, la thématique “Biologie” contient les cours “Le microbiote” et “La théorie de l’évolution”. Esnuite, chaque cours est divisé en petits modules. Par exemple le cours sur “Le microbiote” contient les modules “Influence de l’environnement sur le microbiote” et “Saisonalité du microbiote”. Un module contient une ou plusieurs connaissances qui peuvent être présentées de diverses manières (petit texte à lire, questionnaire, audio, petite vidéo, etc.).

Pour plus d'informations sur le sujet, vous pouvez consulter notre rapport `./Rapport.pdf`.

## Installation

Il faut préalablement installer **SWI-Prolog** pour pouvoir utiliser le raisonneur. Vous pouvez suivre les instructions sur la [page github de pyswip](https://github.com/yuce/pyswip/blob/master/INSTALL.md).

Pour installer tous les packages requis pour ce projet, veuillez lance la commande `make install`.

## Exécuter le code

### Construire la base de connaissances

Vous pouvez utiliser la commande `make build`.\
Si elle ne marche pas, vous pouvez aussi utiliser la commande `streamlit run demonstrator/__main__.py`.

### Lancer la demo (page web)

Pour lancer la demo, vous pouvez utiliser la commande `make demo`.

### Lancer les tests unitaire

Pour lancer les tests, il vous suffit d'exécuter la commande `make test`.\
Si elle ne marche pas, vous pouvez aussi utiliser la commande `pytest`.

### Tester les différentes fonctions

Il est possible de tester les différentes fonctionnalités développées dans le projet:

- Pour tester les requêtes SPARQL, on peut lancer la commande `make requests`
- Pour tester les requêtes Prolog, on peut lancer la commande `make reasoner`
  Si ça ne marche pas, on peut lancer à la place `python -m src.reasoner`

## Structure de fichiers

```
├── demonstrator     <- Les classes et fichiers nécessaires à l'exécution du démonstrateur
│
├── src
│   ├── construction        <- Toutes les classes et les fichiers nécessaires pour construire la structure de l'ontologie.
│   ├── instances           <- Tous les fichiers nécessaires pour créer les instances de l'ontologie.
│   ├── reasoner            <- Tous les fichiers nécessaires pour raisonner en Prolog.
│   ├── requests            <- Tous les fichiers nécessaires pour définir les requêtes SPARQL.
│   ├── builder.py          <- Les fonctions de construction de l'ontologie.
│   └── build.py            <- Le script qui crée et sauvegarde l'ontologie.
│
├── storage                 <- Les fichiers de sauvegarde de l'ontologie et du raisonneur
│
├── tests                   <- Les fichiers de test unitaire
│
├── .flake8
├── .gitignore
├── .pre-commit-config.yaml
├── .pylintrc
├── Makefile
├── mypy.ini
├── pyproject.toml
├── Rapport.pdf             <- Le rapport du projet
├── README.md
├── requirements-dev.txt
└── requirements.txt
```

Dans certains dossiers, on peut trouver les sous-dossiers `micro-learning` et `persons`. Ceux-ci correspondent aux différents sprints réalisés:

- **micro-learning** correspond à la structure de connaissances pures
- **persons** correspond à la structure des utilisateurs et créateurs des cours
