import requests
import folium
import time


url = "http://api.open-notify.org/iss-now.json"

def trace_ISS(number_of_points, wait_time):
    points = []  # List to store ISS positions

    for i in range(number_of_points):
        # Fetch the current position of ISS
        position = requests.get(url).json()
        
        # Extract latitude and longitude
        latitude = position['iss_position']['latitude']
        longitude = position['iss_position']['longitude']
        
        # Convert to float and store as a tuple
        point_coordinates = (float(latitude), float(longitude))
        points.append(point_coordinates)
        
        
        map_iss = folium.Map(location=point_coordinates, zoom_start=5)
        
        
        folium.Marker(
            location=point_coordinates,
            popup="Latitude: {:.6f}, Longitude: {:.6f}".format(float(latitude), float(longitude)),
            tooltip="ISS"
        ).add_to(map_iss)

        print(f"Point {i + 1}: {point_coordinates}")

        
        time.sleep(wait_time)

    # Draw a line connecting all recorded points
    folium.PolyLine(points, color='blue').add_to(map_iss)
    
    # Save the map to an HTML file
    map_iss.save(outfile='position_Iss-20.html')

# Call the function to trace the ISS
trace_ISS(3, 10)  # Get 3 points, waiting 10 seconds between each
