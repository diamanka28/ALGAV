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

    @classmethod
    def reset_comparison_count(cls):
        """
        Réinitialise le compteur de comparaisons.
        """
        cls.comparison_count = 0
