# Exercice 4

## Thème abordé : programmation objet en langage Python

Un fabricant de brioches décide d’informatiser sa gestion des stocks. Il écrit pour cela un programme en langage Python. Une partie de son travail consiste à développer une classe Stock dont la première version est la suivante :

```python
class Stock:
    def __init__(self):
        self.qt_farine = 0  # quantité de farine initialisée à 0 g
        self.nb_oeufs = 0   # nombre d’œufs (0 à l’initialisation)
        self.qt_beurre = 0  # quantité de beurre initialisée à 0 g
```

1. Écrire une méthode ajouter_beurre(self, qt) qui ajoute la quantité qt de beurre à un objet de la classe Stock.
On admet que l’on a écrit deux autres méthodes ajouter_farine et ajouter_oeufs qui ont des fonctionnements analogues.

La méthode ajouter_beurre prend en paramètre la quantité de beurre qt à ajouter. On va simplement l'ajouter à la quantité actuelle de beurre.

```python
def ajouter_beurre(self, qt):
    self.qt_beurre += qt

def ajouter_farine(self, qt):
    self.qt_farine += qt

def ajouter_oeuf(self, qt):
    self.qt_oeuf += qt
```

2.Écrire une méthode afficher(self) qui affiche la quantité de farine, d’œufs et de beurre d’un objet de type Stock.
L’exemple ci-dessous illustre l’exécution de cette méthode dans la console :

```python

>>> mon_stock = Stock()
>>> mon_stock.afficher()
farine: 0
oeuf: 0
beurre: 0

>>> mon_stock.ajouter_beurre(560)
>>> mon_stock.afficher()
farine: 0
oeuf: 0
beurre: 560
```

```python

def afficher(self):
    print("farine:", self.qt_farine)
    print("oeuf:", self.nb_oeufs)
    print("beurre:", self.qt_beurre)
```

3.Pour faire une brioche, il faut 350 g de farine, 175 g de beurre et 4 œufs.
Écrire une méthode stock_suffisant_brioche(self) qui renvoie un booléen : True s’il y a assez d’ingrédients dans le stock pour faire une brioche et False sinon.

Pour savoir s'il y a suffisamment d'ingrédients pour faire une brioche, on vérifie que :

la quantité de farine est d'au moins 350 g,
la quantité de beurre est d'au moins 175 g,
le nombre d’œufs est d'au moins 4.
La méthode renvoie True si ces conditions sont remplies, sinon False.

```python
def stock_suffisant_brioche(self):
    return self.qt_farine >= 350 and self.qt_beurre >= 175 and self.nb_oeufs >= 4
```

4.On considère la méthode supplémentaire produire(self) de la classe Stock donnée par le code suivant :

```python
def produire(self):
    res = 0
    while self.stock_suffisant_brioche():
        self.qt_beurre -= 175
        self.qt_farine -= 350
        self.nb_oeufs -= 4
        res += 1
    return res
```

On considère un stock défini par les instructions suivantes :

```python

>>> mon_stock = Stock()
>>> mon_stock.ajouter_beurre(1000)
>>> mon_stock.ajouter_farine(1000)
>>> mon_stock.ajouter_oeufs(10)
```

a. On exécute ensuite l’instruction mon_stock.produire(). Quelle valeur s’affiche dans la console ? Que représente cette valeur ?

Lorsqu’on exécute mon_stock.produire(), le stock permet de fabriquer 2 brioches (1000 g de farine, 1000 g de beurre et 10 œufs). La fonction renverra donc 2, ce qui représente le nombre de brioches produites.

b. On exécute ensuite l’instruction mon_stock.afficher(). Que s’affiche-t-il dans la console ?

Après la production de 2 brioches, les quantités restantes dans le stock seront :

Farine : 1000 - (2 *350) = 300 g
Beurre : 1000 - (2* 175) = 650 g
Œufs : 10 - (2 * 4) = 2 œufs
Donc, l'affichage de mon_stock.afficher() donnera :

farine: 300
oeuf: 2
beurre: 650
5. L’industriel possède n lieux de production distincts et donc n stocks distincts.
On suppose que ces stocks sont dans une liste dont chaque élément est un objet de type Stock. Écrire une fonction Python nb_brioches(liste_stocks) possédant pour unique paramètre la liste des stocks et renvoyant le nombre total de brioches produites.

Pour calculer le nombre total de brioches produites par plusieurs lieux de production, on crée une fonction nb_brioches qui prend une liste de stocks en paramètre. Cette fonction itère sur chaque stock, appelle la méthode produire et additionne le nombre de brioches produites.

```python
def nb_brioches(liste_stocks):
    total_brioches = 0
    for stock in liste_stocks:
        total_brioches += stock.produire()
    return total_brioches
```

Cette fonction renverra le nombre total de brioches produites pour tous les stocks de la liste.
