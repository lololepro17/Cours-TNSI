# TP exploitation de données Open-Data

## Partie 2 : Exploiter un jeu de données

### Activité 1

1. Jeu de données trouvez
2. Ce jeu de données est issue d'un plus grand jeu de données qui regroupes tout les accidents
3. L'éditeur de ce jeu de données est 'koumoul'.
4.
5.
6.
7. Les entetes qui sont presenter dans le documents sont les suivantes : `Num_Acc,date,an,mois,jour,hrmn,dep,com,lat,long,agg,int,col,lum,atm,catr,circ,nbv,prof,plan,lartpc,larrout,surf,infra,situ,grav,sexe,age,trajet,secuexist,equipement,obs,obsm,choc,manv,vehiculeid,typevehicules,manoeuvehicules,numVehicules`.
8. Il y a 74759 accidents presents dans le document.

### Activité 3

1. Les attributs ne sont pas ecrit tels quel mais on peut identifier
   - `Num_Acc` : INTEGER
   - `date` : TEXT
   - `an` : INTEGER
   - `dep` : TEXT

2. Nombre total d’accidentés sur la période :

   ```sql
   SELECT COUNT(*) AS Nombre_Accidentés FROM accident_velo;
   ```

3. Nombre total d’accidents sur la période :

   ```sql
   SELECT COUNT(DISTINCT Num_Acc) AS Nombre_Accidents FROM accident_velo;
   ```

4. Nombre d’accidentés dans le département du Rhône :

   ```sql
   SELECT COUNT(*) AS Nombre_Accidentés FROM accident_velo WHERE dep = '69';
   ```

5. Nombre d’accidents avec décès de cyclistes dans le Rhône :

   ```sql
   SELECT COUNT(*) AS Nombre_Accidents_Mortels FROM accident_velo WHERE dep = '69' AND grav = '3';
   ```

6. Dates et jours des accidents mortels dans le Rhône :

   ```sql
   SELECT date, jour FROM accident_velo WHERE dep = '69' AND grav = '3' ORDER BY jour;
   ```

7. Classement des données par département :

   ```sql
   SELECT * FROM accident_velo ORDER BY dep DESC;
   ```

8. Accidents selon l’horaire :

   ```sql
   SELECT CASE
       WHEN SUBSTR(hrmn, 1, 2) BETWEEN '06' AND '12' THEN 'Matin'
       WHEN SUBSTR(hrmn, 1, 2) BETWEEN '12' AND '18' THEN 'Après-midi'
       ELSE 'Soir/Nuit'
   END AS Periode, COUNT(*) AS Nombre_Accidents
   FROM accident_velo
   GROUP BY Periode;
   ```

9. Nombre d’accidents par département :

   ```sql
   SELECT dep, COUNT(*) AS Nombre_Accidents FROM accident_velo GROUP BY dep ORDER BY Nombre_Accidents DESC;
   ```

On pourra regarder le fichier `exec.py` pour voir le resultat de c'est requetes.

## Partie 3

### Activité 2

1. Les atributs les plus utiles seront `lat` et `long` qui vont nous permettre de placer les points sur la cartes.

2. si on veut afficher l’identifiant de l’accident, le département, la latitude et la longitude la methode la plus simple doit etre de fiare ainsi :

``` sql
SELECT Num_Acc, dep, lat, long
FROM accident_velo;

```

3. Plusieurs probleme sont a relevées :
   - doublons
   - Coordonées non valides
   - Quantités de données

4.

```python
import sqlite3


FICHIER_BDD = "accidents.db" 
connexion_BD = sqlite3.connect(FICHIER_BDD)
c = connexion_BD.cursor()



MA_REQUETE = "SELECT * FROM accidentsVelo"  
c.execute(MA_REQUETE)

liste_data = c.fetchall()
print("J’ai {} enregistrements dans ma base de données.".format(len(liste_data)))

connexion_BD.close()
```

5.

6.

7.

9.

10. Sa ne se positionne pas au bon endroit ou il y a une erreurs

11. Le petit probleme c'est que ya beacoup d'accidents mais un code bien fait ne fait pas planter la page.