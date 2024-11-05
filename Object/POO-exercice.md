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
mon_livre_favori = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)

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

livre1 = Livre("L'Étranger", "Albert Camus", 1942)
livre2 = Livre("Martin Eden", "Jack London", 1909)
livre3 = Livre("Les Frères Karamazov", "Fiodor Dostoïevski", 1880)

print(plus_ancien(livre1, livre3))

>>> Les Frères Karamazov
```

## Exercice 2 - Classe et salle de classe

### Exercice 2.1

- Écrire une classe Eleve contenant les attributs nom, classe et moyenne.