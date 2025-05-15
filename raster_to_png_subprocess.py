# raster_to_png_subprocess.py
# Sam Hodgdon
# 5/11/2025
#
# This script is made to run the raster_to_png script within the QGIS process
# Uses the qgis proccess batchfile to run the script as opposed to this python environment
# Path of the script is configured to work on other systems but the batch file path must be changed if used by a different user
#



import subprocess
import os

batch_file_path = r"D:\Program Files\QGIS 3.40.6\bin\qgis_process-qgis-ltr.bat" # Absolute path to the qgis process batch file, this is where we pass the script to run

script_path = os.path.abspath("raster_to_png.py") # Absolute path to the script, shouldnt have to be changed to be run by a different user

cmd = [batch_file_path, 'run', r'script:{C:\Users\Sam\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\raster_to_png}']   # Creating the command to run
print("Running command:", cmd)  # print the command (used for debugging)

subprocess.run(cmd) # Run our command
