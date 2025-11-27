import random


def crear_tablero():
    tablero = []
    i = 0
    while i < 10:
        fila = []
        j = 0
        while j < 10:
            fila.append("·")
            j += 1
        tablero.append(fila)
        i += 1
    return tablero



def colocar_tesoros():
    tesoros = []
    while len(tesoros) < 3:
        f = random.randint(0, 9)
        c = random.randint(0, 9)

        repetido = False
        i = 0
        while i < len(tesoros):
            if tesoros[i][0] == f and tesoros[i][1] == c:
                repetido = True
            i += 1

        if repetido == False:
            tesoros.append([f, c])

    return tesoros



def mostrar_tablero(tablero):
    i = 0
    while i < 10:
        j = 0
        linea = ""
        while j < 10:
            linea = linea + tablero[i][j] + " "
            j += 1
        print(linea)
        i += 1
    print()


def jugar():
    tablero = crear_tablero()
    tesoros = colocar_tesoros()

    intentos = 5
    encontrados = 0

    print("BUSCADOR DE TESOROS ")
    print("Tenés 5 intentos. Si encontrás un tesoro, se reinician a 5.")

    while intentos > 0 and encontrados < 3:

        mostrar_tablero(tablero)

        print("Intentos:", intentos)
        print("Tesoros encontrados:", encontrados)
        print()

        try:
            fila = int(input("Elegí fila (0-9): "))
            col = int(input("Elegí columna (0-9): "))
        except:
            print("Debés escribir un número.")
            continue

        if fila < 0 or fila > 9 or col < 0 or col > 9:
            print("Coordenadas fuera de rango.")
            continue


        hay_tesoro = False
        i = 0
        while i < len(tesoros):
            if tesoros[i][0] == fila and tesoros[i][1] == col:
                hay_tesoro = True
            i += 1

        if hay_tesoro:
            print("¡Encontraste un tesoro!")
            tablero[fila][col] = "T"
            encontrados += 1
            intentos = 5
        else:
            print("Nada acá.")
            tablero[fila][col] = "X"
            intentos -= 1

    print("FIN DEL JUEGO ")
    if encontrados == 3:
        print("¡Ganaste! Encontraste los 3 tesoros.")
    else:
        print("Perdiste. Te quedaste sin intentos.")

    print("TABLERO FINAL:")
    mostrar_tablero(tablero)



jugar()
