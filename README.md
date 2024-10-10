# Electricity Spatial Utilities

This repository provides a collection of Python scripts to automate and optimize the handling of geospatial data related to electricity systems, particularly GeoJSON files. The scripts help in downloading, modifying, structuring, and compacting GeoJSON data for consistent and efficient usage.

## Workflow Overview

1. **Download GeoJSON File:**  
   Use the `get_geojson_file.py` script to fetch GeoJSON files from the server via the provided API.
2. **Add Identifiers:**  
   After downloading, you can modify the GeoJSON file to add identifiers (ID and/or ObjectID) using either `add_ID.py` or `add_objectID.py`, or both if needed.
3. **Inspect Identifiers:**  
   Use the `print_ID_ObjectID.py` script to print the ID and ObjectID in the GeoJSON file for verification.
4. **Ensure Consistent Structure:**  
   Run the `tr_structure.py` script to standardize the structure of the GeoJSON file for consistency across all layers.
5. **Automate Compaction:**  
   Inside the `compact_layers_script` folder, use the `automate_compaction.py` script to compact the initial GeoJSON files, reducing file size while preserving essential data.

## Detailed Script Descriptions

### 1. `get_geojson_file.py`

This script downloads the GeoJSON file from a specified server using an API. Ensure that the API configuration (e.g., endpoint, parameters) is correctly set within the script before running.

**Command:**

```bash
python get_geojson_file.py
```

### 2. `add_ID.py` and `add_objectID.py`

These scripts add unique identifiers to the GeoJSON features:

- add_ID.py adds an ID to each feature.
- add_objectID.py adds an ObjectID to each feature.
  You can use one or both scripts depending on the requirements of your GeoJSON data.

**Command:**

```bash
python add_ID.py
```

```bash
python add_objectID.py
```

### 3. `print_ID_ObjectID.py`

This script prints out the ID and ObjectID from the GeoJSON file, allowing you to inspect and verify the identifiers added to the data.

**Command:**

```bash
python print_ID_ObjectID.py
```

### 4. `tr_structure.py`

To maintain consistency across all GeoJSON files, use tr_structure.py. This script enforces a standardized structure in the GeoJSON data, ensuring uniformity and compatibility across different layers.

**Command:**

```bash
python tr_structure.py
```

### 5. `compact_layers_script/automate_compaction.py`

Located inside the compact_layers_script folder, this script automates the compaction of GeoJSON files, reducing their size while preserving necessary spatial details. This is useful for optimizing file storage and enhancing performance when handling large datasets.

**Command:**

```bash
python compact_layers_script/automate_compaction.py
```
