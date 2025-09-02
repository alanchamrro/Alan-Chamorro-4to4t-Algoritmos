def ejercicio1():
   matriz = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]


   for fila in range(len(matriz)):
       suma_fila = sum(matriz[fila])
       print(f"Suma de la fila {fila}: {suma_fila}")




   for columna in range(len(matriz[0])):
       suma_columna = 0
       for x in range(len(matriz)):
           suma_columna += matriz[x][columna]
       print(f"suma de la columna {columna}: {suma_columna}")

def ejercicio2():

    matriz = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    print("matriz original:")
    for fila in matriz:
        print(fila)

    transpuesta = []
    for x in range(len(matriz)):
        nueva_fila = []
        for j in range(len(matriz)):
            nueva_fila.append(matriz[j][x])
        transpuesta.append(nueva_fila)

    print("matriz transpuesta:")
    for fila in transpuesta:
        print(fila)

def ejercicio3():
    matriz= [[1, 5, 3, 5],
            [8, 5, 9, 2],
            [4, 5, 6, 7]]

    numero = int(input("ingresá un numero:"))
    contador = 0
    for fila in matriz:
        for elemento in fila:
            if elemento == numero:
                contador+=1

    print(f"el {numero} aparece {contador} veces")

def ejercicio4():
    matriz = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

    print("matriz original:")
    for fila in matriz:
        print(fila)

    suma = 0
    contador = 0
    for fila in matriz:
        for elemento in fila:
            suma += elemento
            contador += 1

    promedio = suma / contador
    print(f"el promedio de los números es: {promedio}")


    nueva_matriz = []
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            if elemento < promedio:
                nueva_fila.append(promedio)
            else:
                nueva_fila.append(elemento)
        nueva_matriz.append(nueva_fila)

    print("nueva matriz (números menores al promedio reemplazados por el promedio):")
    for fila in nueva_matriz:
        print(fila)



