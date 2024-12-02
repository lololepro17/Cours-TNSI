
# Exercices SQL : Chapitre 11

## Exercice 1

### 1. Instructions pour construire les objets du modèle relationnel

```sql
-- Création de la table Pays
CREATE TABLE Pays (
    Nom_pays VARCHAR(60) NOT NULL,
    Population INTEGER NOT NULL,
    Superficie INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (Nom_pays)
);

-- Création de la table Auteur
CREATE TABLE Auteur (
    Num_securite_sociale BIGINT NOT NULL,
    Nom_auteur VARCHAR(60) NOT NULL,
    Prenom_auteur VARCHAR(60) NOT NULL,
    Date_naissance DATE NOT NULL,
    Nom_pays VARCHAR(60) REFERENCES Pays(Nom_pays),
    PRIMARY KEY (Num_securite_sociale)
);
```

### 2. Saisir les informations sur la France et Marc Opolo

```sql
-- Ajout des données pour la France
INSERT INTO Pays (Nom_pays, Population, Superficie) 
VALUES ('France', 67063703, 543940);

-- Ajout des données pour Marc Opolo
INSERT INTO Auteur (Num_securite_sociale, Nom_auteur, Prenom_auteur, Date_naissance, Nom_pays) 
VALUES (1730820056320, 'Opolo', 'Marc', '1973-08-14', 'France');
```

## Exercice 2

### 1. Requête pour afficher toutes les occurrences de la table `Article`

```sql
SELECT * FROM Article;
```

### 2. Afficher les noms et prix des articles de "TopMark" triés par prix croissant

```sql
SELECT nom, prix FROM Article 
WHERE marque = 'TopMark' 
ORDER BY prix ASC;
```

### 3. Afficher les noms des articles en rupture de stock

```sql
SELECT nom FROM Article 
WHERE quantite = 0;
```

### 4. Mettre à jour le stock après l'achat de 2 savons

```sql
UPDATE Article 
SET quantite = quantite - 2 
WHERE nom = 'monsavon';
```

### 5. Rendre l'affichage de la requête sur les brioches plus lisible

Requête initiale : `SELECT marque WHERE nom LIKE '%brioche%';`

Correction :

```sql
SELECT marque FROM Article 
WHERE nom LIKE '%brioche%';
```

### 6. Modifier le prix d'un article spécifique

```sql
UPDATE Article 
SET prix = 15.7 
WHERE codeBarre = 3005000000000;
```

### 7. Afficher les codes-barres des articles de la catégorie "hygiene"

```sql
SELECT codeBarre FROM Article 
WHERE categorie = 'hygiene';
```

### 8. Afficher les articles avec un prix supérieur à 100 €

```sql
SELECT * FROM Article 
WHERE prix > 100;
```

### 9. Afficher les articles de "droguerie" contenant "soude" dans leur nom

```sql
SELECT * FROM Article 
WHERE categorie = 'droguerie' 
AND nom LIKE '%soude%';
```

### 10. Afficher les articles dont le code-barre commence par 25

```sql
SELECT * FROM Article 
WHERE codeBarre LIKE '25%';
```

### 11. Supprimer tous les articles de "quincaillerie"

```sql
DELETE FROM Article 
WHERE categorie = 'quincaillerie';
```

### 12. Requête pour les articles alimentaires commençant par "bisque"

Requête initiale : `SELECT nom, prix, quantite WHERE categorie = 'alimentaire' AND nom LIKE 'bisque%';`

Correction :

```sql
SELECT nom, prix, quantite FROM Article 
WHERE categorie = 'alimentaire' 
AND nom LIKE 'bisque%';
```

### 13. Afficher les marques qui fabriquent des croquettes pour chiens ou chats

```sql
SELECT DISTINCT marque FROM Article 
WHERE nom LIKE '%croquettes%' 
AND (nom LIKE '%chien%' OR nom LIKE '%chat%');
```
