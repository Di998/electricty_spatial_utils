import json

# Function to read GeoJSON from a file and print feature IDs and object IDs
def print_feature_and_object_ids(file_path):
    with open(file_path, 'r') as file:
        geojson_data = json.load(file)
        
        for feature in geojson_data['features']:
            feature_id = feature.get('id')
            object_id = feature['properties'].get('OBJECTID')  # Adjust property name as needed
            print(f"Feature ID: {feature_id}, Object ID: {object_id}")

# Path to your GeoJSON file
file_path = '/Users/di/Desktop/new-layers/i.geojson'
# Call the function
print_feature_and_object_ids(file_path)
