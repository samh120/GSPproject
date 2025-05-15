# raster_to_png.py
# Sam Hodgdon
# 05/11/2025
#
# This file takes all of our created raster files and converts them to pngs, and applies a custom color ramp
# To display on the web map, the raster needed to be converted to a png, initial raster could not be exported from qgis and retain the coloring
# This file is not run in the python environment but instead is added to the QGIS files as a script (ex: C:\Users\Sam\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\raster_to_png)
# If being run by a different user it would have to be inserted to the same location in the QGIS files in order to be run correctly
# The user would also need to edit to subprocess file with the corresponding location.
#
# Documentation used to figure out needed methods:
# https://qgis.org/pyqgis/3.40/index.html
# https://doc.qt.io/qtforpython-5/PySide2/QtGui/QImage.html
#



# Imports, wont work in python environment, are instead for use inside qgis process

import os
from qgis.core import (QgsRasterLayer,
    QgsRasterShader,
    QgsColorRampShader,
    QgsSingleBandPseudoColorRenderer,
    QgsMapSettings,
    QgsMapRendererCustomPainterJob)

from qgis.PyQt.QtGui import QImage, QPainter, QColor
from qgis.PyQt.QtCore import QSize

input_folder = r"C:\Users\Sam\Desktop\floodmap_project\forecast_rasters"    # File path for project folders containing rasters and for outputs
output_folder = r"C:\Users\Sam\Desktop\floodmap_project\forecast_pngs"  # Must be absolute paths as the file is being run through the qgis process

raster_files = [file for file in os.listdir(input_folder) if file.endswith('.tif')]     # Go through input folder and get all tif files

for raster_file in raster_files:
    raster_path = os.path.join(input_folder, raster_file)   # Rejoin file to absolute path
    raster_layer = QgsRasterLayer(raster_path, raster_file) # Convert to QgsRasterLayer

    if not raster_layer.isValid():  # Check if given raster is valid, if not send error message
        print(f"Failed to load {raster_file}")
        continue    # Skips rest of current loop if not valid

    
    shader = QgsRasterShader()  # Create a raster shader object 
    gyr_ramp = QgsColorRampShader()       # Create ColorRampShader Object
    gyr_ramp.setColorRampType(QgsColorRampShader.Interpolated)    # Set ramp type to interpolated (based on a number of stops)
    gyr_ramp.setColorRampItemList([
        QgsColorRampShader.ColorRampItem(0, QColor(0, 255, 0), 'Low'),  # Defining color ramp stops, green for low, yellow for medium, red for high risk
        QgsColorRampShader.ColorRampItem(50, QColor(255, 255, 0), 'Medium'),
        QgsColorRampShader.ColorRampItem(100, QColor(255, 0, 0), 'High')
    ])
    shader.setRasterShaderFunction(gyr_ramp)  # Pass the color ramp to the shader

    renderer = QgsSingleBandPseudoColorRenderer(raster_layer.dataProvider(), 1, shader) # Raster rendering, input is our raster, one band, shader as our created shader
    raster_layer.setRenderer(renderer)  # Set the renderer of our layer to our created renderer
    raster_layer.triggerRepaint()   

    
    extent = raster_layer.extent()  # Get the extent of the raster image
    width = 1024  # Setting a fixed width for the png image
    height = int(width * (extent.height() / extent.width()))  # Attempting to have the same ratio as the raster, did not work and had to stretch in script.js

    image = QImage(QSize(width, height), QImage.Format_ARGB32_Premultiplied) # Create image of specified size and using 32bit ARGB
    image.fill(0)  # create transparent background
    painter = QPainter(image)

    settings = QgsMapSettings()
    settings.setLayers([raster_layer])
    settings.setExtent(extent)
    settings.setOutputSize(QSize(width, height))
    settings.setBackgroundColor(QColor(255, 255, 255, 0))  # transparent background

    job = QgsMapRendererCustomPainterJob(settings, painter)
    job.start()
    job.waitForFinished()
    painter.end()

    output_path = os.path.join(output_folder, raster_file.replace('.tif', '.png'))
    image.save(output_path)
    print(f"Saved: {output_path}")