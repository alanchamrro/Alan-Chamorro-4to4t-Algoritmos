numero_contacto = []
nombre_contacto = []
while True:
    menusito = int(input("""
                        1- agregar contactos
                        2- buscar nombre del contacto
                        3- salir"
                        
                        elegi:"""))
    if menusito == 1:

        numero = int(input("agrega el numero de contacto:"))
        nombre = input("agrega el nombre del contacto:")

        numero_contacto.append(numero)
        nombre_contacto.append(nombre)
        mostrar_contactos = print(f"tus contactos son: {nombre_contacto}")

    elif menusito == 2:

        buscar = input("ingresa el nombre del contacto: ")
        if buscar in nombre_contacto:
            indice = nombre_contacto.index(buscar)
            print(f" {nombre_contacto[indice]}: {numero_contacto[indice]}")
        else:
             print(" contacto no encontrado.")




    else:
        print("saliste del programa")
        break