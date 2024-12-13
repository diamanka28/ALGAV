'''
Created on 12 déc. 2024

@author: diamanka
@author : omar
'''

import argparse
from rendu.manipTree import *

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
    if len(sys.argv) <= 3:# le nombre d'argument 
        print("Usage : python3 rendu.py <action> <structure> <fichier> ")
        sys.exit(1)
    else : # à faire selon l'action choisie
        print("<<<<<<<PATRICIA & HYBRIDE TRIE>>>>>>>>")
        """logique code d'abord selon la structure et ensuite l'action
        """
        if args.structure :# patricia ou hybride
            """Partie PATRICIA"""
            if args.structure == "0": #Avec la structure Patricia Trie
                if args.action == "inserer":
                    tree = PatriciaTree()
                    if not args.fichier:
                        print("Veillez spécifier le fichier")
                        sys.exit(1)
                    ajout(tree, args.fichier)
                    patricia_to_json(tree, "trie.json")
                    
                elif args.action == "suppression":
                    if not args.fichier:
                        print("Veillez spécifier le fichier")
                        sys.exit(1)
                    tree = json_to_patricia("trie.json")
                    supprime(tree, args.fichier)
                    patricia_to_json(tree, "trie.json")
                
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
                else: 
                    print("Action inconnue")
                #tree.root.child.print_Node()
                """Partie HYBRIDE"""
            else: # avec la structure Hybride
                print("la partie pour les hybrides")
        else: # pas de structure 
            print("rien à faire sur une structure")
    