'''
Created on 17 déc. 2024

@author: diamanka
'''
from node.patricia_node import PatriciaNode
from utilitaire.patricia_util import *


class PatriciaTree:
    """
    Implémentation du Patricia Trie avec suivi du nombre de comparaisons.
    """
    comparison_count = 0  # Compteur global pour suivre les comparaisons

    def __init__(self):
        self.root = PatriciaNode()  # Racine de l'arbre

    def insertion(self, word):
        """
        Insère un mot dans le Patricia Trie tout en comptant les comparaisons.
        """
        current = self.root.child
        parent = None

        if not word:
            return

        if current.is_empty():
            current.key = word
            current.make_key()
            return

        while current:
            diff = ord(head(word)) - ord(head(current.key))
            PatriciaTree.comparison_count += 1  # Comparaison des caractères

            if diff < 0:
                new_sibling = PatriciaNode(word)
                new_sibling.make_key()
                new_sibling.sibling = current
                if parent:
                    if parent.child == current:
                        parent.child = new_sibling
                    else:
                        parent.sibling = new_sibling
                else:
                    self.root.child = new_sibling
                return

            elif diff > 0:
                if not current.sibling:
                    current.sibling = PatriciaNode(word)
                    current.sibling.make_key()
                    return
                parent = current
                current = current.sibling
                continue

            else:
                prefix = longest_prefix(current.key, word)
                PatriciaTree.comparison_count += len(prefix)  # Comparaisons pour le préfixe

                if prefix == current.key:
                    remaining_word = rest(word, prefix)
                    if not remaining_word:
                        if not current.is_key() and not current.child:
                            current.make_key()
                        return
                    if not current.child:
                        current.child = PatriciaNode(remaining_word)
                        current.child.make_key()
                        return
                    parent = current
                    current = current.child
                    word = remaining_word
                    continue

                elif prefix == word:
                    remaining_node_key = rest(current.key, prefix)
                    new_parent = PatriciaNode(word)
                    new_parent.child = PatriciaNode("\x00")
                    new_parent.child.sibling = PatriciaNode(remaining_node_key)
                    new_parent.child.sibling.child = current.child
                    new_parent.sibling = current.sibling

                    if parent:
                        if parent.child == current:
                            parent.child = new_parent
                        else:
                            parent.sibling = new_parent
                    else:
                        self.root.child = new_parent
                    return

                else:
                    remaining_node_key = rest(current.key, prefix)
                    remaining_word = rest(word, prefix)
                    new_parent = PatriciaNode(prefix)

                    if remaining_node_key < remaining_word:
                        new_parent.child = PatriciaNode(remaining_node_key)
                        new_parent.child.sibling = PatriciaNode(remaining_word)
                        new_parent.child.sibling.make_key()
                        new_parent.child.child = current.child
                    else:
                        new_parent.child = PatriciaNode(remaining_word)
                        new_parent.child.make_key()
                        new_parent.child.sibling = PatriciaNode(remaining_node_key)
                        new_parent.child.sibling.child = current.child
                    new_parent.sibling = current.sibling

                    if parent:
                        if parent.child == current:
                            parent.child = new_parent
                        else:
                            parent.sibling = new_parent
                    else:
                        self.root.child = new_parent
                    return

    def recherche(self, word):
        """
        Recherche un mot dans le Patricia Trie en comptant les comparaisons.
        """
        current = self.root.child

        if current.is_empty() or not word:
            return False

        word = finish_key(word)

        while current:
            PatriciaTree.comparison_count += 1  # Comparaison exacte
            if word == current.key:
                return True

            prefix = longest_prefix(word, current.key)
            PatriciaTree.comparison_count += len(prefix)  # Comparaison pour le préfixe

            if prefix:
                if prefix == current.key:
                    word = rest(word, prefix)
                    current = current.child
                else:
                    return False
            else:
                current = current.sibling

        return False

    def suppression(self, word):
        """
        Supprime un mot du Patricia Trie tout en comptant les comparaisons.
        """
        current = self.root.child
        parent = None
        is_child = False

        if current.is_empty() or not word:
            return False

        while current:
            PatriciaTree.comparison_count += 1  # Comparaison pour la suppression
            if not word and current.is_key():
                if not current.child:
                    if parent:
                        if is_child:
                            parent.child = current.sibling
                        else:
                            parent.sibling = current.sibling
                    else:
                        self.root.child = current.sibling
                    return True
                return False

            prefix = longest_prefix(word, current.key)
            PatriciaTree.comparison_count += len(prefix)  # Comparaison pour le préfixe

            if prefix == current.key:
                parent = current
                current = current.child
                is_child = True
                word = rest(word, prefix)
            else:
                parent = current
                current = current.sibling
                is_child = False
        return False

    @classmethod
    def reset_comparison_count(cls):
        """
        Réinitialise le compteur de comparaisons.
        """
        cls.comparison_count = 0
