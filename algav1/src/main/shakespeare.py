'''
Created on 16 déc. 2024

@author: diamanka && Omar
'''

import time
import os
from shake.consArbre import *
from shake.hybride_tree_comp import *
from shake.patricia_tree_comp import *


if __name__ == '__main__':
    
    shakespeare_directory = os.path.join(os.path.dirname(__file__), "../Shakespeare")
    
    # Charger tous les mots des fichiers de Shakespeare
    print("=== Chargement des mots des fichiers de Shakespeare ===")
    words = load_shakespeare_words(shakespeare_directory)
    print(f"{len(words)} mots chargés avec succès.\n")
    
    # Patricia Trie
    print("=== Construction du Patricia Trie ===")
    patricia_tree = PatriciaTree()
    PatriciaTree.reset_comparison_count()
    start_time = time.time()
    patricia_tree = construct_patricia_tree(words)
    patricia_time = time.time() - start_time
    print(f"Patricia Trie construit avec {patricia_tree.ComptageMots()} mots en {patricia_time:.4f} secondes et  {PatriciaTree.comparison_count} comparaisons .\n")
    
    # Hybride Trie
    print("=== Construction du Hybride Trie ===")
    hybride_tree = HybrideTree()
    HybrideTree.reset_comparison_count()
    start_time = time.time()
    hybride_tree = construct_hybride_tree(words)
    hybride_time = time.time() - start_time
    print(f"Hybride Trie construit avec {hybride_tree.comptage_mots(hybride_tree.root)} mots en {hybride_time:.4f} secondes et {HybrideTree.comparison_count} comparaisons.\n")
    
    # Comparaison
    print("=== Comparaison des deux structures ===")
    print(f"Nombre total de mots : {len(words)}")
    print(f"Profondeur moyenne (Patricia Trie) : {patricia_tree.ProfondeurMoyenne()}")
    print(f"Profondeur moyenne (Hybride Trie) : {hybride_tree.profondeur_moyenne()}")
    print(f"Hauteur (Patricia Trie) : {patricia_tree.Hauteur()}")
    print(f"Hauteur (Hybride Trie) : {hybride_tree.hauteur()}")
    print(f"Pointeurs NIL (Patricia Trie) : {patricia_tree.ComptageNil()}")
    print(f"Pointeurs NIL (Hybride Trie) : {hybride_tree.comptage_nil()}")
    print(f"Temps d'insertion : Patricia Trie = {patricia_time:.4f}s, Hybride Trie = {hybride_time:.4f}s")
