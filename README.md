# ALGAV
Programmation en algorithme avancé : Implémentation en Python.

---

## Répertoires
Le projet est structuré en plusieurs répertoires, chacun contenant des fichiers modulaires pour organiser le code :

### `utilitaire`
Contient des fonctions utilitaires pour la manipulation des chaînes ASCII et des opérations annexes, 
utilisées dans la gestion des Patricia & Hybride Tries.

### `node`
Définit les classes de base représentant les nœuds dans les structures d'arbre.

### `tree`
Implémente les Patricia & Hybride Tries, y compris les opérations principales (insertion, suppression, recherche, etc.).

### `rendu`
Inclut des fonctions haut-niveau permettant de manipuler les arbres à partir des données externes (fichiers, JSON).

### 'shakespeare'
Contient l'ensemble des fichiers textes de l'œuvre complète de William Shakespeare.

### 'shake'
consArbre.py : Fonctions pour construire les structures à partir des mots de Shakespeare.
patricia_tree_comp.py : Implémentation de PatriciaTree avec compteur de comparaisons.
hybride_tree_comp.py : Implémentation de HybrideTree avec compteur de comparaisons.

### `main`
Fichier principal pour exécuter les actions sur les Patricia Tries ou les arbres hybrides . 
Ce fichier gère les arguments en ligne de commande.
contient principalement:
#### main.py
répond principalement la partie 5 du projet

#### shakespeare.py
répond principalement la partie 6 du projet

### graphique.py
une version graphique mais incomplete

---

## Exécution
Pour exécuter le projet, suivez ces étapes selon votre système d'exploitation :

---

### Sur Unix/Linux/Mac :
1. **Accédez au répertoire principal du projet :**
   ```bash
   cd <chemin/vers/le/projet>/algav1/src/main
2. **Ajoutez le chemin du projet à la variable d'environnement PYTHONPATH :**
    export PYTHONPATH=$PYTHONPATH:<chemin/vers/le/projet>/algav1/src
3. **Exécutez le fichier principal avec Python :**
    python3 main.py <action> <structure> <arbre ou fichier> [motif]
    
### Sur Windows :
1. **Ajoutez le chemin du projet à la variable d'environnement PYTHONPATH :**
    **Avec cmd :**
        set PYTHONPATH=%PYTHONPATH%;<chemin\vers\le\projet>\algav1\src
    **Avec powerShell :**
        $env:PYTHONPATH = "$env:PYTHONPATH;<chemin\vers\le\projet>\algav1\src"
2. **Accédez au répertoire principal du projet :**
    cd <chemin\vers\le\projet>\algav1\src\main
3. **Exécutez le fichier principal avec Python :**
    <python ou python3 ou py> main.py <action> <structure> <arbre ou fichier> [motif]



