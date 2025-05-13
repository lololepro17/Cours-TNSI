import doctest

def convertit_texte_en_binaire(texte: str) -> str:
    """Convertit chaque caractère du texte en sa représentation binaire (ASCII sur 8 bits)."""
    resultat = ""
    for caractere in texte:
        # Obtenir la valeur ASCII du caractère
        valeur_ascii = ord(caractere)
        # Convertir la valeur en une chaîne binaire sur 8 bits
        binaire = format(valeur_ascii, '08b')
        # Ajouter cette représentation à la chaîne résultat
        resultat += binaire
    return resultat

def convertit_binaire_vers_entier_base_10(chaine_binaire: str) -> int:
    """Convertit une chaîne binaire en un nombre entier (base 10)."""
    # Utilise la fonction intégrée int() avec la base 2 pour la conversion
    entier = int(chaine_binaire, 2)
    return entier

def convertit_binaire_en_texte(chaine_binaire: str) -> str:
    """Convertit une chaîne binaire (8 bits par caractère) en texte ASCII."""
    texte = ""
    # Traiter la chaîne en segments de 8 caractères
    for i in range(0, len(chaine_binaire), 8):
        octet = chaine_binaire[i:i+8]
        # Convertir chaque octet binaire en entier
        valeur = int(octet, 2)
        # Convertir la valeur entière en caractère ASCII
        caractere = chr(valeur)
        texte += caractere
    return texte

def chiffre_xor(chaine_binaire: str, clef_binaire: str) -> str:
    """Applique un XOR bit à bit entre la chaîne binaire et une clé répétée pour couvrir toute sa longueur."""
    # Calculer combien de fois répéter la clé pour couvrir la chaîne
    repetition = (len(chaine_binaire) // len(clef_binaire)) + 1
    clef_complete = clef_binaire * repetition
    # Tronquer la clé au même nombre de bits que la chaîne d'entrée
    clef_finale = clef_complete[:len(chaine_binaire)]
    
    resultat = ""
    # Appliquer l'opération XOR pour chaque paire de bits
    for bit1, bit2 in zip(chaine_binaire, clef_finale):
        xor_bit = int(bit1) ^ int(bit2)
        resultat += str(xor_bit)
    return resultat

def convertit_binaire_vers_decimal(octet: str) -> int:
    """Convertit un octet (8 bits) en son équivalent décimal."""
    decimal_value = int(octet, 2)
    return decimal_value

def genere_clefs_publique_et_privee(a1: int, b1: int, a2: int, b2: int) -> tuple:
    """Génère une paire de clés (publique, privée) pour kidRSA en suivant ces étapes:
    
    1. Calcul de M = a1 * b1 - 1.
    2. Calcul de la clé publique e = a2 * M + a1.
    3. Calcul de la clé privée d = b2 * M + b1.
    4. Calcul du module n = e * d - 1.
    """
    # Calcul intermédiaire
    M = a1 * b1 - 1
    # Calcul de la clé publique
    e = a2 * M + a1
    # Calcul de la clé privée
    d = b2 * M + b1
    # Calcul du module commun
    n = e * d - 1
    return (e, n), (d, n)

def chiffre_message(m: str, clef: tuple) -> list:
    """Crypte un message texte en une liste d'entiers à l'aide de la clé publique (e, n).
    
    Pour chaque caractère du message:
    1. Convertir le caractère en son code ASCII.
    2. Calculer (e * code ASCII) mod n.
    3. Ajouter le résultat dans la liste chiffrée.
    """
    e, n = clef
    message_chiffre = []
    for caractere in m:
        ascii_val = ord(caractere)
        chiffre = (e * ascii_val) % n
        message_chiffre.append(chiffre)
    return message_chiffre

def dechiffre_message(m: list, clef: tuple) -> str:
    """Décrypte une liste d'entiers en reconstituant le texte original à l'aide de la clé privée (d, n).
    
    Pour chaque entier dans la liste chiffrée:
    1. Calculer (d * entier) mod n.
    2. Convertir le résultat en caractère ASCII.
    3. Assembler les caractères pour former le message.
    """
    d, n = clef
    message = ""
    for chiffre in m:
        ascii_val = (d * chiffre) % n
        caractere = chr(ascii_val)
        message += caractere
    return message

def bruteForceKidRSA(e: int, n: int) -> int:
    """Recherche par force brute la clé de décryptage d pour kidRSA telle que (e * d - 1) est divisible par n.
    
    Itère sur des valeurs possibles de d de 1 à n-1.
    """
    for d in range(1, n):
        if (e * d - 1) % n == 0:
            return d
    return -1

def egcd(a: int, b: int) -> tuple:
    """Calcule l'algorithme d'Euclide étendu.
    
    Retourne un tuple (g, x, y) satisfaisant l'équation: a * x + b * y = g,
    où g est le plus grand commun diviseur (PGCD) de a et b.
    """
    if a == 0:
        return (b, 0, 1)
    else:
        # Appel récursif pour calculer le PGCD et les coefficients
        g, x1, y1 = egcd(b % a, a)
        # Calcul des nouveaux coefficients pour l'équation linéaire
        x = y1 - (b // a) * x1
        y = x1
        return (g, x, y)

def modinv(e: int, n: int) -> int:
    """Calcule l'inverse modulaire de e modulo n en utilisant l'algorithme d'Euclide étendu.
    
    Si e et n ne sont pas premiers entre eux, la fonction retourne False.
    """
    g, x, _ = egcd(e, n)
    if g != 1:
        return False
    else:
        return x % n

if __name__ == '__main__':
    import doctest
    doctest.testmod()
