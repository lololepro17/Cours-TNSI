import requests
from datetime import datetime


URL_PLACES = "https://data.angers.fr/api/records/1.0/search/?dataset=parking-angers&rows=1000"

def obtenir_donnees_parking():
    response = requests.get(URL_PLACES)
    data = response.json()
    return data['records']

def générer_tableau_parkings():
    donnees_parkings = obtenir_donnees_parking()
    
    # Création de la page HTML pour le tableau
    html_content = """
    <html>
    <head><title>Tableau des parkings d'Angers</title></head>
    <body>
        <h1>Tableau des parkings d'Angers</h1>
        <table border="1">
            <tr>
                <th>Nom du parking</th>
                <th>Places restantes</th>
                <th>Heure de mise à jour</th>
            </tr>
    """
    
    # Remplissage du tableau
    for record in donnees_parkings:
        nom_parking = record['fields'].get('nom', 'Inconnu')
        places_restantes = record['fields'].get('disponible', 'Inconnu')
        heure_mise_a_jour = record['record_timestamp']
        heure_mise_a_jour = datetime.fromisoformat(heure_mise_a_jour).strftime("%H:%M:%S")
        
        # Ajout des données au tableau
        html_content += f"""
            <tr>
                <td>{nom_parking}</td>
                <td>{places_restantes}</td>
                <td>{heure_mise_a_jour}</td>
            </tr>
        """
    
    # Fermeture du tableau et de la page
    html_content += """
        </table>
    </body>
    </html>
    """
    
    # Sauvegarde du fichier HTML
    with open("tableau_parkings_angers.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Le tableau des parkings a été généré avec succès : tableau_parkings_angers.html")

# générer_tableau_parkings() # Decommenter pour appeler
