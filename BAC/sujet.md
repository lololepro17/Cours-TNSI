# Réponses aux Sujets d'Examen NSI 2024

Reponse en 20 sujet de type bac.

---

## Sujet 01

### Exercice 1 : Taille d'un arbre binaire

**Énoncé :**  
On stocke un arbre binaire de caractères dans un dictionnaire. Pour un nœud donné, `arbre[lettre]` renvoie la liste `[fils_gauche, fils_droit]` (le fils vide est représenté par la chaîne vide `""`). On souhaite définir la fonction récursive `taille(arbre, lettre)` qui renvoie le nombre total de nœuds de l'arbre.

```python
def taille(arbre, lettre):
    # si le nœud est vide, il n'y a pas de nœud à compter
    if lettre == "":
        return 0
    # on récupère les fils gauche et droit
    fils_gauche, fils_droit = arbre[lettre]
    # on compte 1 pour le nœud courant, puis on ajoute la taille des sous-arbres gauche et droit
    return 1 + taille(arbre, fils_gauche) + taille(arbre, fils_droit)
```

Explication :
Si la valeur de lettre est vide il n'y a pas de nœud. Sinon, on compte 1 et on ajoute récursivement la taille des sous-arbres gauche et droit.

### Exercice 2 : Tri par sélection

**Énoncé :**
Compléter le code du tri par sélection

```python
def echange(tab, i, j):
    # échange les éléments d'indice i et j dans le tableau tab
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_selection(tab):
    # trie la liste tab par ordre croissant grâce au tri par sélection
    N = len(tab)
    for k in range(0, N-1):
        imin = k  # on suppose que l'élément minimum se trouve à l'indice k
        for i in range(k+1, N):
            if tab[i] < tab[imin]:
                imin = i
        echange(tab, k, imin)
```

## Sujet 02

### Exercice 1 : Correspondance d’un mot à trous

**Énoncé :**
Écrire la fonction correspond(mot, mot_a_trous) qui renvoie True si le mot peut être obtenu en remplaçant les '*' de mot_a_trous par les lettres appropriées, et False sinon.

```python
def correspond(mot, mot_a_trous):
    # les deux chaînes doivent avoir la même longueur
    if len(mot) != len(mot_a_trous):
        return False
    for i in range(len(mot)):
        # si le caractère du motif n'est pas '*' et qu'il diffère du caractère correspondant dans mot
        if mot_a_trous[i] != '*' and mot[i] != mot_a_trous[i]:
            return False
    return True
```

**Explication :**
On vérifie d'abord que les deux chaînes ont la même longueur. Puis, pour chaque position, si le caractère dans mot_a_trous n'est pas un joker ('*'), il doit être identique au caractère correspondant dans mot.

### Exercice 2 : Plan d'envoi cyclique

**Énoncé :**
On représente un plan d’envoi par un dictionnaire (exemple : {'A':'E', 'B':'F', ...}). Un plan est cyclique si, en partant de 'A' et en suivant les destinataires, on parcourt toutes les personnes avant de revenir à 'A'.

```python
def est_cyclique(plan):
    expediteur_initial = 'A'
    destinataire = plan[expediteur_initial]
    nb_destinataires = 1
    # on suit la chaîne d'envoi jusqu'à revenir à 'A'
    while destinataire != expediteur_initial:
        destinataire = plan[destinataire]
        nb_destinataires += 1
    return nb_destinataires == len(plan)
```

**Explication :**
On part de 'A' et on suit la chaîne d'envois en comptant le nombre de personnes visitées. Si ce nombre est égal au nombre total de personnes dans le plan, le plan est cyclique.

## Sujet 03

### Exercice 1 : Max d'une table

**Énoncé :**
Écrire la fonction maximum_tableau(tab) qui renvoie le max.

```python

def maximum_tableau(tab):
    max_val = tab[0]
    for x in tab[1:]:
        if x > max_val:
            max_val = x
    return max_val
```

**Explication :**
On parcourt la liste en mettant à jour le maximum dès qu’un élément supérieur est trouvé.

### Exercice 2 : Vérification d'un parenthésage

**Énoncé :**
Compléter la fonction bon_parenthesage(ch) qui renvoie True si la chaîne de parenthèses est correctement parenthésée, False sinon. On utilisera une pile.


```python

class Pile:
    def __init__(self):
        self.contenu = []
    def est_vide(self):
        return self.contenu == []
    def empiler(self, v):
        self.contenu.append(v)
    def depiler(self):
        assert not self.est_vide(), "Pile vide!"
        return self.contenu.pop()

def bon_parenthesage(ch):
    pile = Pile()
    for car in ch:
        if car == '(':
            pile.empiler(car)
        elif car == ')':
            if pile.est_vide():
                return False
            pile.depiler()
    return pile.est_vide()
```

**Explication :**
Pour chaque '(' on empile, et pour chaque ')' on dépile. La chaîne est bien parenthésée si la pile est vide à la fin.

## Sujet 04

### Exercice 1 : Recherche de la dernière occurrence

**Énoncé :**
Écrire la fonction recherche(tab, n) qui renvoie l’indice de la dernière occurrence de n dans la liste tab, ou None si n n’y apparaît pas.

```python

def recherche(tab, n):
    indice_derniere = None
    for i in range(len(tab)):
        if tab[i] == n:
            indice_derniere = i
    return indice_derniere
```

**Explication :**
On parcourt le tableau et on met à jour l’indice à chaque fois que n est trouvé. Ainsi, à la fin, l’indice stocké est celui de la dernière occurrence.

### Exercice 2 : Point le plus proche

**Énoncé :**
On dispose d’un tableau de points (tuples d’entiers) et d’un point de départ. La fonction point_le_plus_proche(depart, tab) renvoie le point du tableau le plus proche du point de départ en termes de distance au carré.

```python

def distance_carre(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (x1 - x2)**2 + (y1 - y2)**2

def point_le_plus_proche(depart, tab):
    min_point = tab[0]
    min_dist = distance_carre(depart, min_point)
    for i in range(1, len(tab)):
        d = distance_carre(depart, tab[i])
        if d < min_dist:
            min_dist = d
            min_point = tab[i]
    return min_point
```

**Explication :**
On calcule la distance au carré pour chaque point du tableau et on garde celui dont la distance est minimale.

## Sujet 05

### Exercice 1 : Maximum et indice

**Énoncé :**
Écrire la fonction max_et_indice(tab) qui renvoie un tuple contenant la valeur maximale d’une liste d’entiers et l’indice de sa première apparition.

```python

def max_et_indice(tab):
    max_val = tab[0]
    max_index = 0
    for i in range(1, len(tab)):
        if tab[i] > max_val:
            max_val = tab[i]
            max_index = i
    return (max_val, max_index)
```

**Explication :**
On parcourt la liste en mettant à jour le maximum et son indice dès qu’un élément supérieur est trouvé.

### Exercice 2 : Ordre de gènes et points de rupture

**Énoncé :**
On considère un tableau ordre qui est une permutation des entiers de 1 à n.

La fonction est_un_ordre(tab) vérifie que le tableau contient bien tous les entiers de 1 à n.
La fonction nombre_points_rupture(ordre) renvoie le nombre de points de rupture selon les règles données.

```python

def est_un_ordre(tab):
    n = len(tab)
    vus = []
    for x in tab:
        if x < 1 or x > n or x in vus:
            return False
        vus.append(x)
    return True

def nombre_points_rupture(ordre):
    assert est_un_ordre(ordre), "ordre n'est pas une permutation valide"
    n = len(ordre)
    nb = 0
    if ordre[0] != 1:
        nb += 1
    if ordre[-1] != n:
        nb += 1
    for i in range(n-1):
        diff = ordre[i+1] - ordre[i]
        if diff != 1 and diff != -1:
            nb += 1
    return nb
```

**Explication :**
est_un_ordre s’assure que chaque entier de 1 à n apparaît exactement une fois.
nombre_points_rupture compte un point de rupture si le premier élément n’est pas 1, si le dernier n’est pas n et si deux éléments consécutifs ne se suivent pas (écart différent de 1 ou -1).

## Sujet 06

### Exercice 1 : Vérification de l'ordre croissant

**Énoncé :**
Écrire la fonction verifie(tab) qui renvoie True si la liste est triée en ordre croissant, False sinon.
Un tableau vide ou à un seul élément est considéré comme trié.

```python

def verifie(tab):
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            return False
    return True
```

**Explication :**
On compare chaque élément à celui qui le suit. Si un élément est supérieur à son successeur, l'ordre croissant est violé.

### Exercice 2 : Vote et détermination du gagnant

**Énoncé :**
Écrire deux fonctions :

depouille(urne) qui renvoie un dictionnaire comptant le nombre de voix pour chaque candidat à partir d'une liste de suffrages.
vainqueurs(election) qui renvoie la liste des candidats ayant obtenu le maximum de voix.
Solution :

```python

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] += 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueurs(election):
    nmax = 0
    liste_finale = []
    for candidat, voix in election.items():
        if voix == nmax:
            liste_finale.append(candidat)
        elif voix > nmax:
            nmax = voix
            liste_finale = [candidat]
    return liste_finale
```

**Explication :**
depouille parcourt la liste des votes et construit un dictionnaire de comptage.
vainqueurs parcourt ce dictionnaire pour déterminer le ou les candidats ayant obtenu le plus grand nombre de voix.

## Sujet 07

### Exercice 1 : Conversion d'une liste de booléens en entier

**Énoncé :**
Écrire la fonction gb_vers_entier(tab) qui convertit une liste de booléens (représentation big-endian) en un entier.

```python

def gb_vers_entier(tab):
    entier = 0
    n = len(tab)
    for i, bit in enumerate(tab):
        if bit:
            entier += 2 ** (n - 1 - i)
    return entier
```

**Explication :**
Chaque bit True ajoute 2^(n-1-i) à la somme, où n est la taille de la liste et i l’indice du bit.

### Exercice 2 : Tri par insertion

**Énoncé :**
Compléter la fonction tri_insertion(tab) qui trie la liste en insérant successivement chaque élément dans la partie déjà triée.

```python

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        j = i
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = valeur_insertion
```

**Explication :**
Pour chaque élément à partir du second, on le déplace vers la gauche dans la partie triée jusqu'à trouver sa place.

## Sujet 08

### Exercice 1 : Codage par différence (delta encoding)

**Énoncé :**
Écrire la fonction delta(tab) qui renvoie un tableau où le premier élément reste inchangé et chaque autre élément est remplacé par la différence avec le précédent.

```python

def delta(tab):
    if tab == []:
        return []
    resultat = [tab[0]]
    for i in range(1, len(tab)):
        resultat.append(tab[i] - tab[i-1])
    return resultat
```

**Explication :**
Le premier élément est conservé, et pour chaque position i (à partir de 1), on calcule la différence entre tab[i] et tab[i-1].

### Exercice 2 : Expression arithmétique infixée

**Énoncé :**
Compléter la méthode infixe de la classe Expr qui renvoie la représentation infixe (avec parenthèses) d'une expression arithmétique représentée par un arbre binaire.

```python

def infixe(self):
    if self.est_une_feuille():
        return str(self.valeur)
    partie_gauche = self.gauche.infixe()
    partie_droite = self.droite.infixe()
    return "(" + partie_gauche + str(self.valeur) + partie_droite + ")"
```

**Explication :**
Si le nœud est une feuille, on retourne sa valeur. Sinon, on renvoie la chaîne composée de la représentation infixe du sous-arbre gauche, de la valeur du nœud, puis du sous-arbre droit, le tout encadré de parenthèses.

## Sujet 09

### Exercice 1 : Tri des notes par effectif

**Énoncé :**
À partir d’une liste de notes entières (entre 0 et 10), écrire :

effectif_notes(notes_eval) qui renvoie une liste de longueur 11 contenant le nombre d’occurrences de chaque note.
notes_triees(eff) qui renvoie la liste des notes triées.
Solution :

```python

def effectif_notes(notes_eval):
    eff = [0] * 11
    for note in notes_eval:
        eff[note] += 1
    return eff

def notes_triees(eff):
    resultat = []
    for note, count in enumerate(eff):
        resultat += [note] * count
    return resultat
```

**Explication :**
On compte le nombre d’occurrences de chaque note puis on reconstruit la liste triée en ajoutant chaque note le nombre de fois qu’elle apparaît.

### Exercice 2 : Conversion binaire/décimale récursive

**Énoncé :**
Écrire deux fonctions récursives :

dec_to_bin(nb_dec) qui convertit un entier décimal en chaîne binaire.
bin_to_dec(nb_bin) qui convertit une chaîne binaire en entier décimal.
Solution :

```python

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        return 0 if nb_bin == '0' else 1
    else:
        dernier_bit = 0 if nb_bin[-1] == '0' else 1
        return bin_to_dec(nb_bin[:-1]) * 2 + dernier_bit
```

**Explication :**
Pour dec_to_bin, on divise récursivement par 2 en accumulant le reste. Pour bin_to_dec, on traite la chaîne en retirant le dernier caractère et en multipliant par 2.

### Sujet 10
Exercice 1 : Moyenne pondérée
Énoncé :
Écrire la fonction moyenne(notes) qui calcule la moyenne pondérée d’une liste de tuples (note, coefficient). Si la somme des coefficients est nulle, renvoyer None.

Solution :

python
Toujours afficher les détails

Copier
def moyenne(notes):
    somme_coeff = 0
    somme_ponderee = 0.0
    for note, coeff in notes:
        somme_ponderee += note * coeff
        somme_coeff += coeff
    if somme_coeff == 0:
        return None
    return somme_ponderee / somme_coeff
Explication :
On multiplie chaque note par son coefficient, on somme le tout et on divise par la somme des coefficients. Si cette somme est nulle, on renvoie None.

Exercice 2 : Jeu du Plus ou Moins
Énoncé :
Compléter la fonction plus_ou_moins() qui génère un nombre mystère entre 1 et 99 et permet à l’utilisateur de deviner ce nombre en 10 essais ou moins, en indiquant "Trop petit" ou "Trop grand" à chaque proposition.

Solution :

python
Toujours afficher les détails

Copier
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1
    while nb_mystere != nb_test and compteur < 10:
        if nb_test < nb_mystere:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))
        compteur += 1
    if nb_mystere == nb_test:
        print("Gagné ! Le nombre était", nb_mystere, "trouvé en", compteur, "essais.")
    else:
        print("Perdu... Le nombre mystère était", nb_mystere)
Explication :
On génère un nombre aléatoire et on lit successivement les propositions de l’utilisateur, en donnant un indice à chaque essai. Le jeu s’arrête dès que le nombre mystère est trouvé ou après 10 essais.

Sujet 11
Exercice 1 : Nombre de mots dans une phrase
Énoncé :
Écrire la fonction nombre_de_mots(phrase) qui renvoie le nombre de mots dans une phrase, sachant que les mots sont séparés par un espace.

Solution :

python
Toujours afficher les détails

Copier
def nombre_de_mots(phrase):
    nb_espaces = phrase.count(' ')
    if phrase.endswith(' !') or phrase.endswith(' ?'):
        nb_espaces -= 1
    return nb_espaces + 1 if phrase != "" else 0
Explication :
Le nombre de mots est égal au nombre d’espaces plus 1, en ajustant le cas particulier où la ponctuation finale est précédée d’un espace.

Exercice 2 : Insertion dans un arbre binaire de recherche
Énoncé :
Compléter la méthode inserer(self, cle) de la classe Noeud pour insérer une clé dans un arbre binaire de recherche sans doublon.

Solution :

python
Toujours afficher les détails

Copier
class Noeud:
    def __init__(self, etiquette):
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        if cle < self.etiquette:
            if self.gauche is not None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        elif cle > self.etiquette:
            if self.droit is not None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)
        # si cle == self.etiquette, ne rien faire (pas de doublons)
Explication :
On compare cle à la valeur du nœud courant. Si elle est inférieure, on l’insère dans le sous-arbre gauche (création si nécessaire) ; si elle est supérieure, dans le sous-arbre droit. Aucun traitement n’est fait si la clé existe déjà.

Sujet 12
Exercice 1 : Tri par sélection (version complète)
Énoncé :
Écrire la fonction tri_selection(tab) qui trie la liste par ordre croissant en place.

Solution :

python
Toujours afficher les détails

Copier
def tri_selection(tab):
    N = len(tab)
    for k in range(0, N-1):
        imin = k
        for i in range(k+1, N):
            if tab[i] < tab[imin]:
                imin = i
        tab[k], tab[imin] = tab[imin], tab[k]
Explication :
Même principe que dans Sujet 01. On parcourt la liste et on échange à chaque itération le plus petit élément avec celui en position k.

Exercice 2 : Jeu du Plus ou Moins (version reprise)
Énoncé :
Compléter la fonction plus_ou_moins() pour le jeu de devinette.

Solution :
(Voir Sujet 10, Exercice 2 – le même code est applicable.)

Sujet 13
Exercice 1 : Recherche de la première occurrence
Énoncé :
Écrire la fonction recherche(elt, tab) qui renvoie l’indice de la première occurrence de elt dans tab, ou None si absent.

Solution :

python
Toujours afficher les détails

Copier
def recherche(elt, tab):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return None
Explication :
On parcourt la liste du début et on retourne dès qu’on trouve l’élément recherché.

Exercice 2 : Insertion dans un tableau trié
Énoncé :
Compléter la fonction insere(tab, a) qui insère l’entier a dans une liste triée tab de manière à conserver l’ordre.

Solution :

python
Toujours afficher les détails

Copier
def insere(tab, a):
    tab_a = [a] + tab[:]  # création d'une copie avec a en tête
    i = 0
    while i < len(tab) and a > tab[i]:
        tab_a[i] = tab[i]
        tab_a[i+1] = a
        i += 1
    return tab_a
Explication :
On insère a en tête, puis on décale les éléments jusqu’à trouver la position correcte pour que la nouvelle liste reste triée.

Sujet 14
Exercice 1 : Minimum et maximum d’un tableau
Énoncé :
Écrire la fonction min_et_max(tab) qui renvoie un dictionnaire avec les clés 'min' et 'max'.

Solution :

python
Toujours afficher les détails

Copier
def min_et_max(tab):
    min_val = tab[0]
    max_val = tab[0]
    for x in tab[1:]:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return {'min': min_val, 'max': max_val}
Explication :
On parcourt la liste pour déterminer les valeurs minimale et maximale et on les renvoie dans un dictionnaire.

Exercice 2 : Paquet de cartes
Énoncé :
Compléter la classe Paquet_de_cartes qui doit initialiser un paquet de 52 cartes (ordonnées par couleur et valeur) et la méthode recuperer_carte(pos) qui renvoie la carte à la position pos après avoir vérifié que l’indice est valide.

Solution :

python
Toujours afficher les détails

Copier
class Carte:
    def __init__(self, c, v):
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self):
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def recuperer_couleur(self):
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        self.contenu = []
        for c in range(1, 5):      # 1: pique, 2: coeur, 3: carreau, 4: trèfle
            for v in range(1, 14): # valeurs de 1 à 13
                self.contenu.append(Carte(c, v))

    def recuperer_carte(self, pos):
        assert 0 <= pos < len(self.contenu), "paramètre pos invalide"
        return self.contenu.pop(pos)
Explication :
Le constructeur crée la liste de 52 cartes. La méthode recuperer_carte vérifie que l’indice est valide grâce à une assertion avant de retirer et renvoyer la carte.

Sujet 15
Exercice 1 : Moyenne arithmétique
Énoncé :
Écrire la fonction moyenne(notes) qui renvoie la moyenne simple des nombres d'une liste non vide de flottants.

Solution :

python
Toujours afficher les détails

Copier
def moyenne(notes):
    total = 0.0
    for x in notes:
        total += x
    return total / len(notes)
Explication :
On calcule la somme des éléments puis on divise par le nombre d’éléments.

Exercice 2 : Conversion en binaire
Énoncé :
Compléter la fonction binaire(a) qui convertit un entier en sa représentation binaire sous forme de chaîne.

Solution :

python
Toujours afficher les détails

Copier
def binaire(a):
    if a == 0:
        return '0'
    bin_a = ''
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a
Explication :
On utilise la méthode des divisions successives pour construire la chaîne binaire.

Sujet 16
Exercice 1 : Écriture binaire d’un entier positif
Énoncé :
Écrire la fonction ecriture_binaire_entier_positif(n) qui renvoie la représentation binaire de n sous forme de chaîne, sans utiliser la fonction bin.

Solution :

python
Toujours afficher les détails

Copier
def ecriture_binaire_entier_positif(n):
    if n == 0:
        return '0'
    resultat = ''
    while n > 0:
        resultat = str(n % 2) + resultat
        n = n // 2
    return resultat
Explication :
Même principe que précédemment, on construit la chaîne binaire en préfixant les bits calculés.

Exercice 2 : Tri à bulles
Énoncé :
Compléter la fonction tri_bulles(tab) qui trie la liste en place en utilisant l’algorithme du tri à bulles.

Solution :

python
Toujours afficher les détails

Copier
def echange(tab, i, j):
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_bulles(tab):
    n = len(tab)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if tab[j] > tab[j+1]:
                echange(tab, j, j+1)
Explication :
À chaque passe, le plus grand élément "bulle" jusqu’à la fin du tableau. On répète sur la partie non triée.

Sujet 17
Exercice 1 : Nombre de répétitions
Énoncé :
Écrire la fonction nb_repetitions(elt, tab) qui renvoie le nombre de fois que elt apparaît dans la liste tab.

Solution :

python
Toujours afficher les détails

Copier
def nb_repetitions(elt, tab):
    count = 0
    for x in tab:
        if x == elt:
            count += 1
    return count
Explication :
On incrémente un compteur pour chaque occurrence de l’élément.

Exercice 2 : Conversion en binaire (version reprise)
Énoncé :
Compléter la fonction binaire(a) pour convertir un entier positif en binaire.

Solution :
(Voir Sujet 15, Exercice 2 – même code.)

Sujet 18
Exercice 1 : Multiplication sans utiliser '*' ou '//'
Énoncé :
Écrire la fonction multiplication(n1, n2) qui renvoie le produit de deux nombres entiers en n'utilisant que l'addition et la soustraction.

Solution :

python
Toujours afficher les détails

Copier
def multiplication(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    negatif = False
    if n1 < 0:
        n1 = -n1
        negatif = not negatif
    if n2 < 0:
        n2 = -n2
        negatif = not negatif
    resultat = 0
    for i in range(n2):
        resultat += n1
    return -resultat if negatif else resultat
Explication :
On détermine le signe du résultat, puis on ajoute n1 à lui-même n2 fois.

Exercice 2 : Recherche dichotomique
Énoncé :
Compléter la fonction récursive chercher(tab, x, i, j) qui renvoie l'indice de x dans tab (trié), ou None si x n’est pas présent.

Solution :

python
Toujours afficher les détails

Copier
def chercher(tab, x, i, j):
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x:
        return chercher(tab, x, m+1, j)
    elif tab[m] > x:
        return chercher(tab, x, i, m-1)
    else:
        return m
Explication :
C’est l’algorithme classique de recherche dichotomique, en divisant le tableau en deux à chaque appel récursif.

Sujet 19
Exercice 1 : Liste des puissances
Énoncé :
Écrire la fonction liste_puissances(a, n) qui renvoie la liste des puissances de a de a¹ à aⁿ sans utiliser l'opérateur ** ni pow.
Écrire aussi liste_puissances_borne(a, borne) qui renvoie les puissances de a (à partir de a¹) strictement inférieures à borne.

Solution :

python
Toujours afficher les détails

Copier
def liste_puissances(a, n):
    """Renvoie la liste [a, a², ..., aⁿ] sans utiliser ** ou pow."""
    resultat = []
    current = a
    for i in range(n):
        resultat.append(current)
        current = current * a
    return resultat

def liste_puissances_borne(a, borne):
    """Renvoie la liste des puissances de a (à partir de a¹) strictement inférieures à borne."""
    resultat = []
    current = a
    while current < borne:
        resultat.append(current)
        current = current * a
    return resultat
Explication :
On utilise une variable current initialisée à a et on la multiplie par a à chaque itération pour obtenir la puissance suivante.

Exercice 2 : Code parfait d'un mot
Énoncé :
À l’aide d’un dictionnaire qui associe à chaque lettre son code, écrire la fonction codes_parfait(mot) qui renvoie un triplet (code_additionne, code_concatene, mot_est_parfait)
où :

code_additionne est la somme des codes des lettres du mot
code_concatene est la concaténation des codes (convertie en entier)
mot_est_parfait est un booléen indiquant si code_additionne divise code_concatene.
Solution :

python
Toujours afficher les détails

Copier
dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}

def codes_parfait(mot):
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code = dico[c]
        code_concatene += str(code)
        code_additionne += code
    code_concatene_int = int(code_concatene)
    mot_est_parfait = (code_concatene_int % code_additionne == 0) if code_additionne != 0 else False
    return code_additionne, code_concatene_int, mot_est_parfait
Explication :
Pour chaque lettre du mot, on ajoute son code à la chaîne et à la somme. On teste ensuite si la somme divise le nombre formé par la concaténation.

Sujet 20
Exercice 1 : Lancer de dés et vérification de la paire de 6
Énoncé :

Écrire la fonction lancer(n) qui renvoie une liste de n entiers aléatoires entre 1 et 6.
Écrire la fonction paire_6(tab) qui renvoie True si le nombre de 6 dans tab est supérieur ou égal à 2, sinon False.
Solution :

python
Toujours afficher les détails

Copier
from random import randint

def lancer(n):
    """Renvoie une liste de n entiers aléatoires entre 1 et 6."""
    resultat = []
    for i in range(n):
        resultat.append(randint(1, 6))
    return resultat

def paire_6(tab):
    """Renvoie True si le nombre de 6 dans tab est au moins 2, sinon False."""
    count = 0
    for x in tab:
        if x == 6:
            count += 1
    return count >= 2
Explication :
La fonction lancer utilise randint pour générer des entiers aléatoires compris entre 1 et 6.
La fonction paire_6 compte les 6 dans la liste et vérifie si ce nombre est supérieur ou égal à 2.

Exercice 2 : Conversion en binaire (version itérative)
Énoncé :
Compléter la fonction binaire(a) qui convertit un entier en sa représentation binaire sous forme de chaîne.

Solution :

python
Toujours afficher les détails

Copier
def binaire(a):
    """Convertit l'entier a en sa représentation binaire (chaine de caractères)."""
    if a == 0:
        return '0'
    bin_a = ''
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a
Explication :
On utilise la méthode des divisions successives pour construire la chaîne binaire en préfixant le reste obtenu à chaque division.
