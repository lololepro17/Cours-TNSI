
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
   \[
   \pi_{Salle}(\text{Profs})
   \]

2. **Le nom des professeurs et la salle qu’ils utilisent :**
   \[
   \pi_{\text{Nom, Prénom, Salle}}(\text{Profs})
   \]

3. **Les numéros de téléphone des élèves qui habitent à Jonzac :**
   \[
   \pi_{Tel}(\sigma_{\text{Ville = 'Jonzac'}}(\text{Élèves}))
   \]

4. **Les noms et prénoms des élèves qui sont dans la classe NSI :**
   *(Hypothèse : La classe NSI est identifiable dans une relation non décrite ici)*
   \[
   \pi_{\text{Nom, Prénom}}(\sigma_{\text{Classe = 'NSI'}}(\text{Élèves}))
   \]

5. **Les noms et prénoms des élèves qui ont cours avec M. Python :**
   *(Hypothèse : Le professeur est identifiable par son nom complet)*
   \[
   \pi_{\text{Nom, Prénom}}(\text{Élèves} \bowtie_{\text{Numprof = Id}} \sigma_{\text{Nom = 'Python'}}(\text{Profs}))
   \]

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
   \[
   \pi_{\text{Nom, Prénom}}(\sigma_{\text{Nombre = 1}}(\text{Locataires}))
   \]

2. **Les villes où se trouvent des appartements de plus de 50 m² :**
   \[
   \pi_{\text{Ville}}(\sigma_{\text{Surface > 50}}(\text{Appartements}))
   \]

3. **Les surfaces des appartements loués occupés par plus d’une personne :**
   \[
   \pi_{\text{Surface}}(\sigma_{\text{Nombre > 1}}(\text{Appartements} \bowtie_{\text{IdLoc = Id}} \text{Locataires}))
   \]

4. **Les numéros de téléphone des propriétaires qui possèdent des appartements à louer de plus de 50 m² :**
   \[
   \pi_{\text{Tel}}(\text{Propriétaires} \bowtie_{\text{Id = IdProp}} \sigma_{\text{Surface > 50}}(\text{Appartements}))
   \]

5. **Les noms des locataires qui occupent seuls un appartement et le loyer qu’ils payent :**
   \[
   \pi_{\text{Nom, Prénom, Loyer}}(\sigma_{\text{Nombre = 1}}(\text{Locataires} \bowtie_{\text{Id = IdLoc}} \text{Appartements}))
   \]

6. **Les villes où les appartements ont une surface supérieure à 100 m² avec le nom des propriétaires :**
   \[
   \pi_{\text{Ville, Nom, Prénom}}(\sigma_{\text{Surface > 100}}(\text{Appartements} \bowtie_{\text{IdProp = Id}} \text{Propriétaires}))
   \]

7. **Les noms des propriétaires qui ont des appartements à louer dans la ville où ils habitent :**
   \[
   \pi_{\text{Nom, Prénom}}(\sigma_{\text{Appartements.Ville = Propriétaires.Ville}}(\text{Appartements} \bowtie_{\text{IdProp = Id}} \text{Propriétaires}))
   \]

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
   \[
   \pi_{\text{Nom, Prénom}}(\text{Auteurs})
   \]

2. **Les titres et années de parution de tous les livres :**
   \[
   \pi_{\text{Titre, Année}}(\text{Livres})
   \]

3. **Les titres des livres parus en 2016 :**
   \[
   \pi_{\text{Titre}}(\sigma_{\text{Année = 2016}}(\text{Livres}))
   \]

4. **Les titres et années de parution des livres parus entre 2000 et 2015 (bornes comprises) :**
   \[
   \pi_{\text{Titre, Année}}(\sigma_{\text{2000 ≤ Année ≤ 2015}}(\text{Livres}))
   \]

5. **Les titres des livres coûtant plus de 30 euros HT :**
   \[
   \pi_{\text{Titre}}(\sigma_{\text{PrixHT > 30}}(\text{Livres}))
   \]

6. **Les titres des livres parus en 2016 avec les éditeurs respectifs :**
   \[
   \pi_{\text{Titre, Nom}}(\sigma_{\text{Année = 2016}}(\text{Livres} \bowtie_{\text{Id_editeur = Id}} \text{Éditeurs}))
   \]

7. **Les titres des livres du genre "science" :**
   \[
   \pi_{\text{Titre}}(\sigma_{\text{Genre = 'science'}}(\text{Livres} \bowtie_{\text{Id_genre = Id}} \text{Genres}))
   \]

8. **Les titres des livres avec pour chacun le nom et le prénom de l’auteur :**
   \[
   \pi_{\text{Titre, Nom, Prénom}}(\text{Livres} \bowtie_{\text{Id = Id_titre}} \text{Écrits} \bowtie_{\text{Id_auteur = Id}} \text{Auteurs})
   \]
