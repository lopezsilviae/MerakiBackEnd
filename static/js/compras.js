const formCompras = document.getElementById("procesar_compra")

function RecibirCompra(e){
    //cancelamos el evento por default
    e.preventDefault()
    //leer datos del form
    let cNombre = document.getElementById("nombre").value
    let cTelefono = document.getElementById("telefono").value
    let cEmail = document.getElementById("email").value
    let cDireccion = document.getElementById("direccion").value
    let cCodpostal = document.getElementById("codpostal").value
    let cProducto = document.getElementById("imagen").value
    respuesta.innerHTML=""
    respuesta.innerHTML+=`
        <div >
            <div >
                <span>Recibimos tu Pedido. </span>
                <span>Nos pondremos en contacto a la brevedad</span>
                <h3> ${cNombre} !!!
                </h3>
            </div>
            
        </div>
        `
    }
    
    formCompras.addEventListener("submit",RecibirCompra)   
    