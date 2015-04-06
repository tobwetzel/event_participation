/**
 * Created by Tobias on 02.04.2015.
 */

function mergeNodeLists(list1, list2){
    var array1 = Array.prototype.slice.call(list1);
    var array2 = Array.prototype.slice.call(list2);

    return array1.concat(array2);
}

function selectTrack(element){

    var selected = (element.className.indexOf("selected") == -1 ? 0 : 1);
    var track_class = element.className;

    if (track_class.indexOf("morning") > -1) {
        var tracks = mergeNodeLists(document.getElementsByClassName("track-selectable morning"), document.getElementsByClassName("track-selectable full_day"));
    }
    else if (track_class.indexOf("afternoon") > -1) {
        var tracks = mergeNodeLists(document.getElementsByClassName("track-selectable afternoon"), document.getElementsByClassName("track-selectable full_day"));
    }
    else {
        var tracks = document.getElementsByClassName("track-selectable");
    }


    for(var i = 0; i < tracks.length; i++){

        if(tracks[i].className.indexOf("selected") > -1)
            tracks[i].className = tracks[i].className.replace("selected","");
    }

    //if element has not allready been selected
    if(!selected){
        //add "selected" class to selected element
        element.className += " selected"
    }
}
