import bisect

class ArbreHuffman:
    def __init__(self, lettre, nbocc, g=None, d=None):
        self.lettre = lettre
        self.nbocc = nbocc
        self.gauche = g
        self.droite = d

    def est_feuille(self) -> bool:
        # L'arbre est une feuille si les deux fils (gauche et droite) sont None
        return self.gauche is None and self.droite is None

    def __lt__(self, other):
        # Un arbre est inférieur à un autre si son nombre d'occurrences est plus grand
        # (tri décroissant pour utiliser bisect correctement)
        return self.nbocc > other.nbocc


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
    """Renvoie un dictionnaire avec chaque caractère du texte comme clé
    et le nombre d’apparitions de ce caractère en valeur."""
    occ = {}
    for car in texte:
        if car not in occ:
            occ[car] = 1
        else:
            occ[car] += 1
    return occ


def construit_liste_arbres(texte: str) -> list:
    """Renvoie une liste d’arbres de Huffman, chacun réduit à une feuille."""
    dic_occurrences = compte_occurrences(texte)
    liste_arbres = []
    for lettre, occ in dic_occurrences.items():
        liste_arbres.append(ArbreHuffman(lettre, occ))
    return liste_arbres


def codage_huffman(texte: str) -> dict:
    """Génère le codage de Huffman optimal pour un texte donné."""
    liste_arbres = construit_liste_arbres(texte)
    # Tri par nombres d'occurrences décroissants
    liste_arbres.sort()

    # Tant qu’il reste plus d’un arbre
    while len(liste_arbres) > 1:
        # Fusionner les deux arbres avec les plus petites occurrences
        droite = liste_arbres.pop()
        gauche = liste_arbres.pop()
        new_arbre = fusionne(gauche, droite)
        # Insérer le nouvel arbre dans la liste tout en gardant l'ordre
        bisect.insort(liste_arbres, new_arbre)

    # Il reste un seul arbre : c'est l'arbre de Huffman
    arbre_huffman = liste_arbres.pop()
    dico = {}
    parcours(arbre_huffman, [], dico)
    return dico


def compresser(texte: str, dico: dict) -> list:
    """Détermine le codage binaire d’un texte entier à partir d’un dictionnaire de correspondance."""
    code = []
    for char in texte:
        code.extend(dico[char])
    return code


# Script principal
if __name__ == "__main__":
    # Lire le fichier texte
    with open("swann.txt", "r") as f:
        texte = f.read()

    # Afficher les résultats
    print("Occurrences :", compte_occurrences(texte))
    dico = codage_huffman(texte)
    print("Dictionnaire de Huffman :", dico)
    code = compresser(texte, dico)
    print("Texte compressé :", code)

    taille = len(texte) * 8
    taille_compresse = len(code)
    taux_compression = ((taille - taille_compresse) / taille) * 100

    print(f"Taille originale : {taille} bits")
    print(f"Taille compressée : {taille_compresse} bits")
    print(f"Taux de compression : {taux_compression:.2f}%")
