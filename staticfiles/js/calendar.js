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
    $('.calendar').fullCalendar('renderEvent', {id:1 , title: 'New event', start:  "Thu Mar 15 2018 16:04:40 GMT+0530", end:"Thu Mar 15 2018 19:04:40 GMT+0530", dow:[1,4],className : 'casual_leave' }, true);
    $('.calendar').fullCalendar('renderEvent', {id:2 , title: '2nd event', start: "Thu Mar 15 2018 19:04:40 GMT+0530", end: "Thu Mar 29 2018 19:04:40 GMT+0530" }, true);
    $('.calendar').fullCalendar('renderEvent', {id:3 , title: '3rd event', start: "Thu Mar 22 2018 19:04:40 GMT+0530", end: "Thu Mar 29 2018 19:04:40 GMT+0530" }, true);
    $('.calendar').fullCalendar('renderEvent', {id:4 , title:"Monday",start: '2017-02-28',dow:[1] }, true);
    $('.casual_leave').css('background-color','"pink"');
})



