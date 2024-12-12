'''
Created on 12 déc. 2024

@author: diamanka
'''

import argparse
from rendu.manipTree import *

if __name__ == "__main__":
    """
    la ligne de commande 
    """
    parser = argparse.ArgumentParser(description="Gestion des arbres Patricia.")
    parser.add_argument("action",nargs="?", choices=["inserer", "suppression"], help="Action à effectuer ")
    parser.add_argument("structure", nargs="?", choices=["0", "1"], help="PATRICIA TRI ou HYBRIDE")
    parser.add_argument("fichier", nargs="?", help="Nom du fichier à utiliser pour l'action.")

    args = parser.parse_args()
    if len(sys.argv) <= 3:# le nombre d'argument 
        print("Usage : python3 rendu.py <action> <structure> <fichier> ")
        sys.exit(1)
    else : # à faire selon l'action choisie
        print("Welcome")
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
                    
                else: 
                    print("action pas prete")
                #tree.root.child.print_Node()
                """Partie HYBRIDE"""
            else: # avec la structure Hybride
                print()
        else: # pas de structure 
            print("rien à faire sur une structure")
    