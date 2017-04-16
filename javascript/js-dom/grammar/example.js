/**
 * Created by lth on 17-4-16.
 */

// var
var mood = "happy";
var age = 33;

alert(mood);
alert(age);

// data type
//string
var mood1 = 'happy';
var mood2 = "happy";
var mood3 = "don't ask";
var height = "about 5'10\" tall";
alert(height);
//number
var age1 = 33.25;
var temperature = -20;
var temperature1 = -20.33;
//boolean
var sleeping = true;
//array
var beatles = Array(4);
beatles[0] = "John";
beatles[1] = "Paul";
beatles[2] = "George";
beatles[3] = "Ringo";
var beatles1 = Array("John", "Paul", "George", "Ringo");
var beatles2 = ["John", "Paul"];
//assoc-array
var lennon = Array();
lennon["name"] = "John";
lennon["year"] = 1940;
lennon["living"] = false;

// object
var lennon1 = Object();
lennon1.name = "John";
lennon1.year = 1940;
lennon1.living = false;

// operation
1 + 4
1 + 4 * 5
var total = (1 + 4) * 5;
alert("10" + 20);
alert(10 + 20);

// conditional statement
if (1 > 2) {
    alert("The world has gone bad");
}

// function
function shout() {
    var beatles = ["John", "Paul", "George", "Ringo"];
    for (var count = 0; count < beatles.length; count++)
        alert(beatles[count]);
}