from .constantes import clientes, peliculas
from .funciones_aux import pedirDatos, buscarValor

def iniciarSesion():
    dni = pedirDatos("dni")
    resultado = buscarValor(dni, clientes, 0)
    if resultado == False:
        print("¡Usuario inexistente!")
        return False
    else:
        password = pedirDatos("password")
        acceso = 0
        for i in resultado:
            i = i.split(",")
            if i[0] == dni and i[7] == password:
                acceso = 1
            if acceso == 1:          
                print("¡Acceso correcto!")
                return True
            else:
                print("¡Acceso Incorrecto!")
                return False

def alquilarPeli():
    dni = pedirDatos("dni")
    resultado = buscarValor(dni, clientes, 0)
    if resultado == False:
        print("¡Usuario incorrecto!")
        return False
    
    archivo = open(clientes, "r")
    archivoLeidoClientes = archivo.readlines()
    archivo.close()

    cliente = ""
    for i in archivoLeidoClientes:
        if i[:8] == dni:
            cliente = i.strip()

    if cliente == "":
        print("¡No se encontró el cliente!")
        return False

    clienteDatos = cliente.split(",")
    if clienteDatos[7] == "A":
        print("¡El usuario ya se encuentra alquilando una película!")
        return False

    codigo = input("Ingrese el código de la película que desea alquilar: ")
    resultado = buscarValor(codigo, peliculas, 0)
    if resultado == False:
        print("¡Código inválido!")
        return False
    
    if len(resultado) > 6 and resultado[6] == "A":
        print("¡La película se encuentra en alquiler!")
        return False

    archivo = open(peliculas, "r")
    archivoLeidoPeliculas = archivo.readlines()
    archivo.close()

    pelicula = ""
    for i in archivoLeidoPeliculas:
        if i[:4] == codigo:
            pelicula = i.strip()

    if pelicula == "":
        print("¡Película no encontrada!")
        return False
    
    clienteModi = cliente.replace(",L,", ",A,")
    clienteModi2 = clienteModi.replace(",0", "," + codigo)

    peliculaModi = pelicula.replace(",L,", ",A,")
    peliculaModi2 = peliculaModi.replace(",0", "," + dni)

    archivoLeidoClientesNormalizado = [line.strip() for line in archivoLeidoClientes]
    archivoLeidoClientesNormalizado[archivoLeidoClientesNormalizado.index(cliente)] = clienteModi2

    archivoLeidoPeliculasNormalizado = [line.strip() for line in archivoLeidoPeliculas]
    archivoLeidoPeliculasNormalizado[archivoLeidoPeliculasNormalizado.index(pelicula)] = peliculaModi2

    archivo = open(clientes, "w")
    for i in archivoLeidoClientesNormalizado:
        archivo.write(i + "\n")
    archivo.close()

    archivo = open(peliculas, "w")
    for i in archivoLeidoPeliculasNormalizado:
        archivo.write(i + "\n")    
    archivo.close()

    print("¡Has alquilado la película!")
    
def devolverPeli():
    dni = pedirDatos("dni")
    resultado = buscarValor(dni,clientes,0)
    if resultado == False:
        print("¡Usuario incorrecto!")
        return False
    
    codigo = input("Ingrese el codigo de la pelicula que desea devolver: ")
    resultado = buscarValor(codigo,peliculas,0)
    if resultado == False:
        print("¡Codigo de pelicula invalido!")
        return False
    
    resultado = buscarValor(dni,peliculas,7)
    if dni != resultado:
        print("¡El usuario no corresponde con la pelicula alquilada!")
        return False
    
    archivo = open(clientes,"r")
    archivoLeidoClientes = archivo.readlines()
    archivo.close()

    archivo = open(peliculas,"r")
    archivoLeidoPeliculas = archivo.readlines()
    archivo.close()

    cliente = ""
    for i in archivoLeidoClientes:
        if i[:8] == dni:
            cliente = i
    
    pelicula = ""
    for i in archivoLeidoPeliculas:
        if i[:4] == codigo:
            pelicula = i

    clienteModi = cliente.replace(",A,",",L,")
    clienteModi2 = clienteModi.replace(codigo+"\n","0\n")

    peliculaModi = pelicula.replace(",A,",",L,")
    peliculaModi2 = peliculaModi.replace(dni+"\n","0\n")

    archivoLeidoClientes.remove(cliente)
    archivoLeidoClientes.append(clienteModi2)

    archivoLeidoPeliculas.remove(pelicula)
    archivoLeidoPeliculas.append(peliculaModi2)

    archivo = open(clientes,"w")
    for i in archivoLeidoClientes:
        archivo.write(i)
    archivo.close()

    archivo = open(peliculas,"w")
    for i in archivoLeidoPeliculas:
        archivo.write(i)
    archivo.close()

    print("¡Has devuelto la pelicula satisfactoriamente!")

def verPeliculas():    
    archivo = open(peliculas, "r")
    archivoLeido = archivo.readlines()
    archivo.close()
    for i in archivoLeido:
        i = i.split(",")
        print(i)

def verPeliculasDispo():    
    archivo = open(peliculas, "r")
    archivoLeido = archivo.readlines()
    archivo.close()
    for i in archivoLeido:
        i = i.split(",")
        if i[6] == "L":
            print(i)