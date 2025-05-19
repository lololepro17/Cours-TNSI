# Exo 3

## Q1

**1 → noir**

```python
def creer_goban_vide(n):
    assert n==9 or n==13 or n==19, "valeur de n non permise"
    return [[0] *n  for _ in range(n)
```
 lève l’exception AssertionError en indiquant « valeur de n non permise »

## Q2

```python
 def libertes_pierre(go, pi, pj):
    libertes = []
    n = len(go)
    for i, j in [(pi+1, pj), (pi-1, pj), (pi, pj+1), (pi, pj-1)]:
        if est_valide(i, p, n) and go[i][p] == 0:
            libertes += [(i, j)]
    return libertes
```

## Q3

