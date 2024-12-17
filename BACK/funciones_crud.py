from .constantes import clientes
from .funciones_aux import pedirDatos, buscarValor

def registrarse():
    dni = pedirDatos("dni")
    resultado = buscarValor(dni,clientes,0)
    if resultado == False:
        nombre = pedirDatos("nombre")
        apellido = pedirDatos("apellido")
        direccion = pedirDatos("direccion")
        telefono = pedirDatos("telefono")
        fechaNaci = pedirDatos("fecha de nacimiento")
        email = pedirDatos("email")
        password = pedirDatos("password")
        print("¡Registro exitoso!")
        datos = dni + "," + nombre + "," + apellido + "," + direccion + "," + telefono + "," + fechaNaci + "," + email + "," + password + ",L,0\n"
        archivo = open(clientes,"a")
        archivo.write(datos)
        archivo.close()
    else:
        print("¡Usuario existente!")
        
def verDatos():
    archivo = open(clientes,"r")
    archivoLeido = archivo.readlines()
    for i in archivoLeido:
        print(i)
    
def modificarMail():    
    dni = pedirDatos ("dni")
    archivo = open(clientes,"r")
    archivoLeido = archivo.readlines()
    cliente = None
    indice = None
    for i in archivoLeido:
        if dni in i:
            cliente = i
            indice = archivoLeido.index(i)
    archivo.close()
    
    if cliente != None:
        oldEmail = pedirDatos ("email")
        newEmail = pedirDatos ("nuevo email")
        datos = cliente.replace(oldEmail,newEmail)
        archivoLeido[indice] = datos
        archivo = open(clientes, "w")
        for i in archivoLeido:
            archivo.write(i)
        print("¡Email modificado!")
    else:
        print("¡No se encontro el cliente!")

def eliminarUsuario():
    dni = pedirDatos("dni")
    password = pedirDatos("password")
    archivo = open(clientes,"r")
    archivoLeido = archivo.readlines()
    cliente = None
    estado = None
    
    for i in archivoLeido:
        if dni in i:
            linea = i.strip().split(",")
            if len(linea) > 8:
                estado = linea[8]
    
    if estado != "L":
        cliente = print("¡No puedes darte de baja ya que tienes una pelicula en alquiler!")
        archivo.close()
        return False
        
    for i in archivoLeido:
        if dni in i and password in i:
            cliente = i
    
    if cliente != None:
        archivoLeido.remove(cliente)
        print("¡Cliente eliminado!")
    else:
        print("No se encontro el cliente")
    archivo = open(clientes, "w")

    for i in archivoLeido:
        archivo.write(i)
    archivo.close()