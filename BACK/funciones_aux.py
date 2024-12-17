def pedirDatos(dato):
    datoPedido = input(f"Ingrese su {dato}: ")
    return datoPedido

def buscarValor(valor,BBDD,ubicacion):
    archivo = open(f"{BBDD}","r")
    lineas = archivo.readlines()
    archivo.close()
    for i in lineas:
        i = i.split(",")
        if valor == i[ubicacion]:
            return lineas
    return False
