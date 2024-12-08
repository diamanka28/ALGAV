'''
Created on 27 nov. 2024
@author: diamanka
'''
from node.patricia_node import PatriciaNode
from utilitaire.patricia_util import *

class PatriciaTree(object):
    '''
    Cette classe représente l'arbre de patricia avec notre conception de représentation
    '''
    def __init__(self, params):
        '''
        initialise l'arbre de patricia avec une racine vide
        '''
        
        self.root = PatriciaNode()  # Point d'entrée de l'arbre 
        
    def insertion(self, word):
        """
        Insère un mot dans l'arbre Patricia.
        """
        current = self.root
        while word:
            # Trouver le plus grand préfixe commun avec le nœud courant
            prefix = longest_prefix(word, current.key)
            
            if prefix == current.key:  # Cas où le mot descend dans un enfant
                word = rest(word, prefix)
                if not current.child:  # Si aucun enfant, crée un nouveau nœud
                    current.child = PatriciaNode(word)
                    current.child.make_key()
                    return
                current = current.child
            else:  # Cas où un préfixe partiel correspond (division nécessaire)
                new_sibling = PatriciaNode(word)
                new_sibling.make_key()
                new_sibling.sibling = current.sibling
                current.sibling = new_sibling
                return

        