import json
import csv

# Function to read the CSV file and create a dictionary mapping CENSUSTRAC to Tract_Type
def load_tract_types(csv_file):
    tract_type_map = {}
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tract_type_map[row['CENSUSTRAC']] = row['Tract_Type']
    return tract_type_map

# File paths
geojson_file = '/Users/di/Documents/TechMaven/Tech_Maven_Projects/electricty_spatial_utils/opportunity-zones=8764.-9-10-2019 (1) (1) 2/transformed.geojson'  # Input GeoJSON file
csv_file = '/Users/di/Documents/TechMaven/Tech_Maven_Projects/electricty_spatial_utils/opportunity-zones=8764.-9-10-2019 (1) (1) 2/Opportunitty_Zones - QOZs 14Jun.csv'           # Input CSV file
output_geojson_file = 'updated_geojson.geojson'  # Output GeoJSON file
log_file = 'unmatched_tracts.log'  # Log file for unmatched CENSUSTRAC

# Load the CSV tract data into a dictionary
tract_type_map = load_tract_types(csv_file)

# Open the log file in write mode
with open(log_file, 'w') as log:
    log.write("Unmatched CENSUSTRAC values:\n")
    
    # Read the original GeoJSON file
    with open(geojson_file, 'r') as f:
        geojson_data = json.load(f)

    # Iterate over the features in the GeoJSON
    for feature in geojson_data['features']:
        # Check if the 'CENSUSTRAC' from GeoJSON exists in the tract_type_map
        census_tract = feature['properties'].get('CENSUSTRAC')
        
        if census_tract and census_tract in tract_type_map:
            # Add the Tract_Type to the properties of the feature
            feature['properties']['Tract_Type'] = tract_type_map[census_tract]
        else:
            # Log the unmatched CENSUSTRAC
            log.write(f"Unmatched CENSUSTRAC: {census_tract}\n")
    
    # Save the updated GeoJSON to a new file
    with open(output_geojson_file, 'w') as f:
        json.dump(geojson_data, f, indent=4)

print(f"Updated GeoJSON saved to {output_geojson_file}")
print(f"Unmatched CENSUSTRAC values have been logged to {log_file}")
