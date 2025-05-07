# Exercice 1

2.Les trois états d'un processus sont : prêt, élu, bloqué.

3.Faire une file

```python
class File:
    def __init__(self):
        """Créer une file vide"""
        self.contenu = []

    def enfiler(self, element):
        """Enfiler un élément dans la file"""
        self.contenu.append(element)
    
    def defiler(self):
        """Renvoie le premier élément de la file et le retire de la file"""
        if not self.est_vide():
            return self.contenu.pop(0)
        else:
            return None

    def est_vide(self):
        """Renvoie True si la file est vide, False sinon"""
        return self.contenu == []
```

4.Tableau des processus

|     | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|-----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| P1  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| P2  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| P3  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| P4  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |