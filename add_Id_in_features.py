import json

def add_ids_to_geojson(input_file, output_file):
    # Load the input GeoJSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Check if the GeoJSON has 'features' key
    if 'features' not in data:
        raise ValueError("Invalid GeoJSON format: No 'features' key found.")
    
    # Add 'id' to each feature, placing it right after 'type'
    for index, feature in enumerate(data['features']):
        # Create a new feature dictionary with 'id' right after 'type'
        feature_with_id = {
            'type': feature['type'],
            'id': index + 1,
            **{k: feature[k] for k in feature if k != 'type'}
        }
        # Update the feature in the list
        data['features'][index] = feature_with_id
    
    # Write the modified GeoJSON to the output file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Processed GeoJSON with IDs saved to {output_file}")

# Replace 'input.geojson' and 'output.geojson' with your file paths
input_geojson_file = '/Users/di/Desktop/new-layers/CoastalCriticalHabitatDesignations.geojson'
output_geojson_file = 'output1.geojson'

add_ids_to_geojson(input_geojson_file, output_geojson_file)
