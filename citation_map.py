import folium
import pandas as pd
from geopy.geocoders import GoogleV3
from folium.plugins import MarkerCluster

# Load data from Excel
df = pd.read_excel('final_list.xlsx')

# Create a map object
map = folium.Map(location=[0, 0], zoom_start=2)

# Set up Google Maps Geocoding API
geolocator = GoogleV3(api_key='AIzaSyAtDWKCbDURsdfxGScmPuFH9A9jCNF8X5A')

# Add markers to the map
marker_cluster = MarkerCluster().add_to(map)

for index, row in df.iterrows():
    address = row['University']
    popup = "Title: "
    popup += row['Title']
    popup += ", University: "
    popup += address
    
    location = geolocator.geocode(address)
    if location:
        lat = location.latitude
        lon = location.longitude
        
        marker = folium.Marker(location=[lat, lon], popup=popup)
        marker.add_to(marker_cluster)

# Save the map as an HTML file
map.save('Citation_Map.html')