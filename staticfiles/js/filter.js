var elem = document.querySelector('.datepicker');


    $(document).ready(function(){
        $('.datepicker').datepicker();
        $('#doctor').autocomplete({
      data: {
        "Ms Anchal Garg": null,
        "Mr Kunal": null,
        "Mr Apaar Gupta": null
      },
    });

    $('.dropdown-trigger').dropdown();

    $('#hospital').autocomplete({
      data: {
        "City Hospital": null,
        "Sacred Heart Hospital": null,
        "XYZ Hospital": null
      },
    });

    $('#department').autocomplete({
      data: {
        "Cardiology": null,
        "Surgery": null,
        "Medicine": null
      },
    });


    $(".doc").click(function(){
        //  ---------- slots dikhao iske baad -------/
        //this.id
        console.log("HELLO");


    })

    });

    var x = document.getElementById("demo");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    x.innerHTML = "Latitude: " + position.coords.latitude +
    "<br>Longitude: " + position.coords.longitude;
    var present_lat=position.coords.latitude;
    var present_lon=position.coords.longitude;



}