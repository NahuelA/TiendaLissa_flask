// Función que acredita el pago de la deuda
let btn = document.getElementById("paid-send").addEventListener("click", paid_check);

let length_fiados = document.getElementsByClassName("paid-out-class").length;
let all_fiados = document.getElementsByClassName("paid-out-class");
//let id_fiado = document.getElementById("paid-out")


function paid_check(){

    for (let i=0; i <= length_fiados; i++){

        let checks = document.getElementsByClassName("paid-out-class")[i].checked;

        if (checks){
            document.getElementsByClassName("paid-out-class")[i].value = "pagado";
        }

    }

}

