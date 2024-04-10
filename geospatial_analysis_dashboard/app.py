import folium
import pandas as pd
import json
import branca

# Load GeoJSON data
state_data = pd.read_csv("data/state_data.csv")
# Load JSON data from file
with open("data/state_geo.json", "r") as file:
    state_geo = json.load(file)

AVAILABLE_TILES = [
    "cartodbpositron",  #By default
    "Stadia.StamenTonerBackground",
    "OpenStreetMap.Mapnik",
    "OpenStreetMap.BZH",   # applicabe
    "OpenTopoMap"  # geophysiscal
    "BasemapAT.highdpi"
    "OpenStreetMap.DE"
]

# Choose the templates from here :
# https://leaflet-extras.github.io/leaflet-providers/preview/


# Create a map
S = folium.Map(location=[48, -102],tiles="OpenStreetMap.DE", zoom_start=3)
#m = folium.Map(tiles="cartodbpositron")

# Choropleth layer
folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
    highlight=True,
    tooltip=folium.features.GeoJsonTooltip(
        fields=["State", "Provinces"],
        aliases=["State", "Provinces"],
        labels=True,
        sticky=True,
    ),
).add_to(S)

# Add state names as markers
# for idx, row in state_data.iterrows():
#     folium.Marker(
#        # location=[row['Latitude'], row['Longitude']],  # Adjust these coordinates based on your data
#         tooltip=row['State'],
#         popup=row['Provinces'],  # Adjust this based on your data
#     ).add_to(S)

# Additional markers and polylines


html = """
    <h1> Rahul Bhoyar Residence</h1><br>
    My dreamhouse in USA.
    <p>
    <code>
        you gonna love this place.
    </code>
    </p>
    """

iframe = branca.element.IFrame(html=html, width=500, height=300)
popup = folium.Popup(iframe, max_width=500)

folium.Marker(
    location=[34.3288, -121.6625],
    tooltip="Pacific Kaveri",
    popup=popup,
    icon=folium.Icon(icon="cloud"),
).add_to(S)

image_name = "home.jpeg"
html = f"""
    <h1> Swapnil Kale Residence</h1><br>
    <img src="{image_name}" alt="Image" style="width:200px;height:200px;">
    Any plot for sale, contact: Swapnil Kale
    <p>
    What a wonderful life in Beverly Hills.
    </p>
    """
folium.Marker(
    location=[34.073, -118.400],
    tooltip="Beverly Hills",
    popup=html,
    icon=folium.Icon(color="lightred"),
).add_to(S)


df = pd.DataFrame(
    data=[["Swapnil", "100 Billion"], ["Rahul", "1000 Billion"],["Astik", "10 Billion"]], columns=["Owner", "Money"]
)



html = df.to_html(
    classes="table table-striped table-hover table-condensed table-responsive"
)

popup = folium.Popup(html)

folium.Marker(location=[40.78, -73.96],
    tooltip="Manhatten Island",
    icon=folium.Icon(color="lightred"), popup=popup).add_to(S)



# Let's create a Figure, with a map inside.
f = branca.element.Figure()
folium.Map([-25, 150], zoom_start=3).add_to(f)

# Let's put the figure into an IFrame.
iframe = branca.element.IFrame(width=500, height=300)
f.add_to(iframe)

# Let's put the IFrame in a Popup
popup = folium.Popup(iframe, max_width=2650)

# Let's create another map.
m = folium.Map([43, -100], zoom_start=4)

# Let's put the Popup on a marker, in the second map.
folium.Marker([30, -100], popup=popup).add_to(S)

# We get a map in a Popup. Not really useful, but powerful.


from altair import Chart

import vega_datasets

# load built-in dataset as a pandas DataFrame
cars = vega_datasets.data.cars()

scatter = (
    Chart(cars)
    .mark_circle()
    .encode(
        x="Horsepower",
        y="Miles_per_Gallon",
        color="Origin",
    )
)

vega_lite = folium.VegaLite(
    scatter,
    width="100%",
    height="100%",
)



marker = folium.Marker([39.73,-104.98])

popup = folium.Popup()

vega_lite.add_to(popup)
popup.add_to(marker)

marker.add_to(S)



#### Adding images on the map

# Image file name
image_name = "dp.jpg"

# HTML content with the image embedded
html = f"""
<h3>Rahul Bhoyar Live Location</h3>
<img src="{image_name}" alt="Image" style="width:200px;height:200px;">"""

# Marker with the HTML content as the popup
berlin_location = [52.52, 13.41]
folium.Marker(berlin_location, popup=html, lazy=True).add_to(S)

# Show the map



# Add the icons


kw = {"prefix": "fa", "color": "green", "icon": "arrow-up"}

angle = 180
icon = folium.Icon(angle=angle, **kw)
folium.Marker(location=[41, -72], icon=icon, tooltip=str(angle)).add_to(S)

angle = 45
icon = folium.Icon(angle=angle, **kw)
folium.Marker(location=[41, -75], icon=icon, tooltip=str(angle)).add_to(S)

angle = 90
icon = folium.Icon(angle=angle, **kw)
folium.Marker([41, -78], icon=icon, tooltip=str(angle)).add_to(S)



# Layer control and title
folium.LayerControl().add_to(S)
title_html = '<h3 align="center" style="font-size:20px"><b>US Unemployment Ratio Colorful</b></h3>'
S.get_root().html.add_child(folium.Element(title_html))

# Save the map
S.save("us_unemployment_data.html")
print("Map created successfully.")
