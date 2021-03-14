window.onload = init;

var stickyEl;

function init() {
    var button = document.getElementById("add_button");
    button.onclick = createSticky;

    stickyEl = document.getElementById('stickies');

    var stickiesArray = getStickiesArray();

    for (var i = 0; i < stickiesArray.length; i++) {
        var obj = JSON.parse(stickiesArray[i]);
        console.log(obj);
        //var value = localStorage[key];
        addStickyToDOM(obj);
    }
}

function addStickyToDOM(obj) {
    var stickies = document.getElementById("stickies");
    var sticky = document.createElement("li");
    var span = document.createElement("span");
    span.classList.add("sticky");
    span.innerHTML = obj.stickyValue;
    sticky.appendChild(span);
    sticky.addEventListener('click', function () {
        localStorage.removeItem(obj.stickyId);
        sticky.parentNode.removeChild(sticky);
    });
    stickies.appendChild(sticky);
}

function createSticky() {
    //var stickiesArray = getStickiesArray();
    var currentDate = new Date();
    var key = "sticky_" + currentDate.getTime();
    var value = document.getElementById("note_text").value;

    //stickiesArray.push(key);
    //persist(stickiesArray);

    var item = {stickyId: key, stickyValue: value};

    localStorage.setItem(key, JSON.stringify(item));
    addStickyToDOM(item);
}

function getStickiesArray() {
    var stickiesArray = [];
    for (var x = 0; x < localStorage.length; x++) {
        var key = localStorage.key(x);
        if (key.indexOf('sticky') !== -1) {
            stickiesArray.push(localStorage[key]);
        }
    }
    return stickiesArray;

    // var stickiesArray = localStorage.getItem("stickyStorage");
    // if (stickiesArray == null) {
    //     stickiesArray = [];
    //     persist(stickiesArray);
    // } else {
    //     stickiesArray = JSON.parse(stickiesArray);
    // }
    // if (!stickiesArray) {
    //     stickiesArray = [];
    //     localStorage.setItem("stickiesArray", JSON.stringify(stickiesArray));
    // } else {
    //     stickiesArray = JSON.parse(stickiesArray);
    // }
    return stickiesArray;
}

function persist(value) {
    localStorage.setItem("stickyStorage", JSON.stringify(value));
}