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
    def __init__(self):
        '''
        initialise l'arbre de patricia avec une racine vide
        '''
        
        self.root = PatriciaNode()  # Point d'entrée de l'arbre 
        self.root.child = PatriciaNode()
        
        
    def insertion(self, word):
        """
        Insère un mot dans l'arbre Patricia.
        """
        current = self.root.child  # Commence à la racine
        parent = None  # Suivre le parent pour réassigner les liens correctement
    
        # Si le mot est vide, ne rien faire
        if not word :
            return
        # Si la racine est vide, insérer directement
        if current.is_empty():
            current.key = word
            current.make_key()
            return
    
        while not current.is_empty():
            
            diff = ord(head(word)) - ord(head(current.key))  # Comparer les premiers caractères
    
            if diff < 0:  # Le mot est "plus petit", insérer comme frère mais avant
                new_sibling = PatriciaNode(word)
                new_sibling.make_key()
                new_sibling.sibling = current  # Le nœud courant devient le frère
    
                if parent:  # Si le nœud courant a un parent
                    if parent.child == current:  # Si le nœud courant est un enfant
                        parent.child = new_sibling
                    else:  # Sinon, c'est un frère
                        parent.sibling = new_sibling
                else:  # Si le nœud courant est la racine
                    self.root.child = new_sibling
                return
    
            elif diff > 0:  # Le mot est "plus grand", continuer dans les frères
                if not current.sibling:  # Pas de frère, ajouter directement
                    current.sibling = PatriciaNode(word)
                    current.sibling.make_key()
                    return
                parent = current  # Mettre à jour le parent
                current = current.sibling  # Continuer dans les frères
                continue
    
            else:  # Même premier caractère
                prefix = longest_prefix(current.key, word)
    
                if prefix == current.key:  # Le mot descend dans les enfants
                    remaining_word = rest(word, prefix) 
                    ''' le mot restant du mot
                    si le mot courant est ce une clé
                    if current.is_key():
                        current.put_child("\x000");'''
                    if not remaining_word:  # Si le mot est terminé, marquer le nœud comme terminal
                        if not current.is_key() and not current.child:
                            current.make_key()
                        return
                    if not current.child:  # Aucun enfant, créer un nouveau nœud
                        current.child = PatriciaNode(remaining_word)
                        current.child.make_key()
                        return
                    parent = current  # Mettre à jour le parent
                    current = current.child  # Continuer dans les enfants
                    word = remaining_word  # Mise à jour du mot
                    continue
    
                elif prefix == word:  # Le mot est un préfixe complet de la clé actuelle
                    remaining_node_key = rest(current.key, prefix)  # Partie restante de la clé actuelle
    
                    # Créer un nouveau parent pour le mot
                    new_parent = PatriciaNode(word)
                    #not_key(new_parent.key)
                    new_parent.child = PatriciaNode("\x00")  # Le nouveau parent est terminal
                    new_parent.child.sibling = PatriciaNode(remaining_node_key)  # L'ancienne clé devient enfant
                    new_parent.child.sibling.child = current.child  # Réassigner les enfants existants
                    new_parent.sibling = current.sibling  # Réassigner les frères existants
    
                    if parent:  # Si le nœud courant a un parent
                        if parent.child == current:  # Si le nœud courant est un enfant
                            parent.child = new_parent
                        else:  # Sinon, c'est un frère
                            parent.sibling = new_parent
                    else:  # Si le nœud courant est la racine
                        self.root.child = new_parent
                    return
    
                else:  # Préfixe partiel, division nécessaire
                    remaining_node_key = rest(current.key, prefix)  # Partie restante de la clé actuelle
                    remaining_word = rest(word, prefix)  # Partie restante du mot à insérer
                    
                    # Créer le nouveau parent pour le préfixe
                    new_parent = PatriciaNode(prefix)
    
                    # Comparer les deux restes pour les organiser
                    if remaining_node_key < remaining_word:
                        new_parent.child = PatriciaNode(remaining_node_key)
                        new_parent.child.sibling = PatriciaNode(remaining_word)
                        new_parent.child.sibling.make_key()
                        new_parent.sibling=current.sibling
                        new_parent.child.child = current.child
                    else:
                        new_parent.child = PatriciaNode(remaining_word)
                        new_parent.child.make_key()
                        new_fils = PatriciaNode(remaining_node_key)
                        new_fils.child = current.child
                        new_parent.child.sibling = new_fils
                        new_parent.sibling = current.sibling
                        
                    if parent:  # Si le nœud courant a un parent
                        if parent.child == current:  # Si le nœud courant est un enfant
                            parent.child = new_parent
                        else:  # Sinon, cbnn,'est un frère
                            parent.sibling = new_parent
                    else:  # Si le nœud courant est la racine
                        self.root.child = new_parent
                    return
    
    def suppression(self, word):
        """
        Supprime un mot de l'arbre Patricia.
        """
        current = self.root.child
        parent = None  # Suivre le parent pour réassigner les liens
        is_child = False  # Indique si le nœud courant est un enfant du parent
    
        if current.is_empty() or not word:
            return False
    
        while current:
            # Vérifiez si le mot est terminé et que le nœud est terminal
            if not word and current.is_key():
                # Suppression directe
                if not current.child:  # Pas d'enfant, suppression complète
                    if parent:
                        if is_child:
                            parent.child = current.sibling
                        else:
                            parent.sibling = current.sibling
                    else:  # Si c'est la racine
                        self.root.child = current.sibling
                    return True
                # Ce cas ne devrait pas arriver dans un Patricia Trie bien construit
                return False
            # Vérifiez si le mot correspond exactement à une clé terminale
            if current.is_key() and longest_prefix(word, current.key) == word :
                if not current.child:  # Pas d'enfant, suppression complète
                    if parent:
                        if is_child:
                            parent.child = current.sibling
                        else:
                            parent.sibling = current.sibling
                    else:  # Si c'est la racine
                        self.root.child = current.sibling
                    return True
                return False
            # Rechercher le préfixe commun
            prefix = longest_prefix(word, current.key)
    
            if prefix == current.key:  # Préfixe complet, descente dans les enfants
                parent = current
                is_child = True
                current = current.child
                word = rest(word, prefix)
            elif prefix:  # Préfixe partiel, le mot n'existe pas
                return False
            else:  # Aucun préfixe commun, passez au frère
                parent = current
                is_child = False
                current = current.sibling
        return False  # Si le mot n'a pas été trouvé
          
    def recherche(self, word): 
        """
        Recherche un mot dans le Patricia Trie.
        """
        
        current = self.root.child
        
        # Vérification des cas de base
        if current.is_empty() or not word:
            return False
        if not is_ascii(word):
            print("pas ascii")
            return False
        
        word = finish_key(word)  # Ajoute le caractère de fin au mot
        
        while current:
            # Cas d'égalité exacte
            if word == current.key:
                return True
            
            # Trouver le plus long préfixe commun
            prefix = longest_prefix(word, current.key)
            
            if prefix:  # Un préfixe commun existe
                if prefix == current.key:  # Descente dans les enfants
                    word = rest(word, prefix)  # Mise à jour du reste du mot
                    current = current.child
                else:  # Préfixe partiel mais non égal à la clé actuelle
                    return False
            else:  # Aucun préfixe commun, passez au frère
                current = current.sibling
        
        # Si nous sortons de la boucle sans correspondance
        return False
