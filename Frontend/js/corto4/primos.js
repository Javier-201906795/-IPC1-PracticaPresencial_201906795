//Obtiene los input
const txtinicial = document.getElementById('txtInicial');
const txtfinal = document.getElementById('txtFinal');
const txtprimos = document.getElementById('txtprimos');
const resultado = document.getElementById('resultado');


async function primos(){

    //alert('Inicial: '+ txtinicial.value + " Final: "+ txtfinal.value);


    //Evaluar si esta vacio


    if(txtinicial.value == null || txtinicial.value == ' ' || txtinicial.value ==''){
        labelalerta.innerHTML += 'Ingrese un numero inicial porfavor';
        labelalerta.style.visibility = "visible";
    }else{
        //Si no esta vacio

        const data = {
            "inferior": parseInt(txtinicial.value),
	        "superior": parseInt(txtfinal.value)
        };
        //Convertir en archivo JSON
        const datajson = await JSON.stringify(data);
        console.log(datajson);

        //Peticion a servidor on fetch
        const rawResponse = await fetch("http://127.0.0.1:4000/numerosprimos",{
            method: "PUT",
            body: datajson,
            headers: { 'Content-Type': 'application/json' }
        })

        //Convierte la respuesta del servidor en un archivo JSON
        const respuesta = await rawResponse.json();
        console.log(respuesta);

        if (rawResponse.status == 200){
            alert("Numeros Primos en el rango  =>" +respuesta.primos);
            txtprimos.innerHTML = respuesta.primos;
            resultado.style.visibility = "visible";
        }

        
        
    }
    
}