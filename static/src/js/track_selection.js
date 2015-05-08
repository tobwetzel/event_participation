/**
 * Created by Tobias on 02.04.2015.
 */

function mergeNodeLists(list1, list2){
    var array1 = Array.prototype.slice.call(list1);
    var array2 = Array.prototype.slice.call(list2);

    return array1.concat(array2);
}

function selectTrack(element){

    //check if the element is already selected
    var selected = (element.className.indexOf("selected") == -1 ? 0 : 1);
    //get class name
    var track_class = element.className;
    //get all tracks
    var all_tracks = document.getElementsByClassName("track-selectable");

    //get all tracks that can not be selected while the selected track is selected
    //for 'morning' tracks select full-day tracks and other 'morning' tracks
    if (track_class.indexOf("morning") > -1) {
        var tracks = mergeNodeLists(document.getElementsByClassName("track-selectable morning"), document.getElementsByClassName("track-selectable full_day"));
    }
    //for 'afternoon' tracks select full-day tracks and other 'afternoon' tracks
    else if (track_class.indexOf("afternoon") > -1) {
        var tracks = mergeNodeLists(document.getElementsByClassName("track-selectable afternoon"), document.getElementsByClassName("track-selectable full_day"));
    }
    //for full-day tracks select all tracks
    else {
        var tracks = all_tracks;
    }

    //look through tracks to find other selected tracks
    for(var i = 0; i < tracks.length; i++){
        if(tracks[i].className.indexOf("selected") > -1) {
            //deselect: remove 'selected' class
            tracks[i].className = tracks[i].className.replace("selected", "");
        }
    }

    //if element has not already been selected
    if(!selected){
        //add 'selected' class to selected element
        element.className += " selected"
    }
    else {
        console.log("track was selected before");
        var trackIsSelected = false;

        //check if there is at least one track selected
        for(var j = 0; j < all_tracks.length; j++){
            if(all_tracks[j].className.indexOf("selected") > -1){
                console.log("found other selected track");
                trackIsSelected = true;
                break;
            }
        }

        //if not select the 'I am undecided' slot
        if(!trackIsSelected){
            console.log("found no selected track");
            document.getElementById("track-undecided").className += " selected"
        }
    }

}
