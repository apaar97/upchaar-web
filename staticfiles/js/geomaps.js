    $(document).ready(function(){
            var types = ['hospital'];
            var html = '';
            $.each(types, function( index, value ) {
                var name = value.replace(/_/g, " ");
                html += '<div><label><input type="checkbox" checked class="types" value="'+ value +'" />'+ '<span>'+capitalizeFirstLetter(name) +'</span>'+ '</label></div>';
            });
            $('#type_holder').html(html);
        });
        function capitalizeFirstLetter(string) {
            return string.charAt(0).toUpperCase() + string.slice(1);
        }
        var map;
        var infowindow;
        var autocomplete;
        var countryRestrict = {'country': 'in'};
        var selectedTypes = [];
        function initialize()
        {
            autocomplete = new google.maps.places.Autocomplete((document.getElementById('address')), {
                types: ['(regions)'],
               // componentRestrictions: countryRestrict
            });
            var pyrmont = new google.maps.LatLng(52.5666644, 4.7333304);
            map = new google.maps.Map(document.getElementById('map'), {
                center: pyrmont,
                zoom: 12
            });
        }
        function renderMap()
        {
            // Get the user defined values
            var address = document.getElementById('address').value;
            var radius  = parseInt(document.getElementById('radius').value) * 1000;
            // get the selected type
            selectedTypes = [];
            $('.types').each(function(){
                if($(this).is(':checked'))
                {
                    selectedTypes.push($(this).val());
                }
            });
            var geocoder    = new google.maps.Geocoder();
            var selLocLat   = 0;
            var selLocLng   = 0;
            geocoder.geocode({'address': address}, function(results, status) {
                if (status === 'OK')
                {
                    //console.log(results[0].geometry.location.lat() + ' - ' + results[0].geometry.location.lng());
                    console.log(results[0]);
                    selLocLat   = results[0].geometry.location.lat();
                    selLocLng   = results[0].geometry.location.lng();
                    //var pyrmont = new google.maps.LatLng(52.5666644, 4.7333304);
                    var pyrmont = new google.maps.LatLng(selLocLat, selLocLng);
                    map = new google.maps.Map(document.getElementById('map'), {
                        center: pyrmont,
                        zoom: 11
                    });
                    //console.log(selectedTypes);
                    var request = {
                        location: pyrmont,
                        //radius: 5000,
                        //types: ["atm"]
                        radius: radius,
                        types: selectedTypes
                    };
                    infowindow = new google.maps.InfoWindow();
                    var service = new google.maps.places.PlacesService(map);
                    service.nearbySearch(request, callback);
                }
                else
                {
                    alert('Geocode was not successful for the following reason: ' + status);
                }
            });
        }
        function callback(results, status)
        {
            if (status == google.maps.places.PlacesServiceStatus.OK)
            {
                for (var i = 0; i < results.length; i++)
                {
                    createMarker(results[i], results[i].icon);
                }
            }
        }
        function createMarker(place, icon) {
            console.log(place);
            var placeLoc = place.geometry.location;
            console.log(placeLoc.lat());
            console.log(placeLoc.lng());
            var marker = new google.maps.Marker({
                map: map,
                position: place.geometry.location,
                icon: {
                    url: icon,
                    scaledSize: new google.maps.Size(20, 20) // pixels
                },
                animation: google.maps.Animation.DROP
            });
            google.maps.event.addListener(marker, 'click', function() {
                infowindow.setContent(place.name+ '<br>' +place.vicinity);
                infowindow.open(map, this);
            });
        }
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showPosition);
            }
            else {
                x.innerHTML = "Geolocation is not supported by this browser.";
            }
        }
        var lat=0,log=0;
        function showPosition(position) {
            x.innerHTML = "Latitude: " + position.coords.latitude +
            "<br>Longitude: " + position.coords.longitude;
            var lat=position.coords.latitude;
            var log=position.coords.longitude;
        }