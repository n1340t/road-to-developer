var http = require('http');
var url = require('url');
var fs = require('fs');
var open = require('open');

var server = http.createServer(function(request,response){
  var queryObject = url.parse(request.url,true).query;
  console.log(request.url);
  response.end(queryObject.callback+'('+JSON.stringify(makeRandomData())+')');
});
server.listen(8080, function(){
  open(__dirname+'./index.html');
});

var names = [
"Marilou",
"Leota",
"Maile",
"Sparkle",
"Malika",
"Joselyn",
"Sheena",
"Matilde",
"Renaldo",
"Ocie",
"Rina",
"Darcel",
"Corinna",
"Freeman",
"Hilde",
"Jean",
"Mohammad",
"Trenton",
"Valarie",
"Eusebio"
];

function makeRandomData() {
  return {"name": names[Math.round(20*Math.random())], "age":Math.round(100*Math.random())};
}