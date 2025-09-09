
def mazo_hacer():
    palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    numeros = [1 ,2, 3, 4, 5, 6, 7, 8,9 ,10 , 11, 12, 13]


    mazo= []

    for palo in palos:
        for numero in numeros:
            if numero == 1:
                carta = "A"
            elif numero == 11:
                carta = "J"
            elif numero == 12:
                carta = "Q"
            elif numero == 13:
                carta = "K"
            else:
                carta=numero
            mazo.append([carta, palo])

    return mazo

def calcular_chips(mazo):
    total = 0
    for carta in mazo:
        if carta == "A":
            total+=11
        elif carta in ["J", "Q", "K"]:
            total+=10


    return total

mazo= mazo_hacer()

for fila in mazo:
    print(fila)

chips_totales = calcular_chips(mazo)

print(f"el valor total de los chips del mazo es: {chips_totales}")




















