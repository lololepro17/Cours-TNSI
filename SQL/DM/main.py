# Importdumodule
import sqlite3
 # CONSTANTE
 # Connexion à la Base de données table.sqlite3
connexion_BD =sqlite3.connect("accidentsVelo.sqlite3")
c = connexion_BD.cursor()


c.execute("SELECT name FROM sqlite_master WHERE type='table';")
liste_data = c. fetchall() #Récupération des résultats de la requête sour forme de liste
print("J’ai {} enregistrements dans ma base de données.".format(len(liste_data )))