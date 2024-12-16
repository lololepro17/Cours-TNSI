import sqlite3
import folium

# Connexion à la base de données
conn = sqlite3.connect('table.sqlite3')
cursor = conn.cursor()

# Vérification des tables existantes
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables disponibles :", cursor.fetchall())

# Exemple de requête pour récupérer les données nécessaires
query = """
SELECT field1 AS Num_Acc, field2 AS dep, field9 AS lat, field10 AS long
FROM accidentsVelo
WHERE field9 IS NOT NULL AND field10 IS NOT NULL;
"""

cursor.execute(query)
accidents = cursor.fetchall()
print(f"Nombre d'accidents récupérés : {len(accidents)}")

# Création de la carte avec Folium
carte = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

# Ajout de marqueurs pour chaque accident
for accident in accidents:
    num_acc, dep, lat, long = accident
    folium.Marker(
        location=[float(lat), float(long)],  # Conversion en float si nécessaire
        popup=f"Accident {num_acc} - Département {dep}",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(carte)

# Sauvegarde de la carte
carte.save("carte_accidents.html")
print("Carte générée : carte_accidents.html")

# Fermeture de la connexion
conn.close()
