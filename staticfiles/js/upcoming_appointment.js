$( document ).ready(function() {
    var x=0;
    for(var j=0;j<appointments.length;j++)
    {   if(uid == appointments.patient)
        {   if(x==0)
            {   $("#list").html('<li class="collection-item avatar"><i class="material-icons circle red">play_arrow</i><span class="title" id="hospital'+appointments.hospital+'">Hospital</span><div class="row" ><label class="doctor" id="doctor'+appointments.doctor+'">Doctor</label><br/><label class="tokenNo" id="token'+appointments.token_no+'">Toke Number</label><br/><label class="timeSlot" id="timeSlot'+appointments.time_slot_from+'">TIme Slot</label><br/></div><a href="#!" class="secondary-content"><i class="material-icons">grade</i></a></li>');
                x=1;
            }
            else
            {   $("#list").html('<li class="collection-item avatar"><i class="material-icons circle green">insert_chart</i><span class="title" id="hospital'+appointments.hospital+'">Hospital</span><div class="row" ><label class="doctor" id="doctor'+appointments.doctor+'">Doctor</label><br/><label class="tokenNo" id="token'+appointments.token_no+'">Toke Number</label><br/><label class="timeSlot" id="timeSlot'+appointments.time_slot_from+'">TIme Slot</label><br/></div><a href="#!" class="secondary-content"><i class="material-icons">grade</i></a></li>');
                x=0;
            }
        }
    }
});
