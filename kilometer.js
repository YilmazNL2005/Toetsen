// Schrijf een functie die je vertelt of het mogelijk is om bij het tankstation te komen of niet.
// De functie moet true teruggeven als het mogelijk is en false als dat niet zo is.

function kanBereikenTankstation(kilometersNaarTankstation, kilometersPerLiter, resterendeLiters) {
    let aantal_mog_km = resterendeLiters / kilometersPerLiter;
    let haalbaar = kilometersNaarTankstation - aantal_mog_km;
    if (haalbaar <= 0){
        return true;
    } else if (haalbaar > 0); {
        return false
    }
}


let km_naar_tankstation = prompt("Hoeveel hele km is het nog om naar het tankstation te kunnen? ");
let km_per_l = prompt("Hoeveel km kan je rijden per 1 liter benzine? ");
let aantal_liters = prompt("Hoeveel liter benzine heb je nog over? ");
console.log(km_naar_tankstation);
console.log(km_per_l);
console.log(aantal_liters);



console.log(kanBereikenTankstation(km_naar_tankstation, km_per_l, aantal_liters));