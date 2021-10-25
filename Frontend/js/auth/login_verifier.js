function verficarInicio(){
    //Variable con los datos del Usuario
    const usuario = localStorage.getItem("usuario")
    //Verifica si esta vacio
    if(!usuario){
        //Si es asi redirige a login
        window.location.href = "1_2_login.html"
    }
}