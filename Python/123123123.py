#DAMENIK THAQI
#DAMENIK.THAQI50@myhunter.CUNY.EDu


import folium
import pandas as pd

inputFile = input("Enter CSV file name: ")
outputFile = input("Enter output file: ")

collisions = pd.read_csv(inputFile)

mapCollisions = folium.Map(location=[40.768731, -73964915], tiles="Cartodb Positron")

for index,row in collisions.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["BOROUGH"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCollisions)

mapCollisions.save(outfile=outputFile)