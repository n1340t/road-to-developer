let floatingForm;
let btn;
let selectShape;
let x, y;
let cvs;
window.onload = function() {
  cvs = document.getElementById("canvas");
  floatingForm = document.querySelector(".formClass");
  cvs.onclick = showForm;
  selectShape = document.querySelector("#shapeChoice");
  selectShape.addEventListener("change", onChangeSelect);

  btn = document.querySelector("button");
  btn.addEventListener("click", drawShape);
};
function drawShape() {
  let height = document.querySelector("#heightRec");
  let width = document.querySelector("#widthRec");
  let radius = document.querySelector("#radiusCircle");
  let ctx = cvs.getContext("2d");
  width = parseInt(width.value);
  height = parseInt(height.value);
  radius = parseInt(radius.value);
  let coorX = x - width / 2;
  let coorY = y - height / 2;
  if (selectShape.value === "square") {
    ctx.fillStyle = "#FF0000";
    ctx.fillRect(coorX, coorY, width, height);
  } else if (selectShape.value === "circle") {
    coorX = x - radius;
    coorY = y - radius;
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, 2 * Math.PI);
    ctx.fillStyle = "#FFB6C1";
    ctx.fill();
  }
  floatingForm.classList.toggle("formClass");
}
function onChangeSelect(e) {
  let val = e.target.value;
  btn.className = "";
  let divInput = document.querySelectorAll("canvas + div div");
  if (val === "square") {
    divInput[0].className = "";
    divInput[1].className = "";
    divInput[2].className = "formClass";
  } else if (val === "circle") {
    divInput[2].className = "";
    divInput[0].className = "formClass";
    divInput[1].className = "formClass";
  } else {
    divInput[0].className = "formClass";
    divInput[1].className = "formClass";
    divInput[2].className = "formClass";
  }
}
function showForm(e) {
  x = e.pageX;
  y = e.pageY;
  floatingForm.classList.toggle("formClass");
  floatingForm.style.top = y + "px";
  floatingForm.style.left = x + "px";
}
