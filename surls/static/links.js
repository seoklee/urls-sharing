/**
 * Created by lee on 1/6/16.
 */

"use strict";


//create &delete a new text area
setInterval(function () {
    var links = document.getElementsByName("links");
    var index = links.length - 1;
    var last_link = links[index];
    //input entered & needs another text box
    if (last_link.value != '') {
        var element = document.createElement('input');
        var div = document.getElementById("link-group");
        element.setAttribute("rows", 7);
        element.setAttribute("name", "links");
        element.setAttribute("id", "links");
        element.setAttribute("class", "form-control");
        element.setAttribute("type", text);
        div.appendChild(element);
    }

    //check every text box except the last box. if it's empty, delete.
    //if a text box is remove, move the cursor focus to the previous text box
    for (var i = 0; i < links.length - 1; i++) {
        var curr = links[i];
        if (curr.value === '') {
            curr.remove();
            //if the first box was removed, place the cursor at the new first box
            if (links.length === 1) {
                links[0].select();
                links[0].selectionStart = links[0].value.length;
            }
            //if a box besides the first box is removed, place the cursor at the previous box
            else if (links.length > 1) {
                links[i - 1].select();
                links[i - 1].selectionStart = links[i - 1].value.length;
            }
        }
    }
}, 100);