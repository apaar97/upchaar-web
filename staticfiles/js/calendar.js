$(document).ready(function() {
    $('.calendar').each(function(){
        var calendar = $(this)
        calendar.fullCalendar({
            selectable : true,
            editable : true,
            eventStartEditable: true,
            eventDurationEditable : true,
            header : {
                left : 'prev , next today',
                center : 'title',
                right : 'month,agendaWeek,agendaDay'
            },
            dayClick: function(date) {
                alert('clicked ' + date.format());
            },
            select: function(startDate, endDate) {
                $('.modal').modal('open');
                $('.modal-overlay').css('background-color','pink');
                $('.modal-overlay').css('margin-top','200px');
                $('.modal-overlay').append("<div class='modal-content'><h4>Modal Header</h4><p>A bunch of text</p></div><div class='modal-footer'><a href='#!' class='modal-action modal-close waves-effect waves-green btn-flat'>Agree</a></div></div>");
            }
        });
    })
//    var doc_id=sessionSorage.getItem("id_doctor");
//    var now = new Date();
//        for (var d = new Date(2012, 2, 1); d <= now; d.setDate(d.getDate() + 1))
//        {
//           var count_1=0;
//           var count_2=0;
//           var count_3=0;
//
//           for(var j=0;j<appointments.length;j++)
//            {
//                if(appointments[j].doctor==doc_id)
//                {
//                    if(appointments.appointment_date==d)
//                    {
//                        if(time_slot_from=="09:00:00")
//                        {
//                            count_1++
//
//                        }
//                        else if(time_slot_from=="13:00:00")
//                        {
//                            count_2++;
//                        }
//                        else
//                        {
//                            count_3++;
//                        }
//                    }
//                }
//            }
//            $('.calendar').fullCalendar(
//                'renderEvent',
//                {   id:1,
//                    title: 'Morning Tokens Left='100-count_1,
//                    start: d.getDay()+ d.getYear()+d.getMonth()+d.getDate()+"09:00:00 GMT+0530",
//                    end: d.getDay()+ d.getYear()+d.getMonth()+d.getDate()+"12:00:00 GMT+0530",
//                    className : 'casual_leave'
//                },
//                true);
//            $('.calendar').fullCalendar('renderEvent', {id:1 , title: 'Noon Tokens Left='100-count_2, start: d.getDay()+ d.getYear()+d.getMonth()+d.getDate()+"13:00:00 GMT+0530",end: d.getDay()+ d.getYear()+d.getMonth()+d.getDate()+"16:00:00 GMT+0530" className : 'casual_leave'}, true);
//            $('.calendar').fullCalendar('renderEvent', {id:1 , title: 'Evening Tokens Left='100-count_3, start: d.getDay()+ d.getYear()+d.getMonth()+d.getDate()+"18:00:00 GMT+0530", end: d.getDay()+ d.getYear()+d.getMonth()+d.getDate()+"21:00:00 GMT+0530", className : 'casual_leave'}, true);
//        }
//        for(var i=0;i<dayschedules.length;i++)
//        {   $('.calendar').fullCalendar(
//                'renderEvent',
//                {   id:i+1 ,
//                    title: 'Event',
//                    start: "Thu Mar 15 2018 16:04:40 GMT+0530",
//                    end:"Thu Mar 15 2018 19:04:40 GMT+0530",
//                    className : 'casual_leave'
//                },
//                true);
//        }
    $('.casual_leave').css('background-color','"pink"');
    $('.calendar').fullCalendar('renderEvent', {id:1 , title: 'Morning Slot', start: "Thu Mar 27 2018 09:00:00 GMT+0530", end:"Thu Mar 27 2018 12:00:00 GMT+0530",className : 'casual_leave' }, true);
    $('.calendar').fullCalendar('renderEvent', {id:2 , title: 'Evening Slot', start: "Thu Mar 27 2018 18:00:00 GMT+0530", end: "Thu Mar 27 2018 21:00:00 GMT+0530" }, true);
    $('.calendar').fullCalendar('renderEvent', {id:3 , title: 'Afternoon Slot', start: "Thu Mar 31 2018 13:00:00 GMT+0530", end: "Thu Mar 31 2018 15:04:40 GMT+0530" }, true);
//    $('.calendar').fullCalendar('renderEvent', {id:4 , title:"Monday",start: '2017-02-28',dow:[1] }, true);

})



