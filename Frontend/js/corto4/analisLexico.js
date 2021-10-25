//Obtiene los input
const txtfrase = document.getElementById('txtFrase');
const labelalerta = document.getElementById('labelalerta');
const resultado = document.getElementById('resultado');
const palabras = document.getElementById('txtpalabras');
const vocales = document.getElementById('txtvocales');
const consonantes = document.getElementById('txtconsonantes');



async function anilislexico(){
    //Evaluar si esta vacio
    if(txtfrase.value == null || txtfrase.value == ' ' || txtfrase.value ==''){
        labelalerta.innerHTML = 'ingrese un texto porfavor';
        labelalerta.style.visibility = "visible";
    }else{
        //Si no esta vacio

        const data = {
            "frase": txtfrase.value
        };
        //Convertir en archivo JSON
        const datajson = await JSON.stringify(data);
        console.log(datajson);

        //Peticion a servidor on fetch
        const rawResponse = await fetch("http://127.0.0.1:4000/analisislexico",{
            method: "PUT",
            body: datajson,
            headers: { 'Content-Type': 'application/json' }
        })

        //Convierte la respuesta del servidor en un archivo JSON
        const respuesta = await rawResponse.json();
        console.log(respuesta);

        if (rawResponse.status == 200){
            palabras.innerHTML = respuesta.palabras;
            vocales.innerHTML = respuesta.vocales;
            consonantes.innerHTML = respuesta.consonantes;
            resultado.style.visibility = "visible";
        }

        
        
    }
    
}