'''
Created on 13 déc. 2024

@author: omar
'''
"""
GRAPHIQUE
"""

import tkinter as tk
from tkinter import messagebox
from tree.hybride_tree import HybrideTree

# Interface graphique Tkinter
class HybridTrieApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de HybridTrie")

        self.trie = HybrideTree()

        # Entrée pour le mot
        tk.Label(root, text="Mot :").grid(row=0, column=0, padx=10, pady=10)
        self.mot_entry = tk.Entry(root)
        self.mot_entry.grid(row=0, column=1, padx=10, pady=10)

        # Entrée pour la valeur
        tk.Label(root, text="Valeur :").grid(row=1, column=0, padx=10, pady=10)
        self.valeur_entry = tk.Entry(root)
        self.valeur_entry.grid(row=1, column=1, padx=10, pady=10)

        # Bouton pour ajouter un mot
        self.ajouter_button = tk.Button(root, text="Ajouter", command=self.ajouter_mot)
        self.ajouter_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Entrée pour la recherche
        tk.Label(root, text="Rechercher un mot :").grid(row=3, column=0, padx=10, pady=10)
        self.recherche_entry = tk.Entry(root)
        self.recherche_entry.grid(row=3, column=1, padx=10, pady=10)

        # Bouton pour rechercher un mot
        self.recherche_button = tk.Button(root, text="Rechercher", command=self.rechercher_mot)
        self.recherche_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Bouton pour afficher le trie
        self.afficher_button = tk.Button(root, text="Afficher Trie", command=self.afficher_trie)
        self.afficher_button.grid(row=5, column=0, columnspan=2, pady=10)

    def ajouter_mot(self):
        mot = self.mot_entry.get()
        valeur = self.valeur_entry.get()
        if mot and valeur:
            self.trie = self.trie.ajout_cle(mot, self.trie, valeur)
            messagebox.showinfo("Succès", f"Le mot '{mot}' avec la valeur '{valeur}' a été ajouté.")
        else:
            messagebox.showerror("Erreur", "Veuillez entrer un mot et une valeur.")

    def rechercher_mot(self):
        mot = self.recherche_entry.get()
        if mot:
            trouve = self.trie.recherche(self.trie, mot)
            if trouve:
                messagebox.showinfo("Résultat", f"Le mot '{mot}' existe dans le trie.")
            else:
                messagebox.showinfo("Résultat", f"Le mot '{mot}' n'existe pas dans le trie.")
        else:
            messagebox.showerror("Erreur", "Veuillez entrer un mot à rechercher.")

    def afficher_trie(self):
        print("État actuel du HybridTrie :")
        self.trie.afficher_trie()
        print("-" * 40)

if __name__ == "__main__":
    root = tk.Tk()
    app = HybridTrieApp(root)
    root.mainloop()
    