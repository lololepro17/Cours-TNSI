# Corrigé du sujet 25-NSIJ1AN1 

## Exercice 1

### 1
Feuilles simple -> non
Alterné -> oui
Bord denté -> non
-> Robinier, noyer

**Le vegetal observé corresponds à robinier ou Noyer**

### 2

Feuilles simple -> oui
Alterné -> oui
Inserer en helice -> oui
Forme ovale -> non 
-> - 

**D'apres l'arbre de decision on ne peux pas identifier ce vegetal**

### 3

```python
class Noeud:
    def __init__(self, question, sioui, sinon):
        self.question = question
        self.sioui = sioui
        self.sinon = sinon

class Feuille_resultat:
    def __init__(self, vegetaux):
        self.vegetaux = vegetaux

# Feuilles
feuille_vide = Feuille_resultat([])
feuille_sorbier = Feuille_resultat(['Sorbier'])
feuille_robinier_noyer = Feuille_resultat(['Robinier', 'Noyer'])

# Noeuds
noeud_bord_dente = Noeud("Bord denté ?", feuille_sorbier, feuille_robinier_noyer)
noeud_alternees = Noeud("Alternées ?", noeud_bord_dente, feuille_vide)
noeud_simples = Noeud("Simples ?", feuille_vide, noeud_alternees)

# Racine
arbre_2 = noeud_simples

```

### 4

```python
    def est_resultat(self):
        return False
```

**La méthode est_resultat retourne False car un objet de la classe Noeud représente une question intermédiaire, et pas un résultat final de l’arbre de décision.**

### 5

```python
    def est_resultat(self):
        return True
```

**La méthode est_resultat retourne True car un objet de la classe Feuille_resultat représente une feuille de l’arbre.**

### 6

```python
    def nb_vegetaux(self):
        return len(self.vegetaux)
```

### 7

```python
def nb_vegetaux(self):
        return self.sioui.nb_vegetaux() + self.sinon.nb_vegetaux()
```

### 8

```python
    def liste_questions(self):
        return []
```

### 9

```python
def liste_questions(self):
        return [self.question] + self.sioui.liste_questions() + self.sinon.liste_questions()
```

### 10

```python 

def est_bien_renseigne(dico_vegetal, arbre):
    questions = arbre.liste_questions()
    for question in questions:
        if question not in dico_vegetal:
            return False
    return True
```

### 11

```python
def identifier_vegetaux(dico_vegetal, arbre):
    if arbre.est_resultat():
        return arbre.vegetaux
    if dico_vegetal[arbre.question]:
        return identifier_vegetaux(dico_vegetal, arbre.sioui)
    else:
        return identifier_vegetaux(dico_vegetal, arbre.sinon)
```

## Exercice 2

### 1

```python
def passer_transit(self):
    self.etat = 'transit'
```
