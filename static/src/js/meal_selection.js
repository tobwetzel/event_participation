/**
 * Created by Tobias on 06.04.2015.
 */

function onSelectOption(value){

    var input_other = document.getElementById('input-meal-other');

    if(value == "Other"){
        //display input field when "other" is selected
        input_other.setAttribute('type','text');
    } else {
        //hide input field when "other" is not selected
        input_other.setAttribute('type','hidden');
    }

    var e = document.getElementById("selector-meals");
    var text = e.options[e.selectedIndex].text;

    var input_type = document.getElementById('input-meal-type');
    input_type.setAttribute("value", text);
}