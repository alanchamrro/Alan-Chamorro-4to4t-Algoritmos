def ejercicio1 ():

    num = int(input("dame 1 numero:"))
    num2 = int(input("dame 2 numero:"))
    num3 = int(input("dame 3 numero:"))
    num4 = int(input("dame 4 numero:"))
    num5 = int(input("dame 5 numero:"))

    almacenar = []
    almacenar.append(num)
    almacenar.append(num2)
    almacenar.append(num3)
    almacenar.append(num4)
    almacenar.append(num5)


    for x in almacenar:
        print(x)

def ejercicio2():

    frutas = ["mandarina","banana","naranja","manzana"]
    nombre_fruta = input("dame el nombre de una fruta:").lower()

    if nombre_fruta in frutas:
        indice = frutas.index(nombre_fruta)
        print(f"la fruta {nombre_fruta}   está en el indice {indice}")
    else:
        print(f"la fruta '{nombre_fruta}' no fue encontrada en la lista")

def ejercicio3():

    notas = [3,5,7,6,8,1,4,4,2,10]
    suma = sum(notas)
    promedio = suma / len(notas)

    print(f"las notas son : {notas}")
    print(f"la suma de las notas en total sería: {suma}")
    print(f"el promedio de las notas es: {promedio}")

def ejercicio4():

    temperaturas = [18, 22, 19, 25, 17, 30, 28, 20]

    max_temp = temperaturas[0]
    min_temp = temperaturas[0]

    for temp in temperaturas:
        if temp > max_temp:
            max_temp = temp
        if temp < min_temp:
            min_temp = temp

    print(f"temperatura máxima registrada: {max_temp}")
    print(f"temperatura mínima registrada: {min_temp}")

def ejercicio5():
    numeros = [8, 3, 1, 7, 4, 2, 9, 6, 5]
    numeros.sort()
    print("lista ordenada de forma ascendente:", numeros)

def ejercicio6():
    numeros = [8, 3, 1, 7, 4, 2, 9, 6, 5]

    for i in range(len(numeros) - 1):
        for x in range(len(numeros) - 1 - i):
            if numeros[x] > numeros[x + 1]:
                numeros[x], numeros[x + 1] = numeros[x + 1], numeros[x]

    print("lista ordenada de forma ascendente:", numeros)



