### Réponse au sujet portant sur les arbres binaires, la programmation orientée objet et la récursivité

#### Question 1 : Plus grande somme racine-feuille
Pour l'arbre donné dans le sujet :
```
        5
      /   \
     7     2
    / \   / \
   4   1 8   3
  / \       \
 2   3       5
```

Les chemins racine-feuille et leurs sommes sont :
1. 5 -> 7 -> 4 -> 2 = 18
2. 5 -> 7 -> 4 -> 3 = 19
3. 5 -> 7 -> 1 = 13
4. 5 -> 2 -> 8 = 15
5. 5 -> 2 -> 3 -> 5 = 15

**19**.

---

#### Question 2 : Représentation de l'arbre avec la classe Noeud

```python
class Noeud:
    def __init__(self, v):
        self.etiquette = v
        self.sag = None
        self.sad = None

    def modifier_sag(self, nsag):
        self.sag = nsag

    def modifier_sad(self, nsad):
        self.sad = nsad

racine = Noeud(5)
noeud_7 = Noeud(7)
noeud_2 = Noeud(2)
noeud_4 = Noeud(4)
noeud_1 = Noeud(1)
noeud_8 = Noeud(8)
noeud_3 = Noeud(3)
noeud_2b = Noeud(2)
noeud_3b = Noeud(3)
noeud_5b = Noeud(5)

# Build
racine.modifier_sag(noeud_7)
racine.modifier_sad(noeud_2)

noeud_7.modifier_sag(noeud_4)
noeud_7.modifier_sad(noeud_1)

noeud_2.modifier_sag(noeud_8)
noeud_2.modifier_sad(noeud_3)

noeud_4.modifier_sag(noeud_2b)
noeud_4.modifier_sad(noeud_3b)

noeud_3.modifier_sad(noeud_5b)
```

---

#### Question 3 : Méthode `pgde_somme`
plus grande somme racine-feuille :

```python
class Noeud:

    def pgde_somme(self):
        if self.sag is None and self.sad is None:
            return self.etiquette
        
        somme_gauche = self.sag.pgde_somme() if self.sag else float('-inf')
        somme_droite = self.sad.pgde_somme() if self.sad else float('-inf')
        
        return self.etiquette + max(somme_gauche, somme_droite)
```

---

#### Question 4 : Arbre magique
##### a. Complétion de l'arbre magique
```
        5
      /   \
     7     2
    / \   / \
   4   1 8   3
  / \       \
 3   3       7
```

##### b. Méthode `est_magique`
Methode de verification d'arbre magique :

```python
class Noeud:
    def est_magique(self):
        if self.sag is None and self.sad is None:  # Quand feuille
            return True

        somme_gauche = self.sag.pgde_somme() if self.sag else None
        somme_droite = self.sad.pgde_somme() if self.sad else None

        if somme_gauche != somme_droite:
            return False

        return (self.sag.est_magique() if self.sag else True) and \
               (self.sad.est_magique() if self.sad else True)
```
