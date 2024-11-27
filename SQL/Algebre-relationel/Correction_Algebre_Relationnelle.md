
# Correction des Exercices d'Algèbre Relationnelle

## Introduction
Ce document contient les réponses aux exercices en algèbre relationnelle. Les formules sont rendues avec MathJax pour faciliter la lecture des expressions mathématiques.

## Intégration MathJax
Ajoutez ce fichier dans un environnement compatible avec MathJax (par exemple, un serveur local).

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

---

## Exercice 1 : Gestion des cours

### Schéma relationnel
- **Élèves** \((\text{Id}, \text{Nom}, \text{Prénom}, \text{Adresse}, \text{CP}, \text{Ville}, \text{Tel}, \text{Numprof})\)
- **Profs** \((\text{Id}, \text{Nom}, \text{Prénom}, \text{Tel}, \text{Salle})\)

**Remarque :**
- Clés primaires : \(\text{Id}\) dans chaque table.
- \(\text{Numprof}\) est une clé étrangère référencée à \(\text{Id}\) dans la table **Profs**.

### Réponses

1. **Les salles utilisées par les professeurs :**
   \[
   \pi_{\text{Salle}}(\text{Profs})
   \]

2. **Le nom des professeurs et la salle qu’ils utilisent :**
   \[
   \pi_{\text{Nom, Prénom, Salle}}(\text{Profs})
   \]

3. **Les numéros de téléphone des élèves qui habitent à Jonzac :**
   \[
   \pi_{\text{Tel}}(\sigma_{\text{Ville = 'Jonzac'}}(\text{Élèves}))
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
- **Appartements** \((\text{Id}, \text{Ville}, \text{Loyer}, \text{Surface}, \text{IdProp}, \text{IdLoc})\)
- **Propriétaires** \((\text{Id}, \text{Nom}, \text{Prénom}, \text{Ville}, \text{Tel})\)
- **Locataires** \((\text{Id}, \text{Nom}, \text{Prénom}, \text{Tel}, \text{Nombre})\)

**Remarque :**
- Clés primaires : \(\text{Id}\) dans chaque table.
- \(\text{IdProp}\) et \(\text{IdLoc}\) sont des clés étrangères référencées respectivement dans **Propriétaires** et **Locataires**.

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

---

## Exercice 3 : Gestion d’une librairie

### Schéma relationnel
- **Auteurs** \((\text{Id}, \text{Nom}, \text{Prénom})\)
- **Écrits** \((\text{Id_auteur}, \text{Id_titre})\)
- **Livres** \((\text{Id}, \text{Titre}, \text{PrixHT}, \text{Année}, \text{Id_genre}, \text{Id_editeur})\)
- **Genres** \((\text{Id}, \text{Genre})\)
- **Éditeurs** \((\text{Id}, \text{Nom})\)

**Remarque :**
- Clés primaires : \(\text{Id}\) dans chaque table.

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
