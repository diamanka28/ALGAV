'''
Created on 27 nov. 2024
@author: diamanka
@author: omar
'''

def print_ascii():
    """
    Affiche tous les caractères ASCII avec leur code numérique (de 0 à 127).
    """
    print(f"{'Code':<5} {'Caractère':<10}")
    print("-" * 20)
    for i in range(128):
        char = chr(i)
        display_char = char if char.isprintable() else f"\\x{i:02x}"
        print(f"{i:<5} {display_char:<10}")

def is_ascii(s):
    """
    Vérifie si une chaîne est composée uniquement de caractères ASCII.
    """
    return all(0 <= ord(c) <= 127 for c in s)

def head(s):
    """
    Renvoie le premier caractère ASCII d'une chaîne.
    """
    return s[0] if s else ""

def finish_key(word, cara='\x00'):
    """
    Ajoute un caratèere à la fin d'un mot
    """
    return word + cara

def not_key(word, marker='\x00'):
    """
    Supprime le caractère de fin de mot d'une chaîne.
    """
    return word.rstrip(marker)

def is_key(word, marker='\x00'):
    """
    Vérifie si une chaîne contient le marqueur de fin de mot.
    """
    return word.endswith(marker)

def longest_prefix(s1, s2):
    """
    Trouve le plus grand préfixe commun entre deux chaînes.
    """
    prefix = []
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            prefix.append(c1)
        else:
            break
    return ''.join(prefix)

def longest_suffix(s1, s2):
    """
    Trouve le plus long suffixe commun entre deux chaînes.
    """
    '''Parcourir les deux chaînes à partir de la fin'''
    i, j = len(s1) - 1, len(s2) - 1
    suffix = []
    
    while i >= 0 and j >= 0 and s1[i] == s2[j]:
        suffix.append(s1[i])
        i -= 1
        j -= 1
    
    '''Reconstituer le suffixe dans l'ordre correct'''
    return ''.join(reversed(suffix))

def is_prefix(s1, s2):
    """
    Vérifie si s1 est un préfixe de s2.
    """
    return s2.startswith(s1)

def is_suffix(s1, s2):
    """
    Vérifie si s1 est un suffixe de s2.
    """
    return s2.endswith(s1)

def rest(chaine, sous_chaine):
    """
    Retourne la partie restante de 'chaine' après avoir retiré 'sous_chaine'
    si 'sous_chaine' est un préfixe de 'chaine'. Sinon, retourne None.
    """
    if chaine.startswith(sous_chaine):
        return chaine[len(sous_chaine):]
    return ""#caractere vide

