'''
Plotting Global Fire Activity
Michael Jolley
This code reads a CVS file and plots the first 1000 records of the global fire activity.
'''
import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# --- Step 1: Read the CSV file ---
filename = 'world_fires_1_day.csv'

lons, lats, brights, hover_texts = [], [], [], []

with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    # Find the index of needed columns for flexibility
    date_index = header_row.index("acq_date")
    lat_index = header_row.index("latitude")
    lon_index = header_row.index("longitude")
    bright_index = header_row.index("brightness")

    count = 0
    for row in reader:
        if count >= 1000:
            break  # Limit to first 1000 records
        try:
            brightness = float(row[bright_index])
            lon = float(row[lon_index])
            lat = float(row[lat_index])
            date = row[date_index]
        except (ValueError, IndexError):
            continue  # Skip bad data
        else:
            brights.append(brightness)
            lons.append(lon)
            lats.append(lat)
            hover_texts.append(date)
            count += 1

# --- Step 2: Create the visualization ---
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [0.05 * b for b in brights],  # Scale brightness for marker size
        'color': brights,
        'colorscale': 'Bluered',
        'colorbar': {'title': 'Brightness'},
    }
}]

my_layout = Layout(title='Global Fire Activity – First 1000 Records')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
