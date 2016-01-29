/**
 * Created by lee on 1/6/16.
 */

"use strict";


//js simple url validation
(function () {
    var expression = /[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi;
    var regex = new RegExp(expression);
    var first_elem = document.getElementsByClassName("input-group")[0].children[1];
    first_elem.setAttribute("pattern", regex.source);
})();


//create &delete a new text area
(function () {
    setInterval(function () {
        var links = document.getElementsByClassName("input-group");
        var index = links.length - 1;
        var last_link = links[index];
        //input entered & needs another text box
        if (last_link.children[1].value != '') {
            console.log("cloning and appending");
            var parent = document.getElementById("link-group");
            var inputGroup = last_link.cloneNode(true);
            inputGroup.children[0].innerHTML = links.length + 1;
            inputGroup.children[1].value = '';
            inputGroup.children[1].style.backgroundColor = "";
            parent.appendChild(inputGroup);
        }

        //check every text box except the last box. if it's empty, delete.
        //if a text box is remove, move the cursor focus to the previous text box
        for (var i = 0; i < links.length - 1; i++) {
            var curr = links[i];
            if (curr.children[1].value === '') {
                curr.remove();
                // renumber inputs
                for (var j = i; j < links.length; j++) {
                    links[j].children[0].innerHTML = j + 1;
                }
                //if the first box was removed, place the cursor at the new first box
                if (i === 0) {
                    links[0].children[1].select();
                    links[0].children[1].selectionStart = links[0].children[1].value.length;
                }
                //place the cursor at the previous box
                else {
                    links[i - 1].children[1].select();
                    links[i - 1].children[1].selectionStart = links[i - 1].children[1].value.length;
                }
            }
        }
    }, 100);
})();

//
function deleteLast() {
    var links = document.getElementsByClassName("input-group");
    var index = links.length - 1;
    var last_link = links[index];
    last_link.remove();
}

//highlight "wrong" urls
(function () {
    var failed_links = document.getElementsByClassName("failed-links");
    var links = document.getElementsByClassName("input-group");
    for (var i = 0; i < failed_links.length; i++) {
        var index = parseInt(failed_links[i].innerHTML);
        links[index].children[1].style.backgroundColor = "#f2dede";
    }
})();