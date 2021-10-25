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
