/**
 * Created by Tobias on 06.04.2015.
 */

function validateForm(){
    //add selected tracks
    var input_tracks = document.createElement("input");
    input_tracks.setAttribute("name","tracks");
    input_tracks.setAttribute("type","hidden");

    var selectedElements = document.getElementsByClassName("track-selectable selected");
    console.log(selectedElements);

    var tracks = [];

    for (var i = 0; i < selectedElements.length; i++){
        //tracks.push(selectedElements[i].firstChild.nodeValue);
        tracks.push(selectedElements[i].id);
    }

    input_tracks.setAttribute("value", tracks.toString());

    //get form
    var form = document.getElementById("submit-form");
    //append node
    form.appendChild(input_tracks);
}
