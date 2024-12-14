'''
Created on 13 déc. 2024

@author: omar
@author: diamanka
'''

class HybridTrie:

    def __init__(self, caractere=' ', valeur='', inf=None, eq=None, sup=None):
        self.caractere = caractere
        self.valeur = valeur
        self.inf = inf
        self.eq = eq
        self.sup = sup

    # Getter et Setter pour caractere
    def get_caractere(self):
        return self.caractere

    def set_caractere(self, c):
        self.caractere = c

    # Getter et Setter pour valeur
    def get_valeur(self):
        return self.valeur

    def set_valeur(self, valeur):
        self.valeur = valeur

    # Getter et Setter pour inf
    def get_inf(self):
        return self.inf

    def set_inf(self, inf):
        self.inf = inf

    # Getter et Setter pour eq
    def get_eq(self):
        return self.eq

    def set_eq(self, eq):
        self.eq = eq

    # Getter et Setter pour sup
    def get_sup(self):
        return self.sup

    def set_sup(self, sup):
        self.sup = sup

    # Vérifie si le trie est vide
    def est_vide(self, a):
        if a is None:
            return True
        return a.get_caractere() == ' ' and a.get_valeur() == '' and a.get_inf() is None and a.get_eq() is None and a.get_sup() is None

    # Ajoute une clé avec une valeur au trie hybride
    def ajout_cle(self, cle, a, v):
        if self.est_vide(a):
            if len(cle) == 1:
                return HybridTrie(cle[0], v)
            else:
                a.eq = HybridTrie()
                return HybridTrie(cle[0], "", HybridTrie(), self.ajout_cle(cle[1:], a.eq, v), HybridTrie())
        else:
            p = cle[0]
            if p < a.get_caractere():
                a.inf = HybridTrie()
                return HybridTrie(a.get_caractere(), a.get_valeur(), self.ajout_cle(cle, a.inf, v), a.get_eq(), a.get_sup())
            elif p > a.get_caractere():
                a.sup = HybridTrie()
                return HybridTrie(a.get_caractere(), a.get_valeur(), a.get_inf(), a.get_eq(), self.ajout_cle(cle, a.sup, v))
            a.eq = HybridTrie()
            return HybridTrie(a.get_caractere(), a.get_valeur(), a.get_inf(), self.ajout_cle(cle[1:], a.eq, v), a.get_sup())

    # Recherche si un mot est présent dans le trie
    def recherche(self, a, mot):
        if self.est_vide(a):
            return False
        if len(mot) == 1:
            return mot[0] == a.get_caractere() and a.get_valeur() != ""
        else:
            p = mot[0]
            if p < a.get_caractere():
                return self.recherche(a.get_inf(), mot)
            elif p > a.get_caractere():
                return self.recherche(a.get_sup(), mot)
            return self.recherche(a.get_eq(), mot[1:])

    # Compte le nombre de mots dans le trie hybride
    def comptage_mots(self, a):
        compteur = 0
        if a.get_valeur() != "":
            compteur += 1
        if a.get_inf() is not None:
            compteur += self.comptage_mots(a.get_inf())
        if a.get_eq() is not None:
            compteur += self.comptage_mots(a.get_eq())
        if a.get_sup() is not None:
            compteur += self.comptage_mots(a.get_sup())
        return compteur

    # Liste des mots dans l'ordre alphabétique
    def liste_mots(self, prefixe=""):
        mots = []
        if self.inf:
            mots.extend(self.inf.liste_mots(prefixe))
        if self.caractere != ' ':
            if self.valeur:
                mots.append(prefixe + self.caractere)
            if self.eq:
                mots.extend(self.eq.liste_mots(prefixe + self.caractere))
        if self.sup:
            mots.extend(self.sup.liste_mots(prefixe))
        return mots

    # Compte les pointeurs vers Nil (None)
    def comptage_nil(self):
        compteur = 0
        if self.inf is None:
            compteur += 1
        else:
            compteur += self.inf.comptage_nil()
        if self.eq is None:
            compteur += 1
        else:
            compteur += self.eq.comptage_nil()
        if self.sup is None:
            compteur += 1
        else:
            compteur += self.sup.comptage_nil()
        return compteur

    # Calcule la hauteur de l'arbre
    def hauteur(self):
        if self is None:
            return 0
        hauteur_inf = self.inf.hauteur() if self.inf else 0
        hauteur_eq = self.eq.hauteur() if self.eq else 0
        hauteur_sup = self.sup.hauteur() if self.sup else 0
        return 1 + max(hauteur_inf, hauteur_eq, hauteur_sup)

    # Calcule la profondeur moyenne des feuilles de l'arbre
    def profondeur_moyenne(self, profondeur=0):
        if self is None:
            return 0, 0
        if not self.inf and not self.eq and not self.sup:
            return profondeur, 1
        total_profondeur = 0
        total_feuilles = 0
        if self.inf:
            p, f = self.inf.profondeur_moyenne(profondeur + 1)
            total_profondeur += p
            total_feuilles += f
        if self.eq:
            p, f = self.eq.profondeur_moyenne(profondeur + 1)
            total_profondeur += p
            total_feuilles += f
        if self.sup:
            p, f = self.sup.profondeur_moyenne(profondeur + 1)
            total_profondeur += p
            total_feuilles += f
        return total_profondeur, total_feuilles

    def profondeur_moyenne_arbre(self):
        total_profondeur, total_feuilles = self.profondeur_moyenne()
        return total_profondeur // total_feuilles if total_feuilles != 0 else 0

    # Compte combien de mots du dictionnaire ont le mot "prefixe"
    def prefixe(self, mot):
        compteur = 0
        if self.caractere != ' ':
            if mot == "":
                if self.valeur:
                    compteur += 1
                if self.eq:
                    compteur += self.eq.comptage_mots(self.eq)
            elif self.caractere == mot[0]:
                if self.eq:
                    compteur += self.eq.prefixe(mot[1:])
        if self.inf:
            compteur += self.inf.prefixe(mot)
        if self.sup:
            compteur += self.sup.prefixe(mot)
        return compteur

    # Supprime un mot du trie
    def suppression(self, mot):
        if not mot:
            self.valeur = ""
        elif mot[0] < self.caractere and self.inf:
            self.inf.suppression(mot)
        elif mot[0] > self.caractere and self.sup:
            self.sup.suppression(mot)
        elif mot[0] == self.caractere and self.eq:
            self.eq.suppression(mot[1:])
