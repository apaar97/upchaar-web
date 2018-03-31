var elem = document.querySelector('.datepicker');


    $(document).ready(function(){

        var data_1={};
        for (j = 0; j < doctors.length; j++){
            console.log("HEY"+j);
            for(var i=0;i<users.length;i++)
            {
                if(users[i].pk==doctors[parseInt(j)].pk)
                {
                    data_1[users[i].fields.first_name+" "+users[i].fields.last_name]=null;
                }
            }
        }
        $('.datepicker').datepicker();
        $('#doctor').autocomplete({

      data: data_1,

    });

    var j=0;



    var xy='';
    j=0;
    console.log(doctors[0].pk);
    for (j = 0; j < doctors.length; j++){
        console.log("HEY"+j);
        for(var i=0;i<users.length;i++)
        {
            if(users[i].pk==doctors[j].pk)
            {
                xy += '<div class="col s12 m4"><div class="card" style="height:100%; width: 80%"><div class="card-image"><img style="opacity:0.5" src="https://mahansms.com/Media/Default/Thumbs/0000/0000062---600.jpg"><span class="card-title" style="font-size: 200%; color: Black"><b>'+users[i].fields.first_name+" "+users[i].fields.last_name+'</b></span><a class="btn-floating halfway-fab waves-effect waves-light red doc" id="'+doctors[parseInt(j)].pk+'" ><i class="material-icons">add</i></a></div><div class="card-content"><p><ul><li>Education:&nbsp'+doctors[j].fields.education+'</li><li></li></ul></p></div></div></div>'

            }
        }

    }


    $('#add_cards').html(xy);




    $('.dropdown-trigger').dropdown();

    var data_3={};
        for(var i=0;i<hospitals.length;i++)
        {

                data_3[hospitals[i].fields.hospital_name]=null;

        }

    $('#hospital').autocomplete({
      data: data_3,
    });

    var data_2={};
        for(var i=0;i<departments.length;i++)
        {

                data_2[departments[i].fields.department_name]=null;

        }
    $('#department').autocomplete({
      data: data_2,
    });


    $(".doc").click(function(){
        //  ---------- slots dikhao iske baad -------/

        console.log(this.id);
        sessionStorage.setItem("id_doctor", this.id);
        window.location = "http://127.0.0.1:8000/appointment/calendar";

    })

    $("#filter").click(function(){

    var main_data=[];
    main_data=doctors;


        if($('#fromDate').val()!=''&&$('#fromDate').val()!=null&&$('#toDate').val()!=''&&$('#toDate').val()!=null)
        {
            console.log("KK");
            var fromDate=$('#fromDate');
            var toDate=$('#toDate');

            for (j = 0; j < main_data.length; j++){
                console.log("HEY"+j);

           }


        }
        console.log("MAIN DATA");
        console.log(main_data);

        if($('#doctor').val()!=''&&$('#doctor').val()!=null)
        {
            var new_data=[];
                var k=0;
            for (j = 0; j < main_data.length; j++){
                console.log("HEY"+j);

                for(var i=0;i<users.length;i++)
                {
                    if(users[i].pk==main_data[parseInt(j)].pk)
                    {
                        if(users[i].fields.first_name+" "+users[i].fields.last_name==$('#doctor').val())
                        {
                            new_data[k]=main_data[j];
                            k++;
                        }
                    }
                }

            }
            main_data=new_data;
            console.log(main_data);
        }
        if($('#hospital').val()!=''&&$('#hospital').val()!=null)
        {
            var new_data=[];
                var k=0;

            for (j = 0; j < hospitals.length; j++){

                        for(var l=0;l<daySchedule.length;l++)
                        {

                                if(hospitals[parseInt(t)].pk==daySchedule[l].fields.hospital&&hospitals[parseInt(t)].fields.hospital_name==$('#hospital').val())
                                {
                                    for(var f=0;f<main_data.length;f++)
                                    {
                                        if(daySchedule[l].fields.doctor==main_data[f].pk)
                                        {
                                            new_data[k]=main_data[f];
                                            k++;
                                        }
                                    }
                                }


                        }


            }
            main_data=new_data;
        }

        if($('#department').val()!=''&&$('#department').val()!=null)
        {
            var new_data=[];
            var k=0;
            for(j=0;j < main_data.length;j++)
            {
                for(var i=0;i < departments.length;i++)
                {
                    if(main_data[j].fields.department==department[i].pk)
                    {
                        new_data[k]=main_data[j];
                        k++;
                    }
                }
            }
            main_data=new_data;
        }
        xy='';
        for (j = 0; j < main_data.length; j++){
            console.log("HEY"+j);
            for(var i=0;i<users.length;i++)
            {
                if(users[i].pk==main_data[j].pk)
                {
                    xy += '<div class="col s12 m4"><div class="card" style="height:100%; width: 80%"><div class="card-image"><img style="opacity:0.5" src="https://mahansms.com/Media/Default/Thumbs/0000/0000062---600.jpg"><span class="card-title" style="font-size: 200%; color: Black"><b>'+users[i].fields.first_name+" "+users[i].fields.last_name+'</b></span><a class="btn-floating halfway-fab waves-effect waves-light red doc" id="'+main_data[parseInt(j)].pk+'" ><i class="material-icons">add</i></a></div><div class="card-content"><p><ul><li>Education:&nbsp'+main_data[j].fields.education+'</li><li></li></ul></p></div></div></div>'

                }
            }

        }

        $('#add_cards').html(xy);





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