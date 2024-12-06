Générateur de Configurations Réseau
Introduction

Ce projet permet de générer des configurations réseau uniques à partir d'une séquence de degrés, c'est-à-dire une liste représentant le nombre de connexions (degrés) que chaque nœud d'un réseau doit avoir. Il utilise le théorème d'Erdős–Gallai pour vérifier la validité de la séquence de degrés et génère toutes les configurations possibles qui respectent cette séquence. Les configurations peuvent être sauvegardées dans un fichier JSON et visualisées sous forme de graphes.
Fonctionnalités

    Vérification de la validité d'une séquence de degrés (théorème d'Erdős–Gallai).
    Génération de toutes les configurations réseau uniques respectant une séquence de degrés.
    Option pour sauvegarder les configurations générées dans un fichier JSON.
    Visualisation des configurations sous forme de graphes.

Prérequis

Assurez-vous d'avoir les dépendances suivantes installées avant d'exécuter l'outil :

    Python 3.x
    networkx
    matplotlib
    itertools

Installez-les en utilisant pip :

pip install networkx matplotlib

Utilisation
Lancer l'outil

    Téléchargez ou clonez ce repository.
    Exécutez le script avec la commande suivante :

python generate_network_configurations.py

Arguments

Le script accepte les arguments suivants :

    degree_sequence : Séquence de degrés sous forme d'entiers séparés par des espaces (obligatoire).
    --save : Sauvegarder les configurations dans un fichier JSON (optionnel).
    --json_filename : Nom du fichier JSON où les configurations seront sauvegardées (par défaut : network_configurations.json).
    --visualize : Visualiser les configurations générées (optionnel).

Exemples d'utilisation

    Générer des configurations pour une séquence de degrés et les afficher dans la console :

python generate_network_configurations.py 3 3 2 2 1 1

Cela générera les configurations réseau pour la séquence de degrés [3, 3, 2, 2, 1, 1] et les affichera dans la console.

    Générer des configurations et les sauvegarder dans un fichier JSON :

python generate_network_configurations.py 3 3 2 2 1 1 --save --json_filename configurations.json

Cela génère les configurations pour la séquence de degrés [3, 3, 2, 2, 1, 1] et les sauvegarde dans le fichier configurations.json.

    Générer des configurations et visualiser les graphes :

python generate_network_configurations.py 3 3 2 2 1 1 --visualize

Cela génère les configurations pour la séquence de degrés [3, 3, 2, 2, 1, 1] et affiche les graphes générés à l’aide de matplotlib.

    Générer des configurations, les sauvegarder et visualiser les graphes :

python generate_network_configurations.py 3 3 2 2 1 1 --save --json_filename configurations.json --visualize

Cela génère les configurations pour la séquence de degrés [3, 3, 2, 2, 1, 1], les sauvegarde dans configurations.json et affiche les graphes générés.
Sortie

Le programme affichera les configurations générées dans la console et, si l'option --save est activée, il sauvegardera les configurations dans un fichier JSON.
Exemple de sortie

Configurations réseau uniques pour la séquence de degrés [3, 3, 2, 2, 1, 1]:

Configuration 1:
 Connexion entre les nœuds 0 et 1
 Connexion entre les nœuds 1 et 2
 Connexion entre les nœuds 2 et 3
 Connexion entre les nœuds 0 et 4
 ...

Nombre total de configurations uniques : 2
Les configurations ont été sauvegardées dans 'configurations.json'.
