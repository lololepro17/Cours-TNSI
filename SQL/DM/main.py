import sqlite3
import folium
from folium.plugins import MarkerCluster
import csv

# CONSTANTES
FICHIER_CSV = "accidentsVelo.csv"
FICHIER_BDD = "accidents.db"
TABLE = "accidents"
DEPARTEMENT_CIBLE = "64"

def creation_carte(location:tuple, zoom_start:int):
    """
    Crée une carte centrée sur un point avec un niveau de zoom donné et y ajoute les marqueurs d'accidents.
    
    :param location: Tuple (latitude, longitude) pour centrer la carte.
    :param zoom_start: Entier pour le niveau de zoom de départ (entre 1 et 19).
    :return: La carte générée sous forme d'objet Folium.
    """
    # Connexion à la Base de données SQLite
    connexion_BD = sqlite3.connect(FICHIER_BDD)
    c = connexion_BD.cursor()

    # Extraire les données par département
    MA_REQUETE = f"""
    SELECT Num_Acc, date, grav, typevehicules, lat, long 
    FROM {TABLE}
    WHERE dep = ?
    """
    c.execute(MA_REQUETE, (DEPARTEMENT_CIBLE,))
    data = c.fetchall()

    print(f"J’ai {len(data)} enregistrements dans ma base de données.")

    # Préparer les coordonnées et supprimer les doublons
    coordonnees_utilisees = set()
    data_unique = []
    for accident in data:
        try:
            lat, long = round(accident[4], 4), round(accident[5], 4)
            
            # Vérification si les coordonnées sont valides et non nulles
            if -90 <= lat <= 90 and -180 <= long <= 180 and (lat, long) != (0.00, 0.00):
                if (lat, long) not in coordonnees_utilisees:
                    coordonnees_utilisees.add((lat, long))
                    data_unique.append(accident)
            else:
                print(f"Coordonnées invalides ou nulles pour l'accident #{accident[0]} : ({lat}, {long})")
        except ValueError:
            print(f"Erreur de conversion des coordonnées pour l'accident #{accident[0]}")
            continue

    # Centrer la carte sur la moyenne des positions valides
    if data_unique:
        latitude_moyenne = sum(acc[4] for acc in data_unique) / len(data_unique)
        longitude_moyenne = sum(acc[5] for acc in data_unique) / len(data_unique)
    else:
        latitude_moyenne, longitude_moyenne = location  # Location de depart si aucune n'est valide

    # Générer la carte
    m = folium.Map(location=[latitude_moyenne, longitude_moyenne], zoom_start=zoom_start)

    # Ajouter les tuiles OpenStreetMap avec le ©
    folium.TileLayer(
        'OpenStreetMap',
        attr='© Contributeurs OpenStreetMap'
    ).add_to(m)

    marker_cluster = MarkerCluster().add_to(m)

    # Ajouter les marqueurs pour tout accident valide 
    for accident in data_unique:
        folium.Marker(
            location=[accident[4], accident[5]],
            popup=(f"Numéro d'accident: {accident[0]}<br>"
                   f"Date: {accident[1]}<br>"
                   f"Sinétique: {accident[2]}<br>"
                   f"Type de véhicule: {accident[3]}<br>"
                   f"Position: ({accident[4]}, {accident[5]})"),
            tooltip=f"Accident #{accident[0]}"
        ).add_to(marker_cluster)

    # Sauvegarder la carte en HTML
    NOM_FICHIER = f"carte_accidents_dep_{DEPARTEMENT_CIBLE}.html"
    m.save(NOM_FICHIER)
    print(f"Carte générée : {NOM_FICHIER}")

    # Nettoyer et fermer la base
    connexion_BD.close()

# Appek de la fonction avec un point de depart et un zoom
creation_carte(location=(46.396, 2.505), zoom_start=8)
