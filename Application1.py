# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import numpy
import folium
import pandas

#dir(folium)
#help(folium.Map)

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
nm = list(data['NAME'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start = 6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes")

# for coordinates in range(len(lat)):  #my solution
#     #print(coordinates)
#     fg.add_child(folium.Marker(location=[lat[coordinates], lon[coordinates]], popup = nm[coordinates], icon = folium.Icon(color='green')))


for lt, ln, el, names in zip(lat, lon, elev, nm):  #class solution - zip function allows you to go through 2 separate lists element-by-element    
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup = names + ' ' + str(el) + ' m', fill_color = color_producer(el), color = 'grey',
                                     fill_opacity = 0.7, fill = True))


fgp = folium.FeatureGroup(name = "Population")


fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = 'utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000 
                                                      else 'yellow' if 1000000 <=x['properties']['POP2005'] < 20000000 else 'red'}))
# # Creating HTML code  ##
# html = """<h4>Volcano information:</h4>
# Height: %s m
# """
# for lt, ln, el in zip(lat, lon, elev):
#     iframe = folium.IFrame(html=html % str(el), width=200, height=100)
#     fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
 

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")

