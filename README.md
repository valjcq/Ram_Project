# README : Programme de Machine RAM avec Structure de Graphe

## Description
Ce projet implémente une machine abstraite de type RAM (Random Access Machine), ainsi qu'un mécanisme pour la générer à partir d'un fichier texte. Le programme permet d'exécuter des instructions de base telles que `ADD`, `JEQ`, `JGT`, `JLT`, et d'analyser le flux des instructions à travers un graphe. Les principales fonctionnalités comprennent:

- Lecture d'instructions depuis un fichier texte.
- Exécution d'instructions RAM.
- Affichage de la configuration de la machine.
- Optimisation du graphe d'instructions pour améliorer l'efficacité de l'exécution.

## Structure des Fichiers
- `ram.py`: Contient le code source de la classe `ram` qui représente la machine RAM et de la classe `graph_instruc` qui représente le graphe des instructions.
- `ram.txt`: Fichier d'entrée contenant le mot d'entrée et les instructions de la RAM.

## Instructions du Fichier d'Entrée
Le fichier d'entrée (par défaut, `ram.txt`) doit être structuré comme suit:
- La première ligne contient le mot d'entrée (chaîne de caractères).
- Les lignes suivantes contiennent les instructions de la RAM, séparées par des virgules.
- Les instructions utilisent une syntaxe de type "opération(argument1, argument2, argument3)". Les arguments peuvent être des accès registres ou des valeurs littérales.
Les registres sont représentés par des lettres majuscules (A, B, C, etc.), suivi d'un nombre (A0, B1, C2, etc.).

## Utilisation
Pour exécuter le programme, vous avez besoin de Python installé sur votre système. Utilisez les instructions suivantes pour lancer le programme:

1. Cloner ou télécharger le code source du projet.
2. Exécutez le programme avec Python:
   ```
   python ram.py AB
   ```
   ou
   ```
   python ram.py tableau
   ```
3. Le programme va afficher la configuration de la RAM et exécuter les instructions selon le fichier d'entrée.

## Classes Principales
- `ram`: Représente la machine RAM. Contient des méthodes pour exécuter des instructions, gérer les registres, et afficher la configuration actuelle de la machine.
- `graph_instruc`: Représente le graphe des instructions. Fournit des fonctionnalités pour visualiser, optimiser et modifier le flux des instructions.

## Fonctionnalités
- **Exécution des Instructions**: Le programme peut exécuter des instructions de type `ADD`, `JEQ`, `JGT`, `JLT`, avec la possibilité d'ajouter d'autres opérations.
- **Affichage de la Configuration**: La fonction `afficher_config` affiche l'état actuel de la machine RAM, y compris les registres et l'instruction en cours.
- **Graphe des Instructions**: La classe `graph_instruc` permet de créer et d'analyser un graphe basé sur la séquence d'instructions. Elle fournit des méthodes pour optimiser le graphe en supprimant les instructions inutilisées ou les sauts inutiles.

## Optimisation
La classe `graph_instruc` inclut des méthodes d'optimisation pour:
- Supprimer des instructions inutilisées.
- Fusionner des instructions pour améliorer l'efficacité.
- Adapter le graphe pour refléter les modifications apportées.

## Dépendances
Ce projet n'a pas de dépendances externes au-delà de la bibliothèque standard de Python.

## Limitations et Améliorations Futures
- Les optimisations sont limitées aux instructions de base et pourraient être étendues.
- La classe `ram` peut être étendue pour inclure davantage d'opérations RAM.
- Les validations et les contrôles d'erreurs pourraient être améliorés pour renforcer la robustesse du programme.
- Faire des executions différentes en fonction des arguments donnés.

## Auteur
Ce projet a été développé dans le cadre d'un projet académique. Pour toute question ou suggestion, veuillez contacter l'auteur ou le contributeur principal.