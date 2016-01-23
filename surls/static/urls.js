(function () {
    var a = document.getElementsByClassName("content-url")[0];
    var selection = window.getSelection();
    var range = document.createRange();
    range.selectNodeContents(a);
    selection.removeAllRanges();
    selection.addRange(range);
})();
