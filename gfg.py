def ejercicio1():
    matriz = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    esquina1 = matriz[0][0]
    esquina2 = matriz[0][3]
    esquina3 = matriz[3][0]
    esquina4 = matriz[3][3]

    suma = esquina1 + esquina2 + esquina3 + esquina4

    print("la suma de las esquinas es:", suma)

def ejercicio2():
    matriz = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]


    suma_principal = matriz[0][0] + matriz[1][1] + matriz[2][2]


    suma_secundaria = matriz[0][2] + matriz[1][1] + matriz[2][0]

    print("suma diagonal principal:", suma_principal)
    print("suma diagonal secundaria:", suma_secundaria)


def ejercicio3():
    n = int(input("ingresá el tamaño de la matriz identidad: "))

    matriz = []

    for i in range(n):
        fila = []
        for x in range(n):
            if i == x:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)


    for fila in matriz:
        print(fila)
