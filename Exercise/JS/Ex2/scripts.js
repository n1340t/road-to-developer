let btn = document.querySelector("#createBoxes");
let father = document.querySelector("#father");

btn.addEventListener("click", function() {
  let childDiv = document.createElement("div");

  childDiv.className = 'smallDiv';
  //random position
  childDiv.style.top = `${getRandomIntInclusive(0, 600 - 40)}px`;
  childDiv.style.left = `${getRandomIntInclusive(0, 600 - 40)}px`;
  father.appendChild(childDiv);



  function moveAt(pageX, pageY) {
    let childLeft = pageX - childDiv.offsetWidth / 2 - 10;
    let childTop = pageY - childDiv.offsetHeight / 2 - 35;
    // console.log(childLeft, childTop);
    if (isInRange(childLeft, 0, 560) && isInRange(childTop, 0, 560)) {
      childDiv.style.left = childLeft + "px";
      childDiv.style.top = childTop + "px";
    } else {
      childDiv.removeEventListener("mousemove", onMouseMove);
    }
  }

  function onMouseMove(event) {
    moveAt(event.pageX, event.pageY);
  }


  childDiv.addEventListener("mousedown", function(event) {
    //moveAt(event.pageX, event.pageY);
    // centers the ball at (pageX, pageY) coordinates

    // (3) move the div on mousemove
    childDiv.addEventListener("mousemove", onMouseMove);

    // (4) drop the div, remove unneeded handlers
    childDiv.onmouseup = function () {
      console.log('remove?????');
      childDiv.removeEventListener("mousemove", onMouseMove);
      childDiv.onmouseup = null;
    };
  });
});
function isInRange(val, lower, upper) {
  return lower <= val && val <= upper;
}
function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive
}
