import json
from pyproj import Transformer

# Function to check if the CRS is WGS84 (CRS84)
def is_wgs84(crs):
    if not crs:
        return False
    name = crs.get("properties", {}).get("name", "").lower()
    # CRS84 corresponds to EPSG:4326 with axis order longitude, latitude
    return "crs84" in name or "epsg:4326" in name

# File paths
input_file = '/Users/di/Documents/TechMaven/Tech_Maven_Projects/electricty_spatial_utils/i.geojson'
output_file = 'transformed.geojson'

# Read the original GeoJSON file
with open(input_file, 'r') as f:
    original_geojson = json.load(f)

# Check the CRS of the original GeoJSON
original_crs = original_geojson.get("crs", None)

if is_wgs84(original_crs):
    print("The GeoJSON is already in WGS84 (CRS84). No transformation needed.")
    # Change structure even though coordinates are in WGS84
    new_geojson = {
        "type": "FeatureCollection",
        "name": "Opportunity_Zones",  # Change the name to "Shorelines"
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
            }
        },
        "features": []
    }

    # Use the features from the original GeoJSON without transformation
    for feature in original_geojson['features']:
        # Directly append the feature without changing the coordinates
        new_feature = {
            "type": "Feature",
            "id": feature['id'],
            "properties": feature['properties'],
            "geometry": feature['geometry']
        }
        new_geojson['features'].append(new_feature)

    # Save the modified GeoJSON with new structure
    with open(output_file, 'w') as f:
        json.dump(new_geojson, f, indent=4)

    print(f"Transformed GeoJSON saved to {output_file}")
else:
    print("The GeoJSON is not in WGS84 (CRS84). No transformation performed.")
