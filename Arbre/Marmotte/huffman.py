import bisect

class ArbreHuffman :
    def __init__(self, lettre, nbocc, g=None, d=None):
        self.lettre= lettre
        self.nbocc = nbocc
        self.gauche= g
        self. droite = d

    def est_feuille(self) -> bool:
        return ********** -- 1 -- ************************

    def __lt__(self, other):
        # Un arbre A est strictement inférieur à un arbre B si le nombre d'occurrences indiqué dans A est
        # strictement **supérieur** à celui de B
        return self.nbocc > other.nbocc

def parcours(arbre, chemin_en_cours, dico):
    if arbre is None :
        return
    if arbre.est_feuille():
        dico[arbre.lettre] = chemin_en_cours
    else :
        parcours(arbre.gauche, chemin_en_cours + [0], dico)
        ****************  --  2  -- ******************************

def fusionne(gauche, droite) -> ArbreHuffman:
    nbocc_total = *********** -- 3 -- *********************
    return ArbreHuffman(None, nbocc_total, gauche, droite)

def compte_occurrences(texte: str) -> dict:
    """Renvoie un dictionnaire avec chaque caractère du texte comme clé et le nombre d'apparition de ce caractère
    dans le texte en valeur
    >>> compte_occurrences ( "AABCECA")
    {"A": 3, "B": 1, "C": 2, "E": 1}"""
    occ = dict()
    for car in texte :
        if car not in occ :
            ************* -- 4 -- **************************
        occ[car] = occ[car] + 1
    return *********** -- 5 -- ********************

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
    # Tri par nombres d'occurrences décroissants
    liste_arbres.sort()
    # Tant que tous les arbres n'ont pas été fusionnés
    while len(liste_arbres) > 1:
        # Les deux plus petits nombres d'occurrences sont à la fin de la liste
        droite = liste_arbres.pop()
        gauche = liste_arbres.pop()
        new_arbre = fusionne(gauche, droite)
        # Le module bisect permet d'insérer le nouvel arbre dans la liste, de manière à ce que la
        # liste reste triée
        bisect.insort(liste_arbres, new_arbre)
    # Il ne reste plus qu'un arbre dans la liste, c'est notre arbre de Huffman
    arbre_huffman = liste_arbres.pop()
    # Parcours de l'arbre pour relever les codes
    dico = {}
    parcours(arbre_huffman, [], dico)
    return dico

def compresser(texte,dico):
    """# détermine le codage binaire d'un texte entier à partir
    d'un dictionnaire de correspondance
    entrée :    texte, chaine de caratères contenant le texte à compresser
                dico, dictionnaire de correspondance entre clé et code binaire
    sortie :    code binaire sous forme d'une liste"""
    pass

# Script principal
with open("texte.txt") as f:
    texte= f.read()
print(compte_occurrences(texte)) # à commenter ensuite
print(codage_huffman(texte)) # à commenter ensuite


code = compresser(texte,codage_huffman(texte))
taille = len(texte)*8
taille_compresse = len(code)
taux_compression = ((taille-taille_compresse)/taille*100)

assert taille == 56
assert taille_compresse == 18
assert taux_compression == 67.85714285714286

# à décommenter ensuite #######
# print(taille)
# print(taille_compresse)
# print(taux_compression)