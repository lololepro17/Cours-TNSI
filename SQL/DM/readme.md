# Partie 1 : Qu’est-ce que l’Open Data ?

## Définition des données ouvertes

Les données ouvertes (ou Open Data) sont des informations :

- Accessibles librement et gratuitement.
- Disponibles dans des formats interopérables.

**Objectif :** permettre à tout citoyen, entreprise ou association d’utiliser ces données pour analyser ou extraire des informations utiles.

## Les 8 principes des données ouvertes (2007, Open Government Data, USA)

1. **Complètes** : inclure toutes les données disponibles sauf celles portant atteinte à la vie privée ou à la sécurité.
2. **Primaires** : fournir les données brutes, non modifiées.
3. **Récentes et actualisées** : publier rapidement les données pour conserver leur valeur.
4. **Accessibles** : à disposition du plus grand nombre d’utilisateurs.
5. **Exploitables** : être structurées et documentées pour un traitement informatisé.
6. **Accès non discriminatoire** : accessibles à tous sans besoin d’inscription.
7. **Format non propriétaire** : fournir un format libre de droits (ex : non PDF, non Excel).
8. **Libres de droits** : sans restriction de copyright, marque déposée ou brevet.

## Origine des données ouvertes

- **Publique** : issue des services publics, collectivités ou communes.
- **Privée** : provenant d’entreprises ou institutions contribuant à des projets d’utilité publique (ex : SNCF, RATP).

**En France :**

- Coordonné par la mission Etalab.
- Jeux de données disponibles sur [data.gouv.fr](https://www.data.gouv.fr/fr/).

# Partie 2 : Exploiter un jeu de données

## Activité 1 : Utilisation d’un tableur

1. **Trouver le jeu de données** sur [data.gouv.fr](https://www.data.gouv.fr/).
2. **Lire le descriptif** du jeu de données. -> J'ai lu 
3. **Identifier l’éditeur** de ce jeu de données. c'est koumoul
4. **Télécharger le jeu de données** au format CSV. check
5. **Ouvrir le fichier** dans un tableur. check
6. **Choisir l’encodage correct** : UTF-8 est recommandé.
7. **Analyser les en-têtes de colonnes**. ya plein d'info position nombre de veicule sexe etc

## Activité 2 : Importer les données dans DB Browser

1. **Créer une base de données SQLite3** nommée `BDD_Accidents_Velos.sqlite3`.
2. **Importer le fichier CSV** dans une table appelée `accidents`.

## Activité 3 : Exploiter les données avec DB Browser

### Questions et Requêtes SQL

1. **Types de données :**
   - `Num_Acc` : INTEGER
   - `date` : TEXT
   - `an` : INTEGER
   - `dep` : TEXT

2. **Nombre total d’accidentés sur la période :**

   ```sql
   SELECT COUNT(*) AS Nombre_Accidentés FROM accident_velo;
   ```

3. **Nombre total d’accidents sur la période :**

   ```sql
   SELECT COUNT(DISTINCT Num_Acc) AS Nombre_Accidents FROM accident_velo;
   ```

4. **Nombre d’accidentés dans le département du Rhône :**

   ```sql
   SELECT COUNT(*) AS Nombre_Accidentés FROM accident_velo WHERE dep = '69';
   ```

5. **Nombre d’accidents avec décès de cyclistes dans le Rhône :**

   ```sql
   SELECT COUNT(*) AS Nombre_Accidents_Mortels FROM accident_velo WHERE dep = '69' AND grav = '3';
   ```

6. **Dates et jours des accidents mortels dans le Rhône :**

   ```sql
   SELECT date, jour FROM accident_velo WHERE dep = '69' AND grav = '3' ORDER BY jour;
   ```

7. **Classement des données par département :**

   ```sql
   SELECT * FROM accident_velo ORDER BY dep DESC;
   ```

8. **Accidents selon l’horaire :**

   ```sql
   SELECT CASE
       WHEN SUBSTR(hrmn, 1, 2) BETWEEN '06' AND '12' THEN 'Matin'
       WHEN SUBSTR(hrmn, 1, 2) BETWEEN '12' AND '18' THEN 'Après-midi'
       ELSE 'Soir/Nuit'
   END AS Periode, COUNT(*) AS Nombre_Accidents
   FROM accident_velo
   GROUP BY Periode;
   ```

9. **Nombre d’accidents par département :**

   ```sql
   SELECT dep, COUNT(*) AS Nombre_Accidents FROM accident_velo GROUP BY dep ORDER BY Nombre_Accidents DESC;
   ```

---
