import json

def update_geojson(input_file, output_file):
    # Open and read the GeoJSON file
    with open(input_file, 'r') as file:
        geoJSON_data = json.load(file)

    # Iterate through each feature and update the 'id' and 'OBJECTID'
    for index, item in enumerate(geoJSON_data['features']):
        # Set 'id' and 'OBJECTID'
        item['id'] = index + 1
        if 'properties' not in item:
            item['properties'] = {}
        item['properties']['OBJECTID'] = index + 1
        
        # Reorder properties to ensure 'OBJECTID' is first
        properties = item['properties']
        ordered_properties = {'OBJECTID': properties.pop('OBJECTID')}
        ordered_properties.update(properties)
        item['properties'] = ordered_properties

        # Ensure 'geometry' is correctly placed
        item['geometry'] = item.pop('geometry', {})

    # Write the updated GeoJSON back to a file
    with open(output_file, 'w') as file:
        json.dump(geoJSON_data, file, indent=2)

    print('Dataset converted successfully!')

# Example usage
update_geojson('/Users/di/Desktop/new-layers/transformed.geojson', 'i.geojson')
