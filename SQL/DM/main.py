import folium
import csv
from folium.plugins import MarkerCluster

def coordonnees_valides(lat, long):
    """
    Vérifie si les coordonnées sont valides.
    - lat doit être entre -90 et 90
    - long doit être entre -180 et 180
    """
    try:
        lat = float(lat)
        long = float(long)
        return -90 <= lat <= 90 and -180 <= long <= 180
    except (ValueError, TypeError):
        return False

# Configuration
fichier_csv = "accidentsVelo.csv"  # Remplace par ton chemin
departement_cible = "62"  # Numéro du département à afficher (en tant que chaîne pour correspondre exactement)
data = []

# Charger les données CSV et filtrer par département
with open(fichier_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            # Nettoyer la colonne 'dep' pour s'assurer qu'elle correspond bien
            dep = row['dep'].strip()
            if dep != departement_cible:  # Comparaison stricte
                continue
            
            # Vérifier les coordonnées
            lat = float(row['lat'])
            long = float(row['long'])
            if coordonnees_valides(lat, long):
                data.append({
                    'Num_Acc': row['Num_Acc'],
                    'date': row['date'],
                    'grav': row['grav'],
                    'typevehicules': row['typevehicules'],
                    'lat': lat,
                    'long': long
                })
        except ValueError:
            continue  # Ignorer les lignes avec des erreurs de conversion

# Vérifier si des données valides sont disponibles
if not data:
    raise ValueError(f"Aucune donnée valide trouvée pour le département {departement_cible}.")

# Centrer la carte sur la moyenne des positions valides
latitude_moyenne = sum(d['lat'] for d in data) / len(data)
longitude_moyenne = sum(d['long'] for d in data) / len(data)

# Initialisation de la carte avec clusters
m = folium.Map(location=[latitude_moyenne, longitude_moyenne], zoom_start=8)
marker_cluster = MarkerCluster().add_to(m)

# Ajouter tous les points au cluster
for accident in data:
    folium.Marker(
        location=[accident['lat'], accident['long']],
        popup=(
            f"Numéro d'accident: {accident['Num_Acc']}<br>"
            f"Date: {accident['date']}<br>"
            f"Gravité: {accident['grav']}<br>"
            f"Type de véhicule: {accident['typevehicules']}"
        ),
        tooltip=f"Accident #{accident['Num_Acc']}"
    ).add_to(marker_cluster)

# Sauvegarder la carte en HTML
nom_fichier = f"carte_accidents_dep_{departement_cible}.html"
m.save(nom_fichier)
print(f"Carte générée : {nom_fichier}")
