import random
from datetime import datetime


def jugar_ahorcado():
    palabras = ["perro", "gato", "casa", "python", "escuela",
                "teclado", "monitor", "futbol", "musica", "robot"]

    palabra = random.choice(palabras)
    adivinada = ["_"] * len(palabra)
    intentos = 7

    print(" JUEGO DEL AHORCADO")

    while intentos > 0 and "_" in adivinada:
        print(" ".join(adivinada))
        print(f"Intentos restantes: {intentos}")

        letra = input("Adiviná una letra: ")
        if letra in palabra:
            for x in range(len(palabra)):
                if palabra[x] == letra:
                    adivinada[x] = letra
        else:
            intentos -= 1

    if "_" not in adivinada:
        print(f"¡Ganaste! La palabra era: {palabra}")
    else:
        print(f"Perdiste. La palabra era: {palabra}")


    guardar_palabra_jugada(palabra)


def guardar_palabra_jugada(palabra):

    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("palabras_jugadas.txt", "a", encoding="utf-8") as f:
        f.write(f"{ahora} - {palabra}")

    print(f"(Palabra '{palabra}' guardada en palabras_jugadas.txt)")




numero_contacto = []
nombre_contacto = []

def guardar_contactos():

    with open("contactos.txt", "w", encoding="utf-8") as f:
        for nombre, numero in zip(nombre_contacto, numero_contacto):
            nombre_limpio = nombre.replace(",", " ")
            numero_limpio = numero.replace(",", " ")
            f.write(f"{nombre_limpio}, {numero_limpio}")
    print("Contactos guardados en contactos.txt")


def menu_contactos():
    while True:
        try:
            opcion = int(input("""
 MENÚ DE CONTACTOS
1- Agregar contacto
2- Buscar contacto por nombre
3- Mostrar todos los contactos
4- Salir (y guardar archivo)
Elegí una opción: """))
        except:
            print("Ingresá una opción válida.")
            continue

        if opcion == 1:
            numero = input("Número de contacto: ")
            nombre = input("Nombre del contacto: ")

            numero_contacto.append(numero)
            nombre_contacto.append(nombre)

            print("Contacto agregado correctamente.")

        elif opcion == 2:
            buscar = input("Ingresá el nombre: ")
            if buscar in nombre_contacto:
                i = nombre_contacto.index(buscar)
                print(f"{nombre_contacto[i]}: {numero_contacto[i]}")
            else:
                print("Contacto no encontrado.")

        elif opcion == 3:
            print(" Lista de contactos ")
            if len(nombre_contacto) == 0:
                print("No tenés contactos guardados.")
            else:
                for i in range(len(nombre_contacto)):
                    print(f"{nombre_contacto[i]}: {numero_contacto[i]}")

        elif opcion == 4:
            guardar_contactos()
            print("Saliste del menú de contactos.")
            break

        else:
            print("Opción inválida.")


while True:
    print("""
========= PROGRAMA PRINCIPAL =========
1 - Jugar Ahorcado (TP2)
2 - Menú Contactos (TP3)
3 - Salir
""")
    op = input("Elegí una opción: ")

    if op == "1":
        jugar_ahorcado()

    elif op == "2":
        menu_contactos()

    elif op == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")
