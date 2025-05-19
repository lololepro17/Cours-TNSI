# Correction du sujet 23-NSIJ1PO1 

## Exercice 1 

### 1.

a. L'id equipe doit etre une clé unique car c'est une clé primaire. On essaie de rajouter une equipe avec l'id 11 alors quelle existe deja 
b. Un numeros de telephone est composé de chiffre et de tiré donc chianes de caractere.
c. on obtiens ["Lyon","451 cours d'Emile Zola, 69100 Villuerbanne",0405060708]
d. On obtiens le nombre d'équipes soit 12.
e. 
```
f. 
```SQL
UPDATE Equipe
SET nom='tarbes'
WHERE id_equipe = 4 
```

### 2.
a. L'atribut permer de llié la table joueuse a la table Equipe, c'est une clé etrangere.
b.La supression d'une equipe doit s'acompagner de la modification de la table  joueur pour que l'atribut ne pointe pas vers une equipe qui n'esxiste plus.
c.
```SQL 
 SELECT Joueuse.nom, prenom
 FROM Joueuse
 JOIN Equipe ON Equipe.id_equipe = Joueuse.id_equipe
 WHERE Equipe.nom = ‘Angers’
 ORDER BY Joueuse.nom
 ```
 
### 3.

a.  Match (id_match : INT, date : DATE, #id_eq_dom : INT,
 #id_eq_dep : INT, score_eq_dom : INT, score_eq_dep : INT)
 Les clés étrangères font référence à l’attribut id_equipe de la table Equipe

b.  
```SQL
INSERT INTO Match
 VALUES
 (10, 23/10/2021, 3, 6, 73, 78)
 ```

### 4.

Stat (id_stat : INT, #id_joueuse : INT, #id_match : INT, points : INT, rebonds :
 INT, passes_dec : INT)
 