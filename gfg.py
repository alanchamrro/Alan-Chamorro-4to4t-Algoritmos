import random


def ejercicio1(nombres):
    mas_larga = ""
    for nombre in nombres:
        if len(nombre) > len(mas_larga):
            mas_larga = nombre
    print("la palabra con mas caracteres es:", mas_larga)


def ejercicio2(nombres):
    vocales = "aeiou"
    contador_vocales = 0
    for nombre in nombres:
        for letra in nombre:
            if letra in vocales:
                contador_vocales += 1
    print("cantidad total de vocales en la lista:", contador_vocales)


def ejercicio3():
    numeros = [2, 5, 7, 10, 3, 8]
    factor = int(input("ingresa un factor multiplicador: "))
    nueva_lista = []
    for numero in numeros:
        nueva_lista.append(numero * factor)
    print("lista original:", numeros)
    print("nueva lista multiplicada por", factor, ":", nueva_lista)


def generar_carta():
    palos = ["corazones", "diamantes", "treboles", "picas"]
    numeros = [1,2,3,4,5,6,7,8,9,10,"j","q","k"]
    carta = [random.randint(numeros), random.randint(palos)]
    return carta

def pedir_cartas():
    mano = []
    for i in range(8):
        mano.append(generar_carta())
    print("tus cartas son:")
    for i in range(len(mano)):
        print(i, "-", mano[i])
    return mano

def descartar_cartas(mano):
    cantidad = int(input("cuantas cartas queres descartar?: "))
    for i in range(cantidad):
        indice = int(input("ingresa el numero de la carta a descartar: "))
        if indice >= 0 and indice < len(mano):
            mano[indice] = generar_carta()
        else:
            print("indice invalido")
    print("tu nueva mano es:")
    for i in range(len(mano)):
        print(i, "-", mano[i])

def ejercicio4():
    mano = []
    salir = False
    while salir == False:
        print(""" elegi
        1. pedir cartas")
        2. descartar cartas
        3. salir""")
        opcion = input("elige una opcion: ")

        if opcion == "1":
            mano = pedir_cartas()
        elif opcion == "2":
            if len(mano) == 0:
                print("primero tenes que pedir cartas")
            else:
                descartar_cartas(mano)
        elif opcion == "3":
            print("juego terminado")
            salir = True
        else:
            print("opcion invalida")


def menu():
    nombres = ["camila", "joaquin", "valentina", "santiago", "florencia",
               "mateo", "martina", "lucas", "victoria", "benjamin"]

    salir = False
    while salir == False:
        print("""elegi:
        1. ejercicio 1 (palabra mas larga)
        2. ejercicio 2 (contar vocales)
        3. ejercicio 3 (multiplicar lista por factor)
        4. ejercicio 4 (juego de cartas)
        5. salir""")

        opcion = input("eligi una opcion: ")

        if opcion == "1":
            ejercicio1(nombres)
        elif opcion == "2":
            ejercicio2(nombres)
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            print("programa finalizado")
            salir = True
        else:
            print("opcion invalida")

menu()
