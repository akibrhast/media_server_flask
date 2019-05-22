
//timer for the back to broswe button, appear and dissapear on mouse movement
var timer = 0;

//gets the ID of the video tag
var vid = document.querySelector('video');

//Play pause video with spacebar
    window.onkeypress = function () {PausePlayWithSpace(); }
function PausePlayWithSpace(e)
{
        if (event.keyCode == 32) {
                    if (vid.paused)
            vid.play();
        else
            vid.pause();
        }

}
//back to browse button shows up on mouse move
vid.onmousemove = function () {onMouseMoveFunction()};
function onMouseMoveFunction()
{
    clearTimeout(timer);
    document.getElementById('onmouse').style.display = 'block';
    timer=setTimeout(onMouseOutFunction, 4000);
}
//back to browse button dissapears when mouse stationary
function onMouseOutFunction()
{
    document.getElementById('onmouse').style.display = 'none';
}



  
function CurrentlyWatchingTracker()
{
    var LenghtWatched = vid.currentTime;
    var MovieID = id;


    $.ajax
    ({
        type: "POST",
        url: "/Movies/SaveUserState",
        data: {LenghtWatched, MovieID },
        success: null,
        dataType: "json"
    });

   

}


