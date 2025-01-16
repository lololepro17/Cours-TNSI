import bisect

class ArbreHuffman:
    def __init__(self, lettre, nbocc, g=None, d=None):
        self.lettre = lettre
        self.nbocc = nbocc
        self.gauche = g
        self.droite = d

    def est_feuille(self) -> bool:
        return self.gauche is None and self.droite is None

    def __lt__(self, other):
        return self.nbocc < other.nbocc


def parcours(arbre, chemin_en_cours, dico):
    if arbre is None:
        return
    if arbre.est_feuille():
        dico[arbre.lettre] = chemin_en_cours
    else:
        parcours(arbre.gauche, chemin_en_cours + [0], dico)
        parcours(arbre.droite, chemin_en_cours + [1], dico)


def fusionne(gauche, droite) -> ArbreHuffman:
    nbocc_total = gauche.nbocc + droite.nbocc
    return ArbreHuffman(None, nbocc_total, gauche, droite)


def compte_occurrences(texte: str) -> dict:
    """Renvoie un dictionnaire avec chaque caractère du texte comme clé et le nombre d'apparition de ce caractère
    dans le texte en valeur
    >>> compte_occurrences ( "AABCECA")"""
    occ = {}
    for car in texte:
        if car not in occ:
            occ[car] = 0
        occ[car] += 1
    return occ


def construit_liste_arbres(texte: str) -> list:
    """ Renvoie une liste d'arbres de Huffman, chacun réduit à une feuille"""
    dic_occurrences = compte_occurrences(texte)
    liste_arbres = []
    for lettre, occ in dic_occurrences.items():
        liste_arbres.append(ArbreHuffman(lettre, occ))
    return liste_arbres


def codage_huffman(texte: str) -> dict:
    """ Codage de Huffman optimal à partir d'un texte
    >>> codage_huffman("AAAABBBBBCCD")
    {'A': [0, 0], 'C': [0, 1, 0], 'D': [0, 1, 1], 'B': [1]}"""
    liste_arbres = construit_liste_arbres(texte)
    liste_arbres.sort()
    # Tant que tous les arbres n'ont pas été fusionnés

    while len(liste_arbres) > 1:
        droite = liste_arbres.pop()
        gauche = liste_arbres.pop()
        new_arbre = fusionne(gauche, droite)
        bisect.insort(liste_arbres, new_arbre)
    # Il ne reste plus qu'un arbre dans la liste, c'est notre arbre de Huffman

    arbre_huffman = liste_arbres.pop()
    dico = {}
    parcours(arbre_huffman, [], dico)
    return dico


def compresser(texte, dico):
    code = []
    for char in texte:
        code.extend(dico[char])
    return code


# Script principal
with open("texte.txt", "w") as f:
    f.write("bonjour")

with open("texte.txt") as f:
    texte = f.read()

print("Occurrences :", compte_occurrences(texte))  # À commenter ensuite
dico = codage_huffman(texte)
print("Codage Huffman :", dico)  # À commenter ensuite
code = compresser(texte, dico)

taille = len(texte) * 8  # Taille en bits (ASCII 8 bits)
taille_compresse = len(code)  # Taille compressée
taux_compression = ((taille - taille_compresse) / taille) * 100

print("Taille originale (bits) :", taille)
print("Taille compressée (bits) :", taille_compresse)
print("Taux de compression :", taux_compression)

# Assertions pour vérification
assert taille == 56
assert taille_compresse == 18
assert taux_compression == 67.85714285714286
