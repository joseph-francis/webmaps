import folium

map_val = folium.Map(location=[29.548428, -95.522724])  # tiles="Stamen Terrain", zoom_start=2

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[29.548428, -95.522724], popup="This marker be like..", icon=folium.Icon(color="green")))
map_val.add_child(fg)

map_val.save("Map1.html")

