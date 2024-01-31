"use strict";
let passtring = "";
let eodstring = "";
let colorstring = "";
let rounum = (Math.floor(Math.random() * 38));
let rounumlist = ["0", "34", "10", "21", "28", "4", "18", "9", "27", "22", "12","3",
                  "17", "20", "11", "33", "2", "10", "32", "00", "15", "8", "25", "1",
                  "31", "20", "14", "30", "7","24", "29", "35", "6", "13", "23", "19", "5", "36"];







if(rounum <= 18){
    passtring = "Manque";
} else{
    passtring = "Passe";
}

if (rounum%2 == 0){
    eodstring = "Pair";
} else{
    eodstring = "Impair";
}

let roustring = rounum.toString();
if (roustring === "37"){
    roustring = "00";
}

if(rounumlist.indexOf(roustring) % 2 == 0){
    colorstring = "Rouge";
} else{
    colorstring = "Noir";
}
console.log(roustring, colorstring, eodstring, passtring);