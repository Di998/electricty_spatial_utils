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
    # Save the original GeoJSON as-is to the output file
    with open(output_file, 'w') as f:
        json.dump(original_geojson, f, indent=4)
else:
    print("The GeoJSON is not in WGS84 (CRS84). Performing transformation...")

    # Initialize the CRS transformer (transforming from EPSG:3857 to EPSG:4326)
    transformer = Transformer.from_crs('EPSG:3857', 'EPSG:4326', always_xy=True)

    # Initialize the new GeoJSON structure
    new_geojson = {
        "type": "FeatureCollection",
        "name": "Opportunity_Zones",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
            }
        },
        "features": []
    }

    # Transform each feature
    for feature in original_geojson['features']:
        # Get the geometry of the feature
        geometry = feature['geometry']

        # Only transform coordinates for geometries with coordinates
        if geometry['type'] == 'Point':
            # Transform from EPSG:3857 to EPSG:4326 (CRS84)
            x, y = transformer.transform(geometry['coordinates'][0], geometry['coordinates'][1])
            geometry['coordinates'] = [x, y]

        elif geometry['type'] == 'LineString':
            # Transform all coordinates in the LineString
            geometry['coordinates'] = [list(transformer.transform(x, y)) for x, y in geometry['coordinates']]

        elif geometry['type'] == 'Polygon':
            # Transform all coordinates in the Polygon
            geometry['coordinates'] = [
                [list(transformer.transform(x, y)) for x, y in polygon]
                for polygon in geometry['coordinates']
            ]

        # Create the new feature with transformed geometry
        new_feature = {
            "type": "Feature",
            "id": feature['id'],
            "properties": feature['properties'],
            "geometry": geometry
        }

        new_geojson['features'].append(new_feature)

    # Save the transformed GeoJSON to a new file
    with open(output_file, 'w') as f:
        json.dump(new_geojson, f, indent=4)

    print(f"Transformed GeoJSON saved to {output_file}")
