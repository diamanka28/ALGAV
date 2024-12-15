class Hybrid_Node:
    """
    Classe représentant un nœud d'un HybridTrie avec une valeur entière.
    """

    def __init__(self, caractere='', valeur=None, inf=None, eq=None, sup=None):
        """
        Constructeur du nœud hybride.

        :param caractere: Le caractère contenu dans le nœud.
        :param valeur: La valeur entière associée si le nœud marque la fin d'un mot.
        :param inf: Le sous-arbre des caractères inférieurs.
        :param eq: Le sous-arbre des caractères égaux.
        :param sup: Le sous-arbre des caractères supérieurs.
        """
        if not (0 <= ord(caractere) <= 127):
            raise ValueError("Le caractère doit être ASCII.")
        if valeur is not None and not isinstance(valeur, int):
            raise ValueError("La valeur doit être un entier ou None.")
        
        self.caractere = caractere
        self.valeur = valeur
        self.inf = inf
        self.eq = eq
        self.sup = sup

    def is_key(self):
        """
        Vérifie si ce nœud marque la fin d'un mot (valeur non None).
        """
        return self.valeur is not None

    def make_key(self, valeur):
        """
        Marque ce nœud comme une clé en lui attribuant une valeur entière.
        """
        if not isinstance(valeur, int):
            raise ValueError("La valeur doit être un entier.")
        self.valeur = valeur

    def is_empty(self):
        """
        Vérifie si ce nœud est vide.
        """
        return self.caractere == '' and self.valeur is None and not self.inf and not self.eq and not self.sup

    def print_node(self):
        """
        Affiche les informations du nœud.
        """
        print(f"Caractère: {self.caractere}, Valeur: {self.valeur}")
        if self.inf:
            print(f"  Inf: {self.inf.caractere}")
        if self.eq:
            print(f"  Eq: {self.eq.caractere}")
        if self.sup:
            print(f"  Sup: {self.sup.caractere}")

