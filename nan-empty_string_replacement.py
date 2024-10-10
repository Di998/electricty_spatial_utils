import json
import pandas as pd

# Load the GeoJSON file
with open('/Users/di/Desktop/new-layers/transformed.geojson', 'r') as file:
    geojson_data = json.load(file)

# Function to replace NaN and empty strings with null (None in Python) in properties
def replace_nan_and_empty_with_null(data):

    for feature in data['features']:
        properties = feature['properties']
        for key, value in properties.items():
            if pd.isna(value) or value == "":
                properties[key] = None
    return data

# Replace NaN values and empty strings
updated_geojson = replace_nan_and_empty_with_null(geojson_data)

# Save the modified GeoJSON to a new file
with open('substations_null.geojson', 'w') as file:
    json.dump(updated_geojson, file, indent=2)

print("NaN values and empty strings have been replaced with null and saved to 'substations_null.geojson'.")
