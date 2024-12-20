'''
Created on 17 déc. 2024

@author: diamanka
'''
from node.hybrid_node import Hybrid_Node


class HybrideTree:
    """
    Implémentation de l'arbre Hybride avec suivi des comparaisons.
    """
    comparison_count = 0  # Compteur global

    def __init__(self):
        self.root = None

    def inserer(self, mot, valeur):
        """
        Insère un mot avec une valeur tout en comptant les comparaisons.
        """
        def _inserer(node, mot, valeur):
            if not node:
                if len(mot) == 1:
                    return Hybrid_Node(mot[0], valeur)
                return Hybrid_Node(mot[0], None, None, _inserer(None, mot[1:], valeur), None)

            HybrideTree.comparison_count += 1  # Comparaison pour l'insertion

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

    def recherche(self, mot):
        """
        Recherche un mot dans l'arbre tout en comptant les comparaisons.
        """
        def _recherche(node, mot):
            if not node:
                return False

            HybrideTree.comparison_count += 1  # Comparaison pour la recherche

            if mot[0] < node.caractere:
                return _recherche(node.inf, mot)
            elif mot[0] > node.caractere:
                return _recherche(node.sup, mot)
            elif len(mot) == 1:
                return node.valeur is not None
            else:
                return _recherche(node.eq, mot[1:])

        return _recherche(self.root, mot)
    
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

    @classmethod
    def reset_comparison_count(cls):
        """
        Réinitialise le compteur de comparaisons.
        """
        cls.comparison_count = 0
