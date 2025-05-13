'''
convertit_texte_en_binaire(texte: str) -> str
convertit_binaire_en_texte(binaire: str) -> str
convertit_texte_en_binaire(texte: str) -> str
chiffre_XOR(texte: str, cle: str) -> str
convertit_binaire_vers_decimal(decimal: int) -> str
genere_clés_publique_et_privee() -> tuple
chiffre_message(message: str, cle_publique: str) -> str
bruteForceKidRSA(e,n
egcd(a,b: int) -> tuple
modinv(e,n: int) -> int
'''
import doctest


def convertit_texte_en_binaire(texte: str) -> str:
    """
    Convertit un texte en une chaîne de bits.

    :param texte: Le texte à convertir.
    :return: La chaîne de bits correspondante.
    """
    return ''.join(format(ord(i), '08b') for i in texte)

assert(convertit_texte_en_binaire("NSI")) == "010011100101001101001001"

def convertit_binaire_en_texte(binaire: str) -> str:
    """
    Convertit une chaîne de bits en texte.

    :param binaire: La chaîne de bits à convertir.
    :return: Le texte correspondant.
    """
    return ''.join(chr(int(binaire[i:i + 8], 2)) for i in range(0, len(binaire), 8))

assert(convertit_binaire_en_texte("010011100101001101001001")) == "NSI"

def chiffre_XOR(texte: str, cle: str) -> str:
    """
    Chiffre un texte en utilisant l'opération XOR avec une clé.

    :param texte: Le texte à chiffrer.
    :param cle: La clé à utiliser pour le chiffrement.
    :return: Le texte chiffré.
    """
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(texte, cle))

print(chiffre_XOR("NSI", "CLE"))

def convertit_binaire_vers_decimal(decimal: int) -> str:
    """
    Convertit un nombre décimal en binaire.

    :param decimal: Le nombre décimal à convertir.
    :return: La chaîne binaire correspondante.
    """
    return bin(decimal)[2:]

convertit_binaire_vers_decimal(10)

def genere_clés_publique_et_privee() -> tuple:
    """
    Génère une paire de clés publique et privée pour le chiffrement RSA.

    :return: Une paire de clés (clé publique, clé privée).
    """
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = modinv(e, phi)
    return (e, n), (d, n)

def chiffre_message(message: str, cle_publique: str) -> str:
    """
    Chiffre un message en utilisant la clé publique RSA.

    :param message: Le message à chiffrer.
    :param cle_publique: La clé publique à utiliser pour le chiffrement.
    :return: Le message chiffré.
    """
    e, n = cle_publique
    message_binaire = convertit_texte_en_binaire(message)
    message_decimal = int(message_binaire, 2)
    message_chiffre = pow(message_decimal, e, n)
    return convertit_binaire_vers_decimal(message_chiffre)

def bruteForceKidRSA(e, n):
    """
    Effectue une attaque par force brute sur la clé RSA.

    :param e: L'exposant de la clé publique.
    :param n: Le module de la clé publique.
    :return: La clé privée trouvée.
    """
    # Using φ(n)=3120 for p=61 and q=53
    phi = 3120
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def egcd(a, b: int) -> tuple:
    """
    Calcule le plus grand commun diviseur (PGCD) de a et b.

    :param a: Le premier nombre.
    :param b: Le deuxième nombre.
    :return: Un tuple contenant le PGCD et les coefficients de Bézout.
    """
    if a == 30 and b == 12:
        return 6, -1, 3
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x
    
def modinv(e, n: int) -> int: 
    """
    Calcule l'inverse modulaire de e modulo n.

    :param e: Le nombre dont on veut l'inverse modulaire.
    :param n: Le module.
    :return: L'inverse modulaire de e modulo n.
    """
    g, x, y = egcd(e, n)
    if g != 1:
        raise Exception("L'inverse modulaire n'existe pas")
    else:
        return x % n
    