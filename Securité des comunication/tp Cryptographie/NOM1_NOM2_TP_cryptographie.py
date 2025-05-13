import doctest

def convertit_texte_en_binaire(texte: str) -> str:
    """Convertit chaque caractère du texte en sa représentation binaire (ASCII sur 8 bits)."""
    resultat = ""
    for caractere in texte:
        
        valeur_ascii = ord(caractere) # Obtenir la valeur ASCII du caractère
        
        binaire = format(valeur_ascii, '08b') # Virer le formatage pour obtenir une chaîne binaire de 8 bits
        
        resultat += binaire # Ajouter au résultat
    return resultat

def convertit_binaire_vers_entier_base_10(chaine_binaire: str) -> int:
    """Convertit une chaîne binaire en un nombre entier (base 10)."""
    entier = int(chaine_binaire, 2) # Convertir la chaîne binaire en entier
    return entier

def convertit_binaire_en_texte(chaine_binaire: str) -> str:
    """Convertit une chaîne binaire (8 bits par caractère) en texte ASCII."""
    texte = ""
    for i in range(0, len(chaine_binaire), 8): # Traiter 8 bits à la fois
        octet = chaine_binaire[i:i+8] # Extraire un octet de 8 bits
        valeur = int(octet, 2) # Convertir l'octet binaire en entier
        caractere = chr(valeur) # Convertir l'entier en caractère ASCII
        texte += caractere # Ajouter le caractère au texte
    return texte

def chiffre_xor(chaine_binaire: str, clef_binaire: str) -> str:
    """Applique un XOR bit à bit entre la chaîne binaire et une clé répétée pour couvrir toute sa longueur."""
    repetition = (len(chaine_binaire) // len(clef_binaire)) + 1  # Répéter la clé pour couvrir la longueur de la chaîne binaire
    clef_complete = clef_binaire * repetition  # Répéter la clé
    clef_finale = clef_complete[:len(chaine_binaire)]  # Ajuster la longueur de la clé

    resultat = ""  # Initialiser le résultat
    for i in range(len(chaine_binaire)):
        bit1 = chaine_binaire[i]
        bit2 = clef_finale[i]
        xor_bit = int(bit1) ^ int(bit2)  # Appliquer le XOR bit à bit
        resultat += str(xor_bit)  # Ajouter le résultat du XOR à la chaîne de résultat
    return resultat

def convertit_binaire_vers_decimal(octet: str) -> int:
    """Convertit un octet (8 bits) en son équivalent décimal."""
    decimal_value = int(octet, 2) # Convertir l'octet binaire en entier
    return decimal_value

def genere_clefs_publique_et_privee(a1: int, b1: int, a2: int, b2: int) -> tuple:
    """Génère une paire de clés (publique, privée) pour kidRSA en suivant ces étapes:
    
    1. Calcul de M = a1 * b1 - 1.
    2. Calcul de la clé publique e = a2 * M + a1.
    3. Calcul de la clé privée d = b2 * M + b1.
    4. Calcul du module n = e * d - 1.
    """
    M = a1 * b1 - 1
    e = a2 * M + a1
    d = b2 * M + b1
    
    n = e * d - 1
    return (e, n), (d, n)

def chiffre_message(m: str, clef: tuple) -> list:
    """Crypte un message texte en une liste d'entiers à l'aide de la clé publique (e, n).
    
    Pour chaque caractère du message:
    1. Convertir le caractère en son code ASCII.
    2. Calculer (e * code ASCII) mod n.
    3. Ajouter le résultat dans la liste chiffrée.
    """
    e, n = clef # Extraire la clé publique
    message_chiffre = [] # Initialiser la liste chiffrée
    for caractere in m: 
        ascii_val = ord(caractere) 
        chiffre = (e * ascii_val) % n # Calculer le chiffre
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
    print("Tous les tests ont réussi.")
    # Exemple d'utilisation
    texte = "Bonjour"
    clef = "10101010"
    texte_binaire = convertit_texte_en_binaire(texte)
    print(f"Texte binaire: {texte_binaire}")
    entier = convertit_binaire_vers_entier_base_10(texte_binaire)
    print(f"Entier: {entier}")
    texte_dechiffre = convertit_binaire_en_texte(texte_binaire)
    print(f"Texte déchiffré: {texte_dechiffre}")
    texte_chiffre = chiffre_xor(texte_binaire, clef)
    print(f"Texte chiffré: {texte_chiffre}")
    clef_publique, clef_privee = genere_clefs_publique_et_privee(3, 7, 5, 11)
    print(f"Clé publique: {clef_publique}")
    print(f"Clé privée: {clef_privee}")
    message = "Hello"
    message_chiffre = chiffre_message(message, clef_publique)
    print(f"Message chiffré: {message_chiffre}")
    message_dechiffre = dechiffre_message(message_chiffre, clef_privee)
    print(f"Message déchiffré: {message_dechiffre}")
    d = bruteForceKidRSA(clef_publique[0], clef_publique[1])
    print(f"Clé de déchiffrement trouvée par force brute: {d}")
    clef_inverse = modinv(clef_publique[0], clef_publique[1])
    print(f"Inverse modulaire de la clé publique: {clef_inverse}")
