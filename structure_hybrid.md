### Structure d’un nœud de `HybrideTree`

**Caractère :**
- Chaque nœud dans `HybrideTree` contient un caractère qui correspond à un segment de mot.
- Ce caractère est crucial pour la navigation dans l'arbre, car il permet de distinguer les différents chemins possibles.

**Valeur :**
- La valeur associée au nœud correspond à la donnée entière associée à un mot complet, c'est-à-dire le mot dont ce nœud est la fin (terme).
- Si un mot est incomplet ou si le nœud n'est pas un terme, la valeur sera `None`.

**Enfants (Inf, Eq, Sup) :**
- Un nœud de `HybrideTree` peut avoir jusqu'à trois types d'enfants :
  - **Inf** : Le pointeur vers l'enfant à gauche, représentant des mots dont le caractère actuel est inférieur au caractère du nœud.
  - **Eq** : Le pointeur vers l'enfant central, représentant la suite du mot (le caractère suivant).
  - **Sup** : Le pointeur vers l'enfant à droite, représentant des mots dont le caractère actuel est supérieur au caractère du nœud.
- Cette structure permet de gérer efficacement les relations entre les caractères et de maintenir un tri lexicographique.

### Avantages de cette structure

**Navigation efficace :**
- La gestion de la navigation est réalisée à travers trois pointeurs (`inf`, `eq`, `sup`), permettant de descendre facilement dans l’arbre selon la comparaison du caractère actuel.
- Ce mécanisme optimise les parcours de recherche, car il ne nécessite pas de structures complexes, comme des tableaux ou des listes.

**Optimisation mémoire :**
- La structure de `HybrideTree` est optimisée car elle n'utilise que les pointeurs nécessaires pour la navigation. Contrairement aux tries classiques où chaque nœud peut avoir un tableau de pointeurs pour chaque caractère possible, ici chaque nœud n'a que trois pointeurs (ou moins si non nécessaires).
- Cela rend la mémoire plus économique et l'accès plus rapide.

**Respect de l’ordre lexicographique :**
- L'ordre lexicographique est naturellement respecté grâce à la comparaison des caractères et à la gestion des relations entre `inf`, `eq`, et `sup`. Cela facilite les opérations comme la recherche de mots, la recherche de préfixes ou l'énumération des mots dans l'ordre alphabétique.

### Concept d'un `HybrideTree`

**Définition :**
- Un `HybrideTree` est un arbre avec une racine qui pointe vers un nœud de départ. Tous les autres nœuds (enfants) sont liés entre eux par les relations définies par `inf`, `eq`, et `sup`.
- L'arbre est conçu pour stocker efficacement des mots et leurs valeurs associées, tout en optimisant l'utilisation de la mémoire et les performances de recherche.

**Avantages :**
- La gestion de l’arbre est simplifiée en concentrant la logique d’insertion, de recherche, et de suppression autour des pointeurs `inf`, `eq`, et `sup`.
- L’optimisation mémoire permet de stocker efficacement les mots et d’éviter les chevauchements inutiles.
- Le modèle de navigation est cohérent et réduit les calculs redondants, car il repose sur des comparaisons simples de caractères.

### Fusion de deux `HybrideTree`

**Cas particuliers :**
- Si l’un des deux arbres est vide, la fusion consiste simplement à retourner l'autre arbre.
- Si les arbres contiennent des mots communs, ces mots doivent être insérés sans doublons.

**Points Clés :**
- **Maintenir les propriétés du `HybrideTree`** : Lors de la fusion, l'arbre résultant doit respecter les règles d’organisation du trie hybride, notamment en ce qui concerne les relations entre les caractères dans les différents sous-arbres.
- **Choisir l'arbre de base** : Lors de la fusion, il est important de choisir l'arbre ayant un nombre de mots plus faible ou moins de profondeur pour éviter une croissance excessive.
- **Lister les mots du deuxième arbre** : Pour fusionner les deux arbres, il faut d'abord extraire les mots du second arbre.
- **Insertion des mots dans l'arbre de base** : Chaque mot du deuxième arbre doit être inséré récursivement dans l'arbre de base. Cette insertion doit respecter la structure de trie hybride.

Cette approche pour la fusion vise à maximiser l’efficacité et à minimiser les redondances, tout en préservant l'intégrité des propriétés du `HybrideTree`.