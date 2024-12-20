'''
Created on 27 nov. 2024
@author: diamanka
@author: omar
'''
from utilitaire.patricia_util import *

class PatriciaNode(object):
    '''
    cette classe représente le noeud de l'arbre de patricia
    '''

    def __init__(self, key="", sibling = None, child = None ):
        '''
        Constructor
        ''' 
        if not is_ascii(key):
            raise ValueError("La clé doit contenir uniquement des caractères ASCII.")
        self.key = key
        self.sibling = sibling
        self.child = child
    
    def find_sibling(self, key):
        """
        Trouve un frère avec une clé donnée.
        """
        current = self.sibling
        while current:
            if is_prefix(key, current.key):
                return current
            current = current.sibling
        return None
    
    def find_child(self, key):
        """
        Trouve un enfant avec une clé donnée.
        """
        current = self.child
        while current:
            if is_prefix(key, current.key):
                return current
            current = current.sibling
        return None
    
    def is_key(self):
        """
        Vérifie si ce nœud représente une clé complète (fin de mot).
        """
        return is_key(self.key)
    
    def make_key(self):
        """
        Transforme la clé du nœud en clé terminale.
        """
        if not self.is_key():
            self.key = finish_key(self.key)
    
    def is_empty(self):
        """
        Vérifie si le nœud est vide.
        """
        return not self.key and not self.sibling and not self.child
    
    def get_key(self):
        """
        Récupère la clé du nœud.
        """
        return self.key

    def set_key(self, key):
        """
        Définit la clé du nœud.
        """
        if not is_ascii(key):
            raise ValueError("La clé doit contenir uniquement des caractères ASCII.")
        self.key = key

    def get_sibling(self):
        """
        Récupère le frère immédiat du nœud.
        """
        return self.sibling

    def set_sibling(self, sibling):
        """
        Définit le frère immédiat du nœud.
        """
        self.sibling = sibling

    def get_child(self):
        """
        Récupère l'enfant immédiat du nœud.
        """
        return self.child

    def set_child(self, child):
        """
        Définit l'enfant immédiat du nœud.
        """
        self.child = child
    
    def print_Node(self):
        if self:
            print(self.key)
        else :
            print("Noeud vide")
    
    def put_sibling(self, key):
        """
        Insère une clé dans les frères immédiats du nœud s'il n'existe pas déjà.
        """
        if not self.sibling:  # Aucun frère, on crée un nouveau nœud
            self.sibling = PatriciaNode(key)
            return
    
        current = self.sibling
        prev = None
        while current:
            if current.key == key:  # La clé existe déjà
                return
    
            if is_prefix(current.key, key):  # La clé courante est un préfixe de `key`
                # Extraire la partie restante de `key` après `current.key`
                remaining_key = rest(key, current.key)
                current.put_child(remaining_key)  # Continuer dans les enfants
                return
    
            if head(key) < head(current.key):  # Insérer dans l'ordre ASCII
                new_node = PatriciaNode(key)
                if prev:
                    prev.sibling = new_node
                else:
                    self.sibling = new_node
                new_node.sibling = current
                return
    
            prev = current
            current = current.sibling

        # Si on atteint la fin, on ajoute à la fin des frères
        prev.sibling = PatriciaNode(key)

    def put_child(self, key):
        """
        Insère une clé dans les enfants immédiats du nœud s'il n'existe pas déjà.
        """
        if not self.child:  # Aucun enfant, on crée un nouveau nœud
            self.child = PatriciaNode(key)
            return
    
        current = self.child
        prev = None
        while current:
            if current.key == key:  # La clé existe déjà
                return
    
            if is_prefix(current.key, key):  # La clé courante est un préfixe de `key`
                # Extraire la partie restante de `key` après `current.key`
                remaining_key = rest(key, current.key)
                current.put_child(remaining_key)  # Continuer dans les enfants
                return
    
            if head(key) < head(current.key):  # Insérer dans l'ordre ASCII
                new_node = PatriciaNode(key)
                if prev:
                    prev.sibling = new_node
                else:
                    self.child = new_node
                new_node.sibling = current
                return
    
            prev = current
            current = current.sibling
    
        # Si on atteint la fin, on ajoute à la fin des enfants
        prev.sibling = PatriciaNode(key)
    
    def delete_sibling(self, key):
        """
        Supprime une clé des frères immédiats du nœud. ces enfants ne sont pas conservés
        """
        if not self.sibling:
            return
        
        current = self.sibling
        prev = None
        while current:
            if current.key == key:  # Trouvé, on supprime
                if prev:
                    prev.sibling = current.sibling
                else:
                    self.sibling = current.sibling
                return
            prev = current
            current = current.sibling

    def delete_child(self, key):
        """
        Supprime une clé des enfants immédiats du nœud. ces enfants ne sont pas conservés 
        """
        if not self.child:
            return
        
        current = self.child
        prev = None
        while current:
            if current.key == key:  # Trouvé, on supprime
                if prev:
                    prev.sibling = current.sibling
                else:
                    self.child = current.sibling
                return
            prev = current
            current = current.sibling
            
