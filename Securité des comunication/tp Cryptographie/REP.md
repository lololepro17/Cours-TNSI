# Reponse au question du TP

## Propriété = A à démontrer

| A | B | XOR(A, B) | XOR(XOR(A, B), B) |
|---|---|-----------|-------------------|
| 0 | 0 |     0     |         0         |
| 0 | 1 |     1     |         0         |
| 1 | 0 |     1     |         1         |
| 1 | 1 |     0     |         1         |

**Propriété démontrée :**  
XOR(XOR(A, B), B) = A

## Kid RSA : Calcul de M, e, d, n

Soit deux nombres premiers choisis pour Kid RSA :  

- p = 5  
- q = 11  

Calcul de n :  
n = p × q = 5 × 11 = **55**

Choix de e (premier avec (p-1)×(q-1)) :  
(p-1) × (q-1) = 4 × 10 = 40  
On prend e = **3** (car 3 et 40 premiers entre eux)

Calcul de d (inverse de e modulo 40) :  
d × e ≡ 1 (mod 40)  
d × 3 ≡ 1 (mod 40)  
d = **27** (car 3 × 27 = 81, 81 mod 40 = 1)

**Résumé :**  

- n = 55  
- e = 3  
- d = 27

Pour un message M, l'encodage est :  
C = M^e mod n  
Le décodage est :  
M = C^d mod n

**Clé publique :** (n, e) = (55, 3)  
**Clé privée :** (n, d) = (55, 27)

## Chiffrement du message 'a' avec la clé publique

Le code ASCII de la lettre 'a' est **97**.

Chiffrement avec la clé publique (n = 55, e = 3) :

C = M^e mod n  
C = 97^3 mod 55  
97^3 = 912673  
912673 mod 55 = 48 

**Message chiffré : 48**

## Déchiffrement du message avec la clé privée

48^27 mod 55 = 97

**On retrouve bien le code ASCII de 'a' (97).**

## Taille des clefs RSA et vulnérabilité

Sur Internet, la taille des clefs RSA couramment utilisée est de **2048 bits** ou plus (souvent 3072 ou 4096 bits pour une sécurité accrue).

**Technologie capable de casser RSA en quelques secondes :**  
Un **ordinateur quantique** suffisamment puissant, utilisant l'algorithme de Shor, pourrait factoriser de grands nombres premiers très rapidement et ainsi casser RSA en quelques secondes.
