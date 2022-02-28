# README

### Installations

Pour installer tous les packages requis pour ce projet, veuillez lance la commande `pip install -r requirements.txt`.

Il faut préalablement installer **SWI-Prolog** pour pouvoir utiliser le raisonneur. Vous pouvez suivre les instructions sur la (page github de pyswip)[https://github.com/yuce/pyswip/blob/master/INSTALL.md].

### Exécuter le code

#### Construire la base de connaissances

Vous pouvez utiliser la commande `make build`.\
Si elle ne marche pas, vous pouvez aussi utiliser la commande `streamlit run demonstrator/__main__.py`.

#### Lancer le demo (page web)

Pour lancer la demo, vous pouvez utiliser la commande `make demo`.

#### Requêtes SPARQL

Les requêtes sparQL correpsondent aux questions que nous nous étions posées pendant l'étape de défintion du domaine et de la portée.

### Lancer les tests

Pour lancer les tests, il vous suffit d'exécuter la commande `make test`.\
Si elle ne marche pas, vous pouvez aussi utiliser la commande `pytest`.

# Rapport de projet connaissances et raisonnements

(Editable and updated version of the README)[https://hackmd.io/s/rkPHsd5RF].

## Introduction

Ce projet s'inscrit dans le cadre de la filière entrepreneuriale et du cours de connaissances et raisonnement. Cognitio est une plateforme de micro learning dont l'objectif est d'améliorer la rétention d'information et l'amusement pendant l'apprentissage.

Le micro learning est un concept qui consiste à diviser un cours en une multitude de petits modules de quelques minutes. Décomposer la connaissance en petits morceaux aide à augmenter l’attention et permet un taux de rétention plus élevé. Par exemple, la recherche montre que le micro-apprentissage peut entraîner une augmentation significative des taux de réussite aux examens (jusqu’à 18%) [1].

La plateforme d'apprentissage est ouverte au grand public et devra, à terme, couvrir des thématiques variées telles que la biologie, l'histoire ou l'astronomie. Chaque thématique peut contenir plusieurs cours. Par exemple, la thématique "Biologie" peut contenit les cours "Le microbiote" et "La théorie de l'évolution". Chaque cours est ensuite divisé en petits modules. Par exemple le cours sur "Le microbiote" contiendrait les modules Un module contient une ou plusieurs connaissances qui peuvent être présentées de diverses manières (petit texte à lire, questionnaire, audio, petite vidéo, etc.).

Ce projet entrepreneurial semble bien se prêter àl'application du cours de Connaissances et raisonnements. Nous essaierons dans la suite de ce document de présenter notre démarche de construction d'une ontologie adaptée à notre objectif, flexible, à jour et évolutive. Pour cela, nous allons nous baser sur la méthode de construction d'ontologies en casacade.

TO ADD SOMEWHERE: We chose to implement our owl knwoledge base with python so that it can easily be reused for our project.

# Définition de la KB

## Domaine et portée

La première étape de la création d'une ontologie par cascade consiste à définir le domaine et la portée de l'ontologie.

Nous listons ici l'ensemble des questions auxquelles l'ontologie doit répondre.

- Quelles sont les thématiques ?
- À quelle thématique est associé le cours C ?
- Quelles sont les étapes du cours C (avec ordre) ?
- Quels sont les modules du cours C ?
- Quels sont les modules de l'étape E (avec ordre) ?
- Quelles sont les connaissances associées au cours C/à l'étape E ?
- Quelles sont les connaissances associées au module M ?
- Quels sont les prérequis du cours C ?
- Quel est le premier module du cours C ?
- Quel est le module après M ?
- Quels sont les prérequis du module M ?
- Quels sont les apprentissages d'un module ?
- Combien de points sont rapportés par l'utilisateur grâce à ce module ?
- Quels sont les cours débloqués par un module ?
- Dans quel ordre faut-il afficher les connaissances liées au module M ?
- Quand faut-il que je lance un test de connaissances ?
- Quel est résumé d'une étape ? Les points/achievements associés ?
- Quel est le contenu de la connaissance C ?
- Quelles sont les langues disponibles pour la connaissance C ?
- Combien de fois une connaissance doit-elle être revue ?
- Quels sont les fragments associés à la connaissance C ?
- Quel est le type de ce fragment ? (exemple, fait amusant)
- De quelle forme ce fragment peut être représenté ?
- Ce fragment peut-il constituer un test de connaissance ?
- Qui a terminé le cours C ?
- Qui a créé le cours C ?
- Quelles connaissances à acquis X ?
- À quel cours à accès X ?
- Quels cours X doit-il réviser ?
- Quels cours X devrait-il suivre ?
- Où en est X dans le cours C ?
- Quels modules du cours C X a-t-il débloqué ?
- Combien de personnes ont commencé le cours C ?
- Combien de personnes ont terminé un cours C ?

## Étapes de construction de la connaissance

Nous construisons l'ontologie en quatre grandes étapes et de façon incrémentale :

1. **Tout ce qui a trait aux enseignements:** thèmes, modules, parties, cours, connaissances, fragments.
   Pas de notion d'utilisateur, de gamification, d'affichage, de test
2. **Notions d'implémentation:** Affichage possible, tests
3. **Ce qui concerne les utilisateurs et créateurs:** qui suit quoi, qui a accès à quoi, qui doit réviser quoi et quand...
4. **Ce qui concerne la gamification:** points, badges...

## Étape 1 - Tout ce qui a trait aux enseignements

### 1.1 Domaine et portée

Domaine et portée spécifiques aux enseignements

- Quelles sont les thématiques ?
- À quelle thématique est associé le cours C ?
- Quelles sont les étapes du cours C (avec ordre) ?
- Quels sont les modules du cours C ?
- Quels sont les modules de l'étape E (avec ordre) ?
- Quelles sont les connaissances associées au cours C/à l'étape E ?
- Quelles sont les connaissances associées au module M ?
- Quels sont les prérequis du cours C ?
- Quel est le premier module du cours C ?
- Quel est le module après M ?
- Quels sont les prérequis du module M ?
- Quels sont les apprentissages d'un module ?
- Quels sont les cours débloqués par un module ?
- Dans quel ordre faut-il afficher les connaissances liées au module M ?
- Quel est le contenu de la connaissance C ?
- Quels sont les fragments associés à la connaissance C ?
- Quel est le type de ce fragment ? (exemple, fait amusant)
- Quelle est la durée estimée d'un module ?

### 1.2 Réutilisation d'ontologie

Dans cette étape, nous ne réutiliserons pas d'ontologie préexistante.

### 1.3 Énumération des termes

- thématique
- cours
- étape
- module
- connaissance
- prérequis
- premier module/connaissance
- module/connaissance après
- apprentissages
- cours débloqués
- contenu
- ordre
- fragment
- type de fragment
- associé
- fait amusant

### 1.4 Définition des classes

- **Thematic**, représentant un thème autour duquel s'articulent plusieurs cours
- **Course**, représentant la connaissance associée à un sujet particulier
  - Associée à une Thématique
- **Section**, pour subdiviser les connaissances d'un cours en ensembles cohérents
  - Associée à un Cours
- **Module**, rassemblant un petit ensemblde de connaissances autour d'un sujet très précis
  - Associé à un Cours
- **Knowledge**, unité indivisible de connaissances
  - Associée à un Module
- **Fragment**, donne des précisions sur une connaissance
  - Associé à une Connaissance
  - Partitionné en : complément, exemple, anecdote

`>>>>>>>>>>>>`

- **Complément**, pour donner une indication sur une connaissance précise
  - Sous-classe de Fragment
- **Exemple**, qui illustre une connaissance
  - Sous-classe de Fragment
- **Anecdote**, une anecdote sur une connaissance - Sous-classe de Fragment
  `<<<<<<<<<<<<<<<<`
  `>>>>>>>>>>>>>`
  Du coup j'enlèverai tout ca puisqu'on définit anecdote, complément et example comme
  `<<<<<<<<<<<<<`

### 1.5 Définition des propriétés

A partir des questions définies dans la première partie, nous pouvons identifier un certain nombre de propriétés que doivent vérifier les classes. Par simplicité, nous ne définissons pas les propriétés inverses lorsqu'elles existent et indiquerons simplement que la propriété inverse existe.

#### 1.5.1 Object properties

Dans cette partie, nous définissons les propriétés objet qui relient les différentes classes. Nous essayons notamment d'en créer le moins possible tout en gardant toute la représentation des cas de figure. Par exemple, il n'est pas nécessaire de définir la propriété d'ordre des modules `is_preceeded_by` car celle-ci peut être induite par la propriété `requires_module` de prérequis sur les modules. Les propriétés s'appliquent entre deux classes définies précédement et peuvent être symétriques, réflexives, transitives, fonctionnelle (unicité) etc.

- `is_in_thematic` : Cette propriété indique si un cours fait partie d'une certaine thématique.
  - Range : Thematic
  - Domain : Cours
  - Propriété inverse : has_as_course
- `is_in_course`: Cette propriété indique si une partie fait partie d'un cours
  - Range : Cours
  - Domain : Partie
  - Propriété inverse : `has_as_part`
- `is_in_part` : Cette propriété indique si un module fait partie d'une partie.
  - Range : Partie
  - Domain : Module
  - Propriété inverse : `has_as_module`
- `is_in_module` : Cette prorpiété indique si une connaissance fait partie d'un module
  - Range : Module
  - Domain : Connaissance
  - Propriété inverse : `contains_knowledge`
- `requires_modules` : Cette propriété indique les modules requis pour pouvoir en commencer un autre
  - Range : Module
  - Domain : Module
  - Propriété inverse : `is_required_by_modules`
- `follows_knowledge` : Cette propriété indique quelle connaissance suit une autre connaissance
  - Range : Connaissance
  - Domain : Connaissance
  - Propriété inverse : `is_followed_by_knowledge`

TO MODIFY : Nous avons choisi d'ajouter la dépendance de restriction sur les modules plutot que sur les connaissance car ....

#### 1.5.2 Data properties

- Thématique
  - Titre (string)
  - Description (string)
- Course
  - Titre (string)
  - Description (string)
- Partie
  - Titre (string)
- Module
  - Titre
- Connaissance
  - Titre (string)
  - Description (string)
- Fragment
  - Contenu (string)

`>>>>` To delete

- Complément
- Exemple
- Anecdote
  `<<<<<`

### 1.6 Définition des contraintes

- Un Fragement peut être défini par extension, c'est à dire en listant ces instances plutôt qu'en définissant ces propriéts. Un fragment peut être un complément, une anecdote ou un example.
- Un cours contient au moins 2 modules
- Une partie contient au moins un module
- Un module contient au moins une connaissance
- Une thématique contient au moins un cours

### 1.7 Création des instances

### 1.8 Test de l'ontologie

--> Obtenir le graphe de connaissance avec prolog (ordre des différents modules).
--> A chaque fois qu'on ajoute un cours, il faut faire tourner prolog pour obtenir cet ordre.

## Étape 2 - Notions d'implémentation

### Domaine et portée

Domaine et portée spécifiques à l'implémentation

- Quand faut-il que je lance un test de connaissances ?
- Quel est résumé d'une étape ?
- Quelles sont les langues disponibles pour la connaissance C ?
- Combien de fois une connaissance doit-elle être revue ?
- De quelle forme ce fragment peut être représenté ?
- Ce fragment peut-il constituer un test de connaissance ?

## Étape 3 - Utilisateurs et créateurs

### Domaine et portée

Domaine et portée spécifiques aux utilisateurs/créateurs

- Qui a terminé le cours C ?
- Qui a créé le cours C ?
- Quelles connaissances à acquis X ?
- À quel cours à accès X ?
- Quels cours X doit-il réviser ?
- Quels cours X devrait-il suivre ?
- Où en est X dans le cours C ?
- Quels modules du cours C X a-t-il débloqué ?
- Combien de personnes ont commencé le cours C ?
- Combien de personnes ont terminé un cours C ?
- Quels fragments X a vu ?

### Définition des classes

- Apprenant

## Étape 4 - Gamification

### Domaine et portée

Domaine et portée spécifiques à la gamification

- Combien de points sont rapportés par l'utilisateur grâce à ce module ?
- Quels sont les points/achievements associés à la complétion d'une étape ?

### Défintion des classes

- Quizz
  - Sous-classe de Fragment
- Audio
  - Sous-classe de Fragment
- Article
  - Sous-classe de Fragment

### Défintion des data properties

# Implémentation et inférences

- Créer l'ontologie
- Ajouter les règles de structure
- Peupler l'ontologie avec des exemple (des cours, des individus...)
- Inférer des trucs
  - Ordre des cours
  - Ordre des modules
  - Ordre des connaissances (?)
  - Inférer les cours disponibles pour un utilisateur donné
  - Inférer un quizz à partir d'un cours donné
  - (Trouver comment optimiser le nombre de points en un temps donné)

# Trouver comment lier DBPedia

- Trouver des précisions sur des infos du cours ?
- Créer un cours ?
- Trouver quel cours créer par la suite ?

# Créer un chatbot qui déroule tout --> projet Systèmes de dialogue (en fait y en a pas)

# Sources

[1] Sirwan Mohammed, Gona; Wakil, Karzan; M. Nawroly, Sarkhell Sirwan (2018). "The Effectiveness of Microlearning to Improve Students' Learning Ability". International Journal of Educational Research Review (3): 35. doi:10.24331/ijere.415824. Retrieved March 28, 2021.
