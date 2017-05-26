/**
 * Created by dan on 4/16/17.
 */
var map;
var service;
var infowindow;

//Makes a CSV out of an array of arrays of properties and automatically downloads it.
function makeCSV(data) {
    //Format the data
    let csvRows = [];
    for (let i = 0; i < data.length; ++i)csvRows.push(data[i].join(','));
    let csvString = csvRows.join('\n');

    //Create an anchor that auto-clicks to download the data
    let a         = document.createElement('a');
    a.href        = 'data:attachment/csv;charset=utf-8,' + encodeURI(csvString);
    a.target      = '_blank';
    a.download    = 'parsedLocations.csv';
    document.body.appendChild(a);
    a.click();
}

// Google Maps Initialize callback function
function initMap() {
    var Bucharest = {lat: 44.4378258, lng: 26.0946376};
    map = new google.maps.Map(document.getElementById('map'), {
        center: Bucharest,
        zoom: 13
    });

    var request = {
        location: Bucharest,
        radius: 1000,
        types: ['hospital']
    };

    infowindow = new google.maps.InfoWindow();
    service = new google.maps.places.PlacesService(map);
    var resultsArray = [["place_id","lat","long","name","type"]];
    var placesArray = [];
    var searched_types=["post_office", "school", "police", "subway_station", "hospital"];

    var top_left_Bucharest     = {lat: 44.458035,  lng: 26.039468};
    var top_right_Bucharest    = {lat: 44.456739, lng: 26.150323};
    var bottom_left_Bucharest  = {lat: 44.39375, lng: 26.045763};
    var bottom_right_Bucharest = {lat: 44.384706, lng: 26.174043};

    var distanceWidth  = 5;
    var distanceHeight = 5;

    var widthStride = (top_right_Bucharest.lng - top_left_Bucharest.lng) / distanceWidth;
    var heightStide = (top_left_Bucharest.lat - bottom_left_Bucharest.lat) / distanceHeight;

    var locations = []
    for(let i= 0; i < distanceWidth;  ++i){
       for(let j = 0; j < distanceHeight; ++j) {
           let newItem;
           newItem = {lat: bottom_left_Bucharest.lat + j * heightStide, lng: top_left_Bucharest.lng + widthStride * i};
           locations.push(newItem)
       }
    }
    function getAllPlacesInLocations(k){
        if(k === locations.length){
            makeCSV(resultsArray);
            return;
        }
        request.location = locations[k];
        function getAllPlacesOfSearchedTypes(j) {
            if (j === searched_types.length) {
                setTimeout(getAllPlacesInLocations,1000, k + 1);
                console.log(resultsArray);
                return;
            }
            console.log(j);
            request.types[0] = searched_types[j];
            //Get all the stores either through nearbySearch or radarSearch
            service.nearbySearch(request, result_callback_nearby);
            //    service.radarSearch(request,result_callback_radar);
            function result_callback_nearby(results, status, pagination) {
                for (let i = 0; i < results.length; ++i) {
                    let relevantInfo = [];
                    relevantInfo.push(results[i]["place_id"]);
                    relevantInfo.push(results[i].geometry.location.lat());
                    relevantInfo.push(results[i].geometry.location.lng());
                    relevantInfo.push(results[i]["name"]);
                    relevantInfo.push(results[i]['types'].join('-'));

                    resultsArray.push(relevantInfo);
                }
                if (pagination.hasNextPage) {
                    pagination.nextPage();
                }
                else {
                    //Delay so we can scrape more
                    console.log("am Ajuns unde voiam");
                    setTimeout(getAllPlacesOfSearchedTypes, 1000, j + 1);
                }
            }
        }

        getAllPlacesOfSearchedTypes(0);
    }
    getAllPlacesInLocations(0);

    //Currently not used, useful if we decide to use radarSearch
    function result_callback_radar(results, status) {

        // for(let i = 0; i < results.length; ++i){
        //     let relevantInfo = [];
        //     relevantInfo.push(results[i]["place_id"]);
        //     relevantInfo.push(results[i]["types"].join('-'));
        //     resultsArray.push(relevantInfo);
        // }
        console.log(results);
        for(let i = 0; i < results.length; ++i){
            placesArray.push(results[i]["place_id"]);
        }

        //Utility function in case we decide to parse using RadarSearch and need to individually search for every place_id
        //Rather Slow- Needs to delay API Calls in order to not get a warning from Google
        function getPlaces(i){
            if(i === placesArray.length) doneParsing();
            let req = {
                placeId: placesArray[i]
            };
            service.getDetails(req,function (place, status) {
                let relevantInfo = [];
                console.log(place);
                relevantInfo.push(place["place_id"]);
                relevantInfo.push(place.geometry.location.lat());
                relevantInfo.push(place.geometry.location.lng());
                relevantInfo.push(place["name"]);
                relevantInfo.push(place['types'].join('-'));
                resultsArray.push(relevantInfo);

                //Need to delay the next call so google's API lets us scrape more
               setTimeout( getPlaces, 1000, i + 1);
                // resultsArray.
            });
        }
        // getPlaces(0);


        function doneParsing(){
           makeCSV((resultsArray));
        }

        // makeCSV(resultsArray);
        // console.log(resultsArray);
        // console.log(results);
        // if (status === google.maps.places.PlacesServiceStatus.OK) {
        //     for (let i = 0; i < results.length; i++) {
        //         let place = results[i];
        //         createMarker(results[i]);
        //     }
        // }
    }

    function createMarker(place){
        var placeLoc = place.geometry.location;
        var marker = new google.maps.Marker({
            map: map,
            position: place.geometry.location
        });
        google.maps.event.addListener(marker, 'click', function(){
            infowindow.setContent(place.name);
            infowindow.open(map,this);
        });
    }
}