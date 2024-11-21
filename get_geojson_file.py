import requests
import json

# Define the base URL for the query
url = 'https://ienccloud.us/arcgis/rest/services/IENC_Feature_Classes/SHORELINE_CONSTRUCTION_POINT/MapServer/0/query'

# Parameters for the request
params = {
    'outFields': '*',
    'where': '1=1',
    'f': 'geojson',
    'resultOffset': 0,         # Start from the first record
    'resultRecordCount': 1000  # Fetch 1000 records per request (adjust if needed)
}

# Initialize variables for pagination and storing features
all_features = []

# Loop through paginated results
while True:
    # Send a GET request with pagination
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Load the GeoJSON response into a Python dictionary
        data = response.json()

        # Collect the features from the response
        features = data.get('features', [])
        all_features.extend(features)

        # Print progress
        print(f"Downloaded {params['resultOffset']} to {params['resultOffset'] + params['resultRecordCount']} records.")

        # If no more features are returned, exit the loop
        if len(features) == 0:
            print("No more data to fetch.")
            break

        # Update the offset to fetch the next batch
        params['resultOffset'] += params['resultRecordCount']
    else:
        # If the request fails, stop the process and show an error message
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        break

# Combine all the features into a single GeoJSON FeatureCollection
geojson_data = {
    "type": "FeatureCollection",
    "features": all_features
}

# Save the combined GeoJSON data to a file
output_file = 'o.geojson'
with open(output_file, 'w') as file:
    json.dump(geojson_data, file)

print("GeoJSON file has been downloaded and combined successfully.")

