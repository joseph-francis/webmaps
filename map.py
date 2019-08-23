import folium
import pandas

map_val = folium.Map(location=[29.548428, -95.522724])  # tiles="Stamen Terrain", zoom_start=2

fg = folium.FeatureGroup(name="Volcanoes")
fg_population = folium.FeatureGroup("Population")


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

fg_population.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x: {"fillColor": "blue" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))
map_val.add_child(fg)
map_val.add_child(fg_population)
map_val.add_child(folium.LayerControl())
map_val.save("Map1.html")
