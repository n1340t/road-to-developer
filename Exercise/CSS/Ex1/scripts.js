let paragraph = document.querySelector("#abc");
// let buttonBold = document.querySelector('button:nth-of-type(1)');
// console.log(buttonBold);
// buttonBold.addEventListener('click', function() {
//   // paragraph.classList.toggle('boldText');
//   //method 1
//   console.log(paragraph.style.fontWeight);
//   if(paragraph.style.fontWeight === 'bolder') {
//     paragraph.style.fontWeight = '';
//   } else {
//     paragraph.style.fontWeight = 'bolder';
//   }
// });
class ParaChanger {
  constructor(passedPara) {
    this.classPara = passedPara;
    this.btnBold = document.createElement("button");
    this.btnBold.innerHTML = "Bold";
    this.btnBold.addEventListener("click", e => {
      this.classPara.classList.toggle("boldText");
    });
    // this.addElement = this.addElement.bind(this);
  }
  addElement() {
    // console.log(this);
    document.body.appendChild(this.btnBold);
  }
}

// let obj = new ParaChanger(paragraph);
// obj.addElement();

let myArray = new Array();
for (let i = 0; i < 1000; i++) {
  myArray.push({
    name: "Ngoc" + i,
    value: i
  });
}
function A(arr) {
  return arr.map(elem => ({
    name: elem.name.toUpperCase(),
    value: elem.value * 5
  }));
}
function B(arr) {
  return arr.map(elem => ({
    name: elem.name.toLowerCase(),
    value: elem.value * 3
  }));
}

function C(upper, lower) {
  for(let i = 0; i*3 <= upper.length; i++) {
    upper[3*i].found = [];
    for(let j = 0; j <= 5*i && j < lower.length;j++) {
      if(upper[3*i].value % lower[j].value === 0) {
        upper[3*i].found.push(lower[j]);
      }
    }
  }
}

let upper = A(myArray);
let lower = B(myArray);
C(upper, lower);
document.write(upper);



false.fileExist('bla.txt').then(function(result) {
  // do something
  let keepdoing = 20;
  
  return keepdoing;
}).then(function(result){
  //result = 20;
 let b = 0/0;
  return {status: 200};
}).then(function(result) {
  // result = {status: 200};
  return result;
}).then(run).then()
.catch(function(err) {
  console.log(err);
  if(err === 401) {

  } else if(err === 'Error here') {
    // try again do something
  }
});

 1+1 === 2;
let a = function(parameter) {
  // parameter++;
  parameter();
}


async function run(result) {
  // do something 100 lines of code
  return new Promise(function(resolve, reject) {
    //do something calculate
    if(10/result) {
      resolve('sucess');
      return;
    }
    reject('Divied by 0');
  });
}

function walk() {
  let res = await run(10);
  
}

walk().catch(err => console.log(err));

