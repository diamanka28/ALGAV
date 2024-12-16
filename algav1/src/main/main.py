'''
Created on 12 déc. 2024

@author: diamanka
@author :  omar 
'''

import argparse
from rendu.manipTree import *
from rendu.manipHybride import *
import shutil
columns, _ = shutil.get_terminal_size()
print("<<<<<<<PATRICIA & HYBRIDE TRIE>>>>>>>>".center(columns))


if __name__ == "__main__":
    """
    la ligne de commande 
    """
    parser = argparse.ArgumentParser(description="Gestion des arbres Patricia.")
    parser.add_argument("action",nargs="?", choices=["inserer", "suppression", "listeMots", 
                                                     "profondeurMoyenne", "prefixe", "fusion"], 
                                                     help="Action à effectuer ")
    parser.add_argument("structure", nargs="?", choices=["0", "1"], help="PATRICIA TRI ou HYBRIDE")
    parser.add_argument("fichier", nargs="?", help="Nom du fichier à utiliser pour l'action.")
    parser.add_argument("prefix", nargs="?", help="le prefix à rechercher.")

    args = parser.parse_args()
    # Cas où aucun argument n'est fourni
    if len(sys.argv) == 1:
    
        # Patricia Trie Test
        print("### Test Patricia Trie ###")
        tree_patricia = PatriciaTree()
        mots_patricia = ["arbre", "algorithme", "avance", "python", "patricia", "trie"]
        for mot in mots_patricia:
            tree_patricia.insertion(mot)
        print("Mots insérés dans Patricia Trie : ", mots_patricia)
        print("Liste des mots dans Patricia Trie :", tree_patricia.ListeMots())
        print("Nombre de mots dans Patricia Trie :", tree_patricia.ComptageMots())
        print("La profondeur moyenne de l'arbre :", tree_patricia.ProfondeurMoyenne())
        print("L'hauteur de l'arbre :", tree_patricia.Hauteur())
        print("Le nombre de nil de l'arbre :", tree_patricia.ComptageNil())

        # Hybride Trie Test
        print("\n### Test Hybride Trie ###")
        tree_hybride = HybrideTree()
        mots_hybride = [("arbre", 1), ("algorithme", 2), ("avance", 3), ("python", 4), ("hybride", 5)]
        for mot, valeur in mots_hybride:
            tree_hybride.inserer(mot, valeur)
        print("Mots insérés dans Hybride Trie : ", [mot for mot, _ in mots_hybride])
        print("Liste des mots dans Hybride Trie :", tree_hybride.liste_mots())
        print("Nombre de mots dans Hybride Trie :", tree_hybride.number_mots(tree_hybride.root))
        print("La profondeur moyenne de l'arbre :", tree_hybride.profondeur_moyenne())
        print("L'hauteur de l'arbre :", tree_hybride.hauteur())
        print("Le nombre de nil de l'arbre :", tree_hybride.comptage_nil())

        sys.exit(0)  # Terminer après les tests pratiques

    #Arguments en ligne de commande mais incomplet
    if not args.action or not args.structure:
        print("Usage : python3 rendu.py <action> <structure> <fichier> [<prefix> ou <fichier>]")
        sys.exit(1)
    #Arguments complets
    else : # à faire selon l'action choisie
        if args.structure :# patricia ou hybride
            """Partie PATRICIA"""
            if args.structure == "0": #Avec la structure Patricia Trie
                if args.action == "inserer":
                    tree = PatriciaTree()
                    if not args.fichier:
                        print("Veillez spécifier le fichier")
                        sys.exit(1)
                    ajout(tree, args.fichier)
                    patricia_to_json(tree, "pat.json")
                    
                elif args.action == "suppression":
                    if not args.fichier:
                        print("Veillez spécifier le fichier")
                        sys.exit(1)
                    tree = json_to_patricia("pat.json")
                    supprime(tree, args.fichier)
                    patricia_to_json(tree, "pat.json")
                
                elif args.action == "listeMots":
                    if not args.fichier:
                        print("Veillez spécifier le fichier représentant l'arbre")
                        sys.exit(1)
                    tree = json_to_patricia(args.fichier)
                    lesmots(tree, "mot.txt")
                    
                elif args.action == "profondeurMoyenne":
                    if not args.fichier:
                        print("Veillez spécifier le fichier représentant l'arbre")
                        sys.exit(1)
                    tree = json_to_patricia(args.fichier)
                    profond_moyenne(tree, "profondeur.txt")
                
                elif args.action == "prefixe":
                    if not args.fichier or not args.prefix:
                        print("le fichier ou le prefix")
                        sys.exit(1)
                    tree = json_to_patricia(args.fichier)
                    prefixe(tree, "prefixe.txt", args.prefix)
                elif args.action == "fusion":
                    if not args.fichier or not args.prefix:
                        print("Il faut les deux fichiers pour la FUSION")
                        sys.exit(1)
                    treeA = json_to_patricia(args.fichier)
                    treeB = json_to_patricia(args.prefix)
                    tree = fusion(treeA, treeB)
                    patricia_to_json(tree, "pat.json")
                else: 
                    print("Action inconnue")
            
            elif args.structure == "1":  # Avec la structure Hybride Trie
                if args.action == "inserer":
                    tree = HybrideTree()
                    if not args.fichier:
                        print("Veuillez spécifier le fichier.")
                        sys.exit(1)
                    inserer(tree, args.fichier)
                    hybride_to_json(tree, "trie.json")
                    
                elif args.action == "suppression":
                    if not args.fichier:
                        print("Veuillez spécifier le fichier.")
                        sys.exit(1)
                    tree = json_to_hybride("trie.json")
                    supprimer(tree, args.fichier)
                    hybride_to_json(tree, "trie.json")
                
                elif args.action == "listeMots":
                    if not args.fichier:
                        print("Veuillez spécifier le fichier représentant l'arbre.")
                        sys.exit(1)
                    tree = json_to_hybride(args.fichier)
                    liste_mots(tree, "mot.txt")
                    
                elif args.action == "profondeurMoyenne":
                    if not args.fichier:
                        print("Veuillez spécifier le fichier représentant l'arbre.")
                        sys.exit(1)
                    tree = json_to_hybride(args.fichier)
                    profondeur_moyenne(tree, "profondeur.txt")
                
                elif args.action == "prefixe":
                    if not args.fichier or not args.prefix:
                        print("Le fichier ou le préfixe est manquant.")
                        sys.exit(1)
                    tree = json_to_hybride(args.fichier)
                    prefixe(tree, args.prefix, "prefixe.txt")
                    
                elif args.action == "fusion":
                    if not args.fichier or not args.prefix:
                        print("Il faut les deux fichiers pour la FUSION.")
                        sys.exit(1)
                    treeA = json_to_hybride(args.fichier)
                    treeB = json_to_hybride(args.prefix)
                    tree = fusion_hybride(treeA, treeB)
                    hybride_to_json(tree, "trie.json")
                else: 
                    print("Action inconnue pour Hybride Trie.")
            else:
                print("Structure inconnue, spécifiez 0 pour Patricia Trie ou 1 pour Hybride Trie.")
                