const formCarga = document.getElementById("form_contacto")

function RecibirConsulta(e){
    //cancelamos el evento por default
    e.preventDefault()
    //leer datos del form
    let coNombre = document.getElementById("nombreCt").value
    let cCelular = document.getElementById("celularCt").value
    let cEmail = document.getElementById("emailCt").value
    let cCliente = document.getElementById("clienteCt").value
    let cConsulta = document.getElementById("consultaCt").value
    respuesta.innerHTML=""
    respuesta.innerHTML+=`
        <div>
            <div>
                <span>Recibimos tu consulta. </span>
                <span>Gracias</span>
                <h3> ${coNombre} !!!</h3>
            </div>
            
        </div>`

}

    formCarga.addEventListener("submit",RecibirConsulta)

    