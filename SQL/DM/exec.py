import sqlite3
import csv

def executer_commande_sql(connexion, requete, params=None):
    """
    Exécute une commande SQL sur une connexion SQLite donnée.

    :param connexion: Connexion SQLite.
    :param requete: Requête SQL à exécuter.
    :param params: Paramètres pour la requête (tuple ou None).
    :return: Liste des résultats si applicable.
    """
    try:
        curseur = connexion.cursor()
        if params:
            curseur.execute(requete, params)
        else:
            curseur.execute(requete)
        return curseur.fetchall()
    except sqlite3.Error as e:
        print(f"Erreur SQL : {e}")
        return None

# Connexion à une base de données en mémoire
connexion = sqlite3.connect(":memory:")

# Création de la table accident_velo
connexion.execute("""
CREATE TABLE IF NOT EXISTS accident_velo (
    Num_Acc INTEGER,
    date TEXT,
    an INTEGER,
    dep TEXT,
    grav TEXT,
    hrmn TEXT,
    jour TEXT,
    lat REAL,
    long REAL
);
""")

# Chargement des données depuis le fichier CSV
fichier_csv = "accidentsVelo.csv"
with open(fichier_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            lat, long = row['lat'], row['long']
            if -90 <= float(lat) <= 90 and -180 <= float(long) <= 180:
                connexion.execute(
                    "INSERT INTO accident_velo VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        int(row['Num_Acc']),
                        row['date'],
                        int(row['date'][:4]),  # Extrait l'année de la date
                        row['dep'].strip(),
                        row['grav'],
                        row['hrmn'],
                        row['jour'],
                        float(lat),
                        float(long)
                    )
                )
        except ValueError:
            continue

# Exécution des différentes requêtes SQL
requete_1 = "SELECT COUNT(*) AS Nombre_Accidentés FROM accident_velo"
c = executer_commande_sql(connexion, requete_1)
print("Nombre total d’accidentés sur la période : ", c)

requete_2 = "SELECT COUNT(DISTINCT Num_Acc) AS Nombre_Accidents FROM accident_velo"
c = executer_commande_sql(connexion, requete_2)
print("Nombre total d’accidents sur la période : ", c)

requete_3 = "SELECT COUNT(*) AS Nombre_Accidentés FROM accident_velo WHERE dep = '69'"
c = executer_commande_sql(connexion, requete_3)
# print("Nombre d’accidentés dans le département du Rhône : ", c)

requete_4 = "SELECT COUNT(*) AS Nombre_Accidents_Mortels FROM accident_velo WHERE dep = '69' AND grav = '3'"
c = executer_commande_sql(connexion, requete_4)
# print("Nombre d’accidents avec décès de cyclistes dans le Rhône : ", c)

requete_5 = "SELECT date, jour FROM accident_velo WHERE dep = '69' AND grav = '3' ORDER BY jour"
c = executer_commande_sql(connexion, requete_5)
# print("Dates et jours des accidents mortels dans le Rhône : ", c)

requete_6 = "SELECT * FROM accident_velo ORDER BY dep DESC"
c = executer_commande_sql(connexion, requete_6)
# print("Classement des données par département : ", c)

requete_7 = """
SELECT CASE
    WHEN SUBSTR(hrmn, 1, 2) BETWEEN '06' AND '12' THEN 'Matin'
    WHEN SUBSTR(hrmn, 1, 2) BETWEEN '12' AND '18' THEN 'Après-midi'
    ELSE 'Soir/Nuit'
END AS Periode, COUNT(*) AS Nombre_Accidents
FROM accident_velo
GROUP BY Periode
"""
c = executer_commande_sql(connexion, requete_7)
# print("Accidents selon l’horaire : ", c)

requete_8 = "SELECT dep, COUNT(*) AS Nombre_Accidents FROM accident_velo GROUP BY dep ORDER BY Nombre_Accidents DESC"
c = executer_commande_sql(connexion, requete_8)
print("Nombre d’accidents par département : ", c)

requete_9 = """
SELECT Num_Acc, dep, lat, long 
FROM accident_velo;
"""
c = executer_commande_sql(connexion,requete_9)
# print("Question 3.2.3 : ", c)

# Fermeture de la connexion
connexion.close()
