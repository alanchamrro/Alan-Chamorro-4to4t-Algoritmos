def busqueda_secuencial():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    buscar = int(input("Qué número desea buscar?: "))
    for i in range(len(lista)):
        if lista[i] == buscar:
            return i
    return -1


def busqueda_binaria():
    arreglo = [2, 4, 7, 8, 12, 15, 19]
    valor = int(input("Qué número desea buscar?: "))
    izquierda = 0
    derecha = len(arreglo) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arreglo[medio] == valor:
            return medio
        elif arreglo[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


def ordenamiento_burbuja():
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("lista original:", lista)
    n = len(lista)

    for i in range(n - 1):
        Hay_Cambio = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                Hay_Cambio = True
        if not Hay_Cambio:
            break

    print("lista ordenada (burbuja):", lista)
    return lista


def ordenamiento_seleccion():
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("lista original:", lista)
    n = len(lista)

    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]

    print("lista ordenada (selección):", lista)
    return lista



while True:
    menu = int(input("""Elegí una opción:

       1- Buscar en la lista
       2- Ordenar la lista
       3- Salir
       ---->: """))

    if menu == 1:
        elegir = int(input("""con cuál método querés buscar?
        1- Búsqueda secuencial
        2- Búsqueda binaria
        ---->: """))

        if elegir == 1:
            indice = busqueda_secuencial()
            if indice != -1:
                print(f"elemento encontrado en la posición {indice}")
            else:
                print("elemento no encontrado")

        elif elegir == 2:
            indice = busqueda_binaria()
            if indice != -1:
                print(f"elemento encontrado en la posición {indice}")
            else:
                print("elemento no encontrado")

    elif menu == 2:
        elegir2 = int(input("""Elegí el método de ordenamiento:
        1- Ordenamiento por burbuja
        2- Ordenamiento por selección
        ---->: """))
        if elegir2 == 1:
            ordenamiento_burbuja()
        elif elegir2 == 2:
            ordenamiento_seleccion()

    elif menu == 3:
        print(" saliendo del programa...")
        break
    else:
        print("no")












