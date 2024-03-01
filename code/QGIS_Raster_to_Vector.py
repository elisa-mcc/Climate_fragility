# Run this script in in the QGIS Python console to perform the raster to polygon conversion

# Prompt the user to select a group of layers
selected_group = QgsProject.instance().layerTreeRoot().findGroup("Your Group Name")  # Replace with the actual group name

if selected_group is None:
    print("Group not found.")
else:
    # Iterate through the layers in the selected group
    for layer_node in selected_group.children():
        if isinstance(layer_node, QgsLayerTreeLayer):
            input_layer = layer_node.layer()
            
            # Get the input file name
            input_file_path = input_layer.source()
            input_file_name = input_file_path.split('/')[-1]  # Extract the file name
            
            # Construct the output file path
            output_file_path = '/path/to/output/directory/' + input_file_name.replace('.tif', '_vector.shp')  # Modify the output directory as needed
            
            # Perform the Raster to Polygon conversion
            processing.run("gdal:polygonize", {'INPUT':input_file_path, 'BAND':1, 'OUTPUT':output_file_path})
            
            print(f"Conversion complete for {input_file_name}. Output saved at {output_file_path}")
