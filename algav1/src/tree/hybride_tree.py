from node.hybrid_node import *

class HybrideTree:
    """
    Classe représentant un arbre Hybride Trie avec des valeurs entières.
    """

    def __init__(self):
        self.root = None

    def est_vide(self):
        """
        Vérifie si l'arbre est vide.
        """
        return self.root is None or self.root.is_empty()

    def inserer(self, mot, valeur):
        """
        Insère un mot avec une valeur entière dans l'arbre et rééquilibre l'arbre si nécessaire.
        """
        def _inserer(node, mot, valeur):
            if not node:
                if len(mot) == 1:
                    return Hybrid_Node(mot[0], valeur)
                return Hybrid_Node(mot[0], None, None, _inserer(None, mot[1:], valeur), None)

            if mot[0] < node.caractere:
                node.inf = _inserer(node.inf, mot, valeur)
            elif mot[0] > node.caractere:
                node.sup = _inserer(node.sup, mot, valeur)
            else:
                if len(mot) == 1:
                    node.valeur = valeur
                else:
                    node.eq = _inserer(node.eq, mot[1:], valeur)
            return node

        self.root = _inserer(self.root, mot, valeur)
        self.root = self.reequilibrer(self.root)  # Rééquilibrage après insertion

    def recherche(self, mot):
        """
        Recherche un mot dans l'arbre.
        """
        def _recherche(node, mot):
            if not node:
                return None
            if mot[0] < node.caractere:
                return _recherche(node.inf, mot)
            elif mot[0] > node.caractere:
                return _recherche(node.sup, mot)
            elif len(mot) == 1:
                return node.valeur
            else:
                return _recherche(node.eq, mot[1:])

        return _recherche(self.root, mot)

    def suppression(self, mot):
        """
        Supprime un mot de l'arbre.
        """
        def _suppression(node, mot):
            if not node:
                return None
            if mot[0] < node.caractere:
                node.inf = _suppression(node.inf, mot)
            elif mot[0] > node.caractere:
                node.sup = _suppression(node.sup, mot)
            elif len(mot) == 1:
                node.valeur = None
            else:
                node.eq = _suppression(node.eq, mot[1:])
            if not node.valeur and not node.inf and not node.eq and not node.sup:
                return None
            return node

        self.root = _suppression(self.root, mot)

    def number_mots(self, node):
        """
        Compte le nombre de mots dans l'arbre.
        """
        def _comptage_mots(node):
            if not node:
                return 0
            count = 1 if node.valeur is not None else 0
            count += _comptage_mots(node.inf)
            count += _comptage_mots(node.eq)
            count += _comptage_mots(node.sup)
            return count

        return _comptage_mots(node)

    def liste_mots(self, prefixe=""):
        """
        Liste les mots dans l'ordre alphabétique sans leurs valeurs.
        """
        def _liste_mots(node, prefixe):
            if not node:
                return []
            mots = []
            mots.extend(_liste_mots(node.inf, prefixe))  # Parcours du sous-arbre inférieur
            if node.valeur is not None:  # Si le nœud est terminal
                mots.append(prefixe + node.caractere)
            mots.extend(_liste_mots(node.eq, prefixe + node.caractere))  # Parcours du sous-arbre égal
            mots.extend(_liste_mots(node.sup, prefixe))  # Parcours du sous-arbre supérieur
            return mots
    
        return _liste_mots(self.root, prefixe)

    def comptage_nil(self):
        """
        Compte le nombre de pointeurs vers Nil.
        """
        def _comptage_nil(node):
            if not node:
                return 1
            count = _comptage_nil(node.inf)
            count += _comptage_nil(node.eq)
            count += _comptage_nil(node.sup)
            return count

        return _comptage_nil(self.root)

    def hauteur(self):
        """
        Calcule la hauteur de l'arbre.
        """
        def _hauteur(node):
            if not node:
                return 0
            return 1 + max(_hauteur(node.inf), _hauteur(node.eq), _hauteur(node.sup))

        return _hauteur(self.root)

    def profondeur_moyenne(self):
        """
        Calcule la profondeur moyenne des feuilles.
        """
        def _profondeur_moyenne(node, profondeur):
            if not node:
                return 0, 0
            if not node.inf and not node.eq and not node.sup:
                return profondeur, 1
            total_profondeur, total_feuilles = 0, 0
            p, f = _profondeur_moyenne(node.inf, profondeur + 1)
            total_profondeur += p
            total_feuilles += f
            p, f = _profondeur_moyenne(node.eq, profondeur + 1)
            total_profondeur += p
            total_feuilles += f
            p, f = _profondeur_moyenne(node.sup, profondeur + 1)
            total_profondeur += p
            total_feuilles += f
            return total_profondeur, total_feuilles

        total_profondeur, total_feuilles = _profondeur_moyenne(self.root, 0)
        return total_profondeur / total_feuilles if total_feuilles else 0

    def prefixe(self, mot):
        """
        Compte combien de mots dans l'arbre ont le mot donné comme préfixe.
        """
        def _prefixe(node, mot):
            if not node:
                return 0
            if mot == "":
                return self.number_mots(node)
            if mot[0] < node.caractere:
                return _prefixe(node.inf, mot)
            elif mot[0] > node.caractere:
                return _prefixe(node.sup, mot)
            else:
                if mot[1:] == "" and (node.valeur or node.valeur == 0) :
                    return 1 + _prefixe(node.eq, mot[1:])
                
                return _prefixe(node.eq, mot[1:])

        return _prefixe(self.root, mot)

    def calculDesequilibre(self, node):
        """
        Calcule le facteur de déséquilibre pour un nœud donné.
        """
        if not node:
            return 0
        inf_value = self.comptage_mots(node.inf)
        sup_value = self.comptage_mots(node.sup)
        return inf_value - sup_value

    def reequilibrer(self, node):
        """
        Rééquilibre un sous-arbre si nécessaire.
        """
        if not node:
            return None

        facteur = self.calculDesequilibre(node)
        seuil = 3  # Définissez le seuil pour le déséquilibre

        # Si le facteur de déséquilibre dépasse le seuil
        if facteur > seuil:
            if node.inf and self.calculDesequilibre(node.inf) < -seuil:
                node.inf = self.rotationGauche(node.inf)
            node = self.rotationDroite(node)

        elif facteur < -seuil:
            if node.sup and self.calculDesequilibre(node.sup) > seuil:
                node.sup = self.rotationDroite(node.sup)
            node = self.rotationGauche(node)

        return node

    def rotationGauche(self, node):
        """
        Effectue une rotation gauche sur un nœud.
        """
        new_root = node.sup
        node.sup = new_root.inf
        new_root.inf = node
        return new_root

    def rotationDroite(self, node):
        """
        Effectue une rotation droite sur un nœud.
        """
        new_root = node.inf
        node.inf = new_root.sup
        new_root.sup = node
        return new_root

    def comptage_mots(self, node):
        """
        Compte le nombre de mots dans un sous-arbre.
        """
        if not node:
            return 0
        count = 1 if node.valeur is not None else 0
        count += self.comptage_mots(node.inf)
        count += self.comptage_mots(node.eq)
        count += self.comptage_mots(node.sup)
        return count
