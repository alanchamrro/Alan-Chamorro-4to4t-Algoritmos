numero_contacto = []
nombre_contacto = []

while True:
    menusito = int(input("""
    menú 
    1- Agregar contacto
    2- Buscar contacto por nombre
    3- Mostrar todos los contactos
    4- Salir

    Elegí una opción: """))

    if menusito == 1:
        numero = input("Agregá el número de contacto: ")
        nombre = input("Agregá el nombre del contacto: ")

        numero_contacto.append(numero)
        nombre_contacto.append(nombre)

        print("Contacto agregado correctamente")

    elif menusito == 2:
        buscar = input("Ingresá el nombre del contacto: ")
        if buscar in nombre_contacto:
            indice = nombre_contacto.index(buscar)
            print(f" {nombre_contacto[indice]}: {numero_contacto[indice]}")
        else:
            print(" Contacto no encontrado.")

    elif menusito == 3:
        print(" Lista de contactos:")
        if len(nombre_contacto) == 0:
            print("No tenés contactos guardados.")
        else:
            for i in range(len(nombre_contacto)):
                print(f"{nombre_contacto[i]}: {numero_contacto[i]}")

    elif menusito == 4:
        print("saliste del programa.")
        break

    else:
        print(" opción inválida, probá de nuevo.")
