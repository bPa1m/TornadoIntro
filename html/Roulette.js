

"use strict";
let passtring = "";
let passhex = "";
let eodstring = "";
let eodhex = "";
let colorstring = "";
let colorhex = "";
let texthex = "";
let rounumlist = ["0", "34", "10", "21", "28", "4", "18", "9", "27", "22", "12","3",
                  "17", "20", "11", "33", "2", "10", "32", "00", "15", "8", "25", "1",
                  "31", "20", "14", "30", "7","24", "29", "35", "6", "13", "23", "19", "5", "36"];

let rounum = (Math.floor(Math.random() * 38));
let tbl = document.createElement("table");

function myFunction(){
    rounum = (Math.floor(Math.random() * 38));

    if(rounum <= 18){
        passtring = "Manque";
        passhex = "194D33";
    } else{
        passtring = "Passe";
        passhex = "#DCE775";
    }

    if (rounum%2 == 0){
        eodstring = "Pair";
        eodhex = "#EAD6EA";
    } else{
        eodstring = "Impair";
        eodhex = "#EE91ED";
    }

    let roustring = rounum.toString();
    if (roustring === "37"){
        roustring = "00";
    }

    if(rounumlist.indexOf(roustring) % 2 == 0){
        colorstring = "Rouge";
        colorhex = "#CA292C";
        texthex = "#000000";
    } else{
        colorstring = "Noir";
        colorhex = "#000000";
        texthex = "#ffffff";
    }
    console.log(roustring, colorstring, eodstring, passtring);
    var row = tbl.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    cell1.innerHTML = roustring;
    cell2.innerHTML = colorstring;
    cell3.innerHTML = eodstring;
    cell4.innerHTML = passtring;
    cell2.style.backgroundColor = colorhex;
    cell2.style.color = texthex;
    cell3.style.backgroundColor = eodhex
    cell4.style.backgroundColor = passhex;
}


document.body.appendChild(tbl);



