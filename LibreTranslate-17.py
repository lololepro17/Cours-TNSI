import requests

def traduire_texte():
    
    langue_source = input("Saisir la langue du texte à traduire (en, fr, es, de, auto (pour détection automatique)) : ").strip()
    
    
    langue_cible = input("Saisir la langue dans laquelle traduire le texte (en, fr, es, de) : ").strip()
    
    
    texte_a_traduire = input("Saisir le texte à traduire : ")

    
    url = "https://libretranslate.de/translate"
    payload = {
        "q": texte_a_traduire,
        "source": langue_source,
        "target": langue_cible,
        "format": "text"
    }

    # Envoi de la requête POST à l'API
    response = requests.post(url, json=payload)

    # Vérification du code de statut de la réponse
    if response.status_code == 200:
        
        translation = response.json()
        print(f"Voici la traduction : {translation['translatedText']}")
    else:
        print(f"Erreur: {response.status_code}")
        print(response.text) 


# traduire_texte() #Decommenter pour appeler la fonction

