'''
Created on 16 déc. 2024

@author: diamanka
'''

import os
from shake.patricia_tree_comp import PatriciaTree
from shake.hybride_tree_comp import HybrideTree
from rendu.manipTree import patricia_to_json
from rendu.manipHybride import hybride_to_json

def load_shakespeare_words(directory):
    """
    Charge tous les mots des fichiers dans un répertoire donné.
    """
    # Utilisation d'un chemin absolu
    directory = os.path.abspath(directory)
    
    words = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r") as file:
                words.extend(line.strip() for line in file if line.strip())
    return words

def construct_patricia_tree(words):
    """
    Construit un Patricia Trie à partir d'une liste de mots.
    """
    tree = PatriciaTree()
    for word in words:
        tree.insertion(word)
    return tree


def construct_hybride_tree(words):
    """
    Construit un Hybrid Trie à partir d'une liste de mots avec des valeurs numériques.
    """
    tree = HybrideTree()
    for idx, word in enumerate(words):
        #print(word)
        tree.inserer(word, idx)  # Associe chaque mot à son index
    return tree


def save_tree_to_json(tree, filename, structure="patricia"):
    """
    Sauvegarde un arbre (Patricia ou Hybrid) dans un fichier JSON.
    """
    if structure == "patricia":
        patricia_to_json(tree, filename)
    elif structure == "hybride":
        hybride_to_json(tree, filename)


def compare_trees(patricia_tree, hybride_tree):
    """
    Compare les deux arbres selon différents critères.
    """
    print("=== Comparaison des deux arbres ===")
    print(f"Nombre de mots dans le Patricia Trie : {patricia_tree.ComptageMots()}")
    print(f"Nombre de mots dans le Hybrid Trie : {hybride_tree.number_mots(hybride_tree.root)}")
    print(f"Hauteur du Patricia Trie : {patricia_tree.Hauteur()}")
    print(f"Hauteur du Hybrid Trie : {hybride_tree.hauteur()}")
    print(f"Profondeur moyenne des feuilles (Patricia) : {patricia_tree.ProfondeurMoyenne()}")
    print(f"Profondeur moyenne des feuilles (Hybrid) : {hybride_tree.profondeur_moyenne()}")
