#  Poo: Exercice 

## Exercice 1 - Un rat de bibliothèque


### Exercice 1.1 :

- Instancier un nouveau livre `mon_livre_favori` et afficher ensuite son titre.

```python

# Définition de la classe Livre
class Livre:  
    def __init__(self, un_titre, un_auteur, une_année, une_langue): 
        self.titre  = un_titre 
        self.auteur = un_auteur
        self.année  = une_année
        self.langue = une_langue

        
# Instanciation de plusieurs objets de classe Livre 
livre1 = Livre("L'Étranger", "Albert Camus", 1942, "Fr")
livre2 = Livre("Martin Eden", "Jack London", 1909, "En")
livre3 = Livre("Les Frères Karamazov", "Fiodor Dostoïevski", 1880, "Ru") 
```

### Exercice 1.2:

- Le professeur documentaliste souhaite que vos livres prennent en compte la langue originale d'écriture. Modifiez donc la classe Livre pour inclure un nouvel attribut appelé langue_originale. Ensuite, mettez à jour l'instantiation des quatre livres précédemment créés pour inclure également l'information sur la langue originale.

```python
mon_livre_favori = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, "Fr")

print(mon_livre_favori.titre)
>>> Le Petit Prince
```
### Exercice 1.3

- Écrire une fonction `plus_ancien(livre1, livre2)` qui renvoie le titre du livre ayant été publié en premier parmi les deux livres passés en argument.

```python
def plus_ancien(livre1, livre2):
    if livre1.année < livre2.année:
        return livre1.titre
    else:
        return livre2.titre

livre1 = Livre("L'Étranger", "Albert Camus", 1942, "Fr")
livre2 = Livre("Martin Eden", "Jack London", 1909, "En")
livre3 = Livre("Les Frères Karamazov", "Fiodor Dostoïevski", 1880, "Ru")

print(plus_ancien(livre1, livre3))

>>> Les Frères Karamazov
```

## Exercice 2 - Classe et salle de classe

### Exercice 2.1

- Écrire une classe Eleve contenant les attributs `nom`, `classe` et `moyenne`.

```python
# Définition de la classe Eleve
class Eleve:
    def __init__(self, nom, classe, moyenne):
        self.nom = nom      # Nom de l'élève
        self.classe = classe  # Classe de l'élève (ex: 5ème, 1ère, etc.)
        self.moyenne = moyenne  # Moyenne de l'élève
```

### Exercice 2.2

- Instancier trois élèves de cette classe de NSI.

```python
eleve1 = Eleve("Romain Boutolleau", "5ème", 15.96)
eleve2 = Eleve("Aymeric Petit", "1ère", 12.0)
eleve3 = Eleve("Jean Avril", "1T",18)

print(f"Nom: {eleve1.nom}, Classe: {eleve1.classe}, Moyenne: {eleve1.moyenne}")
print(f"Nom: {eleve2.nom}, Classe: {eleve2.classe}, Moyenne: {eleve2.moyenne}")
print(f"Nom: {eleve3.nom}, Classe: {eleve3.classe}, Moyenne: {eleve3.moyenne}")

>>> Nom: Romain Boutolleau, Classe: 5ème, Moyenne: 15.96
>>> Nom: Aymeric Petit, Classe: 1ère, Moyenne: 12.0
>>> Nom: Jean Avril, Classe: 1T, Moyenne: 18
```

### Exercice 2.3

- Écrire une fonction `chouchou(eleve1, eleve2)` qui renvoie le nom de l'élève ayant la meilleure moyenne.

```python
# Fonction pour déterminer l'élève avec la meilleure moyenne
def chouchou(eleve1, eleve2):
    if eleve1.moyenne > eleve2.moyenne:
        return eleve1.nom
    else:
        return eleve2.nom

print(chouchou(eleve1,eleve2))

>>> Romain Boutolleau
```

## Exercice 3 - Un constructeur plus original

### Exercice 3

- Écrire une classe `TriangleRectangle` qui contiendra les attributs cote1, cote2 et hypotenuse. Cependant, le constructeur ne prendra en paramètres que cote1 et cote2, l'attribut hypotenuse se calculera automatiquement.

```python
import math

class TriangleRectangle:
    def __init__(self, cote1, cote2):
        self.cote1 = cote1  # Premier côté
        self.cote2 = cote2  # Deuxième côté
        self.hypotenuse = math.sqrt(cote1 ** 2 + cote2 ** 2)  # Calcul de l'hypoténuse

        
mon_triangle = TriangleRectangle(3, 4)

# Affichage
print(mon_triangle.cote1)     
print(mon_triangle.cote2)
print(mon_triangle.hypotenuse)
>>> 3
>>> 4
>>> 5.0
```

## Exercice 4 - Ça ne manque pas d'aire !

### Exercice 4.1

- Créer une fonction `calculer_périmètre(rectangle)` externe qui renvoie le périmètre du rectangle donné en argument.

```python
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur  = largeur
        
    def calculer_aire(self):
        return self.longueur * self.largeur

# Création d'objets de la classe Rectangle
rect1 = Rectangle(5, 3)
rect2 = Rectangle(7, 4)
```

### Exercice 4.2

- Transformer cette fonction en une méthode de la classe Rectangle.

```python
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        
    def calculer_aire(self):
        return self.longueur * self.largeur
    
    def calculer_perimetre(self):
        return 2 * (self.longueur + self.largeur)  # Formule du périmètre

    
rect1 = Rectangle(5, 3)
rect2 = Rectangle(7, 4)


print(rect1.calculer_perimetre())
print(rect2.calculer_perimetre()) 

>>> 16
>>> 22
```

### Exercice 4.3

- Au sein du même script où est définit la classe `Rectangle`, définir une nouvelle classe Cercle. On souhaite une fonction ou une méthode qui permet de calculer aussi l'aire pour les instances de Cercle.

```python
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        
    def calculer_aire(self):
        return math.pi * (self.rayon ** 2)  # Formule de l'aire

    def calculer_circonference(self):
        return 2 * math.pi * self.rayon  # Formule de la circonférence


rect1 = Rectangle(5, 3)
rect2 = Rectangle(7, 4)
```

## Exercice 5 - Vroum Vroum

### Exercice 5

  1. Écrire une classe Voiture qui contiendra les attributs kilometrage, consommation (nombre de litres de carburant consommé pour 100 kilomètres) dont les valeurs seront données comme arguments à l'initialisation et un dernier attribut carburant valant 0 par défaut.

  2. Doter la classe d'une méthode affiche qui affiche le kilométrage et le carburant disponible.

  3. Doter la classe d'une méthode remplir qui prend en argument un entier correspondant au volume de carburant à ajouter au réservoir.

  4. Doter la classe d'une méthode avance qui prend en argument un entier correspondant au nombre de kilomètres parcourus et qui actualise les valeurs des attributs kilometrage et consommation.

```python
class Voiture:
    def __init__(self, kilometrage, consommation):
        self.kilometrage = kilometrage  
        self.consommation = consommation  
        self.carburant = 0 

    def affiche(self):
        """Affiche le kilométrage et le carburant disponible."""
        print(f"La voiture a parcouru {self.kilometrage} kilomètres et il y a {self.carburant} litres d'essence dans le réservoir.")

    def remplir(self, volume):
        """Ajoute un volume de carburant au réservoir."""
        self.carburant += volume

    def avance(self, distance):
        """Fait avancer la voiture sur une distance donnée, en ajustant le kilométrage et le carburant."""
        # Calcul de la conso
        carburant_necessaire = (self.consommation / 100) * distance
        
        if carburant_necessaire <= self.carburant:
            self.kilometrage += distance  # Mise à jour du kilométrage
            self.carburant -= carburant_necessaire  # Mise à jour du carburant
        else:
            print("Pas assez de carburant pour parcourir cette distance.")

            
vega_myssil = Voiture(0, 8)
vega_myssil.affiche()  # Affiche le km et le carburant
vega_myssil.remplir(25)  # Remplit le réservoir
vega_myssil.avance(200)  # Avance de 200 km
vega_myssil.affiche()  # Affiche le nouveau kilométrage et le carbu restant

>>> La voiture a parcouru 0 kilomètres et il y a 0 litres d'essence dans le réservoir.
>>> La voiture a parcouru 200 kilomètres et il y a 9.0 litres d'essence dans le réservoir.
```

## Exercice 6 - Tic Tac

### Exercice 6

 1. Écrire une classe Horloge qui contiendra les attributs heures, minutes et secondes.

 2. Doter la classe d'une méthode affiche(self) qui affiche le temps de l'instance self.

 3. Doter la classe d'une méthode avance(self, s) qui avance le temps de s secondes de l'instance self.

```python
class Horloge:
    def __init__(self, heures, minutes, secondes):
        self.heures = heures  # Heures de l'horloge
        self.minutes = minutes  # Minutes de l'horloge
        self.secondes = secondes  # Secondes de l'horloge

    def affiche(self):
        """Affiche l'heure actuelle au format 'Il est hh heures, mm minutes et ss secondes.'"""
        print(f"Il est {self.heures} heures, {self.minutes} minutes et {self.secondes} secondes.")

    def avance(self, s):
        """Avance l'horloge de s secondes."""
        total_secondes = self.heures * 3600 + self.minutes * 60 + self.secondes + s
        total_secondes %= 86400  # Nombre de secondes en une journée

        self.heures = total_secondes // 3600
        self.minutes = (total_secondes % 3600) // 60
        self.secondes = total_secondes % 60

        
h = Horloge(17, 25, 38)
print(h.heures)    # Affiche 17
print(h.minutes)   # Affiche 25
print(h.secondes)  # Affiche 38
h.affiche()        # Affiche l'heure
h.avance(27)      # Avance de 27 secondes
h.affiche()        # Affiche l'heure mise à jour
>>> 17
>>> 25
>>> 38
>>> Il est 17 heures, 25 minutes et 38 secondes.
>>> Il est 17 heures, 26 minutes et 5 secondes.
```

## Exercice 7 - Un début de jeu vidéo

### Exercice 7

- Écrire une classe Player qui :
  - ne prendra aucun argument lors de l'instanciation.
  - affectera à chaque objet créé un attribut energie valant 3 par défaut.
  - affectera à chaque objet créé un attribut alive valant True par défaut.
  - fournira à chaque objet une méthode blessure() qui diminue l'attribut energie de 1.
  - fournira à chaque objet une méthode soin() qui augmente l'attribut energie de 1.
  - si l'attribut energie passe à 0, l'attribut alive doit passer à False et ne doit plus pouvoir évoluer.

```python

class Player:
    def __init__(self):
        self.energie = 3  # Énergie initiale
        self.alive = True  # État du joueur, vivant par défaut

    def blessure(self):
        """Diminue l'énergie de 1. Si l'énergie atteint 0, le joueur meurt."""
        if self.alive:  # Vérifie si le joueur est encore vivant
            self.energie -= 1
            if self.energie <= 0:
                self.energie = 0  # S'assurer que l'énergie ne descend pas en dessous de 0
                self.alive = False  # Le joueur est maintenant mort

    def soin(self):
        """Augmente l'énergie de 1, mais ne change pas l'état vivant."""
        if self.alive:  # Vérifie si le joueur est encore vivant
            self.energie += 1

# Exemple d'utilisation
mario = Player()
print(mario.energie)  
mario.soin()
print(mario.energie) 
mario.blessure()
mario.blessure()
mario.blessure()
print(mario.alive)    
mario.blessure()
print(mario.alive)    
mario.soin()
print(mario.alive)
print(mario.energie) 

>>> 3
>>> 4
>>> True
>>> False
>>> False
>>> 0
  ```

## Exercice 8 - Un stage chez la Société Générale

### Exercice 8

- Définir une classe CompteBancaire dont le constructeur recevra en paramètres :

  1. Un attribut titulaire stockant le nom du propriétaire.
  2. Un attribut solde contenant le solde disponible sur le compte.
  3. Cette classe contiendra deux méthodes retrait et depot qui permettront de retirer ou de déposer de l'argent sur le compte.

```python
class CompteBancaire:
    def __init__(self, titulaire, solde_initial):
        self.titulaire = titulaire  # Nom du titulaire du compte
        self.solde = solde_initial   # Solde initial du compte

    def retrait(self, montant):
        """Permet de retirer de l'argent du compte si le solde le permet."""
        if montant <= self.solde:
            self.solde -= montant
            print(f"Vous avez retiré {montant} euros")
            print(f"Solde actuel du compte : {self.solde} euros")
        else:
            print("Retrait impossible")

    def depot(self, montant):
        """Permet de déposer de l'argent sur le compte."""
        self.solde += montant
        print(f"Vous avez déposé {montant} euros")
        print(f"Solde actuel du compte : {self.solde} euros")

# Use
mon_compte = CompteBancaire("A. Rouquan", 1000)
mon_compte.retrait(50)         
mon_compte.retrait(40000)      
mon_compte.depot(10000000)

>>> Vous avez retiré 50 euros
>>> Solde actuel du compte : 950 euros
>>> Retrait impossible
>>> Vous avez déposé 10000000 euros
>>> Solde actuel du compte : 10000950 euros
```

## Exercice 9 - Des dès

### Énoncé

- On souhaite construire une base d'objets servant à créer des jeux utilisant des dés.

- Un dé possède un nombre de faces, ainsi qu'une valeur (la face supérieure du dé une fois qu'on l'a lancé, et la valeur -1 s'il n'a pas encore été lancé). On doit pouvoir lancer le dé, c'est-à-dire lui attribuer une valeur aléatoire entre 1 et son nombre de faces.

- Un jeu de dés est un ensemble de dés. On doit pouvoir lancer tous les dés (en une fois), faire la somme des valeurs des dés, et on souhaite afficher la valeur des dés ainsi que leur somme.

### Question 9.1

- Déterminer les attributs et méthodes pour deux classes représentant ce problème : une classe Jeu et une classe Dé.

```python
import random

class De:
    def __init__(self, faces):
        self.faces = faces 
        self.valeur = -1     # Valeur initiale, -1 signifie qu'il n'a pas été lancé

    def lancer(self):
        """Lance le dé et attribue une valeur aléatoire entre 1 et le nombre de faces."""
        self.valeur = random.randint(1, self.faces)

class Jeu:
    def __init__(self, nombre_de_de, faces):
        self.des = [De(faces) for _ in range(nombre_de_de)]  # Création d'une liste de dés

    def lancer(self):
        """Lance tous les dés du jeu."""
        for de in self.des:
            de.lancer()

    def somme(self):
        """Calcule la somme des valeurs des dés."""
        return sum(de.valeur for de in self.des)

    def afficher(self):
        """Affiche la valeur des dés et leur somme."""
        if all(de.valeur == -1 for de in self.des):
            print("Les dés n'ont pas été lancés !")
        else:
            valeurs = [de.valeur for de in self.des]
            print(f"Les dés valent {', '.join(map(str, valeurs))} et leur somme vaut {self.somme()}.")

            
j = Jeu(3, 6)  
j.afficher()   
j.lancer()    
print(j.somme())  
j.afficher()   
>>> Les dés n'ont pas été lancés !
>>> 15
>>> Les dés valent 4, 5, 6 et leur somme vaut 15.
```

### Question 9.2

- Définir les classes en Python. sachant qu'une instance de classe Jeu doit prendre en arguments le nombre de dés et le nombre de faces de chaque dé (identique pour tous les dés), et qu'une instance de classe De doit prendre en argument son nombre de faces.

```python
import random

class De:
    def __init__(self, faces):
        self.faces = faces  # Nombre de faces du dé
        self.valeur = -1     # Valeur initiale, -1 signifie qu'il n'a pas été lancé

    def lancer(self):
        """Lance le dé et attribue une valeur aléatoire entre 1 et le nombre de faces."""
        self.valeur = random.randint(1, self.faces)

class Jeu:
    def __init__(self, nombre_de_de, faces):
        self.des = [De(faces) for _ in range(nombre_de_de)]  # Création d'une liste de dés

    def lancer(self):
        """Lance tous les dés du jeu."""
        for de in self.des:
            de.lancer()

    def somme(self):
        """Calcule la somme des valeurs des dés."""
        return sum(de.valeur for de in self.des)

    def afficher(self):
        """Affiche la valeur des dés et leur somme."""
        if all(de.valeur == -1 for de in self.des):
            print("Les dés n'ont pas été lancés !")
        else:
            valeurs = [de.valeur for de in self.des]
            print(f"Les dés valent {', '.join(map(str, valeurs))} et leur somme vaut {self.somme()}.")

            
j = Jeu(3, 6)  
j.afficher() 
j.lancer()   
j.afficher()

>>> Les dés n'ont pas été lancés !
>>> Les dés valent 5, 2, 3 et leur somme vaut 10.
```
