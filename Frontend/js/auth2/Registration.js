//Obtiene los inputs
const txtNombre = document.getElementById('txtnombre');
const txtGenero = document.getElementById('txtgenero');
const txtCorreo = document.getElementById('txtcorreo');
const txtUsuario = document.getElementById('txtusuario');
const txtContraseña = document.getElementById('txtcontraseña');

async function register(){
    //Empaqueta la informacion en un archivo JSON
    const data = {
        "correo": txtCorreo.value,
        "pwd": txtContraseña.value,
        "nombre": txtNombre.value,
        "genero": txtGenero.value,
        "usuario": txtUsuario.value
    };

    //Convertir en archivo JSON
    const datajson = await JSON.stringify(data);
    console.log(datajson);
    
    //Peticion a servidor on fetch
    const rawResponse = await fetch("http://127.0.0.1:4000/crateuser",{
        method: "PUT",
        body: datajson,
        headers: { 'Content-Type': 'application/json' }
    })

    //Convierte la respuesta del servidor en un archivo JSON
    const respuesta = await rawResponse.json();
    console.log(respuesta);
    console.log(respuesta.data);

    //Si se registro un usaurio nuevo
    if (rawResponse.status == 200){
        //Mensaje
        alert("Nuevo Usuario Creado");

        //Limpiar input
        limpiarinput();

        //Redirecciona
        //window.location.href = "1_2_login.html"
    }else{
        alert(respuesta.mensaje)
    }

    

}

function limpiarinput(){
        txtNombre.value = "";
        txtGenero.value = "Genero";
        txtCorreo.value = "";
        txtUsuario.value = "";
        txtContraseña.value = "";
}

