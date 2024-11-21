import json

# Read the original GeoJSON file
with open('/Users/di/Documents/TechMaven/Tech_Maven_Projects/electricty_spatial_utils/o.geojson', 'r') as f:
    original_geojson = json.load(f)

# Initialize the new GeoJSON structure
new_geojson = {
    "type": "FeatureCollection",
    "name": "Shorelines",
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
    new_feature = {
        "type": "Feature",
        "id": feature['id'],
        "properties": feature['properties'],  # Keep properties as they are
        "geometry": feature['geometry']  # Keep geometry as it is
    }
    new_geojson['features'].append(new_feature)

# Save the transformed GeoJSON to a new file
with open('transformed.geojson', 'w') as f:
    json.dump(new_geojson, f, indent=4)
