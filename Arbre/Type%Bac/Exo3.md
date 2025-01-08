# Exercice 3 : Arbres Binaires

1. **Taille et hauteur de l’arbre de décision**

    - **Taille** : La taille d’un arbre binaire est le nombre total de nœuds.Donc cela fait 10.
    - **Hauteur** : La hauteur est définie comme le nombre maximum de nœuds sur le chemin de la racine à une feuille (incluant la racine et la feuille). Donc sa fait 6.

2. **Implémentation d’un arbre binaire avec un dictionnaire**

a. **Représentation graphique** :

L'arbre correspondant à la structure suivante :

```python
{'etiquette' :'a',
 'sag':{'etiquette' :'b',
   'sag':{},
   'sad' : {'etiquette' : 'd',
                 'sag' : {},
                 'sad' : {}}},
 'sad': {'etiquette' :'f',
    'sag' : {'etiquette' : 'g',
   'sag' : {},
   'sad' : {}},
    'sad' : {} }}
```

Représentation graphique :

```Nocode
         a
       /   \
      b     f
       \   /
        d g
```

b. **Représentation graphique du second arbre** :

Pour le code suivant :

```python
{'etiquette' :'H',
 'sag':{ 'etiquette' :'G',
   'sag': {'etiquette' : 'E',
                 'sag' : {},
                 'sad' : {}},
   'sad' : {'etiquette' : 'D',
                 'sag' : {},
                 'sad' : {'etiquette' : 'B',
                          'sag' : {},
      'sad' : {} }}},
 'sad': {'etiquette' :'F',
    'sag' : {'etiquette' : 'C',
   'sag' : {},
   'sad' : {'etiquette' : 'A',
                           'sag' : {} ,
                           'sad' : {}}},
    'sad' : {} }}
```

Représentation graphique :

```Nocode
            H
          /   \
         G     F
       /   \   /
      E     D C
           \   \
            B   A
```

**3. Fonction `parcours` et affichage**

a. **Affichage de la fonction `parcours`** :

Pour l’arbre correspondant au code donné, l’affichage est :

```Nocode
d
b
g
f
a
```

b. **Fonction `parcours_maladies`** :
Cette fonction affiche uniquement les feuilles de l’arbre :

```python
def parcours_maladies(arb):
    if arb == {}:
        return None
    if arb['sag'] == {} and arb['sad'] == {}:
        print(arb['etiquette'])
    else:
        parcours_maladies(arb['sag'])
        parcours_maladies(arb['sad'])
```

**4. Fonction `symptomes` pour afficher les symptômes d’une maladie**
Completages :

```python
def symptomes(arb, mal):
    if arb['sag'] != {}:
        symptomes(arb['sag'], mal)

    if arb['sad'] != {}:
        symptomes(arb['sad'], mal)

    if arb['etiquette'] == mal:
        arb['surChemin'] = True
        print('symptômes de', mal, ':')
    else:
        if arb['sad'] != {} and arb['sad']['surChemin']:
            print(arb['etiquette'])
            arb['surChemin'] = True

        if arb['sag'] != {} and arb['sag']['surChemin']:
            print(arb['etiquette'])
            arb['surChemin'] = True
```
