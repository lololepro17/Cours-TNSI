# ** Poo exercice **

## Exercice 1 - Un rat de bibliothèque
```python

# Définition de la classe Livre
class Livre:  
    def __init__(self, un_titre, un_auteur, une_année): 
        self.titre  = un_titre 
        self.auteur = un_auteur
        self.année  = une_année

        
# Instanciation de plusieurs objets de classe Livre 
livre1 = Livre("L'Étranger", "Albert Camus", 1942)
livre2 = Livre("Martin Eden", "Jack London", 1909)
livre3 = Livre("Les Frères Karamazov", "Fiodor Dostoïevski", 1880)

```