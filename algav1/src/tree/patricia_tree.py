'''
Created on 27 nov. 2024
@author: diamanka
'''
from node.patricia_node import PatriciaNode
from utilitaire.patricia_util import *
from pip._internal.cli.cmdoptions import pre

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
    
    def ComptageMots(self):
        """
        Compte le nombre de mots dans le Patricia Tree.
        """
        def _count_words(node):
            if not node:
                return 0
            count = 1 if node.is_key() else 0
            count += _count_words(node.child)
            count += _count_words(node.sibling)
            return count
    
        return _count_words(self.root)
    
    def ListeMots(self):
        """
        Liste les mots du Patricia Tree dans l'ordre alphabétique.
        """
        def _list_words(node, prefix, result):
            if not node:
                return
            current_word = prefix + not_key(node.key)
            if node.is_key():
                result.append(current_word)
            _list_words(node.child, current_word, result)
            _list_words(node.sibling, prefix, result)
    
        result = []
        _list_words(self.root, "", result)
        return result
    
    def ComptageNil(self):
        """
        Compte le nombre de pointeurs vers Nil dans le Patricia Tree.
        """
        def _count_nil(node):
            if not node:
                return 1
            count = 0
            count += _count_nil(node.child)
            count += _count_nil(node.sibling)
            return count
    
        return _count_nil(self.root)
    
    def Hauteur(self):
        """
        Calcule la hauteur du Patricia Tree.
        """
        def _height(node, ind = 1):
            if not node:
                return 0
            if ind == 1:
                return 1 + max(_height(node.child), _height(node.sibling,0))
            else :
                return max(_height(node.child), _height(node.sibling,0))
    
        return _height(self.root)

    def Prefixe(self, mot):
        """
        Compte le nombre de mots dont le mot donné est un préfixe.
        """
        def _count_prefixed(node, prefix):
            if not node:
                return 0
            # Vérifier si le prefix est dans ou englobe la clé
            if is_prefix(prefix, node.key) or prefix == node.key:
                # Compter les mots à partir de ce nœud
                if node.is_key():
                    return _count_words(node.child) + 1
                else:
                    return _count_words(node.child)
            elif is_prefix(node.key, prefix):
                return _count_prefixed(node.child, rest(prefix, node.key))
            elif not longest_prefix(prefix, node.key) : # Continuer à chercher dans les frères
                return _count_prefixed(node.sibling, prefix)
           
            return 0
        def _count_words(node):# compter les les mots à partir d'un noeud
            if not node:
                return 0
            count = 1 if node.is_key() else 0
            count += _count_words(node.child)
            count += _count_words(node.sibling)
            return count
    
        return _count_prefixed(self.root.child, mot)

    def ProfondeurMoyenne(self):
        """
        Calcule la profondeur moyenne des feuilles d'un Patricia Tree.
        """
        def _calculate_depth(node, current_depth, total_depth, leaf_count):
            if not node:
                return total_depth, leaf_count
            # Si le nœud est une feuille
            if node.is_key() and not node.child:
                total_depth += current_depth
                leaf_count += 1
            # Récursion sur les enfants et les frères
            total_depth, leaf_count = _calculate_depth(node.child, current_depth + 1, total_depth, leaf_count)
            total_depth, leaf_count = _calculate_depth(node.sibling, current_depth, total_depth, leaf_count)
    
            return total_depth, leaf_count
    
        total_depth, leaf_count = _calculate_depth(self.root, 0, 0, 0)
        # Si aucune feuille n'existe, la profondeur moyenne est 0
        if leaf_count == 0:
            return 0
        # Retourner la profondeur moyenne arrondie à l'entier le plus proche
        return round(total_depth / leaf_count)
