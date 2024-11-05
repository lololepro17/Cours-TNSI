#  Poo: Exercice 

## Exercice 1 - Un rat de bibliothèque


### Exercice 1.1 :

- Instancier un nouveau livre mon_livre_favori et afficher ensuite son titre.

```python

# Définition de la classe Livre
class Livre:  
    def __init__(self, un_titre, un_auteur, une_année): 
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

- Écrire une fonction plus_ancien(livre1, livre2) qui renvoie le titre du livre ayant été publié en premier parmi les deux livres passés en argument.

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

- Écrire une classe Eleve contenant les attributs nom, classe et moyenne.

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

- Écrire une fonction chouchou(eleve1, eleve2) qui renvoie le nom de l'élève ayant la meilleure moyenne.

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

- Écrire une classe TriangleRectangle qui contiendra les attributs cote1, cote2 et hypotenuse. Cependant, le constructeur ne prendra en paramètres que cote1 et cote2, l'attribut hypotenuse se calculera automatiquement.

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

- Créer une fonction calculer_périmètre(rectangle) externe qui renvoie le périmètre du rectangle donné en argument.

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

- Au sein du même script où est définit la classe Rectangle, définir une nouvelle classe Cercle. On souhaite une fonction ou une méthode qui permet de calculer aussi l'aire pour les instances de Cercle.

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

- 1.Écrire une classe Voiture qui contiendra les attributs kilometrage, consommation (nombre de litres de carburant consommé pour 100 kilomètres) dont les valeurs seront données comme arguments à l'initialisation et un dernier attribut carburant valant 0 par défaut.

- 2.Doter la classe d'une méthode affiche qui affiche le kilométrage et le carburant disponible.

- 3.Doter la classe d'une méthode remplir qui prend en argument un entier correspondant au volume de carburant à ajouter au réservoir.

- 4.Doter la classe d'une méthode avance qui prend en argument un entier correspondant au nombre de kilomètres parcourus et qui actualise les valeurs des attributs kilometrage et consommation.

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
