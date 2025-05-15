# rainfall.py
# Sam Hodgdon
# 05/10/2025
#
# Takes in rainfall data from the api script and makes alternate versions based on the base risk raster
# Hard programmed for day 5 to have 10 in of rain for demonstration purposes (weather was not very interesting for finals week)
# https://rasterio.readthedocs.io/en/stable/
#


import rasterio     # Import packages 
import numpy as np

from rainapi import update_rainfall     # Import function that gathers rain data


rainfall_values = update_rainfall() # Use rainfall gathered from the api script

mult = 3   # Arbitrary value to multiply with the raster values, could be changed later to be more scientific

# Open the base risk raster once
with rasterio.open("final_risk6.tif") as raster:
    base_risk = raster.read(1)
    meta = raster.meta

# Loop through the rainfall values
for x in range(0, 7):
    # Calculate new risk
    if x == 5:  # Hard coding for demonstration
        rainfall = 10
    else:
        rainfall = rainfall_values[x]   # Grab data for the day
    adjusted_risk = base_risk + (rainfall * mult)   # Add the base risk + rainfall in inches multiplied by the mult factor
    adjusted_risk = np.clip(adjusted_risk, 0, 100)  # clip the value to avoid going out of the raster bounds for the color ramp

    output_path = f"forecast_rasters/risk_day_{x}_rain.tif" # Save to a new raster
    with rasterio.open(output_path, "w", **meta) as file:   # open the file to write and copy metadata from the base raster
        file.write(adjusted_risk.astype(rasterio.float32), 1) # Write to the file, adjusted_risk is converted to a 32 bit float, specified 1 raster band

    print(f"Created: {output_path}")    # Confirm in the terminal that the raster has been created