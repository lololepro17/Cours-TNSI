# Introduction aux bases de données relationnelles

## 1. Qu'est-ce qu'une base de données ?

Une base de données est un ensemble organisé d'informations ou de données stockées de manière à pouvoir être facilement consultées, gérées et mises à jour.

### Exemple

Un carnet d'adresses contenant des informations sur des amis :

- Leur nom,
- Leur numéro de téléphone,
- Leur adresse email.

Ce carnet d'adresses peut être considéré comme une petite base de données.

---

## 2. Les bases de données relationnelles

Une base de données relationnelle est un type particulier de base de données où les informations sont organisées en **tables**. Une table ressemble à un tableau avec des lignes et des colonnes :

- **Les colonnes** représentent les caractéristiques (ou **attributs**) des données.
- **Les lignes** représentent les enregistrements (**tuples**).

### Exemple de table

Table Amis :

| ID | Nom      | Téléphone    | Email              |
|----|----------|----------------|--------------------|
| 1  | Alice    | 06 12 34 56 78 | <alice@mail.com>     |
| 2  | Bob      | 06 98 76 54 32 | <bob@mail.com>       |
| 3  | Charlie  | 06 11 22 33 44 | <charlie@mail.com>   |

- Chaque ligne est une donnée unique sur une personne.
- Chaque colonne décrit une information précise.

---

## 3. Les notions clés dans une base de données relationnelle

### a) Clé primaire

La **clé primaire** est un identifiant unique pour chaque ligne de la table. Elle permet de distinguer chaque enregistrement.

- Dans l'exemple, la colonne **ID** est la clé primaire.

### b) Clé étrangère

Une **clé étrangère** est une colonne qui fait référence à la clé primaire d'une autre table pour créer un lien entre les deux tables.

#### Exemple avec deux tables

1. **Table Amis**

| ID | Nom      | Téléphone    |
|----|----------|----------------|
| 1  | Alice    | 06 12 34 56 78 |
| 2  | Bob      | 06 98 76 54 32 |

2.**Table Activités**

| ID | Activité        | AmiID |
|----|-----------------|-------|
| 1  | Cinéma         | 1     |
| 2  | Football        | 2     |
| 3  | Lecture         | 1     |

Dans cet exemple :

- **AmiID** dans la table Activités est une clé étrangère qui fait référence à l'ID de la table Amis.
- Cela montre que :
  - Alice aime le cinéma et la lecture.
  - Bob aime le football.

---

## 4. Pourquoi utiliser une base relationnelle ?

- **Organisation claire** : Les données sont bien structurées.
- **Réduction des redondances** : Pas besoin de répéter plusieurs fois la même information.
- **Facilité de gestion** : Les relations entre les tables permettent de regrouper les informations liées.

---

## 5. Langage SQL pour manipuler les bases relationnelles

SQL (**Structured Query Language**) est le langage utilisé pour travailler avec les bases de données relationnelles. Voici quelques commandes de base :

### Créer une table

```sql
CREATE TABLE Amis (
    ID INT PRIMARY KEY,
    Nom TEXT,
    Telephone TEXT,
    Email TEXT
);
```

### Ajouter des données

```sql
INSERT INTO Amis (ID, Nom, Telephone, Email)
VALUES (1, 'Alice', '06 12 34 56 78', 'alice@mail.com');
```

### Lire des données

```sql
SELECT * FROM Amis;
```

### Rechercher des données avec un critère

```sql
SELECT * FROM Amis WHERE Nom = 'Alice';
```

### Mettre à jour des données

```sql
UPDATE Amis
SET Telephone = '06 99 88 77 66'
WHERE ID = 1;
```

### Supprimer des données

```sql
DELETE FROM Amis WHERE ID = 2;
```

---

## 6. Exemple d'application concrète

Si tu crées une application pour gérer une bibliothèque :

- Une table **Livres** contiendra les titres, les auteurs et les catégories.
- Une table **Emprunts** indiquera quels livres sont empruntés et par qui.

Avec une base relationnelle, tu peux facilement répondre à des questions comme :

- "Quels livres sont disponibles ?"
- "Qui a emprunté tel livre ?"

---

Ce cours simple te donne les bases pour comprendre les bases de données relationnelles. Si tu veux approfondir, je peux t'aider avec des exemples ou des exercices supplémentaires !
