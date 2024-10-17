import requests

url_languages = "https://libretranslate.com/languages"
response = requests.get(url_languages)
data = response.json()
print(data)

