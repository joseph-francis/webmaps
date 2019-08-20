import folium
import pandas

map_val = folium.Map(location=[29.548428, -95.522724])  # tiles="Stamen Terrain", zoom_start=2

fg = folium.FeatureGroup(name="My Map")


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lng = list(data["LON"])
elev = list(data["ELEV"])

for (lat, lng, elv) in zip(lat, lng, elev):
    fg.add_child(
        folium.Marker(location=[lat, lng], popup=elv, icon=folium.Icon(color=color_producer(elv))))

map_val.add_child(fg)

map_val.save("Map1.html")
