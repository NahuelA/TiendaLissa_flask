/* // Manejador de eventos del template venta
window.addEventListener("load", cargaPagina());
function cargaPagina() {
    let btn = document.getElementById("check-env").addEventListener("click", pay_check());
} */

let btn = document.getElementById("check-env").addEventListener("click", pay_check);

function pay_check(){
    
    let arr = ['0','1','2','3','4','5','6','7']
    let check = "pay-check"
    for (const i in arr) {
        
        check += i
        let checks = document.getElementById(check).checked;

        if (checks){
            
            document.getElementById(check).value = "debe";
        }

        check = "pay-check"
    }
}

