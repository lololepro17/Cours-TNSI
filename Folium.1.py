# on importe le module folium
import folium
# on définit un point géographique par ses coordonnées # longitude et lattitude
coords = (45.44382507842071, -0.4293109318192264)
# on crée une carte centrée sur ce point géographique
map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=8)
# on considère un nouveau point
coords = (45.44218002519302, -0.4319353335565319)
# on ajoute un marqueur correspondant à ce point sur la carte
folium.Marker(location=coords, popup = "Lycée Polyvalent Jean Hippolyte").add_to(map)
# on considère un nouveau point
coords = (45.271025079552146, -0.3935992163742874)
# on ajoute un marqueur correspondant à ce point sur la carte
folium.Marker(location=coords, popup = "Freemusic Festival").add_to(map)
# on sauvegarde la carte dans notre dossier sous la forme # d'un fichier html
# map.save(outfile='map.html')
# map