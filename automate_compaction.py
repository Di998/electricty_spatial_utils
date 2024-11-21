import json
import os

# Folder containing original GeoJSON files
input_folder_path = '/Users/di/Documents/TechMaven/Tech_Maven_Projects/electricty_spatial_utils/uncompacted_layers'

# Folder to save the compacted GeoJSON files
output_folder_path = '/Users/di/Documents/TechMaven/Tech_Maven_Projects/electricty_spatial_utils/compacted_layers'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Initialize a counter
counter = 0

# Iterate over all files in the input folder
for filename in os.listdir(input_folder_path):
    if filename.endswith('.geojson'):  # Check if it's a GeoJSON file
        file_path = os.path.join(input_folder_path, filename)

        print(f"Processing {filename}...")

        try:
            # Load the GeoJSON file
            with open(file_path, 'r') as file:
                data = json.load(file)

            # Convert the GeoJSON to a compact string
            compact_geojson = json.dumps(data, separators=(',', ':'))

            # Create the new file name by appending '_compacted'
            new_filename = f"{os.path.splitext(filename)[0]}_compacted.geojson"
            new_file_path = os.path.join(output_folder_path, new_filename)

            # Save the compacted GeoJSON to the new file in the output folder
            with open(new_file_path, 'w') as file:
                file.write(compact_geojson)

            # Increment the counter
            counter += 1

            print(f"[{counter}] Successfully compacted {filename} and saved as {new_filename} in {output_folder_path}")

        except Exception as e:
            # Catch any errors and print them
            print(f"Error processing {filename}: {e}")

# Print total files processed
print(f"Total files processed successfully: {counter}")
