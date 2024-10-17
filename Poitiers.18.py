import folium

# Coordinates of Poitiers to center the map
CENTRE_POITIERS = [46.580224, 0.340375]
B24_COORDINATES = [46.580102, 0.341056]  # Build B24
SP2MI_COORDINATES = [46.669108, 0.338011]  # Build Sp2mi

# Create the map center on Poitiers
map_poitiers = folium.Map(location=CENTRE_POITIERS, zoom_start=12)

# Add markers for the build
folium.Marker(
    location=B24_COORDINATES,
    popup="Building B24 - Bachelor's in Computer Science",
    tooltip="Campus of Poitiers - B24"
).add_to(map_poitiers)

folium.Marker(
    location=SP2MI_COORDINATES,
    popup="Building Sp2mi - Master's in Computer Science",
    tooltip="Futuroscope Campus - Sp2mi"
).add_to(map_poitiers)
map_poitiers
