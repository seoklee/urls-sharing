/**
 * Created by lee on 1/6/16.
 */

"use strict";


//create &delete a new text area
setInterval(function () {
    var index = document.getElementsByName("links").length - 1;
    var last_link = document.getElementsByName("links")[index];
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

    //check every text box except the first and last box. if it's empty, delete.
    for (var i = 1; i < document.getElementsByName("links").length - 1; i++) {
        var curr = document.getElementsByName("links")[i];
        if (curr.value == '') {
            curr.remove();
        }
    }
}, 100);