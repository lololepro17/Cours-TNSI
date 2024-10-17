import requests
import folium


url = "http://api.open-notify.org/iss-now.json"


donnees_ISS = requests.get(url).json()


print(type(donnees_ISS))
print(donnees_ISS)


latitude = float(donnees_ISS['iss_position']['latitude'])
longitude = float(donnees_ISS['iss_position']['longitude'])


map_iss = folium.Map(location=[latitude, longitude], zoom_start=4)


folium.Marker(
    location=[latitude, longitude],
    popup="Latitude: {:.6f}, Longitude: {:.6f}".format(latitude, longitude),
    tooltip="ISS"
).add_to(map_iss)

# Draw a circle around the ISS position for represent the area overflown
folium.Circle(
    location=[latitude, longitude],
    radius=500000,  # 500 km radius (adjust as you need)
    color='blue',
    fill=True,
    fill_opacity=0.2,
    tooltip="Area Overflown by ISS"
).add_to(map_iss)

# Display the map (for a Jupyter Notebook) or save it as HTML
# map_iss # Uncomment for Notebook
map_iss.save("iss_position-19.2.html")  # Uncomment to save the map as an HTML file
