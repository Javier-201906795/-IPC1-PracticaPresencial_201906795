const txtCorreo = document.getElementById('txtemail')
const txtPassword = document.getElementById('txtcontraseña')

async function login(){
            //alert('Correo: ' + txtCorreo.value + " Contraseña: " + txtPassword.value);

            //Crea un archivo JSON con la informacion requerida para ingresar
            const data = {"correo": txtCorreo.value, "pwd": txtPassword.value}
            let datajson = JSON.stringify(data)
            console.log(datajson)


            //Peticion a servidor on fetch
            const rawResponse = await fetch("http://127.0.0.1:4000/login",{
                method: "POST",
                body: JSON.stringify(data),
                headers: { 'Content-Type': 'application/json' }
            })
            
            //Convierte la respuesta del servidor en un archivo JSON
            const respuesta = await rawResponse.json()
            console.log(respuesta)

            //Guardar informacion
            //LocalStorage para alamacer informacion
            if (rawResponse.status == 200){
                localStorage.setItem("usuario", JSON.stringify(respuesta))
                window.location.href = "1_1_Index.html"
            }else{
                alert(respuesta.mensaje)
            }
            
}