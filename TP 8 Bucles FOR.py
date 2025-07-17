def ejercicio1():
    acumulador = 0
    numeros = [10, 20, 30, 40, 50]
    for x in range(0, len(numeros)):
        acumulador = acumulador + numeros[x]
    print(acumulador)
    return acumulador

def ejercicio2():
    contador_vocales = 0
    vocales = "aeiouAEIOU"
    texto = "hola travieso"
    for vocal in texto:
            if vocal in vocales:
                contador_vocales += 1
    print("hay",contador_vocales,"vocales en el texto")
    return contador_vocales

def ejercicio3():
   numero = 0
   opc = int(input("Ingrese un Número:"))
   for x in range(1 , 10+1):
       numero = opc * x
       print(numero)
   return numero
def ejercicio4():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = []
    for x in range(1, len(numeros)+1):
        if (x % 2) == 0:
            pares.append(x)
    print(pares)
    return pares

def ejercicio5():
    numero_filas = int(input("Ingrese un Número para las filas:"))
    for filas in range(1, numero_filas + 1):
        for x in range(1, filas + 1):
            print("*",end="")
        print(" ")

def menu():
    opc = int(input("""Elegí uno de los ejercicios travieso 
        1. Lista de números 2. Cadena de Texto
        3. User Número entero 4. Números pares
        5. Patrón de asteriscos anidados
        elección: """))
    while opc != 0:
        if opc == 1:
            ejercicio1()
            break
        elif opc == 2:
            ejercicio2()
            break
        elif opc == 3:
            ejercicio3()
            break
        elif opc == 4:
            ejercicio4()
            break
        elif opc == 5:
            ejercicio5()
            break
menu()