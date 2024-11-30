/* data routes */
const receive_url = "/receive"
console.log("reading receive.js")
// Read in beach data and get marker clusters
Promise.all([
    d3.json(receive_url)
    ]).then(function(data) {
        console.log(data);
        // Loop through data

    });













//     // Read in beach data and get marker clusters
// Promise.all([
//     d3.json([dummy_url])
//     ]).then(function(data) {
//         console.log(data);
        
//         var markers = [];
//         var pet_markers = [];
//         var parking_markers = [];
//         var pets_parking = [];

//         console.log(data[0][0].latitude);
//         // Loop through data
//         for (var i = 0; i < data[0].length; i++) {

//             var beachdata = data[0];
//             var pets = beachdata[i].pets_allowed;
//             var parking = beachdata[i].free_parking;

//             markers.push(L.marker([beachdata[i].latitude, beachdata[i].longitude])
//                 .bindPopup("<h4>" + beachdata[i].beach_name + "</h4><hr><p>" + beachdata[i].address + ", " + beachdata[i].city + ", " + beachdata[i].state + " " + beachdata[i].zip + "</p>" + "<p><b>Activities: " +  beachdata[i].activities + "</p>" + "<p><b>Amenities: " + beachdata[i].amenities + "<b></p>"));

            
//             if (pets == "Y") {
//                 pet_markers.push(L.marker([beachdata[i].latitude, beachdata[i].longitude])
//                     .bindPopup("<h4>" + beachdata[i].beach_name + "</h4><hr><p>" + beachdata[i].address + ", " + beachdata[i].city + ", " + beachdata[i].state + " " + beachdata[i].zip + "</p>" + "<p><b>Activities: " +  beachdata[i].activities + "</p>" + "<p><b>Amenities: " + beachdata[i].amenities + "<b></p>"));
//             }

//             if (parking == "Y") {
//                 parking_markers.push(L.marker([beachdata[i].latitude, beachdata[i].longitude])
//                     .bindPopup("<h4>" + beachdata[i].beach_name + "</h4><hr><p>" + beachdata[i].address + ", " + beachdata[i].city + ", " + beachdata[i].state + " " + beachdata[i].zip + "</p>" + "<p><b>Activities: " +  beachdata[i].activities + "</p>" + "<p><b>Amenities: " + beachdata[i].amenities + "<b></p>"));
//             }

//             if (pets == "Y" & parking == "Y") {
//                 pets_parking.push(L.marker([beachdata[i].latitude, beachdata[i].longitude])
//                     .bindPopup("<h4>" + beachdata[i].beach_name + "</h4><hr><p>" + beachdata[i].address + ", " + beachdata[i].city + ", " + beachdata[i].state + " " + beachdata[i].zip + "</p>" + "<p><b>Activities: " +  beachdata[i].activities + "</p>" + "<p><b>Amenities: " + beachdata[i].amenities + "<b></p>"));
//             }
//         }

//         // Streetmap Layer
//         var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//             attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
//             tileSize: 512,
//             maxZoom: 18,
//             zoomOffset: -1,
//             id: "mapbox/streets-v11",
//             accessToken: API_KEY
//         });
        
//         var darkmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//             attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
//             maxZoom: 18,
//             id: "dark-v10",
//             accessToken: API_KEY
//         });
        
//         // Create 3 separate layer groups: one for beaches, pets, and parking
//         var beach_markers = L.layerGroup(markers);
//         var pet = L.layerGroup(pet_markers);
//         var park = L.layerGroup(parking_markers);
//         var petpark = L.layerGroup(pets_parking);
        
//         // Create a baseMaps object
//         var baseMaps = {
//             "Street Map": streetmap,
//             "Dark Map": darkmap
//         };
        
//         // Create an overlay object
//         var overlayMaps = {
//             "All Beaches": beach_markers,
//             "Pets Allowed": pet,
//             "Free Parking": park,
//             "Pets Allowed & Free Parking": petpark
//         };
        
//         // Define a map object and set beach markers for initial loading screen
//         var myMap = L.map("mapviz", {
//             center: [34.019625000000000, -118.510699000000000],
//             zoom: 12,
//             layers: [streetmap, beach_markers]
//         });
        
//         // Pass our map layers into our layer control
//         // Add the layer control to the map
//         L.control.layers(baseMaps, overlayMaps, {
//             collapsed: false
//         }).addTo(myMap);
//     });