<?php

header("Access-Control-Allow-Origin: *");
$names = array(
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
);
    
function makeRandomData() {
        global $names;
      return '{"name": "'.$names[rand(0, count($names))].'", "age":'.round(rand(0, 100)).'}';
}

echo $_GET['callback'] . '(' . makeRandomData() . ')';

?>