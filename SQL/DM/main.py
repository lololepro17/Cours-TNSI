import sqlite3
import folium
from folium import Icon
import math

# CONSTANTES
FICHIER_BDD = "accidents.db"
TABLE = "accidents"
DEPARTEMENT_CIBLE = "46"
RAYON_MAX = 150  # Distance max en kilomètres

def dis(coord1, coord2):
    """
    Calcul la distance entre deux point.
      coord1 : bool de coordonnées
      coord2 : bool de coordonnées
    """
    R = 6371  # Rayon de la Terre en km
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def creation_carte(location: tuple, zoom_start: int):
    
    # Connexions a la bases de données 
    connexion_BD = sqlite3.connect(FICHIER_BDD)
    c = connexion_BD.cursor()
    
    # Recuperation des données dans la base 
    MA_REQUETE = f"""
    SELECT Num_Acc, date, grav, typevehicules, lat, long 
    FROM {TABLE}
    WHERE dep = ?
    """
    c.execute(MA_REQUETE, (DEPARTEMENT_CIBLE,))
    data = c.fetchall()

    print(f"J’ai {len(data)} enregistrements dans ma base de données.")

    coordonnees_utilisees = set() # Utilisation d'un ensemble pour zevitez les doublons.
    data_unique = []
    # Verification que les coordonnées soit sur terres et non nul.
    for accident in data:
        try:
            lat, long = round(accident[4], 4), round(accident[5], 4)
            if -90 <= lat <= 90 and -180 <= long <= 180 and (lat, long) != (0.00, 0.00):
                if (lat, long) not in coordonnees_utilisees:
                    coordonnees_utilisees.add((lat, long))
                    data_unique.append(accident)
            else:
                print(f"Coordonnées invalides ou nulles pour l'accident #{accident[0]} : ({lat}, {long})")
        except ValueError:
            print(f"Erreur de conversion des coordonnées pour l'accident #{accident[0]}")
            continue

    # Calcul des coordonnées moyenne pour pouvoir centrer notre carte dessus.
    if data_unique:
        latitude_moyenne = sum(acc[4] for acc in data_unique) / len(data_unique)
        longitude_moyenne = sum(acc[5] for acc in data_unique) / len(data_unique)
        centre = (latitude_moyenne, longitude_moyenne)

    # Supression des points trop de loin de notre dep.
        data_filtre = []
        for accident in data_unique:
            distance = dis(centre, (accident[4], accident[5]))
            if distance <= RAYON_MAX:
                data_filtre.append(accident)
            else:
                print(f"Accident #{accident[0]} supprimé : distance {distance:.2f} km")
    else:
        latitude_moyenne, longitude_moyenne = location
        centre = location
        data_filtre = []

    # Création d'une carte m centrer sur notre position moyennes des points et rajouts des copyrigt en Layer.
    m = folium.Map(location=[latitude_moyenne, longitude_moyenne], zoom_start=zoom_start)
    folium.TileLayer('OpenStreetMap', attr='© Contributeurs OpenStreetMap').add_to(m)

    # Ajout d'une couleur en fonction de la gravité de l'accidents.
    for accident in data_filtre:
        gravite = accident[2]
        if int(gravite) <= 1:
            couleur = "green"
        elif 1 < int(gravite) <= 2:
            couleur = "blue"
        elif 2 < int(gravite) <= 3:
            couleur = "orange"
        else:
            couleur = "red"

        # Affichage des info sur l'accidents dans le marker.
        folium.Marker(
            location=[accident[4], accident[5]],
            popup=(f"Numéro d'accident: {accident[0]}<br>"
                   f"Date: {accident[1]}<br>"
                   f"Gravité: {gravite}%<br>"
                   f"Type de véhicule: {accident[3]}<br>"
                   f"Position: ({accident[4]}, {accident[5]})"),
            tooltip=f"Accident #{accident[0]} - Gravité: {gravite}%",
            icon=Icon(color=couleur, icon="info-sign")
        ).add_to(m)

    # Marker au centre 
    folium.Marker(
        location=[latitude_moyenne, longitude_moyenne],
        popup=f"Centre des accidents : ({latitude_moyenne}, {longitude_moyenne})",
        icon=Icon(color="purple", icon="star")
    ).add_to(m)

    # Enregistrement de notre carte dans le dossier courant 
    NOM_FICHIER = f".\carte_accidents_dep_{DEPARTEMENT_CIBLE}.html"
    m.save(NOM_FICHIER)
    print(f"Carte générée : {NOM_FICHIER}")

    connexion_BD.close()

creation_carte(location=(46.396, 2.505), zoom_start=8)
