def ejercicio1():
    matriz = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    for fila in matriz:
        print(fila)

def ejercicio2():
    matriz = [[10, 20, 30],
             [40, 50, 60],
             [70, 80, 90]]
    suma = 0

    for fila in matriz:
        for num in fila:
            suma+= num
    print(f"la suma de todos los numeros es:{suma}")

def ejercicio3():

    matriz = [["mati trabaja dale", "los hotspotsitos", "brunini", "xd"],
              ["nose", 4, "q", 1],
              [10, 3432, "no", "claro"],
              ["no quiero", "si quiero", "jasja", "papu"]]


    fila = int(input("ingresa el índice de la fila (0-3): "))
    columna = int(input("ingresa el índice de la columna (0-3): "))
    print("el elemento en ese índice es:", matriz[fila][columna])

def ejercicio4():
        matriz = [
            [10, 20, 30, 15],
            [40, 50, 60, 25],
            [70, 80, 90, 35],
            [100, 110, 120, 140]]


        maximo = matriz[0][0]


        for fila in matriz:
            for num in fila:
                if num > maximo:
                    maximo = num


        print("el número más grande de la matriz es:", maximo)

ejercicio4()







