"""
Created on 11 déc. 2024
@author: diamanka
@author: omar
tous les tests se font ici
"""

import json
import sys
from tree.patricia_tree import PatriciaTree, PatriciaNode, not_key

def ajout(tree, fichier):
    """
    Ajoute tous les mots d'un fichier dans l'arbre Patricia.
    """
    if not isinstance(tree, PatriciaTree):
        raise TypeError("L'objet 'tree' doit être un arbre de Patricia.")
    try:
        with open(fichier, "r") as f:
            for line in f:
                mots = line.strip().split()
                for mot in mots:
                    tree.insertion(mot)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' n'a pas été trouvé.")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur s'est produite dans 'ajout': {e}")
        sys.exit(1)

def supprime(tree, fichier):
    """
    Supprime tous les mots du fichier de l'arbre Patricia.
    """
    if not isinstance(tree, PatriciaTree):
        raise TypeError("L'objet 'tree' doit être un arbre de Patricia.")
    try:
        with open(fichier, "r") as f:
            for line in f:
                mots = line.strip().split()
                for mot in mots:
                    if not tree.suppression(mot):
                        print(mot + " pas supprimé")
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' n'a pas été trouvé.")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur s'est produite dans 'supprime': {e}")
        sys.exit(1)

def node_to_dict(node):
    """
    Convertit un nœud Patricia en un dictionnaire compatible avec JSON.
    """
    if not node:
        return {}

    node_dict = {
        "label": not_key(node.key),
        "is_end_of_word": node.is_key(),
        "children": {}
    }

    child = node.child
    while child:
        first_char = child.key[0] if child.key else ""
        node_dict["children"][first_char] = node_to_dict(child)
        child = child.sibling

    return node_dict

def patricia_to_json(tree, filename):
    """
    Convertit l'arbre en JSON et sauvegarde dans un fichier.
    """
    tree_dict = node_to_dict(tree.root)
    with open(filename, 'w') as f:
        json.dump(tree_dict, f, indent=4)
    print(f"Fichier JSON '{filename}' créé avec succès.")

def dict_to_node(dictionnaire):
    """
    Convertit un dictionnaire en un nœud Patricia.
    """
    node = PatriciaNode(dictionnaire['label'])
    if dictionnaire["is_end_of_word"]:
        node.make_key()

    for _, valeur in dictionnaire['children'].items():
        child = dict_to_node(valeur)
        if not node.child:
            node.child = child
        else:
            sibling = node.child
            while sibling.sibling:
                sibling = sibling.sibling
            sibling.sibling = child
    return node

def json_to_patricia(filename):
    """
    Construit un arbre Patricia à partir d'un fichier JSON.
    """
    tree = PatriciaTree()
    with open(filename, "r") as f:
        dictionnaire = json.load(f)
    tree.root = dict_to_node(dictionnaire)
    return tree

def lesmots(tree, filename):
    """
    Liste les mots de l'arbre dans le fichier 'filename'.
    """
    if not isinstance(tree, PatriciaTree):
        raise TypeError("L'objet doit être un arbre de Patricia.")
    
    try:
        # Appeler la méthode ListeMots pour obtenir tous les mots
        mots = tree.ListeMots()
        
        # Écrire les mots dans le fichier, un par ligne
        with open(filename, "w") as f:
            for mot in mots:
                f.write(mot + "\n")
        print(f"Les mots ont été écrits dans le fichier '{filename}'.")
    
    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur s'est produite dans 'lesmots': {e}")
        sys.exit(1)
   
def profond_moyenne(tree, filename):
    """
    calcule la profondeur moyenne des feuilles
    """
    if not isinstance(tree, PatriciaTree):
        raise TypeError("L'objet doit être un arbre de Patricia.")
    try:
        moyy = tree.ProfondeurMoyenne()
        
        with open(filename, "w") as f:
            f.write(str(moyy))
        print(f"La profondeur moyenne des feuilles est écrite dans '{filename}'.")
    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur s'est produite dans 'lesmots': {e}")
        sys.exit(1)
    
def prefixe(tree, filename, mot):
    """
    calcule la profondeur moyenne des feuilles
    """
    if not isinstance(tree, PatriciaTree):
        raise TypeError("L'objet doit être un arbre de Patricia.")
    try:
        moyy = tree.Prefixe(mot)
        
        with open(filename, "w") as f:
            f.write(str(moyy))
        print(f"Les mots avec comme préfixe '{mot}' sont écrite dans '{filename}'.")
    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur s'est produite dans 'lesmots': {e}")
        sys.exit(1)

def fusion(treeA, treeB):
    """
    fusionne deux arbres de patricia dont l'un d'entre eux est le résultant
    """
    if not isinstance(treeA, PatriciaTree) or not isinstance(treeB, PatriciaTree):
        raise TypeError("fusion : les deux objets doivent etre des patricia")
    
    if treeA.root.child.is_empty() or treeB.root.child.is_empty():
        return treeA if not treeA.child.is_empty() else treeB
    
    """criteres de choix du resultant entre treeA et treeB"""
    # le nombre de mots
    retour = treeA if len(treeA.ListeMots()) >= len(treeB.ListeMots()) else treeB
    """ lister les mots de l'autre arbre"""
    mots = treeA.ListeMots() if len(treeA.ListeMots()) < len(treeB.ListeMots()) else treeB.ListeMots()
    
    for mot in mots :
        retour.insertion(mot)
        
    return retour
    