import requests

url_places = "https://data.angers.fr/api/records/1.0/search/?dataset=parking-angers&rows=1000"


response = requests.get(url_places)

data = response.json()
    
for record in data['records']:
    nom_parking = record['fields']['nom']
    places_restantes = record['fields']['disponible']
        
    print(f"Parking: {nom_parking}, Places restantes: {places_restantes}")

