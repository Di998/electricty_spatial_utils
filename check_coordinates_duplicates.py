import json

def check_for_duplicate_coordinates(input_file):
    # Load the input GeoJSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Check if the GeoJSON has 'features' key
    if 'features' not in data:
        raise ValueError("Invalid GeoJSON format: No 'features' key found.")
    
    coordinates_set = set()
    duplicates = set()
    
    # Check for duplicates in the 'coordinates' field
    for feature in data['features']:
        coords = feature.get('geometry', {}).get('coordinates')
        if coords is None:
            print("Feature with missing 'coordinates':", feature)
            continue
        
        coords_tuple = tuple(coords)  # Convert list to tuple for immutability
        if coords_tuple in coordinates_set:
            duplicates.add(coords_tuple)
        else:
            coordinates_set.add(coords_tuple)
    
    if duplicates:
        print("Duplicate coordinates found:")
        for coord in duplicates:
            print(coord)
    else:
        print("No duplicate coordinates found.")

# Replace 'input.geojson' with your file path
input_geojson_file = '/Users/di/Desktop/new-layers/Terminal_Points_(USACE_IENC).geojson'

check_for_duplicate_coordinates(input_geojson_file)
