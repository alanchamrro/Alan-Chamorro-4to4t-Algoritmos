def crear_tablero():
    return [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]

def mostrar_tablero(tablero):
    print(tablero[0][0], "|", tablero[0][1], "|", tablero[0][2])
    print("---------")
    print(tablero[1][0], "|", tablero[1][1], "|", tablero[1][2])
    print("---------")
    print(tablero[2][0], "|", tablero[2][1], "|", tablero[2][2])

def hay_ganador(tablero, jugador):

    if tablero[0][0] == jugador and tablero[0][1] == jugador and tablero[0][2] == jugador:
        return True
    if tablero[1][0] == jugador and tablero[1][1] == jugador and tablero[1][2] == jugador:
        return True
    if tablero[2][0] == jugador and tablero[2][1] == jugador and tablero[2][2] == jugador:
        return True
    # columnas
    if tablero[0][0] == jugador and tablero[1][0] == jugador and tablero[2][0] == jugador:
        return True
    if tablero[0][1] == jugador and tablero[1][1] == jugador and tablero[2][1] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][2] == jugador and tablero[2][2] == jugador:
        return True
    # diagonales
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True
    return False

def tablero_lleno(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                return False
    return True

def juego():
    tablero = crear_tablero()
    jugador = "X"
    while True:
        mostrar_tablero(tablero)
        print("turno del jugador", jugador)
        fila = int(input("elegí fila (0-2): "))
        col = int(input("elegí columna (0-2): "))

        if tablero[fila][col] == " ":
            tablero[fila][col] = jugador
        else:
            print("casilla ocupada, elegí otra")
            continue

        if hay_ganador(tablero, jugador):
            mostrar_tablero(tablero)
            print("ganó el jugador", jugador)
            break

        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("empate")
            break

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"


juego()
