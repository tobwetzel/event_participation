/**
 * Created by Tobias on 02.04.2015.
 */

function selectTrack(element){

    var selected = (element.className.indexOf("selected") == -1 ? 0 : 1);
    var tracks = document.getElementsByClassName("track-selectable");


    for(var i = 0; i < tracks.length; i++){
        //reset all class names
        tracks[i].className= "track-selectable";
    }

    //if element has not allready been selected
    if(!selected){
        //add "selected" class to selected element
        element.className += " selected"
    }
}
