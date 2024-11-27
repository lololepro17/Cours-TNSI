
# Correction des Exercices d'Algèbre Relationnelle

## Exercice 1 : Gestion des cours

### Schéma relationnel
- **Élèves** (Id, Nom, Prénom, Adresse, CP, Ville, Tel, Numprof)
- **Profs** (Id, Nom, Prénom, Tel, Salle)

**Remarque :**
- Clés primaires : `Id` dans chaque table.
- `Numprof` est une clé étrangère référencée à `Id` dans la table **Profs**.

### Réponses

1. **Les salles utilisées par les professeurs :**  
   `π(Salle)(Profs)`

2. **Le nom des professeurs et la salle qu’ils utilisent :**  
   `π(Nom, Prénom, Salle)(Profs)`

3. **Les numéros de téléphone des élèves qui habitent à Jonzac :**  
   `π(Tel)(σ(Ville = 'Jonzac')(Élèves))`

4. **Les noms et prénoms des élèves qui sont dans la classe NSI :**  
   *(Hypothèse : La classe NSI est identifiable dans une relation non décrite ici)*  
   `π(Nom, Prénom)(σ(Classe = 'NSI')(Élèves))`

5. **Les noms et prénoms des élèves qui ont cours avec M. Python :**  
   *(Hypothèse : Le professeur est identifiable par son nom complet)*  
   `π(Nom, Prénom)(Élèves ⨝(Numprof = Id) σ(Nom = 'Python')(Profs))`

---

## Exercice 2 : Gestion des locations

### Schéma relationnel
- **Appartements** (Id, Ville, Loyer, Surface, IdProp, IdLoc)
- **Propriétaires** (Id, Nom, Prénom, Ville, Tel)
- **Locataires** (Id, Nom, Prénom, Tel, Nombre)

**Remarque :**
- Clés primaires : `Id` dans chaque table.
- `IdProp` et `IdLoc` sont des clés étrangères référencées respectivement dans **Propriétaires** et **Locataires**.

### Réponses

1. **Les noms et prénoms des locataires qui occupent seuls un appartement :**  
   `π(Nom, Prénom)(σ(Nombre = 1)(Locataires))`

2. **Les villes où se trouvent des appartements de plus de 50 m² :**  
   `π(Ville)(σ(Surface > 50)(Appartements))`

3. **Les surfaces des appartements loués occupés par plus d’une personne :**  
   `π(Surface)(σ(Nombre > 1)(Appartements ⨝(IdLoc = Id)(Locataires)))`

4. **Les numéros de téléphone des propriétaires qui possèdent des appartements à louer de plus de 50 m² :**  
   `π(Tel)(Propriétaires ⨝(Id = IdProp) σ(Surface > 50)(Appartements))`

5. **Les noms des locataires qui occupent seuls un appartement et le loyer qu’ils payent :**  
   `π(Nom, Prénom, Loyer)(σ(Nombre = 1)(Locataires ⨝(Id = IdLoc)(Appartements)))`

---

## Exercice 3 : Gestion d’une librairie

### Schéma relationnel
- **Auteurs** (Id, Nom, Prénom)
- **Écrits** (Id_auteur, Id_titre)
- **Livres** (Id, Titre, PrixHT, Année, Id_genre, Id_editeur)
- **Genres** (Id, Genre)
- **Éditeurs** (Id, Nom)

**Remarque :**
- Clés primaires : `Id` dans chaque table.

### Réponses

1. **Les noms et prénoms de tous les auteurs :**  
   `π(Nom, Prénom)(Auteurs)`

2. **Les titres et années de parution de tous les livres :**  
   `π(Titre, Année)(Livres)`

3. **Les titres des livres parus en 2016 :**  
   `π(Titre)(σ(Année = 2016)(Livres))`

4. **Les titres et années de parution des livres parus entre 2000 et 2015 :**  
   `π(Titre, Année)(σ(2000 ≤ Année ≤ 2015)(Livres))`

5. **Les titres des livres coûtant plus de 30 euros HT :**  
   `π(Titre)(σ(PrixHT > 30)(Livres))`

6. **Les titres des livres parus en 2016 avec les éditeurs respectifs :**  
   `π(Titre, Nom)(σ(Année = 2016)(Livres ⨝(Id_editeur = Id)(Éditeurs)))`

7. **Les titres des livres du genre ‘science’ :**  
   `π(Titre)(Livres ⨝(Id_genre = Id)(σ(Genre = 'science')(Genres)))`

8. **Les titres des livres avec pour chacun le nom et le prénom de l’auteur :**  
   `π(Titre, Nom, Prénom)(Livres ⨝(Id = Id_titre)(Écrits ⨝(Id_auteur = Id)(Auteurs)))`
