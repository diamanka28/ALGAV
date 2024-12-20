"""
Created on 14 déc. 2024

@author: diamanka
@author: omar
"""

from tree.hybride_tree import HybrideTree, Hybrid_Node
import sys
import json

def inserer(tree, fichier):
    """Insère successivement les mots du fichier dans l'arbre."""
    if not isinstance(tree, HybrideTree):
        raise TypeError("L'objet doit être un HybrideTree.")
    try:
        with open(fichier, "r") as f:
            i = 0  # Utilisé comme valeur associée pour les mots
            for line in f:
                mots = line.strip().split()
                for mot in mots:
                    tree.inserer(mot, i)
                    i += 1
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' n'a pas été trouvé.")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur s'est produite dans 'inserer': {e}")
        sys.exit(1)

def supprimer(tree, fichier):
    """Supprime successivement les mots du fichier de l'arbre."""
    if not isinstance(tree, HybrideTree):
        raise TypeError("L'objet doit être un HybrideTree.")
    try:
        with open(fichier, "r") as f:
            for line in f:
                mots = line.strip().split()
                for mot in mots:
                    tree.suppression(mot)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' n'a pas été trouvé.")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur s'est produite dans 'supprimer': {e}")
        sys.exit(1)

def hybride_to_json(tree, filename):
    """Convertit un HybrideTree en JSON et sauvegarde dans un fichier."""
    if not isinstance(tree, HybrideTree):
        raise TypeError("L'objet doit être un HybrideTree.")

    def node_to_dict(node):
    
        if not node:
            return None  # Représente un nœud nul dans le JSON
    
        node_dict = {
            "char": node.caractere,  # Le caractère contenu dans le nœud
            "is_end_of_word": node.valeur,  # La valeur entière associée (ou None si pas terminal)
            "left": node_to_dict(node.inf),  # Sous-arbre gauche
            "middle": node_to_dict(node.eq),  # Sous-arbre égal
            "right": node_to_dict(node.sup)  # Sous-arbre droit
        }
        return node_dict

    tree_dict = node_to_dict(tree.root)
    try:
        with open(filename, "w") as f:
            json.dump(tree_dict, f, indent=4)
        print(f"Fichier JSON '{filename}' créé avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la sauvegarde en JSON : {e}")
        sys.exit(1)

def json_to_hybride(filename):
    """Construit un HybrideTree à partir d'un fichier JSON."""
    def dict_to_node(data):
        if not data:
            return None

        node = Hybrid_Node(
            caractere=data["char"],
            valeur=data["is_end_of_word"],
            inf=dict_to_node(data["left"]),
            eq=dict_to_node(data["middle"]),
            sup=dict_to_node(data["right"]),
        )
        return node

    try:
        with open(filename, "r") as f:
            data = json.load(f)
        tree = HybrideTree()
        tree.root = dict_to_node(data)
        return tree
    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur s'est produite dans 'json_to_hybride': {e}")
        sys.exit(1)

def liste_mots(tree, filename):
    """Liste les mots de l'arbre dans l'ordre alphabétique et les écrit dans un fichier."""
    if not isinstance(tree, HybrideTree):
        raise TypeError("L'objet doit être un HybrideTree.")
    try:
        mots = tree.liste_mots()
        with open(filename, "w") as f:
            for mot in mots:
                f.write(mot + "\n")
        print(f"Les mots ont été écrits dans le fichier '{filename}'.")
    except Exception as e:
        print(f"Une erreur s'est produite dans 'liste_mots': {e}")
        sys.exit(1)

def profondeur_moyenne(tree, filename):
    """Calcule la profondeur moyenne des feuilles et l'écrit dans un fichier."""
    if not isinstance(tree, HybrideTree):
        raise TypeError("L'objet doit être un HybrideTree.")
    try:
        moyenne = tree.profondeur_moyenne()
        with open(filename, "w") as f:
            f.write(str(moyenne))
        print(f"La profondeur moyenne des feuilles est écrite dans '{filename}'.")
    except Exception as e:
        print(f"Une erreur s'est produite dans 'profondeur_moyenne': {e}")
        sys.exit(1)

def comptage_mots(tree, filename):
    """Compte les mots dans l'arbre et écrit le résultat dans un fichier."""
    if not isinstance(tree, HybrideTree):
        raise TypeError("L'objet doit être un HybrideTree.")
    try:
        nb_mots = tree.number_mots()
        with open(filename, "w") as f:
            f.write(str(nb_mots))
        print(f"Le nombre de mots a été écrit dans '{filename}'.")
    except Exception as e:
        print(f"Une erreur s'est produite dans 'listemots': {e}")
        sys.exit(1)

def prefixe(tree, prefixe, filename):
    """Compte les mots ayant un préfixe donné et écrit le résultat dans un fichier."""
    if not isinstance(tree, HybrideTree):
        raise TypeError("L'objet doit être un HybrideTree.")
    try:
        nb_prefixe = tree.prefixe(prefixe)
        with open(filename, "w") as f:
            f.write(str(nb_prefixe))
        print(f"Le nombre de mots avec le préfixe '{prefixe}' a été écrit dans '{filename}'.")
    except Exception as e:
        print(f"Une erreur s'est produite dans 'prefixe': {e}")
        sys.exit(1)
        
def fusion_hybride(treeA, treeB):
    """
    fusionne deux arbres d'hybride dont l'un d'entre eux est le résultant
    """
    if not isinstance(treeA, HybrideTree) or not isinstance(treeB, HybrideTree):
        raise TypeError("fusion : les deux objets doivent etre des patricia")
    
    if treeA.est_vide() or treeB.est_vide():
        return treeA if not treeA.est_vide() else treeB     
    
    """criteres de choix du resultant entre treeA et treeB"""
    # le nombre de mots
    retour = treeA if treeA.number_mots(treeA.root) >= treeB.number_mots(treeB.root) else treeB
    """ lister les mots de l'autre arbre"""
    mots = treeA.liste_mots() if treeA.number_mots(treeA.root) < treeB.number_mots(treeB.root) else treeB.liste_mots()
    
    """récupérer la derniere valeur de l'arbre à retourner"""
    valeur = treeA.number_mots(treeA.root) if treeA.number_mots(treeA.root) >= treeB.number_mots(treeB.root) else treeB.number_mots()
    
    for mot in mots :
        retour.inserer(mot, valeur)
        valeur += 1
    
    return retour
    
    


