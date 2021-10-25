#Importaciones Librerias
from logging import debug
from flask import Flask, json, request, jsonify
from flask_cors import CORS
#Importaciones Backend
from CRUD_Users import CRUD_User



# Inicializar servidor flask
app = Flask(__name__)
CORS(app)

# Inicializar Archivos Backend
crud_users = CRUD_User()



#////////////////////////////////
#       {ANALISIS LEXICO}
#////////////////////////////////
@app.route('/analisislexico', methods=['PUT'])
def analisisLexico():
    #Obtiene Frase 
    frase = request.json["frase"]

    #/// { Numero de Palabras } ///
    #contador de Palabras
    palabras = 1
    ##Recorre letra por letra en busquedad de un espacio
    for letra in frase:
        #print(letra)
        if letra == ' ' or letra == '  ':
            #Espacio vacio
            palabras += 1
    

    #/// { Numero de Vocales } ///
    dicvocales = ['a','e','i','o','u','A','E','I','O','U']
    vocales = 0
    ##Recorre letra por letra
    for letra in frase:
        #Evalua si es una vocal (si esta en el diccionario)
        for vocal in dicvocales:
            if letra == vocal:
                #si es una vocal la cuenta
                vocales += 1

    #/// { Numero de Consonantes } ///
    letras = 0
    vacio  = 0
    ##Recorre letra por letra
    for letra in frase:
        if letra == ' ' or letra == '  ':
            #si no es un espacio vacio contar
            vacio += 1
        else:
            letras += 1
    
    consonantes = letras - vocales

    #Resultado
    return jsonify({"palabras": palabras, "vocales": vocales, "consonantes": consonantes}), 200
#----------------------------------------------------------------


#/// { Numeros Primos } ///
@app.route('/numerosprimos', methods=['PUT'])
def numerosprimos():
    inferior = request.json["inferior"]
    superior = request.json["superior"]
    print("superior ", superior, " inferior ", inferior)
    numerosprimos = 0
    #ciclo for
    #RANGO (NUM INICIAL, NUM FINAL)
    for num in range(inferior,superior + 1):
        print("numero: ",num)
        #Evalua si es un numero Primo
        esprimo = False
        for n in range(2, num):
            if num % n != 0:
                print(num, " - Es primo")
                esprimo = True
        if esprimo == True:
            numerosprimos += 1

        print(numerosprimos)
    
    return jsonify({"primos": numerosprimos}), 200


#/// { Calculadora } ///
@app.route('/calculadora', methods=['PUT'])
def calculadora():
    numero1 = request.json["numero1"]
    numero2 = request.json["numero2"]
    signo = request.json["signo"]
    resultado = 0

    if signo == "+":
        resultado = numero1 + numero2
    elif signo == "-":
        resultado = numero1 - numero2
    elif signo == "*":
        resultado = numero1 * numero2
    elif signo == "/":
        resultado = numero1 / numero2
    else:
        resultado = "Ocurrio un error: ingrese un signo correcto"
    return jsonify({"resultado": resultado}), 200

#----------------------------------------------------------------






# Crear Usuario
@app.route('/crateuser', methods=['PUT'])
def newuser():
    print('paso aqui ')
    # Recivir del Frontend
    correo = request.json["correo"]
    pwd = request.json["pwd"]
    nombre = request.json["nombre"]
    genero = request.json["genero"]
    usuario = request.json["usuario"]
    #Respuesta del CRUD
    respuesta = crud_users.createuser(correo, pwd, nombre, genero, usuario)
    #return
    return jsonify({"data": respuesta, "mensaje": "Ok"}), 200

# Test
@app.route('/test', methods=['PUT'])
def test():
    correo = request.json["correo"]
    print('paso aqui ',correo)
    return jsonify({"mensaje": "test2"}),200



# Ver todos los posts
@app.route('/post', methods=["GET"])
def posts():
    return jsonify({"mensaje": "Todo bien"}), 200

# Metodo Main
if __name__ == '__main__':
    #Iniciar servidor en el puerto 4000
    app.run(debug=True, port=4000)
