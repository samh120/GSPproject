// update.js
//
//
//
//
//
//

const map = L.map('map').setView([40.88, -124.108], 13);   // Load map and set view to Arcata, sets zoom to 13

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: '© OpenStreetMap'}).addTo(map); // Adding openstreetmap base layer to the map

let currentRaster = null;   // Declare currentRaster, no initial value


function loadRaster(day) {
    if (currentRaster) {
      map.removeLayer(currentRaster); // Remove any existing raster
    }
  
    const imageUrl = `forecast_pngs/risk_day_${day}_rain.png`;  // Check if the path is correct
    console.log(`Loading raster for day ${day}: ${imageUrl}`);
    
    const bounds = [[40.92667, -124.1705], [40.82835, -124.02484]];  // Check if these bounds are correct
  
    currentRaster = L.imageOverlay(imageUrl, bounds, { opacity: 0.6 }); // makes current raster our png image stretched to the bounds (this bypasses the need to geo reference),
    currentRaster.addTo(map);   // and sets the opacity to .6 in order to see the basemap below. Then is added to the map.
  }

loadRaster(0); // Default day (0 for current day) is loaded

document.getElementById('forecastSelect').addEventListener('change', (e) => {   // load raster based on change to the select on the html page
  loadRaster(e.target.value);
});