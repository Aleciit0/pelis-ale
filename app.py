from BACK import funciones_crud, funciones_np

inter = 1

while inter == 1:
    print("¡Bienvenido a la App PelisAle!")
    opcion = int(input("Ingrese una opcion:\n1. Registro\n2. Login\n3. Salir\n"))
    if opcion == 1:
        print("Creando registro...")
        funciones_crud.registrarse()
    elif opcion == 2:
        print("Logeando...")
        usuarioValido = funciones_np.iniciarSesion()
        if usuarioValido == False:
            continue
        cerrarSesion = 0
        while cerrarSesion == 0:
            opcion = int(input("Ingrese una opcion:\n1. Alquilar pelicula\n2. Devolver pelicula\n3. Ver peliculas disponibles\n4. Ver todas las peliculas\n5. Ver mis datos\n6. Modificar email\n7. Darse de baja\n8. Cerrar sesion\n"))
            if opcion == 1:
                funciones_np.alquilarPeli()
                continue
            elif opcion == 2:
                funciones_np.devolverPeli()
                continue
            elif opcion == 3:
                funciones_np.verPeliculasDispo()
            elif opcion == 4:
                funciones_np.verPeliculas()
            elif opcion == 5:
                funciones_crud.verDatos()
            elif opcion == 6:
                funciones_crud.modificarMail()
            elif opcion == 7:
                pregunta = int(input("¿Estas seguro que quieres darte de baja?\n1. Si\n2. No\n"))
                if pregunta == 1:
                    funciones_crud.eliminarUsuario()
                    cerrarSesion = 1
                elif pregunta == 2:
                    pass
                else:
                    print("Ingrese una opcion valida")
            elif opcion == 8:
                print("Cerrando sesion...")
                print("¡Sesion finalizada con exito!")
                cerrarSesion = 1
            else:
                print("¡Ingrese una opcion correcta!")
    elif opcion == 3:
        print("¡Vuelva pronto!")
        inter = 0
    else:
        print("Ingrese una opcion valida.")
