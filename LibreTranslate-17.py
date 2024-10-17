import requests

def traduire_texte():
    # Demande la langue source
    langue_source = input("Saisir la langue du texte à traduire (en, fr, es, de, auto (pour détection automatique)) : ").strip()
    
    # Demande la langue cible
    langue_cible = input("Saisir la langue dans laquelle traduire le texte (en, fr, es, de) : ").strip()
    
    # Demande le texte à traduire
    texte_a_traduire = input("Saisir le texte à traduire : ")

    # URL de l'API de traduction
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
        # Extraction du texte traduit
        translation = response.json()
        print(f"Voici la traduction : {translation['translatedText']}")
    else:
        print(f"Erreur: {response.status_code}")
        print(response.text)  # Affiche le texte brut de la réponse pour plus d'infos

# Appel de la fonction de traduction
traduire_texte()

