import json

fichier = open("BobAndFriends.json")  # ouverture du flux de lecture
contenu = json.load(fichier)  # mémorisation du fichier json dans le dictionnaire `contenu`
fichier.close()  # on ferme le flux de lecture

type(contenu)

print(contenu)

print(contenu["favoriteNumber"])
print(contenu["hobbies"])
print(contenu["hobbies"]["music"][1])