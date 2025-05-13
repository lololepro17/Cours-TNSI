
import doctest

def convertit_texte_en_binaire(texte: str) -> str:
    """
    convertit un texte en une chaîne binaire (ASCII, 8 bits par caractère)
    >>> convertit_texte_en_binaire("NSI")
    '010011100101001101001001'
    """
    return ''.join(format(ord(c), '08b') for c in texte)

def convertit_binaire_vers_entier_base_10(chaine_binaire: str) -> int:
    """
    convertit une chaîne binaire en entier base 10
    >>> convertit_binaire_vers_entier_base_10("01001110")
    78
    """
    return int(chaine_binaire, 2)

def convertit_binaire_en_texte(chaine_binaire: str) -> str:
    """
    convertit une chaîne binaire (multiple de 8) en texte ASCII
    >>> convertit_binaire_en_texte("010011100101001101001001")
    'NSI'
    """
    return ''.join(chr(int(chaine_binaire[i:i+8], 2)) for i in range(0, len(chaine_binaire), 8))

def chiffre_xor(chaine_binaire: str, clef_binaire: str) -> str:
    """
    chiffre une chaîne binaire par XOR bit à bit avec une clef répétée
    >>> chiffre_xor("010011100101001101001001", "01010100010001010101001001001101")
    '000110100001011000011011'
    """
    clef = (clef_binaire * ((len(chaine_binaire) // len(clef_binaire)) + 1))[:len(chaine_binaire)]
    return ''.join(str(int(a)^int(b)) for a, b in zip(chaine_binaire, clef))

def convertit_binaire_vers_decimal(octet: str) -> int:
    """
    convertit un octet binaire en entier
    >>> convertit_binaire_vers_decimal("01001110")
    78
    """
    return int(octet, 2)

def genere_clefs_publique_et_privee(a1: int, b1: int, a2: int, b2: int) -> tuple:
    """
    génère les clefs publique et privée de kidRSA
    >>> genere_clefs_publique_et_privee(13, 32, 69, 35)
    ((230884490440319, 19432624025979826176), (230884490440319, 491247123152703873))
    """
    M = a1 * b1 - 1
    e = a2 * M + a1
    d = b2 * M + b1
    n = e * d - 1
    return (e, n), (d, n)

def chiffre_message(m: str, clef: tuple) -> list:
    """
    chiffre un message en liste d'entiers avec une clef (e,n)
    >>> chiffre_message("NSI", (230884490440319, 19432624025979826176))[:2]
    [16623683311702968, 19625181687427115]
    """
    e, n = clef
    return [(e * ord(c)) % n for c in m]

def dechiffre_message(m: list, clef: tuple) -> str:
    """
    déchiffre une liste d'entiers en texte avec une clef (d,n)
    >>> dechiffre_message([16623683311702968, 19625181687427115], (491247123152703873, 19432624025979826176))
    'NS'
    """
    d, n = clef
    return ''.join(chr((d * c) % n) for c in m)

def bruteForceKidRSA(e: int, n: int) -> int:
    """
    calcule d tel que (e*d - 1) % n == 0
    >>> bruteForceKidRSA(17, 3120)
    2753
    """
    for d in range(1, n):
        if (e * d - 1) % n == 0:
            return d
    return -1

def egcd(a: int, b: int) -> tuple:
    """
    algorithme d'euclide étendu
    >>> egcd(240, 46)
    (2, -9, 47)
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(e: int, n: int) -> int:
    """
    calcule l'inverse de e modulo n
    >>> modinv(17, 3120)
    2753
    """
    g, x, y = egcd(e, n)
    if g != 1:
        return False
    else:
        return x % n
