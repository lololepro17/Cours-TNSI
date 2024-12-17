# Implémentation d'une Pile en Python

## Exercice 1

### 1. Créer une liste avec les éléments `12`, `14`, `8`, `7`, `19`, `22`

On utilise une pile pour empiler (ajouter) les valeurs dans l'ordre donné.

```python
empiler(12)
empiler(14)
empiler(8)
empiler(7)
empiler(19)
empiler(22)
```

### 2. Instruction pour afficher le sommet de la pile

L'instruction suivante permet de **lire** le sommet de la pile sans le retirer.

```python
liresommet()
```

### 3. Instruction pour montrer la taille de la liste

Pour connaître la **taille** actuelle de la pile, utilise :

```python
taille()
```

### 4. Instruction pour insérer `20` entre `7` et `8` dans la pile

On doit d'abord dépiler jusqu'à atteindre l'endroit souhaité.

```python
depiler()  # Retire 22
depiler()  # Retire 19
depiler()  # Retire 7
empiler(20)  # Insère 20
empiler(7)   # Remet 7
empiler(19)  # Remet 19
empiler(22)  # Remet 22
```
