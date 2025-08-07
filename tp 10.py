def ejercicio1():
    Numero1 = int(input("ingresa un numero"))
    Numero2 = int(input("ingresa otro numero"))
    try:
        division = Numero1/Numero2
        print("el resultado es", division)
    except ZeroDivisionError:
        print("Error no se puede dividir por 0")

def ejercicio2():
    while True:
        try:
            edad = int(input("ponetu edad: "))
            print(f"tu edad es:",edad)
            return
        except ValueError:
            print("Eso no es un número válido, intenta de nuevo.")

def ejercicio3():
    nombres = ["ana", "pedro", "sofía"]

    try:
        indice = int(input("Ingresa un número como índice (0 a 2): "))
        print("el nombre en ese índice es:", nombres[indice])
    except IndexError:
        print("Error: el índice está fuera del rango de la lista.")
    except ValueError:
        print("Error: tenés que ingresar un número entero.")

def ejercicio3():
    num1 = int(input("ingresa el primer número: "))
    num2 = int(input("ingresa el segundo número: "))
    try:

        suma = num1 + num2
        print("la suma es:", suma)
    except ValueError:
        print("error: uno o ambos valores ingresados no son números enteros.")

def ejercicio4():
    Numero1 = int(input("ingresa un numero"))
    Numero2 = int(input("ingresa otro numero"))
    try:
        division = Numero1 / Numero2
        print("el resultado es", division)
    except ZeroDivisionError:
        print("error no se puede dividir por 0")
    finally:
        print("fin del programa de calculo")
ejercicio4()

