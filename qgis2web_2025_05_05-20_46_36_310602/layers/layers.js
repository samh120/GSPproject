var wms_layers = [];


        var lyr_OSMStandard_0 = new ol.layer.Tile({
            'title': 'OSM Standard',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
            attributions: ' &nbsp &middot; <a href="https://www.openstreetmap.org/copyright">© OpenStreetMap contributors, CC-BY-SA</a>',
                url: 'http://tile.openstreetmap.org/{z}/{x}/{y}.png'
            })
        });
var lyr_please_1 = new ol.layer.Image({
        opacity: 1,
        
    title: 'please<br />\
    <img src="styles/legend/please_1_0.png" /> 34.4167<br />\
    <img src="styles/legend/please_1_1.png" /> 50.8125<br />\
    <img src="styles/legend/please_1_2.png" /> 67.2083<br />\
    <img src="styles/legend/please_1_3.png" /> 83.6042<br />\
    <img src="styles/legend/please_1_4.png" /> 100.0000<br />' ,
        
        
        source: new ol.source.ImageStatic({
            url: "./layers/please_1.png",
            attributions: ' ',
            projection: 'EPSG:3857',
            alwaysInRange: true,
            imageExtent: [-13849189.944702, 4866215.479741, -13737554.306555, 5081238.264702]
        })
    });

lyr_OSMStandard_0.setVisible(true);lyr_please_1.setVisible(true);
var layersList = [lyr_OSMStandard_0,lyr_please_1];
