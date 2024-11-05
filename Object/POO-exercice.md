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
