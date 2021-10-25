# Importa metodo constructor de usuarios
from P_usuario import User

#Nueva Clase
class CRUD_User:
    # Constructor
    def __init__(self):
        #Simular base de datos (Array Vacio)
        self.usuarios = []

    # CRUD => CREATE READ UPDATE DELETE

    # CREATE
    def createuser(self, correo, pwd, nombre, genero, usuario):
        #Obtiene el id con el numero de elementos en el array usuarios
        id = len(self.usuarios)
        #Nuevo usuario
        nuevousuario = User(id, correo, pwd, nombre, genero, usuario)
        #Agrega el usaurio al listado 
        self.usuarios.append(nuevousuario)
        #IMPRIMIR usuario
        print("Nuevo usaurio: ",nuevousuario)
        return id

    #READ
    def readuser(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario.dump()
            else:
                return "No se encontro el usuario"

    #TEST
    def test(self):
        mensaje = "hola"
        return mensaje