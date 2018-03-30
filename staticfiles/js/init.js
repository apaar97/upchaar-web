$(document).ready(function(){
    console.log('init');
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('#notification-sidenav').sidenav({edge:'right'});
    $('.dropdown-trigger').dropdown({
        coverTrigger:false
    });
    $('.modal').modal();
});

function closeNotificationSidenav() {
    $('#notification-sidenav').sidenav('close');
};