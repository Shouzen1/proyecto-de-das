function rut(){
    var rut=parseInt(document.getElementById("Rut").value)
    
    if (rut < 9 || rut >20) {
        console.log("No Valido");
    }
}