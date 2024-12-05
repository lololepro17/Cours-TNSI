# Réponses à l'exercice 4 : Gestion d'un club de handball

## 1. Clé primaire pour la table `licencies`

### 1.a. L'attribut `nom` de la table `licencies` pourrait-il servir de clé primaire ? Justifier

Non, l'attribut `nom` ne peut pas servir de clé primaire car il n'est pas unique. Plusieurs licenciés peuvent avoir le même nom, rendant impossible l'identification unique de chaque ligne.

### 1.b. Citer un autre attribut de cette table qui pourrait servir de clé primaire

L'attribut `id_licencie` peut servir de clé primaire car il est unique pour chaque licencié et identifie chaque enregistrement de manière sûre.

---

## 2. Requêtes SQL sur la table `licencies`

### 2.a. Expliquer ce que renvoie la requête suivante

```sql
SELECT prenom, nom FROM licencies WHERE equipe = "-12 ans";
```

Cette requête renvoie les prénoms et noms de tous les licenciés qui jouent dans l'équipe des "-12 ans".

### 2.b. Que renvoie la requête précédente si `prenom, nom` est remplacé par une étoile (*) ?

Elle renvoie tout les attributs des licenciés qui apartiennent à l'équipe des "-12 ans".

### 2.c. Écrire la requête qui permet d'afficher les dates de tous les matchs joués à domicile de l'équipe "Vétérans"

```sql
SELECT date FROM matchs WHERE equipe = "Vétérans" AND lieu = "Domicile";
```

---

## 3. Inscription d'un nouveau licencié

```sql
INSERT INTO licencies (id_licencie, prenom, nom, annee_naissance, equipe)
VALUES (287, "Jean", "Lavenu", 2001, "Hommes 2");
```

---

## 4. Mise à jour des données d'un licencié

```sql
UPDATE licencies SET equipe = "Vétérans"
WHERE prenom = "Joseph" AND nom = "Cuviller" AND equipe = "Hommes 2";
```

---

## 5. Obtenir les noms des licenciés jouant contre le LSC le 19 juin 2021

```sql
SELECT nom FROM licencies
JOIN matchs ON licencies.equipe = matchs.equipe
WHERE matchs.adversaire = "LSC" AND matchs.date = "2021-06-19";
```
