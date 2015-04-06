/**
 * Created by Tobias on 06.04.2015.
 */

function onSelectOption(value){

    var input = document.getElementById('input-meal-other');

    if(value == "other"){
        //display input field when "other" is selected
        input.setAttribute('type','text');
    } else {
        //hide input field when "other" is not selected
        input.setAttribute('type','hidden');
    }
}