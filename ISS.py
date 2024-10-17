import requests
import folium


url = "http://api.open-notify.org/iss-now.json"


donnees_ISS = requests.get(url).json()


print(type(donnees_ISS))
print(donnees_ISS)

# Extract latitude and longitude from the JSON
latitude = float(donnees_ISS['iss_position']['latitude'])
longitude = float(donnees_ISS['iss_position']['longitude'])

# Create a map centered on the current position of the ISS
map_iss = folium.Map(location=[latitude, longitude], zoom_start=3)

# Add a marker for the position of the ISS
folium.Marker(
    location=[latitude, longitude],
    popup="Latitude: {:.6f}, Longitude: {:.6f}".format(latitude, longitude),
    tooltip="ISS"
).add_to(map_iss)

# Display the map (for a Jupyter Notebook) or save it as HTML
# map_iss # Uncomment to visualize in a Notebook
# map_iss.save("iss_position.html")  # Uncomment to save the map as an HTML file
