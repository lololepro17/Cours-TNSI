# Exercice 4
Thème aborder : programation objet en languange Python

## Un fabricant de brioches décide d'informatisez sa gestion des stocks. Il écrit pour cela un programme n language Python. Une partie de son travail consiste à développer une classe `Stock` dont la première dont la pemiere version est la suivante :

 ```python

class Stocks:
    def __init__(self):
        self.qt_farine = 0 #quantité de farine init a 0g
        self.nb_oeuf = 0 # Quantité d'oeuf ( 0 a l'init)
        self.qt_beurre = 0 # Quantité de beurre init a 0g
```

### 1. Ecrire une methode `ajouter_beurre(self, qt)` qui ajoute la quantité de beurre à un objet de la classe `Stock`

## On admet que l'on a écrit deux autres methodes `ajouter_farine` et `ajouter_oeuf` qui ont des fonctionement analogues.

## 2.Ecrire une methode `afficher(self)`qui affiche la quantité de farine d'oeuf et de beurre d'un objet de type `Stock`. L'eample ci dessous illustre l'execution de cette methode dans la console
```python
>>> mon_stock = Stock()
>>> mon_stock.afficher()
farine: 0
oeuf : 0
beurre: 0
>>> mon_stock.ajouter_beurre(560)
>>> mon_stock.afficher()
farine: 0
oeuf : 0
beurre : 560
```

## 3.Pour faire une brioche, il faut 350 gramme de farine, 175g de beurrre et 4 oeufs. écrire une methode stock_suffisant_brioche(self) qui renvoie un booléen : Vrai s'il y a assez d'ingredients dans le stock pour faire une brioche et FAUX sinon.

## 4.On considere la methode sumplementaire prodiore(self) de la class Stock données par le code suivant:
```python
def produire(self):
    res = 0
    while self.stock_suffisant_brioche():
        self.qt_beurre = self.qt_beurre - 175
        self.qt_farine = self.qt_farine 350
        self.nb_oeuf = self.nb_oeuf - 4
        res = res + 1 
    return res
```
On considere un stock défini par les instructions suivantes
