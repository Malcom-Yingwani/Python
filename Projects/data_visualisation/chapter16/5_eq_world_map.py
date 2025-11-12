from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python Object.

path = Path("eq_data/eq_data_30_day_m1.geojson")
contents = path.read_text(encoding = "utf-8")
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path("eq_data/readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data, indent = 4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]
# print(len(all_eq_dicts))

mags, lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    eq_title = eq_dict["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)
# Plot 
title = "Global Earthquakes"
fig = px.scatter_geo(lat = lats, lon = lons, size = mags, title = title,
color = mags,
color_continuous_scale = "Viridis",
labels = {"color": "Magnitude"},
projection = "natural earth",
hover_name = eq_titles,
)

fig.show()


# =====================================================================================================
# Chat GPT SUMMARY
# =====================================================================================================
# Purpose:
#   - Visualizes global earthquake data on an interactive world map using Plotly.
# =====================================================================================================
# Core Functionality:
#   - Reads earthquake data from a GeoJSON file (eq_data_30_day_m1.geojson).
#   - Extracts magnitudes, longitudes, latitudes, and titles for each earthquake.
#   - Saves a formatted (readable) version of the GeoJSON data for inspection.
# =====================================================================================================
# Visualization:
#   - Uses plotly.express.scatter_geo() to plot earthquakes on a "natural earth" projection.
#   - Marker size and color reflect earthquake magnitude.
#   - Employs the "Viridis" color scale and shows titles on hover.
# =====================================================================================================
# Output:
#   - Displays an interactive world map titled “Global Earthquakes”.
# =====================================================================================================
