import requests

# Constantes
CHEMIN_FICHIER_SOURCE = "text.txt"
CHEMIN_FICHIER_TRADUIT = "text_traduit.txt"
URL_API = "https://libretranslate.de/translate"

def traduire_fichier():
    # Demande langue cible
    langue_cible = input("Saisir la langue dans laquelle traduire le texte (en, fr, es, de) : ").strip()
    
    # Ouverture pour lecture
    with open(CHEMIN_FICHIER_SOURCE, 'r', encoding='utf-8') as fichier:
        texte_a_traduire = fichier.read()

    # Paramètres à envoyer à l'API
    payload = {
        "q": texte_a_traduire,
        "source": "auto",  # Utilise la detection automatique de l'API
        "target": langue_cible,
        "format": "text"
    }

    
    response = requests.post(URL_API, json=payload)

    
    translation = response.json()
    texte_traduit = translation['translatedText']
    
    # Sauvegarde du texte traduit
    with open(CHEMIN_FICHIER_TRADUIT, 'w', encoding='utf-8') as fichier_traduit:
        fichier_traduit.write(texte_traduit)
    
    print(f"Le fichier traduit a été sauvegardé sous : {CHEMIN_FICHIER_TRADUIT}")


# traduire_fichier() # Decommenter pour appeler la fonction
