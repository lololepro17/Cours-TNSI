# Reponse au questions de l'exercice 3

## Question 14

- Les données sont envoyées dans l'URL sous forme de paramètres de requête. Par exemple : `https://exemple.com/api?param1=valeur1&param2=valeur2`

- Les données sont envoyées dans le corps de la requête HTTP

## Question 15

- L'URL à contacter est : `POST https://libretranslate.de/translate`.
- Les parametre sont :
  - `q`:le texte a traduire
  - `source`:la langue source du texte ("fr" pour francais)
  - `target`:langue cible dans laquel traduire ("en" pour anglais)
  - `format`(optionel):le format du text. Par default, c'est `text`.

## Question 16

Il faut utiliser `.post()`. Il faut mettre en argument soit `data` pour mettre un formulaire de données soit `json` pour un json (example: `requests.post(url, data={
    "param1": "value1",
    "param2": "value2"
})`)