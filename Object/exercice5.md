# EXERCICE 5 (4 points)
## Thème : Programmation Orientée Objet

Les participants à un jeu de LaserGame sont répartis en équipes. Ils s’affrontent en tirant avec une arme factice qui émet des infrarouges. Les ordinateurs embarqués dans les vestes utilisent la programmation orientée objet pour modéliser les joueurs.

La classe Joueur est définie comme suit :

```python
class Joueur:
    def __init__(self, pseudo, identifiant, equipe):
        ''' constructeur '''
        self.pseudo = pseudo  
        self.equipe = equipe  
        self.id = identifiant  
        self.nb_de_tirs_emis = 0     
        self.liste_id_tirs_recus = []  
        self.est_actif = True 

    def tire(self):
        '''méthode déclenchée par l'appui sur la gâchette'''
        if self.est_actif:
            self.nb_de_tirs_emis += 1 

    def est_determine(self):
        '''méthode qui renvoie True si le joueur réalise un grand nombre de tirs'''
        return self.nb_de_tirs_emis > 500 

    def subit_un_tir(self, id_recu):
        '''méthode déclenchée par les capteurs de la veste'''
        if self.est_actif:
            self.est_actif = False 
            self.liste_id_tirs_recus.append(id_recu) 
```

1. **Recopier l’instruction correcte pour déclarer un objet joueur1, instance de la classe Joueur, avec le pseudo "Sniper", l’identifiant 319, et l’équipe "A".**

- Instruction 1 : joueur1 = ["Sniper", 319, "A"]
- Instruction 2 : joueur1 = new Joueur["Sniper", 319, "A"]
- Instruction 3 : joueur1 = Joueur("Sniper", 319, "A")
- Instruction 4 : joueur1 = Joueur{"pseudo":"Sniper", "id":319, "equipe":"A"}

**Réponse** : L'instruction correcte est : Instruction 3 : joueur1 = Joueur("Sniper", 319, "A")

2. **La méthode subit_un_tir ajoute l’identifiant du tireur à liste_id_tirs_recus et désactive le joueur (en réglant est_actif sur False). Il doit revenir à sa base pour redevenir actif.
a. Écrire la méthode redevenir_actif qui rend le joueur actif uniquement s’il est actuellement désactivé.**

**Réponse** :

```python
def redevenir_actif(self):
    if not self.est_actif:
        self.est_actif = True
```

b. **Écrire la méthode nb_de_tirs_recus qui renvoie le nombre de tirs reçus par un joueur.**

Réponse :

```python
def nb_de_tirs_recus(self):
    return len(self.liste_id_tirs_recus)
```

3. En fin de partie, chaque équipe rejoint sa base où un ordinateur utilise la classe Base pour récupérer les données. La classe Base est définie comme suit :
Attributs :

- equipe : nom de l’équipe (str), par exemple "A"
liste_des_id_de_l_equipe : liste des identifiants des joueurs de l’équipe

- score : score de l’équipe, initialisé à 1000
Méthodes :

- est_un_id_allie : renvoie True si l’identifiant est celui d’un joueur allié, False sinon.
- incremente_score : fait varier le score de l’attribut score selon le nombre passé en paramètre.
- collecte_information : récupère les statistiques d’un participant (instance de Joueur) pour ajuster le score de l’équipe.

```python
def collecte_information(self, participant):
    if participant.equipe == self.equipe:  # test 1
        for id in participant.liste_id_tirs_recus:
            if self.est_un_id_allie(id):  # test 2
                self.incremente_score(-20)
            else:
                self.incremente_score(-10)
```
a. Quel test (test 1 ou test 2) permet de vérifier qu’en fin de partie un joueur n’a pas rejoint la base adverse ?

**Réponse** : Le test 1 permet de vérifier que le joueur est bien dans l’équipe associée à la base.

b. Comment varie le score de la base lorsqu’un joueur de l’équipe a été touché par un coéquipier ?

**Réponse** : Lorsqu’un joueur de l’équipe est touché par un coéquipier, le score de la base diminue de 20 points.

4. On souhaite accorder un bonus de 40 points à la base pour chaque joueur "déterminé" (qui effectue un grand nombre de tirs). Complétez les lignes de code suivantes à ajouter à la fin de la méthode collecte_information.

```python
if participant.est_determine():  # si le participant réalise un grand nombre de tirs
    self.incremente_score(40)  # le score de la base augmente de 40
```
